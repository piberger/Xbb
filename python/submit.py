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
import fnmatch
import hashlib
import json
import math
import datetime
from myutils.sampleTree import SampleTree as SampleTree
from myutils.FileList import FileList
from myutils.Datacard import Datacard
from myutils import BetterConfigParser, ParseInfo
from myutils.copytreePSI import filelist
from myutils.FileLocator import FileLocator
from myutils.BatchSystem import *
from myutils.BranchList import BranchList

try:
    if sys.version_info[0] == 2 and sys.version_info[1] < 7:
        print "\x1b[31mWARNING: unsupported Python version! Python 2.7+ is needed!\x1b[0m"
except:
    print "unable to detect python version!"

parser = OptionParser()
parser.add_option("-b", "--addCollections", "--modules", dest="addCollections", default=None, help="collections to add in sysnew step")
parser.add_option("-B", "--batch", dest="override_to_run_in_batch", action="store_true", default=False,
                      help="Override run_locally option to run in batch")
parser.add_option("-C", "--checkCached", dest="checkCached", action="store_true", default=False,
                      help="check if all cached trees exist before submitting the jobs")
parser.add_option("-c", "--condor-nobatch", dest="condorNobatch", action="store_true", default=False,
                      help="submit in a single submit file per job instead of using batches")
parser.add_option("-d", "--friend", dest="friend", action="store_true", default=False,
                      help="use friend trees")
parser.add_option("-F", "--folderTag", dest="ftag", default="",
                      help="Creats a new folder structure for outputs or uses an existing one with the given name")
parser.add_option("-f", "--force", dest="force", action="store_true", default=False,
                      help="Force overwriting of files if they already exist")
parser.add_option("-g", "--forceN", dest="forceN", action="store_true", default=False,
                      help="Force usage of -N parameter")
parser.add_option("-i", "--interactive", dest="interactive", action="store_true", default=False, help="Interactive mode")
parser.add_option("--input", dest="input", default=None, help="input")
parser.add_option("-j", "--join", dest="join", action="store_true", default=False, help="(experimental) chain all files per sample together in sys step")
parser.add_option("-J", "--task", dest="task", default="",
                      help="Task to be done, i.e. 'dc' for Datacards, 'prep' for preparation of Trees, 'plot' to produce plots or 'eval' to write the MVA output or 'sys' to write regression and systematics (or 'syseval' for both). ")
parser.add_option("-k", "--skipExisting", dest="skipExisting", action="store_true", default=False,
                      help="don't submit jobs if output files already exist")
parser.add_option("-L", "--local", dest="override_to_run_locally", action="store_true", default=False,
                      help="Override run_locally option to run locally")
parser.add_option("-l", "--limit", dest="limit", default=None, help="max number of files to process per sample")
parser.add_option("-N", "--number-of-events-or-files", dest="nevents_split_nfiles_single", default=-1,
                      help="Number of events per file when splitting or number of files when using single file workflow.")
parser.add_option("-o", "--output", dest="output", default=None, help="output")
parser.add_option("-p", "--parallel", dest="parallel", default=None, help="Fine control for per job task parallelization. Higher values are usually faster and reduce IO and overhead, but also consume more memory. If number of running jobs is not limited, lower values could also increase performance. (Default: maximum per job parallelization).")
parser.add_option("-q", "--queue", dest="queue", default=None, help="overwrites queue settings in config")
parser.add_option("-r", "--regions", dest="regions", default=None, help="regions to plot, can contain * as wildcard")
parser.add_option("-S","--samples",dest="samples",default="", help="samples you want to run on")
parser.add_option("--set", dest="setOptions", help="set config option. --set='Section.option:value'")
parser.add_option("-s","--folders",dest="folders",default="", help="folders to check, e.g. PREPout,SYSin")
parser.add_option("-T", "--tag", dest="tag", default="8TeV",
                      help="Tag to run the analysis with, example '8TeV' uses config8TeV and pathConfig8TeV to run the analysis")
parser.add_option("-u","--samplesInfo",dest="samplesInfo", default="", help="path to directory containing the sample .txt files with the sample lists")
parser.add_option("-U", "--resubmit", dest="resubmit", action="store_true", default=False, help="resubmit failed jobs")
parser.add_option("-V", "--verbose", dest="verbose", action="store_true", default=False,
                      help="Activate verbose flag for debug printouts")
parser.add_option("-v","--vars",dest="vars",default="", help="comma separated list of variables")
parser.add_option("-w", "--wait-for", dest="waitFor", default=None, help="wait for another job to finish")
parser.add_option("--unfinished", dest="unfinished", action="store_true", default=False, help="show only unfinished jobs")

(opts, args) = parser.parse_args(sys.argv)

submitScriptRunAllLocally = False
submitScriptSubmitAll = False
debugPrintOUts = opts.verbose
submitTimestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

if opts.tag == "":
    print "Please provide tag to run the analysis with, example '-T 8TeV' uses config8TeV and pathConfig8TeV to run the analysis."
    sys.exit(123)

if opts.task == "":
    print "Please provide a task.\n-J prep:\tpreparation of Trees\n-J sys:\t\twrite regression and systematics\n-J eval:\tcreate MVA output\n-J plot:\tproduce Plots\n-J dc:\t\twrite workspaces and datacards"
    sys.exit(123)

if opts.task == "run":
    opts.task = "sysnew"


batchSystem = None

def signal_handler(signal, frame):
    if (batchSystem and (batchSystem.nJobsSubmitted > 0 or batchSystem.nJobsSkipped > 0)):
        print('\n----------------------------\n')
        print('Files submitted:'+str(batchSystem.nJobsSubmitted))
        print('Files skipped:'+str(batchSystem.nJobsSkipped))
    print('You pressed Ctrl+C!')
    print('\n----------------------------\n')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# split list into sublists of given length
def partitionFileList(sampleFileList, chunkSize=1):
    return [sampleFileList[i:i+chunkSize] for i in range(0, len(sampleFileList), chunkSize)]

#create the list with the samples to run over
samplesList = [x.strip() for x in opts.samples.strip().split(',') if len(x.strip()) > 0]
timestamp = time.strftime("%Y_%m_%d-%H_%M_%S")

if debugPrintOUts:
    print 'samplesList', samplesList
    print 'timestamp', timestamp

# ------------------------------------------------------------------------------
# the LIST OF CONFIG FILES is taken from the path config
# ------------------------------------------------------------------------------
pathconfig = BetterConfigParser()
pathconfig.read('%sconfig/paths.ini'%(opts.tag))
try:
    _configs = pathconfig.get('Configuration', 'List').split(" ")
    _configs.remove('volatile.ini')
    configs = ['%sconfig/'%(opts.tag) + c for c in _configs]
except:
    print("\x1b[31mERROR: configuration file not found. Check config-tag specified with -T and presence of '[Configuration] List' in .ini files.\x1b[0m")
    raise Exception("ConfigNotFound")

configurationNeeded = True #not opts.task.startswith('checklogs')
if opts.ftag == '':
    opts.ftag = opts.task

if debugPrintOUts:
    print 'configs', configs
    print 'opts.ftag', opts.ftag

# read config
config = BetterConfigParser()
config.read(configs)

