#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np
from XbbConfig import XbbConfigReader
from sampleTree import SampleTree 
from sample_parser import ParseInfo
import BetterConfigParser

# applies the smearing to MC jet resolution and modifies the Jet_PtReg* branches of the tree
class JetSmearer(AddCollectionsModule):

    def __init__(self, year, unsmearPreviousCorrection=True, backupPreviousCorrection=True):
        super(JetSmearer, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.unsmearPreviousCorrection = unsmearPreviousCorrection
        self.backupPreviousCorrection = backupPreviousCorrection
        self.quickloadWarningShown = False

        self.year = year if type(year) == str else str(year)
        # sicne again wrong smearing was used in post-processor, undo that one first
        self.unsmear_params = {
                 '2016': [1.013, 0.014, 0.029, 0.047], #updated numbers for v7 nanoAOD production
                 '2017': [1.017, 0.021, 0.058, 0.066],
                 '2018': [0.985, 0.019, 0.080, 0.073],
                 }
        self.smear_params = {
                 '2016': [1.013, 0.014, 0.029, 0.047], #updated numbers for v7 nanoAOD production
                 '2017': [1.017, 0.021, 0.058, 0.066],
                 '2018': [0.985, 0.019, 0.080, 0.073],
                 }
        if self.year not in self.smear_params:
            print("ERROR: smearing for year", self.year, " not available!")
            raise Exception("SmearingError")

        self.scale, self.scale_err, self.smear, self.smear_err = self.smear_params[self.year]

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']
        self.config = initVars['config']

        #smearing params
        if self.config.get('General','nTupleVersion') in ['V11','V12']:
            self.smear_params = {
                     '2016': [1.0, 0.0, 0.0, 0.0],
                     '2017': [1.0029846959, 0.0212893588055, 0.030684, 0.052497],
                     '2018': [0.98667384694, 0.0197153848807, 0.038481, 0.053924],
                     }
        elif self.config.get('General','nTupleVersion') == 'V13':
            self.smear_params = {
                     '2016': [1.013, 0.014, 0.029, 0.047],
                     '2017': [1.017, 0.021, 0.058, 0.066],
                     '2018': [0.985, 0.019, 0.080, 0.073],
                     }
        else:
            print("ERROR: jet smearing not defined for", self.config.get('General','nTupleVersion'),"!")
            raise Exception("SmearingError")

        if self.year not in self.smear_params:
            print("ERROR: smearing for year", self.year, " not available!")
            raise Exception("SmearingError")

        if self.sample.isMC():

            self.maxNjet      = 256
            self.bRegCorr     = array.array('f', [0.0]*self.maxNjet)
            self.Pt           = array.array('f', [0.0]*self.maxNjet)
            self.PtReg        = array.array('f', [0.0]*self.maxNjet)
            self.PtRegUp      = array.array('f', [0.0]*self.maxNjet)
            self.PtRegDown    = array.array('f', [0.0]*self.maxNjet)
            self.sampleTree.tree.SetBranchAddress("Jet_bRegCorr", self.bRegCorr)
            self.sampleTree.tree.SetBranchAddress("Jet_Pt", self.Pt)
            self.sampleTree.tree.SetBranchAddress("Jet_PtReg", self.PtReg)
            self.sampleTree.tree.SetBranchAddress("Jet_PtRegUp", self.PtRegUp)
            self.sampleTree.tree.SetBranchAddress("Jet_PtRegDown", self.PtRegDown)

            if self.backupPreviousCorrection:
                self.addVectorBranch("Jet_PtRegOld",     default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_PtRegOld[nJet]/F")
                self.addVectorBranch("Jet_PtRegOldUp",   default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_PtRegOldUp[nJet]/F")
                self.addVectorBranch("Jet_PtRegOldDown", default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_PtRegOldDown[nJet]/F")

    def processEvent(self, tree):
        if self.active and not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)

            nJet = tree.nJet

            # backup the Jet_PtReg branches as they are in post-processed ntuples
            if self.backupPreviousCorrection:
                for i in range(nJet):
                    self._b("Jet_PtRegOld")[i]     = self.PtReg[i]
                    self._b("Jet_PtRegOldUp")[i]   = self.PtRegUp[i]
                    self._b("Jet_PtRegOldDown")[i] = self.PtRegDown[i]

            # apply smearing
            for i in range(nJet):
                genJetIdx = tree.Jet_genJetIdx[i]
                if genJetIdx > -1 and genJetIdx < len(tree.GenJetWithNeutrinos_pt):
                    gen_pt    = tree.GenJetWithNeutrinos_pt[genJetIdx]

                    # reference: https://github.com/dabercro/hbb/blob/b86589128a6839a12efaf041f579fe88c1d1be38/nanoslimmer/applysmearing/applysmearing.py
                    regressed = self.Pt[i]*self.bRegCorr[i]
                    no_smear  = regressed * self.scale
                    gen_diff  = regressed - gen_pt
                    nominal   = max(0.0, (gen_pt + gen_diff * (1.0 + self.smear)) * self.scale)
                    band      = math.sqrt(pow(nominal/self.scale * self.scale_err, 2) + pow(gen_diff * self.scale * self.smear_err, 2))

                    down, up  = (max(nominal - band, no_smear), nominal + band) if regressed > gen_pt else (min(nominal + band, no_smear), nominal - band)  
                else:
                    regressed = self.Pt[i] * self.bRegCorr[i]
                    nominal   = regressed * self.scale
                    up        = regressed * (self.scale + self.scale_err)
                    down      = regressed * (self.scale - self.scale_err)

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


if __name__ == '__main__':

    config = XbbConfigReader.read('Zvv2018')

    info = ParseInfo(config=config)
    
    sample = [x for x in info if x.identifier == 'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8'][0]
    # read sample
    sampleTree = SampleTree(['/store/group/phys_higgs/hbb/ntuples/VHbbPostNano/2018/V13/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02A85/200519_095652/0000/tree_1.root'], treeName='Events', xrootdRedirector="root://eoscms.cern.ch/")
    # initialize module
    w = JetSmearer("2018")
    w.customInit({'sampleTree': sampleTree, 'sample': sample})
    n=0
    for event in sampleTree:
        w.processEvent(event)
        n=n+1
        if n==3: break

    #sampleTree.addOutputBranches(w.getBranches()) 

    # output files
    #sampleTree.addOutputTree('/scratch/krgedia/test.root', cut='MET_Pt>0', branches='*')

    # loop over all events!
    #sampleTree.process()
