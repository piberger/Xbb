from __future__ import print_function
import xml.etree.ElementTree
import subprocess

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

class BatchSystemSGE(BatchSystem):
    
    def __init__(self):
        self.name = 'SGE'

    def getJobNames(self):
        xmlData = xml.etree.ElementTree.fromstring(subprocess.Popen(["qstat","-xml"], stdout=subprocess.PIPE).stdout.read())
        jobNames = [job.find('JB_name').text for job in xmlData.iter('job_list')]
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