# ------------------------------------------------------------------------------
# COPY CONFIG files to log output folder
# TODO: clean up
# ------------------------------------------------------------------------------
combinedConfigFileName = None
if configurationNeeded:
    tagDir = pathconfig.get('Directories', 'tagDir')
    if debugPrintOUts:
        print 'tagDir', tagDir
    DirStruct={
        'tagDir': tagDir,
        'ftagdir': '%s/%s/'%(tagDir, opts.ftag),
        'logpath': '%s/%s/%s/'%(tagDir, opts.ftag, 'Logs'),
        'plotpath': '%s/%s/%s/'%(tagDir, opts.ftag, 'Plots'),
        'limitpath': '%s/%s/%s/'%(tagDir, opts.ftag, 'Limits'),
        'confpath': '%s/%s/%s/'%(tagDir, opts.ftag, 'config')
    }

    if debugPrintOUts:
        print 'DirStruct', DirStruct

    for keys in ['tagDir', 'ftagdir', 'logpath', 'plotpath', 'limitpath', 'confpath']:
        try:
            os.stat(DirStruct[keys])
        except:
            os.mkdir(DirStruct[keys])

    # new behavior: write special .ini file, which is not under version control and is always recreated again
    with open("{tag}config/volatile.ini".format(tag=opts.tag), "w") as outputFile:
        vConfig = BetterConfigParser()
        vConfig.add_section('Directories')
        vConfig.set('Directories', 'plotpath', DirStruct['plotpath'])
        vConfig.set('Directories', 'logpath', DirStruct['logpath'])
        vConfig.set('Directories', 'limits', DirStruct['limitpath'])

        # replace arbitrary options with --set command line argument:
        # e.g. --set='Plot_general.var:=<!Plot_general|vars_reduced!>'
        # this will set var in [Plot_general] to: <!Plot_general|vars_reduced!>
        # to set multiple options, use ; to separate, e.g. --set='Plot_general.var:=Hmass;Plot_general.saveDataHistograms:=True'
        if opts.setOptions:
            # escaping of semicolon
            opts.setOptions = opts.setOptions.replace('\;', '##SEMICOLON##')
            for optValue in opts.setOptions.split(";"):
                optValue = optValue.replace('##SEMICOLON##', ';').strip()
                syntaxOk = True
                try:
                    if ':=' in optValue:
                        opt = optValue.split(':=')[0]
                        value = optValue.split(':=')[1]
                    elif optValue:
                        opt = optValue.split(':')[0]
                        value = optValue.split(':')[1]
                except Exception as e:
                    print "ERROR:",e
                    print "ERROR: syntax error in:", optValue
                    print "ERROR: use ; to separate options and use \; to escape semicolons in case they are inside the value. Use := for assignment."
                    syntaxOk = False
                    raise

                if syntaxOk:
                    if not vConfig.has_section(opt.split('.')[0]):
                        vConfig.add_section(opt.split('.')[0])
                    vConfig.set(opt.split('.')[0], opt.split('.')[1], value)
                    print "\x1b[31mCONFIG: SET", opt, "=", value, "\x1b[0m"

        outputFile.write('# this file has been created automatically and will be overwritten by submit.py!\n')
        vConfig.write(outputFile)

    config.read("{tag}config/volatile.ini".format(tag=opts.tag))

    # old behavior: overwrite paths.ini (will only be done if one of the paths to modify has been found!)
    pathfile = open('%sconfig/paths.ini'%opts.tag)
    buffer = pathfile.readlines()
    pathfile.close()
    volatilePathsFound = False
    for line in buffer:
        if line.startswith('plotpath') or line.startswith('logpath') or line.startswith('limits'):
            volatilePathsFound = True
    if volatilePathsFound:
        os.rename('%sconfig/paths.ini'%opts.tag,'%sconfig/paths.ini.bkp'%opts.tag)
        pathfile = open('%sconfig/paths.ini'%opts.tag,'w')
        for line in buffer:
            if line.startswith('plotpath'):
                line = 'plotpath: %s\n'%DirStruct['plotpath']
            elif line.startswith('logpath'):
                line = 'logpath: %s\n'%DirStruct['logpath']
            elif line.startswith('limits'):
                line = 'limits: %s\n'%DirStruct['limitpath']
            pathfile.write(line)
        pathfile.close()

    # copy config files
    for item in configs:
        # if relative path to other config folder, just take file name
        destConfigFileName = item.split('/')[-1]
        shutil.copyfile(item, '%s/%s'%(DirStruct['confpath'], destConfigFileName))
    # combined config
    combinedConfigFileName = '%s/submission_%s.ini'%(DirStruct['confpath'], submitTimestamp)
    with open(combinedConfigFileName, 'w') as combinedConfigFile:
        config.write(combinedConfigFile)
        print 'wrote config to:', combinedConfigFileName
    config = BetterConfigParser()
    config.read(combinedConfigFileName)


# ------------------------------------------------------------------------------
# RETRIEVE RELEVANT VARIABLES FROM CONFIG FILES AND FROM COMMAND LINE OPTIONS
# TODO: clean up
# ------------------------------------------------------------------------------
counter = 0
logPath = config.get('Directories', 'logpath')
#samplesinfo = config.get('Directories', 'samplesinfo')
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

# ------------------------------------------------------------------------------
# CREATE DIRECTORIES
# ------------------------------------------------------------------------------
fileLocator = FileLocator(config=config)
if 'PSI' in whereToLaunch:
    for dirName in ['PREPout', 'SYSout', 'MVAout', 'tmpSamples']:
        if not fileLocator.exists(config.get('Directories', dirName)):
            fileLocator.makedirs(config.get('Directories', dirName))
if 'condor' in whereToLaunch:
    if 'X509_USER_PROXY' not in os.environ:
        print '\x1b[41m\x1b[97mX509 proxy certificate not set, run:\x1b[0m'
        print '--------------'
        print 'voms-proxy-init -voms cms -rfc -out ${HOME}/.x509up_${UID} -valid 192:00'
        print 'export X509_USER_PROXY=${HOME}/.x509up_${UID}'
        print '--------------'

# check if the logPath exist. If not exit
if not os.path.isdir(logPath):
    print '@ERROR : ' + logPath + ': dir not found.'
    print '@ERROR : Create it before submitting '
    print 'Exit'
    sys.exit(-1)

# ------------------------------------------------------------------------------
# SUBMIT SCRIPT options defined in config general.ini [SubmitOptions]
submitQueueDict = {
        'hadd': 'short.q',
        'prep': 'all.q',
        'sysnew': 'all.q',
        'trainReg': 'all.q',
        'cacheplot': 'short.q',
        'runplot': 'short.q', 
        'cachetraining': 'short.q',
        'runtraining': 'short.q',
        'eval': 'all.q',
        'cachedc': 'short.q',
        'rundc': 'short.q',
        'mergedc': 'short.q',
}

# Overwrite by config
if pathconfig.has_section('SubmitOptions'):
    if pathconfig.has_option('SubmitOptions', 'submitQueueDict'):
        submitQueueDict.update(eval(pathconfig.get('SubmitOptions', 'submitQueueDict')))

# Overwrite queue when command line option is set. Otherwise use config if it is avaiable for given task. Default is 'all.q'
if opts.queue is not None:
    _queue = opts.queue
else:
    _queue = 'all.q'
    for key in submitQueueDict:
        if opts.task.startswith(key):
            _queue = submitQueueDict[key]
            break

# ------------------------------------------------------------------------------
# CREATE DICTIONARY TO BE USED AT JOB SUBMISSION TIME
#  ------------------------------------------------------------------------------
repDict = {
    'en': opts.tag,
    'logpath': logPath,
    'job': '',
    'task': opts.task,
    'queue': _queue,
    'timestamp': timestamp,
    'additional': '',
    'job_id': 'noid',
    'nprocesses': str(max(int(pathconfig.get('Configuration', 'nprocesses')), 1))
}

list_submitted_singlejobs = {}
condorBatchGroups = {}

# ------------------------------------------------------------------------------
# get job queue
# ------------------------------------------------------------------------------
def getJobQueue():
    return batchSystem.getJobNames()

# ------------------------------------------------------------------------------
# wait for other jobs to finish first
# ------------------------------------------------------------------------------
def waitFor(jobNameList):
    matches = -1
    while matches != 0:
        matches = 0
        jobNames = [x.strip() for x in jobNameList.split(',') if len(x.strip()) > 0]
        if len(jobNames) > 0:
            jobQueue = getJobQueue()
            for jobName in jobNames:
                matches += len([jobName for job in jobQueue if jobName in job])
                print "\x1b[44m\x1b[97mwaiting for \x1b[92m", matches, "\x1b[97m jobs of type \x1b[93m", jobName, "\x1b[97m to finish....\x1b[0m"
                if matches > 0:
                    break
        if matches > 0:
            time.sleep(30)

# ------------------------------------------------------------------------------
# filter sample list with simple wildcard (*) syntax, used for -S option
# ------------------------------------------------------------------------------
def filterSampleList(sampleIdentifiers, samplesList):
    if samplesList and len([x for x in samplesList if x]) > 0:
        filteredList = []
        for expr in samplesList:
            if expr in sampleIdentifiers:
                filteredList.append(expr)
            elif '*' in expr:
                for sampleIdentifier in sampleIdentifiers:
                    if fnmatch.fnmatch(sampleIdentifier, expr):
                        filteredList.append(sampleIdentifier)
        filteredList = list(set(filteredList))
        return filteredList
    else:
        return sampleIdentifiers

# ------------------------------------------------------------------------------
# STANDARD WORKFLOW SUBMISSION FUNCTION
# ------------------------------------------------------------------------------
def submit(job, repDict):
    batchSystem.submit(job, repDict)

# ------------------------------------------------------------------------------
# status 
# ------------------------------------------------------------------------------
def printSamplesStatus(samples, regions, status):
    print("regions:")
    for i,region in enumerate(regions):
        print ('  %02d: %s'%(i, region))

    print("-"*80)
    header = ' '*40 + ' '.join(['%02d'%x for x in range(len(regions))])
    print(header)
    nFound = 0
    nNotFound = 0
    sampleNames = sorted(list(set([sample.name for sample in samples])))
    for sampleName in sampleNames: 
        line = sampleName.rjust(39) + ' '
        for region in regions:
            if region in status and sampleName in status[region]:
                if status[region][sampleName]:
                    line += '\x1b[42m\x1b[97m[+]\x1b[0m'
                    nFound += 1
                else:
                    line += '\x1b[41m\x1b[97m[X]\x1b[0m'
                    nNotFound += 1
            else:
                line += '\x1b[45m[?]\x1b[0m'
        print line
    print('summary:\n----------\nfound: %d\nnot found:%d'%(nFound, nNotFound))
    return nFound, nNotFound

def getCachingChunkSize(sample, config):
    # number of files to process per job
    chunkSize = int(config.get('General', 'mergeCachingSize')) if config.has_option('General', 'mergeCachingSize') else 100
    if sample.mergeCachingSize > 0:
        chunkSize = sample.mergeCachingSize
    if int(opts.nevents_split_nfiles_single) > 0:
        chunkSize = int(opts.nevents_split_nfiles_single)
        print "\x1b[31mINFO: chunk size overwritten with -N parameter!\x1b[0m"
    return chunkSize

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                              process commands
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# initialize batch system 
# -----------------------------------------------------------------------------
batchSystem = BatchSystem.create(config, interactive=opts.interactive, local=opts.override_to_run_locally, configFile=combinedConfigFileName)

