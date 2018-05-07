#!/usr/bin/env python
import ROOT
import array
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
sys.path.append("..")
from tfZllDNN.TensorflowDNNClassifier import TensorflowDNNClassifier

class tensorflowEvaluator(AddCollectionsModule):

    def __init__(self, nano=False):
        self.nano = nano
        self.debug = False
        super(tensorflowEvaluator, self).__init__()

        self.branchName = 'dnn'
        self.addCollection(Collection(self.branchName, ['Nominal'], leaves=True))


        self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/tfZllDNN/export/Zll2016highpt_23_qAloss_H6v1.cfg'
        self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/tfZllDNN/export/Zll2016highpt_23_qAloss_H6v1-7346705/model.ckpt'

        self.clf = None
        self.reloadModel()


    def reloadModel(self):

        # read network architecture/hyper parameters from file
        with open(self.tensforflowConfig, 'r') as inputFile:
            lines = inputFile.read()
        self.parameters = eval(lines)
        self.clf = TensorflowDNNClassifier(parameters=self.parameters, nFeatures=23)
        self.clf.buildModel()
        self.clf.restore(self.checkpoint)

    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            print "process event ", tree.GetReadEntry()

        return True
