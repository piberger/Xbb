#!/usr/bin/env python
import ROOT
import numpy as np
import array

class AdditionalJetIndex(object):

    def __init__(self):
        self.branches = []
        self.treeIdx = None
        self.AJidx = None
        self.HV = None
        self.maxnAJ = 2
        self.branches.append({'name': 'AddJetIdx0', 'formula': lambda tree: self.getAJidx(tree)[0] , 'type': 'i'})
        self.branches.append({'name': 'AddJetIdx1', 'formula': lambda tree: self.getAJidx(tree)[1] , 'type': 'i'})
        self.branches.append({'name': 'HVcombined_pt', 'formula': lambda tree: self.getHV(tree).Pt(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_eta', 'formula': lambda tree: self.getHV(tree).Eta(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_phi', 'formula': lambda tree: self.getHV(tree).Phi(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_mass', 'formula': lambda tree: self.getHV(tree).M(), 'type': 'f'})

    def getBranches(self):
        return self.branches

    def getAJidx(self, tree):
        if tree.GetReadEntry() == self.treeIdx:
            if self.AJidx is not None:
                return self.AJidx
        else:
            self.HV = None
        self.AJidx = []
        self.treeIdx = tree.GetReadEntry()
        j = 0
        for jet_idx in tree.Jet_btagCmvaIdx:
            if jet_idx < tree.nJet and tree.Jet_pt[jet_idx] > 20 and abs(tree.Jet_eta[jet_idx]) < 5.2 and tree.Jet_puId[jet_idx] >= 4 and jet_idx != tree.hJCMVAV2idx[0] and jet_idx != tree.hJCMVAV2idx[1]:
                self.AJidx.append(jet_idx)
                j += 1
                if j >= self.maxnAJ:
                    return self.AJidx
        for i in range(j,self.maxnAJ):
            self.AJidx.append(-1)
        return self.AJidx
        
    def getHV(self,tree):
        if tree.GetReadEntry() == self.treeIdx:
            if self.HV is not None:
                return self.HV
        else:
            self.AJidx = None
        self.treeIdx = tree.GetReadEntry()
        h = ROOT.TLorentzVector()
        h.SetPtEtaPhiM(tree.HCMVAV2_pt,tree.HCMVAV2_eta,tree.HCMVAV2_phi,tree.HCMVAV2_mass)
        v = ROOT.TLorentzVector()
        v.SetPtEtaPhiM(tree.V_new_pt,tree.V_new_eta,tree.V_new_phi,tree.V_new_mass)
        self.HV = h+v
        return self.HV

