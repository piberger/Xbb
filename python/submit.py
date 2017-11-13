#! /usr/bin/env python
from optparse import OptionParser
import sys
import time
import os
import shutil
import subprocess
import signal
import ROOT
ROOT.gROOT.SetBatch(True)
from myutils.sampleTree import SampleTree as SampleTree
from myutils.FileList import FileList
from myutils.Datacard import Datacard
from myutils import BetterConfigParser, ParseInfo
from myutils.copytreePSI import filelist
from myutils.FileLocator import FileLocator

parser = OptionParser()
parser.add_option("-T", "--tag", dest="tag", default="8TeV",
                      help="Tag to run the analysis with, example '8TeV' uses config8TeV and pathConfig8TeV to run the analysis")
parser.add_option("-J", "--task", dest="task", default="",
                      help="Task to be done, i.e. 'dc' for Datacards, 'prep' for preparation of Trees, 'plot' to produce plots or 'eval' to write the MVA output or 'sys' to write regression and systematics (or 'syseval' for both). ")
parser.add_option("-S","--samples",dest="samples",default="", help="samples you want to run on")
parser.add_option("-F", "--folderTag", dest="ftag", default="",
                      help="Creats a new folder structure for outputs or uses an existing one with the given name")
parser.add_option("-N", "--number-of-events-or-files", dest="nevents_split_nfiles_single", default=-1,
                      help="Number of events per file when splitting or number of files when using single file workflow.")
parser.add_option("-V", "--verbose", dest="verbose", action="store_true", default=False,
                      help="Activate verbose flag for debug printouts")
parser.add_option("-L", "--local", dest="override_to_run_locally", action="store_true", default=False,
                      help="Override run_locally option to run locally")
parser.add_option("-B", "--batch", dest="override_to_run_in_batch", action="store_true", default=False,
                      help="Override run_locally option to run in batch")
parser.add_option("-i", "--interactive", dest="interactive", action="store_true", default=False, help="Interactive mode")
parser.add_option("-f", "--force", dest="force", action="store_true", default=False,
                      help="Force overwriting of files if they already exist")
parser.add_option("-l", "--limit", dest="limit", default=None, help="max number of files to process per sample")

(opts, args) = parser.parse_args(sys.argv)


debugPrintOUts = opts.verbose

if opts.tag == "":
    print "Please provide tag to run the analysis with, example '-T 8TeV' uses config8TeV and pathConfig8TeV to run the analysis."
    sys.exit(123)

if opts.task == "":
    print "Please provide a task.\n-J prep:\tpreparation of Trees\n-J sys:\t\twrite regression and systematics\n-J eval:\tcreate MVA output\n-J plot:\tproduce Plots\n-J dc:\t\twrite workspaces and datacards"
    sys.exit(123)

globalFilesSubmitted = 0
globalFilesSkipped = 0

def signal_handler(signal, frame):
    if (globalFilesSubmitted > 0 or globalFilesSkipped > 0):
        print('\n----------------------------\n')
        print('Files submitted:'+str(globalFilesSubmitted))
        print('Files skipped:'+str(globalFilesSkipped))
    print('You pressed Ctrl+C!')
    print('\n----------------------------\n')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

en = opts.tag

#create the list with the samples to run over
samplesList=opts.samples.split(",")
timestamp = time.strftime("%Y_%m_%d-%H_%M_%S")

if(debugPrintOUts): print 'samplesList',samplesList
if(debugPrintOUts): print 'timestamp',timestamp

# the list of the config is taken from the path config
pathconfig = BetterConfigParser()
pathconfig.read('%sconfig/paths.ini'%(en))
_configs = pathconfig.get('Configuration','List').split(" ")
configs = [ '%sconfig/'%(en) + c for c in _configs  ]

if(debugPrintOUts): print 'configs',configs
if(debugPrintOUts): print 'opts.ftag',opts.ftag

