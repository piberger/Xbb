#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from sampleTree import SampleTree 

# adds the weight from General->weightF as a new branch
class WeightAsBranch(AddCollectionsModule):

    def __init__(self, branchName='weight'):
        super(WeightAsBranch, self).__init__()
        self.branchName = branchName

    def customInit(self, initVars):
        self.sample     = initVars['sample']
        self.sampleTree = initVars['sampleTree']
        self.config     = initVars['config']
        self.addBranch(self.branchName)
        self.addBranch("weightF")
        self.addBranch("weightXS")

        if not self.sample.isData():
            self.weightString = self.config.get('Weights','weightF')
            # per sample special weight
            if self.config.has_option('Weights', 'useSpecialWeight') and eval(self.config.get('Weights', 'useSpecialWeight')):
                specialweight = self.sample.specialweight
                self.weightString = "(({weight})*({specialweight}))".format(weight=self.weightString, specialweight=specialweight)
                print ("INFO: use specialweight: {specialweight}".format(specialweight=specialweight))

            self.evalCut = self.config.get('Cuts','EvalCut')
            self.sampleTree.addFormula(self.weightString)
            self.sampleTree.addFormula(self.evalCut)

            self.excludeTrainingSet = False

            # to compute the correct scale to cross-section, all trees of the sample have to be used!
            sampleTreeForCount = SampleTree({'sample': self.sample, 'folder': initVars['pathIN']}, config=self.config)
            self.weightScaleToXS = sampleTreeForCount.getScale(self.sample) * (2.0 if self.excludeTrainingSet else 1.0)
            print "scale:", self.weightScaleToXS, self.sample

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0] = 1.0
            self._b("weightF")[0] = 1.0
            self._b("weightXS")[0] = 1.0

            if not self.sample.isData():

                if not self.excludeTrainingSet or self.sampleTree.evaluate(self.evalCut):
                    weightF = self.sampleTree.evaluate(self.weightString)
                    self._b(self.branchName)[0] = weightF * self.weightScaleToXS
                    self._b("weightF")[0]       = weightF 
                    self._b("weightXS")[0]      = self.weightScaleToXS 
                else:
                    return False
