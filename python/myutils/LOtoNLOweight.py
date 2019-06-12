#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule

class LOtoNLOweight(AddCollectionsModule):

    def __init__(self, branchName='weightLOtoNLO', paperStyle=True):
        super(LOtoNLOweight, self).__init__()
        self.branchName = branchName

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']
        if not self.sample.isData():
            self.addBranch(self.branchName)

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.sample.isData() and not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0] = 1.0

            if self.applies(tree):
                etabb = abs(tree.Jet_eta[tree.hJidx[0]]-tree.Jet_eta[tree.hJidx[1]])
                njets = tree.sampleIndex % 10
                if njets < 3:
                    self._b(self.branchName)[0] = 1.153 * self.LOtoNLOWeightBjetSplitEtabb(etabb, njets) 
                else:
                    print("\x1b[31mERROR: sampleIndex==", tree.sampleIndex, "\x1b[0m")
                    raise Exception("IllegalSampleIndex")

    def applies(self, tree):
        isVJets = False
        sampleCat = int(tree.sampleIndex - (tree.sampleIndex % 10))

        # sync with AT: DYJetsToLL_M-4to50 not reweighted

        # Z+jets normal, W+jets normal, W+jets b-enriched
        if sampleCat in [4000,4100,4200,4300,4400,4500,4600,4700,5000,5100,5300,5400,11000,11100,11200,11300,11400,11500,11600,11700,15000,15100,15200,15300,15400,15500,15600]:
            isVJets = True
        
        # Z+jets b-enriched
        if sampleCat in [14000,12000,12100,12200,14100,14200,16000,16100,16200,16300]:
            isVJets = True

        return isVJets

    def LOtoNLOWeightBjetSplitEtabb(self, etabb, njets):
        SF = 1.
        if etabb < 5:
            if njets < 1:
                SF = 0.935422 + 0.0403162*etabb -0.0089026*etabb*etabb +0.0064324*etabb*etabb*etabb -0.000212443*etabb*etabb*etabb*etabb
            elif njets == 1:
                SF = 0.962415 +0.0329463*etabb -0.0414479*etabb*etabb +0.0240993*etabb*etabb*etabb -0.00278271*etabb*etabb*etabb*etabb
            elif njets >= 2:
                SF = (0.721265 -0.105643*etabb -0.0206835*etabb*etabb +0.00558626*etabb*etabb*etabb)*np.exp(0.450244*etabb)
        return SF