# TODO: clean up
if not opts.ftag == '':
    tagDir = pathconfig.get('Directories','tagDir')
    if(debugPrintOUts): print 'tagDir',tagDir
    DirStruct={
        'tagDir': tagDir,
        'ftagdir': '%s/%s/'%(tagDir, opts.ftag),
        'logpath':'%s/%s/%s/'%(tagDir, opts.ftag, 'Logs'),
        'plotpath':'%s/%s/%s/'%(tagDir, opts.ftag, 'Plots'),
        'limitpath':'%s/%s/%s/'%(tagDir, opts.ftag, 'Limits'),
        'confpath':'%s/%s/%s/'%(tagDir, opts.ftag, 'config')
    }

    if(debugPrintOUts): print 'DirStruct',DirStruct

    for keys in ['tagDir', 'ftagdir', 'logpath', 'plotpath', 'limitpath', 'confpath']:
        try:
            os.stat(DirStruct[keys])
        except:
            os.mkdir(DirStruct[keys])

    pathfile = open('%sconfig/paths.ini'%(en))
    buffer = pathfile.readlines()
    pathfile.close()
    os.rename('%sconfig/paths.ini'%(en),'%sconfig/paths.ini.bkp'%(en))
    pathfile = open('%sconfig/paths.ini'%(en),'w')
    for line in buffer:
        if line.startswith('plotpath'):
            line = 'plotpath: %s\n'%DirStruct['plotpath']
        elif line.startswith('logpath'):
            line = 'logpath: %s\n'%DirStruct['logpath']
        elif line.startswith('limits'):
            line = 'limits: %s\n'%DirStruct['limitpath']
        pathfile.write(line)
    pathfile.close()

    #copy config files
    for item in configs:
        shutil.copyfile(item,'%s/%s/%s'%(tagDir,opts.ftag,item.replace(en, '')))

if(debugPrintOUts): print configs
config = BetterConfigParser()
config.read(configs)

# RETRIEVE RELEVANT VARIABLES FROM CONFIG FILES AND FROM COMMAND LINE OPTIONS
# TODO: clean up
counter = 0
logPath = config.get('Directories', 'logpath')
samplesinfo = config.get('Directories', 'samplesinfo')
whereToLaunch = config.get('Configuration', 'whereToLaunch')
run_locally = str(config.get('Configuration', 'run_locally'))

if opts.override_to_run_locally and opts.override_to_run_in_batch:
    print 'both override_to_run_locally and override_to_run_in_batch ativated, using str(config.get("Configuration","run_locally")) instead'
elif opts.override_to_run_locally:
    run_locally = 'True'
    print 'using override_to_run_locally to override str(config.get("Configuration","run_locally"))'
elif opts.override_to_run_in_batch:
    run_locally = 'False'
    print 'using override_to_run_in_batch to override str(config.get("Configuration","run_locally"))'

print 'whereToLaunch', whereToLaunch
print 'run_locally', run_locally

# CREATE DIRECTORIES
fileLocator = FileLocator(config=config)
if 'PSI' in whereToLaunch:
    for dirName in ['PREPout', 'SYSout', 'MVAout', 'tmpSamples']:
        if not fileLocator.exists(config.get('Directories', dirName)):
            fileLocator.makedirs(config.get('Directories', dirName))

def dump_config(configs,output_file):
    """
    Dump all the configs in a output file
    Args:
        output_file: the file where the log will be dumped
        configs: list of files (string) to be dumped
    Returns:
        nothing
    """
    outf = open(output_file,'w')
    for i in configs:
        try:
            f=open(i,'r')
            outf.write(f.read())
        except: print '@WARNING: Config' + i + ' not found. It will not be used.'

#check if the logPath exist. If not exit
if( not os.path.isdir(logPath) ):
    print '@ERROR : ' + logPath + ': dir not found.'
    print '@ERROR : Create it before submitting '
    print 'Exit'
    sys.exit(-1)

# CREATE DICTIONARY TO BE USED AT JOB SUBMISSION TIME
repDict = {
    'en': en,
    'logpath': logPath,
    'job': '',
    'task': opts.task,
    'queue': 'all.q',
    'timestamp': timestamp,
    'additional': '',
    'job_id': 'noid',
    'nprocesses': str(max(int(pathconfig.get('Configuration', 'nprocesses')), 1))
}

list_submitted_singlejobs = {}

