#!/usr/bin/env python
import ROOT
import numpy as np
import array
from pdgId import pdgId
import sys

class VptWeightSimFit():

    def __init__(self, sample=None, nano=False):

        self.nano = nano
        self.branchBuffers = {}
        self.branches = []
        self.branchBuffers['FitCorrVpt'] = np.ones(3, dtype=np.float32)
        self.branches.append({'name': 'FitCorrVpt', 'formula': self.getVectorBranch, 'arguments': {'branch': 'FitCorrVpt', 'length':3}, 'length': 3})

        if sample:
            self.customInit(sample=sample)

    def customInit(self, initVars):
        sample = initVars['sample']
        self.config = initVars['config']
        self.dataset = self.config.get('General','dataset')
        
        #get slope
        self.tt_nom      = eval(self.config.get('Sys','tt_nom_Vpt'))
        self.tt_up       = self.tt_nom + eval(self.config.get('Sys','tt_uncert_Vpt'))
        self.tt_down     = self.tt_nom - eval(self.config.get('Sys','tt_uncert_Vpt'))

        self.whf_nom     = eval(self.config.get('Sys','whf_nom_Vpt'))
        self.whf_up      = self.whf_nom + eval(self.config.get('Sys','whf_uncert_Vpt'))
        self.whf_down    = self.whf_nom - eval(self.config.get('Sys','whf_uncert_Vpt'))

        self.wlf_nom     = eval(self.config.get('Sys','wlf_nom_Vpt'))
        self.wlf_up      = self.wlf_nom + eval(self.config.get('Sys','wlf_uncert_Vpt'))
        self.wlf_down    = self.wlf_nom - eval(self.config.get('Sys','wlf_uncert_Vpt'))

        #get doubleB boundary
        self.Vptlow = eval(self.config.get('Sys','Vptlow'))

        #get normalisation factor for linear correction
        self.norm_tt_nominal  = self.getVptNorm(self.tt_nom)
        self.norm_tt_up       = self.getVptNorm(self.tt_up)
        self.norm_tt_down     = self.getVptNorm(self.tt_down)
        self.norm_whf_nominal  = self.getVptNorm(self.whf_nom)
        self.norm_whf_up       = self.getVptNorm(self.whf_up)
        self.norm_whf_down     = self.getVptNorm(self.whf_down)
        self.norm_wlf_nominal  = self.getVptNorm(self.wlf_nom)
        self.norm_wlf_up       = self.getVptNorm(self.wlf_up)
        self.norm_wlf_down     = self.getVptNorm(self.wlf_down)
        
        self.isData = sample.type == 'DATA'
        self.identifier = sample.identifier
        if self.isData:
            self.branches = []

    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        #print 'arguments are', arguments
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):
        if self.isData:
            return True 
        else:
            #no Fat Jet
            if tree.Hbb_fjidx == -1:
                self.branchBuffers['FitCorrVpt'][0] = 1.0
                self.branchBuffers['FitCorrVpt'][1] = 1.0
                self.branchBuffers['FitCorrVpt'][2] = 1.0
                return True

            CorrFactor = [1, 1, 1]
            Vpt = tree.V_pt
            sample_ = None

            ####
            ##TT
            ####
            if 'TT' in self.identifier:
                sample_ = 'tt'
            if 'ST' in self.identifier:
                sample_ = 'whf'
                
            elif ('WJets' in self.identifier or 'WBJets' in self.identifier ):
                count = 0

                for i in range(tree.nGenJet):
                    if tree.GenJet_pt[i]>20 and abs(tree.GenJet_eta[i])<2.4 and  tree.GenJet_hadronFlavour[i]==5:
                        count += 1
                ####
                ##Whf
                ####
                if count >= 1:
                    sample_ = 'whf'

                ####
                ##Wlf
                ####
                else: 
                    sample_ = 'wlf'


            if sample_:
                CorrFactor =  [
                    self.getVptweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_nom'%sample_),Vpt),
                    self.getVptweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_down'%sample_),Vpt),
                    self.getVptweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_up'%sample_),Vpt)
                    ]
         
        self.branchBuffers['FitCorrVpt'][0] = CorrFactor[0]
        self.branchBuffers['FitCorrVpt'][1] = CorrFactor[1]
        self.branchBuffers['FitCorrVpt'][2] = CorrFactor[2]

        return True 

    def getVptNorm(self, slope):
        d = self.Vptlow
        norm = 1 - slope*self.Vptlow
        return norm

    def getVptweight(self, norm, slope, Vpt):
        weight = norm + slope*Vpt
        return weight