# -----------------------------------------------------------------------------
# check prerequisities
# -----------------------------------------------------------------------------
if opts.waitFor:
    waitFor(opts.waitFor)

# -----------------------------------------------------------------------------
# DATASETS: create list of .root files for each dataset
# -----------------------------------------------------------------------------
if opts.task == 'datasets':
    dasQuery = config.get("Configuration", "dasQuery")
    datasetsFileName = config.get("Configuration", "datasets")
    samplefiles = config.get('Directories', 'samplefiles')
    try:
        os.makedirs(samplefiles)
    except:
        pass
    with open(datasetsFileName, 'r') as datasetsFile:
        datasets = datasetsFile.readlines()
    for dataset in datasets:
        print "DATASET:", dataset
        getDatasetFilesComand = [dasQuery.format(dataset=dataset.strip())]
        p = subprocess.Popen(getDatasetFilesComand, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        print "command:", getDatasetFilesComand
        print "root files:\n", out
        datasetName = dataset.strip().strip('/').split('/')[0]
        with open(samplefiles + '/' + datasetName + '.txt', 'w') as datasetFile:
            datasetFile.write(out)

# -----------------------------------------------------------------------------
# summary: To check prep, sysnew and eval step
# At the end of the prep, sysnew and eval, a table witht the number of files missing BEFORE the submission
# -----------------------------------------------------------------------------

def PrintProcessedFiles(path, subfolder, sampleFileList, prepOUT = None):

    n_missing_files = 0
    n_total_files = len(sampleFileList)

    for sampleFile in  sampleFileList:
        #if step == sys:
        filename=fileLocator.getFilenameAfterPrep(sampleFile)
        FileExist = fileLocator.isValidRootFile("{path}/{subfolder}/{filename}".format(path=pathOUT, subfolder=subfolder, filename=filename))
        #print 'yeah'
        #FileExist = fileLocator.remoteFileExists("{path}/{subfolder}/{filename}".format(path=pathOUT, subfolder=subfolder, filename=filename))

        if not FileExist:
            #If prepOUT is not None: checking the sysnew step or the eval step. Need to check if the broken/missing file in the SYSout/MVAout was in the PREPout to start with. If not, this file will NOT be reported ass missing.
            if prepOUT:
                FileExist = fileLocator.remoteFileExists("{path}/{subfolder}/{filename}".format(path=prepOUT, subfolder=subfolder, filename=filename))
                if FileExist:
                    n_missing_files += 1
                else:
                    n_total_files -= 1
            else:
                n_missing_files += 1

    #if n_missing_files == 0:
    #    print "\x1b[32m All files for",  subfolder, "were already produced. Nothing to submit \x1b[0m.."
    #else:
    #    print "\x1b[36m", n_missing_files,"/", len(sampleFileList), "\x1b[0m missing files for sample \x1b[36m", subfolder, " \x1b[0m.."

    return [n_missing_files, n_total_files]

# -----------------------------------------------------------------------------
# PREP: copy skimmed ntuples to local storage
# -----------------------------------------------------------------------------
if opts.task == 'prep' or opts.task == 'checkprep':

    pathOUT = config.get("Directories", "PREPout")
    samplefiles = config.get('Directories', 'samplefiles')
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, pathOUT)
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)

    chunkSize = 10 if int(opts.nevents_split_nfiles_single) < 1 else int(opts.nevents_split_nfiles_single)

    # for checksysnew step: dic contains missing number of files for each sample
    missingFiles = {}

    # process all sample identifiers (correspond to folders with ROOT files)
    for sampleIdentifier in sampleIdentifiers:
        try:
            sampleFileList = filelist(samplefiles, sampleIdentifier)
        except:
            print "\x1b[31mERROR:", sampleIdentifier, " could not be found!\x1b[0m"
            continue
        if opts.limit and len(sampleFileList) > int(opts.limit):
            sampleFileList = sampleFileList[0:int(opts.limit)]
        splitFilesChunks = [sampleFileList[i:i+chunkSize] for i in range(0, len(sampleFileList), chunkSize)]

        # for checksysnew step: only list of missing files are printed. No jobs are submited
        if opts.task == 'checkprep':
            print "going to check \x1b[36m", len(sampleFileList), "\x1b[0m files for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."
            missingFiles[sampleIdentifier] =  PrintProcessedFiles(pathOUT, sampleIdentifier, sampleFileList)
            continue

        print "going to submit \x1b[36m", len(splitFilesChunks), "\x1b[0m jobs for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."
        # submit a job for a chunk of N files
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks):

            if opts.skipExisting:
                skipChunk = all([fileLocator.isValidRootFile("{path}/{subfolder}/{filename}".format(path=pathOUT, subfolder=sampleIdentifier, filename=fileLocator.getFilenameAfterPrep(fileName))) for fileName in splitFilesChunk])
            else:
                skipChunk = False

            if not skipChunk or opts.force:
                jobDict = repDict.copy()
                jobDict.update({
                    'arguments': {
                        'sampleIdentifier': sampleIdentifier,
                        'fileList': FileList.compress(splitFilesChunk),
                    },
                    'batch': 'prep_' + sampleIdentifier,
                    })
                if opts.force:
                    jobDict['arguments']['force'] = ''
                jobName = 'prep_{sample}_part{part}'.format(sample=sampleIdentifier, part=chunkNumber)
                submit(jobName, jobDict)
            else:
                print "SKIP: chunk #%d, all files exist and are valid root files!"%chunkNumber

    # printing the content of missingFiles
    if opts.task == 'checkprep':
        print '\n================'
        print 'SUMMARY: checkprep'
        print '==================\n'
        for sampleIdentifier in sampleIdentifiers:
            n_missing_files = missingFiles[sampleIdentifier][0]
            n_total_files = missingFiles[sampleIdentifier][1]
            if n_missing_files == 0:
                print "\x1b[32m All files for \x1b[36m", sampleIdentifier, "\x1b[32m were already produced. Nothing to submit \x1b[0m.."
            else:
                print "\x1b[31m WARNING:", n_missing_files,"/", n_total_files, "missing or broken root files for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."

# -----------------------------------------------------------------------------
# HADD: this can merge files partially to avoid too many small trees
# -----------------------------------------------------------------------------
if opts.task == 'hadd':
    from hadd import PartialFileMerger

    inputDir          = opts.input if opts.input else "HADDin"
    outputDir         = opts.output if opts.output else "HADDout"
    inputPath = config.get("Directories", inputDir)
    outputPath = config.get("Directories", outputDir) 

    samplefiles = config.get('Directories', 'samplefiles')
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, inputPath)
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)

    samplefilesMerged = samplefiles + '/merged_' + opts.tag + '/'
    fileLocator.makedirs(samplefilesMerged)

    # process all sample identifiers (correspond to folders with ROOT files)
    for sampleIdentifier in sampleIdentifiers:
        
        try: 
            chunkSize = -1
            if config.has_section('Hadd') and config.has_option('Hadd', sampleIdentifier):
                chunkSize = int(config.get('Hadd', sampleIdentifier).strip())
                print "INFO: chunkSize read from config => ", chunkSize
            else:
                raise Exception("HaddChunkSizeUndefined")

            sampleFileList = filelist(samplefiles, sampleIdentifier)
            if opts.limit and len(sampleFileList) > int(opts.limit):
                sampleFileList = sampleFileList[0:int(opts.limit)]
            splitFilesChunks = [sampleFileList[i:i+chunkSize] for i in range(0, len(sampleFileList), chunkSize)]

            mergedFileNames = []
            for i, splitFilesChunk in enumerate(splitFilesChunks):

                # only give good files to hadd
                fileNames = []
                for fileName in splitFilesChunk:
                    fileNameAfterPrep = "{path}/{sample}/{fileName}".format(path=config.get('Directories','HADDin'), sample=sampleIdentifier, fileName=fileLocator.getFilenameAfterPrep(fileName))
                    #if fileLocator.isValidRootFile(fileNameAfterPrep):
                    if fileLocator.exists(fileNameAfterPrep):
                        fileNames.append(fileName)
                        print ".",
                    else:
                        print "x",
                print "INFO: #files=", len(splitFilesChunk), ", good=", len(fileNames)

                if len(fileNames) > 0:
                    # 'fake' filenames to write into text file for merged files
                    partialFileMerger = PartialFileMerger(fileNames, i, config=config, sampleIdentifier=sampleIdentifier)
                    mergedFileName = partialFileMerger.getMergedFakeFileName()
                    mergedFileNames.append(mergedFileName)

                    outputFileName = partialFileMerger.getOutputFileName()

                    if (opts.force or not fileLocator.isValidRootFile(outputFileName)):
                        jobDict = repDict.copy()
                        jobDict.update({
                            #'queue': submitQueueDict['hadd'],
                            'arguments':{
                                'sampleIdentifier': sampleIdentifier,
                                'fileList': FileList.compress(fileNames),
                                'chunkNumber': i,
                                'inputDir': inputDir,
                                'outputDir': outputDir,
                            },
                            'batch': opts.task + '_' + sampleIdentifier,
                            })
                        if opts.force:
                            jobDict['arguments']['force'] = ''
                        jobName = 'hadd_{sample}_part{part}'.format(sample=sampleIdentifier, part=i)
                        submit(jobName, jobDict)
                else:
                    print "\x1b[31mERROR: no good files for this sample available:",sampleIdentifier,"!\x1b[0m"

            # write text file for merged files
            mergedFileListFileName = '{path}/{sample}.{ext}'.format(path=samplefilesMerged, sample=sampleIdentifier, ext='txt')
            with open(mergedFileListFileName, 'w') as mergedFileListFile:
                mergedFileListFile.write('\n'.join(mergedFileNames))

            print "INFO: hadd {sample}: {a} => {b}".format(sample=sampleIdentifier, a=len(sampleFileList), b=len(splitFilesChunks))
            print "INFO:  > {mergedFileListFileName}".format(mergedFileListFileName=mergedFileListFileName)
        except Exception as e:
            print "\x1b[31mERROR: hadd failed for sample", sampleIdentifier, ": ", e, "\x1b[0m"



