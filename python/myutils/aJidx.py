#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from myutils.Jet import Jet

class aJidx(AddCollectionsModule):

    def __init__(self):
        super(aJidx, self).__init__()
        self.nAddJetMax = 10

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']

        self.addIntegerVectorBranch("aJidx_202p5", default=-1, length=self.nAddJetMax)
        self.addIntegerBranch("naJ_202p5",default=-1)

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            for bn in ['aJidx_202p5']:
                for k in range(self.nAddJetMax):
                    self._b(bn)[k] = -1

            jets = Jet.get(tree)

            jetSelection = lambda x: x.pt>20.0 and abs(x.eta) < 2.5 and x.index!=tree.hJidx[0] and x.index!=tree.hJidx[1]
            additionalJets = sorted([x for x in jets if jetSelection(x)], key=lambda j: -j.pt)
            additionalJetIndices = [x.index for x in additionalJets]

            self._b("naJ_202p5")[0] = min(len(additionalJetIndices), self.nAddJetMax)
            for i in range(self._b("naJ_202p5")[0]): 
                self._b("aJidx_202p5")[i] = additionalJetIndices[i]

