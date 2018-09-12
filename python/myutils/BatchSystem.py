from __future__ import print_function
import xml.etree.ElementTree
import subprocess
import fnmatch

class BatchSystem(object):

    def __init__(self):
        self.name = 'undefined'

    def getName(self):
        return self.name
    
    def getJobs(self):
        raise Exception("not implemented")
    
    @staticmethod
    def create(config):
        if 1:
            return BatchSystemSGE()
        else:
            return BatchSystemHTCondor()
    
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


class BatchSystemSGE(BatchSystem):
    
    def __init__(self):
        self.name = 'SGE'

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

class BatchSystemHTCondor(BatchSystem):
    
    def __init__(self):
        self.name = 'HTCondor'

    def getJobNames(self):
        p = subprocess.Popen(["condor_q", "-nobatch"], stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        return out.split("\n")