# -----------------------------------------------------------------------------
# count: files and events
# -----------------------------------------------------------------------------
if opts.task == 'count':

    # need prepout to get list of file processed during the prep. Files missing in both the prepout and the sysout will not be considered as missing during the sys step
    pathIN = config.get("Directories", opts.input if opts.input else "SYSin")
    samplefiles = config.get('Directories','samplefiles')
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, pathIN)
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)

    haddTargetNumEvents = int(config.get('Configuration', 'haddTargetNumEvents')) if config.has_option('Configuration', 'haddTargetNumEvents') else 30000
    print "INFO: target number of events after merge:", haddTargetNumEvents

    # process all sample identifiers (correspond to folders with ROOT files)
    eventNumberOffsetDict = {}
    chunkSizes = []
    for sampleIdentifier in sampleIdentifiers:
        try:
            sampleFileList = filelist(samplefiles, sampleIdentifier)
        except:
            print "\x1b[31mERROR: sample", sampleIdentifier, " does not exist => skip.\x1b[0m"
            continue
        offset = 0

        if sampleIdentifier not in eventNumberOffsetDict:
            eventNumberOffsetDict[sampleIdentifier] = {}

        for fileName in sampleFileList:
            localFileName = fileLocator.getFilenameAfterPrep(fileName)
            inputFileName = "{path}/{subfolder}/{filename}".format(path=pathIN, subfolder=sampleIdentifier, filename=localFileName)
            eventNumberOffsetDict[sampleIdentifier][inputFileName] = offset

            sampleTree = SampleTree([inputFileName], config=config)
            nEvents = sampleTree.tree.GetEntries()
            print fileName, nEvents
            offset += nEvents
        numberOfTrees = len(sampleFileList)
        totalEvents = offset
        eventsPerTree = totalEvents*1.0/numberOfTrees
        chunkSize = math.ceil(haddTargetNumEvents/eventsPerTree) if eventsPerTree > 0 else 9999
        chunkSizes.append([sampleIdentifier, chunkSize])
    print "---"
    for sampleIdentifier, chunkSize in chunkSizes:
        print "{s}: {c}".format(s=sampleIdentifier, c=int(chunkSize))
    print "---"
    countsFileName = opts.tag + 'config/event_counts.dat'
    with open(countsFileName, 'w') as ofile:
        ofile.write('%r'%eventNumberOffsetDict)


# -----------------------------------------------------------------------------
# SYSNEW: add additional branches and branches for sys variations
# -----------------------------------------------------------------------------
if opts.task == 'sysnew' or opts.task == 'checksysnew':

    # need prepout to get list of file processed during the prep. Files missing in both the prepout and the sysout will not be considered as missing during the sys step
    prepOUT           = config.get("Directories", "PREPout")
    inputDir          = opts.input if opts.input else "SYSin"
    outputDir         = opts.output if opts.output else "SYSout"
    path              = config.get("Directories", inputDir) 
    pathOUT           = config.get("Directories", outputDir)
    samplefiles       = config.get('Directories','samplefiles')
    samplesinfo       = config.get('Directories', 'samplesinfo')
    info              = ParseInfo(samplesinfo, path)
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)

    # check for empty list of collections to add
    addCollections = opts.addCollections
    if not addCollections or len(addCollections.strip())<1:
        print "\x1b[31mWARNING: No collections specified, using the default \x1b[32m'Sys.all'\x1b[31m instead, to force adding nothing, use \x1b[32m--addCollections None\x1b[31m!\x1b[0m"
        addCollections = 'Sys.all'

    # for checksysnew step: dic contains missing number of files for each sample
    missingFiles = {}

    # process all sample identifiers (correspond to folders with ROOT files)
    for sampleIdentifier in sampleIdentifiers:
        try:
            sampleFileList = filelist(samplefiles, sampleIdentifier)
        except:
            print "\x1b[31mERROR: sample", sampleIdentifier, " does not exist => skip.\x1b[0m"
            continue

        # specified with -N option
        chunkSize = 1 if int(opts.nevents_split_nfiles_single) < 1 else int(opts.nevents_split_nfiles_single)

        # for some samples consisting of many files, force override the -N option!
        if config.has_option(sampleIdentifier, 'minFilesPerJob') and not opts.forceN:
            minFilesPerJob = int(config.get(sampleIdentifier, 'minFilesPerJob'))
            if minFilesPerJob > chunkSize:
                chunkSize = minFilesPerJob
                print "\x1b[34mINFO: override chunk size given by -N with value from config:", chunkSize, "\x1b[0m"

        # limit numebr of files per sample
        if opts.limit and len(sampleFileList) > int(opts.limit):
            sampleFileList = sampleFileList[0:int(opts.limit)]

        splitFilesChunks = [sampleFileList[i:i+chunkSize] for i in range(0, len(sampleFileList), chunkSize)]

        # for checksysnew step: only list of missing files are printed. No jobs are submited
        if opts.task == 'checksysnew':
            print "going to check \x1b[36m", len(sampleFileList), "\x1b[0m files for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."
            missingFiles[sampleIdentifier] =  PrintProcessedFiles(pathOUT, sampleIdentifier, sampleFileList, prepOUT)
            continue

        print "going to submit \x1b[36m", len(splitFilesChunks), "\x1b[0m jobs for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."

        # for sysnew
        # submit a job for a chunk of N files
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks):

            if opts.skipExisting:
                # skip, if all output files exist
                skipChunk = all([fileLocator.isValidRootFile("{path}/{subfolder}/{filename}".format(path=pathOUT, subfolder=sampleIdentifier, filename=fileLocator.getFilenameAfterPrep(fileName))) for fileName in splitFilesChunk])
                # skip, if all input files do not exist/are broken
                #allInputFilesMissing = False
                allInputFilesMissing = not any([fileLocator.isValidRootFile("{path}/{subfolder}/{filename}".format(path=path, subfolder=sampleIdentifier, filename=fileLocator.getFilenameAfterPrep(fileName))) or fileLocator.isValidRootFile("{path}/{filename}".format(path=path, filename=fileName)) for fileName in splitFilesChunk])
            else:
                skipChunk = False
                allInputFilesMissing = False

            if (not skipChunk and not allInputFilesMissing) or opts.force:
                jobDict = repDict.copy()
                jobDict.update({
                    'arguments':{
                        'sampleIdentifier': sampleIdentifier,
                        'fileList': FileList.compress(splitFilesChunk),
                        'addCollections': addCollections,
                        'inputDir': inputDir,
                        'outputDir': outputDir,
                    },
                    'batch': opts.task + '_' + sampleIdentifier,
                    })
                if opts.force:
                    jobDict['arguments']['force'] = ''
                if opts.friend:
                    jobDict['arguments']['friend'] = ''
                if opts.join:
                    jobDict['arguments']['join'] = ''
                filesSpec = '_files{start}to{end}'.format(start=chunkNumber*chunkSize, end=chunkNumber*chunkSize+len(splitFilesChunk)) if len(splitFilesChunk) > 1 else ''
                jobName = 'sysnew_{sample}_part{part}{files}'.format(sample=sampleIdentifier, part=chunkNumber, files=filesSpec)
                submit(jobName, jobDict)
            else:
                if allInputFilesMissing:
                    print "\x1b[31mSKIP: chunk %d, all input files of this chunk are missing!\x1b[0m"%chunkNumber
                else:
                    print "SKIP: chunk #%d, all files exist and are valid root files!"%chunkNumber

    if opts.task == 'checksysnew':
        # printing the content of missingFiles
        print '\n=================='
        print 'SUMMARY: checksysnew'
        print '====================\n'
        for sampleIdentifier in sampleIdentifiers:
            #print 'sampleIdentifier is', sampleIdentifier
            n_missing_files = missingFiles[sampleIdentifier][0]
            n_total_files = missingFiles[sampleIdentifier][1]
            if n_missing_files == 0:
                print "\x1b[32m All files for \x1b[36m", sampleIdentifier, "\x1b[32m were already produced wrt the current prepOUT path \x1b[0m.."
            else:
                print "\x1b[31m WARNING:", n_missing_files,"/", n_total_files, "missing or broken root files wrt the current prepOUT path for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."

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
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, config.get('Directories', 'MVAin'))
    samples = info.get_samples(allBackgrounds + allSignals)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    sampleIdentifiers = filterSampleList(list(set([sample.identifier for sample in samples])), samplesList)
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
    
    # per job parallelization parameter can split regions into several job
    if opts.parallel:
        regionChunkSize = int(opts.parallel)
        regionChunks = [trainingRegions[i:i + regionChunkSize] for i in xrange(0, len(trainingRegions), regionChunkSize)]
    else:
        # default is all at once
        regionChunks = [trainingRegions]
    
    # submit separate jobs for all samples
    for sampleIdentifier in sampleIdentifiers:

        # number of files to process per job 
        splitFilesChunkSize = min([getCachingChunkSize(sample, config) for sample in samples if sample.identifier==sampleIdentifier])
        splitFilesChunks = SampleTree({'name': sampleIdentifier, 'folder': config.get('Directories', 'MVAin')}, countOnly=True, splitFilesChunkSize=splitFilesChunkSize, config=config).getSampleFileNameChunks()
        print "DEBUG: split after ", splitFilesChunkSize, " files => number of parts = ", len(splitFilesChunks)
        
        # submit all the single chunks for one sample
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks, start=1):

            for regionChunkNumber, regionChunk in enumerate(regionChunks):
                jobDict = repDict.copy()
                jobDict.update({
                    'arguments':
                        {
                            'trainingRegions': ','.join(regionChunk),
                            'sampleIdentifier': sampleIdentifier,
                            'chunkNumber': chunkNumber,
                            'splitFilesChunks': len(splitFilesChunks),
                            'splitFilesChunkSize': splitFilesChunkSize,
                        },
                    'batch': opts.task + '_' + sampleIdentifier,
                    })
                if opts.force:
                    jobDict['arguments']['force'] = ''
                # pass file list, if only a chunk of it is processed
                if len(splitFilesChunks) > 1:
                    compressedFileList = FileList.compress(splitFilesChunk)
                    jobDict['arguments']['fileList'] = compressedFileList
                jobName = 'training_cache_{sample}_part{part}_{regionChunkNumber}'.format(sample=sampleIdentifier, part=chunkNumber, regionChunkNumber=regionChunkNumber)
                submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# EXPORT HDF5: export training regions to HDF5 format for DNN training 
