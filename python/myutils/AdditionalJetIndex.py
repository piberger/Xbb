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
        self.PS_treeIdx = None
        self.Sisr_treeIdx = None
        self.nhj_treeIdx = None
        self.AJidx = None
        self.PtSL = None
        self.HV = None
        self.ISRidx = None
        self.nhj_idx = None
        self.Sisr = None
        self.maxnAJ = 5
        self.branches.append({'name': 'AddJet0_idx', 'formula': lambda tree: self.getAJidx(tree)[0] , 'type': 'i'})
        self.branches.append({'name': 'AddJet1_idx', 'formula': lambda tree: self.getAJidx(tree)[1] , 'type': 'i'})
        self.branches.append({'name': 'HVcombined_pt', 'formula': lambda tree: self.getHV(tree).Pt(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_eta', 'formula': lambda tree: self.getHV(tree).Eta(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_phi', 'formula': lambda tree: self.getHV(tree).Phi(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_mass', 'formula': lambda tree: self.getHV(tree).M(), 'type': 'f'})
        self.branches.append({'name': 'AddJet0_nhJ_dPhiSq', 'formula': lambda tree: self.getAJ0_nhJ_dPhi2(tree), 'type': 'f'})
        self.branches.append({'name': 'AddJet0_nhJ_dEtaSq', 'formula': lambda tree: self.getAJ0_nhJ_dEta2(tree), 'type': 'f'})
        self.branches.append({'name': 'AddJet0_nhJ_idx', 'formula': lambda tree: self.getAJ_nhJ_idx(tree)[0], 'type': 'i'})
        self.branches.append({'name': 'ISR0_idx', 'formula': lambda tree: self.getISRidx(tree)[0] , 'type': 'i'})
        self.branches.append({'name': 'ISR1_idx', 'formula': lambda tree: self.getISRidx(tree)[1] , 'type': 'i'})
        self.branches.append({'name': 'SumISR_pt', 'formula': lambda tree: self.getSumISR(tree).Pt(), 'type': 'f'})
        self.branches.append({'name': 'SumISR_eta', 'formula': lambda tree: self.getSumISR(tree).Eta(), 'type': 'f'})
        self.branches.append({'name': 'SumISR_phi', 'formula': lambda tree: self.getSumISR(tree).Phi(), 'type': 'f'})
        self.branches.append({'name': 'SumISR_mass', 'formula': lambda tree: self.getSumISR(tree).M(), 'type': 'f'})

    def getBranches(self):
        return self.branches

    def getPtSortedList(self,tree):
        if tree.GetReadEntry() == self.PS_treeIdx:
            return self.PtSL
        self.PtSL = np.argsort(-np.array(tree.Jet_pt))
        self.PS_treeIdx = tree.GetReadEntry()
        return self.PtSL

    def getAJidx(self, tree):
        if tree.GetReadEntry() == self.AJ_treeIdx:
            if self.AJidx is not None:
                return self.AJidx
        self.AJidx = []
        self.AJ_treeIdx = tree.GetReadEntry()
        j = 0
        for jet_idx in self.getPtSortedList(tree):
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
    
    def getSumISR(self,tree):
        if tree.GetReadEntry() == self.Sisr_treeIdx:
             return self.Sisr:
        v = ROOT.TLorentzVector()
        for idx in self.getISRidx(tree):
            if idx == -1:
                break
            j = ROOT.TLorentzVector()
            j.SetPtEtaPhiM(tree.Jet_pt[idx],tree.Jet_eta[idx],tree.Jet_phi[idx],tree.Jet_mass[idx])
            v += j
        self.Sisr_treeIdx=tree.GetReadEntry() 
        self.Sisr = v
        return v

    def dj(self,eta1,eta2,phi1,phi2):
        return np.sqrt((eta1 - eta2)**2 + self.dPhi(phi1, phi2)**2)

    def dPhi(self,phi1,phi2):
        dp = phi1 - phi2
        if dp > np.pi:
            dp -= 2*np.pi
        if dp < -np.pi:
            dp += 2*np.pi
        return dp

    def dR_(self,eta1,eta2,phi1,phi2):
        return self.dR(eta1,-eta2,phi1,phi2+np.pi)
    
    def getAJ0_nhJ_dPhi2(self,tree):
        nhJ_idx = self.getAJ_nhJ_idx(tree)[0]
        idx = self.getAJidx(tree)[0]
        if idx>0 and nhJ_idx > 0:
            return self.dPhi(tree.Jet_phi[idx],tree.Jet_phi[nhJ_idx])**2
        return -1

    def getAJ0_nhJ_dEta2(self,tree):
        nhJ_idx = self.getAJ_nhJ_idx(tree)[0]
        idx = self.getAJidx(tree)[0]
        if idx>0 and nhJ_idx > 0:
            return (tree.Jet_eta[idx]-tree.Jet_eta[nhJ_idx])**2
        return -1

    def getAJ_nhJ_idx(self,tree):
        if tree.GetReadEntry() == self.nhj_treeIdx:
            return self.nhj_idx
        self.nhj_treeIdx = tree.GetReadEntry()
        self.nhj_idx = []
        j = 0
        h0 = tree.hJCMVAV2idx[0]
        h1 = tree.hJCMVAV2idx[1]
        if 0 <= h0 < tree.nJet and 0 <= h1 < tree.nJet:
            for idx in self.getAJidx(tree):
                if idx < 0:
                    break
                dRh1 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h1],tree.Jet_phi[idx],tree.Jet_phi[h1])
                dRh0 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h0],tree.Jet_phi[idx],tree.Jet_phi[h0])
                if dRh0 < dRh1:
                    self.nhj_idx.append(h0)
                self.nhj_idx.append(h1)
                j += 1
        for i in range(j,self.maxnAJ):
            self.nhj_idx.append(-1)
        return self.nhj_idx

    def getISRidx(self,tree):
        if tree.GetReadEntry() == self.ISR_treeIdx and self.ISRidx is not None:
            return self.ISRidx
        self.ISRidx = []
        self.ISR_treeIdx = tree.GetReadEntry()
        j = 0
        h0 = tree.hJCMVAV2idx[0]
        h1 = tree.hJCMVAV2idx[1]
        if 0 <= h0 < tree.nJet and 0 <= h1 < tree.nJet:
            for idx in self.getAJidx(tree):
                if idx < 0:
                    break
                dRh0 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h0],tree.Jet_phi[idx],tree.Jet_phi[h0])
                #dR_h0 = self.dR_(tree.Jet_eta[idx],tree.Jet_eta[h0],tree.Jet_phi[idx],tree.Jet_phi[h0])
                dRh1 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h1],tree.Jet_phi[idx],tree.Jet_phi[h1])
                #dR_h1 = self.dR_(tree.Jet_eta[idx],tree.Jet_eta[h1],tree.Jet_phi[idx],tree.Jet_phi[h1])
                nh0 = dRh0 < 0.8 #and dR_h0 > 2.5 and dR_h0 < 3.5
                nh1 = dRh1 < 0.8 #and dR_h1 > 2.5 and dR_h1 < 3.5
                cut = not nh0 and not nh1
                if cut:
                    self.ISRidx.append(idx)
                    j += 1
        for i in range(j,self.maxnAJ):
            self.ISRidx.append(-1)
        return self.ISRidx