# ------------------------------------------------------------------------------
# SUBMIT SCRIPT options defined here, TODO: move to config
# ------------------------------------------------------------------------------
submitScriptTemplate = 'qsub {options} -o {logfile} {runscript}'
submitScriptOptionsTemplate = '-V -cwd -q %(queue)s -N %(name)s -j y -pe smp %(nprocesses)s'
submitScriptSpecialOptions = {
        'mergesyscachingdcsplit': ' -l h_vmem=6g ',
        'singleeval': ' -l h_vmem=6g ',
        #'cacheplot': ' -l h_vmem=6g ',
        #'cachetraining': ' -l h_vmem=6g ',
        }

# STANDARD WORKFLOW SUBMISSION FUNCTION
def submit(job, repDict):
    global counter
    repDict['job'] = job
    counter += 1
    repDict['name'] = '%(job)s_%(en)s%(task)s' %repDict

    # run script
    runScript = 'runAll.sh %(job)s %(en)s '%(repDict)
    runScript += opts.task + ' ' + repDict['nprocesses']+ ' ' + repDict['job_id'] + ' ' + repDict['additional']

    # add named arguments to run script
    if 'arguments' in repDict:
        for argument, value in repDict['arguments'].iteritems():
            runScript += (' --{argument}={value} '.format(argument=argument, value=value)) if len('{value}'.format(value=value)) > 0 else ' --{argument} '.format(argument=argument)

    # log=batch system log, out=stdout of process
    logOutputPath = '%(logpath)s/%(task)s_%(timestamp)s_%(job)s_%(en)s_%(additional)s.log' %(repDict)
    errorOutputPath = '%(logpath)s/%(task)s_%(timestamp)s_%(job)s_%(en)s_%(additional)s.err' %(repDict)
    outOutputPath = '%(logpath)s/%(task)s_%(timestamp)s_%(job)s_%(en)s_%(additional)s.out' %(repDict)

    # -----------------------------------------------------------------------------
    # CONDOR
    # -----------------------------------------------------------------------------
    if 'condor' in whereToLaunch:
        with open('batch/condor/template.sub', 'r') as template:
            lines = template.readlines()
        dictHash = '%(task)s_%(timestamp)s'%(repDict) + '_%x'%hash('%r'%repDict)
        condorDict = {
            'runscript': runScript.split(' ')[0],
            'arguments': ' '.join(runScript.split(' ')[1:]),
            'output': outOutputPath,
            'log': logOutputPath,
            'error': errorOutputPath,
            'queue': 'workday',
        }
        submitFileName = 'condor_{hash}.sub'.format(hash=dictHash)
        with open(submitFileName, 'w') as submitFile:
            for line in lines:
                submitFile.write(line.format(**condorDict))
        print "COMMAND:\x1b[35m", runScript, "\x1b[0m"
        command = 'condor_submit {submitFileName}'.format(submitFileName=submitFileName)

    # -----------------------------------------------------------------------------
    # SGE
    # -----------------------------------------------------------------------------
    else:
        qsubOptions = submitScriptOptionsTemplate%(repDict) 

        if opts.task in submitScriptSpecialOptions: 
            qsubOptions += submitScriptSpecialOptions[opts.task]

        command = submitScriptTemplate.format(options=qsubOptions, logfile=outOutputPath, runscript=runScript)
        dump_config(configs, "%(logpath)s/%(timestamp)s_%(job)s_%(en)s_%(task)s.config" %(repDict))

    # run command
    if opts.interactive:
        print "SUBMIT:\x1b[34m", command, "\x1b[0m\n(press ENTER to run it and continue)"
        answer = raw_input().strip()
        if answer.lower() in ['no', 'n', 'skip']:
            return
        elif answer.lower() in ['l', 'local']:
            print "run locally"
            command = 'sh {runscript}'.format(runscript=runScript)
    else:
        print "the command is ", command
    subprocess.call([command], shell=True)

