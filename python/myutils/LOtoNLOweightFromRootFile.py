#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule

# add in config: LOtoNLOweightV6 = LOtoNLOweightFromRootFile.LOtoNLOweightFromRootFile(fileName="nloweight_histograms_{sample}_V6_{nb}b.root")

class LOtoNLOweightFromRootFile(AddCollectionsModule):

    def __init__(self, fileName, branchName='weightLOtoNLO_LHEVptV7'):
        super(LOtoNLOweightFromRootFile, self).__init__()
        self.branchName = branchName
        self.fileName = fileName
        self.version = 2

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.sampleTypes = ['DYJets','ZJets','WJets','DYBJets','ZBJets','WBJets']
        self.fallbackSample = {'DYBJets':'DYJets','ZBJets':'ZJets','WBJets':'WJets'}

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
                for sample in self.sampleTypes: 
                    fN = self.fileName.format(nb=nb,sample=sample)
                    if os.path.isfile(fN):
                        self.rootFile[nb][sample] = ROOT.TFile.Open(fN, "READ")
                        self.fit[nb][sample]      = self.rootFile[nb][sample].Get("fit")
                        self.error[nb][sample]    = self.rootFile[nb][sample].Get("ci68")

                        self.addBranch(self.branchName + '_' + sample + '%d'%nb + '_Up')
                        self.addBranch(self.branchName + '_' + sample + '%d'%nb + '_Down')

            self.sampleTree = initVars['sampleTree']
            self.nGenBJetsFormula = "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)"
            self.sampleTree.addFormula(self.nGenBJetsFormula)

    def getSampleType(self):
        if 'DYBJets' in self.sample.identifier or ('DYJets' in self.sample.identifier and 'BGenFilter' in self.sample.identifier): 
            sampleType = 'DYBJets'
        elif 'DYJets' in self.sample.identifier:
            sampleType = 'DYJets'
        elif 'ZBJets' in self.sample.identifier or ('ZJets' in self.sample.identifier and 'BGenFilter' in self.sample.identifier):
            sampleType = 'ZBJets'
        elif 'ZJets' in self.sample.identifier:
            sampleType = 'ZJets'
        elif 'WBJets' in self.sample.identifier or ('WJets' in self.sample.identifier and 'BGenFilter' in self.sample.identifier):
            sampleType = 'WBJets'
        elif 'WJets' in self.sample.identifier:
            sampleType = 'WJets'
        else:
            raise Exception("UnknownSampleType")
        return sampleType

    # read central value from TF1, errors from TGraphErrors (68% CI) with linear interpolation
    def getWeight(self, nb, vpt, syst=0):
        sampleType = self.getSampleType()

        # udsc component in b-enriched sample: take weight from default sample
        if sampleType not in self.fit[nb]:
            sampleType = self.fallbackSample[sampleType]

        vpt = min(vpt,1000.0)
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
            
            for nb in [0,1,2]:
                for sample in self.sampleTypes: 
                    if sample in self.fit[nb]:
                        self._b(self.branchName + '_' + sample + '%d'%nb + '_Up')[0]   = 1.0
                        self._b(self.branchName + '_' + sample + '%d'%nb + '_Down')[0] = 1.0
           
            # only apply to LO V+jets samples
            if self.applies(tree):
                nb = int(min(max(self.sampleTree.evaluate(self.nGenBJetsFormula),0),2))

                self._b(self.branchName)[0]           = self.getWeight(nb, tree.LHE_Vpt)
                self._b(self.branchName + '_Up')[0]   = self.getWeight(nb, tree.LHE_Vpt, 1.0)
                self._b(self.branchName + '_Down')[0] = self.getWeight(nb, tree.LHE_Vpt, -1.0)
        
                thisSampleType = self.getSampleType() 
                # udsc component in b-enriched sample: take weight from default sample
                if thisSampleType not in self.fit[nb]:
                    thisSampleType = self.fallbackSample[thisSampleType]
            
                for nb in [0,1,2]:
                    for sampleType in self.sampleTypes: 
                        if sampleType in self.fit[nb]:
                            if sampleType == thisSampleType: 
                                self._b(self.branchName + '_' + sampleType + '%d'%nb + '_Up')[0]   = self._b(self.branchName + '_Up')[0]
                                self._b(self.branchName + '_' + sampleType + '%d'%nb + '_Down')[0] = self._b(self.branchName + '_Down')[0]
                            else:
                                self._b(self.branchName + '_' + sampleType + '%d'%nb + '_Up')[0]   = self._b(self.branchName)[0]
                                self._b(self.branchName + '_' + sampleType + '%d'%nb + '_Down')[0] = self._b(self.branchName)[0]

    
    # select all LO V+jets samples            
    def applies(self, tree):
        return any([x in self.sample.identifier for x in ['DYJets','DYBJets','WJets','WBJets','ZJets','ZBJets']]) and 'amcatnlo' not in self.sample.identifier and 'M-4to50' not in self.sample.identifier


