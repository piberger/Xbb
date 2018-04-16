#!/usr/bin/env python
import ROOT
import array
from Jet import Jet

# propagate JES/JER systematics from jets to higgs candidate dijet pair 
class HiggsCandidateSystematics(object):
    
    def __init__(self, addSystematics=True):
        self.debug = False
        self.lastEntry = -1
        self.branches = []
        self.branchBuffers = {}
        self.addSystematics = addSystematics

        self.jetSystematics = ['jer','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesSubTotalPileUp','jesSubTotalRelative','jesSubTotalPt','jesSubTotalScale','jesSubTotalAbsolute','jesSubTotalMC','jesTotal','jesTotalNoFlavor','jesTotalNoTime','jesTotalNoFlavorNoTime','jesFlavorZJet','jesFlavorPhotonJet','jesFlavorPureGluon','jesFlavorPureQuark','jesFlavorPureCharm','jesFlavorPureBottom','jesCorrelationGroupMPFInSitu','jesCorrelationGroupIntercalibration','jesCorrelationGroupbJES','jesCorrelationGroupFlavor','jesCorrelationGroupUncorrelated']

        # corrected Higgs properties
        self.higgsProperties = ['H_reg_pt', 'H_reg_eta', 'H_reg_phi', 'H_reg_mass']
    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.higgsPropertiesWithSys = self.higgsProperties if self.sample.type != 'DATA' else []
        for higgsProperty in self.higgsProperties: 
            self.branchBuffers[higgsProperty] = array.array('f', [0.0])
            self.branches.append({'name': higgsProperty, 'formula': self.getBranch, 'arguments': higgsProperty})
            if higgsProperty in self.higgsPropertiesWithSys:
                for syst in self.jetSystematics:
                    for Q in ['Up', 'Down']:
                        higgsPropertySyst = "{p}_{s}_{q}".format(p=higgsProperty, s=syst, q=Q)
                        self.branchBuffers[higgsPropertySyst] = array.array('f', [0.0])
                        self.branches.append({'name': higgsPropertySyst, 'formula': self.getBranch, 'arguments': higgsPropertySyst})


    def getBranches(self):
        return self.branches
 
    # read from buffers which have been filled in processEvent()    
    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        # if current entry has not been processed yet
        if currentEntry != self.lastEntry:
            self.lastEntry = currentEntry

            hJidx0 = tree.hJidx[0]
            hJidx1 = tree.hJidx[1]

            # nominal value
            hJ0 = ROOT.TLorentzVector()
            hJ1 = ROOT.TLorentzVector()
            hJ0.SetPtEtaPhiM(tree.Jet_bReg[hJidx0]*tree.Jet_Pt[hJidx0]/tree.Jet_pt[hJidx0],tree.Jet_eta[hJidx0],tree.Jet_phi[hJidx0],tree.Jet_mass[hJidx0])
            hJ1.SetPtEtaPhiM(tree.Jet_bReg[hJidx1]*tree.Jet_Pt[hJidx1]/tree.Jet_pt[hJidx1],tree.Jet_eta[hJidx1],tree.Jet_phi[hJidx1],tree.Jet_mass[hJidx1])
            dijet = hJ0 + hJ1
            dijet_Nominal = dijet

            self.branchBuffers['H_reg_pt'][0] = dijet.Pt()
            self.branchBuffers['H_reg_eta'][0] = dijet.Eta()
            self.branchBuffers['H_reg_phi'][0] = dijet.Phi()
            self.branchBuffers['H_reg_mass'][0] = dijet.M()

            # systematics
            if self.addSystematics and self.sample.type != 'DATA':
                for syst in self.jetSystematics:
                    for Q in ['Up', 'Down']:
                        if self.sample.type != 'DATA':
                            hJ0.SetPtEtaPhiM(tree.Jet_bReg[hJidx0]*getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))[hJidx0]/tree.Jet_pt[hJidx0],tree.Jet_eta[hJidx0],tree.Jet_phi[hJidx0],getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))[hJidx0])
                            hJ1.SetPtEtaPhiM(tree.Jet_bReg[hJidx1]*getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))[hJidx1]/tree.Jet_pt[hJidx1],tree.Jet_eta[hJidx1],tree.Jet_phi[hJidx1],getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))[hJidx1])
                            dijet = hJ0 + hJ1
                        else:
                            dijet = dijet_Nominal
                        
                        self.branchBuffers['H_reg_pt_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.Pt()
                        self.branchBuffers['H_reg_eta_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.Eta()
                        self.branchBuffers['H_reg_phi_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.Phi()
                        self.branchBuffers['H_reg_mass_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.M()
        return True

