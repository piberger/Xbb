#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os

from BranchTools import Collection
from BranchTools import AddCollectionsModule

class Jet :
    def __init__(self, pt, eta, fl, csv) :
        self.pt = pt
        self.eta = eta
        self.hadronFlavour = fl
        self.csv = csv

class BTagWeights(AddCollectionsModule):

    def __init__(self, fileCSV=None, fileCMVA=None, nano=False, useLeaves=False, includeFixPtEtaBins=True, branchName=None):
        super(BTagWeights, self).__init__()
        self.nano = nano
        self.useLeaves = useLeaves
        self.includeFixPtEtaBins = includeFixPtEtaBins
        self.branchBaseName = branchName if branchName else "bTagWeightCMVAV2"
        self.lastEntry = -1
        self.branchBuffers = {}
        self.branches = []
        print 'load BTagCalibrationStandalone...'
        self.btagCalibratorFileName = "../interface/BTagCalibrationStandalone_cpp.so"
        if os.path.isfile(self.btagCalibratorFileName):
            ROOT.gSystem.Load(self.btagCalibratorFileName)
        else:
            print "\x1b[31m:ERROR: BTagCalibrationStandalone not found! Go to Xbb directory and run 'make'!\x1b[0m"
            raise Exception("BTagCalibrationStandaloneNotFound")
        print 'load bTag CSV files...'
        self.calib_csv = ROOT.BTagCalibration("csvv2", fileCSV if fileCSV else  "csv/CSVv2_Moriond17_B_H.csv")
        self.calib_cmva = ROOT.BTagCalibration("cmvav2", fileCMVA if fileCMVA else "csv/cMVAv2_Moriond17_B_H.csv")
        # map between algo/flavour and measurement type
        self.sf_type_map = {
            "CSV" : {
                "file" : self.calib_csv,
                "bc" : "comb",
                "l" : "incl",
                },
            "CMVAV2" : {
                "file" : self.calib_cmva,
                "bc" : "ttbar",
                "l" : "incl",
                }
            }

        # map of calibrators. E.g. btag_calibrators["CSVM_nominal_bc"], btag_calibrators["CSVM_up_l"], ...
        self.sysRefMap = {}
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

        self.btag_calibrators = {}
        for algo in ["CSV", "CMVAV2"]:
            print "[btagSF]: Loading calibrator for algo:", algo, "systematic: all"
            self.btag_calibrators[algo+"_iterative"] = ROOT.BTagCalibrationReader(3, "central", v_sys)
            for fl in range(3):
                self.btag_calibrators[algo+"_iterative"].load(self.sf_type_map[algo]["file"], fl, "iterativefit")
        print 'INFO: bTag initialization done.'

    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'
        if not self.isData:
            self.systBranches = [""] #nominal
            self.systBranches += [syst + sdir for syst in self.systList for sdir in self.systVars]
            if self.includeFixPtEtaBins:
                self.systBranches += [syst+"_pt"+str(ipt)+"_eta"+str(ieta)+sdir for syst in self.systList for sdir in self.systVars for ipt in range(0,5) for ieta in range(1,4)]

            self.btagCollection = Collection(self.branchBaseName, self.systBranches, leaves=self.useLeaves)
            self.addCollection(self.btagCollection)
            print "sys:", self.systBranches

    def getBranches(self):
        return self.branches

    # read from buffers which have been filled in processEvent()    
    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

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
    def get_SF(self, pt=30., eta=0.0, fl=5, val=0.0, syst="central", algo="CSV", wp="M", shape_corr=False):
        
        # the .csv files use the convention: b=0, c=1, l=2. Convert into hadronFlavour convention: b=5, c=4, f=0
        fl_index = min(-fl+5,2)
        sf = self.btag_calibrators[algo+"_iterative"].eval_auto_bounds(syst if self.applies(fl, syst) else "central", fl_index, eta, pt, val)
        if sf < 0.01 and fl_index==0:
            print 'sf is 0 for:', fl_index ,eta, pt, val, algo+"_iterative_"+syst
        return sf

    def get_event_SF(self, ptmin, ptmax, etamin, etamax, jets=[], syst="central", algo="CSV"):
        weight = 1.0

        #print 'gonna add the jet SF'
        for jet in jets:
            #print 'ptmin', ptmin, 'ptmax', ptmax, 'etamin', etamin, 'etamax', etamax
            #print 'jet: pt', jet.pt, 'eta', jet.eta
            if (jet.pt > ptmin and jet.pt < ptmax and abs(jet.eta) > etamin and abs(jet.eta) < etamax):
                weight *= self.get_SF(pt=jet.pt, eta=jet.eta, fl=jet.hadronFlavour, val=jet.csv, syst=syst, algo=algo, wp="", shape_corr=True)
            else:
                weight *= self.get_SF(pt=jet.pt, eta=jet.eta, fl=jet.hadronFlavour, val=jet.csv, syst="central", algo=algo, wp="", shape_corr=True)
        return weight

    # compute all the btag weights
    def processEvent(self, tree):

        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree) and not self.isData:
            self.markProcessed(tree)

            jets_csv = []
            jets_cmva = []

            if self.nano:
                for i in range(tree.nJet):
                    # if (tree.Jet_bReg[i]*tree.Jet_Pt[i]/tree.Jet_pt[i] > 20 and abs(tree.Jet_eta[i]) < 2.4):
                    #    jet_cmva = Jet(tree.Jet_bReg[i]*tree.Jet_Pt[i]/tree.Jet_pt[i], tree.Jet_eta[i], tree.Jet_hadronFlavour[i], tree.Jet_btagCMVA[i])

                    #Modifed for 2016 Nano v4
                    if (tree.Jet_PtReg[i] > 20 and abs(tree.Jet_eta[i]) < 2.4):
                        jet_cmva = Jet(tree.Jet_PtReg[i], tree.Jet_eta[i], tree.Jet_hadronFlavour[i], tree.Jet_btagCMVA[i])
                        jets_cmva.append(jet_cmva)
            else:
                for i in range(tree.nJet):
                    if (tree.Jet_pt_reg[i] > 20 and abs(tree.Jet_eta[i]) < 2.4):
                        jet_cmva = Jet(tree.Jet_pt_reg[i], tree.Jet_eta[i], tree.Jet_hadronFlavour[i], tree.Jet_btagCMVAV2[i])
                        jets_cmva.append(jet_cmva)

            ptmin = 20.
            ptmax = 1000.
            etamin = 0.
            etamax = 2.4

            central_SF = self.get_event_SF(ptmin, ptmax, etamin, etamax, jets_cmva, "central", "CMVAV2")
            self.btagCollection.setProperty('', central_SF)

            for syst in ["JES", "LF", "HF", "LFStats1", "LFStats2", "HFStats1", "HFStats2", "cErr1", "cErr2"]:
                for sdir in ["Up", "Down"]:
                    self.btagCollection.setProperty(syst + sdir, self.get_event_SF( ptmin, ptmax, etamin, etamax, jets_cmva, self.sysMap[syst+sdir], "CMVAV2"))

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
                            self.btagCollection.setProperty(sysName, self.get_event_SF(ptmin, ptmax, etamin, etamax, jets_cmva, self.sysMap[syst+sdir], "CMVAV2"))
        return True
