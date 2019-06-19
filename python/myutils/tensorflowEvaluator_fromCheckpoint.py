#!/usr/bin/env python
import ROOT
import numpy as np
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
sys.path.append("..")
sys.path.append("../tfZllDNN/")
sys.path.append("../tfVHbbDNN/")

# tfZllDNN repository has to be cloned inside the python folder
from tfVHbbDNN.tfDNNevaluator import TensorflowDNNEvaluator

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
        self.tensorflowConfig = self.config.get(self.mvaName, 'tensorflowConfig') if self.config.has_option(self.mvaName, 'tensorflowConfig') else None
        self.scalerDump = self.config.get(self.mvaName, 'scalerDump') if self.config.has_option(self.mvaName, 'scalerDump') else '/'.join(self.tensorflowConfig.split('/')[:-1]) + '/scaler.dmp'
        self.checkpoint = self.config.get(self.mvaName, 'checkpoint') if self.config.has_option(self.mvaName, 'checkpoint') else '/'.join(self.tensorflowConfig.split('/')[:-1]) + '/checkpoints/model.ckpt'
        self.branchName = self.config.get(self.mvaName, 'branchName')

        # CLASSES
        self.classes = eval(self.config.get(self.mvaName, 'classes')) if self.config.has_option(self.mvaName, 'classes') else None
        if self.classes:
            self.nClasses = len(self.classes)
        else:
            try:
                self.nClasses = eval(self.config.get(self.mvaName, 'nClasses'))
            except Exception as e:
                self.nClasses = 1
        
        # FEATURES
        self.nFeatures = len(self.config.get(self.config.get(self.mvaName, "treeVarSet"), "Nominal").strip().split(" "))

        # SIGNAL definition
        self.signalIndex = 0
        if self.config.has_option(self.mvaName, 'signalIndex'):
            self.signalIndex = eval(self.config.get(self.mvaName, 'signalIndex'))
        self.signalClassIds = [self.signalIndex]
        if self.classes:
            self.signalClassIds = [x for x,y in enumerate(self.classes) if y[0].startswith('SIG')]
            print "INFO: signals:", self.signalClassIds

        print "\x1b[31mnum categories:", self.nClasses, "\x1b[0m"

        # systematics
        self.systematics = self.config.get('systematics', 'systematics').split(' ')

        # create output branches
        self.dnnCollections = []
        for i in range(self.nClasses):
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

        # additional pre-computed values for multi-classifiers
        if self.nClasses > 1:
            self.dnnCollectionsMulti = {
                        'argmax' : Collection(self.branchName + "_argmax", self.systematics, leaves=True),
                        'max'    : Collection(self.branchName + "_max",    self.systematics, leaves=True),
                        'max2'   : Collection(self.branchName + "_max2",   self.systematics, leaves=True),  
                        'signal' : Collection(self.branchName + "_signal", self.systematics, leaves=True),
                        'default': Collection(self.branchName,   self.systematics, leaves=True),
                    }

            for k,v in self.dnnCollectionsMulti.items(): 
                self.addCollection(v)

        # create tensorflow graph
        self.ev = TensorflowDNNEvaluator(checkpoint=self.checkpoint, scaler=self.scalerDump)

    # called from main loop for every event
    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            # fill input variables
            inputs = np.full((len(self.systematics), self.nFeatures), 0.0, dtype=np.float32)
            for j, syst in enumerate(self.systematics):
                for i, var in enumerate(self.inputVariables[syst]):
                    inputs[j,i] = self.sampleTree.evaluate(var)

            # use TensorflowDNNEvaluator 
            probabilities = self.ev.eval(inputs)

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
                for j, syst in enumerate(self.systematics):
                    self.dnnCollectionsMulti['argmax']._b()[j] = np.argmax(probabilities[j])
                    sortedValues = np.sort(probabilities[j])
                    self.dnnCollectionsMulti['max']._b()[j] = min(sortedValues[-1], 0.9999)
                    self.dnnCollectionsMulti['max2']._b()[j] = min(sortedValues[-2], 0.9999)

                    # sum the total signal probability, useful in case of multiple signals
                    self.dnnCollectionsMulti['signal']._b()[j] = min(sum([probabilities[j, i] for i in self.signalClassIds]), 0.9999)

                    # default linearization method
                    #self.dnnCollectionsMulti['default']._b()[j] = self.dnnCollectionsMulti['argmax']._b()[j] + min(np.power(sortedValues[-1] - sortedValues[-2], 0.25), 0.9999)
                    self.dnnCollectionsMulti['default']._b()[j] = self.dnnCollectionsMulti['argmax']._b()[j] + min(sortedValues[-1], 0.9999) 

        return True

    def cleanUp(self):
        pass

