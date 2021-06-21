#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os
import math
import numpy as np
from XbbConfig import XbbConfigTools
import time
from XbbConfig import XbbConfigReader, XbbConfigTools
from sample_parser import ParseInfo
from BranchList import BranchList
from FileLocator import FileLocator
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double
from sampleTree import SampleTree
import copy
import csv

# correlates the JECs according to new JEC correlation scheme (V11 -> V13) 
class JECcorrelator(AddCollectionsModule):

    def __init__(self, year):
        super(JECcorrelator, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.quickloadWarningShown = False
        self.existingBranches = {}

        self.year = year if type(year) == str else str(year)

    # only add as new branch if they don't exists already
    def addVectorBranch(self, branchName, default=0, branchType='d', length=1, leaflist=None):
        if branchName not in self.existingBranches:
            super(JECcorrelator, self).addVectorBranch(branchName, default, branchType, length, leaflist)
        else:
            print("DEBUG: skip adding branch:", branchName)
    def addBranch(self, branchName, default=0.0):
        if branchName not in self.existingBranches:
            super(JECcorrelator, self).addBranch(branchName, default)
        else:
            print("DEBUG: skip adding branch:", branchName)

    # can be used to overwrite branch if it already exists
    def _b(self, branchName):
        if branchName not in self.existingBranches:
            return super(JECcorrelator, self)._b(branchName)
        else:
            return self.existingBranches[branchName]

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

        self.correlation_scheme_for_met = {}
        for i in self.correlation_scheme: self.correlation_scheme_for_met[i] = [i]
        if self.debug: 
            print("correlation_scheme_for_met is ",self.correlation_scheme_for_met)

        if self.sample.isMC():

            self.JEC_reduced = self.correlation_scheme.keys()
            self.JEC_full    = sum([v for k,v in self.correlation_scheme.items()], [])

            if self.debug: 
                print("JEC_reduced : ",self.JEC_reduced)
                print("JEC_full : ",self.JEC_full)

            self.maxNjet   = 256
            self.maxNfatjet = 50
            self.nEvent = 0

            # load needed information
            for syst in self.JEC_full+["nom"]:
                if syst != "nom": UD = ["Up","Down"]
                else: UD = [""]
                for Q in UD:
                    for v in ["Jet_pt_"+syst+Q, "Jet_mass_"+syst+Q, "MET_pt_"+syst+Q, "MET_phi_"+syst+Q, "FatJet_pt_"+syst+Q, "FatJet_msoftdrop_"+syst+Q]:
                        if v.startswith('Jet_'):
                            self.existingBranches[v] = array.array('f', [0.0]*self.maxNjet)
                        elif v.startswith('FatJet_'):
                            self.existingBranches[v] = array.array('f', [0.0]*self.maxNfatjet)
                        else:
                            self.existingBranches[v] = array.array('f', [0.0])

                        self.sampleTree.tree.SetBranchAddress(v, self.existingBranches[v])

            for var in ["Jet_eta","Jet_phi","Jet_neEmEF","Jet_chEmEF"]:
                self.existingBranches[var] = array.array('f', [0.0]*self.maxNjet)
                self.sampleTree.tree.SetBranchAddress(var, self.existingBranches[var])

            for var in ["Jet_muonIdx1","Jet_muonIdx2"]:
                self.existingBranches[var] = array.array('i', [0]*self.maxNjet)
                self.sampleTree.tree.SetBranchAddress(var, self.existingBranches[var])

            for var in ["nJet","nMuon"]:
                self.existingBranches[var] = array.array('i', [0])
                self.sampleTree.tree.SetBranchAddress(var, self.existingBranches[var])

            for var in ["Muon_pt"]:
                self.existingBranches[var] = array.array('f', [0.0]*50)
                self.sampleTree.tree.SetBranchAddress(var, self.existingBranches[var])

            for var in ["Jet_eta","Jet_phi","Jet_neEmEF","Jet_chEmEF"]:
                setattr(self,var.lower(),array.array('f', [0.0]*self.maxNjet))
                self.sampleTree.tree.SetBranchAddress(var, getattr(self, var.lower()))

            for var in ["Jet_muonIdx1","Jet_muonIdx2"]:
                setattr(self,var.lower(),array.array('i', [0]*self.maxNjet))
                self.sampleTree.tree.SetBranchAddress(var, getattr(self, var.lower()))

            for var in ["nJet","nMuon"]:
                setattr(self,var.lower(),array.array('i', [0]))
                self.sampleTree.tree.SetBranchAddress(var, getattr(self, var.lower()))

            for var in ["Muon_pt"]:
                setattr(self,var.lower(),array.array('f', [0.0]*50))
                self.sampleTree.tree.SetBranchAddress(var, getattr(self, var.lower()))

            for syst in self.JEC_reduced:
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
                    
    def maxmin(self, Q, sum_1, sum_2):
        if Q == "Up":
            return max(sum_1,sum_2)
        if Q == "Down":
            return min(sum_1,sum_2)
                    
    def correlator(self,syst,idx,Q,var,attr):

        nom = attr[var]["nom"][idx]

        # RelativeSample uncertainty missing in 2016 datasets
        if syst == "jesRelativeSample_2016":
            return nom
        jec_to_correlate = self.correlation_scheme[syst]
        squared_sum_1 = 0
        squared_sum_2 = 0
        sum_1 = 0
        sum_2 = 0
        if (len(jec_to_correlate)==1):
            j=jec_to_correlate[0]
            if var=="FatJet_msoftdrop":
                squared_sum_1 = (attr[var][j]['Up'][idx])*nom - nom
                squared_sum_2 = (attr[var][j]['Down'][idx])*nom - nom
            else:    
                squared_sum_1 = attr[var][j]['Up'][idx] - nom
                squared_sum_2 = attr[var][j]['Down'][idx] - nom
            sum_1 = nom+(squared_sum_1)
            sum_2 = nom+(squared_sum_2)
        else:
            for j in jec_to_correlate:
                if var=="FatJet_msoftdrop":
                    squared_sum_1 += ((attr[var][j]['Up'][idx])*nom - nom)**2
                    squared_sum_2 += ((attr[var][j]['Down'][idx])*nom - nom)**2   
                else: 
                    squared_sum_1 += (attr[var][j]['Up'][idx] - nom)**2
                    squared_sum_2 += (attr[var][j]['Down'][idx] - nom)**2   
            sum_1 = nom+np.sqrt(squared_sum_1)
            sum_2 = nom-np.sqrt(squared_sum_2)
        return self.maxmin(Q, sum_1, sum_2)
    
    def METcorrelator(self,syst,Q,var,attr):
        MET_nom = ROOT.TLorentzVector()
        MET_nom.SetPtEtaPhiM(attr["MET_pt"]["nom"][0], 0.0, attr["MET_phi"]["nom"][0], 0.0)
        met_px_nom = MET_nom.X()
        met_py_nom = MET_nom.Y()
        
        if syst == "jesRelativeSample_2016":
            if var=="MET_pt": return attr["MET_pt"]["nom"][0]
            if var=="MET_phi": return attr["MET_phi"]["nom"][0]

        met_px_sys = {"Up":[],"Down":[]}
        met_py_sys = {"Up":[],"Down":[]}

        jec_to_correlate = self.correlation_scheme_for_met[syst]
         
        for q in ["Up","Down"]:
            for j in jec_to_correlate:
                sum_rel_px_jsys = 0  
                sum_rel_py_jsys = 0 
                met_px_jsys = 0
                met_py_jsys = 0
                njets_selected = 0
                for i in range(attr["nJet"]):
                    muon_in_jet_pt = 0
                    if (attr["Jet_muonIdx1"][i]>-1): muon_in_jet_pt += attr["Muon_pt"][attr["Jet_muonIdx1"][i]]
                    if (attr["Jet_muonIdx2"][i]>-1): muon_in_jet_pt += attr["Muon_pt"][attr["Jet_muonIdx2"][i]]
                    if (((attr["Jet_neEmEF"][i] + attr["Jet_chEmEF"][i]) < 0.9) and ((attr["Jet_pt"]["nom"][i] - muon_in_jet_pt) > 15.0)):
                        njets_selected += 1
                        sum_rel_px_jsys += (attr["Jet_pt"][j][q][i]*np.cos(attr["Jet_phi"][i]) - attr["Jet_pt"]["nom"][i]*np.cos(attr["Jet_phi"][i]))
                        sum_rel_py_jsys += (attr["Jet_pt"][j][q][i]*np.sin(attr["Jet_phi"][i]) - attr["Jet_pt"]["nom"][i]*np.sin(attr["Jet_phi"][i]))
                if njets_selected == 0:
                    if var=="MET_pt":
                        return attr["MET_pt"]["nom"][0]
                    if var=="MET_phi":
                        return attr["MET_phi"]["nom"][0]                    
                else:    
                    met_px_jsys = met_px_nom - sum_rel_px_jsys
                    met_py_jsys = met_py_nom - sum_rel_py_jsys
                    met_px_sys[q].append(met_px_jsys)
                    met_py_sys[q].append(met_py_jsys)


        sum_rel_px_sys_1,sum_rel_px_sys_2 = 0,0
        sum_rel_py_sys_1,sum_rel_py_sys_2 = 0,0
        met_px_sys_Reduced_1,met_px_sys_Reduced_2 = 0,0
        met_py_sys_Reduced_1,met_py_sys_Reduced_2 = 0,0
        met_pt_sys_Reduced_1,met_pt_sys_Reduced_2 = 0,0
        met_phi_sys_Reduced_1,met_phi_sys_Reduced_2 = 0,0
        
        if (len(jec_to_correlate)==1):
            sum_rel_px_sys_1 += (met_px_sys['Up'][0] - met_px_nom)
            sum_rel_py_sys_1 += (met_py_sys['Up'][0] - met_py_nom)
            met_px_sys_Reduced_1 = (sum_rel_px_sys_1) + met_px_nom
            met_py_sys_Reduced_1 = (sum_rel_py_sys_1) + met_py_nom
            sum_rel_px_sys_2 += (met_px_sys['Down'][0] - met_px_nom)
            sum_rel_py_sys_2 += (met_py_sys['Down'][0] - met_py_nom)
            met_px_sys_Reduced_2 = (sum_rel_px_sys_2) + met_px_nom
            met_py_sys_Reduced_2 = (sum_rel_py_sys_2) + met_py_nom
            if var=="MET_pt":
                met_pt_sys_Reduced_1 = np.sqrt(met_px_sys_Reduced_1**2 + met_py_sys_Reduced_1**2)
                met_pt_sys_Reduced_2 = np.sqrt(met_px_sys_Reduced_2**2 + met_py_sys_Reduced_2**2)
                if Q=="Up": return met_pt_sys_Reduced_1 
                if Q =="Down": return met_pt_sys_Reduced_2 
                #return self.maxmin(Q,met_pt_sys_Reduced_1,met_pt_sys_Reduced_2)
            if var=="MET_phi":
                met_phi_sys_Reduced_1 = math.atan2(met_py_sys_Reduced_1, met_px_sys_Reduced_1)
                met_phi_sys_Reduced_2 = math.atan2(met_py_sys_Reduced_2, met_px_sys_Reduced_2)
                if Q=="Up": return met_phi_sys_Reduced_1 
                if Q =="Down": return met_phi_sys_Reduced_2 
                #return self.maxmin(Q,met_phi_sys_Reduced_1,met_phi_sys_Reduced_2)

        else: 
            for j in range(len(jec_to_correlate)):
                sum_rel_px_sys_1 += (met_px_sys['Up'][j] - met_px_nom)**2
                sum_rel_py_sys_1 += (met_py_sys['Up'][j] - met_py_nom)**2
                sum_rel_px_sys_2 += (met_px_sys['Down'][j] - met_px_nom)**2
                sum_rel_py_sys_2 += (met_py_sys['Down'][j] - met_py_nom)**2
            met_px_sys_Reduced_1 = met_px_nom + np.sqrt(sum_rel_px_sys_1)   
            met_py_sys_Reduced_1 = met_py_nom + np.sqrt(sum_rel_py_sys_1)
            met_px_sys_Reduced_2 = met_px_nom - np.sqrt(sum_rel_px_sys_2)   
            met_py_sys_Reduced_2 = met_py_nom - np.sqrt(sum_rel_py_sys_2)
            
            if var=="MET_pt":
                met_pt_sys_reduced_1 = np.sqrt(met_px_sys_reduced_1**2 + met_py_sys_reduced_1**2)
                met_pt_sys_reduced_2 = np.sqrt(met_px_sys_reduced_2**2 + met_py_sys_reduced_2**2)
                #use following to return statements if you do not want to keep up>down convention
                if Q=="Up": return met_pt_sys_reduced_1 
                if Q=="Down": return met_pt_sys_reduced_2 
                #following line will force up>down variation
                #return self.maxmin(Q, met_pt_sys_reduced_1, met_pt_sys_reduced_2)
            if var=="MET_phi":
                met_phi_sys_reduced_1 = math.atan2(met_py_sys_reduced_1, met_px_sys_reduced_1)
                met_phi_sys_reduced_2 = math.atan2(met_py_sys_reduced_2, met_px_sys_reduced_2)
                #use following to return statements if you do not want to keep up>down convention
                if Q=="Up": return met_phi_sys_reduced_1
                if Q=="Down": return met_phi_sys_reduced_2 
                #following line will force up>down variation
                #return self.maxmin(Q, met_phi_sys_reduced_1, met_phi_sys_reduced_2)

    def eventCheck(self,event):
        if (self.event.MET_pt_nom>140):
            return True
        else:
            return False

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and self.sample.isMC():
            self.markProcessed(tree)
          
            nJet = tree.nJet
            nFatJet = tree.nFatJet

            attr = {}
            for var in ["Jet_pt", "Jet_mass", "MET_pt", "MET_phi", "FatJet_pt", "FatJet_msoftdrop"]:
                attr[var] ={}
                attr[var]["nom"] = self.existingBranches[var+"_nom"]
            for var in ["Jet_eta", "Jet_phi", "Jet_neEmEF", "Jet_chEmEF", "Muon_pt","Jet_muonIdx1","Jet_muonIdx2"]:
                attr[var] = self.existingBranches[var]
            attr["nMuon"] = tree.nMuon
            attr["nJet"]  = tree.nJet
            for var in ["Jet_pt", "Jet_mass", "MET_pt", "MET_phi", "FatJet_pt", "FatJet_msoftdrop"]:
                for syst in self.JEC_full:
                    #print("syst :",syst)
                    attr[var][syst] = {}
                    for Q in self._variations(syst):
                        attr[var][syst][Q] = list(self.existingBranches[var+"_"+syst+Q])
            for var in ["Jet_pt", "Jet_mass"]:
                for syst in self.JEC_reduced:
                    if syst not in attr[var]:
                        attr[var][syst] = {}
                        for Q in self._variations(syst):
                            attr[var][syst][Q] = []
            for syst in self.JEC_reduced:
                for Q in self._variations(syst):
                   
                    # update Jet_pt and Jet_mass variations 
                    for i in range(nJet):
                        pt   = self.correlator(syst,i,Q,"Jet_pt",attr)
                        mass = self.correlator(syst,i,Q,"Jet_mass",attr)
                        self._b(self._v("Jet_pt", syst, Q, ""))[i] = pt
                        self._b(self._v("Jet_mass", syst, Q, ""))[i] = mass
                        attr["Jet_pt"][syst][Q].append(pt)
                        attr["Jet_mass"][syst][Q].append(mass)

                for Q in self._variations(syst):
                    # update MET_pt and MET_phi variations
                    self._b(self._v("MET_pt", syst, Q, ""))[0] = self.METcorrelator(syst,Q,"MET_pt",attr) 
                    self._b(self._v("MET_phi", syst, Q, ""))[0] = self.METcorrelator(syst,Q,"MET_phi",attr)

                    for i in range(nFatJet):
                        self._b(self._v("FatJet_pt", syst, Q, ""))[i] = self.correlator(syst,i,Q,"FatJet_pt",attr)
                        self._b(self._v("FatJet_msoftdrop", syst, Q, ""))[i] = self.correlator(syst,i,Q,"FatJet_msoftdrop",attr)
                        if ((getattr(self,"fatjet_msoftdrop"+"_"+syst+Q)[i]>0) and (getattr(self,"fatjet_pt"+"_"+syst+Q)[i]>0)):
                            #histograms["FatJet_pt"][syst][Q].Fill((getattr(self,"fatjet_pt"+"_"+syst+Q)[i] - self._b(self._v("FatJet_pt", syst, Q, ""))[i])/(getattr(self,"fatjet_pt"+"_"+syst+Q)[i])) 
                            #histograms["FatJet_msoftdrop"][syst][Q].Fill((getattr(self,"fatjet_msoftdrop"+"_"+syst+Q)[i] - self._b(self._v("FatJet_msoftdrop", syst, Q, ""))[i])/(getattr(self,"fatjet_msoftdrop"+"_"+syst+Q)[i])) 
                            attr["FatJet_pt"][syst][Q].append(self._b(self._v("FatJet_pt", syst, Q, ""))[i])
                            attr["FatJet_msoftdrop"][syst][Q].append(self._b(self._v("FatJet_msoftdrop", syst, Q, ""))[i])
                            #true_attr["FatJet_pt"][syst][Q].append(getattr(self,"fatjet_pt"+"_"+syst+Q)[i])
                            #true_attr["FatJet_msoftdrop"][syst][Q].append(getattr(self,"fatjet_msoftdrop"+"_"+syst+Q)[i])

            #self.nEvent += 1
            #if self.nEvent % 1000 == 0:
            #    t2 = time.time()
            #    tot_time = t2 - self.t0

            #   print("Processed {0} events in {1:.2f} seconds, {2:.2f} ev/s".format(self.nEvent, tot_time, self.nEvent/tot_time))




if __name__=='__main__':

    config = XbbConfigReader.read('Zvv2018')
    info = ParseInfo(config=config)
    sample = [x for x in info if x.identifier == 'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8'][0]

    #sampleTree = SampleTree(['/store/group/phys_higgs/hbb/ntuples/VHbbPostNano/2018/V12/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25O133/200221_205457/0000/tree_1.root'], treeName='Events', xrootdRedirector="root://eoscms.cern.ch/")
    sampleTree = SampleTree(['/store/group/phys_higgs/hbb/ntuples/VHbbPostNano/2018/V13/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02A85/200519_095652/0000/tree_1.root'], treeName='Events', xrootdRedirector="root://eoscms.cern.ch/")
    w = JECcorrelator("2018")
    w.customInit({'sampleTree': sampleTree, 'sample': sample, 'config': config})
    sampleTree.addOutputBranches(w.getBranches())
    histograms={}
    for jec in w.JEC_reduced:                                                                                                                   histograms[jec] = {}

    for var in ["Jet_pt", "Jet_mass", "MET_pt", "MET_phi", "FatJet_pt", "FatJet_msoftdrop"]:
        histograms[var] = {}
        for syst in w.JEC_reduced:
            histograms[var][syst] = {}
            for Q in ['Up','Down']:
                histograms[var][syst][Q]=ROOT.TH1F(var+syst+Q, var+syst+Q, 400, -2.0, 2.0 )

    n=0 
    #var = "MET_phi"
    for event in sampleTree:
        n=n+1
        event,run,true_attr, attr = w.processEvent(event)
        #if n==10: break

   # with open('jec_validate_'+var+'.csv', 'w') as file:
   #     writer = csv.writer(file)
   #     writer.writerow(["event","run","Q",'true_jesAbsolute','jesAbsolute','AT','diff','true_jesAbsolute_2018','jesAbsolute_2018','AT','diff','true_jesBBEC1','jesBBEC1','AT','diff','true_jesBBEC1_2018','jesBBEC1_2018','AT','diff','true_jesEC2','jesEC2','AT','diff','true_jesEC2_2018','jesEC2_2018','AT','diff','true_jesHF','jesHF','AT','diff','true_jesHF_2018','jesHF_2018','AT','diff','true_jesRelativeSample_2018','jesRelativeSample_2018','AT','diff'])
   #     for event in sampleTree:
   #         n=n+1
   #         event,run,true_attr, attr = w.processEvent(event)
   #         for Q in ['Up','Down']:
   #             njet = len(true_attr[var][w.JEC_reduced[0]][Q])
   #             if njet>1:
   #                 for i in range(njet):
   #                     writer.writerow([event,run,Q,true_attr[var]['jesAbsolute'][Q][i],attr[var]['jesAbsolute'][Q][i],'','',true_attr[var]['jesAbsolute_2018'][Q][i],attr[var]['jesAbsolute_2018'][Q][i],'','',true_attr[var]['jesBBEC1'][Q][i],attr[var]['jesBBEC1'][Q][i],'','',true_attr[var]['jesBBEC1_2018'][Q][i],attr[var]['jesBBEC1_2018'][Q][i],'','',true_attr[var]['jesEC2'][Q][i],attr[var]['jesEC2'][Q][i],'','',true_attr[var]['jesEC2_2018'][Q][i],attr[var]['jesEC2_2018'][Q][i],'','',true_attr[var]['jesHF'][Q][i],attr[var]['jesHF'][Q][i],'','',true_attr[var]['jesHF_2018'][Q][i],attr[var]['jesHF_2018'][Q][i],'','',true_attr[var]['jesRelativeSample_2018'][Q][i],attr[var]['jesRelativeSample_2018'][Q][i],'',''])
   #             else:
   #                 writer.writerow([event,run,Q,true_attr[var]['jesAbsolute'][Q][0],attr[var]['jesAbsolute'][Q][0],'','',true_attr[var]['jesAbsolute_2018'][Q][0],attr[var]['jesAbsolute_2018'][Q][0],'','',true_attr[var]['jesBBEC1'][Q][0],attr[var]['jesBBEC1'][Q][0],'','',true_attr[var]['jesBBEC1_2018'][Q][0],attr[var]['jesBBEC1_2018'][Q][0],'','',true_attr[var]['jesEC2'][Q][0],attr[var]['jesEC2'][Q][0],'','',true_attr[var]['jesEC2_2018'][Q][0],attr[var]['jesEC2_2018'][Q][0],'','',true_attr[var]['jesHF'][Q][0],attr[var]['jesHF'][Q][0],'','',true_attr[var]['jesHF_2018'][Q][0],attr[var]['jesHF_2018'][Q][0],'','',true_attr[var]['jesRelativeSample_2018'][Q][0],attr[var]['jesRelativeSample_2018'][Q][0],'',''])

   #         #print("----------events over------------")
   #         if n==5: break

    f = TFile("delete.root","RECREATE")

    for var in ["Jet_pt", "Jet_mass", "MET_pt", "MET_phi", "FatJet_pt", "FatJet_msoftdrop"]:
        for syst in w.JEC_reduced:
            for Q in ['Up','Down']:
                histograms[var][syst][Q].Write()
    f.Close()
