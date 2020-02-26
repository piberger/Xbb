#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np
import array
import os
from bisect import bisect
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from sampleTree import SampleTree 
from sample_parser import ParseInfo
import BetterConfigParser
from XbbConfig import XbbConfigReader
import root_numpy

# adds the weight from General->weightF as a new branch
class JetPUIDSF(AddCollectionsModule):

    def __init__(self, branchName='weightJetPUID', year=2017, workingPoint="tight", ptCut=30.0, etaCut=2.5, jetIdCut=4, fName_sf="data/jetPUID/2020_01_22/h2_eff_sf_2017_T.root", hName_sf="h2_eff_sf2017_T", fName_mcEff="data/jetPUID/2020_01_22/h2_eff_mc_2017_T.root", hName_mcEff="h2_eff_mc2017_T"):
        super(JetPUIDSF, self).__init__()

        self.ptCut = ptCut
        self.etaCut = etaCut
        self.jetIdCut = jetIdCut
        self.puidCut = {"loose":0, "medium":4, "tight":6}[workingPoint]

        # add new branch
        self.branchName = branchName
        self.addBranch(self.branchName)
        self.addBranch(self.branchName + '_Up')
        self.addBranch(self.branchName + '_Down')

        self.scalefactors, self.ptBins, self.etaBins = self.loadHistogram(fName_sf, hName_sf)
        self.mcEfficiencies, self.ptBins, self.etaBins = self.loadHistogram(fName_mcEff, hName_mcEff)

    def loadHistogram(self, fName, hName):
        if not os.path.exists(fName):
            raise Exception("JetPUID correction file not found.")
        rootfile = ROOT.TFile.Open(fName)
        histo = rootfile.Get(hName)
        arr, bins = root_numpy.hist2array(histo, return_edges=True)
        ptBins = bins[0].tolist() + [100000]
        etaBins = bins[1].tolist()[1:-1]
        return arr, ptBins, etaBins

    def getJetPUIDSF(self, pt, eta):
        eta = min(max(eta,-5.0),5.0)
        if pt<self.ptBins[0] or pt>self.ptBins[-2]: return 1.0
        ptBin  = bisect(self.ptBins, pt) - 1
        etaBin = bisect(self.etaBins, eta) 
        return self.scalefactors[ptBin, etaBin]
    
    def getJetPUIDEfficiency(self, pt, eta):
        eta = min(max(eta,-5.0),5.0)
        if pt<self.ptBins[0] or pt>self.ptBins[-2]: return 1.0
        ptBin  = bisect(self.ptBins, pt) - 1
        etaBin = bisect(self.etaBins, eta)
        return self.mcEfficiencies[ptBin, etaBin]

    # reference: https://indico.cern.ch/event/860457/contributions/3623772/attachments/1939432/3215160/puid5nov2019.pdf
    def getEventSF(self, tree, var=0.0):
        eventSF = 1.0
        for i in range(tree.nJet):
            if tree.Jet_lepFilter[i] and (tree.Jet_Pt[i] > self.ptCut and tree.Jet_Pt[i] < 50.0) and abs(tree.Jet_eta[i]) < self.etaCut and tree.Jet_jetId[i] > self.jetIdCut:
                # sf is eff(data)/eff(MC)
                sf = max(self.getJetPUIDSF(tree.Jet_Pt[i], tree.Jet_eta[i]) + var, 0.0)
                if tree.Jet_puId[i] > self.puidCut:
                    eventSF *= sf 
                else:
                    # epsilon is eff(MC)
                    epsilon = self.getJetPUIDEfficiency(tree.Jet_Pt[i], tree.Jet_eta[i])
                    eventSF *= ((1.0 - sf * epsilon) / (1.0 - epsilon)) if epsilon < 1.00 else 1.0
        return eventSF

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0]           = self.getEventSF(tree)
            self._b(self.branchName + '_Up')[0]   = self.getEventSF(tree, var=0.01)
            self._b(self.branchName + '_Down')[0] = self.getEventSF(tree, var=-0.01)

