#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule

# add in config: LOtoNLOweightV6 = LOtoNLOweightFromRootFile.LOtoNLOweightFromRootFile(fileName="nloweight_histograms_{sample}_V6_{nb}b.root")

class LOtoNLOweightFromRootFile(AddCollectionsModule):

    def __init__(self, fileName, branchName='weightLOtoNLO_LHEVptV6'):
        super(LOtoNLOweightFromRootFile, self).__init__()
        self.branchName = branchName
        self.fileName = fileName

    def customInit(self, initVars):
        self.sample = initVars['sample']

        if not self.sample.isData():
            self.addBranch(self.branchName)
            self.addBranch(self.branchName + '_Up')
            self.addBranch(self.branchName + '_Down')

            self.rootFile = {}
            self.fit = {}
            self.error = {}
            for nb in [0,1,2]:
                self.rootFile[nb] = {}
                self.fit[nb] = {}
                self.error[nb] = {}
                for sample in ['DYJets','ZJets','WJets']:
                    fN = self.fileName.format(nb=nb,sample=sample)
                    if os.path.isfile(fN):
                        self.rootFile[nb][sample] = ROOT.TFile.Open(fN, "READ")
                        self.fit[nb][sample]      = self.rootFile[nb][sample].Get("fit")
                        self.error[nb][sample]    = self.rootFile[nb][sample].Get("ci68")

            self.sampleTree = initVars['sampleTree']
            self.nGenBJetsFormula = "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)"
            self.sampleTree.addFormula(self.nGenBJetsFormula)

    def getSampleType(self):
        if 'DYJets' in self.sample.identifier or 'DYBJets' in self.sample.identifier:
            sampleType = 'DYJets'
        elif 'ZJets' in self.sample.identifier or 'ZBJets' in self.sample.identifier:
            sampleType = 'ZJets'
        elif 'WJets' in self.sample.identifier or 'WBJets' in self.sample.identifier:
            sampleType = 'WJets'
        else:
            raise Exception("UnknownSampleType")
        return sampleType

    # read central value from TF1, errors from TGraphErrors (68% CI) with linear interpolation
    def getWeight(self, nb, vpt, syst=0):
        sampleType = self.getSampleType()
        w = self.fit[nb][sampleType].Eval(vpt)
        if syst != 0:
            x  = np.array(self.error[nb][sampleType].GetX())
            ey = np.array(self.error[nb][sampleType].GetEY())
            p  = min(max(np.searchsorted(x, vpt),1),len(x)-1)
            w += syst * (ey[p-1] + (vpt - x[p-1])/(x[p]-x[p-1])*(ey[p]-ey[p-1]))
        return w

    def processEvent(self, tree):
        if not self.sample.isData() and not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0]           = 1.0
            self._b(self.branchName + '_Up')[0]   = 1.0
            self._b(self.branchName + '_Down')[0] = 1.0
           
            # only apply to LO V+jets samples
            if self.applies(tree):
                nb = int(min(max(self.sampleTree.evaluate(self.nGenBJetsFormula),0),2))

                self._b(self.branchName)[0]           = self.getWeight(nb, tree.LHE_Vpt)
                self._b(self.branchName + '_Up')[0]   = self.getWeight(nb, tree.LHE_Vpt, 1.0)
                self._b(self.branchName + '_Down')[0] = self.getWeight(nb, tree.LHE_Vpt, -1.0)

    
    # select all LO V+jets samples            
    def applies(self, tree):
        return any([x in self.sample.identifier for x in ['DYJets','DYBJets','WJets','WBJets','ZJets','ZBJets']]) and 'amcatnlo' not in self.sample.identifier and 'M-4to50' not in self.sample.identifier


