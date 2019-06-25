#!/usr/bin/env python
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os

# do jet/lepton selection and skimming 
class VHbbSelection(AddCollectionsModule):

    def __init__(self, debug=False, year="2018", channels=["Wln","Zll","Znn"]):
        self.debug = debug or 'XBBDEBUG' in os.environ
        self.year = year
        self.channels = channels
        self.debugEvents = []
        super(VHbbSelection, self).__init__()

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        self.sample = initVars['sample']

        # settings
        # originally Electron_mvaFall17V1Iso_WP80 was used for 2017, which was called Electron_mvaFall17Iso_WP80
        self.electronID = {
                    1: {
                                "2018": "Electron_mvaFall17V2Iso_WP80",
                                "2017": "Electron_mvaFall17V2Iso_WP80",
                                "2016": "Electron_mvaSpring16GP_WP80",
                            },
                    2: {
                                "2018": "Electron_mvaFall17V2Iso_WP90",
                                "2017": "Electron_mvaFall17V2Iso_WP90",
                                "2016": "Electron_mvaSpring16GP_WP90",
                            }
                    }

        if self.year == "2016":
            self.metFilters = ["Flag_goodVertices", "Flag_globalTightHalo2016Filter", "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter", "Flag_EcalDeadCellTriggerPrimitiveFilter"]
        elif self.year in ["2017","2018"]:
            self.metFilters = ["Flag_goodVertices", "Flag_globalTightHalo2016Filter", "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter", "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter", "Flag_BadChargedCandidateFilter", "Flag_ecalBadCalibFilter"]
        if self.isData:
            self.metFilters.append("Flag_eeBadScFilter")

        self.taggerName = "Jet_btagDeepB"
        self.btagWPs = {
                       "2018": {
                      'Jet_btagDeepB': {
                            'loose':  0.1241,
                            'medium': 0.4184,
                            'tight':  0.7527,
                            'none': -1.0,
                            },
                        },
                        "2017": {
                        'Jet_btagDeepB': {
                            'loose':  0.1522,
                            'medium': 0.4941,
                            'tight':  0.8001,
                            'none': -1.0,
                            },
                        },
                        "2016": {
                        'Jet_btagDeepB': {
                            'loose':  0.2217,
                            'medium': 0.6321,
                            'tight':  0.8953,
                            'none': -1.0,
                            },
                        },
                   }


        #self.taggerName = "Jet_btagDeepFlavB"

        #self.btagWPs = {
        #               "2018": {
        #              'Jet_btagDeepFlavB': {
        #                    'loose':  0.0494,
        #                    'medium': 0.2770,
        #                    'tight':  0.7264,
        #                    'none': -1.0,
        #                    },
        #                },
        #            }

        self.btagWP = self.btagWPs[self.year][self.taggerName]



        if self.year == "2018": 
            self.HltPaths = {
                        'Znn': ['HLT_PFMET120_PFMHT120_IDTight','HLT_PFMET120_PFMHT120_IDTight_PFHT60'],
                        'Wln': ['HLT_Ele32_WPTight_Gsf','HLT_IsoMu24'],
                        'Zll': ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8', 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'],
                        }
        elif self.year == "2017": 
            self.HltPaths = {
                        'Znn': ['HLT_PFMET120_PFMHT120_IDTight','HLT_PFMET120_PFMHT120_IDTight_PFHT60'],
                        'Wln': ['HLT_Ele32_WPTight_Gsf_L1DoubleEG','HLT_IsoMu27'],
                        'Zll': ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8', 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8', 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'],
                        }
        elif self.year == "2016":
            self.HltPaths = {
                        'Znn': [],
                        'Wln': [],
                        'Zll': ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL','HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL','HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ','HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ','HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'],
                        }
        else: 
            raise Execption("unknown year")

        self.leptonFlav = {
                'DoubleMuon': 0,
                'DoubleEG': 1,
                'SingleMuon': 2,
                'SingleElectron': 3,
                'MET': 4,
                }

        self.cutFlow = [0] * 16

        # new branches to write
        self.addIntegerBranch("isZee")
        self.addIntegerBranch("isZmm")
        self.addIntegerBranch("isWmunu")
        self.addIntegerBranch("isWenu")
        self.addIntegerBranch("isZnn")

        self.addIntegerVectorBranch("vLidx", default=-1, length=2)
        self.addIntegerVectorBranch("hJidx", default=-1, length=2)

        self.addBranch("lepMetDPhi")
        self.addBranch("V_mt")
        self.addBranch("V_pt")
        self.addBranch("V_eta")
        self.addBranch("V_phi")
        self.addBranch("V_mass")

        print "DEBUG: sample identifier:", self.sample.identifier, " lep flav", self.leptonFlav, " -> ", self.leptonFlav[self.sample.identifier] if self.sample.identifier in self.leptonFlav else "UNDEFINED LEPTON FLAVOR!!"

    def HighestPtGoodElectronsOppCharge(self, tree, min_pt, max_rel_iso, idcut, etacut, isOneLepton):
        indices = []
        for i in range(tree.nElectron):
            passEleIDCut = getattr(tree, self.electronID[1 if isOneLepton else 2][self.year])[i]
            if abs(tree.Electron_eta[i]) < etacut and tree.Electron_pt[i] > min_pt and tree.Electron_pfRelIso03_all[i] < max_rel_iso and passEleIDCut:
                if len(indices) < 1:
                    indices.append(i)
                    if isOneLepton:
                        break 
                else:
                    if tree.Electron_charge[i] * tree.Electron_charge[indices[0]] < 0:
                        indices.append(i)
                        break 
        return indices

    def HighestPtGoodMuonsOppCharge(self, tree, min_pt, max_rel_iso, idcut, etacut, isOneLepton):
        indices = []
        for i in range(tree.nMuon):
            if abs(tree.Muon_eta[i]) < etacut and tree.Muon_pt[i] > min_pt and tree.Muon_pfRelIso04_all[i] < max_rel_iso and (not isOneLepton or tree.Muon_tightId[i] > 0):
                if len(indices) < 1:
                    indices.append(i)
                    if isOneLepton:
                        break 
                else:
                    if tree.Muon_charge[i] * tree.Muon_charge[indices[0]] < 0:
                        indices.append(i)
                        break 
        return indices

    def HighestTaggerValueBJets(self, tree, j1ptCut, j2ptCut, taggerName):
        indices = []
        #print('----------------------event start')
        #print('len(tree.nJet)', tree.nJet)
        for i in range(tree.nJet):
            #print('Jet No.', i)
            #print('Jet_lepFilter', tree.Jet_lepFilter[i])
            #print('Jet_puId', tree.Jet_puId[i])
            #print('Jet_PtReg', tree.Jet_PtReg[i])
            #print('Jet_eta', abs(tree.Jet_eta[i]))  
            #print('------------------------')
            if tree.Jet_lepFilter[i] and tree.Jet_puId[i] > 0 and tree.Jet_PtReg[i] > j1ptCut and abs(tree.Jet_eta[i]) < 2.5:
                if len(indices) < 1:
                    indices.append(i)
                    #print('indices',indices)
                else:
                    if getattr(tree, taggerName)[i] > getattr(tree, taggerName)[indices[0]]:
                        indices[0] = i
        #print('indices[0] for event is', indices)
        #print('-----------------event over')
        if len(indices) > 0:
            for i in range(tree.nJet):
                if i == indices[0]:
                    continue
                if tree.Jet_lepFilter[i] and tree.Jet_puId[i] > 0 and tree.Jet_PtReg[i] > j2ptCut and abs(tree.Jet_eta[i]) < 2.5:
                    if len(indices) < 2:
                        indices.append(i)
                    else:
                        if getattr(tree, taggerName)[i] > getattr(tree, taggerName)[indices[1]]:
                            indices[1] = i

        if len(indices) > 1:
            if getattr(tree, taggerName)[indices[1]] > getattr(tree, taggerName)[indices[0]]:
                indices = [indices[1], indices[0]]
       
        return indices

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            for n in ["isZmm", "isZee", "isWenu", "isWmunu", "isZnn"]:
                self._b(n)[0] = 0
            self._b("lepMetDPhi")[0] = -99.0
            self._b("V_mt")[0] = -99.0
            self._b("V_pt")[0] = -99.0
            self._b("V_eta")[0] = -99.0
            self._b("V_phi")[0] = -99.0
            self._b("V_mass")[0] = -99.0
            self._b("hJidx")[0] = -1
            self._b("hJidx")[1] = -1
            self._b("vLidx")[0] = -1
            self._b("vLidx")[1] = -1

            self.cutFlow[0] += 1

            debugEvent = [tree.run, tree.event] in self.debugEvents
            if debugEvent:
                print "DEBUG-EVENT:", tree.run, tree.event

            # TRIGGER
            triggerPassed = {k: any([getattr(tree, x) for x in v if hasattr(tree,x)])  for k,v in self.HltPaths.items()}
            #print("------------------------------------")
            #for k,v in self.HltPaths.items():
            #    print(k,v)
            #    for x in v:
            #        print(x, hasattr(tree,x))
            #        if hasattr(tree,x):
            #            print(getattr(tree,x))
                        
            #print(triggerPassed, "triggerPassed")
            #print(self.channels, "self.channels")
            #if not ((triggerPassed['0-lep'] and "Znn" in self.channels) or (triggerPassed['1-lep'] and "Wln" in self.channels) or (triggerPassed['2-lep'] and  "Zll" in self.channels)):

            if debugEvent:
                print "triggers:", triggerPassed

            isZnn = tree.Vtype == 4 and triggerPassed['Znn']
            isWln = tree.Vtype in [2,3] and triggerPassed['Wln']
            isZll = tree.Vtype in [0,1] and triggerPassed['Zll']

            if not any([isZll, isWln, isZnn]):
                return False
            self.cutFlow[1] += 1
            #print(self.cutFlow[1], ': cutFlow[1]')
            

            # LEPTONS
            if self.sample.identifier not in self.leptonFlav or self.leptonFlav[self.sample.identifier] == tree.Vtype:
                if tree.Vtype == 0:
                    good_muons_2lep = self.HighestPtGoodMuonsOppCharge(tree, min_pt=20.0, max_rel_iso=0.25, idcut=None, etacut=2.4, isOneLepton=False)
                    if len(good_muons_2lep) > 1:
                        self._b("isZmm")[0] = 1
                        self._b("vLidx")[0] = good_muons_2lep[0]
                        self._b("vLidx")[1] = good_muons_2lep[1]
                    elif debugEvent:
                        print "DEBUG-EVENT: 2 mu event, but less than 2 good muons -> discard"
                elif tree.Vtype == 1:
                    good_elecs_2lep = self.HighestPtGoodElectronsOppCharge(tree, min_pt=20.0, max_rel_iso=0.15, idcut=1, etacut=2.5, isOneLepton=False)
                    if len(good_elecs_2lep) > 1:
                        self._b("isZee")[0] = 1
                        self._b("vLidx")[0] = good_elecs_2lep[0]
                        self._b("vLidx")[1] = good_elecs_2lep[1]
                    elif debugEvent:
                        print "DEBUG-EVENT: 2 e event, but less than 2 good electrons -> discard"
                elif tree.Vtype == 2:
                    good_muons_1lep = self.HighestPtGoodMuonsOppCharge(tree, min_pt=25.0, max_rel_iso=0.06, idcut=None, etacut=2.4, isOneLepton=True)
                    if len(good_muons_1lep) > 0:
                        self._b("isWmunu")[0] = 1
                        self._b("vLidx")[0] = good_muons_1lep[0]
                        self._b("vLidx")[1] = -1 
                    elif debugEvent:
                        print "DEBUG-EVENT: 1 mu event, but no good muon found"
                elif tree.Vtype == 3:
                    good_elecs_1lep = self.HighestPtGoodElectronsOppCharge(tree, min_pt=30.0, max_rel_iso=0.06, idcut=1, etacut=2.5, isOneLepton=True)
                    if len(good_elecs_1lep) > 0:
                        self._b("isWenu")[0] = 1
                        self._b("vLidx")[0] = good_elecs_1lep[0]
                        self._b("vLidx")[1] = -1
                    elif debugEvent:
                        print "DEBUG-EVENT: 1 e event, but no good electron found"
                elif tree.Vtype == 4:
                        passMetFilters = all([getattr(tree, x) for x in self.metFilters]) 
                        if tree.MET_Pt > 170.0 and passMetFilters:
                            self._b("isZnn")[0] = 1
                        else:
                            if debugEvent:
                                print "DEBUG-EVENT: 0 lep event, but MET criteria not passed!"
                            return False
                else:
                    return False
            else:
                return False
            self.cutFlow[2] += 1
            
            if (self._b("isZmm")[0] or self._b("isZee")[0]) and not "Zll" in self.channels:
                return False
            elif (self._b("isWmunu")[0] or self._b("isWenu")[0]) and not ("Wln" in self.channels or "Znn" in self.channels):
                return False
            elif (self._b("isZnn")[0]) and not "Znn" in self.channels:
                return False
            self.cutFlow[3] += 1

            # JETS
            if self._b("isZnn")[0]:
                j1ptCut = 35.0
                j2ptCut = 35.0
                j1Btag = self.btagWP['loose']
            elif self._b("isWmunu")[0] or self._b("isWenu")[0]:
                j1ptCut = 25.0
                j2ptCut = 25.0
                j1Btag = self.btagWP['loose']
            elif self._b("isZmm")[0] or self._b("isZee")[0]:
                j1ptCut = 20.0
                j2ptCut = 20.0
                j1Btag = self.btagWP['none']
            else:
                return False
            j2Btag = self.btagWP['none'] 

            selectedJets = self.HighestTaggerValueBJets(tree, j1ptCut, j2ptCut, self.taggerName)

            if len(selectedJets) == 2:
                self._b("hJidx")[0] = selectedJets[0]
                self._b("hJidx")[1] = selectedJets[1]
                if getattr(tree, self.taggerName)[selectedJets[0]] < j1Btag:
                    if debugEvent:
                        print "DEBUG-EVENT: highest btag < ", j1Btag, " -> discard"
                    return False
                elif getattr(tree, self.taggerName)[selectedJets[1]] < j2Btag:
                    if debugEvent:
                        print "DEBUG-EVENT: second btag < ", j2Btag, " -> discard"
                    return False
                elif self._b("isZnn")[0]:
                    if max(tree.Jet_PtReg[selectedJets[0]], tree.Jet_PtReg[selectedJets[1]]) < 60.0:
                        if debugEvent:
                            print "DEBUG-EVENT: max bjet pt < 60 -> discard" 
                        return False
            else:
                return False
            self.cutFlow[4] += 1

            # VECTOR
            if self._b("isZee")[0] or self._b("isZmm")[0]:
                lep1 = ROOT.TLorentzVector()
                lep2 = ROOT.TLorentzVector()
                i1 = self._b("vLidx")[0]
                i2 = self._b("vLidx")[1]
                if self._b("isZee")[0]:
                    lep1.SetPtEtaPhiM(tree.Electron_pt[i1], tree.Electron_eta[i1], tree.Electron_phi[i1], tree.Electron_mass[i1])
                    lep2.SetPtEtaPhiM(tree.Electron_pt[i2], tree.Electron_eta[i2], tree.Electron_phi[i2], tree.Electron_mass[i2])
                elif self._b("isZmm")[0]:
                    lep1.SetPtEtaPhiM(tree.Muon_pt[i1], tree.Muon_eta[i1], tree.Muon_phi[i1], tree.Muon_mass[i1])
                    lep2.SetPtEtaPhiM(tree.Muon_pt[i2], tree.Muon_eta[i2], tree.Muon_phi[i2], tree.Muon_mass[i2])
                V = lep1 + lep2
            elif self._b("isWenu")[0] or self._b("isWmunu")[0]:
                i1 = self._b("vLidx")[0]
                if self._b("isWenu")[0]:
                    sel_lepton_pt   = tree.Electron_pt[i1]
                    sel_lepton_eta  = tree.Electron_eta[i1]
                    sel_lepton_phi  = tree.Electron_phi[i1]
                    sel_lepton_mass = tree.Electron_mass[i1]
                elif self._b("isWmunu")[0]:
                    sel_lepton_pt   = tree.Muon_pt[i1]
                    sel_lepton_eta  = tree.Muon_eta[i1]
                    sel_lepton_phi  = tree.Muon_phi[i1]
                    sel_lepton_mass = tree.Muon_mass[i1]
                self._b("lepMetDPhi")[0] = abs(ROOT.TVector2.Phi_mpi_pi(sel_lepton_phi - tree.MET_Phi))
                #if self._b("lepMetDPhi")[0] > 2.0:
                #    return False

                MET = ROOT.TLorentzVector()
                Lep = ROOT.TLorentzVector()
                MET.SetPtEtaPhiM(tree.MET_Pt, 0.0, tree.MET_Phi, 0.0)
                Lep.SetPtEtaPhiM(sel_lepton_pt, sel_lepton_eta, sel_lepton_phi, sel_lepton_mass)
                cosPhi12 = (Lep.Px()*MET.Px() + Lep.Py()*MET.Py()) / (Lep.Pt() * MET.Pt())
                self._b("V_mt")[0] = ROOT.TMath.Sqrt(2*Lep.Pt()*MET.Pt() * (1 - cosPhi12))

                V = MET + Lep
            elif self._b("isZnn")[0]:
                MET = ROOT.TLorentzVector()
                MET.SetPtEtaPhiM(tree.MET_Pt, 0.0, tree.MET_Phi, 0.0)
                V = MET
            self.cutFlow[5] += 1

            self._b("V_pt")[0] = V.Pt()
            self._b("V_eta")[0] = V.Eta()
            self._b("V_phi")[0] = V.Phi()
            self._b("V_mass")[0] = V.M()

            if (self._b("isZee")[0] or self._b("isZmm")[0]) and self._b("V_pt")[0] < 50.0:
                return False
            elif self._b("isZnn")[0] and self._b("V_pt")[0] < 150.0:
                return False
            elif (self._b("isWenu")[0] or self._b("isWmunu")[0]) and (self._b("V_pt")[0] < 150.0 and MET.Pt() < 170.0):
                return False

            self.cutFlow[6] += 1

            # yield in the end
            self.cutFlow[7] += 1
            if debugEvent:
                print "DEBUG-EVENT: event passed!!!" 

        return True

    def afterProcessing(self):
        print "cut-flow:"
        print "  beginning          ", self.cutFlow[0]
        print "  HLT                ", self.cutFlow[1]
        print "  Leptons            ", self.cutFlow[2]
        print "  Channel            ", self.cutFlow[3]
        print "  Jets               ", self.cutFlow[4]
        print "  Vector boson       ", self.cutFlow[5]
        print "  Vpt                ", self.cutFlow[6]
        print "  end                ", self.cutFlow[7]

        print "efficiency:", 1.0*self.cutFlow[7]/self.cutFlow[0]

