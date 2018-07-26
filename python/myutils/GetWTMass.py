#!/usr/bin/env python
import ROOT
import numpy as np
import array
from pdgId import pdgId
import sys
import math as m
import pdb

class GetWTMass(object):

    def __init__(self, sample=None, nano=False):
        self.nano = nano
        self.lastEntry = -1
        self.branchBuffers = {}
        self.branches = []
        self.branches.append({'name': 'V_mt', 'formula': self.getBranch, 'arguments': 'V_mt'})
        self.branchBuffers['V_mt'] = array.array('f', [0])

    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getBranches(self):
        return self.branches

    # read from buffers which have been filled in processEvent()
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        if currentEntry != self.lastEntry:
            self.lastEntry = currentEntry

            Lep = ROOT.TLorentzVector()
            MET = ROOT.TLorentzVector()

            if not self.nano:
                MET.SetPtEtaPhiM(tree.met_pt, tree.met_eta, tree.met_phi, tree.met_mass)
                Lep.SetPtEtaPhiM(tree.vLeptons_new_pt[0], tree.vLeptons_new_eta[0], tree.vLeptons_new_phi[0], tree.vLeptons_new_mass[0])
            else:
                MET.SetPtEtaPhiM(tree.MET_pt, 0, tree.MET_phi, 0)
                if len(getattr(tree,'VMuonIdx')) == 1:
                    Lep.SetPtEtaPhiM(tree.Muon_pt[tree.VMuonIdx[0]], tree.Muon_eta[tree.VMuonIdx[0]], tree.Muon_phi[tree.VMuonIdx[0]], tree.Muon_mass[tree.VMuonIdx[0]])
                if len(getattr(tree,'VElectronIdx')) == 1:
                    Lep.SetPtEtaPhiM(tree.Electron_pt[tree.VElectronIdx[0]], tree.Electron_eta[tree.VElectronIdx[0]], tree.Electron_phi[tree.VElectronIdx[0]], tree.Electron_mass[tree.VElectronIdx[0]])


            cosPhi12 = min(1,(Lep.Px()*MET.Px() + Lep.Py()*MET.Py()) / (Lep.Pt() * MET.Pt()))
            self.branchBuffers['V_mt'][0] = m.sqrt(2*Lep.Pt()*MET.Pt() * (1 - cosPhi12))

            return True
