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

# adds the weight from General->weightF as a new branch
class JetPUIDSF(AddCollectionsModule):

    def __init__(self, branchName='weightJetPUID', year=2017, workingPoint="tight", ptCut=30.0, etaCut=2.5):
        super(JetPUIDSF, self).__init__()

        self.ptCut = ptCut
        self.etaCut = etaCut
        self.puidCut = {"loose":0, "medium":4, "tight":6}[workingPoint]

        # add new branch
        self.branchName = branchName
        self.addBranch(self.branchName)
        self.addBranch(self.branchName + '_Up')
        self.addBranch(self.branchName + '_Down')
        
        # reference: https://lathomas.web.cern.ch/lathomas/JetMETStuff/PUIDStudies/Oct2019/
        # preliminary 2017 SF
        self.ptBins  = [15,20,25,30,40,50,100000]
        self.etaBins = [-3.0, -2.75, -2.5, -2.0, -1.5, 0, 1.5, 2.0, 2.5, 2.75, 3.0]
        if year==2017 and workingPoint=="tight":
            self.scalefactors = [
                [1.0,0.78,0.85,0.85,0.79,0.86,1.0],
                [1.0,0.94,0.91,0.88,0.81,0.85,1.0],
                [1.0,0.99,0.98,0.96,0.95,0.95,1.0],
                [1.0,0.82,0.90,0.93,0.90,0.93,1.0],
                [1.0,0.85,0.91,0.94,0.91,0.95,1.0],
                [1.0,0.87,0.91,0.94,0.94,0.97,1.0],
                [1.0,0.88,0.92,0.95,0.94,0.97,1.0],
                [1.0,0.84,0.89,0.92,0.90,0.94,1.0],
                [1.0,0.84,0.88,0.91,0.88,0.92,1.0],
                [1.0,0.97,0.97,0.93,0.91,0.92,1.0],
                [1.0,1.01,0.90,0.86,0.79,0.82,1.0],
                [1.0,0.88,0.85,0.89,0.83,0.87,1.0]
            ]
            self.mcEfficiencies = [
                    [1.00,0.00,0.00,0.52,0.44,0.61,1.00],
                    [1.00,0.59,0.59,0.68,0.68,0.79,1.00],
                    [1.00,0.78,0.82,0.88,0.90,0.95,1.00],
                    [1.00,0.55,0.66,0.75,0.70,0.79,1.00],
                    [1.00,0.54,0.66,0.78,0.74,0.82,1.00],
                    [1.00,0.60,0.75,0.84,0.82,0.98,1.00],
                    [1.00,0.59,0.74,0.84,0.81,0.88,1.00],
                    [1.00,0.54,0.67,0.77,0.73,0.82,1.00],
                    [1.00,0.52,0.65,0.74,0.68,0.76,1.00],
                    [1.00,0.81,0.80,0.86,0.88,0.92,1.00],
                    [1.00,0.55,0.57,0.63,0.63,0.75,1.00],
                    [1.00,0.00,0.00,0.51,0.44,0.61,1.00]
                    ]
        elif year==2017 and workingPoint=="medium":
            self.scalefactors = [
                [1.0, 0.84, 0.89, 0.91, 0.88, 0.92, 1.0],
                [1.0, 0.99, 0.94, 0.91, 0.83, 0.88, 1.0],
                [1.0, 1.01, 1.00, 0.97, 0.96, 0.97, 1.0],
                [1.0, 0.89, 0.95, 0.96, 0.95, 0.96, 1.0],
                [1.0, 0.91, 0.95, 0.97, 0.96, 0.98, 1.0],
                [1.0, 0.91, 0.95, 0.97, 0.97, 0.98, 1.0],
                [1.0, 0.92, 0.95, 0.97, 0.97, 0.98, 1.0],
                [1.0, 0.89, 0.94, 0.95, 0.95, 0.97, 1.0],
                [1.0, 0.91, 0.93, 0.96, 0.94, 0.96, 1.0],
                [1.0, 0.97, 1.03, 0.96, 0.93, 0.95, 1.0],
                [1.0, 1.03, 0.96, 0.89, 0.82, 0.87, 1.0],
                [1.0, 0.91, 0.91, 0.94, 0.89, 0.93, 1.0]
                ]
            self.mcEfficiencies = [
                    [1.00,0.45,0.57,0.70,0.62,0.78,1.00],
                    [1.00,0.70,0.70,0.77,0.78,0.88,1.00],
                    [1.00,0.86,0.88,0.93,0.93,0.97,1.00],
                    [1.00,0.75,0.81,0.87,0.85,0.89,1.00],
                    [1.00,0.74,0.82,0.88,0.87,0.91,1.00],
                    [1.00,0.78,0.87,0.92,0.92,0.95,1.00],
                    [1.00,0.77,0.86,0.92,0.92,0.95,1.00],
                    [1.00,0.74,0.82,0.89,0.87,0.91,1.00],
                    [1.00,0.71,0.81,0.86,0.84,0.88,1.00],
                    [1.00,0.90,0.84,0.91,0.92,0.95,1.00],
                    [1.00,0.68,0.67,0.74,0.74,0.84,1.00],
                    [1.00,0.42,0.56,0.68,0.62,0.77,1.00]
                    ]
        else:
            raise Exception("JetPUID:Year/WP combination not found.")

    def getJetPUIDSF(self, pt, eta):
        eta = min(max(eta,-5.0),5.0)
        ptBin  = bisect(self.ptBins, pt)
        etaBin = bisect(self.etaBins, eta)
        return self.scalefactors[etaBin][ptBin]
    
    def getJetPUIDEfficiency(self, pt, eta):
        eta = min(max(eta,-5.0),5.0)
        ptBin  = bisect(self.ptBins, pt)
        etaBin = bisect(self.etaBins, eta)
        return self.mcEfficiencies[etaBin][ptBin]

    # reference: https://indico.cern.ch/event/860457/contributions/3623772/attachments/1939432/3215160/puid5nov2019.pdf
    def getEventSF(self, tree, var=0.0):
        eventSF = 1.0
        for i in range(tree.nJet):
            if tree.Jet_lepFilter[i] and (tree.Jet_Pt[i] > self.ptCut and tree.Jet_Pt[i] < 50.0) and abs(tree.Jet_eta[i]) < self.etaCut:
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

