#!/usr/bin/env python
import ROOT
import numpy as np
import array
from pdgId import pdgId
import sys
import math as m
import pdb

class GetWTMass(object):

    def __init__(self, sample=None, nano=False,branchName= 'V_mt'):
        self.nano = nano
        self.lastEntry = -1
        self.branchName = branchName
        self.branchBuffers = {}
        self.branches = []
        self.branches.append({'name': self.branchName, 'formula': self.getBranch, 'arguments': self.branchName})
        self.branchBuffers[self.branchName] = array.array('f', [0])

    def customInit(self, initVars):
#        self.sample = initVars['sample']
        self.config = initVars['config']
        
        self.dataset = self.config.get('General','dataset')

        #Branch names from config
        if self.config.has_option('General', 'eIdx') and  self.config.has_option('General', 'muIdx'):
           self.eIdx = self.config.get('General', 'eIdx')
           self.muIdx = self.config.get('General', 'muIdx')
        else:
           print "WARNING: eIdx and muIdx not defined in [General]! Using default lepton index: \'vLidx\' "
           self.eIdx = "vLidx"
           self.muIdx = "vLidx" 

        if self.dataset == '2016':
           self.METpt = 'MET_pt' 
           self.METphi = 'MET_phi' 
        elif self.dataset == '2017':
           self.METpt = 'MET_Pt' 
           self.METphi = 'MET_Phi' 

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


            e1Idx = getattr(tree,self.eIdx)[0]
            mu1Idx = getattr(tree,self.muIdx)[0]
            treeMETpt = getattr(tree,self.METpt) 
            treeMETphi = getattr(tree,self.METphi) 

            Lep = ROOT.TLorentzVector()
            MET = ROOT.TLorentzVector()

            if not self.nano:
                MET.SetPtEtaPhiM(tree.met_pt, tree.met_eta, tree.met_phi, tree.met_mass)
                Lep.SetPtEtaPhiM(tree.vLeptons_new_pt[0], tree.vLeptons_new_eta[0], tree.vLeptons_new_phi[0], tree.vLeptons_new_mass[0])
            else:
                MET.SetPtEtaPhiM(treeMETpt, 0, treeMETphi, 0)
                if tree.Vtype == 2 :
                    Lep.SetPtEtaPhiM(tree.Muon_pt[mu1Idx], tree.Muon_eta[mu1Idx], tree.Muon_phi[mu1Idx], tree.Muon_mass[mu1Idx])
                if tree.Vtype == 3:
                    Lep.SetPtEtaPhiM(tree.Electron_pt[e1Idx], tree.Electron_eta[e1Idx], tree.Electron_phi[e1Idx], tree.Electron_mass[e1Idx])


            cosPhi12 = min(1,(Lep.Px()*MET.Px() + Lep.Py()*MET.Py()) / (Lep.Pt() * MET.Pt()))
            self.branchBuffers[self.branchName][0] = m.sqrt(2*Lep.Pt()*MET.Pt() * (1 - cosPhi12))

            return True
