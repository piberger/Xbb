#!/usr/bin/env python
import ROOT
import array
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
sys.path.append("..")
sys.path.append("../tfZllDNN/")
# tfZllDNN repository has to be cloned inside the python folder
from tfZllDNN.TensorflowDNNClassifier import TensorflowDNNClassifier
from MyStandardScaler import StandardScaler
import numpy as np
import pickle

# reads tensorflow checkpoints and applies DNN output to ntuples,
# including variations from systematic uncertainties
# needs: tensorflow >=1.4
class tensorflowEvaluator(AddCollectionsModule):

    def __init__(self, mvaName, nano=False):
        self.mvaName = mvaName
        self.nano = nano
        self.debug = False
        super(tensorflowEvaluator, self).__init__()

    def customInit(self, initVars):
        self.config = initVars['config']
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        self.tensorflowConfig = self.config.get(self.mvaName, 'tensorflowConfig')
        self.scalerDump = self.config.get(self.mvaName, 'scalerDump')
        self.checkpoint = self.config.get(self.mvaName, 'checkpoint')
        self.branchName = self.config.get(self.mvaName, 'branchName')
        self.signalIndex = 0
        if self.config.has_option(self.mvaName, 'signalIndex'):
            self.signalIndex = int(self.config.get(self.mvaName, 'signalIndex'))
        try:
            self.nClasses = int(self.config.get(self.mvaName, 'nClasses'))
        except Exception as e:
            print "exception:",e
            self.nClasses = 1
        print "\x1b[31mnum categories:", self.nClasses, "\x1b[0m"

        # Jet systematics
        self.systematics = self.config.get('systematics', 'systematics').split(' ')
        
        self.dnnCollections = []

        for i in range(self.nClasses):
            # create output branches
            collectionName = self.branchName if self.nClasses==1 else self.branchName + "_%d"%i
            self.dnnCollection = Collection(collectionName, self.systematics, leaves=True) 
            self.addCollection(self.dnnCollection)
            self.dnnCollections.append(self.dnnCollection)

            # create formulas for input variables
            self.inputVariables = {}
            for syst in self.systematics:
                self.inputVariables[syst] = self.config.get(self.config.get(self.mvaName, "treeVarSet"), syst if self.sample.isMC() else 'Nominal').split(' ')
                for var in self.inputVariables[syst]:
                    self.sampleTree.addFormula(var)

        # create tensorflow graph
        self.reloadModel()

    # read network architecture/hyper parameters from *.cfg file
    def loadModelConfig(self):
        with open(self.tensorflowConfig, 'r') as inputFile:
            lines = inputFile.read()
        return eval(lines)

    # rebuild tensorflow graph
    def reloadModel(self):
        self.parameters = self.loadModelConfig()
        
        # for evaluation of weights always set limitResources=True which limits threads (and therefore memory)
        self.clf = TensorflowDNNClassifier(parameters=self.parameters, nFeatures=len(self.inputVariables[self.systematics[0]]), limitResources=True, nClasses=self.nClasses if self.nClasses>1 else 2)
        self.clf.buildModel()

        # restore rom checkpoint
        self.clf.restore(self.checkpoint)
        with open(self.scalerDump, "r") as inputFile:
            self.scaler = pickle.load(inputFile)

        # initialize arrays for transfering data to graph
        self.data = {'test':{
                                'X': np.full((len(self.systematics), self.clf.nFeatures), 0.0),
                                'y': np.full((len(self.systematics),), 1.0, dtype=np.float32),
                                'sample_weight': np.full((len(self.systematics),), 1.0, dtype=np.float32),
                            }
                    }

    # called from main loop for every event
    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            # fill input variables
            for j, syst in enumerate(self.systematics):
                for i, var in enumerate(self.inputVariables[syst]):
                    self.data['test']['X'][j,i] = self.sampleTree.evaluate(var)
            
            # standardize
            self.data['test']['X_sc'] = self.scaler.transform(self.data['test']['X'])
            
            if self.debug:
                print("INPUTS:", "".join([("%1.3f"%self.data['test']['X_sc'][0,i]).ljust(11) for i in range(self.clf.nFeatures)]))
            
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
            if len(self.dnnCollections) == 1:
                # for signal/background store just one of the two, selected by self.signalIndex
                for i,dnnCollection in enumerate(self.dnnCollections):
                    for j, syst in enumerate(self.systematics):
                        dnnCollection[dnnCollection.name][j] = probabilities[j, self.signalIndex]
            else:
                # for multi-class, store all
                for i,dnnCollection in enumerate(self.dnnCollections):
                    for j, syst in enumerate(self.systematics):
                        dnnCollection[dnnCollection.name][j] = probabilities[j, i]

        return True
