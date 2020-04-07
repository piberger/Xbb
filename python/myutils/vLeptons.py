#!/usr/bin/env python
import array

class lepton(object):
    def __init__(self, pt, eta, phi, mass, charge):
        self.pt = pt
        self.eta = eta
        self.phi = phi
        self.mass = mass
        self.charge = charge

class vLeptonSelector(object):

    def __init__(self, tree, config, isoZmm=0.25, isoZee=0.15, isoWmn=0.06, isoWen=0.06, muonID=None, muonIDcut=None):

        self.electronMVA = config.get('General', 'electronMVA') if config.has_option('General', 'electronMVA') else 'Electron_mvaSpring16GP_WP90' 
        self.electronMVA_80 = config.get('General', 'electronMVA80') if config.has_option('General', 'electronMVA80') else self.electronMVA
        self.electronMVA_90 = config.get('General', 'electronMVA90') if config.has_option('General', 'electronMVA90') else self.electronMVA

        self.muonID = config.get('General', 'muonMVA') if config.has_option('General', 'muonMVA') else "Muon_tightId"
        self.muonIDcut = config.get('General', 'muonMVAcut') if config.has_option('General', 'muonMVAcut') else 1

        if muonID is not None:
            self.muonID = muonID
        if muonIDcut is not None:
            self.muonIDcut = muonIDcut

        zMuons = []
        zElectrons = []
        wElectrons = []
        wMuons = []

        self.vMuonIdx = []
        self.vElectronIdx = []
        for i in range(tree.nMuon):
            if tree.Muon_pt[i]>20 and tree.Muon_pfRelIso04_all[i]<isoZmm and tree.Muon_dxy[i]<0.05 and tree.Muon_dz[i]<0.2:
                zMuons.append(lepton(pt=tree.Muon_pt[i], eta=tree.Muon_eta[i], phi=tree.Muon_phi[i], mass=tree.Muon_mass[i], charge=tree.Muon_charge[i]))
                self.vMuonIdx.append(i)
        for i in range(tree.nElectron):
            if tree.Electron_pt[i]>20 and getattr(tree, self.electronMVA_90)[i] and tree.Electron_pfRelIso03_all[i]<isoZee:
                zElectrons.append(lepton(pt=tree.Electron_pt[i], eta=tree.Electron_eta[i], phi=tree.Electron_phi[i], mass=tree.Electron_mass[i], charge=tree.Electron_charge[i]))
                self.vElectronIdx.append(i)

        for i in range(tree.nMuon):
            if tree.Muon_pt[i]>25 and getattr(tree, self.muonID)[i] >= self.muonIDcut and tree.Muon_pfRelIso04_all[i]<isoWmn and tree.Muon_dxy[i]<0.05 and tree.Muon_dz[i]<0.2:
                wMuons.append(lepton(pt=tree.Muon_pt[i], eta=tree.Muon_eta[i], phi=tree.Muon_phi[i], mass=tree.Muon_mass[i], charge=tree.Muon_charge[i]))
                self.vMuonIdx.append(i)
        for i in range(tree.nElectron):
            if tree.Electron_pt[i]>25 and getattr(tree, self.electronMVA_80)[i] and tree.Electron_pfRelIso03_all[i]<isoWen:
                wElectrons.append(lepton(pt=tree.Electron_pt[i], eta=tree.Electron_eta[i], phi=tree.Electron_phi[i], mass=tree.Electron_mass[i], charge=tree.Electron_charge[i]))
                self.vElectronIdx.append(i)

        vLeptons = [] 
        Vtype = 0 
        if len(zMuons) >= 2:
            if zMuons[0].pt > 20:
                for i in xrange(1,len(zMuons)):
                    if zMuons[0].charge * zMuons[i].charge < 0:
                        Vtype = 0
                        vLeptons = [zMuons[0],zMuons[i]]
                        self.vMuonIdx = [self.vMuonIdx[0], self.vMuonIdx[i]]
                        break
        elif len(zElectrons) >= 2:
            if zElectrons[0].pt > 20:
                for i in xrange(1,len(zElectrons)):
                    if zElectrons[0].charge * zElectrons[i].charge < 0:
                        Vtype = 1
                        vLeptons = [zElectrons[0],zElectrons[i]]
                        self.vElectronIdx = [self.vElectronIdx[0], self.vElectronIdx[i]]
                        break
        elif len(wElectrons) + len(wMuons) == 1:
            if len(wMuons) == 1:
                Vtype = 2
                vLeptons = [wMuons[0]]
            if len(wElectrons) == 1:
                Vtype = 3
                vLeptons = [wElectrons[0]]
        elif len(zElectrons) + len(zMuons) > 0:
            Vtype = 5
        else:
            Vtype = 4
            if tree.MET_Pt < 150:
                Vtype = -1

        # count additional + veto leptons the same way as AT (02.07.2018)
        nVetoLeptons = 0
        nAddLeptons = 0
        for i in range(tree.nMuon):
            if (tree.Muon_pt[i] > 4.5 and abs(tree.Muon_eta[i]) < 2.4 and tree.Muon_pfRelIso04_all[i] < 0.4 and abs(tree.Muon_dz[i])<0.2 and abs(tree.Muon_dxy[i])<0.05): 
                nVetoLeptons += 1
            if i in wMuons or i in zMuons:
                continue
            if tree.Muon_pt[i] > 15 and abs(tree.Muon_eta[i]) < 2.5 and tree.Muon_pfRelIso04_all[i] < 0.1:
                nAddLeptons += 1
        for i in range(tree.nElectron):
            if tree.Electron_pt[i] > 6.5 and abs(tree.Electron_eta[i])<2.5 and tree.Electron_pfRelIso03_all[i] < 0.4 and abs(tree.Electron_dz[i])<0.2 and abs(tree.Electron_dxy[i])<0.05 and tree.Electron_lostHits[i]<1.0:
                nVetoLeptons += 1
            if i in zElectrons or i in wElectrons:
                continue
            if tree.Electron_pt[i] > 15 and abs(tree.Electron_eta[i]) < 2.5 and tree.Electron_pfRelIso03_all[i] < 0.1:
                nAddLeptons += 1

        self.Vtype = Vtype
        self.vLeptons = vLeptons
        self.zMuons = zMuons
        self.zElectrons = zElectrons
        self.vMuonIdx = sorted(list(set(self.vMuonIdx)))
        self.vElectronIdx = sorted(list(set(self.vElectronIdx)))
        self.nVetoLeptons = nVetoLeptons
        self.nAddLeptons = nAddLeptons

    def getVleptons(self):
        return self.vLeptons
    
    def getVtype(self):
        return self.Vtype
    
    def getZelectrons(self):
        return self.zElectrons

    def getWelectrons(self):
        return self.wElectrons

    def getZmuons(self):
        return self.zMuons

    def getWmuons(self):
        return self.wMuons

