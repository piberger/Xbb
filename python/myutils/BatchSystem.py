from __future__ import print_function
import xml.etree.ElementTree
import subprocess
import fnmatch
import hashlib
import json

class BatchJob(object):
    def __init__(self, jobName='', submitCommand='', log=''):
        self.data = {
                'jobName': jobName,
                'submitCommand': submitCommand,
                'log': log,
                'err': '',
                'outputFiles': []
                }

    def setProperty(self, prop, value):
        self.data[prop] = value

    def toDict(self):
        return self.data

class BatchSystem(object):

    def __init__(self, interactive=False, local=False, configFile=None):
        self.name = 'undefined'
        self.nJobsProcessed = 0
        self.nJobsSubmitted = 0
        self.nJobsSkipped = 0
        self.interactive = interactive
        self.submittedJobs = []
        self.runLocally = local
        self.configFile = None if interactive else configFile

    def getName(self):
        return self.name
    
    def getJobs(self):
        raise Exception("not implemented")
    
    @staticmethod
    def create(config, interactive=False, local=False, configFile=None):
        whereToLaunch = config.get('Configuration', 'whereToLaunch')
        if 'condor' in whereToLaunch.lower():
            return BatchSystemHTCondor(config, interactive=interactive, local=local, configFile=configFile)
        else:
            return BatchSystemSGE(config, interactive=interactive, local=local, configFile=configFile)
    
    def get_single_job_name(self, jobPrefix, sampleIdentifier, fileNumber, jobSuffix):
        return jobPrefix + '_' + sampleIdentifier + '_part%d'%(fileNumber) + '_' + jobSuffix

    def job_for_file_exists(self, jobList, jobPrefix, sampleIdentifier, fileNumber, jobSuffix):
        # 1 file per job
        if self.get_single_job_name(jobPrefix, sampleIdentifier, fileNumber, jobSuffix) in jobList:
            return True

        # multiple files per job
        jobName = jobPrefix + '_' + sampleIdentifier + '_part*_files*'
        for runningJob in jobList:
            if fnmatch.fnmatch(runningJob, jobName):
                filesSpec = runningJob.split('_files')[1].split('_')[0]
                filesFrom = int(filesSpec.split('to')[0])
                filesTo = int(filesSpec.split('to')[1])
                if filesFrom <= fileNumber and fileNumber <= filesTo:
                    return True
        return False

    def getNJobsSubmitted(self):
        return self.nJobsSubmitted

    def getRunScriptCommand(self, repDict):
        # -----------------------------------------------------------------------------
        # prepare RUN SCRIPT
        # (this is independent of batch system or local)
        # -----------------------------------------------------------------------------
        runScript = 'runAll.sh %(job)s %(en)s '%(repDict)
        runScript += repDict['task'] + ' ' + repDict['nprocesses'] + ' ' + repDict['job_id'] + ' ' + repDict['additional']

        # add named arguments to run script
        if 'arguments' in repDict:
            for argument, value in repDict['arguments'].iteritems():
                runScript += (' --{argument}={value} '.format(argument=argument, value=value)) if len('{value}'.format(value=value)) > 0 else ' --{argument} '.format(argument=argument)

        # add path to config file (Can be dumped combined config instead of single files!)
        if self.configFile:
            runScript += " --configFile=" + self.configFile
        
        if self.interactive or self.runLocally:
            runScript += " --noretry"

        return runScript

    def getLogPaths(self, repDict):
        # log=batch system log, out=stdout of process
        logPaths = {
                'log': '%(logpath)s/%(task)s_%(timestamp)s_%(job)s_%(en)s_%(additional)s.log' %(repDict),
                'error': '%(logpath)s/%(task)s_%(timestamp)s_%(job)s_%(en)s_%(additional)s.err' %(repDict),
                'out': '%(logpath)s/%(task)s_%(timestamp)s_%(job)s_%(en)s_%(additional)s.out' %(repDict),
                'config': "%(logpath)s/%(timestamp)s_%(task)s.config" %(repDict),
            }
        return logPaths

    def submitPreprocess(self, job, repDict):
        repDict['job'] = job
        repDict['name'] = '%(job)s_%(en)s%(task)s' %repDict

    def run(self, command, runScript='', repDict={}, getJobIdFn=None):
        # -----------------------------------------------------------------------------
        # RUN command
        # -----------------------------------------------------------------------------
        if command:
            batchJob = BatchJob(repDict['name'], command, self.getLogPaths(repDict)['out'])
            batchJob.setProperty('repDict', repDict)

            if self.interactive or self.runLocally:
                if self.runLocally:
                    answer = 'l'
                else:
                    print("SUBMIT:\x1b[34m", command, "\x1b[0m\n(press ENTER to run it and continue, \x1b[34ml\x1b[0m to run it locally, \x1b[34md\x1b[0m for debug mode, \x1b[34ma\x1b[0m to run all jobs locally and \x1b[34ms\x1b[0m to submit the remaining jobs)")
                    answer = raw_input().strip()
                if answer.lower() in ['no', 'n']:
                    self.nJobsSkipped += 1
                    return
                elif answer.lower() == 's':
                    self.interactive = False
                    self.nJobsSubmitted += 1
                elif answer.lower() in ['l', 'local', 'a','d']:
                    if answer.lower() == 'a':
                        self.runLocally = True
                    print("run locally")
                    command = 'sh {runscript}'.format(runscript=runScript)
                    if answer.lower() == 'd':
                        command = "XBBDEBUG=1 " + command
                else:
                    self.nJobsSubmitted += 1

            else:
                print("the command is ", command)
                self.nJobsSubmitted += 1

            if getJobIdFn and not (self.interactive or self.runLocally):
                try:
                    stdOutput = subprocess.check_output([command], shell=True)
                except Exception as e:
                    print("\x1b[31mERROR: SUBMISSION FAILED!", e,"\x1b[0m")
                    stdOutput = ""

                try:
                    jobId = getJobIdFn(stdOutput)
                    batchJob.setProperty('id', jobId)
                except:
                    pass
            else:
                subprocess.call([command], shell=True)

            self.submittedJobs.append(batchJob)
            return batchJob
    
    def submitQueue(self):
        pass

    def dumpSubmittedJobs(self, fileName):
        with open(fileName, 'w') as outfile:
            json.dump([x.toDict() for x in self.submittedJobs], outfile)

