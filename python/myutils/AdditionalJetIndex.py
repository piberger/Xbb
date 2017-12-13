#!/usr/bin/env python
import ROOT
import numpy as np
import array

class AdditionalJetIndex(object):

    def __init__(self):
        #Tree idex Buffer
        self.HV_treeIdx = None
        self.AJ_treeIdx = None
        self.PS_treeIdx = None
        self.nhj_treeIdx = None
        self.process_treeIdx = None
        self.HVpp_treeIdx = None

        #Tree Buffers
        self.AJidx = None
        self.PtSL = None
        self.HV = None
        self.nhj_idx = None
        self.nhj_dR = None
        self.HVpp = None
        self.ISR_treeIdx = {}
        self.Sisr_treeIdx = {}
        self.Sfsr_treeIdx = {}
        self.ISRidx = {}
        self.FSRidx = {}
        self.Sisr = {}
        self.Sfsr = {}
        self.nISR = {}
        self.nFSR = {}
        self.cuts = ['advCut','ptCut','dRCut','dRppCut']
        for cut in self.cuts:
            self.ISR_treeIdx[cut] = None
            self.Sisr_treeIdx[cut] = None
            self.Sfsr_treeIdx[cut] = None
            self.ISRidx[cut] = None
            self.FSRidx[cut] = None
            self.Sisr[cut] = None
            self.Sfsr[cut] = None
            self.nISR[cut] = None
            self.nFSR[cut] = None
        self.nAJ = None
        self.maxnAJ = 8
        self.nJet = 12

        #Branches
        self.branches = []
        self.branchBuffers = {}
        self.branches.append({'name': 'HVcombined_pt', 'formula': lambda tree: self.getHV(tree).Pt(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_eta', 'formula': lambda tree: self.getHV(tree).Eta(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_phi', 'formula': lambda tree: self.getHV(tree).Phi(), 'type': 'f'})
        self.branches.append({'name': 'HVcombined_mass', 'formula': lambda tree: self.getHV(tree).M(), 'type': 'f'})
        self.branches.append({'name': 'nAddJet', 'formula': self.getNAJ, 'type': 'i'})
        self.branches.append({'name': 'rAddJet_idx', 'formula': self.getrAJ, 'type': 'i'})
        wName = 'AddJet_idx'
        self.branchBuffers[wName] = np.zeros(self.maxnAJ, dtype=np.int16)
        self.branches.append({'name': wName, 'formula': self.getVectorBranch, 'arguments': {'branch': wName, 'length': self.maxnAJ}, 'length': self.maxnAJ, 'type': 'i'})
        wName = 'Jet_nhJidx'
        self.branchBuffers[wName] = np.zeros(self.maxnAJ, dtype=np.int16)
        self.branches.append({'name': wName, 'formula': self.getVectorBranch, 'arguments': {'branch': wName, 'length': self.nJet}, 'length': self.nJet , 'type': 'i'})
        wName= 'Jet_nhJdR'
        self.branchBuffers[wName] = np.zeros(self.maxnAJ, dtype=np.int16)
        self.branches.append({'name': wName, 'formula': self.getVectorBranch, 'arguments': {'branch': wName, 'length': self.nJet}, 'length': self.nJet , 'type': 'f'})
        
        for definition in self.cuts:
            for wName in ['SumISR_'+definition+'_pt','SumISR_'+definition+'_eta','SumISR_'+definition+'_phi','SumISR_'+definition+'_mass','SumFSR_'+definition+'_pt','SumFSR_'+definition+'_eta','SumFSR_'+definition+'_phi','SumFSR_'+definition+'_mass']:
                self.branchBuffers[wName] = 0.0
                self.branches.append({'name': wName, 'formula': self.getCutBranch, 'arguments': {'branch': wName}, 'type': 'f'})

            for wName in ['nISR_'+definition,'nFSR_'+definition,'rISR_'+definition+'_idx','rFSR_'+definition+'_idx']:
                self.branchBuffers[wName] = 0
                self.branches.append({'name': wName, 'formula': self.getCutBranch, 'arguments': {'branch': wName}, 'type': 'i'})

            for wName in ['ISR_'+definition+'_idx', 'FSR_'+definition+'_idx']:
                self.branchBuffers[wName] = np.zeros(self.maxnAJ, dtype=np.int16)
                self.branches.append({'name': wName, 'formula': self.getVectorBranch, 'arguments': {'branch': wName, 'length': self.maxnAJ}, 'length': self.maxnAJ, 'type': 'i'})

    # read from buffers which have been filled in processEvent()    
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getCutBranch(self, event, arguments=None, destination=None):
        self.processEvent(event)
        return self.branchBuffers[arguments['branch']]

    def processEvent(self, tree):
        if self.process_treeIdx != tree.GetReadEntry():
            self.process_treeIdx = tree.GetReadEntry()

            self.branchBuffers['AddJet_idx'] = self.getAJidx(tree)
            self.branchBuffers['Jet_nhJidx'] = self.getJet_nhJ_idx(tree)
            self.branchBuffers['Jet_nhJdR'] = self.getJet_nhJ_dR(tree)

            for definition in self.cuts:
                self.branchBuffers['ISR_'+definition+'_idx'] = self.getISRidx(tree,definition)
                self.branchBuffers['FSR_'+definition+'_idx'] = self.getFSRidx(tree,definition)
                self.branchBuffers['SumISR_'+definition+'_pt'] = self.getSumISR(tree,definition).Pt()
                self.branchBuffers['SumISR_'+definition+'_eta'] = self.getSumISR(tree,definition).Eta()
                self.branchBuffers['SumISR_'+definition+'_phi'] = self.getSumISR(tree,definition).Phi()
                self.branchBuffers['SumISR_'+definition+'_mass'] = self.getSumISR(tree,definition).M()
                self.branchBuffers['SumFSR_'+definition+'_pt'] = self.getSumFSR(tree,definition).Pt()
                self.branchBuffers['SumFSR_'+definition+'_eta'] = self.getSumFSR(tree,definition).Eta()
                self.branchBuffers['SumFSR_'+definition+'_phi'] = self.getSumFSR(tree,definition).Phi()
                self.branchBuffers['SumFSR_'+definition+'_mass'] = self.getSumFSR(tree,definition).M()
                self.branchBuffers['nISR_'+definition] = self.getNISR(tree,definition)
                self.branchBuffers['nFSR_'+definition] = self.getNFSR(tree,definition)
                self.branchBuffers['rISR_'+definition+'_idx'] = self.getrISR(tree,definition)
                self.branchBuffers['rFSR_'+definition+'_idx'] = self.getrFSR(tree,definition)
            
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
            if jet_idx < tree.nJet and abs(tree.Jet_eta[jet_idx]) < 5.2 and tree.Jet_puId[jet_idx] >= 4 and jet_idx != tree.hJCMVAV2idx[0] and jet_idx != tree.hJCMVAV2idx[1]:
                self.AJidx.append(jet_idx)
                j += 1
        self.nAJ = j
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
    
    def getNISR(self,tree,cut):
        self.getISRidx(tree,cut)
        return self.nISR[cut]

    def getNFSR(self,tree,cut):
        self.getISRidx(tree,cut)
        return self.nFSR[cut]

    def getNAJ(self,tree):
        self.getAJidx(tree)
        return self.nAJ

    def getrISR(self,tree,cut):
        n = self.getNISR(tree,cut)
        if not n:
            return -1
        return self.getISRidx(tree,cut)[np.random.randint(n)]

    def getrFSR(self,tree,cut):
        n = self.getNFSR(tree,cut)
        if not n:
            return -1
        return self.getFSRidx(tree,cut)[np.random.randint(n)]

    def getrAJ(self,tree):
        n = self.getNAJ(tree)
        if not n:
            return -1
        return self.getAJidx(tree)[np.random.randint(n)]

    def getSumISR(self,tree,cut):
        if tree.GetReadEntry() == self.Sisr_treeIdx[cut]:
             return self.Sisr[cut]
        v = ROOT.TLorentzVector()
        for idx in self.getISRidx(tree,cut):
            if idx == -1:
                break
            j = ROOT.TLorentzVector()
            j.SetPtEtaPhiM(tree.Jet_pt[idx],tree.Jet_eta[idx],tree.Jet_phi[idx],tree.Jet_mass[idx])
            v += j
        self.Sisr_treeIdx[cut]=tree.GetReadEntry() 
        self.Sisr[cut] = v
        return v

    def getSumFSR(self,tree,cut):
        if tree.GetReadEntry() == self.Sfsr_treeIdx[cut]:
             return self.Sfsr[cut]
        v = ROOT.TLorentzVector()
        for idx in self.getFSRidx(tree,cut):
            if idx == -1:
                break
            j = ROOT.TLorentzVector()
            j.SetPtEtaPhiM(tree.Jet_pt[idx],tree.Jet_eta[idx],tree.Jet_phi[idx],tree.Jet_mass[idx])
            v += j
        self.Sfsr_treeIdx[cut] = tree.GetReadEntry() 
        self.Sfsr[cut] = v
        return v

    def dR(self,eta1,eta2,phi1,phi2):
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
        idx = self.getAJidx(tree)[0]
        nhJ_idx = self.getJet_nhJ_idx(tree)[idx]
        if idx>0 and nhJ_idx > 0:
            return self.dPhi(tree.Jet_phi[idx],tree.Jet_phi[nhJ_idx])**2
        return -1

    def getAJ0_nhJ_dEta2(self,tree):
        idx = self.getAJidx(tree)[0]
        nhJ_idx = self.getJet_nhJ_idx(tree)[idx]
        if idx>0 and nhJ_idx > 0:
            return (tree.Jet_eta[idx]-tree.Jet_eta[nhJ_idx])**2
        return -1

    def getJet_nhJ_idx(self,tree):
        if tree.GetReadEntry() == self.nhj_treeIdx:
            return self.nhj_idx
        self.nhj_treeIdx = tree.GetReadEntry()
        self.nhj_idx = []
        self.nhj_dR = []
        h0 = tree.hJCMVAV2idx[0]
        h1 = tree.hJCMVAV2idx[1]
        if 0 <= h0 < tree.nJet and 0 <= h1 < tree.nJet:
            for idx in range(self.nJet):
                if idx < tree.nJet:
                    dRh1 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h1],tree.Jet_phi[idx],tree.Jet_phi[h1])
                    dRh0 = self.dR(tree.Jet_eta[idx],tree.Jet_eta[h0],tree.Jet_phi[idx],tree.Jet_phi[h0])
                    if dRh0 < dRh1:
                        self.nhj_idx.append(h0)
                        self.nhj_dR.append(dRh0)
                    else:
                        self.nhj_idx.append(h1)
                        self.nhj_dR.append(dRh1)
                else:
                    self.nhj_idx.append(-1)
                    self.nhj_dR.append(-1)
        else:
            for i in range(self.nJet):
                self.nhj_idx.append(-1)
                self.nhj_dR.append(-1)
        return self.nhj_idx

    def getJet_nhJ_dR(self,tree):
        self.getJet_nhJ_idx(tree)
        return self.nhj_dR

    def getJet_HV_pp(self,tree):
        if tree.GetReadEntry() == self.HVpp_treeIdx:
            return self.HVpp
        self.HVpp_treeIdx = tree.GetReadEntry()
        HV = self.getHV(tree)
        self.HVpp = []
        Jet = ROOT.TLorentzVector()
        for idx in range(self.nJet):
            if idx < tree.nJet:
                Jet.SetPtEtaPhiM(tree.Jet_pt[idx],tree.Jet_eta[idx],tree.Jet_phi[idx],tree.Jet_mass[idx])
                self.HVpp.append((HV * Jet) / (Jet.Pt() * HV.M()))
            else:
                self.HVpp.append(-1)
        return self.HVpp

    def getISRidx(self,tree,cut):
        if tree.GetReadEntry() == self.ISR_treeIdx[cut] and self.ISRidx[cut] is not None:
            return self.ISRidx[cut]
        
        self.ISRidx[cut] = []
        self.FSRidx[cut] = []
        self.ISR_treeIdx[cut] = tree.GetReadEntry()
        nhJidx = self.getJet_nhJ_idx(tree)
        j = 0
        l = 0

        for idx in self.getAJidx(tree):
            if idx < 0 or self.nJet <= idx or nhJidx[idx] < 0:
                break
            
            if cut == 'advCut':
                HV = self.getHV(tree)
                dRh = self.getJet_nhJ_dR(tree)[idx]
                dRHV_ = self.dR_(tree.Jet_eta[idx],HV.Eta(),tree.Jet_phi[idx],HV.Phi())
                dRHV = self.dR(tree.Jet_eta[idx],HV.Eta(),tree.Jet_phi[idx],HV.Phi())
                fsr1 = dRh < 1.1 and (dRHV < 2.7 or 1.7 < dRHV_ < 3.2)
                fsr2 = dRh < 0.7 
                isr_cut = not fsr1 and not fsr2
            
            if cut == 'ptCut':
                isr_cut = tree.Jet_pt[idx] > 30

            if cut == 'dRCut':
                dRh = self.getJet_nhJ_dR(tree)[idx]
                isr_cut = dRh > 0.8
            
            if cut == 'dRppCut':
                dRh = self.getJet_nhJ_dR(tree)[idx]
                pp = self.getJet_HV_pp(tree)[idx]
                isr_cut = (dRh-0.6)**2 + (np.log10(pp-0.6)/1.5 + 0.1)**2 > 0.3**2

            if isr_cut:
                self.ISRidx[cut].append(idx)
                j += 1
            else:
                self.FSRidx[cut].append(idx)
                l += 1
        
        self.nISR[cut] = j
        self.nFSR[cut] = l
        for i in range(j,self.maxnAJ):
            self.ISRidx[cut].append(-1)
        for i in range(l,self.maxnAJ):
            self.FSRidx[cut].append(-1)
        return self.ISRidx[cut]

    def getFSRidx(self,tree,cut):
        self.getISRidx(tree,cut)
        return self.FSRidx[cut]