# -----------------------------------------------------------------------------
# PREP: copy skimmed ntuples to local storage
# -----------------------------------------------------------------------------
if opts.task == 'prep':

    path = config.get("Directories", "PREPin")
    samplefiles = config.get('Directories','samplefiles')
    info = ParseInfo(samplesinfo, path)
    sampleIdentifiers = info.getSampleIdentifiers() 
    if samplesList and len(samplesList) > 0:
        sampleIdentifiers = [x for x in sampleIdentifiers if x in samplesList]
    
    chunkSize = 10 if int(opts.nevents_split_nfiles_single) < 1 else int(opts.nevents_split_nfiles_single)

    # process all sample identifiers (correspond to folders with ROOT files)
    for sampleIdentifier in sampleIdentifiers:
        sampleFileList = filelist(samplefiles, sampleIdentifier)
        if opts.limit and len(sampleFileList) > int(opts.limit):
            sampleFileList = sampleFileList[0:int(opts.limit)]
        splitFilesChunks = [sampleFileList[i:i+chunkSize] for i in range(0, len(sampleFileList), chunkSize)]

        # submit a job for a chunk of N files
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks):
            jobDict = repDict.copy()
            jobDict.update({'arguments':{
                    'sampleIdentifier': sampleIdentifier,
                    'fileList': FileList.compress(splitFilesChunk),
                }})
            jobName = 'prep_{sample}_part{part}'.format(sample=sampleIdentifier, part=chunkNumber)
            submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# CACHETRAINING: prepare skimmed trees including the training/eval cuts 
# -----------------------------------------------------------------------------
if opts.task.startswith('cachetraining'):
    trainingRegions = [x.strip() for x in (config.get('MVALists','List_for_submitscript')).split(',')]
    allBackgrounds = list(set(sum([eval(config.get(trainingRegion, 'backgrounds')) for trainingRegion in trainingRegions], [])))
    allSignals = list(set(sum([eval(config.get(trainingRegion, 'signals')) for trainingRegion in trainingRegions], [])))
    print "backgrounds:"
    for sampleName in sorted(allBackgrounds):
        print " >", sampleName
    print "signals:"
    for sampleName in sorted(allSignals):
        print " >", sampleName
    
    # get samples info
    info = ParseInfo(samplesinfo, config.get('Directories', 'MVAin'))
    samples = info.get_samples(allBackgrounds + allSignals)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    samplesToCache = [x.strip() for x in opts.samples.strip().split(',') if len(x.strip()) > 0]
    sampleIdentifiers = sorted(list(set([sample.identifier for sample in samples if sample.identifier in samplesToCache or len(samplesToCache) < 1])))
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
    
    # submit separate jobs for all samples
    for sampleIdentifier in sampleIdentifiers:

        # number of files to process per job 
        splitFilesChunkSize = min([sample.mergeCachingSize for sample in samples if sample.identifier==sampleIdentifier])
        splitFilesChunks = SampleTree({'name': sampleIdentifier, 'folder': config.get('Directories', 'MVAin')}, countOnly=True, splitFilesChunkSize=splitFilesChunkSize, config=config).getSampleFileNameChunks()
        print "DEBUG: split after ", splitFilesChunkSize, " files => number of parts = ", len(splitFilesChunks)
        
        # submit all the single chunks for one sample
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks, start=1):
            jobDict = repDict.copy()
            jobDict.update({
                'queue': 'short.q',
                'arguments':
                    {
                        'trainingRegions': ','.join(trainingRegions),
                        'sampleIdentifier': sampleIdentifier,
                        'chunkNumber': chunkNumber,
                        'splitFilesChunks': len(splitFilesChunks),
                        'splitFilesChunkSize': splitFilesChunkSize,
                    }
                })
            if opts.force:
                jobDict['arguments']['force'] = ''
            # pass file list, if only a chunk of it is processed
            if len(splitFilesChunks) > 1:
                compressedFileList = FileList.compress(splitFilesChunk)
                jobDict['arguments']['fileList'] = compressedFileList
            jobName = 'training_cache_{sample}_part{part}'.format(sample=sampleIdentifier, part=chunkNumber)
            submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# RUNTRAINING: train mva, outputs .xml file. Needs cachetraining before. 
# -----------------------------------------------------------------------------
if opts.task.startswith('runtraining'):
    # training regions
    trainingRegions = [x.strip() for x in (config.get('MVALists', 'List_for_submitscript')).split(',')]

    # separate job for all training regions
    for trainingRegion in trainingRegions:
        jobDict = repDict.copy()
        jobDict.update({'arguments': {'trainingRegions': trainingRegion}})
        jobName = 'training_run_{trainingRegions}'.format(trainingRegions=trainingRegion)
        submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# CACHEPLOT: prepare skimmed trees with cuts for the CR/SR 