class BatchSystemSGE(BatchSystem):
    
    def __init__(self, config=None, interactive=False, local=False, configFile=None):
        super(BatchSystemSGE, self).__init__(interactive=interactive, local=local, configFile=configFile)
        self.name = 'SGE'
        self.config = config

        self.submitScriptTemplate = 'qsub {options} -o {logfile} {runscript}'
        self.submitScriptOptionsTemplate = '-V -cwd -q %(queue)s -N %(name)s -j y -pe smp %(nprocesses)s'
        self.submitScriptSpecialOptions = {
            'mergesyscachingdcsplit': ' -l h_vmem=6g ',
            'singleeval': ' -l h_vmem=6g ',
            'runtraining': ' -l h_vmem=6g ',
            'eval': ' -l h_vmem=4g ',
            'cachedc': ' -l h_vmem=6g ',
            'cacheplot': ' -l h_vmem=6g ',
            'cachetraining': ' -l h_vmem=6g ',
            'hadd': ' -l h_vmem=6g ',
            'dnn': ' -l h_vmem=12g ',
        }
        if self.config and self.config.has_section('SubmitOptions'):
            if self.config.has_option('SubmitOptions', 'submitScriptTemplate'):
                submitScriptTemplate = self.config.get('SubmitOptions', 'submitScriptTemplate')

            if self.config.has_option('SubmitOptions', 'submitScriptOptionsTemplate'):
                self.submitScriptOptionsTemplate = self.config.get('SubmitOptions', 'submitScriptOptionsTemplate')

            if self.config.has_option('SubmitOptions', 'submitScriptSpecialOptions'):
                self.submitScriptSpecialOptions.update(eval(self.config.get('SubmitOptions', 'submitScriptSpecialOptions')))

            if self.config.has_option('SubmitOptions', 'submitQueueDict'):
                self.submitQueueDict.update(eval(self.config.get('SubmitOptions', 'submitQueueDict')))


    def getJobNames(self, includeDeleted=True):
        xmlData = xml.etree.ElementTree.fromstring(subprocess.Popen(["qstat","-xml"], stdout=subprocess.PIPE).stdout.read())
        if includeDeleted:
            jobNames = [job.find('JB_name').text for job in xmlData.iter('job_list')]
        else:
            jobNames = [job.find('JB_name').text for job in xmlData.iter('job_list') if not job.find('state').text.strip().startswith('d')]
        return jobNames
    
    def getJobNamesRunning(self):
        xmlData = xml.etree.ElementTree.fromstring(subprocess.Popen(["qstat","-xml"], stdout=subprocess.PIPE).stdout.read())
        jobNames = [job.find('JB_name').text for job in xmlData.iter('job_list') if job.find('state').text.strip() == 'r']
        return jobNames

    def getJobIDfromOutput(self, stdOutput):
        jobId = -1
        for line in stdOutput.split("\n"):
            #Your job 123 ("name") has been submitted
            lineParts = line.strip().split(" ")
            if len(lineParts) > 5 and lineParts[-3] == 'has' and lineParts[-2] == 'been' and lineParts[-1] == 'submitted' and lineParts[0] == 'Your' and lineParts[1] == 'job':
                try:
                    jobId = int(lineParts[2])
                except:
                    pass
        return jobId

    def submit(self, job, repDict):
        self.nJobsProcessed += 1
        self.submitPreprocess(job, repDict)
        
        runScript = self.getRunScriptCommand(repDict)
        logPaths = self.getLogPaths(repDict)

        qsubOptions = self.submitScriptOptionsTemplate%(repDict)

        if repDict['task'] in self.submitScriptSpecialOptions:
            qsubOptions += self.submitScriptSpecialOptions[repDict['task']]

        command = self.submitScriptTemplate.format(options=qsubOptions, logfile=logPaths['out'], runscript=runScript)
        #if not os.path.isfile(logPaths['config']):
        #    dump_config(configs, logPaths['config'])

        return self.run(command, runScript, repDict, getJobIdFn=self.getJobIDfromOutput)


