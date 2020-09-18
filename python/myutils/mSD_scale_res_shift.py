#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np
from XbbConfig import XbbConfigTools

class mSD_scale_res_shift(AddCollectionsModule):

    def __init__(self, year = None):
        super(mSD_scale_res_shift, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ

        self.year = year if type(year) == str else str(year)
        self.scale_params = {
                 '2018': [0.9, 0.01, 0.9, 0.01],
                 }
        if self.year not in self.scale_params.keys():
            raise Exception('Please specify the year correspoding to the correction!')

        self.scale, self.scale_err, self.res, self.res_err = self.scale_params[self.year]

        self.scale_up   = self.scale + self.scale_err 
        self.scale_down = self.scale - self.scale_err 
        self.res_up     = self.res + self.res_err 
        self.res_down   = self.res - self.res_err 

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']
        self.config      = initVars['config']
        self.xbbConfig   = XbbConfigTools(self.config)
        self.systematics = self.xbbConfig.getJECuncertainties()
        self.systematicsBoosted = [x for x in self.systematics if 'jerReg' not in x] + ['jms', 'jmr']
        self.maxnFatJet   = 256

        if self.sample.isMC():

            self.FatJet_Msoftdrop         = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_nom     = array.array('f', [0.0]*self.maxnFatJet)

            self.sampleTree.tree.SetBranchAddress("FatJet_Msoftdrop", self.FatJet_Msoftdrop)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_nom", self.FatJet_msoftdrop_nom)

            #create backup branches
            self.addVectorBranch("FatJet_MsoftdropOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_MsoftdropOld[nFatJet]/F")
            self.addVectorBranch("FatJet_msoftdrop_nomOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_nomOld[nFatJet]/F")

            self.FatJet_msoftdrop_syst  = {}
            for syst in self.systematicsBoosted:
                self.FatJet_msoftdrop_syst[syst] = {}
                for Q in self._variations(syst):

                    self.FatJet_msoftdrop_syst[syst][Q]  = array.array('f', [0.0]*self.maxnFatJet)
                    self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_"+syst+Q, self.FatJet_msoftdrop_syst[syst][Q])
                    
                    #backup branches
                    self.addVectorBranch('FatJet_msoftdrop_'+syst+Q+'Old', default=0.0, branchType='f', length=self.maxnFatJet,leaflist='FatJet_msoftdrop_'+syst+Q+'Old[nFatJet]/F')

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
            
            nFatJet = tree.nFatJet

            if self.sample.isMC():
                for i in range(nFatJet):

                    #fill backup branches
                    self._b("FatJet_MsoftdropOld")[i]     = self.FatJet_Msoftdrop[i]
                    self._b("FatJet_msoftdrop_nomOld")[i]   = self.FatJet_msoftdrop_nom[i]

                    #overwrite branches
                    self.FatJet_Msoftdrop[i]     = self._b('FatJet_MsoftdropOld')[i]*self.scale
                    self.FatJet_msoftdrop_nom[i] = self._b("FatJet_msoftdrop_nomOld")[i]*self.scale

                    for syst in self.systematicsBoosted:
                        for Q in self._variations(syst):
                            
                            # fill backup branches
                            self._b("FatJet_msoftdrop_"+syst+Q+'Old')[i] = self.FatJet_msoftdrop_syst[syst][Q][i]

                            # overwrite branches
                            if syst=='jms':
                                if Q=='Up':
                                    self.FatJet_msoftdrop_syst[syst][Q][i] = self._b("FatJet_msoftdrop_nomOld")[i]*self.scale_up
                                else:
                                    self.FatJet_msoftdrop_syst[syst][Q][i] = self._b("FatJet_msoftdrop_nomOld")[i]*self.scale_down
                            elif syst=='jmr':
                                self.FatJet_msoftdrop_syst[syst][Q][i] = self._b("FatJet_msoftdrop_"+syst+Q+'Old')[i]*self.res

                            else:    
                                self.FatJet_msoftdrop_syst[syst][Q][i]  = self._b("FatJet_msoftdrop_"+syst+Q+'Old')[i]*self.scale

