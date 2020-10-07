#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np
from XbbConfig import XbbConfigTools
import time

# correlates the JECs according to new JEC correlation scheme (V11 -> V13) 
class JECcorrelator(AddCollectionsModule):

    def __init__(self, year):
        super(JECcorrelator, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.quickloadWarningShown = False

        self.year = year if type(year) == str else str(year)
    
    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        self.config = initVars['config']

        self.correlation_scheme = {
            "jesAbsolute" : ["jesAbsoluteMPFBias","jesAbsoluteScale","jesFragmentation","jesPileUpDataMC","jesPileUpPtRef","jesRelativeFSR","jesSinglePionECAL","jesSinglePionHCAL"],
            "jesAbsolute_"+self.year : ["jesAbsoluteStat","jesRelativeStatFSR","jesTimePtEta"],
            "jesBBEC1": ["jesPileUpPtBB","jesPileUpPtEC1","jesRelativePtBB"],
            "jesBBEC1_"+self.year: ["jesRelativeJEREC1","jesRelativePtEC1","jesRelativeStatEC"],
            "jesEC2": ["jesPileUpPtEC2"],
            "jesEC2_"+self.year: ["jesRelativeJEREC2","jesRelativePtEC2"],
            "jesFlavorQCD": ["jesFlavorQCD"],
            "jesHF": ["jesPileUpPtHF","jesRelativeJERHF","jesRelativePtHF"],
            "jesHF_"+self.year: ["jesRelativeStatHF"],
            "jesRelativeBal": ["jesRelativeBal"],
            "jesRelativeSample_"+self.year: ["jesRelativeSample"],
        }

        if self.sample.isMC():

            self.xbbConfig  = XbbConfigTools(self.config)
            self.JEC_reduced = self.xbbConfig.getJECuncertainties(step='reduced')
            # remove JER uncertainties
            self.JEC_reduced = [x for x in self.JEC_reduced if not x.startswith("jer")]
            #remove branches with same name to avoid issues due to same naming scheme
            self.JEC_reduced = [x for x in self.JEC_reduced if x not in ["jesFlavorQCD","jesRelativeBal"]]
            print(self.JEC_reduced)

            self.JEC_full = self.xbbConfig.getJECuncertainties()
            self.JEC_full = [x for x in self.JEC_full if not x.startswith("jer")]
            #self.JEC_full = ["jesAbsoluteMPFBias","jesAbsoluteScale","jesFragmentation","jesPileUpDataMC","jesPileUpPtRef","jesRelativeFSR","jesSinglePionECAL","jesSinglePionHCAL","jesAbsoluteStat","jesRelativeStatFSR","jesTimePtEta","jesPileUpPtBB","jesPileUpPtEC1","jesRelativePtBB","jesRelativeJEREC1","jesRelativePtEC1","jesRelativeStatEC","jesPileUpPtEC2","jesRelativeJEREC2","jesRelativePtEC2","jesPileUpPtHF","jesRelativeJERHF","jesRelativePtHF","jesRelativeStatHF","jesRelativeBal","jesRelativeSample"]
            if self.year == "2016":
                self.JEC_full.remove("jesRelativeSample")

            self.maxNjet   = 256
            self.maxNfatjet = 50
            self.nEvent = 0

            # load needed information
            for syst in self.JEC_full+["nom"]:
                if syst != "nom": UD = ["Up","Down"]
                else: UD = [""]
                for Q in UD:
                    setattr(self,"jet_pt_"+syst+Q,array.array('f', [0.0]*self.maxNjet))
                    setattr(self,"jet_mass_"+syst+Q,array.array('f', [0.0]*self.maxNjet))
                    setattr(self,"met_pt_"+syst+Q,array.array('f', [0.0]))
                    setattr(self,"met_phi_"+syst+Q,array.array('f', [0.0]))
                    setattr(self,"fatjet_pt_"+syst+Q,array.array('f', [0.0]*self.maxNfatjet))
                    setattr(self,"fatjet_msoftdrop_"+syst+Q,array.array('f', [0.0]*self.maxNfatjet))

                    self.sampleTree.tree.SetBranchAddress("Jet_pt_"+syst+Q, getattr(self, "jet_pt_"+syst+Q))
                    self.sampleTree.tree.SetBranchAddress("Jet_mass_"+syst+Q, getattr(self, "jet_mass_"+syst+Q))
                    self.sampleTree.tree.SetBranchAddress("MET_pt_"+syst+Q, getattr(self, "met_pt_"+syst+Q))
                    self.sampleTree.tree.SetBranchAddress("MET_phi_"+syst+Q, getattr(self, "met_phi_"+syst+Q))
                    self.sampleTree.tree.SetBranchAddress("FatJet_pt_"+syst+Q, getattr(self, "fatjet_pt_"+syst+Q))
                    self.sampleTree.tree.SetBranchAddress("FatJet_msoftdrop_"+syst+Q, getattr(self, "fatjet_msoftdrop_"+syst+Q))

            for syst in self.JEC_reduced:
                for Q in self._variations(syst):
                    self.addVectorBranch("Jet_pt_"+syst+Q, default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_pt_"+syst+Q+"[nJet]/F")
                    self.addVectorBranch("Jet_mass_"+syst+Q, default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet_mass_"+syst+Q+"[nJet]/F")
                    self.addBranch("MET_pt_"+syst+Q, default=0.0)
                    self.addBranch("MET_phi_"+syst+Q, default=0.0)
                    self.addVectorBranch("FatJet_pt_"+syst+Q, default=0.0, branchType='f', length=self.maxNfatjet, leaflist="FatJet_pt_"+syst+Q+"[nFatJet]/F")
                    self.addVectorBranch("FatJet_msoftdrop_"+syst+Q, default=0.0, branchType='f', length=self.maxNfatjet, leaflist="FatJet_msoftdrop_"+syst+Q+"[nFatJet]/F")

            self.t0 = time.time()
                    
    def correlator(self,syst,idx,Q,var,attr):

        nom = attr[var]["nom"][idx]

        # RelativeSample uncertainty missing in 2016 datasets
        if syst == "jesRelativeSample_2016":
            return nom
        jec_to_correlate = self.correlation_scheme[syst]
        squared_sum = 0
        if (len(jec_to_correlate)==1):
            j=jec_to_correlate[0]
            squared_sum = attr[var][j][Q][idx] - nom
            return nom+(squared_sum)
        else:
            for j in jec_to_correlate:
                squared_sum += (attr[var][j][Q][idx] - nom)**2
            if Q == "Up":
                return nom+np.sqrt(squared_sum)
            if Q == "Down":
                return nom-np.sqrt(squared_sum)

    def METPhicorrelator(self,syst,Q,var,attr):

        MET_nom = ROOT.TLorentzVector()
        MET_nom.SetPtEtaPhiM(attr["MET_pt"]["nom"][0], 0.0, attr["MET_phi"]["nom"][0], 0.0)
        MET_nom_x = MET_nom.X()
        MET_nom_y = MET_nom.Y()

        # RelativeSample uncertainty missing in 2016 datasets
        if syst == "jesRelativeSample_2016":
            return nom

        jec_to_correlate = self.correlation_scheme[syst]
        squared_sum_x = 0
        squared_sum_y = 0

        if (len(jec_to_correlate)==1):
            j=jec_to_correlate[0]
            MET_syst = ROOT.TLorentzVector()
            MET_syst.SetPtEtaPhiM(attr["MET_pt"][j][Q][0], 0.0, attr["MET_phi"][j][Q][0], 0.0)
            MET_syst_x = MET_syst.X()
            MET_syst_y = MET_syst.Y()
            squared_sum_x += (MET_syst_x - MET_nom_x)
            squared_sum_y += (MET_syst_y - MET_nom_y)
            px = MET_nom_x+(squared_sum_x)
            py = MET_nom_y+(squared_sum_y)
            return math.atan2(py, px)
        else:         
            for j in jec_to_correlate:
                MET_syst = ROOT.TLorentzVector()
                MET_syst.SetPtEtaPhiM(attr["MET_pt"][j][Q][0], 0.0, attr["MET_phi"][j][Q][0], 0.0)
                MET_syst_x = MET_syst.X()
                MET_syst_y = MET_syst.Y()
                squared_sum_x += (MET_syst_x - MET_nom_x)**2
                squared_sum_y += (MET_syst_y - MET_nom_y)**2
            if Q == "Up":
                px = MET_nom_x+np.sqrt(squared_sum_x)
                py = MET_nom_y+np.sqrt(squared_sum_y)
                return math.atan2(py, px)
            if Q == "Down":
                px = MET_nom_x-np.sqrt(squared_sum_x)
                py = MET_nom_y-np.sqrt(squared_sum_y)
                return math.atan2(py, px)

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
          
            nJet = tree.nJet
            nFatJet = tree.nFatJet

            attr = {}
            for var in ["Jet_pt", "Jet_mass", "MET_pt", "MET_phi", "FatJet_pt", "FatJet_msoftdrop"]:
                attr[var] ={}
                attr[var]["nom"] = getattr(self,var.lower()+"_nom")
            for var in ["Jet_pt", "Jet_mass", "MET_pt", "MET_phi", "FatJet_pt", "FatJet_msoftdrop"]:
                for syst in self.JEC_full:
                    attr[var][syst] = {}
                    for Q in self._variations(syst):
                        attr[var][syst][Q] = getattr(self,var.lower()+"_"+syst+Q)
            

            for syst in self.JEC_reduced:
                for Q in self._variations(syst):
                   
                    # update Jet_pt and Jet_mass variations 
                    for i in range(nJet):
                        self._b(self._v("Jet_pt", syst, Q, ""))[i] = self.correlator(syst,i,Q,"Jet_pt",attr)
                        self._b(self._v("Jet_mass", syst, Q, ""))[i] = self.correlator(syst,i,Q,"Jet_mass",attr)

                    # update MET_pt and MET_phi variations
                    self._b(self._v("MET_pt", syst, Q, ""))[0] = self.correlator(syst,0,Q,"MET_pt",attr) 
                    self._b(self._v("MET_phi", syst, Q, ""))[0] = self.METPhicorrelator(syst,Q,"MET_phi",attr)

                    for i in range(nFatJet):
                        self._b(self._v("FatJet_pt", syst, Q, ""))[i] = self.correlator(syst,i,Q,"FatJet_pt",attr)
                        self._b(self._v("FatJet_msoftdrop", syst, Q, ""))[i] = self.correlator(syst,i,Q,"FatJet_msoftdrop",attr)

            self.nEvent += 1
            if self.nEvent % 1000 == 0:
                t2 = time.time()
                tot_time = t2 - self.t0

                print("Processed {0} events in {1:.2f} seconds, {2:.2f} ev/s".format(self.nEvent, tot_time, self.nEvent/tot_time))
