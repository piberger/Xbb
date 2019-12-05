#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
sys.path.append('../')
from myutils.XbbTools import XbbTools

class TestSystVarReplacements(unittest.TestCase):

    def setUp(self):
        self.testStrings = [
                'min(MHT_pt, MET_Pt) > 100 && Jet_Pt[hJidx[0]] > 30 && Jet_Pt[hJidx[1]] > 30 && Jet_btagDeepB[hJidx[1]] > 0.1522 && H_mass < 500 && H_pt > 120.0 && Jet_btagDeepB[hJidx[0]] > 0.4941 && MET_Pt > 170.0 && abs(TVector2::Phi_mpi_pi(H_phi-V_phi)) > 2.0 && Min$(abs(TVector2::Phi_mpi_pi(Jet_phi[hJidx]-MET_Phi))) < 1.57',
                'max(Lepton_pt[vLidx[0]],Lepton_pt[vLidx[1]]) > 50 && Sum$(Lepton_pt>10)>1'
                ]
        # specific expressions like 'Lepton_pt[vLidx[0]]' have to be placed before general ones like 'Lepton_pt'
        self.replacementsList = [
                'H_mass>H_mass_{syst}_{UD}',
                'H_phi>H_phi_{syst}_{UD}',
                'H_pt>H_pt_{syst}_{UD}',
                'H_eta>H_eta_{syst}_{UD}',
                'Jet_Pt[hJidx[0]]>Jet_pt_{syst}{UD}[hJidx[0]]',
                'Jet_Pt[hJidx[1]]>Jet_pt_{syst}{UD}[hJidx[1]]',
                'Lepton_pt[vLidx[0]]>Lepton_pt[vLidx[0]]*Lepton_pt_corr{syst}{UD}[vLidx[0]]',
                'Lepton_pt[vLidx[1]]>Lepton_pt[vLidx[1]]*Lepton_pt_corr{syst}{UD}[vLidx[1]]',
                'Lepton_pt>Lepton_pt*Lepton_pt_corr{syst}{UD}',
            ]

        self.results = [
                'min(MHT_pt, MET_Pt) > 100 && Jet_pt_{syst}{UD}[hJidx[0]] > 30 && Jet_pt_{syst}{UD}[hJidx[1]] > 30 && Jet_btagDeepB[hJidx[1]] > 0.1522 && H_mass_{syst}_{UD} < 500 && H_pt_{syst}_{UD} > 120.0 && Jet_btagDeepB[hJidx[0]] > 0.4941 && MET_Pt > 170.0 && abs(TVector2::Phi_mpi_pi(H_phi_{syst}_{UD}-V_phi)) > 2.0 && Min$(abs(TVector2::Phi_mpi_pi(Jet_phi[hJidx]-MET_Phi))) < 1.57',
                'max(Lepton_pt[vLidx[0]]*Lepton_pt_corr{syst}{UD}[vLidx[0]],Lepton_pt[vLidx[1]]*Lepton_pt_corr{syst}{UD}[vLidx[1]]) > 50 && Sum$(Lepton_pt*Lepton_pt_corr{syst}{UD}>10)>1'
            ]

    def test_splitJoin(self):
        for x in self.testStrings:
            self.assertEqual(x,XbbTools.joinParts(XbbTools.splitParts(x)))
    
    def test_replace(self):
        for i,x in enumerate(self.testStrings):
            y = XbbTools.getSystematicsVariationTemplate(x,self.replacementsList)
            self.assertEqual(y, self.results[i])

    def test_badBrackets(self):
        with self.assertRaises(Exception) as e:
            # this string is missing a closing ] on purpose
            XbbTools.getSystematicsVariationTemplate('Jet_Pt[hJidx[0]', self.replacementsList)



if __name__ == '__main__':
    unittest.main()
