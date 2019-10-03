from __future__ import print_function
import xml.etree.ElementTree
import subprocess
import fnmatch
import hashlib
import json
from BatchSystem import BatchSystem

class BatchSystemSGE(BatchSystem):
    
    def __init__(self, config=None, interactive=False, local=False, configFile=None):
        super(BatchSystemSGE, self).__init__(interactive=interactive, local=local, configFile=configFile)
        self.name = 'SGE'
        self.config = config

        self.submitScriptTemplate        = 'qsub {options} -o {logfile} {runscript}'
        self.cancelJobTemplate           = 'qdel {jobId}'
        self.submitScriptOptionsTemplate = '-V -cwd -q %(queue)s -N %(name)s -j y -pe smp %(nprocesses)s'
        self.submitScriptSpecialOptions  = {
            'mergesyscachingdcsplit': ' -l h_vmem=6g ',
            'singleeval': ' -l h_vmem=6g ',
            'runtraining': ' -l h_vmem=6g ',
            'eval': ' -l h_vmem=4g ',
            'cachedc': ' -l h_vmem=6g ',
            'cacheplot': ' -l h_vmem=6g ',
            'cachetraining': ' -l h_vmem=6g ',
            'hadd': ' -l h_vmem=6g ',
            'sysnew': ' -l h_vmem=6g ',
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

    def getJobs(self, includeDeleted=True):
        xmlData = xml.etree.ElementTree.fromstring(subprocess.Popen(["qstat","-xml"], stdout=subprocess.PIPE).stdout.read())
        result = []
        for job in xmlData.iter('job_list'):
            jobDict = {
                    'name': job.find('JB_name').text,
                    'id': int(job.find('JB_job_number').text),
                    'state': job.find('state').text.strip(),
                    'slots': int(job.find('slots').text.strip()),
                    'is_deleted': job.find('state').text.strip().startswith('d'),
                    'is_running': job.find('state').text.strip().startswith('r'),
                    'is_pending': job.find('state').text.strip().startswith('q'),
                    }
            result.append(jobDict)
        return result

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

    def resubmit(self, job):
        stdOutput = subprocess.check_output([job['submitCommand']], shell=True)
        job['id'] = self.getJobIDfromOutput(stdOutput)
        return job

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
    
    def cancelJob(self, job):
        jobId = int(job['id'])
        command = self.cancelJobTemplate.format(jobId=jobId)
        commandOutput = self.runShell([command])
        return commandOutput is not None and 'has deleted job' in commandOutput
