#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule

class LOtoNLOweight(AddCollectionsModule):

    def __init__(self, branchName='weightLOtoNLO', year=2016):
        super(LOtoNLOweight, self).__init__()
        self.branchName = branchName
        self.year = int(year)

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']
        if not self.sample.isData():
            self.addBranch(self.branchName)
            self.addBranch(self.branchName + '_LHEVpt')
            self.addBranch(self.branchName + '_LHEVptShape')
            self.addBranch(self.branchName + '_2016')

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.sample.isData() and not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0] = 1.0
            self._b(self.branchName + '_LHEVpt')[0] = 1.0
            self._b(self.branchName + '_LHEVptShape')[0] = 1.0
            self._b(self.branchName + '_2016')[0] = 1.0

            if self.applies(tree):
                etabb = abs(tree.Jet_eta[tree.hJidx[0]]-tree.Jet_eta[tree.hJidx[1]])
                njets = tree.sampleIndex % 10
                if njets < 3:
                    if self.year == 2017:
                        # apply only one of them!
                        self._b(self.branchName)[0] = 1.153 * self.LOtoNLOWeightBjetSplitEtabb2017(etabb, njets) 
                        self._b(self.branchName + '_LHEVpt')[0] = 1.153 * self.LOtoNLOWeightBjetSplitVpt2017(tree.LHE_Vpt, njets)
                        self._b(self.branchName + '_LHEVptShape')[0] = 1.153 * self.LOtoNLOWeightBjetSplitVpt2017preserveNormalization(tree.LHE_Vpt, njets)
                        self._b(self.branchName + '_2016')[0] = 1.153 * self.LOtoNLOWeightBjetSplitEtabb(etabb, njets) 
                    else:
                        self._b(self.branchName)[0] = 1.153 * self.LOtoNLOWeightBjetSplitEtabb(etabb, njets) 
                else:
                    print("\x1b[31mERROR: sampleIndex==", tree.sampleIndex, "\x1b[0m")
                    raise Exception("IllegalSampleIndex")

    def applies(self, tree):
        isVJets = False
        sampleCat = int(tree.sampleIndex - (tree.sampleIndex % 10))

        # sync with AT: DYJetsToLL_M-4to50 not reweighted

        # Z+jets normal, W+jets normal, W+jets b-enriched
        if sampleCat in [4000,4100,4200,4300,4400,4500,4600,4700,5000,5100,5300,5400,11000,11100,11200,11300,11400,11500,11600,11700,15000,15100,15200,15300,15400,15500,15600]:
            isVJets = True
        
        # Z+jets b-enriched
        if sampleCat in [14000,12000,12100,12200,14100,14200,16000,16100,16200,16300]:
            isVJets = True

        return isVJets

    def LOtoNLOWeightBjetSplitEtabb(self, etabb, njets):
        SF = 1.
        if etabb < 5:
            if njets < 1:
                SF = 0.935422 + 0.0403162*etabb -0.0089026*etabb*etabb +0.0064324*etabb*etabb*etabb -0.000212443*etabb*etabb*etabb*etabb
            elif njets == 1:
                SF = 0.962415 +0.0329463*etabb -0.0414479*etabb*etabb +0.0240993*etabb*etabb*etabb -0.00278271*etabb*etabb*etabb*etabb
            elif njets >= 2:
                SF = (0.721265 -0.105643*etabb -0.0206835*etabb*etabb +0.00558626*etabb*etabb*etabb)*np.exp(0.450244*etabb)
        return SF

    def LOtoNLOWeightBjetSplitEtabb2017(self, etabb, njets):
        SF = 1.0
        etabb = min(etabb, 5.0)
        if njets < 1:
            SF = (0.958 + 0.0286 * etabb + 0.0014156 * etabb * etabb)
        elif njets == 1:
            SF = ((0.972 - 0.264 * etabb + 0.026919 * etabb * etabb) * np.exp(0.29901 * etabb))
        else:
            SF = (0.81 + 0.1493 * etabb - 0.000965976 * etabb * etabb)
        return SF
    
    def LOtoNLOWeightBjetSplitVpt2017(self, vpt, njets):
        SF = 1.0
        vpt = max(min(vpt,500.0),50.0)
        if njets < 1:
            SF = 1.1596-7.1563e-04*(vpt-5.000e+01)-1.1169e-06*(vpt-5.000e+01)**2 
        elif njets == 1:
            SF = 1.1153-7.3720e-04*(vpt-5.000e+01)-1.7232e-06*(vpt-5.000e+01)**2
        else:
            SF = 1.1667-8.9528e-04*(vpt-5.000e+01)-2.1150e-06*(vpt-5.000e+01)**2
        return SF
    
    def LOtoNLOWeightBjetSplitVpt2017preserveNormalization(self, vpt, njets):
        SF = 1.0
        vpt = max(min(vpt,500.0),50.0)
        if njets < 1:
            SF = 0.883*(1.1596-7.1563e-04*(vpt-5.000e+01)-1.1169e-06*(vpt-5.000e+01)**2) 
        elif njets == 1:
            SF = 0.926*(1.1153-7.3720e-04*(vpt-5.000e+01)-1.7232e-06*(vpt-5.000e+01)**2)
        else:
            SF = 0.887*(1.1667-8.9528e-04*(vpt-5.000e+01)-2.1150e-06*(vpt-5.000e+01)**2)
        return SF


