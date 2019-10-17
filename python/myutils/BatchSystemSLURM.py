from __future__ import print_function
import xml.etree.ElementTree
import subprocess
import fnmatch
import hashlib
import json
from BatchSystem import BatchSystem
from time import sleep

class BatchSystemSLURM(BatchSystem):

    def __init__(self, config=None, interactive=False, local=False, configFile=None):
        super(BatchSystemSLURM, self).__init__(interactive=interactive, local=local, configFile=configFile)
        self.name = 'SLURM'
        self.config = config
        self.submitScriptTemplate = "sbatch --job-name={jobName} --mem={memory} --time={time} --output={output} {extraOptions} {runscript}"

    def getJobNames(self, includeDeleted=True):
        return jobNames
    
    def getJobNamesRunning(self):
        xmlData = xml.etree.ElementTree.fromstring(subprocess.Popen(["qstat","-xml"], stdout=subprocess.PIPE).stdout.read())
        jobNames = [job.find('JB_name').text for job in xmlData.iter('job_list') if job.find('state').text.strip() == 'r']
        return jobNames

    def getJobs(self, includeDeleted=True):
        lines = subprocess.Popen(["squeue -u $USER"], shell=True, stdout=subprocess.PIPE).stdout.read().split("\n")
        headerParts = [x.strip() for x in lines[0].strip().split(' ') if len(x.strip()) > 0]
        result = []
        for line in lines[1:]:
            if len(line.strip()) > 0:
                lineParts = [x.strip() for x in line.strip().split(' ') if len(x.strip()) > 0]
                jobDict = {
                        'name':       lineParts[headerParts.index('NAME')], 
                        'id':         lineParts[headerParts.index('JOBID')],
                        'state':      lineParts[headerParts.index('ST')],
                        'slots':      lineParts[headerParts.index('NODES')],
                        'is_deleted': False, 
                        'is_running': lineParts[headerParts.index('ST')].strip() == 'R', 
                        'is_pending': lineParts[headerParts.index('ST')].strip() == 'PD', 
                        }
                result.append(jobDict)
        return result

    def getJobIDfromOutput(self, stdOutput):
        jobId = -1
        if stdOutput.startswith('Submitted batch job'):
            jobId = int(stdOutput.split('Submitted batch job')[1].strip())
        else:
            print("WARNING: can't interpret:", stdOutput)
        print("JOB ID was", jobId)
        return jobId

    def resubmit(self, job):
        print("RESUBMIT:", job['submitCommand'])
        stdOutput = subprocess.check_output([job['submitCommand']], shell=True)
        job['id'] = self.getJobIDfromOutput(stdOutput)
        return job

    def submit(self, job, repDict):
        self.nJobsProcessed += 1
        self.submitPreprocess(job, repDict)

        runscript = self.getRunScriptCommand(repDict)
        logPaths = self.getLogPaths(repDict)

        memoryLimit = '6000M'
        if 'queue' in repDict:
            if repDict['queue'] == 'all.q':
                timeLimit = '0-10:00'
            elif repDict['queue'] == 'long.q':
                timeLimit = '1-00:00'
            elif repDict['queue'] == 'short.q':
                timeLimit = '0-01:30'
            elif repDict['queue'] == 'bigmem.q':
                timeLimit = '1-00:00'
                memoryLimit = '12000M'

        extraOptions = self.config.get('SLURM', 'options') if self.config.has_section('SLURM') and self.config.has_option('SLURM', 'options') else ''

        command = self.submitScriptTemplate.format(jobName=repDict['name'], memory=memoryLimit, time=timeLimit, runscript=runscript, output=logPaths['out'], extraOptions=extraOptions)
        return self.run(command, runscript, repDict, getJobIdFn=self.getJobIDfromOutput)

    def cancelJob(self, job):
        jobId = int(job['id'])
        command = self.cancelJobTemplate.format(jobId=jobId)
        commandOutput = self.runShell([command])
        return commandOutput is not None and 'has deleted job' in commandOutput
