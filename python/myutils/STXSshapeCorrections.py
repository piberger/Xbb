#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np
from XbbConfig import XbbConfigTools
import time
from XbbConfig import XbbConfigReader, XbbConfigTools
from sample_parser import ParseInfo
from BranchList import BranchList
from FileLocator import FileLocator
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double
from sampleTree import SampleTree
import copy
import csv

# calculates the STXS acceptance uncertainties (shape) based on the STXS bin in Vpt and NJet  
class STXSshapeCorrections(AddCollectionsModule):

    def __init__(self, year):
        super(STXSshapeCorrections, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.quickloadWarningShown = False
        self.existingBranches = {}

        self.year = year if type(year) == str else str(year)

    def addBranch(self, branchName, default=0.0):
        if branchName not in self.existingBranches:
            super(STXSshapeCorrections, self).addBranch(branchName, default)
        else:
            print("DEBUG: skip adding branch:", branchName)

    # can be used to overwrite branch if it already exists
    def _b(self, branchName):
        if branchName not in self.existingBranches:
            return super(STXSshapeCorrections, self)._b(branchName)
        else:
            return self.existingBranches[branchName]

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        self.config = initVars['config']

        self.corrections = {
        "ZH": {
        "FORWARD": 0.0,
        "PTV_0_75_0J": 0.028,
        "PTV_0_75_1J": 0.08450443775,
        "PTV_0_75_GE2J": 0.1294951737,
        "PTV_75_150_0J": 0.035,
        "PTV_75_150_1J": 0.08202438662,
        "PTV_75_150_GE2J": 0.1182074448,
        "PTV_150_250_0J": 0.0,
        "PTV_150_250_1J": 0.08156592426,
        "PTV_150_250_GE2J": 0.1053090689,
        "PTV_250_400_0J": 0.05714017851,
        "PTV_250_400_1J": 0.08297590012,
        "PTV_250_400_GE2J": 0.09471008394,
        "PTV_GT400_0J": 0.07462010453,
        "PTV_GT400_1J": 0.09067061266,
        "PTV_GT400_GE2J": 0.09588618253,
        },

        "WH": {
        "FORWARD": 0.0,
        "PTV_0_75_0J": 0.026,
        "PTV_0_75_1J": 0.07440430095,
        "PTV_0_75_GE2J": 0.1115168149,
        "PTV_75_150_0J": 0.031,
        "PTV_75_150_1J": 0.07083784299,
        "PTV_75_150_GE2J": 0.1001698557,
        "PTV_150_250_0J": 0.039,
        "PTV_150_250_1J": 0.07071067812,
        "PTV_150_250_GE2J": 0.09013878189,
        "PTV_250_400_0J": 0.05315072906,
        "PTV_250_400_1J": 0.07438413809,
        "PTV_250_400_GE2J": 0.08614522622,
        "PTV_GT400_0J": 0.07049794323,
        "PTV_GT400_1J": 0.08549830408,
        "PTV_GT400_GE2J": 0.09203781831,
        },

        "ggZH": {
        "FORWARD": 0.0,
        "PTV_0_75_0J": 0.391,
        "PTV_0_75_1J": 0.3115541686,
        "PTV_0_75_GE2J": 0.3620414341,
        "PTV_75_150_0J": 0.364,
        "PTV_75_150_1J": 0.3137036818,
        "PTV_75_150_GE2J": 0.3719381669,
        "PTV_150_250_0J": 0.0,
        "PTV_150_250_1J": 0.3587659404,
        "PTV_150_250_GE2J": 0.3910306893,
        "PTV_250_400_0J": 0.9002005332,
        "PTV_250_400_1J": 0.5260446749,
        "PTV_250_400_GE2J": 0.4225849027,
        "PTV_GT400_0J": 0.9155457389,
        "PTV_GT400_1J": 0.896829972,
        "PTV_GT400_GE2J": 0.896829972,
        }
        }

        self.STXSname = {
        0: "FORWARD", # used for events with Higgs rapidity > 2.5 where we have very little acceptance, so it doent matter which values we put here (use default)
        1: "PTV_0_75_0J",
        2: "PTV_75_150_0J",
        3: "PTV_150_250_0J",
        4: "PTV_250_400_0J",
        5: "PTV_GT400_0J",
        6: "PTV_0_75_1J",
        7: "PTV_75_150_1J",
        8: "PTV_150_250_1J",
        9: "PTV_250_400_1J",
        10: "PTV_GT400_1J",
        11: "PTV_0_75_GE2J",
        12: "PTV_75_150_GE2J",
        13: "PTV_150_250_GE2J",
        14: "PTV_250_400_GE2J",
        15: "PTV_GT400_GE2J",
        }

        if self.sample.isMC():

            # load needed information
            self.existingBranches["HTXS_stage1_1_fine_cat_pTjet30GeV"] = array.array('i', [0])
            self.sampleTree.tree.SetBranchAddress("HTXS_stage1_1_fine_cat_pTjet30GeV", self.existingBranches["HTXS_stage1_1_fine_cat_pTjet30GeV"])

            self.addBranch("THU_ZH_accUp", default=1.0)
            self.addBranch("THU_ZH_accDown", default=1.0)
            self.addBranch("THU_WH_accUp", default=1.0)
            self.addBranch("THU_WH_accDown", default=1.0)
            self.addBranch("THU_ggZH_accUp", default=1.0)
            self.addBranch("THU_ggZH_accDown", default=1.0)
                    
    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)

            # check for WH sample
            if (self.sample.index == -12501) or (self.sample.index == -12500):
                STXSname = self.STXSname[self.existingBranches["HTXS_stage1_1_fine_cat_pTjet30GeV"][0]-300]
                self._b("THU_WH_accUp")[0] = 1.0 + self.corrections["WH"][STXSname] 
                self._b("THU_WH_accDown")[0] = 1.0 - self.corrections["WH"][STXSname] 

            # check for ZH sample
            elif (self.sample.index == -12502) or (self.sample.index == -12504):
                STXSname = self.STXSname[self.existingBranches["HTXS_stage1_1_fine_cat_pTjet30GeV"][0]-400]
                self._b("THU_ZH_accUp")[0] = 1.0 + self.corrections["ZH"][STXSname] 
                self._b("THU_ZH_accDown")[0] = 1.0 - self.corrections["ZH"][STXSname]
  
            # check for ggZH sample
            elif (self.sample.index == -12503) or (self.sample.index == -12505):
                STXSname = self.STXSname[self.existingBranches["HTXS_stage1_1_fine_cat_pTjet30GeV"][0]-500]
                self._b("THU_ggZH_accUp")[0] = 1.0 + self.corrections["ggZH"][STXSname] 
                self._b("THU_ggZH_accDown")[0] = 1.0 - self.corrections["ggZH"][STXSname]

            #print(self._b("THU_WH_accUp")[0])
            #print(self._b("THU_WH_accDown")[0])

            #print(self._b("THU_ZH_accUp")[0])
            #print(self._b("THU_ZH_accDown")[0])

            #print(self._b("THU_ggZH_accUp")[0])        
            #print(self._b("THU_ggZH_accDown")[0])        


if __name__=='__main__':

    print("main")

    config = XbbConfigReader.read('Zvv2016')
    info = ParseInfo(config=config)
    sample = [x for x in info if x.identifier == 'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8'][0]

    sampleTree = SampleTree(['/pnfs/psi.ch/cms/trivcat/store/user/creissel/VHbb/Zvv/VHbbPostNano2016_V11/2020_11_01/eval_boostedVZ/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/tree_0daeeaa419203ed1ca7bc5b1abb63105e5eb6c93e2e4032c8d9dbf4f_000000_000000_0000_6_365ec88febcb9c2a9f97b3c92a920f8ba2b348d0651e246ceee1770a.root'], treeName='Events', xrootdRedirector="root://t3dcachedb03.psi.ch:1094/")
    w = STXSshapeCorrections("2016")
    w.customInit({'sampleTree': sampleTree, 'sample': sample, 'config': config})
    sampleTree.addOutputBranches(w.getBranches())

    n=0
    for event in sampleTree:
        print(event)
        event,run = w.processEvent(event)