# -----------------------------------------------------------------------------
if opts.task.startswith('export_h5') or opts.task.startswith('export_hdf5'):
    trainingRegions = [x.strip() for x in (config.get('MVALists','List_for_submitscript')).split(',')]
    for region in trainingRegions:
        jobDict = repDict.copy()
        jobDict.update({
            'arguments': {'trainingRegions': region}, 
            })
        jobName = 'export_h5_{trainingRegions}'.format(trainingRegions=region)
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
        jobDict.update({
            'arguments': {'trainingRegions': trainingRegion}, 
            })
        jobName = 'training_run_{trainingRegions}'.format(trainingRegions=trainingRegion)
        submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# DNN: DNN training 
# -----------------------------------------------------------------------------
if opts.task.startswith('dnn'):
    # training regions
    trainingRegions = [x.strip() for x in (config.get('MVALists', 'List_for_submitscript')).split(',')]

    # separate job for all training regions
    for trainingRegion in trainingRegions:
        if config.has_option(trainingRegion, 'h5'):
            h5file = config.get(trainingRegion, 'h5')
            jobDict = repDict.copy()
            jobDict.update({
                'arguments': {'trainingRegions': h5file}, 
                })
            jobName = 'dnn_run_{trainingRegions}'.format(trainingRegions=trainingRegion)
            submit(jobName, jobDict)
        else:
            print "\x1b[31mERROR: DNN training region needs option 'h5' to specify location of .h5 file. This region will be skipped:", trainingRegion, "\x1b[0m"



# -----------------------------------------------------------------------------
# CACHEPLOT: prepare skimmed trees with cuts for the CR/SR
# -----------------------------------------------------------------------------
if opts.task.startswith('cacheplot'):
    regions = [x.strip() for x in (config.get('Plot_general', 'List')).split(',')]
    sampleNames = eval(config.get('Plot_general', 'samples'))
    dataSampleNames = eval(config.get('Plot_general', 'Data'))

    # get samples info
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, config.get('Directories', 'plottingSamples'))
    samples = info.get_samples(sampleNames + dataSampleNames)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    sampleIdentifiers = filterSampleList(sorted(list(set([sample.identifier for sample in samples]))), samplesList)
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
    
    # submit jobs, 1 to n separate jobs per sample
    for sampleIdentifier in sampleIdentifiers:

        # per job parallelization parameter can split regions into several job
        if opts.parallel:
            regionChunkSize = int(opts.parallel)
            regionChunks = [regions[i:i + regionChunkSize] for i in xrange(0, len(regions), regionChunkSize)]
        else:
            # default is all at once
            regionChunks = [regions]

        # number of files to process per job 
        splitFilesChunkSize = min([getCachingChunkSize(sample, config) for sample in samples if sample.identifier == sampleIdentifier])
        splitFilesChunks = SampleTree({
                'name': sampleIdentifier, 
                'folder': config.get('Directories', 'plottingSamples')
            }, countOnly=True, splitFilesChunkSize=splitFilesChunkSize, config=config).getSampleFileNameChunks()
        print "DEBUG: split after ", splitFilesChunkSize, " files => number of parts = ", len(splitFilesChunks)
            
        # submit all the single parts
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks, start=1):
            compressedFileList = FileList.compress(splitFilesChunk)

            # submit a separate job for all region chunks
            for regionChunkNumber, regionChunk in enumerate(regionChunks): 
                jobDict = repDict.copy()
                jobDict.update({
                        #'queue': submitQueueDict['cacheplot'],
                        'arguments':
                            {
                            'regions': ','.join(regionChunk),
                            'sampleIdentifier': sampleIdentifier,
                            'chunkNumber': chunkNumber,
                            'splitFilesChunks': len(splitFilesChunks),
                            'splitFilesChunkSize': splitFilesChunkSize,
                            },
                        'batch': opts.task + '_' + sampleIdentifier,
                        })
                if opts.force:
                    jobDict['arguments']['force'] = ''
                # pass file list, if only a chunk of it is processed
                if len(splitFilesChunks) > 1:
                    jobDict['arguments']['fileList'] = compressedFileList
                jobName = 'plot_cache_{sample}_part{chunk}_{regionChunkNumber}'.format(sample=sampleIdentifier, chunk=chunkNumber, regionChunkNumber=regionChunkNumber)
                submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# RUNPLOT: make CR/SR plots. Needs cacheplot before. 
# -----------------------------------------------------------------------------
if opts.task.startswith('runplot'):
    # if only a subset of samples is plotted
    if len(opts.samples.strip()) > 0:
        # get samples info
        samplesinfo = config.get('Directories', 'samplesinfo')
        info = ParseInfo(samplesinfo, config.get('Directories', 'plottingSamples'))
        sampleNames = eval(config.get('Plot_general', 'samples'))
        dataSampleNames = eval(config.get('Plot_general', 'Data'))
        samples = info.get_samples(sampleNames + dataSampleNames)
        sampleIdentifiers = filterSampleList(sorted(list(set([sample.identifier for sample in samples]))), samplesList)
    else:
        sampleIdentifiers = None

    regions = [x.strip() for x in (config.get('Plot_general', 'List')).split(',')]
    if len(opts.vars.strip()) > 0:
        plotVars = opts.vars.strip().split(',')
    else:
        plotVars = [x.strip() for x in (config.get('Plot_general', 'var')).split(',')]

    # split list of variables to plot for multiple jobs
    if opts.parallel:
        plotVarChunks = [plotVars[i:i + int(opts.parallel)] for i in xrange(0, len(plotVars), int(opts.parallel))]
    else:
        plotVarChunks = [plotVars]

    # submit all the plot regions as separate jobs
    nRegionsMatched = 0
    for region in regions:

        # if --regions is given, only plot those regions
        regionMatched = any([fnmatch.fnmatch(region, enabledRegion) for enabledRegion in opts.regions.split(',')]) if opts.regions else True
        if regionMatched:
            nRegionsMatched += 1
            for j, plotVarList in enumerate(plotVarChunks):
                jobDict = repDict.copy()
                jobDict.update({
                    'arguments':
                        {
                            'regions': region,
                            'vars': ','.join(plotVarList),
                        }
                    })
                if sampleIdentifiers:
                    jobDict['arguments']['sampleIdentifier'] = ','.join(sampleIdentifiers)
                jobName = 'plot_run_{region}_{chunk}'.format(region=region, chunk=j)
                submit(jobName, jobDict)
    if nRegionsMatched < 1:
        print "WARNING: no plot regions found - nothing to do."

