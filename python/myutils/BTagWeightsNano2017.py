#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule

class Jet:
    def __init__(self, pt, eta, fl, csv) :
        self.pt = pt
        self.eta = eta
        self.hadronFlavour = fl
        self.csv = csv

# example how to included it in config for sys step:
# BTagWeights = BTagWeightsNano2017.BTagWeights(calibName='DeepCSV',calibFile='DeepCSV_94XSF_V1_B_F.csv')

class BTagWeights(AddCollectionsModule):

    def __init__(self, calibName, calibFile, method="iterativefit", branchName=None, jetBtagBranchName="Jet_btagDeepB", includeFixPtEtaBins=False, jetPtBranchName="Jet_Pt"):
        super(BTagWeights, self).__init__()
        self.jetPtBranchName = jetPtBranchName
        self.method = method
        self.calibName = calibName
        self.includeFixPtEtaBins = includeFixPtEtaBins
        self.branchBaseName = branchName if branchName else "bTagWeight"+calibName
        self.jetBtagBranchName = jetBtagBranchName
        
        # map of calibrators. E.g. btag_calibrators["CSVM_nominal_bc"], btag_calibrators["CSVM_up_l"], ...
        self.sysMap = {
                    "JESUp": "up_jes",
                    "JESDown": "down_jes",
                    "LFUp": "up_lf",
                    "LFDown": "down_lf",
                    "HFUp": "up_hf",
                    "HFDown": "down_hf",
                    "HFStats1Up": "up_hfstats1",
                    "HFStats1Down": "down_hfstats1",
                    "HFStats2Up": "up_hfstats2",
                    "HFStats2Down": "down_hfstats2",
                    "LFStats1Up": "up_lfstats1",
                    "LFStats1Down": "down_lfstats1",
                    "LFStats2Up": "up_lfstats2",
                    "LFStats2Down": "down_lfstats2",
                    "cErr1Up": "up_cferr1",
                    "cErr1Down": "down_cferr1",
                    "cErr2Up": "up_cferr2",
                    "cErr2Down": "down_cferr2",
                }
        self.systList = ["JES", "LF", "HF", "LFStats1", "LFStats2", "HFStats1", "HFStats2", "cErr1", "cErr2"]
        self.systVars = ["Up", "Down"]
        self.systematics = ["central", "up_jes", "down_jes", "up_lf", "down_lf", "up_hf", "down_hf", "up_hfstats1", "down_hfstats1", "up_hfstats2", "down_hfstats2", "up_lfstats1", "down_lfstats1", "up_lfstats2", "down_lfstats2", "up_cferr1", "down_cferr1", "up_cferr2", "down_cferr2"]

        v_sys = getattr(ROOT, 'vector<string>')()
        for syst in self.systematics:
            v_sys.push_back(syst)

        print 'load BTagCalibrationStandalone...'
        self.btagCalibratorFileName = "../interface/BTagCalibrationStandalone_cpp.so"
        if os.path.isfile(self.btagCalibratorFileName):
            ROOT.gSystem.Load(self.btagCalibratorFileName)
        else:
            print "\x1b[31m:ERROR: BTagCalibrationStandalone not found! Go to Xbb directory and run 'make'!\x1b[0m"
            raise Exception("BTagCalibrationStandaloneNotFound")

        print 'load bTag CSV files...'
        calib = ROOT.BTagCalibration(calibName, calibFile)
        self.btag_calibrators = {}
        print "[btagSF]: Loading calibrator for algo:", self.calibName
        self.btag_calibrators[self.calibName+"_iterative"] = ROOT.BTagCalibrationReader(3, "central", v_sys)
        for fl in range(3):
            self.btag_calibrators[self.calibName+"_iterative"].load(calib, fl, self.method)

        print 'INFO: bTag initialization done.'


    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'
        if not self.isData:
            self.systBranches = [""] #nominal
            self.systBranches += [syst + sdir for syst in self.systList for sdir in self.systVars]
            if self.includeFixPtEtaBins:
                self.systBranches += [syst+"_pt"+str(ipt)+"_eta"+str(ieta)+sdir for syst in self.systList for sdir in self.systVars for ipt in range(0,5) for ieta in range(1,4)]

            self.btagCollection = Collection(self.branchBaseName, self.systBranches, leaves=False)
            self.addCollection(self.btagCollection)
            print "sys:", self.systBranches

    # depending on flavour, only a sample of systematics matter
    def applies(self, flavour, syst):
        if flavour==5 and syst not in ["central", "up_jes", "down_jes",  "up_lf", "down_lf",  "up_hfstats1", "down_hfstats1", "up_hfstats2", "down_hfstats2"]:
            return False
        elif flavour==4 and syst not in ["central", "up_cferr1", "down_cferr1", "up_cferr2", "down_cferr2" ]:
            return False
        elif flavour==0 and syst not in ["central", "up_jes", "down_jes", "up_hf", "down_hf",  "up_lfstats1", "down_lfstats1", "up_lfstats2", "down_lfstats2" ]:
            return False
        return True

    # function that reads the SF
    def get_SF(self, pt=30., eta=0.0, fl=5, val=0.0, syst="central", algo="CSV", wp="M"):
        
        # the .csv files use the convention: b=0, c=1, l=2. (fl_index)
        # hadronFlavour convention: b=5, c=4, f=0  (fl)
        fl_index = min(-fl+5,2)
        sf = self.btag_calibrators[algo+"_iterative"].eval_auto_bounds(syst if self.applies(fl, syst) else "central", fl_index, eta, pt, val)
        return sf

    def get_event_SF(self, ptmin, ptmax, etamin, etamax, jets=[], syst="central", algo="CSV"):
        weight = 1.0

        #print 'gonna add the jet SF'
        for jet in jets:
            if (jet.pt > ptmin and jet.pt < ptmax and abs(jet.eta) > etamin and abs(jet.eta) < etamax):
                weight *= self.get_SF(pt=jet.pt, eta=jet.eta, fl=jet.hadronFlavour, val=jet.csv, syst=syst, algo=algo, wp="")
            else:
                weight *= self.get_SF(pt=jet.pt, eta=jet.eta, fl=jet.hadronFlavour, val=jet.csv, syst="central", algo=algo, wp="")
        return weight
    
    # compute all the btag weights
    def processEvent(self, tree):

        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree) and not self.isData:
            self.markProcessed(tree)

            jets_cmva = []
            treeJet_Pt = getattr(tree, self.jetPtBranchName)
            for i in range(tree.nJet):
                if (tree.Jet_bReg[i]*treeJet_Pt[i]/tree.Jet_pt[i] > 20 and abs(tree.Jet_eta[i]) < 2.4 and tree.Jet_lepFilter[i] > 0):
                    jet_cmva = Jet(tree.Jet_bReg[i]*treeJet_Pt[i]/tree.Jet_pt[i], tree.Jet_eta[i], tree.Jet_hadronFlavour[i], getattr(tree,self.jetBtagBranchName)[i])
                    jets_cmva.append(jet_cmva)

            ptmin = 20.
            ptmax = 1000.
            etamin = 0.
            etamax = 2.4

            central_SF = self.get_event_SF(ptmin, ptmax, etamin, etamax, jets_cmva, "central", self.calibName)
            self.btagCollection[''][0] = central_SF

            for syst in ["JES", "LF", "HF", "LFStats1", "LFStats2", "HFStats1", "HFStats2", "cErr1", "cErr2"]:
                for sdir in ["Up", "Down"]:
                    self.btagCollection[syst + sdir][0] = self.get_event_SF( ptmin, ptmax, etamin, etamax, jets_cmva, self.sysMap[syst+sdir], self.calibName)

                    if self.includeFixPtEtaBins:
                        for ipt in range(0,5):

                            ptmin = 20.
                            ptmax = 1000.
                            etamin = 0.
                            etamax = 2.4

                            if ipt == 0:
                                ptmin = 20.
                                ptmax = 30.
                            elif ipt == 1:
                                ptmin = 30.
                                ptmax = 40.
                            elif ipt ==2:
                                ptmin = 40.
                                ptmax = 60.
                            elif ipt ==3:
                                ptmin = 60.
                                ptmax = 100.
                            elif ipt ==4:
                                ptmin = 100.
                                ptmax = 1000.

                            for ieta in range(1,4):
                                if ieta ==1:
                                    etamin = 0.
                                    etamax = 0.8
                                elif ieta ==2:
                                    etamin = 0.8
                                    etamax = 1.6
                                elif ieta ==3:
                                    etamin = 1.6
                                    etamax = 2.4

                                sysName = syst+"_pt"+str(ipt)+"_eta"+str(ieta)+sdir
                                self.btagCollection[sysName][0] = self.get_event_SF(ptmin, ptmax, etamin, etamax, jets_cmva, self.sysMap[syst+sdir], self.calibName)
        return True
