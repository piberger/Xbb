#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np

# applies the smearing to MC jet resolution and modifies the Jet_PtReg* branches of the tree
class mSD_sys_2017(AddCollectionsModule):

    def __init__(self, year = None, backupPreviousCorrection=True):
        super(mSD_sys_2017, self).__init__()
        self.version = 2
        self.debug = 'XBBDEBUG' in os.environ
        self.backupPreviousCorrection = backupPreviousCorrection
        self.backupPreviousCorrection = False
        self.quickloadWarningShown = False

        self.year = year if type(year) == str else str(year)
        self.scale_params = {
                 '2017': [0.93, 0.01, 0.93, 0.01],
                 }
        self.applyToNtupleVersions = ['V13']
        self.active = False

        #if self.year not in self.smear_params:
        #    print("ERROR: smearing for year", self.year, " not available!")
        #    raise Exception("SmearingError")

        self.scale, self.scale_err, self.res, self.res_err = self.scale_params[self.year]

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']
        self.config = initVars['config']

        if self.config.get('General','nTupleVersion') in self.applyToNtupleVersions:
            self.active = True
            print("INFO: soft-drop mass correction is active!")
        else:
            self.active = False
            print("INFO: soft-drop mass correction is NOT active!")

        if self.sample.isMC() and self.active:
            # resolutions used in post-processor smearing
            self.maxnFatJet   = 256
            self.FatJet_Msoftdrop                             = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_nom                         = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmrUp                       = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmrDown                     = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmsUp                       = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jmsDown                     = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesAbsoluteUp               = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesAbsoluteDown             = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesAbsolute_2017Up          = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesAbsolute_2017Down        = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesBBEC1Up                  = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesBBEC1Down                = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesBBEC1_2017Up             = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesBBEC1_2017Down           = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesEC2Up                    = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesEC2Down                  = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesEC2_2017Up               = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesEC2_2017Down             = array.array('f', [0.0]*self.maxnFatJet)            
            self.FatJet_msoftdrop_jesFlavorQCDUp              = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesFlavorQCDDown            = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesHFUp                     = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesHFDown                   = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesHF_2017Up                = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesHF_2017Down              = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesRelativeBalUp            = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesRelativeBalDown          = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesRelativeSample_2017Up    = array.array('f', [0.0]*self.maxnFatJet)
            self.FatJet_msoftdrop_jesRelativeSample_2017Down  = array.array('f', [0.0]*self.maxnFatJet)


            self.sampleTree.tree.SetBranchAddress("FatJet_Msoftdrop", self.FatJet_Msoftdrop)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_nom", self.FatJet_msoftdrop_nom)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmrUp", self.FatJet_msoftdrop_jmrUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmrDown", self.FatJet_msoftdrop_jmrDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmsUp", self.FatJet_msoftdrop_jmsUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jmsDown", self.FatJet_msoftdrop_jmsDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesAbsoluteUp", self.FatJet_msoftdrop_jesAbsoluteUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesAbsoluteDown", self.FatJet_msoftdrop_jesAbsoluteDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesAbsolute_2017Up", self.FatJet_msoftdrop_jesAbsolute_2017Up)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesAbsolute_2017Down", self.FatJet_msoftdrop_jesAbsolute_2017Down)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesBBEC1Up", self.FatJet_msoftdrop_jesBBEC1Up)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesBBEC1Down", self.FatJet_msoftdrop_jesBBEC1Down)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesBBEC1_2017Up", self.FatJet_msoftdrop_jesBBEC1_2017Up)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesBBEC1_2017Down", self.FatJet_msoftdrop_jesBBEC1_2017Down)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesFlavorQCDUp", self.FatJet_msoftdrop_jesFlavorQCDUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesFlavorQCDDown", self.FatJet_msoftdrop_jesFlavorQCDDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesHFUp", self.FatJet_msoftdrop_jesHFUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesHFDown", self.FatJet_msoftdrop_jesHFDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesHF_2017Up", self.FatJet_msoftdrop_jesHF_2017Up)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesHF_2017Down", self.FatJet_msoftdrop_jesHF_2017Down)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesRelativeBalUp", self.FatJet_msoftdrop_jesRelativeBalUp)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesRelativeBalDown", self.FatJet_msoftdrop_jesRelativeBalDown)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesRelativeSample_2017Up", self.FatJet_msoftdrop_jesRelativeSample_2017Up)
            self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_jesRelativeSample_2017Down", self.FatJet_msoftdrop_jesRelativeSample_2017Down)
      


            if self.backupPreviousCorrection:
                self.addVectorBranch("FatJet_MsoftdropOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_MsoftdropOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_nomOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_nomOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmrUpOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmrUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmrDownOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmrDownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmsUpOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmsUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jmsDownOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmsDownOld[nJet]/F")
                #self.addVectorBranch("FatJet_msoftdrop_jmsDownOld",     default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jmsDownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesAbsoluteUpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesAbsoluteUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesAbsoluteDownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesAbsoluteDownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesAbsolute_2017UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesAbsolute_2017UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesAbsolute_2017DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesAbsolute_2017DownOld[nJet]/F")

                self.addVectorBranch("FatJet_msoftdrop_jesBBEC1UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesBBEC1UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesBBEC1DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesBBEC1DownOld[nJet]/F") 
                self.addVectorBranch("FatJet_msoftdrop_jesBBEC1_2017UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesBBEC1_2017UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesBBEC1_2017DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesBBEC1_2017DownOld[nJet]/F")


                self.addVectorBranch("FatJet_msoftdrop_jesEC2UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesEC2UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesEC2DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesEC2DownOld[nJet]/F")

            
                self.addVectorBranch("FatJet_msoftdrop_jesEC2_2017UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesEC2_2017UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesEC2_2017DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesEC2_2017DownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesFlavorQCDUpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesFlavorQCDUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesFlavorQCDDownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesFlavorQCDDownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesHFUpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesHFUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesHFDownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesHFDownOld[nJet]/F")

                self.addVectorBranch("FatJet_msoftdrop_jesHF_2017UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesHF_2017UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesHF_2017DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesHF_2017DownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesRelativeBalUpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesRelativeBalUpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesRelativeBalDownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesRelativeBalDownOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesRelativeSample_2017UpOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesRelativeSample_2017UpOld[nJet]/F")
                self.addVectorBranch("FatJet_msoftdrop_jesRelativeSample_2017DownOld", default=0.0, branchType='f', length=self.maxnFatJet, leaflist="FatJet_msoftdrop_jesRelativeSample_2017DownOld[nJet]/F")

            


    def processEvent(self, tree):
        if self.active and not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
            
            nJet = tree.nFatJet

            # backup the Jet_PtReg branches with the old smearing
            if self.backupPreviousCorrection:
                for i in range(nJet):
                    self._b("FatJet_MsoftdropOld")[i]                                = self.FatJet_Msoftdrop[i]
                    self._b("FatJet_msoftdrop_nomOld")[i]                            = self.FatJet_msoftdrop_nom[i]
                    self._b("FatJet_msoftdrop_jmrUpOld")[i]                          = self.FatJet_msoftdrop_jmrUp[i]
                    self._b("FatJet_msoftdrop_jmrDownOld")[i]                        = self.FatJet_msoftdrop_jmrDown[i]
                    self._b("FatJet_msoftdrop_jmsUpOld")[i]                          = self.FatJet_msoftdrop_jmsUp[i]
                    self._b("FatJet_msoftdrop_jmsDownOld")[i]                        = self.FatJet_msoftdrop_jmsDown[i]
                    self._b("FatJet_msoftdrop_jesAbsoluteUpOld")[i]                  = self.FatJet_msoftdrop_jesAbsoluteUp[i]
                    self._b("FatJet_msoftdrop_jesAbsoluteUpOld")[i]                  = self.FatJet_msoftdrop_jesAbsoluteDown[i]
                    self._b("FatJet_msoftdrop_jesAbsolute_2017UpOld")[i]             = self.FatJet_msoftdrop_jesAbsolute_2017Up[i]
                    self._b("FatJet_msoftdrop_jesAbsolute_2017DownOld")[i]           = self.FatJet_msoftdrop_jesAbsolute_2017Down[i]
                    self._b("FatJet_msoftdrop_jesBBEC1UpOld")[i]                     = self.FatJet_msoftdrop_jesBBEC1Up[i]
                    self._b("FatJet_msoftdrop_jesBBEC1DownOld")[i]                   = self.FatJet_msoftdrop_jesBBEC1Down[i]
                    self._b("FatJet_msoftdrop_jesBBEC1_2017UpOld")[i]                = self.FatJet_msoftdrop_jesBBEC1_2017Up[i] 
                    self._b("FatJet_msoftdrop_jesBBEC1_2017DownOld")[i]              = self.FatJet_msoftdrop_jesBBEC1_2017Down[i] 
                    self._b("FatJet_msoftdrop_jesEC2UpOld")[i]                       = self.FatJet_msoftdrop_jesEC2Up[i] 
                    self._b("FatJet_msoftdrop_jesEC2DownOld")[i]                     = self.FatJet_msoftdrop_jesEC2Down[i] 
                    self._b("FatJet_msoftdrop_jesEC2_2017UpOld")[i]                  = self.FatJet_msoftdrop_jesEC2_2017Up[i] 
                    self._b("FatJet_msoftdrop_jesEC2_2017DownOld")[i]                = self.FatJet_msoftdrop_jesEC2_2017Down[i] 
                    self._b("FatJet_msoftdrop_jesFlavorQCDUpOld")[i]                 = self.FatJet_msoftdrop_jesFlavorQCDUp[i] 
                    self._b("FatJet_msoftdrop_jesFlavorQCDDownOld")[i]               = self.FatJet_msoftdrop_jesFlavorQCDDown[i] 
                    self._b("FatJet_msoftdrop_jesHFUpOld")[i]                        = self.FatJet_msoftdrop_jesHFUp[i] 
                    self._b("FatJet_msoftdrop_jesHFDownOld")[i]                      = self.FatJet_msoftdrop_jesHFDown[i] 
                    self._b("FatJet_msoftdrop_jesHF_2017UpOld")[i]                   = self.FatJet_msoftdrop_jesHF_2017Up[i] 
                    self._b("FatJet_msoftdrop_jesHF_2017DownOld")[i]                 = self.FatJet_msoftdrop_jesHF_2017Down[i] 
                    self._b("FatJet_msoftdrop_jesRelativeBalUpOld")[i]               = self.FatJet_msoftdrop_jesRelativeBalUp[i] 
                    self._b("FatJet_msoftdrop_jesRelativeBalDownOld")[i]             = self.FatJet_msoftdrop_jesRelativeBalDown[i] 
                    self._b("FatJet_msoftdrop_jesRelativeSample_2017UpOld")[i]       = self.FatJet_msoftdrop_jesRelativeSample_2017Up[i] 
                    self._b("FatJet_msoftdrop_jesRelativeSample_2017DownOld")[i]     = self.FatJet_msoftdrop_jesRelativeSample_2017Down[i] 



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
                    #self.FatJet_msoftdrop_jmsUp[i]                          = self.FatJet_msoftdrop_jmsUp[i]*self.scale*self.scale_err 
                    self.FatJet_msoftdrop_jmsUp[i]                          = self.FatJet_msoftdrop_jmsUp[i]*scale_up 
                    #self.FatJet_msoftdrop_jmsDown[i]                        = self.FatJet_msoftdrop_jmsDown[i]*self.scale*self.scale_err
                    self.FatJet_msoftdrop_jmsDown[i]                        = self.FatJet_msoftdrop_jmsDown[i]*scale_down
                    self.FatJet_msoftdrop_jesAbsoluteUp[i]                  = self.FatJet_msoftdrop_jesAbsoluteUp[i]*self.scale
                    self.FatJet_msoftdrop_jesAbsoluteDown[i]                = self.FatJet_msoftdrop_jesAbsoluteDown[i]*self.scale
                    self.FatJet_msoftdrop_jesAbsolute_2017Up[i]             = self.FatJet_msoftdrop_jesAbsolute_2017Up[i]*self.scale
                    self.FatJet_msoftdrop_jesAbsolute_2017Down[i]           = self.FatJet_msoftdrop_jesAbsolute_2017Down[i]*self.scale
                    self.FatJet_msoftdrop_jesBBEC1Up[i]                     = self.FatJet_msoftdrop_jesBBEC1Up[i]*self.scale
                    self.FatJet_msoftdrop_jesBBEC1Down[i]                   = self.FatJet_msoftdrop_jesBBEC1Down[i]*self.scale
                    self.FatJet_msoftdrop_jesBBEC1_2017Up[i]                = self.FatJet_msoftdrop_jesBBEC1_2017Up[i]*self.scale 
                    self.FatJet_msoftdrop_jesBBEC1_2017Down[i]              = self.FatJet_msoftdrop_jesBBEC1_2017Down[i]*self.scale 
                    self.FatJet_msoftdrop_jesEC2Up[i]                       = self.FatJet_msoftdrop_jesEC2Up[i]*self.scale 
                    self.FatJet_msoftdrop_jesEC2Down[i]                     = self.FatJet_msoftdrop_jesEC2Down[i]*self.scale 
                    self.FatJet_msoftdrop_jesEC2_2017Up[i]                  = self.FatJet_msoftdrop_jesEC2_2017Up[i]*self.scale 
                    self.FatJet_msoftdrop_jesEC2_2017Down[i]                = self.FatJet_msoftdrop_jesEC2_2017Down[i]*self.scale 
                    self.FatJet_msoftdrop_jesFlavorQCDUp[i]                 = self.FatJet_msoftdrop_jesFlavorQCDUp[i]*self.scale 
                    self.FatJet_msoftdrop_jesFlavorQCDDown[i]               = self.FatJet_msoftdrop_jesFlavorQCDDown[i]*self.scale 
                    self.FatJet_msoftdrop_jesHFUp[i]                        = self.FatJet_msoftdrop_jesHFUp[i]*self.scale 
                    self.FatJet_msoftdrop_jesHFDown[i]                      = self.FatJet_msoftdrop_jesHFDown[i]*self.scale 
                    self.FatJet_msoftdrop_jesHF_2017Up[i]                   = self.FatJet_msoftdrop_jesHF_2017Up[i]*self.scale 
                    self.FatJet_msoftdrop_jesHF_2017Down[i]                 = self.FatJet_msoftdrop_jesHF_2017Down[i]*self.scale 
                    self.FatJet_msoftdrop_jesRelativeBalUp[i]               = self.FatJet_msoftdrop_jesRelativeBalUp[i]*self.scale 
                    self.FatJet_msoftdrop_jesRelativeBalDown[i]             = self.FatJet_msoftdrop_jesRelativeBalDown[i]*self.scale 
                    self.FatJet_msoftdrop_jesRelativeSample_2017Up[i]       = self.FatJet_msoftdrop_jesRelativeSample_2017Up[i]*self.scale 
                    self.FatJet_msoftdrop_jesRelativeSample_2017Down[i]     = self.FatJet_msoftdrop_jesRelativeSample_2017Down[i]*self.scale 





                    #print("next jet")
                    #print("FatJet_MsoftdropiOld ",self._b("FatJet_MsoftdropOld")[i])
                    #print("FatJet_Msoftdrop ",self.FatJet_Msoftdrop[i]) 
                    #print("FatJet_msoftdrop_nom ",self.FatJet_msoftdrop_nom[i])
                    #print("FatJet_msoftdrop_jmrUp ",self.FatJet_msoftdrop_jmrUp[i])
                    #print("FatJet_msoftdrop_jmrUpOld ",self._b("FatJet_msoftdrop_jmrUpOld")[i])
                    #print("FatJet_msoftdrop_jmsUp ",self.FatJet_msoftdrop_jmsUp[i])
                    #print("FatJet_msoftdrop_jmsDown ",self.FatJet_msoftdrop_jmsDown[i])
            #print("---------------------------------------")