# -----------------------------------------------------------------------------
# DCYIELDS: print yields table for data in datacar regions, without caching
# -----------------------------------------------------------------------------
if opts.task.startswith('dcyields'):
    # get list of all sample names used in DC step
    sampleNames = []
    regions = [x.strip() for x in config.get('LimitGeneral', 'List').split(',') if len(x.strip()) > 0]
    for region in regions:
        for sampleType in ['data']:
            sampleNames += eval(config.get('dc:%s'%region, sampleType))
    sampleNames = list(set(sampleNames))
    
    # get samples info
    sampleFolder = config.get('Directories', 'dcSamples')
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, sampleFolder)
    samples = info.get_samples(sampleNames)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    sampleIdentifiers = filterSampleList(sorted(list(set([sample.identifier for sample in samples]))), samplesList)
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
    
    # submit jobs, 1 to n separate jobs per sample
    for sampleIdentifier in sampleIdentifiers:
        sampleObject = [x for x in samples if x.identifier == sampleIdentifier]
        if len(sampleObject) != 1:
            print "ERROR: samples missing or not unique!!"
            continue
        sample = sampleObject[0]
        sampleTree = SampleTree({
                'name': sampleIdentifier,
                'folder': sampleFolder,
            }, config=config)
        branchList = BranchList(sample.subcut) 
        cutDict = {}
        for region in regions:
            cutDict[region] = config.get('Cuts', config.get('dc:%s'%region, 'cut') )
            branchList.addCut(cutDict[region])
            sampleTree.addFormula(cutDict[region])
        branchList.addCut(config.get('Weights', 'weightF'))
        branchList.addCut(eval(config.get('Branches', 'keep_branches')))
        branchesToKeep = branchList.getListOfBranches()

        sampleTree.enableBranches(branchesToKeep)
        
        eventsPassed = {x:0 for x,v in cutDict.items()}
        for event in sampleTree:
            for region in regions:
                if sampleTree.evaluate(cutDict[region]):
                    eventsPassed[region] += 1
        print "events passed:", eventsPassed

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
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, sampleFolder)
    samples = info.get_samples(sampleNames)

    # find all sample identifiers that have to be cached, if given list is empty, run it on all
    sampleIdentifiers = filterSampleList(sorted(list(set([sample.identifier for sample in samples]))), samplesList)
    print "sample identifiers: (", len(sampleIdentifiers), ")"
    for sampleIdentifier in sampleIdentifiers:
        print " >", sampleIdentifier
        
    # check existence of cached files before job submission, otherwise it will be checked at the beginning of the job
    if opts.skipExisting:
        status = {}
        for i, region in enumerate(regions):
            dcMaker = Datacard(config=config, region=region, verbose=False)
            status[region] = dcMaker.getCacheStatus(useSampleIdentifiers=sampleIdentifiers)
            print "INFO: done checking files for region\x1b[34m",region, "\x1b[0m(",i, "of", len(regions),")"
        printSamplesStatus(samples=samples, regions=regions, status=status)
    
    # per job parallelization parameter can split regions into several jobs
    if opts.parallel:
        regionChunkSize = int(opts.parallel)
        regionChunks = [regions[i:i + regionChunkSize] for i in xrange(0, len(regions), regionChunkSize)]
    else:
        # default is all at once
        regionChunks = [regions]

    # submit jobs, 1 to n separate jobs per sample
    for sampleIdentifier in sampleIdentifiers:

        # if file existence has already been checked, check if it exists for all the regions 
        if opts.skipExisting:
            sampleNames = sorted(list(set([sample.name for sample in samples if sample.identifier == sampleIdentifier])))
            filesMissing = False
            for sampleName in sampleNames:
                for region in regions:
                    if region in status and sampleName in status[region]:
                        if not status[region][sampleName]:
                            filesMissing = True
                            break
            if not filesMissing:
                print 'INFO: SKIP samples:', sampleNames,'files already exist!'
                continue
            else:
                print 'INFO: files do not exist yet!'

        # number of files to process per job
        chunkSize = getCachingChunkSize(sample, config)

        # each entry in the array is for a subsample
        # use same size for all subsamples for now
        sampleSizesList = [chunkSize for sample in samples if sample.identifier == sampleIdentifier]
        splitFilesChunkSize = min(sampleSizesList) if len(sampleSizesList) > 0 else 3
        splitFilesChunks = SampleTree({
                'name': sampleIdentifier, 
                'folder': sampleFolder
            }, countOnly=True, splitFilesChunkSize=splitFilesChunkSize, config=config).getSampleFileNameChunks()
        print "DEBUG: split after ", splitFilesChunkSize, " files => number of parts = ", len(splitFilesChunks)

        # submit all the single parts
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks, start=1):
            compressedFileList = FileList.compress(splitFilesChunk)

            # separate job for all region chunks (default: 1 chunk consisting of all regions)
            for regionChunkNumber, regionChunk in enumerate(regionChunks):
                jobDict = repDict.copy()
                jobDict.update({
                    'arguments':
                        {
                            'regions': ','.join(regionChunk),
                            'sampleIdentifier': sampleIdentifier,
                            'chunkNumber': chunkNumber,
                            'splitFilesChunks': len(splitFilesChunks),
                            'splitFilesChunkSize': splitFilesChunkSize,
                        },
                    'batch': opts.task + '_' + sampleIdentifier,
                    #'queue': submitQueueDict['cachedc'],
                    })
                if opts.force:
                    jobDict['arguments']['force'] = ''
                # pass file list, if only a chunk of it is processed
                if len(splitFilesChunks) > 1:
                    jobDict['arguments']['fileList'] = compressedFileList
                jobName = 'dc_cache_{sample}_part{chunk}_{regionChunkNumber}'.format(sample=sampleIdentifier, chunk=chunkNumber, regionChunkNumber=regionChunkNumber)
                submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# RUNDC: produce DC .txt and .root files. Needs cachedc before.
# -----------------------------------------------------------------------------
if opts.task.startswith('rundc'):
    
    regions = Datacard.getRegions(config=config)
    samples = Datacard.getSamples(config=config, regions=regions)
    sampleIdentifiers = sorted(filterSampleList(list(set([sample.identifier for sample in samples])), samplesList))

    # check existence of cached files
    if opts.checkCached:
        status = {}
        for region in regions:
            dcMaker = Datacard(config=config, region=region, verbose=False)
            status[region] = dcMaker.getCacheStatus(useSampleIdentifiers=sampleIdentifiers)
        nFound, nNotFound = printSamplesStatus(samples=samples, regions=regions, status=status)
        if nNotFound>0:
            print('run cachedc again!')
            raise Exception("NotCached")

    # submit all the DC regions as separate jobs
    for region in regions:
        regionMatched = any([fnmatch.fnmatch(region, enabledRegion) for enabledRegion in opts.regions.split(',')]) if opts.regions else True
        if regionMatched:
            # submit separate jobs for either sampleIdentifiers
            for sampleIdentifier in sampleIdentifiers:

                # large samples can be split further
                if config.has_option(sampleIdentifier, 'dcChunkSize'):
                    chunkSize = int(config.get(sampleIdentifier, 'dcChunkSize'))
                    datacard = Datacard(config=config, region=region, verbose=False)
                    nFiles = datacard.getNumberOfCachedFiles(sampleIdentifier)
                    nJobs = datacard.getNumberOfChunks(sampleIdentifier)

                    if debugPrintOUts:
                        print('INFO: chunk size is ', chunkSize)
                        print('INFO: number of files is ', nFiles)
                        print('INFO: number of jobs is ', nJobs)

                    if nJobs < 1:
                        print '\x1b[31mERROR: not cached:', sampleIdentifier, ", run cachedc again\x1b[0m"
                        raise Exception("NotCached")

                    for chunkNumber in range(1, nJobs+1):
                        jobDict = repDict.copy()
                        jobDict.update({
                            'arguments':
                                {
                                    'regions': region,
                                    'sampleIdentifier': sampleIdentifier,
                                    'chunkNumber': '%d'%chunkNumber,
                                },
                            'batch': opts.task + '_' + sampleIdentifier,
                            })
                        if opts.force:
                            jobDict['arguments']['force'] = ''
                        jobName = 'dc_run_' + '_'.join([v for k,v in jobDict['arguments'].iteritems()])
                        submit(jobName, jobDict)
                else:
                    jobDict = repDict.copy()
                    jobDict.update({
                        'arguments':
                            {
                                'regions': region,
                                'sampleIdentifier': sampleIdentifier,
                            },
                        'batch': opts.task + '_' + sampleIdentifier,
                        })
                    if opts.force:
                        jobDict['arguments']['force'] = ''
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
            #'queue': submitQueueDict['mergedc'],
            'arguments':
                {
                    'regions': region,
                }
            })
        jobName = 'dc_merge_' + '_'.join([v for k,v in jobDict['arguments'].iteritems()])
        submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# regression training
# -----------------------------------------------------------------------------
if opts.task == 'trainReg':
    #repDict['queue'] = 'all.q'
    submit('trainReg',repDict)