# -----------------------------------------------------------------------------
if opts.task.startswith('cacheplot'):
    regions = [x.strip() for x in (config.get('Plot_general', 'List')).split(',')]
    sampleNames = eval(config.get('Plot_general', 'samples')) 
    dataSampleNames = eval(config.get('Plot_general', 'Data')) 

    # get samples info
    info = ParseInfo(samplesinfo, config.get('Directories', 'plottingSamples'))
    samples = info.get_samples(sampleNames + dataSampleNames)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    samplesToCache = [x.strip() for x in opts.samples.strip().split(',') if len(x.strip()) > 0]
    sampleIdentifiers = sorted(list(set([sample.identifier for sample in samples if sample.identifier in samplesToCache or len(samplesToCache) < 1])))
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
    
    # submit jobs, 1 to n separate jobs per sample
    for sampleIdentifier in sampleIdentifiers:

        # number of files to process per job 
        splitFilesChunkSize = min([sample.mergeCachingSize for sample in samples if sample.identifier == sampleIdentifier])
        splitFilesChunks = SampleTree({'name': sampleIdentifier, 'folder': config.get('Directories', 'plottingSamples')}, countOnly=True, splitFilesChunkSize=splitFilesChunkSize, config=config).getSampleFileNameChunks()
        print "DEBUG: split after ", splitFilesChunkSize, " files => number of parts = ", len(splitFilesChunks)
        
        # submit all the single parts
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks, start=1):
            compressedFileList = FileList.compress(splitFilesChunk)
            jobDict = repDict.copy()
            jobDict.update({
                    'queue': 'short.q',
                    'arguments':
                        {
                        'regions': ','.join(regions),
                        'sampleIdentifier': sampleIdentifier,
                        'chunkNumber': chunkNumber,
                        'splitFilesChunks': len(splitFilesChunks),
                        'splitFilesChunkSize': splitFilesChunkSize,
                        }
                    })
            if opts.force:
                jobDict['arguments']['force'] = ''
            # pass file list, if only a chunk of it is processed
            if len(splitFilesChunks) > 1:
                jobDict['arguments']['fileList'] = compressedFileList
            jobName = 'plot_cache_{sample}_part{chunk}'.format(sample=sampleIdentifier, chunk=chunkNumber)
            submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# RUNPLOT: make CR/SR plots. Needs cacheplot before. 
# -----------------------------------------------------------------------------
if opts.task.startswith('runplot'):
    regions = [x.strip() for x in (config.get('Plot_general', 'List')).split(',')]

    # submit all the plot regions as separate jobs
    for region in regions:
        jobDict = repDict.copy()
        jobDict.update({
            'arguments':
                {
                    'regions': region,
                }
            })
        jobName = 'plot_run_{region}'.format(region=region)
        submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# CACHEDC: prepare skimmed trees for DC, which have looser cuts to include 
# variations of systematics. 
# -----------------------------------------------------------------------------
if opts.task.startswith('cachedc'):
    # get list of all sample names used in DC step
    sampleNames = []
    regions = [x.strip() for x in config.get('LimitGeneral', 'List').split(',') if len(x.strip()) > 0]
    if config.has_option('LimitGeneral', 'addSample_sys'):
        addSample_sys = eval(config.get('LimitGeneral', 'addSample_sys'))
        sampleNames += [addSample_sys[key] for key in addSample_sys]
    for region in regions:
        for sampleType in ['data', 'signal', 'background']:
            sampleNames += eval(config.get('dc:%s'%region, sampleType))

    # get samples info
    sampleFolder = config.get('Directories', 'dcSamples')
    info = ParseInfo(samplesinfo, sampleFolder)
    samples = info.get_samples(sampleNames)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    samplesToCache = [x.strip() for x in opts.samples.strip().split(',') if len(x.strip()) > 0]
    sampleIdentifiers = sorted(list(set([sample.identifier for sample in samples if sample.identifier in samplesToCache or len(samplesToCache) < 1])))
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
    
    # submit jobs, 1 to n separate jobs per sample
    for sampleIdentifier in sampleIdentifiers:

        # number of files to process per job 
        splitFilesChunkSize = min([sample.mergeCachingSize for sample in samples if sample.identifier == sampleIdentifier])
        splitFilesChunks = SampleTree({'name': sampleIdentifier, 'folder': sampleFolder}, countOnly=True, splitFilesChunkSize=splitFilesChunkSize, config=config).getSampleFileNameChunks()
        print "DEBUG: split after ", splitFilesChunkSize, " files => number of parts = ", len(splitFilesChunks)
        
        # submit all the single parts
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks, start=1):
            compressedFileList = FileList.compress(splitFilesChunk)
            jobDict = repDict.copy()
            jobDict.update({
                'arguments':
                    {
                        'sampleIdentifier': sampleIdentifier,
                        'chunkNumber': chunkNumber,
                        'splitFilesChunks': len(splitFilesChunks),
                        'splitFilesChunkSize': splitFilesChunkSize,
                    }
                })
            # pass file list, if only a chunk of it is processed
            if len(splitFilesChunks) > 1:
                jobDict['arguments']['fileList'] = compressedFileList
            jobName = 'dc_cache_{sample}_part{chunk}'.format(sample=sampleIdentifier, chunk=chunkNumber)
            submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# RUNDC: produce DC .txt and .root files. Needs cachedc before. 