class BatchSystemHTCondor(BatchSystem):
    
    def __init__(self, config=None, local=False, configFile=None):
        super(BatchSystemHTCondor, self).__init__(configFile=configFile)
        self.name = 'HTCondor'
        self.config = config
        self.noBatch = False
        self.templateFileName = 'batch/condor/template.sub'
        self.template = None
        self.runLocally = local
        self.condorBatchGroups = {}

    def loadTemplate(self):
        with open(self.templateFileName, 'r') as templateFile:
            self.template = templateFile.read()

    def getJobNames(self):
        p = subprocess.Popen(["condor_q", "-nobatch"], stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        return out.split("\n")

    def submit(self, job, repDict):
        self.nJobsProcessed += 1
        self.submitPreprocess(job, repDict)

        runScript = self.getRunScriptCommand(repDict)
        logPaths = self.getLogPaths(repDict)

        if not self.template:
            self.loadTemplate()

        # -----------------------------------------------------------------------------
        # CONDOR
        # -----------------------------------------------------------------------------
        firstFileOfBatch = False
        isBatched = 'batch' in repDict and not self.noBatch
        if isBatched:
            if repDict['batch'] not in self.condorBatchGroups:
                # first file of batch -> make new submit file
                firstFileOfBatch = True
                self.condorBatchGroups[repDict['batch']] = '%(task)s_%(timestamp)s_%(batch)s'%(repDict)
            # use existing submit file and append
            dictHash = self.condorBatchGroups[repDict['batch']]
        else:
            # create a new submit file
            dictHash = '%(task)s_%(timestamp)s'%(repDict) + '_%x'%hash('%r'%repDict)

        condorDict = {
            'runscript': runScript.split(' ')[0],
            'arguments': ' '.join(runScript.split(' ')[1:]),
            'output': logPaths['out'],
            'log': logPaths['log'],
            'error': logPaths['error'],
            'queue': 'workday',
        }
        submitFileName = 'condor_{hash}.sub'.format(hash=dictHash)

        # append to existing bath
        if isBatched:
            with open(submitFileName, 'a') as submitFile:
                submitFile.write("\n")
                submitFile.write(self.template.format(**condorDict))
            command = None
        else:
            with open(submitFileName, 'w') as submitFile:
                submitFile.write(self.template.format(**condorDict))
            command = 'condor_submit {submitFileName}'.format(submitFileName=submitFileName)
        print("COMMAND:\x1b[35m", runScript, "\x1b[0m")
        return self.run(command, runScript, repDict)

    def submitQueue(self):
        for batchName, submitFileIdentifier in condorBatchGroups.iteritems():
            submitFileName = 'condor_{identifier}.sub'.format(identifier=submitFileIdentifier)
            command = 'condor_submit {submitFileName}  -batch-name {batchName}'.format(submitFileName=submitFileName, batchName=batchName)
            if self.interactive:
                print("SUBMIT:\x1b[34m", command, "\x1b[0m\n(press ENTER to run it and continue)")
                answer = raw_input().strip()
                if answer.lower() in ['no', 'n', 'skip']:
                    continue
            else:
                print("the command is ", command)
            subprocess.call([command], shell=True)