# -----------------------------------------------------------------------------
# OLD sys step (here to keep compatibility, use 'sysnew' if possible!!)
# -----------------------------------------------------------------------------
# ADD SYSTEMATIC UNCERTAINTIES AND ADDITIONAL HIGHER LEVEL VARIABLES TO THE TREES
if opts.task == 'sys' or opts.task == 'syseval':
    path = config.get("Directories", "SYSin")
    samplefiles = config.get('Directories','samplefiles')
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, path)
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)
    chunkSize = 10 if int(opts.nevents_split_nfiles_single) < 1 else int(opts.nevents_split_nfiles_single)

    # process all sample identifiers (correspond to folders with ROOT files)
    for sampleIdentifier in sampleIdentifiers:
        sampleFileList = filelist(samplefiles, sampleIdentifier)
        if opts.limit and len(sampleFileList) > int(opts.limit):
            sampleFileList = sampleFileList[0:int(opts.limit)]
        splitFilesChunks = [sampleFileList[i:i+chunkSize] for i in range(0, len(sampleFileList), chunkSize)]
        
        print "going to submit \x1b[36m",len(splitFilesChunks),"\x1b[0m jobs for sample \x1b[36m", sampleIdentifier, " \x1b[0m.." 
        # submit a job for a chunk of N files
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks):
            jobDict = repDict.copy()
            jobDict.update({'arguments':{
                    'sampleIdentifier': sampleIdentifier,
                    'fileList': FileList.compress(splitFilesChunk),
                }})
            jobName = 'sys_{sample}_part{part}'.format(sample=sampleIdentifier, part=chunkNumber)
            submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# EVALUATION OF EVENT BY EVENT BDT SCORE
# -----------------------------------------------------------------------------
if opts.task == 'eval' or opts.task.startswith('eval_'):
    #repDict['queue'] = 'long.q'
    path = config.get("Directories", "MVAin")
    pathOUT = config.get("Directories", "MVAout")
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, path)
    samplefiles = config.get('Directories', 'samplefiles')
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)
    chunkSize = 10 if int(opts.nevents_split_nfiles_single) < 1 else int(opts.nevents_split_nfiles_single)

    # process all sample identifiers (correspond to folders with ROOT files)
    for sampleIdentifier in sampleIdentifiers:
        try:
            splitFilesChunks = partitionFileList(filelist(samplefiles, sampleIdentifier), chunkSize=chunkSize)
        except:
            print "\x1b[31mERROR: missing ", sampleIdentifier, " => skip \x1b[0m"

        # submit a job for each chunk of up to N files
        print "going to submit \x1b[36m",len(splitFilesChunks),"\x1b[0m jobs for sample \x1b[36m", sampleIdentifier, " \x1b[0m.."
        for chunkNumber, splitFilesChunk in enumerate(splitFilesChunks):
            # check existence of OUTPUT files
            if opts.skipExisting:
                skipChunk = all([fileLocator.isValidRootFile("{path}/{subfolder}/{filename}".format(path=pathOUT, subfolder=sampleIdentifier, filename=fileLocator.getFilenameAfterPrep(fileName))) for fileName in splitFilesChunk])
            else:
                skipChunk = False

            if not skipChunk or opts.force:
                jobDict = repDict.copy()
                jobDict.update({
                    'arguments':{
                        'sampleIdentifier': sampleIdentifier,
                        'fileList': FileList.compress(splitFilesChunk),
                    },
                    'batch': opts.task + '_' + sampleIdentifier,
                })
                jobName = 'eval_{sample}_part{part}'.format(sample=sampleIdentifier, part=chunkNumber)
                submit(jobName, jobDict)
            else:
                print "SKIP: chunk #%d, all files exist and are valid root files!"%chunkNumber

# -----------------------------------------------------------------------------
# summary: print list of cuts for CR+SR
# TODO: this should also run some basic checks on the configuration
# -----------------------------------------------------------------------------
if opts.task == 'summary':
    print "-"*80
    print " paths"
    print "-"*80
    for path in ['PREPout', 'SYSin', 'SYSout', 'MVAin', 'MVAout', 'tmpSamples', 'samplesinfo']:
        try:
            print "%s:"%path, "\x1b[34m", config.get('Directories', path) ,"\x1b[0m"
        except:
            print "\x1b[31mERROR: did not find path in config section [Directories]:",path,"\x1b[0m"

    print "-"*80
    print " pre-selection ('prep')"
    print "-"*80
    
    _configs = config.get('Configuration', 'List').split(" ")
    configs = ['%sconfig/'%(opts.tag) + c for c in _configs]
    cumulativeConfig = BetterConfigParser()
    cumulativeConfig2 = BetterConfigParser()

    for addConfig in configs:
        print "CONFIG:", addConfig
        cumulativeConfig2.read(addConfig)

        for s in cumulativeConfig2.sections():
            for v in cumulativeConfig2.options(s):
                try:
                    if cumulativeConfig.has_section(s) and cumulativeConfig.has_option(s, v) and cumulativeConfig.get(s, v) != cumulativeConfig2.get(s, v):
                        print "\x1b[31mWARNING: overwrite config '", s, "' -> '", v , "'"
                        print " from:", cumulativeConfig.get(s, v)
                        print "   to:", cumulativeConfig2.get(s, v)
                        print "\x1b[0m"
                except:
                    pass
        cumulativeConfig.read(addConfig)


    cutDict = {}
    samplesinfo=config.get('Directories','samplesinfo')
    info = ParseInfo(samplesinfo, '')
    # don't look at subsamples, because they have the same pre-selection cut
    samples = [x for x in info if not x.subsample]
    for sample in samples:
        addTreeCut = sample.addtreecut.replace(' ','')
        if addTreeCut not in cutDict:
            cutDict[addTreeCut] = []
        cutDict[addTreeCut].append(sample.identifier)
    for preselectionCut, listOfSamples in cutDict.iteritems():
        print "SAMPLES: \x1b[34m", ','.join(listOfSamples), "\x1b[0m"
        print "CUT: \x1b[32m", preselectionCut,"\x1b[0m"
        print "-"*40

    print "-"*80
    print " plot samples"
    print "-"*80
    plotSamples = eval(config.get('Plot_general', 'samples'))
    samplesUsed = [x for x in info if x.name in plotSamples]
    sampleIdentifiersUsed = sorted(list(set([x.identifier for x in samplesUsed])))
    for sampleIdentifier in sampleIdentifiersUsed:
        print sampleIdentifier
        for sample in samplesUsed:
            if sample.identifier == sampleIdentifier:
                print " >>> ", sample.name

    print "-"*80
    print " CR and SR definitions:"
    print "-"*80
    regions = [x.strip() for x in (config.get('Plot_general', 'List')).split(',')]
    # submit all the plot regions as separate jobs
    for region in regions:
        try:
            regionCut = config.get("Cuts", region)
        except:
            regionCut = "\x1b[31mregion cut missing in cuts.ini!\x1b[0m"
        print " \x1b[33m",region,"\x1b[0m"
        print "  - cut:\x1b[34m", regionCut, "\x1b[0m"
    print "-"*80
    print " weight "
    print "-"*80
    try:
        print config.get('Weights', 'weightF')
    except:
        print "\x1b[31mERROR: 'weightF' missing in section 'Weights'!\x1b[0m"

# checks file status for several steps/folders at once
if opts.task.replace(':','.').split('.')[0] == 'status':
    fileLocator = FileLocator(config=config)
    path = config.get("Directories", "PREPout")
    samplefiles = config.get('Directories','samplefiles') if len(opts.samplesInfo) < 1 else opts.samplesInfo
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, path)
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)

    foldersToCheck = ["SYSout"] if len(opts.folders.strip()) < 1 else opts.folders.split(',')
    basePaths = dict([(x, config.get("Directories", x)) for x in foldersToCheck])

    maxPrintoutLen = 70

    # get list of running jobs
    jobs = {}
    jobPrefix = opts.task.replace(':','.').split('.')[1] if '.' in opts.task or ':' in opts.task else ''
    jobSuffix = opts.tag + jobPrefix
    try:
        #batchSystem = BatchSystem.create(config)
        jobs = {k: True for k in batchSystem.getJobNames()}
        jobsRunning = {k: True for k in batchSystem.getJobNamesRunning()}
    except Exception as e:
        print "ERROR: could not get list of running jobs: ", e

    # process all sample identifiers (correspond to folders with ROOT files)
    fileStatus = {}
    failedJobs = []
    for x in foldersToCheck:
        fileStatus[x] = {}
    for sampleIdentifier in sampleIdentifiers:
        for x in foldersToCheck:
            fileStatus[x][sampleIdentifier] = []
        try:
            sampleFileList = filelist(samplefiles, sampleIdentifier)
        except:
            sampleFileList = []
        for partNumber, sampleFileName in enumerate(sampleFileList):
            localFileName = fileLocator.getFilenameAfterPrep(sampleFileName)
            for folder in foldersToCheck:
                localFilePath = "{base}/{sample}/{file}".format(base=basePaths[folder], sample=sampleIdentifier, file=localFileName)
                fileStatus[folder][sampleIdentifier].append([fileLocator.exists(localFilePath), partNumber])
   
    # print the full sample name at the end so can resubmit them using -S sample1,sample2
    missing_samples_list = []
    completely_empty_samples_list = []
    nFiles = 0
    nFilesDone = 0
    for folder in foldersToCheck:
        folderStatus = fileStatus[folder]
        print "---",folder,"-"*100
        for sampleIdentifier, sampleStatus in folderStatus.iteritems():
            sampleShort = (sampleIdentifier if len(sampleIdentifier)<maxPrintoutLen else sampleIdentifier[:maxPrintoutLen]).ljust(maxPrintoutLen+1)
            statusBar = ""
            for x,number in sampleStatus:
                if batchSystem.job_for_file_exists(jobsRunning, jobPrefix, sampleIdentifier, number, jobSuffix):
                    statusBar = statusBar + ('\x1b[44m\x1b[97m?\x1b[0m' if x else '\x1b[45m\x1b[97mR\x1b[0m')
                elif batchSystem.job_for_file_exists(jobs, jobPrefix, sampleIdentifier, number, jobSuffix):
                    statusBar = statusBar + ('\x1b[44m\x1b[97m?\x1b[0m' if x else '\x1b[43mQ\x1b[0m')
                else:
                    if not x:
                        failedJobs.append(batchSystem.get_single_job_name(jobPrefix, sampleIdentifier, number, jobSuffix))
                    statusBar = statusBar + ('\x1b[42m+\x1b[0m' if x else '\x1b[41mX\x1b[0m')
            nSamplesGood = len([x for x,n in sampleStatus if x])
            if nSamplesGood != len(sampleStatus):
                missing_samples_list.append(sampleIdentifier)
            if nSamplesGood == 0:
                completely_empty_samples_list.append(sampleIdentifier)
            if len(sampleStatus) < 1:
                sampleShort = "\x1b[31m" + sampleShort + "\x1b[0m"
            elif len([x for x,n in sampleStatus if x])==len(sampleStatus):
                sampleShort = "\x1b[32m" + sampleShort + "\x1b[0m"
            print sampleShort, ("%03d/%03d"%(len([x for x,n in sampleStatus if x]),len(sampleStatus))).ljust(8), statusBar, "\x1b[0m "
            nFiles += len(sampleStatus)
            nFilesDone += len([x for x,n in sampleStatus if x])
        print "total: %d/%d"%(nFilesDone, nFiles)
    if len(missing_samples_list) > 0:
        print 'To submit missing sample only, used option -S', ','.join(missing_samples_list)
    if len(completely_empty_samples_list) > 0:
        print '\nTo submit empty samples, used option -S', ','.join(completely_empty_samples_list)
    if len(failedJobs) > 0:
        print "-"*20
        print "failed jobs (%d):"%len(failedJobs)
        if len(failedJobs) > 20:
            failedJobs = failedJobs[:20]
        print "\n".join(failedJobs)
        print "(up to 20 jobs are printed)"