# -----------------------------------------------------------------------------
if opts.task.startswith('rundc'):
    
    regions = Datacard.getRegions(config=config)
    samples = Datacard.getSamples(config=config, regions=regions)

    sampleIdentifiers = sorted(list(set([sample.identifier for sample in samples])))

    # only process given samples (if option is present)
    samplesToCache = [x.strip() for x in opts.samples.strip().split(',') if len(x.strip()) > 0]
    if len(samplesToCache) > 0:
        sampleIdentifiers = [x for x in sampleIdentifiers if x in samplesToCache]

    # submit all the DC regions as separate jobs
    for region in regions:
        # submit separate jobs for either sampleIdentifiers
        for sampleIdentifier in sampleIdentifiers: 
            jobDict = repDict.copy()
            jobDict.update({
                'queue': 'short.q',
                'arguments':
                    {
                        'regions': region,
                        'sampleIdentifier': sampleIdentifier,
                    }
                })
            jobName = 'dc_run_' + '_'.join([v for k,v in jobDict['arguments'].iteritems()])
            submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# MERGEDC: merge DC .root files for all samples per region and produce combined
# .root and .txt files. Needs rundc before. 
# -----------------------------------------------------------------------------
if opts.task.startswith('mergedc'):
    regions = Datacard.getRegions(config=config)

    # submit all the DC regions as separate jobs
    for region in regions:
        jobDict = repDict.copy()
        jobDict.update({
            'queue': 'short.q',
            'arguments':
                {
                    'regions': region,
                }
            })
        jobName = 'dc_merge_' + '_'.join([v for k,v in jobDict['arguments'].iteritems()])
        submit(jobName, jobDict)

if opts.task == 'trainReg':
    repDict['queue'] = 'all.q'
    submit('trainReg',repDict)

# ADD SYSTEMATIC UNCERTAINTIES AND ADDITIONAL HIGHER LEVEL VARIABLES TO THE TREES
if opts.task == 'sys' or opts.task == 'syseval':
    path = config.get("Directories","SYSin")
    info = ParseInfo(samplesinfo,path)
    if opts.samples == "":
        for job in info:
            if (job.subsample):
                continue # avoid multiple submissions form subsamples
            # TO FIX FOR SPLITTED SAMPLE
            submit(job.name,repDict)
    else:
        for sample in samplesList:
            submit(sample,repDict)


# EVALUATION OF EVENT BY EVENT BDT SCORE
if opts.task == 'eval':
    repDict['queue'] = 'long.q'
    path = config.get("Directories","MVAin")
    info = ParseInfo(samplesinfo,path)
    if opts.samples == "":
        for job in info:
            if (job.subsample):
                continue # avoid multiple submissions from subsamples
            if(info.checkSplittedSampleName(job.identifier)): # if multiple entries for one name  (splitted samples) use the identifier to submit
                print '@INFO: Splitted samples: submit through identifier'
                submit(job.identifier,repDict)
            else: submit(job.name,repDict)
    else:
        for sample in samplesList:
            print sample
            submit(sample,repDict)