class vLeptons(object):
    def __init__(self, recomputeVtype=False, isoZmm=0.25, isoZee=0.15, isoWmn=0.06, isoWen=0.06):
        self.recomputeVtype = recomputeVtype
        self.version = 2
        self.isoZmm = isoZmm
        self.isoZee = isoZee
        self.isoWmn = isoWmn
        self.isoWen = isoWen
        self.lastEntry = -1

        # TODO: rewrite with new fucntions to add branches
        self.branches = []
        self.branchBuffers = {}

        self.branchBuffers['nVMuonIdx'] = array.array('i', [0])
        self.branchBuffers['nVElectronIdx'] = array.array('i', [0])
        self.branches.append({'name': 'nVMuonIdx', 'formula': self.getBranch, 'arguments': 'nVMuonIdx', 'type': 'i'})
        self.branches.append({'name': 'nVElectronIdx', 'formula': self.getBranch, 'arguments': 'nVElectronIdx', 'type': 'i'})

        self.branchBuffers['VMuonIdx'] = array.array('i', [-1, -1])
        self.branchBuffers['VElectronIdx'] = array.array('i', [-1, -1])
        self.branches.append({'name': 'VMuonIdx', 'formula': self.getVMuonIdx, 'length':2, 'type': 'i', 'leaflist': 'VMuonIdx[nVMuonIdx]/I'})
        self.branches.append({'name': 'VElectronIdx', 'formula': self.getVElectronIdx, 'length':2, 'type': 'i', 'leaflist': 'VelectronIdx[nVElectronIdx]/I'})
        
        self.branchBuffers['nVetoLeptons'] = array.array('i', [0])
        self.branchBuffers['nAddLeptons'] = array.array('i', [0])
        self.branches.append({'name': 'nVetoLeptons', 'formula': self.getBranch, 'arguments': 'nVetoLeptons', 'type': 'i'})
        self.branches.append({'name': 'nAddLeptons', 'formula': self.getBranch, 'arguments': 'nAddLeptons', 'type': 'i'})

        if self.recomputeVtype:
            self.branchBuffers['Vtype'] = array.array('i', [0])
            self.branches.append({'name': 'Vtype', 'formula': self.getBranch, 'arguments': 'Vtype', 'type': 'i'})

        self.selector = None

    def customInit(self, initVars):
        self.config = initVars['config']

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        # if current entry has not been processed yet
        if currentEntry != self.lastEntry:
            self.lastEntry = currentEntry
            self.selector = vLeptonSelector(tree, config=self.config, isoZmm=self.isoZmm, isoZee=self.isoZee, isoWmn=self.isoWmn, isoWen=self.isoWen)

            self.branchBuffers['VMuonIdx'][0] = self.selector.vMuonIdx[0] if len(self.selector.vMuonIdx) > 0 else -2 
            self.branchBuffers['VMuonIdx'][1] = self.selector.vMuonIdx[1] if len(self.selector.vMuonIdx) > 1 else -2 
            self.branchBuffers['VElectronIdx'][0] = self.selector.vElectronIdx[0] if len(self.selector.vElectronIdx) > 0 else -2 
            self.branchBuffers['VElectronIdx'][1] = self.selector.vElectronIdx[1] if len(self.selector.vElectronIdx) > 1 else -2 
            self.branchBuffers['nVMuonIdx'][0] = min(len(self.selector.vMuonIdx),2)
            self.branchBuffers['nVElectronIdx'][0] = min(len(self.selector.vElectronIdx),2)
            self.branchBuffers['nVetoLeptons'][0] = self.selector.nVetoLeptons
            self.branchBuffers['nAddLeptons'][0] = self.selector.nAddLeptons

            if self.recomputeVtype:
                self.branchBuffers['Vtype'][0] = self.selector.getVtype()


        return True


    # read from buffers which have been filled in processEvent()    
    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getVMuonIdx(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        size = len(self.selector.vMuonIdx)
        destinationArray[0:size] = self.branchBuffers['VMuonIdx'][0:size]
    
    def getVElectronIdx(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        size = len(self.selector.vElectronIdx)
        destinationArray[0:size] = self.branchBuffers['VElectronIdx'][0:size]