# outputs a simple python code to read the whole sample as chain
if opts.task == 'sample':
    fileLocator = FileLocator(config=config)
    path = config.get("Directories", "SYSout")
    samplefiles = config.get('Directories','samplefiles')
    samplesinfo = config.get('Directories', 'samplesinfo')
    info = ParseInfo(samplesinfo, path)
    print ">", info.getSampleIdentifiers()
    print "filter by:", samplesList
    sampleIdentifiers = filterSampleList(info.getSampleIdentifiers(), samplesList)
    foldersToCheck = ["SYSout"] if len(opts.folders.strip()) < 1 else opts.folders.split(',')
    print "samples:", sampleIdentifiers
    print "folders:", foldersToCheck
    basePaths = dict([(x, config.get("Directories", x)) for x in foldersToCheck])

    for folder in foldersToCheck:
        path = basePaths[folder]
        print "check:", path
        for sampleIdentifier in sampleIdentifiers:
            matchingSamples = [x for x in info if x.identifier == sampleIdentifier]
            sampleObject = matchingSamples[0] if len(matchingSamples)>0 else None
            sampleTree = SampleTree({'name': sampleIdentifier, 'folder': path}, countOnly=False, splitFilesChunkSize=-1, config=config)
            splitFilesChunks = sampleTree.getSampleFileNameChunks()
            try:
                sampleScale = sampleTree.getScale(sampleObject) if sampleObject else 1.0
            except:
                sampleScale = 1.0
            
            fileList = "\n".join(["    '{fileName}',".format(fileName=sampleFileName) for sampleFileName in splitFilesChunks[0]])
            xsWeight = '%f'%sampleScale
            mcWeight = config.get('Weights','weightF')
            weight = "(%s)*%s"%(mcWeight, xsWeight)

            with open('skim_template.dat','r') as skimTemplateFile:
                skimTemplate = skimTemplateFile.read()

            skimTemplate = skimTemplate.replace('{sampleIdentifier}', sampleIdentifier).replace('{fileList}',fileList).replace('{xsWeight}',xsWeight).replace('{mcWeight}',mcWeight).replace('{weight}',weight)
            if opts.output:
                with open(opts.output + '_' + sampleIdentifier + '.py','w') as outputFile:
                    outputFile.write(skimTemplate)
                print "written to: \x1b[34m",opts.output,"\x1b[0m"
            else:
                print "----",sampleIdentifier,"----"
                print skimTemplate

if opts.task.startswith('checklogs'):
    
    # if no task is given (with checklogs:task), then use the one from last submission for the config
    checkTask = None
    if ':' in opts.task:
        checkTask = opts.task.split(':')[1]
    
    # define some error markers to look for besides return code
    errorMarkers = ['Traceback (most recent call last)', '[FATAL] Auth failed', 'bad alloc', 'EXCEPTION:', 'segmentation', 'glibc','file does not exist or is broken, will be SKIPPED']

    # load list of jobs/logs from submission
    try:
        jsonFileName = 'last-submission-' + opts.tag + '_' + checkTask + '.json' if checkTask else 'last-submission-' + opts.tag + '.json'
        with open(jsonFileName, 'r') as infile:
            lastSubmission = json.load(infile)
    except:
        print "ERROR: nothing to check, there is no submission yet!"
        exit(0)
    
    # check job status
    batchSystem = BatchSystem.create(config)
    unfinishedJobs = {k: True for k in batchSystem.getJobNames(includeDeleted=False)}

    nFailed = 0
    nResubmitted = 0
    nComplete = 0
    nRetries = 0
    for job in lastSubmission:
        errorLines = []
        errorStatus = False
        if job['jobName'] in unfinishedJobs:
            status = 'running/queued'
        else:
            if os.path.isfile(job['log']):
                with open(job['log'], 'r') as logfile:
                    for i, line in enumerate(logfile.readlines(), 1):
                        if line.startswith('exit code:'):
                            job['exitCode'] = int(line.split('exit code:')[1].strip())
                        if line.startswith('duration (real time)'):
                            job['duration'] = line.split('duration (real time):')[1].strip()
                        for errorMarker in errorMarkers:
                            if errorMarker in line:
                                errorLines.append("line %d: %s"%(i, line))
                                break
                        # new job output appended to old log -> ignore all errors up to here
                        if line.startswith('Configuration Files:'):
                            errorLines = []
                        # retry
                        if line.strip() == '--- RETRY ---':
                            errorLines = []
                            nRetries += 1

            if 'exitCode' in job:
                if job['exitCode'] == 0:
                    status = 'success'
                    nComplete += 1
                    if 'duration' in job:
                        status += " duration:" + job['duration']
                else:
                    status = 'error=%d'%job['exitCode']
                    errorStatus = True
            else:
                status = 'crashed'
                errorStatus = True
        if len(errorLines) > 0:
            errorStatus = True
        if not opts.unfinished or errorStatus or not status.startswith('success'):
            print "-"*80
            print " NAME:", job['jobName']
            print " LOG:", job['log']
            print " STATUS:", ("\x1b[31m"+status+"\x1b[0m" if errorStatus else status)
            if len(errorLines) > 0:
                print " ERRORS:"
                for errorLine in errorLines:
                    print "  \x1b[31m" + errorLine + "\x1b[0m"
            if errorStatus:
                print " RESUBMIT: \x1b[34m" + job['submitCommand']  + "\x1b[0m"
                nFailed += 1
                if opts.resubmit:
                    subprocess.call([job['submitCommand']], shell=True)
                    nResubmitted += 1
    print "%d jobs in total, %d complete, %d jobs failed, %d jobs resubmitted, %d retries"%(len(lastSubmission), nComplete, nFailed, nResubmitted, nRetries)

# -----------------------------------------------------------------------------
# postfitplot 
# -----------------------------------------------------------------------------
if opts.task.startswith('postfitplot'):
    jobDict = repDict.copy()
    jobName = 'postfitplot'
    submit(jobName, jobDict)

# -----------------------------------------------------------------------------
# make_skims 
# -----------------------------------------------------------------------------
if opts.task.startswith('make_skims'):
    sampleIdentifiers = None

    regions = [x.strip() for x in (config.get('Plot_general', 'List')).split(',')]

    # submit all the plot regions as separate jobs
    nRegionsMatched = 0
    for region in regions:

        # if --regions is given, only plot those regions
        regionMatched = any([fnmatch.fnmatch(region, enabledRegion) for enabledRegion in opts.regions.split(',')]) if opts.regions else True
        if regionMatched:
            nRegionsMatched += 1
            jobDict = repDict.copy()
            jobDict.update({
                'arguments':
                    {
                        'regions': region,
                    }
                })
            jobName = 'makeskims_{region}'.format(region=region)
            submit(jobName, jobDict)
    if nRegionsMatched < 1:
        print "WARNING: no plot regions found - nothing to do."

# if there are still jobs in the local queue, submit them to the batch queue
batchSystem.submitQueue()

# dump submitted jobs
if batchSystem.getNJobsSubmitted() > 0 and not opts.resubmit:
    for fileName in ['last-submission-' + opts.tag + '.json', 'last-submission-' + opts.tag + '_' + opts.task + '.json']:
        try:
            batchSystem.dumpSubmittedJobs(fileName)
        except Exception as e:
            print "ERROR: coudn't dump submitted jobs to json file ", fileName, "!", e
