#!/usr/bin/env python
import ROOT
import numpy as np
import array
from pdgId import pdgId
import sys

class DoubleBTagWeightsSimFit(object):

    def __init__(self, sample=None, nano=False):

        self.nano = nano
        self.branchBuffers = {}
        self.branches = []
        self.branchBuffers['FitCorrBTag'] = np.ones(3, dtype=np.float32)
        self.branches.append({'name': 'FitCorrBTag', 'formula': self.getVectorBranch, 'arguments': {'branch': 'FitCorrBTag', 'length':3}, 'length': 3})

        if sample:
            self.customInit(sample=sample)

    def customInit(self, initVars):
        sample = initVars['sample']
        self.config = initVars['config']
        self.dataset = self.config.get('General','dataset')
        
        #get slope
        self.tt_nom      = eval(self.config.get('Sys','tt_nom'))
        self.tt_up       = self.tt_nom + eval(self.config.get('Sys','tt_uncert'))
        self.tt_down     = self.tt_nom - eval(self.config.get('Sys','tt_uncert'))

        self.vvl_nom     = eval(self.config.get('Sys','vvl_nom'))
        self.vvl_up      = self.vvl_nom + eval(self.config.get('Sys','vvl_uncert'))
        self.vvl_down    = self.vvl_nom - eval(self.config.get('Sys','vvl_uncert'))

        self.whf_nom     = eval(self.config.get('Sys','whf_nom'))
        self.whf_up      = self.whf_nom + eval(self.config.get('Sys','whf_uncert'))
        self.whf_down    = self.whf_nom - eval(self.config.get('Sys','whf_uncert'))

        self.wlf_nom     = eval(self.config.get('Sys','wlf_nom'))
        self.wlf_up      = self.wlf_nom + eval(self.config.get('Sys','wlf_uncert'))
        self.wlf_down    = self.wlf_nom - eval(self.config.get('Sys','wlf_uncert'))

        #get doubleB boundary
        self.doubleBlow  = eval(self.config.get('Sys','doubleBlow'))
        self.doubleBhigh = eval(self.config.get('Sys','doubleBhigh'))

        #get normalisation factor for linear correction
        self.norm_tt_nominal  = self.getDoubleBNorm(self.tt_nom)
        self.norm_tt_up       = self.getDoubleBNorm(self.tt_up)
        self.norm_tt_down     = self.getDoubleBNorm(self.tt_down)
        self.norm_vvl_nominal  = self.getDoubleBNorm(self.vvl_nom)
        self.norm_vvl_up       = self.getDoubleBNorm(self.vvl_up)
        self.norm_vvl_down     = self.getDoubleBNorm(self.vvl_down)
        self.norm_whf_nominal  = self.getDoubleBNorm(self.whf_nom)
        self.norm_whf_up       = self.getDoubleBNorm(self.whf_up)
        self.norm_whf_down     = self.getDoubleBNorm(self.whf_down)
        self.norm_wlf_nominal  = self.getDoubleBNorm(self.wlf_nom)
        self.norm_wlf_up       = self.getDoubleBNorm(self.wlf_up)
        self.norm_wlf_down     = self.getDoubleBNorm(self.wlf_down)
        
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
                self.branchBuffers['FitCorrBTag'][0] = 1.0
                self.branchBuffers['FitCorrBTag'][1] = 1.0
                self.branchBuffers['FitCorrBTag'][2] = 1.0
                return True

            CorrFactor = [1, 1, 1]
            doubleB = tree.FatJet_btagHbb[tree.Hbb_fjidx]

            ####
            ##TT
            ####
            if 'TT' in self.identifier or 'ST' in self.identifier:
                sample_ = 'tt'
                CorrFactor =  [
                    self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_nom'%sample_),doubleB),
                    self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_down'%sample_),doubleB),
                    self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_up'%sample_),doubleB)
                    ]
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
                    CorrFactor =  [
                        self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_nom'%sample_),doubleB),
                        self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_down'%sample_),doubleB),
                        self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_up'%sample_),doubleB)
                        ]
                ####
                ##Wlf
                ####
                else: 
                    sample_ = 'wlf'
                    CorrFactor =  [
                        self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_nom'%sample_),doubleB),
                        self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_down'%sample_),doubleB),
                        self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_up'%sample_),doubleB)
                        ]
            elif 'ZZ' in self.identifier or 'WW' in self.identifier or 'WZ' in self.identifier:
                sample_ = 'vvl'
                CorrFactor =  [
                    self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_nom'%sample_),doubleB),
                    self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_down'%sample_),doubleB),
                    self.getDoubleBweight(getattr(self,'norm_%s_nominal'%sample_),getattr(self,'%s_up'%sample_),doubleB)
                    ]
         
        self.branchBuffers['FitCorrBTag'][0] = CorrFactor[0]
        self.branchBuffers['FitCorrBTag'][1] = CorrFactor[1]
        self.branchBuffers['FitCorrBTag'][2] = CorrFactor[2]

        #print 'doubleB is', doubleB
        #print 'sample is', self.identifier 
        #print 'FitCorrBTag is', CorrFactor
        #import sys
        #sys.exit()

        return True 

    def getDoubleBNorm(self, slope):
        d = self.doubleBlow 
        u = self.doubleBhigh
        f_d = 1 + slope*d
        f_u = 1 + slope*u
        #norm = (u-d)*(1 + 0.5*(f_u - f_d))
        norm = (1 + 0.5*(f_u - f_d)*(u+d)/(u-d))
        #print 'u is', u
        #print 'd is', d
        #print 'f_d is', f_d
        #print 'f_u is', f_u
        #print 'norm is', norm
        #sys.exit()
        return 1./norm

    def getDoubleBweight(self, norm, slope, doublB):
        #print 'slope', slope
        #print 'norm', norm
        weight = norm*(1 + slope*doublB)
        return weight
