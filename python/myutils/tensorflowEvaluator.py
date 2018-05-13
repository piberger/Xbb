#!/usr/bin/env python
import ROOT
import array
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
sys.path.append("..")
from tfZllDNN.TensorflowDNNClassifier import TensorflowDNNClassifier
from MyStandardScaler import StandardScaler
import numpy as np
import pickle

class tensorflowEvaluator(AddCollectionsModule):

    def __init__(self, nano=False):
        self.nano = nano
        self.debug = False
        super(tensorflowEvaluator, self).__init__()

    def customInit(self, initVars):
        self.config = initVars['config']
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        
        #self.mvaName = 'ZllBDT_highptCMVAnew'
        #self.branchName = 'dnnHigh'
        #self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_23_qAloss_H6v1.cfg'
        #self.scalerDump =  '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_23_qAloss_H6v1-7346705/scaler.dmp'
        #self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_23_qAloss_H6v1-7346705/model.ckpt'
        
        #self.mvaName = 'ZllBDT_lowptCMVAnew'
        #self.branchName = 'dnnLow'
        #self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016lowpt_23_qAloss_H4v1.cfg'
        #self.scalerDump =  '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016lowpt_23_qAloss_H4v1/scaler.dmp'
        #self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016lowpt_23_qAloss_H4v1/model.ckpt'
        #export/Zll2016highpt_15_qAloss_v3/Zll2016highpt_15_qAloss_H6v2.cfg
        
        #self.mvaName = 'tfZllDNN_highpt15'
        #self.branchName = 'dnn15High'
        #self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_15_qAloss_v3/Zll2016highpt_15_qAloss_H6v2.cfg'
        #self.scalerDump =  '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_15_qAloss_v3/scaler.dmp'
        #self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_15_qAloss_v3/checkpoints/model.ckpt'

        #Zll2016lowpt_15_qAloss_v1/Zll2016lowpt_15_qAloss_H6v2.cfg
        #self.mvaName = 'tfZllDNN_lowpt15'
        #self.branchName = 'dnn15Low'
        #self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016lowpt_15_qAloss_v1/Zll2016lowpt_15_qAloss_H6v2.cfg'
        #self.scalerDump =  '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016lowpt_15_qAloss_v1/scaler.dmp'
        #self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016lowpt_15_qAloss_v1/checkpoints/model.ckpt'

        #self.mvaName = 'tfZllDNN_incl15'
        #self.branchName = 'dnn15Incl'
        #self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016incl_15_qAloss_v4/Zll2016incl_15_qAloss_H6v4.cfg'
        #self.scalerDump =  '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016incl_15_qAloss_v4/scaler.dmp'
        #self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016incl_15_qAloss_v4/checkpoints/model.ckpt'
        
        self.mvaName = 'tfZllDNN_highpt15'
        self.branchName = 'dnn15HighBtagSys'
        self.tensforflowConfig = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_15_qAS_btagsystematics_v2/Zll2016highpt_23to15_qAS_v4.cfg'
        self.scalerDump =  '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_15_qAS_btagsystematics_v2/scaler.dmp'
        self.checkpoint = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/export/Zll2016highpt_15_qAS_btagsystematics_v2/checkpoints/model.ckpt'

        #Zll2016highpt_15_qAS_btagsystematics_v2/Zll2016highpt_23to15_qAS_v4.cfg
        self.systematics = self.config.get('systematics', 'systematics').split(' ')

        # create output branches
        self.dnnCollection = Collection(self.branchName, self.systematics, leaves=True) 
        self.addCollection(self.dnnCollection)

        # create formulas for input variables
        self.inputVariables = {}
        for syst in self.systematics:
            self.inputVariables[syst] = self.config.get(self.config.get(self.mvaName, "treeVarSet"), syst if self.sample.isMC() else 'Nominal').split(' ')
            for var in self.inputVariables[syst]:
                self.sampleTree.addFormula(var)

        # create tensorflow graph
        self.reloadModel()

    def loadModelConfig(self):
        # read network architecture/hyper parameters from file
        with open(self.tensforflowConfig, 'r') as inputFile:
            lines = inputFile.read()
        return eval(lines)

    def reloadModel(self):
        self.parameters = self.loadModelConfig()
        
        # build tensorflow graph
        self.clf = TensorflowDNNClassifier(parameters=self.parameters, nFeatures=len(self.inputVariables[self.systematics[0]]), limitResources=True)
        self.clf.buildModel()

        # restore rom checkpoint
        self.clf.restore(self.checkpoint)
        with open(self.scalerDump, "r") as inputFile:
            self.scaler = pickle.load(inputFile)

        # initialize arrays for transfering data to graph
        self.data = {}
        self.data['test'] = {
                    'X': np.full((len(self.systematics), self.clf.nFeatures), 0.0),
                    'y': np.full((len(self.systematics),), 1.0, dtype=np.float32),
                    'sample_weight': np.full((len(self.systematics),), 1.0, dtype=np.float32),
                }

    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            # fill input variables
            for j, syst in enumerate(self.systematics):
                for i, var in enumerate(self.inputVariables[syst]):
                    self.data['test']['X'][j,i] = self.sampleTree.evaluate(var)

            # standardize
            self.data['test']['X_sc'] = self.scaler.transform(self.data['test']['X'])
            
            # evaluate
            probabilities = self.clf.session.run(self.clf.predictions, feed_dict={
                                self.clf.x: self.data['test']['X_sc'], 
                                self.clf.y_: self.data['test']['y'].astype(int),
                                self.clf.w: self.data['test']['sample_weight'],
                                self.clf.keep_prob: np.array([1.0]*len(self.clf.pKeep), dtype=np.float32),
                                self.clf.learning_rate_adam: self.parameters['learning_rate_adam_start'],
                                self.clf.is_training: False,
                            })

            # fill output branches
            for j, syst in enumerate(self.systematics):
                self.dnnCollection[self.branchName][j] = probabilities[j,0]

        return True
