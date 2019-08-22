#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
import os
import json
sys.path.append("..")
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

        self.scalerDump = self.config.get(self.mvaName, 'scalerDump') if self.config.has_option(self.mvaName, 'scalerDump') else None
        self.checkpoint = self.config.get(self.mvaName, 'checkpoint') if self.config.has_option(self.mvaName, 'checkpoint') else None
        self.branchName = self.config.get(self.mvaName, 'branchName')

        if self.checkpoint is None:
            print("\x1b[31mERROR: 'checkpoint' option missing for MVA config section [%s]! .../model.ckpt has to be specified to be able to restore classifier.\x1b[0m"%self.mvaName)
            raise Exception("CheckpointError")

        if self.scalerDump is not None and not os.path.isfile(self.scalerDump):
            self.scalerDump = None

        if os.path.isdir(self.checkpoint):
            self.checkpoint += '/model.ckpt' 

        if not os.path.isfile(self.checkpoint + '.meta'):
            print("\x1b[31mERROR: can't restore from graph! .meta file not found in checkpoint:", self.checkpoint, "\x1b[0m")
            raise Exception("CheckpointError")

        # INFO file (with training parameters)
        if os.path.isfile(self.checkpoint + '.info'):
            with open(self.checkpoint + '.info', 'r') as infoFile:
                self.info = json.load(infoFile)
        else:
            print("WARNING: (optional) .info file not found in checkpoint!")
            self.info = {}

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
        self.features  = self.config.get(self.config.get(self.mvaName, "treeVarSet"), "Nominal").strip().split(" ")
        self.nFeatures = len(self.features)
        if 'variables' in self.info:
            if len(self.info['variables']) != self.nFeatures:
                print("\x1b[31mERROR: number of input features does not match!")
                print(" > classifier expects:", len(self.info['variables']))
                print(" > configuration has:", self.nFeatures, "\x1b[0m")
                raise Exception("CheckpointError")
            print("INFO: list of input features:")
            print("INFO:", "config".ljust(40), "---->", "checkpoint")
            match = True
            for i in range(self.nFeatures):
                if self.features[i] != self.info['variables'][i]: 
                    print("\x1b[41m\x1b[37mINFO:", self.features[i].ljust(40), "---->", self.info['variables'][i].ljust(40), " => MISMATCH!\x1b[0m")
                    match = False
                else:
                    print("INFO:\x1b[32m", self.features[i].ljust(40), "---->", self.info['variables'][i], "(match)\x1b[0m")
            if match:
                print("INFO: => all input variables match!")
            else:
                print("WARNING: some variables are not identically defined as for the training, please check!")

        # SIGNAL definition
        self.signalIndex = 0
        if self.config.has_option(self.mvaName, 'signalIndex'):
            self.signalIndex = eval(self.config.get(self.mvaName, 'signalIndex'))
        self.signalClassIds = [self.signalIndex]
        if self.classes:
            self.signalClassIds = [x for x,y in enumerate(self.classes) if y[0].startswith('SIG')]
            print("INFO: signals:", self.signalClassIds)

        print("INFO: number of classes:", self.nClasses if self.nClasses > 1 else 2)

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

