#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
sys.path.append('../')
from myutils.BranchList import BranchList


class TestBranchListMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_BranchList(self):
        longCutString = "((V_new_mass>75.&V_new_mass<105.&Jet_btagCMVAV2[hJCMVAV2idx[0]]<0.9432&Jet_btagCMVAV2[hJCMVAV2idx[1]]<-0.5884&abs(VHbb::deltaPhi(HCMVAV2_reg_phi_corrJERUp,V_new_phi))>2.5&BasicCutsCMVA&(hJetCMVAV2_pt_reg_0_corrJERUp>20&hJetCMVAV2_pt_reg_1_corrJERUp>20))&V_new_pt>50)&(Vtype_new==1&(abs(vLeptons_new_eta[0])>=1.57||abs(vLeptons_new_eta[0])<=1.44)&(abs(vLeptons_new_eta[1])>=1.57||abs(vLeptons_new_eta[1])<=1.44))&(V_new_pt>50&V_new_pt<150)"
        branchList = BranchList(longCutString)
        branchesWhichShouldExist = ['hJetCMVAV2_pt_reg_0_corrJERUp', 'V_new_mass', 'Jet_btagCMVAV2', 'hJetCMVAV2_pt_reg_1_corrJERUp', 'V_new_pt',
         'HCMVAV2_reg_phi_corrJERUp', 'V_new_phi', 'Vtype_new', 'hJCMVAV2idx', 'BasicCutsCMVA',
         'vLeptons_new_eta']
        for branchName in branchesWhichShouldExist:
            self.assertTrue(branchName in branchList.getListOfBranches())

    def test_BanchListDuplicates(self):
        branchList = BranchList(['a', 'b', 'c', 'c', 'c'])
        branchList.addCut(['c','d','d'])
        self.assertEqual(len(branchList.getListOfBranches()), 4)


if __name__ == '__main__':
    unittest.main()
