#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np

class mSD_scale_res_shift(AddCollectionsModule):

    def __init__(self, year = None, backupPreviousCorrection=True):
        super(mSD_scale_res_shift, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.backupPreviousCorrection = backupPreviousCorrection

        self.year = year if type(year) == str else str(year)
        self.scale_params = {
                 '2018': [0.9, 0.01, 0.9, 0.01],
                 }

        self.scale, self.scale_err, self.res, self.res_err = self.scale_params[self.year]

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']

        if self.sample.isMC():
            self.maxnFatJet   = 256
            self.FatJet_Msoftdrop         = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_nom     = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmrUp   = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmrDown = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmsUp   = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmsDown = array.array('f', [0.0]*self.maxnFatJet)
            self.sampleTree.tree.SetBranchAddress("FatJet_Msoftdrop", self.FatJet_Msoftdrop)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_nom", self.FatJet_msoftdrop_nom)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmrUp", self.FatJet_msoftdrop_jmrUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmrDown", self.FatJet_msoftdrop_jmrDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmsUp", self.FatJet_msoftdrop_jmsUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmsDown", self.FatJet_msoftdrop_jmsDown)

            if self.backupPreviousCorrection:
                self.addVectorBranch("FatJet_MsoftdropOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_MsoftdropOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_nomOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_nomOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmrUpOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmrUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmrDownOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmrDownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmsUpOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmsUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmsDownOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmsDownOld[nJet]/F")

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
            
            nJet = tree.nFatJet

            if self.backupPreviousCorrection:
                for i in range(nJet):
                    self._b("FatJet_MsoftdropOld")[i]     = self.FatJet_Msoftdrop[i]
                    self._b("FatJet_msoftdrop_nomOld")[i]   = self.FatJet_msoftdrop_nom[i]
                    self._b("FatJet_msoftdrop_jmrUpOld")[i] = self.FatJet_msoftdrop_jmrUp[i]
                    self._b("FatJet_msoftdrop_jmrDownOld")[i] = self.FatJet_msoftdrop_jmrDown[i]
                    self._b("FatJet_msoftdrop_jmsUpOld")[i] = self.FatJet_msoftdrop_jmsUp[i]
                    self._b("FatJet_msoftdrop_jmsDownOld")[i] = self.FatJet_msoftdrop_jmsDown[i]

            for i in range(nJet):

                    scale_up   = self.scale + self.scale_err 
                    scale_down = self.scale - self.scale_err 
                    res_up     = self.res + self.res_err 
                    res_down   = self.res - self.res_err 

                    self.FatJet_Msoftdrop[i]         = self.FatJet_Msoftdrop[i]*self.scale
                    self.FatJet_msoftdrop_nom[i]     = self.FatJet_msoftdrop_nom[i]*self.scale
                    self.FatJet_msoftdrop_jmrUp[i]   = self.FatJet_msoftdrop_jmrUp[i]*self.scale
                    self.FatJet_msoftdrop_jmrDown[i] = self.FatJet_msoftdrop_jmrDown[i]*self.scale
                    self.FatJet_msoftdrop_jmsUp[i]   = self.FatJet_msoftdrop_jmsUp[i]*scale_up 
                    self.FatJet_msoftdrop_jmsDown[i] = self.FatJet_msoftdrop_jmsDown[i]*scale_down
