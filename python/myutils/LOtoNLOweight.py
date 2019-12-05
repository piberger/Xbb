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
            self.addBranch(self.branchName + '_LHEVptV2')
            self.addBranch(self.branchName + '_LHEVptV2_p0_Up')
            self.addBranch(self.branchName + '_LHEVptV2_p0_Down')
            self.addBranch(self.branchName + '_LHEVptV2_p1_Up')
            self.addBranch(self.branchName + '_LHEVptV2_p1_Down')
            self.addBranch(self.branchName + '_2016')

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.sample.isData() and not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0]                       = 1.0
            self._b(self.branchName + '_LHEVptV2')[0]         = 1.0
            self._b(self.branchName + '_LHEVptV2_p0_Up')[0]   = 1.0
            self._b(self.branchName + '_LHEVptV2_p0_Down')[0] = 1.0
            self._b(self.branchName + '_LHEVptV2_p1_Up')[0]   = 1.0
            self._b(self.branchName + '_LHEVptV2_p1_Down')[0] = 1.0
            self._b(self.branchName + '_2016')[0]             = 1.0

            if self.applies(tree):
                etabb = abs(tree.Jet_eta[tree.hJidx[0]]-tree.Jet_eta[tree.hJidx[1]])
                njets = tree.sampleIndex % 10
                if njets < 3:
                    if self.year == 2017:
                        # apply only one of them!

                        # eta bb derived from 2017 DY
                        self._b(self.branchName)[0] = 1.153 * self.LOtoNLOWeightBjetSplitEtabb2017(etabb, njets) 

                        # eta bb derived from 2016 DY
                        self._b(self.branchName + '_2016')[0] = 1.153 * self.LOtoNLOWeightBjetSplitEtabb(etabb, njets) 

                        # vpt derived from 2017 ZJetsNuNu/WJetsLNu/DY
                        self._b(self.branchName + '_LHEVptV2')[0]         = self.LOtoNLOWeightBjetSplitVpt2017V2(tree.LHE_Vpt, njets, self.sample.identifier)
                        self._b(self.branchName + '_LHEVptV2_p0_Up')[0]   = self.LOtoNLOWeightBjetSplitVpt2017V2(tree.LHE_Vpt, njets, self.sample.identifier, var0=1.0)
                        self._b(self.branchName + '_LHEVptV2_p0_Down')[0] = self.LOtoNLOWeightBjetSplitVpt2017V2(tree.LHE_Vpt, njets, self.sample.identifier, var0=-1.0)
                        self._b(self.branchName + '_LHEVptV2_p1_Up')[0]   = self.LOtoNLOWeightBjetSplitVpt2017V2(tree.LHE_Vpt, njets, self.sample.identifier, var1=1.0)
                        self._b(self.branchName + '_LHEVptV2_p1_Down')[0] = self.LOtoNLOWeightBjetSplitVpt2017V2(tree.LHE_Vpt, njets, self.sample.identifier, var1=-1.0)
                        
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

    ## each of the 0b/1b/2b components relative contribution is taken from LO
    #def LOtoNLOWeightBjetSplitVpt2017V2_HFcompositionFromLO(self, vpt, njets, sampleIdentifier, var=0.0):
    #    SF = 1.0
    #    vpt = max(min(vpt,500.0),50.0)
    #    # exclude NLO samples itself
    #    if 'amc' not in sampleIdentifier:
    #        if any([x in sampleIdentifier for x in ['WJets', 'WBJets']]):
    #            if njets < 1:
    #                SF = 1.210 - (1.013e-3 + var*0.010e-3)*vpt 
    #            elif njets == 1:
    #                SF = 1.098 - (1.230e-3 + var*0.051e-3)*vpt 
    #            else:
    #                SF = 1.087 - (0.871e-3 + var*0.102e-3)*vpt
    #        elif any([x in sampleIdentifier for x in ['ZJets', 'ZBJets']]):
    #            pass
    #        elif any([x in sampleIdentifier for x in ['DYJets', 'DYBJets']]):
    #            if njets < 1:
    #                SF = 1.290 - (1.167e-3 + var*0.014e-3)*vpt 
    #            elif njets == 1:
    #                SF = 1.122 - (1.065e-3 + var*0.054e-3)*vpt 
    #            else:
    #                SF = 1.110 - (1.345e-3 + var*0.095e-3)*vpt
    #    return SF

    # relative 0b/1b/2b contributions from NLO, scaled to NNLO (LO x NNLO-k factor)
    def LOtoNLOWeightBjetSplitVpt2017V2(self, vpt, njets, sampleIdentifier, var0=0.0, var1=0.0):
        SF = 1.0
        vpt = max(min(vpt,500.0),50.0)
        # exclude NLO samples itself
        if 'amc' not in sampleIdentifier:
            if any([x in sampleIdentifier for x in ['WJets', 'WBJets']]):
                if njets < 1:
                    SF = (1.209 + var0*0.002) - (1.013e-3 + var1*0.010e-3)*vpt 
                elif njets == 1:
                    SF = (1.241 + var0*0.009) - (1.391e-3 + var1*0.057e-3)*vpt 
                else:
                    SF = (1.087 + var0*0.019) - (0.871e-3 + var1*0.103e-3)*vpt
            elif any([x in sampleIdentifier for x in ['ZJets', 'ZBJets']]):
                if njets < 1:
                    SF = (1.185 + var0*0.0036) - (1.248e-3 + var1*0.015e-3)*vpt 
                elif njets == 1:
                    SF = (1.109 + var0*0.0145) - (1.259e-3 + var1*0.062e-3)*vpt 
                else:
                    SF = (1.017 + var0*0.0253) - (1.173e-3 + var1*0.104e-3)*vpt
            elif any([x in sampleIdentifier for x in ['DYJets', 'DYBJets']]):
                if njets < 1:
                    SF = (1.288 + var0*0.002) - (1.166e-3 + var1*0.014e-3)*vpt 
                elif njets == 1:
                    SF = (1.231 + var0*0.006) - (1.168e-3 + var1*0.059e-3)*vpt 
                else:
                    SF = (1.219 + var0*0.013) - (1.478e-3 + var1*0.105e-3)*vpt
        return SF
    

    

