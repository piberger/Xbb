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

# applies the smearing to MC jet resolution and modifies the Jet_PtReg* branches of the tree
class mSD_sys(AddCollectionsModule):

    def __init__(self, year = None, backupPreviousCorrection=True):
        super(mSD_sys, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.backupPreviousCorrection = backupPreviousCorrection
        self.quickloadWarningShown = False

        self.year = year if type(year) == str else str(year)
        self.scale_params = {
                 '2017': [0.93, 0.01, 0.93, 0.01],
                 '2016': [0.93, 0.01, 0.93, 0.01],
                 }
        if self.year not in self.scale_params:
            print("ERROR: smearing for year", self.year, " not available!")
            raise Exception("SmearingError")

        self.scale, self.scale_err, self.res, self.res_err = self.scale_params[self.year]

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']

        self.config = initVars['config']
        self.xbbConfig  = XbbConfigTools(self.config)
        self.jetSystematicsResolved = self.xbbConfig.getJECuncertainties()
        self.jetSystematics         = self.jetSystematicsResolved + ['jmr','jms']
        self.jetSystematics  = [e for e in self.jetSystematics if e not in {'jer', 'jerReg'}]
        #print(self.jetSystematics)

        if self.sample.isMC():
            # resolutions used in post-processor smearing
            self.maxnFatJet   = 256
            for jec in self.jetSystematics:
                setattr(self, "FatJet_msoftdrop_"+jec+"Up",array.array('f', [0.0]*self.maxnFatJet))
                setattr(self, "FatJet_msoftdrop_"+jec+"Down",array.array('f', [0.0]*self.maxnFatJet))
                
                self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_"+jec+"Up", getattr(self,"FatJet_msoftdrop_"+jec+"Up"))
                self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_"+jec+"Down", getattr(self,"FatJet_msoftdrop_"+jec+"Down"))

            self.FatJet_Msoftdrop                             = array.array('f', [0.0]*self.maxnFatJet)
            self.sampleTree.tree.SetBranchAddress("FatJet_Msoftdrop", self.FatJet_Msoftdrop)
            self.FatJet_msoftdrop_nom                          = array.array('f', [0.0]*self.maxnFatJet)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_nom", self.FatJet_msoftdrop_nom)


            if self.backupPreviousCorrection:

                for jec in self.jetSystematics:
                    self.addVectorBranch("FatJet_msoftdrop_"+jec+"Up"+"Old", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_"+jec+"Up[nJet]/F")
                    self.addVectorBranch("FatJet_msoftdrop_"+jec+"Down"+"Old", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_"+jec+"Down[nJet]/F")

                self.addVectorBranch("FatJet_MsoftdropOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_MsoftdropOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_nomOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_nomOld[nJet]/F")

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
            
            nJet = tree.nFatJet

            # backup the Jet_PtReg branches with the old smearing
            if self.backupPreviousCorrection:
                for i in range(nJet):
                    for jec in self.jetSystematics:
                        self._b("FatJet_msoftdrop_"+jec+"Up"+"Old")[i] = getattr(self,"FatJet_msoftdrop_"+jec+"Up")[i]
                        self._b("FatJet_msoftdrop_"+jec+"Down"+"Old")[i] = getattr(self,"FatJet_msoftdrop_"+jec+"Down")[i]
                    self._b("FatJet_MsoftdropOld")[i]                                = self.FatJet_Msoftdrop[i]
                    self._b("FatJet_msoftdrop_nomOld")[i]                            = self.FatJet_msoftdrop_nom[i]
           
            # apply new smearing
            for i in range(nJet):
                    scale_up   = self.scale + self.scale_err 
                    scale_down = self.scale - self.scale_err 
                    res_up     = self.res + self.res_err 
                    res_down   = self.res - self.res_err 

                    self.FatJet_Msoftdrop[i]                                = self.FatJet_Msoftdrop[i]*self.scale
                    self.FatJet_msoftdrop_nom[i]                            = self.FatJet_msoftdrop_nom[i]*self.scale

                    self.FatJet_msoftdrop_jmrUp[i]                          = self.FatJet_msoftdrop_jmrUp[i]*self.scale
                    self.FatJet_msoftdrop_jmrDown[i]                        = self.FatJet_msoftdrop_jmrDown[i]*self.scale
                    self.FatJet_msoftdrop_jmsUp[i]                          = self.FatJet_msoftdrop_jmsUp[i]*scale_up 
                    self.FatJet_msoftdrop_jmsDown[i]                        = self.FatJet_msoftdrop_jmsDown[i]*scale_down

                    for jec in self.jetSystematics:
                        if ((jec != "jmr") or (jec != "jms")):
                            getattr(self, "FatJet_msoftdrop_"+jec+"Up")[i] = getattr(self, "FatJet_msoftdrop_"+jec+"Up")[i]*self.scale
                            getattr(self, "FatJet_msoftdrop_"+jec+"Down")[i] = getattr(self, "FatJet_msoftdrop_"+jec+"Down")[i]*self.scale

                    #print("next jet")
                    #print("FatJet_MsoftdropiOld ",self._b("FatJet_MsoftdropOld")[i])
                    #print("FatJet_Msoftdrop ",self.FatJet_Msoftdrop[i]) 
                    #print("FatJet_msoftdrop_nom ",self.FatJet_msoftdrop_nom[i])
                    #print("FatJet_msoftdrop_jmrUp ",self.FatJet_msoftdrop_jmrUp[i])
                    #print("FatJet_msoftdrop_jmrUpOld ",self._b("FatJet_msoftdrop_jmrUpOld")[i])
                    #print("FatJet_msoftdrop_jmsUp ",self.FatJet_msoftdrop_jmsUp[i])
                    #print("FatJet_msoftdrop_jmsDown ",self.FatJet_msoftdrop_jmsDown[i])
            #print("---------------------------------------")
