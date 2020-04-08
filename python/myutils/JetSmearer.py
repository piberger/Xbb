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
class JetSmearer(AddCollectionsModule):

    def __init__(self, year, unsmearPreviousCorrection=True, backupPreviousCorrection=True):
        super(JetSmearer, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.unsmearPreviousCorrection = unsmearPreviousCorrection
        self.backupPreviousCorrection = backupPreviousCorrection
        self.quickloadWarningShown = False

        self.year = year if type(year) == str else str(year)
        self.smear_params = {
                 '2016': [1.0, 0.0, 0.0, 0.0],
                 '2017': [1.0029846959, 0.0212893588055, 0.030684, 0.052497],
                 '2018': [0.98667384694, 0.0197153848807, 0.038481, 0.053924],
                 }
        if self.year not in self.smear_params:
            print("ERROR: smearing for year", self.year, " not available!")
            raise Exception("SmearingError")

        self.scale, self.scale_err, self.smear, self.smear_err = self.smear_params[self.year]

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']

        if self.sample.isMC():
            # resolutions used in post-processor smearing
            self.unsmearResNom  = 1.1
            self.unsmearResUp   = 1.2
            self.unsmearResDown = 1.0

            self.maxNjet   = 256
            self.PtReg     = array.array('f', [0.0]*self.maxNjet)
            self.PtRegUp   = array.array('f', [0.0]*self.maxNjet)
            self.PtRegDown = array.array('f', [0.0]*self.maxNjet)
            self.sampleTree.tree.SetBranchAddress("Jet_PtReg", self.PtReg)
            self.sampleTree.tree.SetBranchAddress("Jet_PtRegUp", self.PtRegUp)
            self.sampleTree.tree.SetBranchAddress("Jet_PtRegDown", self.PtRegDown)

            if self.backupPreviousCorrection:
                self.addVectorBranch("Jet_PtRegOld",     default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_PtRegOld[nJet]/F")
                self.addVectorBranch("Jet_PtRegOldUp",   default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_PtRegOldUp[nJet]/F")
                self.addVectorBranch("Jet_PtRegOldDown", default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_PtRegOldDown[nJet]/F")

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
            
            nJet = tree.nJet

            # backup the Jet_PtReg branches with the old smearing
            if self.backupPreviousCorrection:
                for i in range(nJet):
                    self._b("Jet_PtRegOld")[i]     = self.PtReg[i]
                    self._b("Jet_PtRegOldUp")[i]   = self.PtRegUp[i]
                    self._b("Jet_PtRegOldDown")[i] = self.PtRegDown[i]

            # original post-procesor smearing which is undone:
            # if isMC:
            #     # until we have final post-regression smearing factors we assume a flat 10%
            #     if sysVar==0: # nominal
            #        resSmear = 1.1
            #    elif sysVar==1: # up
            #        resSmear = 1.2
            #    elif sysVar==-1: # down
            #        resSmear = 1.0
            #    smearedPt = jet.pt*jet.bRegCorr 
            #    if jet.genJetIdx >=0 and  jet.genJetIdx < len(self.genJetsWithNeutrinos) :
            #        genJet=self.genJetsWithNeutrinos[jet.genJetIdx]
            #        dPt = smearedPt - genJet.Pt()
            #        smearedPt=genJet.Pt()+resSmear*dPt
            #    return smearedPt

            # undo old smearing
            if self.unsmearPreviousCorrection:
                for i in range(nJet):
                    genJetIdx = tree.Jet_genJetIdx[i]
                    if genJetIdx > -1 and genJetIdx < len(tree.GenJetWithNeutrinos_pt):
                        genJetPt = tree.GenJetWithNeutrinos_pt[genJetIdx]

                        self.PtReg[i]     = genJetPt + (self.PtReg[i] - genJetPt)/self.unsmearResNom
                        self.PtRegUp[i]   = genJetPt + (self.PtRegUp[i] - genJetPt)/self.unsmearResUp 
                        self.PtRegDown[i] = genJetPt + (self.PtRegDown[i] - genJetPt)/self.unsmearResDown

                    # after undoing the smearing, check if up/down variations are the same
                    assert (max(abs(self.PtReg[i]-self.PtRegUp[i]),abs(self.PtRegUp[i]-self.PtRegDown[i])) < 0.001 or self.PtReg[i] < 0)

            # apply new smearing
            for i in range(nJet):
                genJetIdx = tree.Jet_genJetIdx[i]
                if genJetIdx > -1 and genJetIdx < len(tree.GenJetWithNeutrinos_pt):
                    gen_pt    = tree.GenJetWithNeutrinos_pt[genJetIdx]

                    # reference: https://github.com/dabercro/hbb/blob/b86589128a6839a12efaf041f579fe88c1d1be38/nanoslimmer/applysmearing/applysmearing.py
                    regressed = self.PtReg[i]
                    no_smear  = regressed * self.scale
                    gen_diff  = regressed - gen_pt
                    nominal   = max(0.0, (gen_pt + gen_diff * (1.0 + self.smear)) * self.scale)
                    band      = math.sqrt(pow(nominal/self.scale * self.scale_err, 2) + pow(gen_diff * self.scale * self.smear_err, 2))

                    down, up  = (max(nominal - band, no_smear), nominal + band) if regressed > gen_pt else (min(nominal + band, no_smear), nominal - band)  

                    self.PtReg[i]     = nominal
                    self.PtRegUp[i]   = up
                    self.PtRegDown[i] = down


            # formulas by default reload the branch content when evaluating the first instance of the object!
            # SetQuickLoad(1) turns off this behavior
            for formulaName, treeFormula in self.sampleTree.formulas.items():
                if 'Jet_PtReg' in formulaName:
                    if not self.quickloadWarningShown:
                        self.quickloadWarningShown = True
                        print("INFO: SetQuickLoad(1) called for formula:", formulaName)
                        print("INFO: -> EvalInstance(0) on formulas will not re-load branches but will take values from memory, which might have been modified by this module.") 
                    treeFormula.SetQuickLoad(1)
                #    print("\x1b[31mERROR: this module can't be used together with others which use formulas based on branches changed inside this module!\x1b[0m")
                #    raise Exception("NotImplemented")


