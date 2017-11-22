#!/usr/bin/env python
import ROOT
import numpy as np
import array

class AdditionalJetIndex(object):

    def __init__(self):
        self.branches = []
        self.HV_treeIdx = None
        self.AJ_treeIdx = None
        self.ISR_treeIdx = None
        self.AJidx = None
        self.HV = None
        self.ISRidx = None
        self.maxnAJ = 5
        self.branches.append({'name': 'AddJetIdx0', 'formula': lambda tree: self.getAJidx(tree)[0] , 'type': 'i'})
        self.branches.append({'name': 'AddJetIdx1', 'formula': lambda tree: self.getAJidx(tree)[1] , 'type': 'i'})
        self.branches.append({'name': 'HVcombined_pt', 'formula': lambda tree: self.getHV(tree).Pt(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_eta', 'formula': lambda tree: self.getHV(tree).Eta(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_phi', 'formula': lambda tree: self.getHV(tree).Phi(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_mass', 'formula': lambda tree: self.getHV(tree).M(), 'type': 'f'})
        self.branches.append({'name': 'ISRIdx0', 'formula': lambda tree: self.getISRidx(tree)[0] , 'type': 'i'})
        self.branches.append({'name': 'ISRIdx1', 'formula': lambda tree: self.getISRidx(tree)[1] , 'type': 'i'})

    def getBranches(self):
        return self.branches

    def getAJidx(self, tree):
        if tree.GetReadEntry() == self.AJ_treeIdx:
            if self.AJidx is not None:
                return self.AJidx
        self.AJidx = []
        self.AJ_treeIdx = tree.GetReadEntry()
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
        if tree.GetReadEntry() == self.HV_treeIdx:
            if self.HV is not None:
                return self.HV
        self.HV_treeIdx = tree.GetReadEntry()
        h = ROOT.TLorentzVector()
        h.SetPtEtaPhiM(tree.HCMVAV2_pt,tree.HCMVAV2_eta,tree.HCMVAV2_phi,tree.HCMVAV2_mass)
        v = ROOT.TLorentzVector()
        v.SetPtEtaPhiM(tree.V_new_pt,tree.V_new_eta,tree.V_new_phi,tree.V_new_mass)
        self.HV = h+v
        return self.HV
    
    def dR(self,eta1,eta2,phi1,phi2):
        return np.sqrt((eta1 - eta2)**2 + self.dPhi(phi1, phi2)**2)

    def dPhi(self,phi1,phi2):
        dp = phi1 - phi2
        if dp > np.pi:
            dp -= 2*np.pi
        if dp < np.pi:
            dp += 2*np.pi
        return dp

    def dR_(self,eta1,eta2,phi1,phi2):
        return self.dR(eta1,-eta2,phi1,phi2+np.pi)

    def getISRidx(self,tree):
        if tree.GetReadEntry() == self.ISR_treeIdx and self.ISRidx is not None:
            return self.ISRidx
        self.ISRidx = []
        self.ISR_treeIdx = tree.GetReadEntry()
        j = 0
        h0 = tree.hJCMVAV2idx[0]
        h1 = tree.hJCMVAV2idx[1]
        for idx in self.getAJidx(tree):
            if idx < 0 or h1 < 0 or h1 >= tree.nJet:
                break
            dRh0 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h0],tree.Jet_phi[idx],tree.Jet_phi[h0])
            dR_h0 = self.dR_(tree.Jet_eta[idx],tree.Jet_eta[h0],tree.Jet_phi[idx],tree.Jet_phi[h0])
            dRh1 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h1],tree.Jet_phi[idx],tree.Jet_phi[h1])
            dR_h1 = self.dR_(tree.Jet_eta[idx],tree.Jet_eta[h1],tree.Jet_phi[idx],tree.Jet_phi[h1])
            nh0 = dRh0 < 1.0 and dR_h0 > 2.5 and dR_h0 < 3.5
            nh1 = dRh1 < 1.0 and dR_h1 > 2.5 and dR_h1 < 3.5
            cut = not nh0 and not nh1
            if cut:
                self.ISRidx.append(idx)
                j += 1
        for i in range(j,self.maxnAJ):
            self.ISRidx.append(-1)
        return self.ISRidx

