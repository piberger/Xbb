#!/usr/bin/env python
import ROOT
import sys
import numpy as np
import math

#Estimate the smearing systematics on the Fat Jets
##Method taken from 
#https://twiki.cern.ch/twiki/bin/view/Sandbox/PUPPIJetMassScaleAndResolution#PUPPI_softdrop_jet_mass_scale_an

##Resolution taken from 
#https://github.com/thaarres/PuppiSoftdropMassCorr/tree/master/weights

class FatJetMassJER(object):

    def __init__(self, Rnom = 1, Rdown = 1, Rup = 1, Snom = 1, Sdown = 1, Sup = 1):
        self.branchBuffers = {}
        self.branches = []

        #Mass scale
        self.branchBuffers['FatJet_msoftdrop_jmsUp'] = np.zeros(21, dtype=np.float32)
        self.branches.append({'name': 'FatJet_msoftdrop_jmsUp', 'formula': self.getBranch, 'arguments': 'FatJet_msoftdrop_jmsUp'})

        self.branchBuffers['FatJet_msoftdrop_jmsDown'] = np.zeros(21, dtype=np.float32)
        self.branches.append({'name': 'FatJet_msoftdrop_jmsDown', 'formula': self.getBranch, 'arguments': 'FatJet_msoftdrop_jmsDown'})

        self.Snom = Snom
        self.Sdown = Sdown
        self.Sup = Sup

        #Mass resolution (smearing)
        self.branchBuffers['FatJet_msoftdrop_jmrUp'] = np.zeros(21, dtype=np.float32)
        self.branches.append({'name': 'FatJet_msoftdrop_jmrUp', 'formula': self.getBranch, 'arguments': 'FatJet_msoftdrop_jmrUp'})

        self.branchBuffers['FatJet_msoftdrop_jmrDown'] = np.zeros(21, dtype=np.float32)
        self.branches.append({'name': 'FatJet_msoftdrop_jmrDown', 'formula': self.getBranch, 'arguments': 'FatJet_msoftdrop_jmrDown'})

        #data/MC scale factors for smearing
        self.Rnom = Rnom
        self.Rdown = Rdown
        self.Rup = Rup

        self.rnd = ROOT.TRandom3(12345)

    def customInit(self, initVars):

        self.config = initVars['config']
        self.sample = initVars['sample']

        #Load .root file with resolution.
        self.config = initVars['config']
        wdir = self.config.get('Directories', 'vhbbpath')
        filejmr = ROOT.TFile.Open(wdir+"/python/data/softdrop/puppiSoftdropResol.root","READ")
        self.puppisd_resolution_cen = filejmr.Get("massResolution_0eta1v3")
        self.puppisd_resolution_for = filejmr.Get("massResolution_1v3eta2v5")


    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getBranches(self):
        return self.branches

    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def processEvent(self, tree):


        # no Fat Jet
        if tree.Hbb_fjidx == -1:
            # Mass scale
            self.branchBuffers['FatJet_msoftdrop_jmsUp'][0]     = 1.0
            self.branchBuffers['FatJet_msoftdrop_jmsDown'][0]   = 1.0

            # Mass resolution 
            self.branchBuffers['FatJet_msoftdrop_jmrUp'][0]     = 1.0
            self.branchBuffers['FatJet_msoftdrop_jmrDown'][0]   = 1.0
        else:
            msoftdrop = tree.FatJet_msoftdrop[tree.Hbb_fjidx]
            
            # Mass scale
            self.branchBuffers['FatJet_msoftdrop_jmsUp'][0]     = msoftdrop*self.Sup
            self.branchBuffers['FatJet_msoftdrop_jmsDown'][0]   = msoftdrop*self.Sdown

            # Mass resolution 
            jmr_sys = self.get_msoftdrop_smear(tree.FatJet_pt[tree.Hbb_fjidx], tree.FatJet_eta[tree.Hbb_fjidx])
            self.branchBuffers['FatJet_msoftdrop_jmrDown'][0]   = msoftdrop*jmr_sys[0]
            self.branchBuffers['FatJet_msoftdrop_jmrUp'][0]     = msoftdrop*jmr_sys[1]

        return True

    def get_msoftdrop_smear(self, pt, eta):

        #get mass resolution
        massResolution = 0
        if eta <= 1.3:
            massResolution = self.puppisd_resolution_cen.Eval(pt)
        else: 
            massResolution = self.puppisd_resolution_for.Eval(pt)

        ###
        cup     = 1.
        cdown   = 1.
        r       = self.rnd.Gaus(0, massResolution - 1) 

        cup     = 1. + r*math.sqrt(max(self.Rup**2-1,0))
        cdown   = 1. + r*math.sqrt(max(self.Rdown**2-1,0))

        return [cup, cdown]
