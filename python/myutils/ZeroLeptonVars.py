#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from myutils.Jet import Jet

class ZeroLeptonVars(AddCollectionsModule):

    def __init__(self):
        super(ZeroLeptonVars, self).__init__()

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']
        self.addBranch("otherJetsBestBtag")
        self.addBranch("otherJetsHighestPt")
        self.addBranch("minDPhiFromOtherJets")
        self.addBranch("minHdEtaFromOtherJets")
        self.addBranch("minHdPhiFromOtherJets")

    def processEvent(self, tree):
        if not self.sample.isData() and not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            jets = Jet.get(tree)

            self._b("otherJetsBestBtag")[0]    = max([jet.btag for jet in jets if jet.index not in [tree.hJidx[0], tree.hJidx[1]] and jet.pt_reg > 25.0] or [-99.0])
            self._b("otherJetsHighestPt")[0]   = max([jet.pt_reg for jet in jets if jet.index not in [tree.hJidx[0], tree.hJidx[1]] and jet.pt_reg > 25.0] or [-99.0])
            self._b("minDPhiFromOtherJets")[0] = min([abs(ROOT.TVector2.Phi_mpi_pi(jet.phi-tree.MET_Phi)) for jet in jets if jet.index not in [tree.hJidx[0], tree.hJidx[1]] and jet.pt > 30.0] or [99.0])
            self._b("minHdPhiFromOtherJets")[0] = min([abs(ROOT.TVector2.Phi_mpi_pi(jet.phi-tree.H_phi)) for jet in jets if jet.index not in [tree.hJidx[0], tree.hJidx[1]] and jet.pt > 30.0] or [9.0])
            self._b("minHdEtaFromOtherJets")[0] = min([abs(jet.eta-tree.H_eta) for jet in jets if jet.index not in [tree.hJidx[0], tree.hJidx[1]] and jet.pt > 30.0] or [9.0])

            return True


