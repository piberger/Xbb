//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Jul 29 18:12:02 2018 by ROOT version 6.10/09
// from TTree Events/Events
// found on file: root://t3dcachedb03.psi.ch//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/VHbbPostNano2016/Wlv/sys_v2/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/tree_arizzi-RunIIMoriond17-DeepAndR148_180517_170415_0000_7_c65a9993f5ddd46b3c2a8e157ec02743f21cb1f963092c580b77243b.root
//////////////////////////////////////////////////////////

#ifndef myclass_h
#define myclass_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class myclass {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   UInt_t          run;
   UInt_t          luminosityBlock;
   ULong64_t       event;
   Float_t         btagWeight_CSVV2;
   Float_t         btagWeight_CMVA;
   Float_t         CaloMET_phi;
   Float_t         CaloMET_pt;
   Float_t         CaloMET_sumEt;
   UInt_t          nElectron;
   Float_t         Electron_deltaEtaSC[8];   //[nElectron]
   Float_t         Electron_dr03EcalRecHitSumEt[8];   //[nElectron]
   Float_t         Electron_dr03HcalDepth1TowerSumEt[8];   //[nElectron]
   Float_t         Electron_dr03TkSumPt[8];   //[nElectron]
   Float_t         Electron_dxy[8];   //[nElectron]
   Float_t         Electron_dxyErr[8];   //[nElectron]
   Float_t         Electron_dz[8];   //[nElectron]
   Float_t         Electron_dzErr[8];   //[nElectron]
   Float_t         Electron_eCorr[8];   //[nElectron]
   Float_t         Electron_eInvMinusPInv[8];   //[nElectron]
   Float_t         Electron_energyErr[8];   //[nElectron]
   Float_t         Electron_eta[8];   //[nElectron]
   Float_t         Electron_hoe[8];   //[nElectron]
   Float_t         Electron_ip3d[8];   //[nElectron]
   Float_t         Electron_mass[8];   //[nElectron]
   Float_t         Electron_miniPFRelIso_all[8];   //[nElectron]
   Float_t         Electron_miniPFRelIso_chg[8];   //[nElectron]
   Float_t         Electron_mvaSpring16GP[8];   //[nElectron]
   Float_t         Electron_mvaSpring16HZZ[8];   //[nElectron]
   Float_t         Electron_pfRelIso03_all[8];   //[nElectron]
   Float_t         Electron_pfRelIso03_chg[8];   //[nElectron]
   Float_t         Electron_phi[8];   //[nElectron]
   Float_t         Electron_pt[8];   //[nElectron]
   Float_t         Electron_r9[8];   //[nElectron]
   Float_t         Electron_sieie[8];   //[nElectron]
   Float_t         Electron_sip3d[8];   //[nElectron]
   Float_t         Electron_mvaTTH[8];   //[nElectron]
   Int_t           Electron_charge[8];   //[nElectron]
   Int_t           Electron_cutBased[8];   //[nElectron]
   Int_t           Electron_cutBased_HLTPreSel[8];   //[nElectron]
   Int_t           Electron_jetIdx[8];   //[nElectron]
   Int_t           Electron_pdgId[8];   //[nElectron]
   Int_t           Electron_photonIdx[8];   //[nElectron]
   Int_t           Electron_tightCharge[8];   //[nElectron]
   Int_t           Electron_vidNestedWPBitmap[8];   //[nElectron]
   Bool_t          Electron_convVeto[8];   //[nElectron]
   Bool_t          Electron_cutBased_HEEP[8];   //[nElectron]
   Bool_t          Electron_isPFcand[8];   //[nElectron]
   UChar_t         Electron_lostHits[8];   //[nElectron]
   Bool_t          Electron_mvaSpring16GP_WP80[8];   //[nElectron]
   Bool_t          Electron_mvaSpring16GP_WP90[8];   //[nElectron]
   Bool_t          Electron_mvaSpring16HZZ_WPL[8];   //[nElectron]
   UChar_t         Flag_BadChargedCandidateFilter;
   UChar_t         Flag_BadGlobalMuon;
   UChar_t         Flag_BadPFMuonFilter;
   UChar_t         Flag_CloneGlobalMuon;
   UInt_t          nGenJetAK8;
   Float_t         GenJetAK8_eta[4];   //[nGenJetAK8]
   Float_t         GenJetAK8_mass[4];   //[nGenJetAK8]
   Float_t         GenJetAK8_phi[4];   //[nGenJetAK8]
   Float_t         GenJetAK8_pt[4];   //[nGenJetAK8]
   UInt_t          nGenJet;
   Float_t         GenJet_eta[22];   //[nGenJet]
   Float_t         GenJet_mass[22];   //[nGenJet]
   Float_t         GenJet_phi[22];   //[nGenJet]
   Float_t         GenJet_pt[22];   //[nGenJet]
   UInt_t          nGenPart;
   Float_t         GenPart_eta[125];   //[nGenPart]
   Float_t         GenPart_mass[125];   //[nGenPart]
   Float_t         GenPart_phi[125];   //[nGenPart]
   Float_t         GenPart_pt[125];   //[nGenPart]
   Int_t           GenPart_genPartIdxMother[125];   //[nGenPart]
   Int_t           GenPart_pdgId[125];   //[nGenPart]
   Int_t           GenPart_status[125];   //[nGenPart]
   Int_t           GenPart_statusFlags[125];   //[nGenPart]
   Float_t         Generator_binvar;
   Float_t         Generator_scalePDF;
   Float_t         Generator_weight;
   Float_t         Generator_x1;
   Float_t         Generator_x2;
   Float_t         Generator_xpdf1;
   Float_t         Generator_xpdf2;
   Int_t           Generator_id1;
   Int_t           Generator_id2;
   Float_t         genWeight;
   Float_t         LHEWeight_originalXWGTUP;
   UInt_t          nLHEPdfWeight;
   Float_t         LHEPdfWeight[101];   //[nLHEPdfWeight]
   UInt_t          nLHEScaleWeight;
   Float_t         LHEScaleWeight[9];   //[nLHEScaleWeight]
   UInt_t          nJet;
   Float_t         Jet_area[37];   //[nJet]
   Float_t         Jet_btagCMVA[37];   //[nJet]
   Float_t         Jet_btagCSVV2[37];   //[nJet]
   Float_t         Jet_btagDeepB[37];   //[nJet]
   Float_t         Jet_btagDeepC[37];   //[nJet]
   Float_t         Jet_btagDeepFlavB[37];   //[nJet]
   Float_t         Jet_chEmEF[37];   //[nJet]
   Float_t         Jet_chHEF[37];   //[nJet]
   Float_t         Jet_eta[37];   //[nJet]
   Float_t         Jet_mass[37];   //[nJet]
   Float_t         Jet_neEmEF[37];   //[nJet]
   Float_t         Jet_neHEF[37];   //[nJet]
   Float_t         Jet_phi[37];   //[nJet]
   Float_t         Jet_pt[37];   //[nJet]
   Float_t         Jet_qgl[37];   //[nJet]
   Float_t         Jet_rawFactor[37];   //[nJet]
   Float_t         Jet_bReg[37];   //[nJet]
   Float_t         Jet_bRegOld[37];   //[nJet]
   Float_t         Jet_bRegRes[37];   //[nJet]
   Int_t           Jet_electronIdx1[37];   //[nJet]
   Int_t           Jet_electronIdx2[37];   //[nJet]
   Int_t           Jet_jetId[37];   //[nJet]
   Int_t           Jet_muonIdx1[37];   //[nJet]
   Int_t           Jet_muonIdx2[37];   //[nJet]
   Int_t           Jet_nConstituents[37];   //[nJet]
   Int_t           Jet_nElectrons[37];   //[nJet]
   Int_t           Jet_nMuons[37];   //[nJet]
   Int_t           Jet_puId[37];   //[nJet]
   Float_t         LHE_HT;
   Float_t         LHE_HTIncoming;
   Float_t         LHE_Vpt;
   UChar_t         LHE_Njets;
   UChar_t         LHE_Nb;
   UChar_t         LHE_Nc;
   UChar_t         LHE_Nuds;
   UChar_t         LHE_Nglu;
   UChar_t         LHE_NpNLO;
   UChar_t         LHE_NpLO;
   UInt_t          nLHEPart;
   Float_t         LHEPart_pt[6];   //[nLHEPart]
   Float_t         LHEPart_eta[6];   //[nLHEPart]
   Float_t         LHEPart_phi[6];   //[nLHEPart]
   Float_t         LHEPart_mass[6];   //[nLHEPart]
   Int_t           LHEPart_pdgId[6];   //[nLHEPart]
   Float_t         GenMET_phi;
   Float_t         GenMET_pt;
   Float_t         MET_MetUnclustEnUpDeltaX;
   Float_t         MET_MetUnclustEnUpDeltaY;
   Float_t         MET_covXX;
   Float_t         MET_covXY;
   Float_t         MET_covYY;
   Float_t         MET_phi;
   Float_t         MET_pt;
   Float_t         MET_significance;
   Float_t         MET_sumEt;
   UInt_t          nMuon;
   Float_t         Muon_dxy[6];   //[nMuon]
   Float_t         Muon_dxyErr[6];   //[nMuon]
   Float_t         Muon_dz[6];   //[nMuon]
   Float_t         Muon_dzErr[6];   //[nMuon]
   Float_t         Muon_eta[6];   //[nMuon]
   Float_t         Muon_ip3d[6];   //[nMuon]
   Float_t         Muon_mass[6];   //[nMuon]
   Float_t         Muon_miniPFRelIso_all[6];   //[nMuon]
   Float_t         Muon_miniPFRelIso_chg[6];   //[nMuon]
   Float_t         Muon_pfRelIso03_all[6];   //[nMuon]
   Float_t         Muon_pfRelIso03_chg[6];   //[nMuon]
   Float_t         Muon_pfRelIso04_all[6];   //[nMuon]
   Float_t         Muon_phi[6];   //[nMuon]
   Float_t         Muon_pt[6];   //[nMuon]
   Float_t         Muon_ptErr[6];   //[nMuon]
   Float_t         Muon_segmentComp[6];   //[nMuon]
   Float_t         Muon_sip3d[6];   //[nMuon]
   Float_t         Muon_mvaTTH[6];   //[nMuon]
   Int_t           Muon_charge[6];   //[nMuon]
   Int_t           Muon_jetIdx[6];   //[nMuon]
   Int_t           Muon_nStations[6];   //[nMuon]
   Int_t           Muon_nTrackerLayers[6];   //[nMuon]
   Int_t           Muon_pdgId[6];   //[nMuon]
   Int_t           Muon_tightCharge[6];   //[nMuon]
   UChar_t         Muon_highPtId[6];   //[nMuon]
   Bool_t          Muon_isPFcand[6];   //[nMuon]
   Bool_t          Muon_mediumId[6];   //[nMuon]
   Bool_t          Muon_softId[6];   //[nMuon]
   Bool_t          Muon_tightId[6];   //[nMuon]
   Float_t         Pileup_nTrueInt;
   Int_t           Pileup_nPU;
   Int_t           Pileup_sumEOOT;
   Int_t           Pileup_sumLOOT;
   Float_t         PuppiMET_phi;
   Float_t         PuppiMET_pt;
   Float_t         PuppiMET_sumEt;
   Float_t         RawMET_phi;
   Float_t         RawMET_pt;
   Float_t         RawMET_sumEt;
   Float_t         fixedGridRhoFastjetAll;
   Float_t         fixedGridRhoFastjetCentralCalo;
   Float_t         fixedGridRhoFastjetCentralNeutral;
   UInt_t          nGenDressedLepton;
   Float_t         GenDressedLepton_eta[3];   //[nGenDressedLepton]
   Float_t         GenDressedLepton_mass[3];   //[nGenDressedLepton]
   Float_t         GenDressedLepton_phi[3];   //[nGenDressedLepton]
   Float_t         GenDressedLepton_pt[3];   //[nGenDressedLepton]
   Int_t           GenDressedLepton_pdgId[3];   //[nGenDressedLepton]
   UInt_t          nSoftActivityJet;
   Float_t         SoftActivityJet_eta[6];   //[nSoftActivityJet]
   Float_t         SoftActivityJet_phi[6];   //[nSoftActivityJet]
   Float_t         SoftActivityJet_pt[6];   //[nSoftActivityJet]
   Float_t         SoftActivityJetHT;
   Float_t         SoftActivityJetHT10;
   Float_t         SoftActivityJetHT2;
   Float_t         SoftActivityJetHT5;
   Int_t           SoftActivityJetNjets10;
   Int_t           SoftActivityJetNjets2;
   Int_t           SoftActivityJetNjets5;
   Float_t         TkMET_phi;
   Float_t         TkMET_pt;
   Float_t         TkMET_sumEt;
   Int_t           genTtbarId;
   UInt_t          nOtherPV;
   Float_t         OtherPV_z[3];   //[nOtherPV]
   Float_t         PV_ndof;
   Float_t         PV_x;
   Float_t         PV_y;
   Float_t         PV_z;
   Float_t         PV_chi2;
   Float_t         PV_score;
   Int_t           PV_npvs;
   Int_t           PV_npvsGood;
   UInt_t          nSV;
   Float_t         SV_dlen[12];   //[nSV]
   Float_t         SV_dlenSig[12];   //[nSV]
   Float_t         SV_pAngle[12];   //[nSV]
   Int_t           Electron_genPartIdx[8];   //[nElectron]
   UChar_t         Electron_genPartFlav[8];   //[nElectron]
   Int_t           GenJetAK8_partonFlavour[4];   //[nGenJetAK8]
   UChar_t         GenJetAK8_hadronFlavour[4];   //[nGenJetAK8]
   Int_t           GenJet_partonFlavour[22];   //[nGenJet]
   UChar_t         GenJet_hadronFlavour[22];   //[nGenJet]
   Int_t           Jet_genJetIdx[37];   //[nJet]
   Int_t           Jet_hadronFlavour[37];   //[nJet]
   Int_t           Jet_partonFlavour[37];   //[nJet]
   Int_t           Muon_genPartIdx[6];   //[nMuon]
   UChar_t         Muon_genPartFlav[6];   //[nMuon]
   Float_t         MET_fiducialGenPhi;
   Float_t         MET_fiducialGenPt;
   UChar_t         Electron_cleanmask[8];   //[nElectron]
   UChar_t         Jet_cleanmask[37];   //[nJet]
   UChar_t         Muon_cleanmask[6];   //[nMuon]
   Float_t         SV_chi2[12];   //[nSV]
   Float_t         SV_eta[12];   //[nSV]
   Float_t         SV_mass[12];   //[nSV]
   Float_t         SV_ndof[12];   //[nSV]
   Float_t         SV_phi[12];   //[nSV]
   Float_t         SV_pt[12];   //[nSV]
   Float_t         SV_x[12];   //[nSV]
   Float_t         SV_y[12];   //[nSV]
   Float_t         SV_z[12];   //[nSV]
   Bool_t          L1simulation_step;
   Bool_t          HLTriggerFirstPath;
   Bool_t          HLT_Mu7p5_L2Mu2_Jpsi;
   Bool_t          HLT_Mu7p5_L2Mu2_Upsilon;
   Bool_t          HLT_Mu7p5_Track2_Jpsi;
   Bool_t          HLT_Mu7p5_Track3p5_Jpsi;
   Bool_t          HLT_Mu7p5_Track7_Jpsi;
   Bool_t          HLT_Mu7p5_Track2_Upsilon;
   Bool_t          HLT_Mu7p5_Track3p5_Upsilon;
   Bool_t          HLT_Mu7p5_Track7_Upsilon;
   Bool_t          HLT_Ele17_Ele8_Gsf;
   Bool_t          HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28;
   Bool_t          HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29;
   Bool_t          HLT_Ele22_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_Ele23_WPLoose_Gsf;
   Bool_t          HLT_Ele23_WPLoose_Gsf_WHbbBoost;
   Bool_t          HLT_Ele24_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20;
   Bool_t          HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30;
   Bool_t          HLT_Ele25_WPTight_Gsf;
   Bool_t          HLT_Ele25_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_Ele25_eta2p1_WPTight_Gsf;
   Bool_t          HLT_Ele27_WPLoose_Gsf;
   Bool_t          HLT_Ele27_WPLoose_Gsf_WHbbBoost;
   Bool_t          HLT_Ele27_WPTight_Gsf;
   Bool_t          HLT_Ele27_WPTight_Gsf_L1JetTauSeeded;
   Bool_t          HLT_Ele27_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_Ele27_eta2p1_WPTight_Gsf;
   Bool_t          HLT_Ele30_WPTight_Gsf;
   Bool_t          HLT_Ele30_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_Ele30_eta2p1_WPTight_Gsf;
   Bool_t          HLT_Ele32_WPTight_Gsf;
   Bool_t          HLT_Ele32_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_Ele32_eta2p1_WPTight_Gsf;
   Bool_t          HLT_Ele35_WPLoose_Gsf;
   Bool_t          HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50;
   Bool_t          HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_Ele45_WPLoose_Gsf;
   Bool_t          HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded;
   Bool_t          HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50;
   Bool_t          HLT_Ele105_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_Ele30WP60_SC4_Mass55;
   Bool_t          HLT_Ele30WP60_Ele8_Mass55;
   Bool_t          HLT_Mu16_eta2p1_MET30;
   Bool_t          HLT_IsoMu16_eta2p1_MET30;
   Bool_t          HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1;
   Bool_t          HLT_IsoMu17_eta2p1;
   Bool_t          HLT_IsoMu17_eta2p1_LooseIsoPFTau20;
   Bool_t          HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_IsoMu18;
   Bool_t          HLT_IsoMu19_eta2p1_LooseIsoPFTau20;
   Bool_t          HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg;
   Bool_t          HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20;
   Bool_t          HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg;
   Bool_t          HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg;
   Bool_t          HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg;
   Bool_t          HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg;
   Bool_t          HLT_IsoMu20;
   Bool_t          HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1;
   Bool_t          HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg;
   Bool_t          HLT_IsoMu22;
   Bool_t          HLT_IsoMu22_eta2p1;
   Bool_t          HLT_IsoMu24;
   Bool_t          HLT_IsoMu27;
   Bool_t          HLT_IsoTkMu18;
   Bool_t          HLT_IsoTkMu20;
   Bool_t          HLT_IsoTkMu22;
   Bool_t          HLT_IsoTkMu22_eta2p1;
   Bool_t          HLT_IsoTkMu24;
   Bool_t          HLT_IsoTkMu27;
   Bool_t          HLT_JetE30_NoBPTX3BX;
   Bool_t          HLT_JetE30_NoBPTX;
   Bool_t          HLT_JetE50_NoBPTX3BX;
   Bool_t          HLT_JetE70_NoBPTX3BX;
   Bool_t          HLT_L2Mu10;
   Bool_t          HLT_L2DoubleMu23_NoVertex;
   Bool_t          HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10;
   Bool_t          HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10;
   Bool_t          HLT_L2Mu10_NoVertex_NoBPTX3BX;
   Bool_t          HLT_L2Mu10_NoVertex_NoBPTX;
   Bool_t          HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX;
   Bool_t          HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX;
   Bool_t          HLT_LooseIsoPFTau50_Trk30_eta2p1;
   Bool_t          HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80;
   Bool_t          HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90;
   Bool_t          HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110;
   Bool_t          HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120;
   Bool_t          HLT_VLooseIsoPFTau120_Trk50_eta2p1;
   Bool_t          HLT_VLooseIsoPFTau140_Trk50_eta2p1;
   Bool_t          HLT_Mu17_Mu8;
   Bool_t          HLT_Mu17_Mu8_DZ;
   Bool_t          HLT_Mu17_Mu8_SameSign;
   Bool_t          HLT_Mu17_Mu8_SameSign_DZ;
   Bool_t          HLT_Mu20_Mu10;
   Bool_t          HLT_Mu20_Mu10_DZ;
   Bool_t          HLT_Mu20_Mu10_SameSign;
   Bool_t          HLT_Mu20_Mu10_SameSign_DZ;
   Bool_t          HLT_Mu17_TkMu8_DZ;
   Bool_t          HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL;
   Bool_t          HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ;
   Bool_t          HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL;
   Bool_t          HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ;
   Bool_t          HLT_Mu25_TkMu0_dEta18_Onia;
   Bool_t          HLT_Mu27_TkMu8;
   Bool_t          HLT_Mu30_TkMu11;
   Bool_t          HLT_Mu30_eta2p1_PFJet150_PFJet50;
   Bool_t          HLT_Mu40_TkMu11;
   Bool_t          HLT_Mu40_eta2p1_PFJet200_PFJet50;
   Bool_t          HLT_Mu20;
   Bool_t          HLT_TkMu17;
   Bool_t          HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL;
   Bool_t          HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ;
   Bool_t          HLT_TkMu20;
   Bool_t          HLT_Mu24_eta2p1;
   Bool_t          HLT_TkMu24_eta2p1;
   Bool_t          HLT_Mu27;
   Bool_t          HLT_TkMu27;
   Bool_t          HLT_Mu45_eta2p1;
   Bool_t          HLT_Mu50;
   Bool_t          HLT_TkMu50;
   Bool_t          HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL;
   Bool_t          HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL;
   Bool_t          HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL;
   Bool_t          HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL;
   Bool_t          HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL;
   Bool_t          HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight;
   Bool_t          HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose;
   Bool_t          HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose;
   Bool_t          HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight;
   Bool_t          HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose;
   Bool_t          HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose;
   Bool_t          HLT_Mu28NoFiltersNoVtx_CentralCaloJet40;
   Bool_t          HLT_SingleCentralPFJet170_CFMax0p1;
   Bool_t          HLT_MET60_IsoTrk35_Loose;
   Bool_t          HLT_MET75_IsoTrk50;
   Bool_t          HLT_MET90_IsoTrk50;
   Bool_t          HLT_Mu8_TrkIsoVVL;
   Bool_t          HLT_Mu17_TrkIsoVVL;
   Bool_t          HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded;
   Bool_t          HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_Mu8_DiEle12_CaloIdL_TrackIdL;
   Bool_t          HLT_Mu12_Photon25_CaloIdL;
   Bool_t          HLT_Mu12_Photon25_CaloIdL_L1ISO;
   Bool_t          HLT_Mu12_Photon25_CaloIdL_L1OR;
   Bool_t          HLT_Mu17_Photon22_CaloIdL_L1ISO;
   Bool_t          HLT_Mu17_Photon30_CaloIdL_L1ISO;
   Bool_t          HLT_Mu17_Photon35_CaloIdL_L1ISO;
   Bool_t          HLT_Mu3er_PFHT140_PFMET125;
   Bool_t          HLT_Mu6_PFHT200_PFMET80_BTagCSV_p067;
   Bool_t          HLT_Mu6_PFHT200_PFMET100;
   Bool_t          HLT_Mu14er_PFMET100;
   Bool_t          HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Ele17_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_Ele17_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Ele23_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Ele27_eta2p1_WPLoose_Gsf_HT200;
   Bool_t          HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250;
   Bool_t          HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300;
   Bool_t          HLT_Mu10_CentralPFJet30_BTagCSV_p13;
   Bool_t          HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13;
   Bool_t          HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT350_PFMET50;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT600;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT350;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT400_PFMET50;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT400;
   Bool_t          HLT_Ele50_IsoVVVL_PFHT400;
   Bool_t          HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60;
   Bool_t          HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60;
   Bool_t          HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT350_PFMET50;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT600;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT350;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT400_PFMET50;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT400;
   Bool_t          HLT_Mu50_IsoVVVL_PFHT400;
   Bool_t          HLT_Mu16_TkMu0_dEta18_Onia;
   Bool_t          HLT_Mu16_TkMu0_dEta18_Phi;
   Bool_t          HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx;
   Bool_t          HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx;
   Bool_t          HLT_Mu8;
   Bool_t          HLT_Mu17;
   Bool_t          HLT_Mu3_PFJet40;
   Bool_t          HLT_Ele8_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele12_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele17_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele23_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165;
   Bool_t          HLT_Ele115_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_Mu55;
   Bool_t          HLT_PixelTracks_Multiplicity60ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity85ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity110ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity135ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity160ForEndOfFill;
   Bool_t          HLT_ECALHT800;
   Bool_t          HLT_MET100;
   Bool_t          HLT_MET150;
   Bool_t          HLT_MET200;
   Bool_t          HLT_Ele27_HighEta_Ele20_Mass55;
   Bool_t          HLT_Random;
   Bool_t          HLT_EcalCalibration;
   Bool_t          HLT_HcalCalibration;
   Bool_t          HLT_GlobalRunHPDNoise;
   Bool_t          HLT_HcalNZS;
   Bool_t          HLT_HcalPhiSym;
   Bool_t          HLT_HcalIsolatedbunch;
   Bool_t          HLT_Mu300;
   Bool_t          HLT_Mu350;
   Bool_t          HLT_MET250;
   Bool_t          HLT_MET300;
   Bool_t          HLT_MET600;
   Bool_t          HLT_MET700;
   Bool_t          HLT_Ele250_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_Ele300_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_IsoTrackHE;
   Bool_t          HLT_IsoTrackHB;
   Bool_t          HLTriggerFinalPath;
   Bool_t          Flag_HBHENoiseFilter;
   Bool_t          Flag_HBHENoiseIsoFilter;
   Bool_t          Flag_CSCTightHaloFilter;
   Bool_t          Flag_CSCTightHaloTrkMuUnvetoFilter;
   Bool_t          Flag_CSCTightHalo2015Filter;
   Bool_t          Flag_globalTightHalo2016Filter;
   Bool_t          Flag_globalSuperTightHalo2016Filter;
   Bool_t          Flag_HcalStripHaloFilter;
   Bool_t          Flag_hcalLaserEventFilter;
   Bool_t          Flag_EcalDeadCellTriggerPrimitiveFilter;
   Bool_t          Flag_EcalDeadCellBoundaryEnergyFilter;
   Bool_t          Flag_goodVertices;
   Bool_t          Flag_eeBadScFilter;
   Bool_t          Flag_ecalLaserCorrFilter;
   Bool_t          Flag_trkPOGFilters;
   Bool_t          Flag_chargedHadronTrackResolutionFilter;
   Bool_t          Flag_muonBadTrackFilter;
   Bool_t          Flag_trkPOG_manystripclus53X;
   Bool_t          Flag_trkPOG_toomanystripclus53X;
   Bool_t          Flag_trkPOG_logErrorTooManyClusters;
   Bool_t          Flag_METFilters;
   Float_t         puWeight;
   Float_t         puWeightUp;
   Float_t         puWeightDown;
   Float_t         Jet_pt_nom[37];   //[nJet]
   Float_t         Jet_mass_nom[37];   //[nJet]
   Float_t         MET_pt_nom;
   Float_t         MET_phi_nom;
   Float_t         Jet_pt_jerUp[37];   //[nJet]
   Float_t         Jet_mass_jerUp[37];   //[nJet]
   Float_t         Jet_mass_jmrUp[37];   //[nJet]
   Float_t         Jet_mass_jmsUp[37];   //[nJet]
   Float_t         MET_pt_jerUp;
   Float_t         MET_phi_jerUp;
   Float_t         Jet_pt_jesAbsoluteStatUp[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteStatUp[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteStatUp;
   Float_t         MET_phi_jesAbsoluteStatUp;
   Float_t         Jet_pt_jesAbsoluteScaleUp[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteScaleUp[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteScaleUp;
   Float_t         MET_phi_jesAbsoluteScaleUp;
   Float_t         Jet_pt_jesAbsoluteFlavMapUp[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteFlavMapUp[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteFlavMapUp;
   Float_t         MET_phi_jesAbsoluteFlavMapUp;
   Float_t         Jet_pt_jesAbsoluteMPFBiasUp[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteMPFBiasUp[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteMPFBiasUp;
   Float_t         MET_phi_jesAbsoluteMPFBiasUp;
   Float_t         Jet_pt_jesFragmentationUp[37];   //[nJet]
   Float_t         Jet_mass_jesFragmentationUp[37];   //[nJet]
   Float_t         MET_pt_jesFragmentationUp;
   Float_t         MET_phi_jesFragmentationUp;
   Float_t         Jet_pt_jesSinglePionECALUp[37];   //[nJet]
   Float_t         Jet_mass_jesSinglePionECALUp[37];   //[nJet]
   Float_t         MET_pt_jesSinglePionECALUp;
   Float_t         MET_phi_jesSinglePionECALUp;
   Float_t         Jet_pt_jesSinglePionHCALUp[37];   //[nJet]
   Float_t         Jet_mass_jesSinglePionHCALUp[37];   //[nJet]
   Float_t         MET_pt_jesSinglePionHCALUp;
   Float_t         MET_phi_jesSinglePionHCALUp;
   Float_t         Jet_pt_jesFlavorQCDUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorQCDUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorQCDUp;
   Float_t         MET_phi_jesFlavorQCDUp;
   Float_t         Jet_pt_jesTimePtEtaUp[37];   //[nJet]
   Float_t         Jet_mass_jesTimePtEtaUp[37];   //[nJet]
   Float_t         MET_pt_jesTimePtEtaUp;
   Float_t         MET_phi_jesTimePtEtaUp;
   Float_t         Jet_pt_jesRelativeJEREC1Up[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC1Up[37];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC1Up;
   Float_t         MET_phi_jesRelativeJEREC1Up;
   Float_t         Jet_pt_jesRelativeJEREC2Up[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC2Up[37];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC2Up;
   Float_t         MET_phi_jesRelativeJEREC2Up;
   Float_t         Jet_pt_jesRelativeJERHFUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeJERHFUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativeJERHFUp;
   Float_t         MET_phi_jesRelativeJERHFUp;
   Float_t         Jet_pt_jesRelativePtBBUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtBBUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtBBUp;
   Float_t         MET_phi_jesRelativePtBBUp;
   Float_t         Jet_pt_jesRelativePtEC1Up[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC1Up[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC1Up;
   Float_t         MET_phi_jesRelativePtEC1Up;
   Float_t         Jet_pt_jesRelativePtEC2Up[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC2Up[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC2Up;
   Float_t         MET_phi_jesRelativePtEC2Up;
   Float_t         Jet_pt_jesRelativePtHFUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtHFUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtHFUp;
   Float_t         MET_phi_jesRelativePtHFUp;
   Float_t         Jet_pt_jesRelativeBalUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeBalUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativeBalUp;
   Float_t         MET_phi_jesRelativeBalUp;
   Float_t         Jet_pt_jesRelativeFSRUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeFSRUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativeFSRUp;
   Float_t         MET_phi_jesRelativeFSRUp;
   Float_t         Jet_pt_jesRelativeStatFSRUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatFSRUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativeStatFSRUp;
   Float_t         MET_phi_jesRelativeStatFSRUp;
   Float_t         Jet_pt_jesRelativeStatECUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatECUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativeStatECUp;
   Float_t         MET_phi_jesRelativeStatECUp;
   Float_t         Jet_pt_jesRelativeStatHFUp[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatHFUp[37];   //[nJet]
   Float_t         MET_pt_jesRelativeStatHFUp;
   Float_t         MET_phi_jesRelativeStatHFUp;
   Float_t         Jet_pt_jesPileUpDataMCUp[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpDataMCUp[37];   //[nJet]
   Float_t         MET_pt_jesPileUpDataMCUp;
   Float_t         MET_phi_jesPileUpDataMCUp;
   Float_t         Jet_pt_jesPileUpPtRefUp[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtRefUp[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtRefUp;
   Float_t         MET_phi_jesPileUpPtRefUp;
   Float_t         Jet_pt_jesPileUpPtBBUp[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtBBUp[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtBBUp;
   Float_t         MET_phi_jesPileUpPtBBUp;
   Float_t         Jet_pt_jesPileUpPtEC1Up[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC1Up[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC1Up;
   Float_t         MET_phi_jesPileUpPtEC1Up;
   Float_t         Jet_pt_jesPileUpPtEC2Up[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC2Up[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC2Up;
   Float_t         MET_phi_jesPileUpPtEC2Up;
   Float_t         Jet_pt_jesPileUpPtHFUp[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtHFUp[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtHFUp;
   Float_t         MET_phi_jesPileUpPtHFUp;
   Float_t         Jet_pt_jesPileUpMuZeroUp[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpMuZeroUp[37];   //[nJet]
   Float_t         MET_pt_jesPileUpMuZeroUp;
   Float_t         MET_phi_jesPileUpMuZeroUp;
   Float_t         Jet_pt_jesPileUpEnvelopeUp[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpEnvelopeUp[37];   //[nJet]
   Float_t         MET_pt_jesPileUpEnvelopeUp;
   Float_t         MET_phi_jesPileUpEnvelopeUp;
   Float_t         Jet_pt_jesSubTotalPileUpUp[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPileUpUp[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalPileUpUp;
   Float_t         MET_phi_jesSubTotalPileUpUp;
   Float_t         Jet_pt_jesSubTotalRelativeUp[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalRelativeUp[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalRelativeUp;
   Float_t         MET_phi_jesSubTotalRelativeUp;
   Float_t         Jet_pt_jesSubTotalPtUp[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPtUp[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalPtUp;
   Float_t         MET_phi_jesSubTotalPtUp;
   Float_t         Jet_pt_jesSubTotalScaleUp[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalScaleUp[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalScaleUp;
   Float_t         MET_phi_jesSubTotalScaleUp;
   Float_t         Jet_pt_jesSubTotalAbsoluteUp[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalAbsoluteUp[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalAbsoluteUp;
   Float_t         MET_phi_jesSubTotalAbsoluteUp;
   Float_t         Jet_pt_jesSubTotalMCUp[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalMCUp[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalMCUp;
   Float_t         MET_phi_jesSubTotalMCUp;
   Float_t         Jet_pt_jesTotalUp[37];   //[nJet]
   Float_t         Jet_mass_jesTotalUp[37];   //[nJet]
   Float_t         MET_pt_jesTotalUp;
   Float_t         MET_phi_jesTotalUp;
   Float_t         Jet_pt_jesTotalNoFlavorUp[37];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorUp[37];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorUp;
   Float_t         MET_phi_jesTotalNoFlavorUp;
   Float_t         Jet_pt_jesTotalNoTimeUp[37];   //[nJet]
   Float_t         Jet_mass_jesTotalNoTimeUp[37];   //[nJet]
   Float_t         MET_pt_jesTotalNoTimeUp;
   Float_t         MET_phi_jesTotalNoTimeUp;
   Float_t         Jet_pt_jesTotalNoFlavorNoTimeUp[37];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorNoTimeUp[37];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorNoTimeUp;
   Float_t         MET_phi_jesTotalNoFlavorNoTimeUp;
   Float_t         Jet_pt_jesFlavorZJetUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorZJetUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorZJetUp;
   Float_t         MET_phi_jesFlavorZJetUp;
   Float_t         Jet_pt_jesFlavorPhotonJetUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPhotonJetUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPhotonJetUp;
   Float_t         MET_phi_jesFlavorPhotonJetUp;
   Float_t         Jet_pt_jesFlavorPureGluonUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureGluonUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureGluonUp;
   Float_t         MET_phi_jesFlavorPureGluonUp;
   Float_t         Jet_pt_jesFlavorPureQuarkUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureQuarkUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureQuarkUp;
   Float_t         MET_phi_jesFlavorPureQuarkUp;
   Float_t         Jet_pt_jesFlavorPureCharmUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureCharmUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureCharmUp;
   Float_t         MET_phi_jesFlavorPureCharmUp;
   Float_t         Jet_pt_jesFlavorPureBottomUp[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureBottomUp[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureBottomUp;
   Float_t         MET_phi_jesFlavorPureBottomUp;
   Float_t         Jet_pt_jesTimeRunBCDUp[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunBCDUp[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunBCDUp;
   Float_t         MET_phi_jesTimeRunBCDUp;
   Float_t         Jet_pt_jesTimeRunEFUp[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunEFUp[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunEFUp;
   Float_t         MET_phi_jesTimeRunEFUp;
   Float_t         Jet_pt_jesTimeRunGUp[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunGUp[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunGUp;
   Float_t         MET_phi_jesTimeRunGUp;
   Float_t         Jet_pt_jesTimeRunHUp[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunHUp[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunHUp;
   Float_t         MET_phi_jesTimeRunHUp;
   Float_t         Jet_pt_jesCorrelationGroupMPFInSituUp[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupMPFInSituUp[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupMPFInSituUp;
   Float_t         MET_phi_jesCorrelationGroupMPFInSituUp;
   Float_t         Jet_pt_jesCorrelationGroupIntercalibrationUp[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupIntercalibrationUp[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupIntercalibrationUp;
   Float_t         MET_phi_jesCorrelationGroupIntercalibrationUp;
   Float_t         Jet_pt_jesCorrelationGroupbJESUp[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupbJESUp[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupbJESUp;
   Float_t         MET_phi_jesCorrelationGroupbJESUp;
   Float_t         Jet_pt_jesCorrelationGroupFlavorUp[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupFlavorUp[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupFlavorUp;
   Float_t         MET_phi_jesCorrelationGroupFlavorUp;
   Float_t         Jet_pt_jesCorrelationGroupUncorrelatedUp[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupUncorrelatedUp[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupUncorrelatedUp;
   Float_t         MET_phi_jesCorrelationGroupUncorrelatedUp;
   Float_t         MET_pt_unclustEnUp;
   Float_t         MET_phi_unclustEnUp;
   Float_t         Jet_pt_jerDown[37];   //[nJet]
   Float_t         Jet_mass_jerDown[37];   //[nJet]
   Float_t         Jet_mass_jmrDown[37];   //[nJet]
   Float_t         Jet_mass_jmsDown[37];   //[nJet]
   Float_t         MET_pt_jerDown;
   Float_t         MET_phi_jerDown;
   Float_t         Jet_pt_jesAbsoluteStatDown[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteStatDown[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteStatDown;
   Float_t         MET_phi_jesAbsoluteStatDown;
   Float_t         Jet_pt_jesAbsoluteScaleDown[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteScaleDown[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteScaleDown;
   Float_t         MET_phi_jesAbsoluteScaleDown;
   Float_t         Jet_pt_jesAbsoluteFlavMapDown[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteFlavMapDown[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteFlavMapDown;
   Float_t         MET_phi_jesAbsoluteFlavMapDown;
   Float_t         Jet_pt_jesAbsoluteMPFBiasDown[37];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteMPFBiasDown[37];   //[nJet]
   Float_t         MET_pt_jesAbsoluteMPFBiasDown;
   Float_t         MET_phi_jesAbsoluteMPFBiasDown;
   Float_t         Jet_pt_jesFragmentationDown[37];   //[nJet]
   Float_t         Jet_mass_jesFragmentationDown[37];   //[nJet]
   Float_t         MET_pt_jesFragmentationDown;
   Float_t         MET_phi_jesFragmentationDown;
   Float_t         Jet_pt_jesSinglePionECALDown[37];   //[nJet]
   Float_t         Jet_mass_jesSinglePionECALDown[37];   //[nJet]
   Float_t         MET_pt_jesSinglePionECALDown;
   Float_t         MET_phi_jesSinglePionECALDown;
   Float_t         Jet_pt_jesSinglePionHCALDown[37];   //[nJet]
   Float_t         Jet_mass_jesSinglePionHCALDown[37];   //[nJet]
   Float_t         MET_pt_jesSinglePionHCALDown;
   Float_t         MET_phi_jesSinglePionHCALDown;
   Float_t         Jet_pt_jesFlavorQCDDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorQCDDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorQCDDown;
   Float_t         MET_phi_jesFlavorQCDDown;
   Float_t         Jet_pt_jesTimePtEtaDown[37];   //[nJet]
   Float_t         Jet_mass_jesTimePtEtaDown[37];   //[nJet]
   Float_t         MET_pt_jesTimePtEtaDown;
   Float_t         MET_phi_jesTimePtEtaDown;
   Float_t         Jet_pt_jesRelativeJEREC1Down[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC1Down[37];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC1Down;
   Float_t         MET_phi_jesRelativeJEREC1Down;
   Float_t         Jet_pt_jesRelativeJEREC2Down[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC2Down[37];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC2Down;
   Float_t         MET_phi_jesRelativeJEREC2Down;
   Float_t         Jet_pt_jesRelativeJERHFDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeJERHFDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativeJERHFDown;
   Float_t         MET_phi_jesRelativeJERHFDown;
   Float_t         Jet_pt_jesRelativePtBBDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtBBDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtBBDown;
   Float_t         MET_phi_jesRelativePtBBDown;
   Float_t         Jet_pt_jesRelativePtEC1Down[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC1Down[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC1Down;
   Float_t         MET_phi_jesRelativePtEC1Down;
   Float_t         Jet_pt_jesRelativePtEC2Down[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC2Down[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC2Down;
   Float_t         MET_phi_jesRelativePtEC2Down;
   Float_t         Jet_pt_jesRelativePtHFDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativePtHFDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativePtHFDown;
   Float_t         MET_phi_jesRelativePtHFDown;
   Float_t         Jet_pt_jesRelativeBalDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeBalDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativeBalDown;
   Float_t         MET_phi_jesRelativeBalDown;
   Float_t         Jet_pt_jesRelativeFSRDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeFSRDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativeFSRDown;
   Float_t         MET_phi_jesRelativeFSRDown;
   Float_t         Jet_pt_jesRelativeStatFSRDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatFSRDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativeStatFSRDown;
   Float_t         MET_phi_jesRelativeStatFSRDown;
   Float_t         Jet_pt_jesRelativeStatECDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatECDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativeStatECDown;
   Float_t         MET_phi_jesRelativeStatECDown;
   Float_t         Jet_pt_jesRelativeStatHFDown[37];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatHFDown[37];   //[nJet]
   Float_t         MET_pt_jesRelativeStatHFDown;
   Float_t         MET_phi_jesRelativeStatHFDown;
   Float_t         Jet_pt_jesPileUpDataMCDown[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpDataMCDown[37];   //[nJet]
   Float_t         MET_pt_jesPileUpDataMCDown;
   Float_t         MET_phi_jesPileUpDataMCDown;
   Float_t         Jet_pt_jesPileUpPtRefDown[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtRefDown[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtRefDown;
   Float_t         MET_phi_jesPileUpPtRefDown;
   Float_t         Jet_pt_jesPileUpPtBBDown[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtBBDown[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtBBDown;
   Float_t         MET_phi_jesPileUpPtBBDown;
   Float_t         Jet_pt_jesPileUpPtEC1Down[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC1Down[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC1Down;
   Float_t         MET_phi_jesPileUpPtEC1Down;
   Float_t         Jet_pt_jesPileUpPtEC2Down[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC2Down[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC2Down;
   Float_t         MET_phi_jesPileUpPtEC2Down;
   Float_t         Jet_pt_jesPileUpPtHFDown[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtHFDown[37];   //[nJet]
   Float_t         MET_pt_jesPileUpPtHFDown;
   Float_t         MET_phi_jesPileUpPtHFDown;
   Float_t         Jet_pt_jesPileUpMuZeroDown[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpMuZeroDown[37];   //[nJet]
   Float_t         MET_pt_jesPileUpMuZeroDown;
   Float_t         MET_phi_jesPileUpMuZeroDown;
   Float_t         Jet_pt_jesPileUpEnvelopeDown[37];   //[nJet]
   Float_t         Jet_mass_jesPileUpEnvelopeDown[37];   //[nJet]
   Float_t         MET_pt_jesPileUpEnvelopeDown;
   Float_t         MET_phi_jesPileUpEnvelopeDown;
   Float_t         Jet_pt_jesSubTotalPileUpDown[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPileUpDown[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalPileUpDown;
   Float_t         MET_phi_jesSubTotalPileUpDown;
   Float_t         Jet_pt_jesSubTotalRelativeDown[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalRelativeDown[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalRelativeDown;
   Float_t         MET_phi_jesSubTotalRelativeDown;
   Float_t         Jet_pt_jesSubTotalPtDown[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPtDown[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalPtDown;
   Float_t         MET_phi_jesSubTotalPtDown;
   Float_t         Jet_pt_jesSubTotalScaleDown[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalScaleDown[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalScaleDown;
   Float_t         MET_phi_jesSubTotalScaleDown;
   Float_t         Jet_pt_jesSubTotalAbsoluteDown[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalAbsoluteDown[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalAbsoluteDown;
   Float_t         MET_phi_jesSubTotalAbsoluteDown;
   Float_t         Jet_pt_jesSubTotalMCDown[37];   //[nJet]
   Float_t         Jet_mass_jesSubTotalMCDown[37];   //[nJet]
   Float_t         MET_pt_jesSubTotalMCDown;
   Float_t         MET_phi_jesSubTotalMCDown;
   Float_t         Jet_pt_jesTotalDown[37];   //[nJet]
   Float_t         Jet_mass_jesTotalDown[37];   //[nJet]
   Float_t         MET_pt_jesTotalDown;
   Float_t         MET_phi_jesTotalDown;
   Float_t         Jet_pt_jesTotalNoFlavorDown[37];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorDown[37];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorDown;
   Float_t         MET_phi_jesTotalNoFlavorDown;
   Float_t         Jet_pt_jesTotalNoTimeDown[37];   //[nJet]
   Float_t         Jet_mass_jesTotalNoTimeDown[37];   //[nJet]
   Float_t         MET_pt_jesTotalNoTimeDown;
   Float_t         MET_phi_jesTotalNoTimeDown;
   Float_t         Jet_pt_jesTotalNoFlavorNoTimeDown[37];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorNoTimeDown[37];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorNoTimeDown;
   Float_t         MET_phi_jesTotalNoFlavorNoTimeDown;
   Float_t         Jet_pt_jesFlavorZJetDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorZJetDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorZJetDown;
   Float_t         MET_phi_jesFlavorZJetDown;
   Float_t         Jet_pt_jesFlavorPhotonJetDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPhotonJetDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPhotonJetDown;
   Float_t         MET_phi_jesFlavorPhotonJetDown;
   Float_t         Jet_pt_jesFlavorPureGluonDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureGluonDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureGluonDown;
   Float_t         MET_phi_jesFlavorPureGluonDown;
   Float_t         Jet_pt_jesFlavorPureQuarkDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureQuarkDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureQuarkDown;
   Float_t         MET_phi_jesFlavorPureQuarkDown;
   Float_t         Jet_pt_jesFlavorPureCharmDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureCharmDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureCharmDown;
   Float_t         MET_phi_jesFlavorPureCharmDown;
   Float_t         Jet_pt_jesFlavorPureBottomDown[37];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureBottomDown[37];   //[nJet]
   Float_t         MET_pt_jesFlavorPureBottomDown;
   Float_t         MET_phi_jesFlavorPureBottomDown;
   Float_t         Jet_pt_jesTimeRunBCDDown[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunBCDDown[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunBCDDown;
   Float_t         MET_phi_jesTimeRunBCDDown;
   Float_t         Jet_pt_jesTimeRunEFDown[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunEFDown[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunEFDown;
   Float_t         MET_phi_jesTimeRunEFDown;
   Float_t         Jet_pt_jesTimeRunGDown[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunGDown[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunGDown;
   Float_t         MET_phi_jesTimeRunGDown;
   Float_t         Jet_pt_jesTimeRunHDown[37];   //[nJet]
   Float_t         Jet_mass_jesTimeRunHDown[37];   //[nJet]
   Float_t         MET_pt_jesTimeRunHDown;
   Float_t         MET_phi_jesTimeRunHDown;
   Float_t         Jet_pt_jesCorrelationGroupMPFInSituDown[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupMPFInSituDown[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupMPFInSituDown;
   Float_t         MET_phi_jesCorrelationGroupMPFInSituDown;
   Float_t         Jet_pt_jesCorrelationGroupIntercalibrationDown[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupIntercalibrationDown[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupIntercalibrationDown;
   Float_t         MET_phi_jesCorrelationGroupIntercalibrationDown;
   Float_t         Jet_pt_jesCorrelationGroupbJESDown[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupbJESDown[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupbJESDown;
   Float_t         MET_phi_jesCorrelationGroupbJESDown;
   Float_t         Jet_pt_jesCorrelationGroupFlavorDown[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupFlavorDown[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupFlavorDown;
   Float_t         MET_phi_jesCorrelationGroupFlavorDown;
   Float_t         Jet_pt_jesCorrelationGroupUncorrelatedDown[37];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupUncorrelatedDown[37];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupUncorrelatedDown;
   Float_t         MET_phi_jesCorrelationGroupUncorrelatedDown;
   Float_t         MET_pt_unclustEnDown;
   Float_t         MET_phi_unclustEnDown;
   Float_t         Muon_pt_corrected[6];   //[nMuon]
   Float_t         MHT_pt;
   Float_t         MHT_phi;
   UChar_t         Jet_mhtCleaning[37];   //[nJet]
   Float_t         Jet_btagSF[37];   //[nJet]
   Float_t         Jet_btagSF_up[37];   //[nJet]
   Float_t         Jet_btagSF_down[37];   //[nJet]
   Float_t         Jet_btagSF_shape[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_jes[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_jes[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_lf[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_lf[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_hf[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_hf[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_hfstats1[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_hfstats1[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_hfstats2[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_hfstats2[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_lfstats1[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_lfstats1[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_lfstats2[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_lfstats2[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_cferr1[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_cferr1[37];   //[nJet]
   Float_t         Jet_btagSF_shape_up_cferr2[37];   //[nJet]
   Float_t         Jet_btagSF_shape_down_cferr2[37];   //[nJet]
   Int_t           Vtype;
   Float_t         V_pt;
   Float_t         V_eta;
   Float_t         V_phi;
   Float_t         V_mass;
   Bool_t          Jet_lepFilter[37];   //[nJet]
   Int_t           vLidx[2];
   Int_t           hJidx[2];
   Int_t           hJidxCMVA[2];
   Float_t         HCMVA_pt;
   Float_t         HCMVA_eta;
   Float_t         HCMVA_phi;
   Float_t         HCMVA_mass;
   Float_t         HFSR_pt;
   Float_t         HFSR_eta;
   Float_t         HFSR_phi;
   Float_t         HFSR_mass;
   Float_t         SA_Ht;
   Float_t         SA5;
   Float_t         Jet_Pt[37];   //[nJet]
   Float_t         Jet_PtReg[37];   //[nJet]
   Float_t         MET_Pt;
   Float_t         MET_Phi;
   Int_t           Pt_fjidx;
   Int_t           Msd_fjidx;
   Int_t           Hbb_fjidx;
   Float_t         SAptfj_HT;
   Float_t         SAptfj5;
   Float_t         SAmfj_HT;
   Float_t         SAmfj5;
   Float_t         SAhbbfj_HT;
   Float_t         SAhbbfj5;
   Int_t           nVMuonIdx;
   Int_t           nVElectronIdx;
   Int_t           VMuonIdx[1];   //[nVMuonIdx]
   Int_t           VElectronIdx[1];   //[nVElectronIdx]
   Int_t           nVetoLeptons;
   Int_t           nAddLeptons;
   Float_t         TTW;
   Float_t         weight_SF_TightID[3];
   Float_t         weight_SF_TightISO[3];
   Float_t         weight_SF_TightIDnISO[3];
   Float_t         weight_SF_TRK[3];
   Float_t         weight_SF_Lepton[3];
   Float_t         eTrigSFWeight_singleEle80[3];
   Float_t         muTrigSFWeight_singlemu[3];
   Float_t         NLOw;
   Float_t         DYw;
   Float_t         EWKw[3];
   Float_t         EWKwSIG[3];
   Float_t         EWKwVJets[3];
   Float_t         bTagWeightCMVAV2;
   Float_t         bTagWeightCMVAV2_JESUp;
   Float_t         bTagWeightCMVAV2_JESDown;
   Float_t         bTagWeightCMVAV2_LFUp;
   Float_t         bTagWeightCMVAV2_LFDown;
   Float_t         bTagWeightCMVAV2_HFUp;
   Float_t         bTagWeightCMVAV2_HFDown;
   Float_t         bTagWeightCMVAV2_LFStats1Up;
   Float_t         bTagWeightCMVAV2_LFStats1Down;
   Float_t         bTagWeightCMVAV2_LFStats2Up;
   Float_t         bTagWeightCMVAV2_LFStats2Down;
   Float_t         bTagWeightCMVAV2_HFStats1Up;
   Float_t         bTagWeightCMVAV2_HFStats1Down;
   Float_t         bTagWeightCMVAV2_HFStats2Up;
   Float_t         bTagWeightCMVAV2_HFStats2Down;
   Float_t         bTagWeightCMVAV2_cErr1Up;
   Float_t         bTagWeightCMVAV2_cErr1Down;
   Float_t         bTagWeightCMVAV2_cErr2Up;
   Float_t         bTagWeightCMVAV2_cErr2Down;
   Float_t         bTagWeightCMVAV2_JES_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_JES_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_JES_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_JES_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_JES_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_JES_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_JES_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_JES_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_JES_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_JES_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_JES_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_JES_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_JES_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_JES_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_JES_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_JES_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_JES_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_JES_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_JES_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_JES_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_JES_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_JES_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_JES_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_JES_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_JES_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_JES_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_JES_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_JES_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_JES_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_JES_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_LF_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_LF_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_LF_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_LF_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_LF_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_LF_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_LF_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_LF_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_LF_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_LF_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_LF_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_LF_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_LF_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_LF_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_LF_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_LF_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_LF_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_LF_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_LF_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_LF_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_LF_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_LF_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_LF_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_LF_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_LF_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_LF_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_LF_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_LF_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_LF_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_LF_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_HF_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_HF_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_HF_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_HF_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_HF_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_HF_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_HF_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_HF_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_HF_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_HF_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_HF_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_HF_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_HF_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_HF_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_HF_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_HF_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_HF_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_HF_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_HF_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_HF_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_HF_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_HF_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_HF_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_HF_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_HF_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_HF_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_HF_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_HF_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_HF_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_HF_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats1_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats1_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_LFStats2_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_LFStats2_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats1_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats1_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_HFStats2_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_HFStats2_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr1_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr1_pt4_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt0_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt0_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt0_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt1_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt1_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt1_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt2_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt2_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt2_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt3_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt3_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt3_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt4_eta1Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt4_eta2Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt4_eta3Up;
   Float_t         bTagWeightCMVAV2_cErr2_pt0_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt0_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt0_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt1_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt1_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt1_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt2_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt2_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt2_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt3_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt3_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt3_eta3Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt4_eta1Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt4_eta2Down;
   Float_t         bTagWeightCMVAV2_cErr2_pt4_eta3Down;
   Float_t         minDphiJetMet;
   Int_t           nAddJetQCD;
   Float_t         hJets_pt_reg_max;
   Int_t           nAddJet30;
   Float_t         hJets_pt_reg_min;
   Float_t         dPhiMetTkMet;
   Float_t         dPhiVH;
   Float_t         hJets_pt_reg_1;
   Float_t         hJets_pt_reg_0;
   Float_t         H_pt;
   Float_t         H_pt_jer_Up;
   Float_t         H_pt_jer_Down;
   Float_t         H_pt_jesAbsoluteStat_Up;
   Float_t         H_pt_jesAbsoluteStat_Down;
   Float_t         H_pt_jesAbsoluteScale_Up;
   Float_t         H_pt_jesAbsoluteScale_Down;
   Float_t         H_pt_jesAbsoluteFlavMap_Up;
   Float_t         H_pt_jesAbsoluteFlavMap_Down;
   Float_t         H_pt_jesAbsoluteMPFBias_Up;
   Float_t         H_pt_jesAbsoluteMPFBias_Down;
   Float_t         H_pt_jesFragmentation_Up;
   Float_t         H_pt_jesFragmentation_Down;
   Float_t         H_pt_jesSinglePionECAL_Up;
   Float_t         H_pt_jesSinglePionECAL_Down;
   Float_t         H_pt_jesSinglePionHCAL_Up;
   Float_t         H_pt_jesSinglePionHCAL_Down;
   Float_t         H_pt_jesFlavorQCD_Up;
   Float_t         H_pt_jesFlavorQCD_Down;
   Float_t         H_pt_jesRelativeJEREC1_Up;
   Float_t         H_pt_jesRelativeJEREC1_Down;
   Float_t         H_pt_jesRelativeJEREC2_Up;
   Float_t         H_pt_jesRelativeJEREC2_Down;
   Float_t         H_pt_jesRelativeJERHF_Up;
   Float_t         H_pt_jesRelativeJERHF_Down;
   Float_t         H_pt_jesRelativePtBB_Up;
   Float_t         H_pt_jesRelativePtBB_Down;
   Float_t         H_pt_jesRelativePtEC1_Up;
   Float_t         H_pt_jesRelativePtEC1_Down;
   Float_t         H_pt_jesRelativePtEC2_Up;
   Float_t         H_pt_jesRelativePtEC2_Down;
   Float_t         H_pt_jesRelativePtHF_Up;
   Float_t         H_pt_jesRelativePtHF_Down;
   Float_t         H_pt_jesRelativeBal_Up;
   Float_t         H_pt_jesRelativeBal_Down;
   Float_t         H_pt_jesRelativeFSR_Up;
   Float_t         H_pt_jesRelativeFSR_Down;
   Float_t         H_pt_jesRelativeStatFSR_Up;
   Float_t         H_pt_jesRelativeStatFSR_Down;
   Float_t         H_pt_jesRelativeStatEC_Up;
   Float_t         H_pt_jesRelativeStatEC_Down;
   Float_t         H_pt_jesRelativeStatHF_Up;
   Float_t         H_pt_jesRelativeStatHF_Down;
   Float_t         H_pt_jesPileUpDataMC_Up;
   Float_t         H_pt_jesPileUpDataMC_Down;
   Float_t         H_pt_jesPileUpPtRef_Up;
   Float_t         H_pt_jesPileUpPtRef_Down;
   Float_t         H_pt_jesPileUpPtBB_Up;
   Float_t         H_pt_jesPileUpPtBB_Down;
   Float_t         H_pt_jesPileUpPtEC1_Up;
   Float_t         H_pt_jesPileUpPtEC1_Down;
   Float_t         H_pt_jesPileUpPtEC2_Up;
   Float_t         H_pt_jesPileUpPtEC2_Down;
   Float_t         H_pt_jesPileUpPtHF_Up;
   Float_t         H_pt_jesPileUpPtHF_Down;
   Float_t         H_pt_jesPileUpMuZero_Up;
   Float_t         H_pt_jesPileUpMuZero_Down;
   Float_t         H_pt_jesPileUpEnvelope_Up;
   Float_t         H_pt_jesPileUpEnvelope_Down;
   Float_t         H_pt_jesTotal_Up;
   Float_t         H_pt_jesTotal_Down;
   Float_t         H_pt_minmax_Up;
   Float_t         H_pt_minmax_Down;
   Float_t         H_eta;
   Float_t         H_eta_jer_Up;
   Float_t         H_eta_jer_Down;
   Float_t         H_eta_jesAbsoluteStat_Up;
   Float_t         H_eta_jesAbsoluteStat_Down;
   Float_t         H_eta_jesAbsoluteScale_Up;
   Float_t         H_eta_jesAbsoluteScale_Down;
   Float_t         H_eta_jesAbsoluteFlavMap_Up;
   Float_t         H_eta_jesAbsoluteFlavMap_Down;
   Float_t         H_eta_jesAbsoluteMPFBias_Up;
   Float_t         H_eta_jesAbsoluteMPFBias_Down;
   Float_t         H_eta_jesFragmentation_Up;
   Float_t         H_eta_jesFragmentation_Down;
   Float_t         H_eta_jesSinglePionECAL_Up;
   Float_t         H_eta_jesSinglePionECAL_Down;
   Float_t         H_eta_jesSinglePionHCAL_Up;
   Float_t         H_eta_jesSinglePionHCAL_Down;
   Float_t         H_eta_jesFlavorQCD_Up;
   Float_t         H_eta_jesFlavorQCD_Down;
   Float_t         H_eta_jesRelativeJEREC1_Up;
   Float_t         H_eta_jesRelativeJEREC1_Down;
   Float_t         H_eta_jesRelativeJEREC2_Up;
   Float_t         H_eta_jesRelativeJEREC2_Down;
   Float_t         H_eta_jesRelativeJERHF_Up;
   Float_t         H_eta_jesRelativeJERHF_Down;
   Float_t         H_eta_jesRelativePtBB_Up;
   Float_t         H_eta_jesRelativePtBB_Down;
   Float_t         H_eta_jesRelativePtEC1_Up;
   Float_t         H_eta_jesRelativePtEC1_Down;
   Float_t         H_eta_jesRelativePtEC2_Up;
   Float_t         H_eta_jesRelativePtEC2_Down;
   Float_t         H_eta_jesRelativePtHF_Up;
   Float_t         H_eta_jesRelativePtHF_Down;
   Float_t         H_eta_jesRelativeBal_Up;
   Float_t         H_eta_jesRelativeBal_Down;
   Float_t         H_eta_jesRelativeFSR_Up;
   Float_t         H_eta_jesRelativeFSR_Down;
   Float_t         H_eta_jesRelativeStatFSR_Up;
   Float_t         H_eta_jesRelativeStatFSR_Down;
   Float_t         H_eta_jesRelativeStatEC_Up;
   Float_t         H_eta_jesRelativeStatEC_Down;
   Float_t         H_eta_jesRelativeStatHF_Up;
   Float_t         H_eta_jesRelativeStatHF_Down;
   Float_t         H_eta_jesPileUpDataMC_Up;
   Float_t         H_eta_jesPileUpDataMC_Down;
   Float_t         H_eta_jesPileUpPtRef_Up;
   Float_t         H_eta_jesPileUpPtRef_Down;
   Float_t         H_eta_jesPileUpPtBB_Up;
   Float_t         H_eta_jesPileUpPtBB_Down;
   Float_t         H_eta_jesPileUpPtEC1_Up;
   Float_t         H_eta_jesPileUpPtEC1_Down;
   Float_t         H_eta_jesPileUpPtEC2_Up;
   Float_t         H_eta_jesPileUpPtEC2_Down;
   Float_t         H_eta_jesPileUpPtHF_Up;
   Float_t         H_eta_jesPileUpPtHF_Down;
   Float_t         H_eta_jesPileUpMuZero_Up;
   Float_t         H_eta_jesPileUpMuZero_Down;
   Float_t         H_eta_jesPileUpEnvelope_Up;
   Float_t         H_eta_jesPileUpEnvelope_Down;
   Float_t         H_eta_jesTotal_Up;
   Float_t         H_eta_jesTotal_Down;
   Float_t         H_eta_minmax_Up;
   Float_t         H_eta_minmax_Down;
   Float_t         H_phi;
   Float_t         H_phi_jer_Up;
   Float_t         H_phi_jer_Down;
   Float_t         H_phi_jesAbsoluteStat_Up;
   Float_t         H_phi_jesAbsoluteStat_Down;
   Float_t         H_phi_jesAbsoluteScale_Up;
   Float_t         H_phi_jesAbsoluteScale_Down;
   Float_t         H_phi_jesAbsoluteFlavMap_Up;
   Float_t         H_phi_jesAbsoluteFlavMap_Down;
   Float_t         H_phi_jesAbsoluteMPFBias_Up;
   Float_t         H_phi_jesAbsoluteMPFBias_Down;
   Float_t         H_phi_jesFragmentation_Up;
   Float_t         H_phi_jesFragmentation_Down;
   Float_t         H_phi_jesSinglePionECAL_Up;
   Float_t         H_phi_jesSinglePionECAL_Down;
   Float_t         H_phi_jesSinglePionHCAL_Up;
   Float_t         H_phi_jesSinglePionHCAL_Down;
   Float_t         H_phi_jesFlavorQCD_Up;
   Float_t         H_phi_jesFlavorQCD_Down;
   Float_t         H_phi_jesRelativeJEREC1_Up;
   Float_t         H_phi_jesRelativeJEREC1_Down;
   Float_t         H_phi_jesRelativeJEREC2_Up;
   Float_t         H_phi_jesRelativeJEREC2_Down;
   Float_t         H_phi_jesRelativeJERHF_Up;
   Float_t         H_phi_jesRelativeJERHF_Down;
   Float_t         H_phi_jesRelativePtBB_Up;
   Float_t         H_phi_jesRelativePtBB_Down;
   Float_t         H_phi_jesRelativePtEC1_Up;
   Float_t         H_phi_jesRelativePtEC1_Down;
   Float_t         H_phi_jesRelativePtEC2_Up;
   Float_t         H_phi_jesRelativePtEC2_Down;
   Float_t         H_phi_jesRelativePtHF_Up;
   Float_t         H_phi_jesRelativePtHF_Down;
   Float_t         H_phi_jesRelativeBal_Up;
   Float_t         H_phi_jesRelativeBal_Down;
   Float_t         H_phi_jesRelativeFSR_Up;
   Float_t         H_phi_jesRelativeFSR_Down;
   Float_t         H_phi_jesRelativeStatFSR_Up;
   Float_t         H_phi_jesRelativeStatFSR_Down;
   Float_t         H_phi_jesRelativeStatEC_Up;
   Float_t         H_phi_jesRelativeStatEC_Down;
   Float_t         H_phi_jesRelativeStatHF_Up;
   Float_t         H_phi_jesRelativeStatHF_Down;
   Float_t         H_phi_jesPileUpDataMC_Up;
   Float_t         H_phi_jesPileUpDataMC_Down;
   Float_t         H_phi_jesPileUpPtRef_Up;
   Float_t         H_phi_jesPileUpPtRef_Down;
   Float_t         H_phi_jesPileUpPtBB_Up;
   Float_t         H_phi_jesPileUpPtBB_Down;
   Float_t         H_phi_jesPileUpPtEC1_Up;
   Float_t         H_phi_jesPileUpPtEC1_Down;
   Float_t         H_phi_jesPileUpPtEC2_Up;
   Float_t         H_phi_jesPileUpPtEC2_Down;
   Float_t         H_phi_jesPileUpPtHF_Up;
   Float_t         H_phi_jesPileUpPtHF_Down;
   Float_t         H_phi_jesPileUpMuZero_Up;
   Float_t         H_phi_jesPileUpMuZero_Down;
   Float_t         H_phi_jesPileUpEnvelope_Up;
   Float_t         H_phi_jesPileUpEnvelope_Down;
   Float_t         H_phi_jesTotal_Up;
   Float_t         H_phi_jesTotal_Down;
   Float_t         H_phi_minmax_Up;
   Float_t         H_phi_minmax_Down;
   Float_t         H_mass;
   Float_t         H_mass_jer_Up;
   Float_t         H_mass_jer_Down;
   Float_t         H_mass_jesAbsoluteStat_Up;
   Float_t         H_mass_jesAbsoluteStat_Down;
   Float_t         H_mass_jesAbsoluteScale_Up;
   Float_t         H_mass_jesAbsoluteScale_Down;
   Float_t         H_mass_jesAbsoluteFlavMap_Up;
   Float_t         H_mass_jesAbsoluteFlavMap_Down;
   Float_t         H_mass_jesAbsoluteMPFBias_Up;
   Float_t         H_mass_jesAbsoluteMPFBias_Down;
   Float_t         H_mass_jesFragmentation_Up;
   Float_t         H_mass_jesFragmentation_Down;
   Float_t         H_mass_jesSinglePionECAL_Up;
   Float_t         H_mass_jesSinglePionECAL_Down;
   Float_t         H_mass_jesSinglePionHCAL_Up;
   Float_t         H_mass_jesSinglePionHCAL_Down;
   Float_t         H_mass_jesFlavorQCD_Up;
   Float_t         H_mass_jesFlavorQCD_Down;
   Float_t         H_mass_jesRelativeJEREC1_Up;
   Float_t         H_mass_jesRelativeJEREC1_Down;
   Float_t         H_mass_jesRelativeJEREC2_Up;
   Float_t         H_mass_jesRelativeJEREC2_Down;
   Float_t         H_mass_jesRelativeJERHF_Up;
   Float_t         H_mass_jesRelativeJERHF_Down;
   Float_t         H_mass_jesRelativePtBB_Up;
   Float_t         H_mass_jesRelativePtBB_Down;
   Float_t         H_mass_jesRelativePtEC1_Up;
   Float_t         H_mass_jesRelativePtEC1_Down;
   Float_t         H_mass_jesRelativePtEC2_Up;
   Float_t         H_mass_jesRelativePtEC2_Down;
   Float_t         H_mass_jesRelativePtHF_Up;
   Float_t         H_mass_jesRelativePtHF_Down;
   Float_t         H_mass_jesRelativeBal_Up;
   Float_t         H_mass_jesRelativeBal_Down;
   Float_t         H_mass_jesRelativeFSR_Up;
   Float_t         H_mass_jesRelativeFSR_Down;
   Float_t         H_mass_jesRelativeStatFSR_Up;
   Float_t         H_mass_jesRelativeStatFSR_Down;
   Float_t         H_mass_jesRelativeStatEC_Up;
   Float_t         H_mass_jesRelativeStatEC_Down;
   Float_t         H_mass_jesRelativeStatHF_Up;
   Float_t         H_mass_jesRelativeStatHF_Down;
   Float_t         H_mass_jesPileUpDataMC_Up;
   Float_t         H_mass_jesPileUpDataMC_Down;
   Float_t         H_mass_jesPileUpPtRef_Up;
   Float_t         H_mass_jesPileUpPtRef_Down;
   Float_t         H_mass_jesPileUpPtBB_Up;
   Float_t         H_mass_jesPileUpPtBB_Down;
   Float_t         H_mass_jesPileUpPtEC1_Up;
   Float_t         H_mass_jesPileUpPtEC1_Down;
   Float_t         H_mass_jesPileUpPtEC2_Up;
   Float_t         H_mass_jesPileUpPtEC2_Down;
   Float_t         H_mass_jesPileUpPtHF_Up;
   Float_t         H_mass_jesPileUpPtHF_Down;
   Float_t         H_mass_jesPileUpMuZero_Up;
   Float_t         H_mass_jesPileUpMuZero_Down;
   Float_t         H_mass_jesPileUpEnvelope_Up;
   Float_t         H_mass_jesPileUpEnvelope_Down;
   Float_t         H_mass_jesTotal_Up;
   Float_t         H_mass_jesTotal_Down;
   Float_t         H_mass_minmax_Up;
   Float_t         H_mass_minmax_Down;
   Float_t         Jet_pt_minmaxUp[37];   //[nJet]
   Float_t         Jet_pt_minmaxDown[37];   //[nJet]
   Float_t         Jet_mass_minmaxUp[37];   //[nJet]
   Float_t         Jet_mass_minmaxDown[37];   //[nJet]
   Float_t         isSignal;
   Float_t         isWH;
   Float_t         isData;
   Int_t           nGenVbosons;
   Float_t         GenVbosons_pt[1];   //[nGenVbosons]
   Float_t         GenVbosons_pdgId[1];   //[nGenVbosons]
   Float_t         GenVbosons_GenPartIdx[1];   //[nGenVbosons]
   Int_t           nGenTop;
   Float_t         GenTop_pt[1];   //[nGenTop]
   Float_t         GenTop_GenPartIdx[1];   //[nGenTop]
   Int_t           nGenHiggsBoson;
   Float_t         GenHiggsBoson_pt[1];   //[nGenHiggsBoson]
   Float_t         GenHiggsBoson_GenPartIdx[1];   //[nGenHiggsBoson]
   Int_t           VtypeSim;
   Float_t         FitCorr[3];
   Float_t         top_mass;
   Float_t         V_mt;

   // List of branches
   TBranch        *b_run;   //!
   TBranch        *b_luminosityBlock;   //!
   TBranch        *b_event;   //!
   TBranch        *b_btagWeight_CSVV2;   //!
   TBranch        *b_btagWeight_CMVA;   //!
   TBranch        *b_CaloMET_phi;   //!
   TBranch        *b_CaloMET_pt;   //!
   TBranch        *b_CaloMET_sumEt;   //!
   TBranch        *b_nElectron;   //!
   TBranch        *b_Electron_deltaEtaSC;   //!
   TBranch        *b_Electron_dr03EcalRecHitSumEt;   //!
   TBranch        *b_Electron_dr03HcalDepth1TowerSumEt;   //!
   TBranch        *b_Electron_dr03TkSumPt;   //!
   TBranch        *b_Electron_dxy;   //!
   TBranch        *b_Electron_dxyErr;   //!
   TBranch        *b_Electron_dz;   //!
   TBranch        *b_Electron_dzErr;   //!
   TBranch        *b_Electron_eCorr;   //!
   TBranch        *b_Electron_eInvMinusPInv;   //!
   TBranch        *b_Electron_energyErr;   //!
   TBranch        *b_Electron_eta;   //!
   TBranch        *b_Electron_hoe;   //!
   TBranch        *b_Electron_ip3d;   //!
   TBranch        *b_Electron_mass;   //!
   TBranch        *b_Electron_miniPFRelIso_all;   //!
   TBranch        *b_Electron_miniPFRelIso_chg;   //!
   TBranch        *b_Electron_mvaSpring16GP;   //!
   TBranch        *b_Electron_mvaSpring16HZZ;   //!
   TBranch        *b_Electron_pfRelIso03_all;   //!
   TBranch        *b_Electron_pfRelIso03_chg;   //!
   TBranch        *b_Electron_phi;   //!
   TBranch        *b_Electron_pt;   //!
   TBranch        *b_Electron_r9;   //!
   TBranch        *b_Electron_sieie;   //!
   TBranch        *b_Electron_sip3d;   //!
   TBranch        *b_Electron_mvaTTH;   //!
   TBranch        *b_Electron_charge;   //!
   TBranch        *b_Electron_cutBased;   //!
   TBranch        *b_Electron_cutBased_HLTPreSel;   //!
   TBranch        *b_Electron_jetIdx;   //!
   TBranch        *b_Electron_pdgId;   //!
   TBranch        *b_Electron_photonIdx;   //!
   TBranch        *b_Electron_tightCharge;   //!
   TBranch        *b_Electron_vidNestedWPBitmap;   //!
   TBranch        *b_Electron_convVeto;   //!
   TBranch        *b_Electron_cutBased_HEEP;   //!
   TBranch        *b_Electron_isPFcand;   //!
   TBranch        *b_Electron_lostHits;   //!
   TBranch        *b_Electron_mvaSpring16GP_WP80;   //!
   TBranch        *b_Electron_mvaSpring16GP_WP90;   //!
   TBranch        *b_Electron_mvaSpring16HZZ_WPL;   //!
   TBranch        *b_Flag_BadChargedCandidateFilter;   //!
   TBranch        *b_Flag_BadGlobalMuon;   //!
   TBranch        *b_Flag_BadPFMuonFilter;   //!
   TBranch        *b_Flag_CloneGlobalMuon;   //!
   TBranch        *b_nGenJetAK8;   //!
   TBranch        *b_GenJetAK8_eta;   //!
   TBranch        *b_GenJetAK8_mass;   //!
   TBranch        *b_GenJetAK8_phi;   //!
   TBranch        *b_GenJetAK8_pt;   //!
   TBranch        *b_nGenJet;   //!
   TBranch        *b_GenJet_eta;   //!
   TBranch        *b_GenJet_mass;   //!
   TBranch        *b_GenJet_phi;   //!
   TBranch        *b_GenJet_pt;   //!
   TBranch        *b_nGenPart;   //!
   TBranch        *b_GenPart_eta;   //!
   TBranch        *b_GenPart_mass;   //!
   TBranch        *b_GenPart_phi;   //!
   TBranch        *b_GenPart_pt;   //!
   TBranch        *b_GenPart_genPartIdxMother;   //!
   TBranch        *b_GenPart_pdgId;   //!
   TBranch        *b_GenPart_status;   //!
   TBranch        *b_GenPart_statusFlags;   //!
   TBranch        *b_Generator_binvar;   //!
   TBranch        *b_Generator_scalePDF;   //!
   TBranch        *b_Generator_weight;   //!
   TBranch        *b_Generator_x1;   //!
   TBranch        *b_Generator_x2;   //!
   TBranch        *b_Generator_xpdf1;   //!
   TBranch        *b_Generator_xpdf2;   //!
   TBranch        *b_Generator_id1;   //!
   TBranch        *b_Generator_id2;   //!
   TBranch        *b_genWeight;   //!
   TBranch        *b_LHEWeight_originalXWGTUP;   //!
   TBranch        *b_nLHEPdfWeight;   //!
   TBranch        *b_LHEPdfWeight;   //!
   TBranch        *b_nLHEScaleWeight;   //!
   TBranch        *b_LHEScaleWeight;   //!
   TBranch        *b_nJet;   //!
   TBranch        *b_Jet_area;   //!
   TBranch        *b_Jet_btagCMVA;   //!
   TBranch        *b_Jet_btagCSVV2;   //!
   TBranch        *b_Jet_btagDeepB;   //!
   TBranch        *b_Jet_btagDeepC;   //!
   TBranch        *b_Jet_btagDeepFlavB;   //!
   TBranch        *b_Jet_chEmEF;   //!
   TBranch        *b_Jet_chHEF;   //!
   TBranch        *b_Jet_eta;   //!
   TBranch        *b_Jet_mass;   //!
   TBranch        *b_Jet_neEmEF;   //!
   TBranch        *b_Jet_neHEF;   //!
   TBranch        *b_Jet_phi;   //!
   TBranch        *b_Jet_pt;   //!
   TBranch        *b_Jet_qgl;   //!
   TBranch        *b_Jet_rawFactor;   //!
   TBranch        *b_Jet_bReg;   //!
   TBranch        *b_Jet_bRegOld;   //!
   TBranch        *b_Jet_bRegRes;   //!
   TBranch        *b_Jet_electronIdx1;   //!
   TBranch        *b_Jet_electronIdx2;   //!
   TBranch        *b_Jet_jetId;   //!
   TBranch        *b_Jet_muonIdx1;   //!
   TBranch        *b_Jet_muonIdx2;   //!
   TBranch        *b_Jet_nConstituents;   //!
   TBranch        *b_Jet_nElectrons;   //!
   TBranch        *b_Jet_nMuons;   //!
   TBranch        *b_Jet_puId;   //!
   TBranch        *b_LHE_HT;   //!
   TBranch        *b_LHE_HTIncoming;   //!
   TBranch        *b_LHE_Vpt;   //!
   TBranch        *b_LHE_Njets;   //!
   TBranch        *b_LHE_Nb;   //!
   TBranch        *b_LHE_Nc;   //!
   TBranch        *b_LHE_Nuds;   //!
   TBranch        *b_LHE_Nglu;   //!
   TBranch        *b_LHE_NpNLO;   //!
   TBranch        *b_LHE_NpLO;   //!
   TBranch        *b_nLHEPart;   //!
   TBranch        *b_LHEPart_pt;   //!
   TBranch        *b_LHEPart_eta;   //!
   TBranch        *b_LHEPart_phi;   //!
   TBranch        *b_LHEPart_mass;   //!
   TBranch        *b_LHEPart_pdgId;   //!
   TBranch        *b_GenMET_phi;   //!
   TBranch        *b_GenMET_pt;   //!
   TBranch        *b_MET_MetUnclustEnUpDeltaX;   //!
   TBranch        *b_MET_MetUnclustEnUpDeltaY;   //!
   TBranch        *b_MET_covXX;   //!
   TBranch        *b_MET_covXY;   //!
   TBranch        *b_MET_covYY;   //!
   TBranch        *b_MET_phi;   //!
   TBranch        *b_MET_pt;   //!
   TBranch        *b_MET_significance;   //!
   TBranch        *b_MET_sumEt;   //!
   TBranch        *b_nMuon;   //!
   TBranch        *b_Muon_dxy;   //!
   TBranch        *b_Muon_dxyErr;   //!
   TBranch        *b_Muon_dz;   //!
   TBranch        *b_Muon_dzErr;   //!
   TBranch        *b_Muon_eta;   //!
   TBranch        *b_Muon_ip3d;   //!
   TBranch        *b_Muon_mass;   //!
   TBranch        *b_Muon_miniPFRelIso_all;   //!
   TBranch        *b_Muon_miniPFRelIso_chg;   //!
   TBranch        *b_Muon_pfRelIso03_all;   //!
   TBranch        *b_Muon_pfRelIso03_chg;   //!
   TBranch        *b_Muon_pfRelIso04_all;   //!
   TBranch        *b_Muon_phi;   //!
   TBranch        *b_Muon_pt;   //!
   TBranch        *b_Muon_ptErr;   //!
   TBranch        *b_Muon_segmentComp;   //!
   TBranch        *b_Muon_sip3d;   //!
   TBranch        *b_Muon_mvaTTH;   //!
   TBranch        *b_Muon_charge;   //!
   TBranch        *b_Muon_jetIdx;   //!
   TBranch        *b_Muon_nStations;   //!
   TBranch        *b_Muon_nTrackerLayers;   //!
   TBranch        *b_Muon_pdgId;   //!
   TBranch        *b_Muon_tightCharge;   //!
   TBranch        *b_Muon_highPtId;   //!
   TBranch        *b_Muon_isPFcand;   //!
   TBranch        *b_Muon_mediumId;   //!
   TBranch        *b_Muon_softId;   //!
   TBranch        *b_Muon_tightId;   //!
   TBranch        *b_Pileup_nTrueInt;   //!
   TBranch        *b_Pileup_nPU;   //!
   TBranch        *b_Pileup_sumEOOT;   //!
   TBranch        *b_Pileup_sumLOOT;   //!
   TBranch        *b_PuppiMET_phi;   //!
   TBranch        *b_PuppiMET_pt;   //!
   TBranch        *b_PuppiMET_sumEt;   //!
   TBranch        *b_RawMET_phi;   //!
   TBranch        *b_RawMET_pt;   //!
   TBranch        *b_RawMET_sumEt;   //!
   TBranch        *b_fixedGridRhoFastjetAll;   //!
   TBranch        *b_fixedGridRhoFastjetCentralCalo;   //!
   TBranch        *b_fixedGridRhoFastjetCentralNeutral;   //!
   TBranch        *b_nGenDressedLepton;   //!
   TBranch        *b_GenDressedLepton_eta;   //!
   TBranch        *b_GenDressedLepton_mass;   //!
   TBranch        *b_GenDressedLepton_phi;   //!
   TBranch        *b_GenDressedLepton_pt;   //!
   TBranch        *b_GenDressedLepton_pdgId;   //!
   TBranch        *b_nSoftActivityJet;   //!
   TBranch        *b_SoftActivityJet_eta;   //!
   TBranch        *b_SoftActivityJet_phi;   //!
   TBranch        *b_SoftActivityJet_pt;   //!
   TBranch        *b_SoftActivityJetHT;   //!
   TBranch        *b_SoftActivityJetHT10;   //!
   TBranch        *b_SoftActivityJetHT2;   //!
   TBranch        *b_SoftActivityJetHT5;   //!
   TBranch        *b_SoftActivityJetNjets10;   //!
   TBranch        *b_SoftActivityJetNjets2;   //!
   TBranch        *b_SoftActivityJetNjets5;   //!
   TBranch        *b_TkMET_phi;   //!
   TBranch        *b_TkMET_pt;   //!
   TBranch        *b_TkMET_sumEt;   //!
   TBranch        *b_genTtbarId;   //!
   TBranch        *b_nOtherPV;   //!
   TBranch        *b_OtherPV_z;   //!
   TBranch        *b_PV_ndof;   //!
   TBranch        *b_PV_x;   //!
   TBranch        *b_PV_y;   //!
   TBranch        *b_PV_z;   //!
   TBranch        *b_PV_chi2;   //!
   TBranch        *b_PV_score;   //!
   TBranch        *b_PV_npvs;   //!
   TBranch        *b_PV_npvsGood;   //!
   TBranch        *b_nSV;   //!
   TBranch        *b_SV_dlen;   //!
   TBranch        *b_SV_dlenSig;   //!
   TBranch        *b_SV_pAngle;   //!
   TBranch        *b_Electron_genPartIdx;   //!
   TBranch        *b_Electron_genPartFlav;   //!
   TBranch        *b_GenJetAK8_partonFlavour;   //!
   TBranch        *b_GenJetAK8_hadronFlavour;   //!
   TBranch        *b_GenJet_partonFlavour;   //!
   TBranch        *b_GenJet_hadronFlavour;   //!
   TBranch        *b_Jet_genJetIdx;   //!
   TBranch        *b_Jet_hadronFlavour;   //!
   TBranch        *b_Jet_partonFlavour;   //!
   TBranch        *b_Muon_genPartIdx;   //!
   TBranch        *b_Muon_genPartFlav;   //!
   TBranch        *b_MET_fiducialGenPhi;   //!
   TBranch        *b_MET_fiducialGenPt;   //!
   TBranch        *b_Electron_cleanmask;   //!
   TBranch        *b_Jet_cleanmask;   //!
   TBranch        *b_Muon_cleanmask;   //!
   TBranch        *b_SV_chi2;   //!
   TBranch        *b_SV_eta;   //!
   TBranch        *b_SV_mass;   //!
   TBranch        *b_SV_ndof;   //!
   TBranch        *b_SV_phi;   //!
   TBranch        *b_SV_pt;   //!
   TBranch        *b_SV_x;   //!
   TBranch        *b_SV_y;   //!
   TBranch        *b_SV_z;   //!
   TBranch        *b_L1simulation_step;   //!
   TBranch        *b_HLTriggerFirstPath;   //!
   TBranch        *b_HLT_Mu7p5_L2Mu2_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_L2Mu2_Upsilon;   //!
   TBranch        *b_HLT_Mu7p5_Track2_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_Track3p5_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_Track7_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_Track2_Upsilon;   //!
   TBranch        *b_HLT_Mu7p5_Track3p5_Upsilon;   //!
   TBranch        *b_HLT_Mu7p5_Track7_Upsilon;   //!
   TBranch        *b_HLT_Ele17_Ele8_Gsf;   //!
   TBranch        *b_HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28;   //!
   TBranch        *b_HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29;   //!
   TBranch        *b_HLT_Ele22_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_Ele23_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele23_WPLoose_Gsf_WHbbBoost;   //!
   TBranch        *b_HLT_Ele24_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20;   //!
   TBranch        *b_HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30;   //!
   TBranch        *b_HLT_Ele25_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele25_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele25_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele27_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele27_WPLoose_Gsf_WHbbBoost;   //!
   TBranch        *b_HLT_Ele27_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele27_WPTight_Gsf_L1JetTauSeeded;   //!
   TBranch        *b_HLT_Ele27_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_Ele27_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele30_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele30_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele30_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele32_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele32_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_Ele32_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele35_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50;   //!
   TBranch        *b_HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_Ele45_WPLoose_Gsf;   //!
   TBranch        *b_HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded;   //!
   TBranch        *b_HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50;   //!
   TBranch        *b_HLT_Ele105_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_Ele30WP60_SC4_Mass55;   //!
   TBranch        *b_HLT_Ele30WP60_Ele8_Mass55;   //!
   TBranch        *b_HLT_Mu16_eta2p1_MET30;   //!
   TBranch        *b_HLT_IsoMu16_eta2p1_MET30;   //!
   TBranch        *b_HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1;   //!
   TBranch        *b_HLT_IsoMu17_eta2p1;   //!
   TBranch        *b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20;   //!
   TBranch        *b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_IsoMu18;   //!
   TBranch        *b_HLT_IsoMu19_eta2p1_LooseIsoPFTau20;   //!
   TBranch        *b_HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20;   //!
   TBranch        *b_HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_IsoMu20;   //!
   TBranch        *b_HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1;   //!
   TBranch        *b_HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_IsoMu22;   //!
   TBranch        *b_HLT_IsoMu22_eta2p1;   //!
   TBranch        *b_HLT_IsoMu24;   //!
   TBranch        *b_HLT_IsoMu27;   //!
   TBranch        *b_HLT_IsoTkMu18;   //!
   TBranch        *b_HLT_IsoTkMu20;   //!
   TBranch        *b_HLT_IsoTkMu22;   //!
   TBranch        *b_HLT_IsoTkMu22_eta2p1;   //!
   TBranch        *b_HLT_IsoTkMu24;   //!
   TBranch        *b_HLT_IsoTkMu27;   //!
   TBranch        *b_HLT_JetE30_NoBPTX3BX;   //!
   TBranch        *b_HLT_JetE30_NoBPTX;   //!
   TBranch        *b_HLT_JetE50_NoBPTX3BX;   //!
   TBranch        *b_HLT_JetE70_NoBPTX3BX;   //!
   TBranch        *b_HLT_L2Mu10;   //!
   TBranch        *b_HLT_L2DoubleMu23_NoVertex;   //!
   TBranch        *b_HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10;   //!
   TBranch        *b_HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10;   //!
   TBranch        *b_HLT_L2Mu10_NoVertex_NoBPTX3BX;   //!
   TBranch        *b_HLT_L2Mu10_NoVertex_NoBPTX;   //!
   TBranch        *b_HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX;   //!
   TBranch        *b_HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX;   //!
   TBranch        *b_HLT_LooseIsoPFTau50_Trk30_eta2p1;   //!
   TBranch        *b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80;   //!
   TBranch        *b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90;   //!
   TBranch        *b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110;   //!
   TBranch        *b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120;   //!
   TBranch        *b_HLT_VLooseIsoPFTau120_Trk50_eta2p1;   //!
   TBranch        *b_HLT_VLooseIsoPFTau140_Trk50_eta2p1;   //!
   TBranch        *b_HLT_Mu17_Mu8;   //!
   TBranch        *b_HLT_Mu17_Mu8_DZ;   //!
   TBranch        *b_HLT_Mu17_Mu8_SameSign;   //!
   TBranch        *b_HLT_Mu17_Mu8_SameSign_DZ;   //!
   TBranch        *b_HLT_Mu20_Mu10;   //!
   TBranch        *b_HLT_Mu20_Mu10_DZ;   //!
   TBranch        *b_HLT_Mu20_Mu10_SameSign;   //!
   TBranch        *b_HLT_Mu20_Mu10_SameSign_DZ;   //!
   TBranch        *b_HLT_Mu17_TkMu8_DZ;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ;   //!
   TBranch        *b_HLT_Mu25_TkMu0_dEta18_Onia;   //!
   TBranch        *b_HLT_Mu27_TkMu8;   //!
   TBranch        *b_HLT_Mu30_TkMu11;   //!
   TBranch        *b_HLT_Mu30_eta2p1_PFJet150_PFJet50;   //!
   TBranch        *b_HLT_Mu40_TkMu11;   //!
   TBranch        *b_HLT_Mu40_eta2p1_PFJet200_PFJet50;   //!
   TBranch        *b_HLT_Mu20;   //!
   TBranch        *b_HLT_TkMu17;   //!
   TBranch        *b_HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ;   //!
   TBranch        *b_HLT_TkMu20;   //!
   TBranch        *b_HLT_Mu24_eta2p1;   //!
   TBranch        *b_HLT_TkMu24_eta2p1;   //!
   TBranch        *b_HLT_Mu27;   //!
   TBranch        *b_HLT_TkMu27;   //!
   TBranch        *b_HLT_Mu45_eta2p1;   //!
   TBranch        *b_HLT_Mu50;   //!
   TBranch        *b_HLT_TkMu50;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL;   //!
   TBranch        *b_HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL;   //!
   TBranch        *b_HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL;   //!
   TBranch        *b_HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL;   //!
   TBranch        *b_HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL;   //!
   TBranch        *b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight;   //!
   TBranch        *b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose;   //!
   TBranch        *b_HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose;   //!
   TBranch        *b_HLT_Mu28NoFiltersNoVtx_CentralCaloJet40;   //!
   TBranch        *b_HLT_SingleCentralPFJet170_CFMax0p1;   //!
   TBranch        *b_HLT_MET60_IsoTrk35_Loose;   //!
   TBranch        *b_HLT_MET75_IsoTrk50;   //!
   TBranch        *b_HLT_MET90_IsoTrk50;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL;   //!
   TBranch        *b_HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded;   //!
   TBranch        *b_HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_Mu8_DiEle12_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_Mu12_Photon25_CaloIdL;   //!
   TBranch        *b_HLT_Mu12_Photon25_CaloIdL_L1ISO;   //!
   TBranch        *b_HLT_Mu12_Photon25_CaloIdL_L1OR;   //!
   TBranch        *b_HLT_Mu17_Photon22_CaloIdL_L1ISO;   //!
   TBranch        *b_HLT_Mu17_Photon30_CaloIdL_L1ISO;   //!
   TBranch        *b_HLT_Mu17_Photon35_CaloIdL_L1ISO;   //!
   TBranch        *b_HLT_Mu3er_PFHT140_PFMET125;   //!
   TBranch        *b_HLT_Mu6_PFHT200_PFMET80_BTagCSV_p067;   //!
   TBranch        *b_HLT_Mu6_PFHT200_PFMET100;   //!
   TBranch        *b_HLT_Mu14er_PFMET100;   //!
   TBranch        *b_HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Ele17_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_Ele17_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Ele27_eta2p1_WPLoose_Gsf_HT200;   //!
   TBranch        *b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250;   //!
   TBranch        *b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300;   //!
   TBranch        *b_HLT_Mu10_CentralPFJet30_BTagCSV_p13;   //!
   TBranch        *b_HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT350_PFMET50;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT600;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT350;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT400_PFMET50;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT400;   //!
   TBranch        *b_HLT_Ele50_IsoVVVL_PFHT400;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60;   //!
   TBranch        *b_HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT350_PFMET50;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT600;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT350;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT400_PFMET50;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT400;   //!
   TBranch        *b_HLT_Mu50_IsoVVVL_PFHT400;   //!
   TBranch        *b_HLT_Mu16_TkMu0_dEta18_Onia;   //!
   TBranch        *b_HLT_Mu16_TkMu0_dEta18_Phi;   //!
   TBranch        *b_HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx;   //!
   TBranch        *b_HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx;   //!
   TBranch        *b_HLT_Mu8;   //!
   TBranch        *b_HLT_Mu17;   //!
   TBranch        *b_HLT_Mu3_PFJet40;   //!
   TBranch        *b_HLT_Ele8_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele12_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele17_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele23_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165;   //!
   TBranch        *b_HLT_Ele115_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_Mu55;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity60ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity85ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity110ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity135ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity160ForEndOfFill;   //!
   TBranch        *b_HLT_ECALHT800;   //!
   TBranch        *b_HLT_MET100;   //!
   TBranch        *b_HLT_MET150;   //!
   TBranch        *b_HLT_MET200;   //!
   TBranch        *b_HLT_Ele27_HighEta_Ele20_Mass55;   //!
   TBranch        *b_HLT_Random;   //!
   TBranch        *b_HLT_EcalCalibration;   //!
   TBranch        *b_HLT_HcalCalibration;   //!
   TBranch        *b_HLT_GlobalRunHPDNoise;   //!
   TBranch        *b_HLT_HcalNZS;   //!
   TBranch        *b_HLT_HcalPhiSym;   //!
   TBranch        *b_HLT_HcalIsolatedbunch;   //!
   TBranch        *b_HLT_Mu300;   //!
   TBranch        *b_HLT_Mu350;   //!
   TBranch        *b_HLT_MET250;   //!
   TBranch        *b_HLT_MET300;   //!
   TBranch        *b_HLT_MET600;   //!
   TBranch        *b_HLT_MET700;   //!
   TBranch        *b_HLT_Ele250_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_Ele300_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_IsoTrackHE;   //!
   TBranch        *b_HLT_IsoTrackHB;   //!
   TBranch        *b_HLTriggerFinalPath;   //!
   TBranch        *b_Flag_HBHENoiseFilter;   //!
   TBranch        *b_Flag_HBHENoiseIsoFilter;   //!
   TBranch        *b_Flag_CSCTightHaloFilter;   //!
   TBranch        *b_Flag_CSCTightHaloTrkMuUnvetoFilter;   //!
   TBranch        *b_Flag_CSCTightHalo2015Filter;   //!
   TBranch        *b_Flag_globalTightHalo2016Filter;   //!
   TBranch        *b_Flag_globalSuperTightHalo2016Filter;   //!
   TBranch        *b_Flag_HcalStripHaloFilter;   //!
   TBranch        *b_Flag_hcalLaserEventFilter;   //!
   TBranch        *b_Flag_EcalDeadCellTriggerPrimitiveFilter;   //!
   TBranch        *b_Flag_EcalDeadCellBoundaryEnergyFilter;   //!
   TBranch        *b_Flag_goodVertices;   //!
   TBranch        *b_Flag_eeBadScFilter;   //!
   TBranch        *b_Flag_ecalLaserCorrFilter;   //!
   TBranch        *b_Flag_trkPOGFilters;   //!
   TBranch        *b_Flag_chargedHadronTrackResolutionFilter;   //!
   TBranch        *b_Flag_muonBadTrackFilter;   //!
   TBranch        *b_Flag_trkPOG_manystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_toomanystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_logErrorTooManyClusters;   //!
   TBranch        *b_Flag_METFilters;   //!
   TBranch        *b_puWeight;   //!
   TBranch        *b_puWeightUp;   //!
   TBranch        *b_puWeightDown;   //!
   TBranch        *b_Jet_pt_nom;   //!
   TBranch        *b_Jet_mass_nom;   //!
   TBranch        *b_MET_pt_nom;   //!
   TBranch        *b_MET_phi_nom;   //!
   TBranch        *b_Jet_pt_jerUp;   //!
   TBranch        *b_Jet_mass_jerUp;   //!
   TBranch        *b_Jet_mass_jmrUp;   //!
   TBranch        *b_Jet_mass_jmsUp;   //!
   TBranch        *b_MET_pt_jerUp;   //!
   TBranch        *b_MET_phi_jerUp;   //!
   TBranch        *b_Jet_pt_jesAbsoluteStatUp;   //!
   TBranch        *b_Jet_mass_jesAbsoluteStatUp;   //!
   TBranch        *b_MET_pt_jesAbsoluteStatUp;   //!
   TBranch        *b_MET_phi_jesAbsoluteStatUp;   //!
   TBranch        *b_Jet_pt_jesAbsoluteScaleUp;   //!
   TBranch        *b_Jet_mass_jesAbsoluteScaleUp;   //!
   TBranch        *b_MET_pt_jesAbsoluteScaleUp;   //!
   TBranch        *b_MET_phi_jesAbsoluteScaleUp;   //!
   TBranch        *b_Jet_pt_jesAbsoluteFlavMapUp;   //!
   TBranch        *b_Jet_mass_jesAbsoluteFlavMapUp;   //!
   TBranch        *b_MET_pt_jesAbsoluteFlavMapUp;   //!
   TBranch        *b_MET_phi_jesAbsoluteFlavMapUp;   //!
   TBranch        *b_Jet_pt_jesAbsoluteMPFBiasUp;   //!
   TBranch        *b_Jet_mass_jesAbsoluteMPFBiasUp;   //!
   TBranch        *b_MET_pt_jesAbsoluteMPFBiasUp;   //!
   TBranch        *b_MET_phi_jesAbsoluteMPFBiasUp;   //!
   TBranch        *b_Jet_pt_jesFragmentationUp;   //!
   TBranch        *b_Jet_mass_jesFragmentationUp;   //!
   TBranch        *b_MET_pt_jesFragmentationUp;   //!
   TBranch        *b_MET_phi_jesFragmentationUp;   //!
   TBranch        *b_Jet_pt_jesSinglePionECALUp;   //!
   TBranch        *b_Jet_mass_jesSinglePionECALUp;   //!
   TBranch        *b_MET_pt_jesSinglePionECALUp;   //!
   TBranch        *b_MET_phi_jesSinglePionECALUp;   //!
   TBranch        *b_Jet_pt_jesSinglePionHCALUp;   //!
   TBranch        *b_Jet_mass_jesSinglePionHCALUp;   //!
   TBranch        *b_MET_pt_jesSinglePionHCALUp;   //!
   TBranch        *b_MET_phi_jesSinglePionHCALUp;   //!
   TBranch        *b_Jet_pt_jesFlavorQCDUp;   //!
   TBranch        *b_Jet_mass_jesFlavorQCDUp;   //!
   TBranch        *b_MET_pt_jesFlavorQCDUp;   //!
   TBranch        *b_MET_phi_jesFlavorQCDUp;   //!
   TBranch        *b_Jet_pt_jesTimePtEtaUp;   //!
   TBranch        *b_Jet_mass_jesTimePtEtaUp;   //!
   TBranch        *b_MET_pt_jesTimePtEtaUp;   //!
   TBranch        *b_MET_phi_jesTimePtEtaUp;   //!
   TBranch        *b_Jet_pt_jesRelativeJEREC1Up;   //!
   TBranch        *b_Jet_mass_jesRelativeJEREC1Up;   //!
   TBranch        *b_MET_pt_jesRelativeJEREC1Up;   //!
   TBranch        *b_MET_phi_jesRelativeJEREC1Up;   //!
   TBranch        *b_Jet_pt_jesRelativeJEREC2Up;   //!
   TBranch        *b_Jet_mass_jesRelativeJEREC2Up;   //!
   TBranch        *b_MET_pt_jesRelativeJEREC2Up;   //!
   TBranch        *b_MET_phi_jesRelativeJEREC2Up;   //!
   TBranch        *b_Jet_pt_jesRelativeJERHFUp;   //!
   TBranch        *b_Jet_mass_jesRelativeJERHFUp;   //!
   TBranch        *b_MET_pt_jesRelativeJERHFUp;   //!
   TBranch        *b_MET_phi_jesRelativeJERHFUp;   //!
   TBranch        *b_Jet_pt_jesRelativePtBBUp;   //!
   TBranch        *b_Jet_mass_jesRelativePtBBUp;   //!
   TBranch        *b_MET_pt_jesRelativePtBBUp;   //!
   TBranch        *b_MET_phi_jesRelativePtBBUp;   //!
   TBranch        *b_Jet_pt_jesRelativePtEC1Up;   //!
   TBranch        *b_Jet_mass_jesRelativePtEC1Up;   //!
   TBranch        *b_MET_pt_jesRelativePtEC1Up;   //!
   TBranch        *b_MET_phi_jesRelativePtEC1Up;   //!
   TBranch        *b_Jet_pt_jesRelativePtEC2Up;   //!
   TBranch        *b_Jet_mass_jesRelativePtEC2Up;   //!
   TBranch        *b_MET_pt_jesRelativePtEC2Up;   //!
   TBranch        *b_MET_phi_jesRelativePtEC2Up;   //!
   TBranch        *b_Jet_pt_jesRelativePtHFUp;   //!
   TBranch        *b_Jet_mass_jesRelativePtHFUp;   //!
   TBranch        *b_MET_pt_jesRelativePtHFUp;   //!
   TBranch        *b_MET_phi_jesRelativePtHFUp;   //!
   TBranch        *b_Jet_pt_jesRelativeBalUp;   //!
   TBranch        *b_Jet_mass_jesRelativeBalUp;   //!
   TBranch        *b_MET_pt_jesRelativeBalUp;   //!
   TBranch        *b_MET_phi_jesRelativeBalUp;   //!
   TBranch        *b_Jet_pt_jesRelativeFSRUp;   //!
   TBranch        *b_Jet_mass_jesRelativeFSRUp;   //!
   TBranch        *b_MET_pt_jesRelativeFSRUp;   //!
   TBranch        *b_MET_phi_jesRelativeFSRUp;   //!
   TBranch        *b_Jet_pt_jesRelativeStatFSRUp;   //!
   TBranch        *b_Jet_mass_jesRelativeStatFSRUp;   //!
   TBranch        *b_MET_pt_jesRelativeStatFSRUp;   //!
   TBranch        *b_MET_phi_jesRelativeStatFSRUp;   //!
   TBranch        *b_Jet_pt_jesRelativeStatECUp;   //!
   TBranch        *b_Jet_mass_jesRelativeStatECUp;   //!
   TBranch        *b_MET_pt_jesRelativeStatECUp;   //!
   TBranch        *b_MET_phi_jesRelativeStatECUp;   //!
   TBranch        *b_Jet_pt_jesRelativeStatHFUp;   //!
   TBranch        *b_Jet_mass_jesRelativeStatHFUp;   //!
   TBranch        *b_MET_pt_jesRelativeStatHFUp;   //!
   TBranch        *b_MET_phi_jesRelativeStatHFUp;   //!
   TBranch        *b_Jet_pt_jesPileUpDataMCUp;   //!
   TBranch        *b_Jet_mass_jesPileUpDataMCUp;   //!
   TBranch        *b_MET_pt_jesPileUpDataMCUp;   //!
   TBranch        *b_MET_phi_jesPileUpDataMCUp;   //!
   TBranch        *b_Jet_pt_jesPileUpPtRefUp;   //!
   TBranch        *b_Jet_mass_jesPileUpPtRefUp;   //!
   TBranch        *b_MET_pt_jesPileUpPtRefUp;   //!
   TBranch        *b_MET_phi_jesPileUpPtRefUp;   //!
   TBranch        *b_Jet_pt_jesPileUpPtBBUp;   //!
   TBranch        *b_Jet_mass_jesPileUpPtBBUp;   //!
   TBranch        *b_MET_pt_jesPileUpPtBBUp;   //!
   TBranch        *b_MET_phi_jesPileUpPtBBUp;   //!
   TBranch        *b_Jet_pt_jesPileUpPtEC1Up;   //!
   TBranch        *b_Jet_mass_jesPileUpPtEC1Up;   //!
   TBranch        *b_MET_pt_jesPileUpPtEC1Up;   //!
   TBranch        *b_MET_phi_jesPileUpPtEC1Up;   //!
   TBranch        *b_Jet_pt_jesPileUpPtEC2Up;   //!
   TBranch        *b_Jet_mass_jesPileUpPtEC2Up;   //!
   TBranch        *b_MET_pt_jesPileUpPtEC2Up;   //!
   TBranch        *b_MET_phi_jesPileUpPtEC2Up;   //!
   TBranch        *b_Jet_pt_jesPileUpPtHFUp;   //!
   TBranch        *b_Jet_mass_jesPileUpPtHFUp;   //!
   TBranch        *b_MET_pt_jesPileUpPtHFUp;   //!
   TBranch        *b_MET_phi_jesPileUpPtHFUp;   //!
   TBranch        *b_Jet_pt_jesPileUpMuZeroUp;   //!
   TBranch        *b_Jet_mass_jesPileUpMuZeroUp;   //!
   TBranch        *b_MET_pt_jesPileUpMuZeroUp;   //!
   TBranch        *b_MET_phi_jesPileUpMuZeroUp;   //!
   TBranch        *b_Jet_pt_jesPileUpEnvelopeUp;   //!
   TBranch        *b_Jet_mass_jesPileUpEnvelopeUp;   //!
   TBranch        *b_MET_pt_jesPileUpEnvelopeUp;   //!
   TBranch        *b_MET_phi_jesPileUpEnvelopeUp;   //!
   TBranch        *b_Jet_pt_jesSubTotalPileUpUp;   //!
   TBranch        *b_Jet_mass_jesSubTotalPileUpUp;   //!
   TBranch        *b_MET_pt_jesSubTotalPileUpUp;   //!
   TBranch        *b_MET_phi_jesSubTotalPileUpUp;   //!
   TBranch        *b_Jet_pt_jesSubTotalRelativeUp;   //!
   TBranch        *b_Jet_mass_jesSubTotalRelativeUp;   //!
   TBranch        *b_MET_pt_jesSubTotalRelativeUp;   //!
   TBranch        *b_MET_phi_jesSubTotalRelativeUp;   //!
   TBranch        *b_Jet_pt_jesSubTotalPtUp;   //!
   TBranch        *b_Jet_mass_jesSubTotalPtUp;   //!
   TBranch        *b_MET_pt_jesSubTotalPtUp;   //!
   TBranch        *b_MET_phi_jesSubTotalPtUp;   //!
   TBranch        *b_Jet_pt_jesSubTotalScaleUp;   //!
   TBranch        *b_Jet_mass_jesSubTotalScaleUp;   //!
   TBranch        *b_MET_pt_jesSubTotalScaleUp;   //!
   TBranch        *b_MET_phi_jesSubTotalScaleUp;   //!
   TBranch        *b_Jet_pt_jesSubTotalAbsoluteUp;   //!
   TBranch        *b_Jet_mass_jesSubTotalAbsoluteUp;   //!
   TBranch        *b_MET_pt_jesSubTotalAbsoluteUp;   //!
   TBranch        *b_MET_phi_jesSubTotalAbsoluteUp;   //!
   TBranch        *b_Jet_pt_jesSubTotalMCUp;   //!
   TBranch        *b_Jet_mass_jesSubTotalMCUp;   //!
   TBranch        *b_MET_pt_jesSubTotalMCUp;   //!
   TBranch        *b_MET_phi_jesSubTotalMCUp;   //!
   TBranch        *b_Jet_pt_jesTotalUp;   //!
   TBranch        *b_Jet_mass_jesTotalUp;   //!
   TBranch        *b_MET_pt_jesTotalUp;   //!
   TBranch        *b_MET_phi_jesTotalUp;   //!
   TBranch        *b_Jet_pt_jesTotalNoFlavorUp;   //!
   TBranch        *b_Jet_mass_jesTotalNoFlavorUp;   //!
   TBranch        *b_MET_pt_jesTotalNoFlavorUp;   //!
   TBranch        *b_MET_phi_jesTotalNoFlavorUp;   //!
   TBranch        *b_Jet_pt_jesTotalNoTimeUp;   //!
   TBranch        *b_Jet_mass_jesTotalNoTimeUp;   //!
   TBranch        *b_MET_pt_jesTotalNoTimeUp;   //!
   TBranch        *b_MET_phi_jesTotalNoTimeUp;   //!
   TBranch        *b_Jet_pt_jesTotalNoFlavorNoTimeUp;   //!
   TBranch        *b_Jet_mass_jesTotalNoFlavorNoTimeUp;   //!
   TBranch        *b_MET_pt_jesTotalNoFlavorNoTimeUp;   //!
   TBranch        *b_MET_phi_jesTotalNoFlavorNoTimeUp;   //!
   TBranch        *b_Jet_pt_jesFlavorZJetUp;   //!
   TBranch        *b_Jet_mass_jesFlavorZJetUp;   //!
   TBranch        *b_MET_pt_jesFlavorZJetUp;   //!
   TBranch        *b_MET_phi_jesFlavorZJetUp;   //!
   TBranch        *b_Jet_pt_jesFlavorPhotonJetUp;   //!
   TBranch        *b_Jet_mass_jesFlavorPhotonJetUp;   //!
   TBranch        *b_MET_pt_jesFlavorPhotonJetUp;   //!
   TBranch        *b_MET_phi_jesFlavorPhotonJetUp;   //!
   TBranch        *b_Jet_pt_jesFlavorPureGluonUp;   //!
   TBranch        *b_Jet_mass_jesFlavorPureGluonUp;   //!
   TBranch        *b_MET_pt_jesFlavorPureGluonUp;   //!
   TBranch        *b_MET_phi_jesFlavorPureGluonUp;   //!
   TBranch        *b_Jet_pt_jesFlavorPureQuarkUp;   //!
   TBranch        *b_Jet_mass_jesFlavorPureQuarkUp;   //!
   TBranch        *b_MET_pt_jesFlavorPureQuarkUp;   //!
   TBranch        *b_MET_phi_jesFlavorPureQuarkUp;   //!
   TBranch        *b_Jet_pt_jesFlavorPureCharmUp;   //!
   TBranch        *b_Jet_mass_jesFlavorPureCharmUp;   //!
   TBranch        *b_MET_pt_jesFlavorPureCharmUp;   //!
   TBranch        *b_MET_phi_jesFlavorPureCharmUp;   //!
   TBranch        *b_Jet_pt_jesFlavorPureBottomUp;   //!
   TBranch        *b_Jet_mass_jesFlavorPureBottomUp;   //!
   TBranch        *b_MET_pt_jesFlavorPureBottomUp;   //!
   TBranch        *b_MET_phi_jesFlavorPureBottomUp;   //!
   TBranch        *b_Jet_pt_jesTimeRunBCDUp;   //!
   TBranch        *b_Jet_mass_jesTimeRunBCDUp;   //!
   TBranch        *b_MET_pt_jesTimeRunBCDUp;   //!
   TBranch        *b_MET_phi_jesTimeRunBCDUp;   //!
   TBranch        *b_Jet_pt_jesTimeRunEFUp;   //!
   TBranch        *b_Jet_mass_jesTimeRunEFUp;   //!
   TBranch        *b_MET_pt_jesTimeRunEFUp;   //!
   TBranch        *b_MET_phi_jesTimeRunEFUp;   //!
   TBranch        *b_Jet_pt_jesTimeRunGUp;   //!
   TBranch        *b_Jet_mass_jesTimeRunGUp;   //!
   TBranch        *b_MET_pt_jesTimeRunGUp;   //!
   TBranch        *b_MET_phi_jesTimeRunGUp;   //!
   TBranch        *b_Jet_pt_jesTimeRunHUp;   //!
   TBranch        *b_Jet_mass_jesTimeRunHUp;   //!
   TBranch        *b_MET_pt_jesTimeRunHUp;   //!
   TBranch        *b_MET_phi_jesTimeRunHUp;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupMPFInSituUp;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupMPFInSituUp;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupMPFInSituUp;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupMPFInSituUp;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupIntercalibrationUp;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupIntercalibrationUp;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupIntercalibrationUp;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupIntercalibrationUp;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupbJESUp;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupbJESUp;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupbJESUp;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupbJESUp;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupFlavorUp;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupFlavorUp;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupFlavorUp;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupFlavorUp;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupUncorrelatedUp;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupUncorrelatedUp;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupUncorrelatedUp;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupUncorrelatedUp;   //!
   TBranch        *b_MET_pt_unclustEnUp;   //!
   TBranch        *b_MET_phi_unclustEnUp;   //!
   TBranch        *b_Jet_pt_jerDown;   //!
   TBranch        *b_Jet_mass_jerDown;   //!
   TBranch        *b_Jet_mass_jmrDown;   //!
   TBranch        *b_Jet_mass_jmsDown;   //!
   TBranch        *b_MET_pt_jerDown;   //!
   TBranch        *b_MET_phi_jerDown;   //!
   TBranch        *b_Jet_pt_jesAbsoluteStatDown;   //!
   TBranch        *b_Jet_mass_jesAbsoluteStatDown;   //!
   TBranch        *b_MET_pt_jesAbsoluteStatDown;   //!
   TBranch        *b_MET_phi_jesAbsoluteStatDown;   //!
   TBranch        *b_Jet_pt_jesAbsoluteScaleDown;   //!
   TBranch        *b_Jet_mass_jesAbsoluteScaleDown;   //!
   TBranch        *b_MET_pt_jesAbsoluteScaleDown;   //!
   TBranch        *b_MET_phi_jesAbsoluteScaleDown;   //!
   TBranch        *b_Jet_pt_jesAbsoluteFlavMapDown;   //!
   TBranch        *b_Jet_mass_jesAbsoluteFlavMapDown;   //!
   TBranch        *b_MET_pt_jesAbsoluteFlavMapDown;   //!
   TBranch        *b_MET_phi_jesAbsoluteFlavMapDown;   //!
   TBranch        *b_Jet_pt_jesAbsoluteMPFBiasDown;   //!
   TBranch        *b_Jet_mass_jesAbsoluteMPFBiasDown;   //!
   TBranch        *b_MET_pt_jesAbsoluteMPFBiasDown;   //!
   TBranch        *b_MET_phi_jesAbsoluteMPFBiasDown;   //!
   TBranch        *b_Jet_pt_jesFragmentationDown;   //!
   TBranch        *b_Jet_mass_jesFragmentationDown;   //!
   TBranch        *b_MET_pt_jesFragmentationDown;   //!
   TBranch        *b_MET_phi_jesFragmentationDown;   //!
   TBranch        *b_Jet_pt_jesSinglePionECALDown;   //!
   TBranch        *b_Jet_mass_jesSinglePionECALDown;   //!
   TBranch        *b_MET_pt_jesSinglePionECALDown;   //!
   TBranch        *b_MET_phi_jesSinglePionECALDown;   //!
   TBranch        *b_Jet_pt_jesSinglePionHCALDown;   //!
   TBranch        *b_Jet_mass_jesSinglePionHCALDown;   //!
   TBranch        *b_MET_pt_jesSinglePionHCALDown;   //!
   TBranch        *b_MET_phi_jesSinglePionHCALDown;   //!
   TBranch        *b_Jet_pt_jesFlavorQCDDown;   //!
   TBranch        *b_Jet_mass_jesFlavorQCDDown;   //!
   TBranch        *b_MET_pt_jesFlavorQCDDown;   //!
   TBranch        *b_MET_phi_jesFlavorQCDDown;   //!
   TBranch        *b_Jet_pt_jesTimePtEtaDown;   //!
   TBranch        *b_Jet_mass_jesTimePtEtaDown;   //!
   TBranch        *b_MET_pt_jesTimePtEtaDown;   //!
   TBranch        *b_MET_phi_jesTimePtEtaDown;   //!
   TBranch        *b_Jet_pt_jesRelativeJEREC1Down;   //!
   TBranch        *b_Jet_mass_jesRelativeJEREC1Down;   //!
   TBranch        *b_MET_pt_jesRelativeJEREC1Down;   //!
   TBranch        *b_MET_phi_jesRelativeJEREC1Down;   //!
   TBranch        *b_Jet_pt_jesRelativeJEREC2Down;   //!
   TBranch        *b_Jet_mass_jesRelativeJEREC2Down;   //!
   TBranch        *b_MET_pt_jesRelativeJEREC2Down;   //!
   TBranch        *b_MET_phi_jesRelativeJEREC2Down;   //!
   TBranch        *b_Jet_pt_jesRelativeJERHFDown;   //!
   TBranch        *b_Jet_mass_jesRelativeJERHFDown;   //!
   TBranch        *b_MET_pt_jesRelativeJERHFDown;   //!
   TBranch        *b_MET_phi_jesRelativeJERHFDown;   //!
   TBranch        *b_Jet_pt_jesRelativePtBBDown;   //!
   TBranch        *b_Jet_mass_jesRelativePtBBDown;   //!
   TBranch        *b_MET_pt_jesRelativePtBBDown;   //!
   TBranch        *b_MET_phi_jesRelativePtBBDown;   //!
   TBranch        *b_Jet_pt_jesRelativePtEC1Down;   //!
   TBranch        *b_Jet_mass_jesRelativePtEC1Down;   //!
   TBranch        *b_MET_pt_jesRelativePtEC1Down;   //!
   TBranch        *b_MET_phi_jesRelativePtEC1Down;   //!
   TBranch        *b_Jet_pt_jesRelativePtEC2Down;   //!
   TBranch        *b_Jet_mass_jesRelativePtEC2Down;   //!
   TBranch        *b_MET_pt_jesRelativePtEC2Down;   //!
   TBranch        *b_MET_phi_jesRelativePtEC2Down;   //!
   TBranch        *b_Jet_pt_jesRelativePtHFDown;   //!
   TBranch        *b_Jet_mass_jesRelativePtHFDown;   //!
   TBranch        *b_MET_pt_jesRelativePtHFDown;   //!
   TBranch        *b_MET_phi_jesRelativePtHFDown;   //!
   TBranch        *b_Jet_pt_jesRelativeBalDown;   //!
   TBranch        *b_Jet_mass_jesRelativeBalDown;   //!
   TBranch        *b_MET_pt_jesRelativeBalDown;   //!
   TBranch        *b_MET_phi_jesRelativeBalDown;   //!
   TBranch        *b_Jet_pt_jesRelativeFSRDown;   //!
   TBranch        *b_Jet_mass_jesRelativeFSRDown;   //!
   TBranch        *b_MET_pt_jesRelativeFSRDown;   //!
   TBranch        *b_MET_phi_jesRelativeFSRDown;   //!
   TBranch        *b_Jet_pt_jesRelativeStatFSRDown;   //!
   TBranch        *b_Jet_mass_jesRelativeStatFSRDown;   //!
   TBranch        *b_MET_pt_jesRelativeStatFSRDown;   //!
   TBranch        *b_MET_phi_jesRelativeStatFSRDown;   //!
   TBranch        *b_Jet_pt_jesRelativeStatECDown;   //!
   TBranch        *b_Jet_mass_jesRelativeStatECDown;   //!
   TBranch        *b_MET_pt_jesRelativeStatECDown;   //!
   TBranch        *b_MET_phi_jesRelativeStatECDown;   //!
   TBranch        *b_Jet_pt_jesRelativeStatHFDown;   //!
   TBranch        *b_Jet_mass_jesRelativeStatHFDown;   //!
   TBranch        *b_MET_pt_jesRelativeStatHFDown;   //!
   TBranch        *b_MET_phi_jesRelativeStatHFDown;   //!
   TBranch        *b_Jet_pt_jesPileUpDataMCDown;   //!
   TBranch        *b_Jet_mass_jesPileUpDataMCDown;   //!
   TBranch        *b_MET_pt_jesPileUpDataMCDown;   //!
   TBranch        *b_MET_phi_jesPileUpDataMCDown;   //!
   TBranch        *b_Jet_pt_jesPileUpPtRefDown;   //!
   TBranch        *b_Jet_mass_jesPileUpPtRefDown;   //!
   TBranch        *b_MET_pt_jesPileUpPtRefDown;   //!
   TBranch        *b_MET_phi_jesPileUpPtRefDown;   //!
   TBranch        *b_Jet_pt_jesPileUpPtBBDown;   //!
   TBranch        *b_Jet_mass_jesPileUpPtBBDown;   //!
   TBranch        *b_MET_pt_jesPileUpPtBBDown;   //!
   TBranch        *b_MET_phi_jesPileUpPtBBDown;   //!
   TBranch        *b_Jet_pt_jesPileUpPtEC1Down;   //!
   TBranch        *b_Jet_mass_jesPileUpPtEC1Down;   //!
   TBranch        *b_MET_pt_jesPileUpPtEC1Down;   //!
   TBranch        *b_MET_phi_jesPileUpPtEC1Down;   //!
   TBranch        *b_Jet_pt_jesPileUpPtEC2Down;   //!
   TBranch        *b_Jet_mass_jesPileUpPtEC2Down;   //!
   TBranch        *b_MET_pt_jesPileUpPtEC2Down;   //!
   TBranch        *b_MET_phi_jesPileUpPtEC2Down;   //!
   TBranch        *b_Jet_pt_jesPileUpPtHFDown;   //!
   TBranch        *b_Jet_mass_jesPileUpPtHFDown;   //!
   TBranch        *b_MET_pt_jesPileUpPtHFDown;   //!
   TBranch        *b_MET_phi_jesPileUpPtHFDown;   //!
   TBranch        *b_Jet_pt_jesPileUpMuZeroDown;   //!
   TBranch        *b_Jet_mass_jesPileUpMuZeroDown;   //!
   TBranch        *b_MET_pt_jesPileUpMuZeroDown;   //!
   TBranch        *b_MET_phi_jesPileUpMuZeroDown;   //!
   TBranch        *b_Jet_pt_jesPileUpEnvelopeDown;   //!
   TBranch        *b_Jet_mass_jesPileUpEnvelopeDown;   //!
   TBranch        *b_MET_pt_jesPileUpEnvelopeDown;   //!
   TBranch        *b_MET_phi_jesPileUpEnvelopeDown;   //!
   TBranch        *b_Jet_pt_jesSubTotalPileUpDown;   //!
   TBranch        *b_Jet_mass_jesSubTotalPileUpDown;   //!
   TBranch        *b_MET_pt_jesSubTotalPileUpDown;   //!
   TBranch        *b_MET_phi_jesSubTotalPileUpDown;   //!
   TBranch        *b_Jet_pt_jesSubTotalRelativeDown;   //!
   TBranch        *b_Jet_mass_jesSubTotalRelativeDown;   //!
   TBranch        *b_MET_pt_jesSubTotalRelativeDown;   //!
   TBranch        *b_MET_phi_jesSubTotalRelativeDown;   //!
   TBranch        *b_Jet_pt_jesSubTotalPtDown;   //!
   TBranch        *b_Jet_mass_jesSubTotalPtDown;   //!
   TBranch        *b_MET_pt_jesSubTotalPtDown;   //!
   TBranch        *b_MET_phi_jesSubTotalPtDown;   //!
   TBranch        *b_Jet_pt_jesSubTotalScaleDown;   //!
   TBranch        *b_Jet_mass_jesSubTotalScaleDown;   //!
   TBranch        *b_MET_pt_jesSubTotalScaleDown;   //!
   TBranch        *b_MET_phi_jesSubTotalScaleDown;   //!
   TBranch        *b_Jet_pt_jesSubTotalAbsoluteDown;   //!
   TBranch        *b_Jet_mass_jesSubTotalAbsoluteDown;   //!
   TBranch        *b_MET_pt_jesSubTotalAbsoluteDown;   //!
   TBranch        *b_MET_phi_jesSubTotalAbsoluteDown;   //!
   TBranch        *b_Jet_pt_jesSubTotalMCDown;   //!
   TBranch        *b_Jet_mass_jesSubTotalMCDown;   //!
   TBranch        *b_MET_pt_jesSubTotalMCDown;   //!
   TBranch        *b_MET_phi_jesSubTotalMCDown;   //!
   TBranch        *b_Jet_pt_jesTotalDown;   //!
   TBranch        *b_Jet_mass_jesTotalDown;   //!
   TBranch        *b_MET_pt_jesTotalDown;   //!
   TBranch        *b_MET_phi_jesTotalDown;   //!
   TBranch        *b_Jet_pt_jesTotalNoFlavorDown;   //!
   TBranch        *b_Jet_mass_jesTotalNoFlavorDown;   //!
   TBranch        *b_MET_pt_jesTotalNoFlavorDown;   //!
   TBranch        *b_MET_phi_jesTotalNoFlavorDown;   //!
   TBranch        *b_Jet_pt_jesTotalNoTimeDown;   //!
   TBranch        *b_Jet_mass_jesTotalNoTimeDown;   //!
   TBranch        *b_MET_pt_jesTotalNoTimeDown;   //!
   TBranch        *b_MET_phi_jesTotalNoTimeDown;   //!
   TBranch        *b_Jet_pt_jesTotalNoFlavorNoTimeDown;   //!
   TBranch        *b_Jet_mass_jesTotalNoFlavorNoTimeDown;   //!
   TBranch        *b_MET_pt_jesTotalNoFlavorNoTimeDown;   //!
   TBranch        *b_MET_phi_jesTotalNoFlavorNoTimeDown;   //!
   TBranch        *b_Jet_pt_jesFlavorZJetDown;   //!
   TBranch        *b_Jet_mass_jesFlavorZJetDown;   //!
   TBranch        *b_MET_pt_jesFlavorZJetDown;   //!
   TBranch        *b_MET_phi_jesFlavorZJetDown;   //!
   TBranch        *b_Jet_pt_jesFlavorPhotonJetDown;   //!
   TBranch        *b_Jet_mass_jesFlavorPhotonJetDown;   //!
   TBranch        *b_MET_pt_jesFlavorPhotonJetDown;   //!
   TBranch        *b_MET_phi_jesFlavorPhotonJetDown;   //!
   TBranch        *b_Jet_pt_jesFlavorPureGluonDown;   //!
   TBranch        *b_Jet_mass_jesFlavorPureGluonDown;   //!
   TBranch        *b_MET_pt_jesFlavorPureGluonDown;   //!
   TBranch        *b_MET_phi_jesFlavorPureGluonDown;   //!
   TBranch        *b_Jet_pt_jesFlavorPureQuarkDown;   //!
   TBranch        *b_Jet_mass_jesFlavorPureQuarkDown;   //!
   TBranch        *b_MET_pt_jesFlavorPureQuarkDown;   //!
   TBranch        *b_MET_phi_jesFlavorPureQuarkDown;   //!
   TBranch        *b_Jet_pt_jesFlavorPureCharmDown;   //!
   TBranch        *b_Jet_mass_jesFlavorPureCharmDown;   //!
   TBranch        *b_MET_pt_jesFlavorPureCharmDown;   //!
   TBranch        *b_MET_phi_jesFlavorPureCharmDown;   //!
   TBranch        *b_Jet_pt_jesFlavorPureBottomDown;   //!
   TBranch        *b_Jet_mass_jesFlavorPureBottomDown;   //!
   TBranch        *b_MET_pt_jesFlavorPureBottomDown;   //!
   TBranch        *b_MET_phi_jesFlavorPureBottomDown;   //!
   TBranch        *b_Jet_pt_jesTimeRunBCDDown;   //!
   TBranch        *b_Jet_mass_jesTimeRunBCDDown;   //!
   TBranch        *b_MET_pt_jesTimeRunBCDDown;   //!
   TBranch        *b_MET_phi_jesTimeRunBCDDown;   //!
   TBranch        *b_Jet_pt_jesTimeRunEFDown;   //!
   TBranch        *b_Jet_mass_jesTimeRunEFDown;   //!
   TBranch        *b_MET_pt_jesTimeRunEFDown;   //!
   TBranch        *b_MET_phi_jesTimeRunEFDown;   //!
   TBranch        *b_Jet_pt_jesTimeRunGDown;   //!
   TBranch        *b_Jet_mass_jesTimeRunGDown;   //!
   TBranch        *b_MET_pt_jesTimeRunGDown;   //!
   TBranch        *b_MET_phi_jesTimeRunGDown;   //!
   TBranch        *b_Jet_pt_jesTimeRunHDown;   //!
   TBranch        *b_Jet_mass_jesTimeRunHDown;   //!
   TBranch        *b_MET_pt_jesTimeRunHDown;   //!
   TBranch        *b_MET_phi_jesTimeRunHDown;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupMPFInSituDown;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupMPFInSituDown;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupMPFInSituDown;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupMPFInSituDown;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupIntercalibrationDown;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupIntercalibrationDown;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupIntercalibrationDown;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupIntercalibrationDown;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupbJESDown;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupbJESDown;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupbJESDown;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupbJESDown;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupFlavorDown;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupFlavorDown;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupFlavorDown;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupFlavorDown;   //!
   TBranch        *b_Jet_pt_jesCorrelationGroupUncorrelatedDown;   //!
   TBranch        *b_Jet_mass_jesCorrelationGroupUncorrelatedDown;   //!
   TBranch        *b_MET_pt_jesCorrelationGroupUncorrelatedDown;   //!
   TBranch        *b_MET_phi_jesCorrelationGroupUncorrelatedDown;   //!
   TBranch        *b_MET_pt_unclustEnDown;   //!
   TBranch        *b_MET_phi_unclustEnDown;   //!
   TBranch        *b_Muon_pt_corrected;   //!
   TBranch        *b_MHT_pt;   //!
   TBranch        *b_MHT_phi;   //!
   TBranch        *b_Jet_mhtCleaning;   //!
   TBranch        *b_Jet_btagSF;   //!
   TBranch        *b_Jet_btagSF_up;   //!
   TBranch        *b_Jet_btagSF_down;   //!
   TBranch        *b_Jet_btagSF_shape;   //!
   TBranch        *b_Jet_btagSF_shape_up_jes;   //!
   TBranch        *b_Jet_btagSF_shape_down_jes;   //!
   TBranch        *b_Jet_btagSF_shape_up_lf;   //!
   TBranch        *b_Jet_btagSF_shape_down_lf;   //!
   TBranch        *b_Jet_btagSF_shape_up_hf;   //!
   TBranch        *b_Jet_btagSF_shape_down_hf;   //!
   TBranch        *b_Jet_btagSF_shape_up_hfstats1;   //!
   TBranch        *b_Jet_btagSF_shape_down_hfstats1;   //!
   TBranch        *b_Jet_btagSF_shape_up_hfstats2;   //!
   TBranch        *b_Jet_btagSF_shape_down_hfstats2;   //!
   TBranch        *b_Jet_btagSF_shape_up_lfstats1;   //!
   TBranch        *b_Jet_btagSF_shape_down_lfstats1;   //!
   TBranch        *b_Jet_btagSF_shape_up_lfstats2;   //!
   TBranch        *b_Jet_btagSF_shape_down_lfstats2;   //!
   TBranch        *b_Jet_btagSF_shape_up_cferr1;   //!
   TBranch        *b_Jet_btagSF_shape_down_cferr1;   //!
   TBranch        *b_Jet_btagSF_shape_up_cferr2;   //!
   TBranch        *b_Jet_btagSF_shape_down_cferr2;   //!
   TBranch        *b_Vtype;   //!
   TBranch        *b_V_pt;   //!
   TBranch        *b_V_eta;   //!
   TBranch        *b_V_phi;   //!
   TBranch        *b_V_mass;   //!
   TBranch        *b_Jet_lepFilter;   //!
   TBranch        *b_vLidx;   //!
   TBranch        *b_hJidx;   //!
   TBranch        *b_hJidxCMVA;   //!
   TBranch        *b_HCMVA_pt;   //!
   TBranch        *b_HCMVA_eta;   //!
   TBranch        *b_HCMVA_phi;   //!
   TBranch        *b_HCMVA_mass;   //!
   TBranch        *b_HFSR_pt;   //!
   TBranch        *b_HFSR_eta;   //!
   TBranch        *b_HFSR_phi;   //!
   TBranch        *b_HFSR_mass;   //!
   TBranch        *b_SA_Ht;   //!
   TBranch        *b_SA5;   //!
   TBranch        *b_Jet_Pt;   //!
   TBranch        *b_Jet_PtReg;   //!
   TBranch        *b_MET_Pt;   //!
   TBranch        *b_MET_Phi;   //!
   TBranch        *b_Pt_fjidx;   //!
   TBranch        *b_Msd_fjidx;   //!
   TBranch        *b_Hbb_fjidx;   //!
   TBranch        *b_SAptfj_HT;   //!
   TBranch        *b_SAptfj5;   //!
   TBranch        *b_SAmfj_HT;   //!
   TBranch        *b_SAmfj5;   //!
   TBranch        *b_SAhbbfj_HT;   //!
   TBranch        *b_SAhbbfj5;   //!
   TBranch        *b_nVMuonIdx;   //!
   TBranch        *b_nVElectronIdx;   //!
   TBranch        *b_VMuonIdx;   //!
   TBranch        *b_VElectronIdx;   //!
   TBranch        *b_nVetoLeptons;   //!
   TBranch        *b_nAddLeptons;   //!
   TBranch        *b_TTW;   //!
   TBranch        *b_weight_SF_TightID;   //!
   TBranch        *b_weight_SF_TightISO;   //!
   TBranch        *b_weight_SF_TightIDnISO;   //!
   TBranch        *b_weight_SF_TRK;   //!
   TBranch        *b_weight_SF_Lepton;   //!
   TBranch        *b_eTrigSFWeight_singleEle80;   //!
   TBranch        *b_muTrigSFWeight_singlemu;   //!
   TBranch        *b_NLOw;   //!
   TBranch        *b_DYw;   //!
   TBranch        *b_EWKw;   //!
   TBranch        *b_EWKwSIG;   //!
   TBranch        *b_EWKwVJets;   //!
   TBranch        *b_bTagWeightCMVAV2;   //!
   TBranch        *b_bTagWeightCMVAV2_JESUp;   //!
   TBranch        *b_bTagWeightCMVAV2_JESDown;   //!
   TBranch        *b_bTagWeightCMVAV2_LFUp;   //!
   TBranch        *b_bTagWeightCMVAV2_LFDown;   //!
   TBranch        *b_bTagWeightCMVAV2_HFUp;   //!
   TBranch        *b_bTagWeightCMVAV2_HFDown;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_JES_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LF_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HF_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats1_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_LFStats2_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats1_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_HFStats2_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr1_pt4_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt0_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt0_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt0_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt1_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt1_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt1_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt2_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt2_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt2_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt3_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt3_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt3_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt4_eta1Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt4_eta2Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt4_eta3Up;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt0_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt0_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt0_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt1_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt1_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt1_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt2_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt2_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt2_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt3_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt3_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt3_eta3Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt4_eta1Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt4_eta2Down;   //!
   TBranch        *b_bTagWeightCMVAV2_cErr2_pt4_eta3Down;   //!
   TBranch        *b_minDphiJetMet;   //!
   TBranch        *b_nAddJetQCD;   //!
   TBranch        *b_hJets_pt_reg_max;   //!
   TBranch        *b_nAddJet30;   //!
   TBranch        *b_hJets_pt_reg_min;   //!
   TBranch        *b_dPhiMetTkMet;   //!
   TBranch        *b_dPhiVH;   //!
   TBranch        *b_hJets_pt_reg_1;   //!
   TBranch        *b_hJets_pt_reg_0;   //!
   TBranch        *b_H_pt;   //!
   TBranch        *b_H_pt_jer_Up;   //!
   TBranch        *b_H_pt_jer_Down;   //!
   TBranch        *b_H_pt_jesAbsoluteStat_Up;   //!
   TBranch        *b_H_pt_jesAbsoluteStat_Down;   //!
   TBranch        *b_H_pt_jesAbsoluteScale_Up;   //!
   TBranch        *b_H_pt_jesAbsoluteScale_Down;   //!
   TBranch        *b_H_pt_jesAbsoluteFlavMap_Up;   //!
   TBranch        *b_H_pt_jesAbsoluteFlavMap_Down;   //!
   TBranch        *b_H_pt_jesAbsoluteMPFBias_Up;   //!
   TBranch        *b_H_pt_jesAbsoluteMPFBias_Down;   //!
   TBranch        *b_H_pt_jesFragmentation_Up;   //!
   TBranch        *b_H_pt_jesFragmentation_Down;   //!
   TBranch        *b_H_pt_jesSinglePionECAL_Up;   //!
   TBranch        *b_H_pt_jesSinglePionECAL_Down;   //!
   TBranch        *b_H_pt_jesSinglePionHCAL_Up;   //!
   TBranch        *b_H_pt_jesSinglePionHCAL_Down;   //!
   TBranch        *b_H_pt_jesFlavorQCD_Up;   //!
   TBranch        *b_H_pt_jesFlavorQCD_Down;   //!
   TBranch        *b_H_pt_jesRelativeJEREC1_Up;   //!
   TBranch        *b_H_pt_jesRelativeJEREC1_Down;   //!
   TBranch        *b_H_pt_jesRelativeJEREC2_Up;   //!
   TBranch        *b_H_pt_jesRelativeJEREC2_Down;   //!
   TBranch        *b_H_pt_jesRelativeJERHF_Up;   //!
   TBranch        *b_H_pt_jesRelativeJERHF_Down;   //!
   TBranch        *b_H_pt_jesRelativePtBB_Up;   //!
   TBranch        *b_H_pt_jesRelativePtBB_Down;   //!
   TBranch        *b_H_pt_jesRelativePtEC1_Up;   //!
   TBranch        *b_H_pt_jesRelativePtEC1_Down;   //!
   TBranch        *b_H_pt_jesRelativePtEC2_Up;   //!
   TBranch        *b_H_pt_jesRelativePtEC2_Down;   //!
   TBranch        *b_H_pt_jesRelativePtHF_Up;   //!
   TBranch        *b_H_pt_jesRelativePtHF_Down;   //!
   TBranch        *b_H_pt_jesRelativeBal_Up;   //!
   TBranch        *b_H_pt_jesRelativeBal_Down;   //!
   TBranch        *b_H_pt_jesRelativeFSR_Up;   //!
   TBranch        *b_H_pt_jesRelativeFSR_Down;   //!
   TBranch        *b_H_pt_jesRelativeStatFSR_Up;   //!
   TBranch        *b_H_pt_jesRelativeStatFSR_Down;   //!
   TBranch        *b_H_pt_jesRelativeStatEC_Up;   //!
   TBranch        *b_H_pt_jesRelativeStatEC_Down;   //!
   TBranch        *b_H_pt_jesRelativeStatHF_Up;   //!
   TBranch        *b_H_pt_jesRelativeStatHF_Down;   //!
   TBranch        *b_H_pt_jesPileUpDataMC_Up;   //!
   TBranch        *b_H_pt_jesPileUpDataMC_Down;   //!
   TBranch        *b_H_pt_jesPileUpPtRef_Up;   //!
   TBranch        *b_H_pt_jesPileUpPtRef_Down;   //!
   TBranch        *b_H_pt_jesPileUpPtBB_Up;   //!
   TBranch        *b_H_pt_jesPileUpPtBB_Down;   //!
   TBranch        *b_H_pt_jesPileUpPtEC1_Up;   //!
   TBranch        *b_H_pt_jesPileUpPtEC1_Down;   //!
   TBranch        *b_H_pt_jesPileUpPtEC2_Up;   //!
   TBranch        *b_H_pt_jesPileUpPtEC2_Down;   //!
   TBranch        *b_H_pt_jesPileUpPtHF_Up;   //!
   TBranch        *b_H_pt_jesPileUpPtHF_Down;   //!
   TBranch        *b_H_pt_jesPileUpMuZero_Up;   //!
   TBranch        *b_H_pt_jesPileUpMuZero_Down;   //!
   TBranch        *b_H_pt_jesPileUpEnvelope_Up;   //!
   TBranch        *b_H_pt_jesPileUpEnvelope_Down;   //!
   TBranch        *b_H_pt_jesTotal_Up;   //!
   TBranch        *b_H_pt_jesTotal_Down;   //!
   TBranch        *b_H_pt_minmax_Up;   //!
   TBranch        *b_H_pt_minmax_Down;   //!
   TBranch        *b_H_eta;   //!
   TBranch        *b_H_eta_jer_Up;   //!
   TBranch        *b_H_eta_jer_Down;   //!
   TBranch        *b_H_eta_jesAbsoluteStat_Up;   //!
   TBranch        *b_H_eta_jesAbsoluteStat_Down;   //!
   TBranch        *b_H_eta_jesAbsoluteScale_Up;   //!
   TBranch        *b_H_eta_jesAbsoluteScale_Down;   //!
   TBranch        *b_H_eta_jesAbsoluteFlavMap_Up;   //!
   TBranch        *b_H_eta_jesAbsoluteFlavMap_Down;   //!
   TBranch        *b_H_eta_jesAbsoluteMPFBias_Up;   //!
   TBranch        *b_H_eta_jesAbsoluteMPFBias_Down;   //!
   TBranch        *b_H_eta_jesFragmentation_Up;   //!
   TBranch        *b_H_eta_jesFragmentation_Down;   //!
   TBranch        *b_H_eta_jesSinglePionECAL_Up;   //!
   TBranch        *b_H_eta_jesSinglePionECAL_Down;   //!
   TBranch        *b_H_eta_jesSinglePionHCAL_Up;   //!
   TBranch        *b_H_eta_jesSinglePionHCAL_Down;   //!
   TBranch        *b_H_eta_jesFlavorQCD_Up;   //!
   TBranch        *b_H_eta_jesFlavorQCD_Down;   //!
   TBranch        *b_H_eta_jesRelativeJEREC1_Up;   //!
   TBranch        *b_H_eta_jesRelativeJEREC1_Down;   //!
   TBranch        *b_H_eta_jesRelativeJEREC2_Up;   //!
   TBranch        *b_H_eta_jesRelativeJEREC2_Down;   //!
   TBranch        *b_H_eta_jesRelativeJERHF_Up;   //!
   TBranch        *b_H_eta_jesRelativeJERHF_Down;   //!
   TBranch        *b_H_eta_jesRelativePtBB_Up;   //!
   TBranch        *b_H_eta_jesRelativePtBB_Down;   //!
   TBranch        *b_H_eta_jesRelativePtEC1_Up;   //!
   TBranch        *b_H_eta_jesRelativePtEC1_Down;   //!
   TBranch        *b_H_eta_jesRelativePtEC2_Up;   //!
   TBranch        *b_H_eta_jesRelativePtEC2_Down;   //!
   TBranch        *b_H_eta_jesRelativePtHF_Up;   //!
   TBranch        *b_H_eta_jesRelativePtHF_Down;   //!
   TBranch        *b_H_eta_jesRelativeBal_Up;   //!
   TBranch        *b_H_eta_jesRelativeBal_Down;   //!
   TBranch        *b_H_eta_jesRelativeFSR_Up;   //!
   TBranch        *b_H_eta_jesRelativeFSR_Down;   //!
   TBranch        *b_H_eta_jesRelativeStatFSR_Up;   //!
   TBranch        *b_H_eta_jesRelativeStatFSR_Down;   //!
   TBranch        *b_H_eta_jesRelativeStatEC_Up;   //!
   TBranch        *b_H_eta_jesRelativeStatEC_Down;   //!
   TBranch        *b_H_eta_jesRelativeStatHF_Up;   //!
   TBranch        *b_H_eta_jesRelativeStatHF_Down;   //!
   TBranch        *b_H_eta_jesPileUpDataMC_Up;   //!
   TBranch        *b_H_eta_jesPileUpDataMC_Down;   //!
   TBranch        *b_H_eta_jesPileUpPtRef_Up;   //!
   TBranch        *b_H_eta_jesPileUpPtRef_Down;   //!
   TBranch        *b_H_eta_jesPileUpPtBB_Up;   //!
   TBranch        *b_H_eta_jesPileUpPtBB_Down;   //!
   TBranch        *b_H_eta_jesPileUpPtEC1_Up;   //!
   TBranch        *b_H_eta_jesPileUpPtEC1_Down;   //!
   TBranch        *b_H_eta_jesPileUpPtEC2_Up;   //!
   TBranch        *b_H_eta_jesPileUpPtEC2_Down;   //!
   TBranch        *b_H_eta_jesPileUpPtHF_Up;   //!
   TBranch        *b_H_eta_jesPileUpPtHF_Down;   //!
   TBranch        *b_H_eta_jesPileUpMuZero_Up;   //!
   TBranch        *b_H_eta_jesPileUpMuZero_Down;   //!
   TBranch        *b_H_eta_jesPileUpEnvelope_Up;   //!
   TBranch        *b_H_eta_jesPileUpEnvelope_Down;   //!
   TBranch        *b_H_eta_jesTotal_Up;   //!
   TBranch        *b_H_eta_jesTotal_Down;   //!
   TBranch        *b_H_eta_minmax_Up;   //!
   TBranch        *b_H_eta_minmax_Down;   //!
   TBranch        *b_H_phi;   //!
   TBranch        *b_H_phi_jer_Up;   //!
   TBranch        *b_H_phi_jer_Down;   //!
   TBranch        *b_H_phi_jesAbsoluteStat_Up;   //!
   TBranch        *b_H_phi_jesAbsoluteStat_Down;   //!
   TBranch        *b_H_phi_jesAbsoluteScale_Up;   //!
   TBranch        *b_H_phi_jesAbsoluteScale_Down;   //!
   TBranch        *b_H_phi_jesAbsoluteFlavMap_Up;   //!
   TBranch        *b_H_phi_jesAbsoluteFlavMap_Down;   //!
   TBranch        *b_H_phi_jesAbsoluteMPFBias_Up;   //!
   TBranch        *b_H_phi_jesAbsoluteMPFBias_Down;   //!
   TBranch        *b_H_phi_jesFragmentation_Up;   //!
   TBranch        *b_H_phi_jesFragmentation_Down;   //!
   TBranch        *b_H_phi_jesSinglePionECAL_Up;   //!
   TBranch        *b_H_phi_jesSinglePionECAL_Down;   //!
   TBranch        *b_H_phi_jesSinglePionHCAL_Up;   //!
   TBranch        *b_H_phi_jesSinglePionHCAL_Down;   //!
   TBranch        *b_H_phi_jesFlavorQCD_Up;   //!
   TBranch        *b_H_phi_jesFlavorQCD_Down;   //!
   TBranch        *b_H_phi_jesRelativeJEREC1_Up;   //!
   TBranch        *b_H_phi_jesRelativeJEREC1_Down;   //!
   TBranch        *b_H_phi_jesRelativeJEREC2_Up;   //!
   TBranch        *b_H_phi_jesRelativeJEREC2_Down;   //!
   TBranch        *b_H_phi_jesRelativeJERHF_Up;   //!
   TBranch        *b_H_phi_jesRelativeJERHF_Down;   //!
   TBranch        *b_H_phi_jesRelativePtBB_Up;   //!
   TBranch        *b_H_phi_jesRelativePtBB_Down;   //!
   TBranch        *b_H_phi_jesRelativePtEC1_Up;   //!
   TBranch        *b_H_phi_jesRelativePtEC1_Down;   //!
   TBranch        *b_H_phi_jesRelativePtEC2_Up;   //!
   TBranch        *b_H_phi_jesRelativePtEC2_Down;   //!
   TBranch        *b_H_phi_jesRelativePtHF_Up;   //!
   TBranch        *b_H_phi_jesRelativePtHF_Down;   //!
   TBranch        *b_H_phi_jesRelativeBal_Up;   //!
   TBranch        *b_H_phi_jesRelativeBal_Down;   //!
   TBranch        *b_H_phi_jesRelativeFSR_Up;   //!
   TBranch        *b_H_phi_jesRelativeFSR_Down;   //!
   TBranch        *b_H_phi_jesRelativeStatFSR_Up;   //!
   TBranch        *b_H_phi_jesRelativeStatFSR_Down;   //!
   TBranch        *b_H_phi_jesRelativeStatEC_Up;   //!
   TBranch        *b_H_phi_jesRelativeStatEC_Down;   //!
   TBranch        *b_H_phi_jesRelativeStatHF_Up;   //!
   TBranch        *b_H_phi_jesRelativeStatHF_Down;   //!
   TBranch        *b_H_phi_jesPileUpDataMC_Up;   //!
   TBranch        *b_H_phi_jesPileUpDataMC_Down;   //!
   TBranch        *b_H_phi_jesPileUpPtRef_Up;   //!
   TBranch        *b_H_phi_jesPileUpPtRef_Down;   //!
   TBranch        *b_H_phi_jesPileUpPtBB_Up;   //!
   TBranch        *b_H_phi_jesPileUpPtBB_Down;   //!
   TBranch        *b_H_phi_jesPileUpPtEC1_Up;   //!
   TBranch        *b_H_phi_jesPileUpPtEC1_Down;   //!
   TBranch        *b_H_phi_jesPileUpPtEC2_Up;   //!
   TBranch        *b_H_phi_jesPileUpPtEC2_Down;   //!
   TBranch        *b_H_phi_jesPileUpPtHF_Up;   //!
   TBranch        *b_H_phi_jesPileUpPtHF_Down;   //!
   TBranch        *b_H_phi_jesPileUpMuZero_Up;   //!
   TBranch        *b_H_phi_jesPileUpMuZero_Down;   //!
   TBranch        *b_H_phi_jesPileUpEnvelope_Up;   //!
   TBranch        *b_H_phi_jesPileUpEnvelope_Down;   //!
   TBranch        *b_H_phi_jesTotal_Up;   //!
   TBranch        *b_H_phi_jesTotal_Down;   //!
   TBranch        *b_H_phi_minmax_Up;   //!
   TBranch        *b_H_phi_minmax_Down;   //!
   TBranch        *b_H_mass;   //!
   TBranch        *b_H_mass_jer_Up;   //!
   TBranch        *b_H_mass_jer_Down;   //!
   TBranch        *b_H_mass_jesAbsoluteStat_Up;   //!
   TBranch        *b_H_mass_jesAbsoluteStat_Down;   //!
   TBranch        *b_H_mass_jesAbsoluteScale_Up;   //!
   TBranch        *b_H_mass_jesAbsoluteScale_Down;   //!
   TBranch        *b_H_mass_jesAbsoluteFlavMap_Up;   //!
   TBranch        *b_H_mass_jesAbsoluteFlavMap_Down;   //!
   TBranch        *b_H_mass_jesAbsoluteMPFBias_Up;   //!
   TBranch        *b_H_mass_jesAbsoluteMPFBias_Down;   //!
   TBranch        *b_H_mass_jesFragmentation_Up;   //!
   TBranch        *b_H_mass_jesFragmentation_Down;   //!
   TBranch        *b_H_mass_jesSinglePionECAL_Up;   //!
   TBranch        *b_H_mass_jesSinglePionECAL_Down;   //!
   TBranch        *b_H_mass_jesSinglePionHCAL_Up;   //!
   TBranch        *b_H_mass_jesSinglePionHCAL_Down;   //!
   TBranch        *b_H_mass_jesFlavorQCD_Up;   //!
   TBranch        *b_H_mass_jesFlavorQCD_Down;   //!
   TBranch        *b_H_mass_jesRelativeJEREC1_Up;   //!
   TBranch        *b_H_mass_jesRelativeJEREC1_Down;   //!
   TBranch        *b_H_mass_jesRelativeJEREC2_Up;   //!
   TBranch        *b_H_mass_jesRelativeJEREC2_Down;   //!
   TBranch        *b_H_mass_jesRelativeJERHF_Up;   //!
   TBranch        *b_H_mass_jesRelativeJERHF_Down;   //!
   TBranch        *b_H_mass_jesRelativePtBB_Up;   //!
   TBranch        *b_H_mass_jesRelativePtBB_Down;   //!
   TBranch        *b_H_mass_jesRelativePtEC1_Up;   //!
   TBranch        *b_H_mass_jesRelativePtEC1_Down;   //!
   TBranch        *b_H_mass_jesRelativePtEC2_Up;   //!
   TBranch        *b_H_mass_jesRelativePtEC2_Down;   //!
   TBranch        *b_H_mass_jesRelativePtHF_Up;   //!
   TBranch        *b_H_mass_jesRelativePtHF_Down;   //!
   TBranch        *b_H_mass_jesRelativeBal_Up;   //!
   TBranch        *b_H_mass_jesRelativeBal_Down;   //!
   TBranch        *b_H_mass_jesRelativeFSR_Up;   //!
   TBranch        *b_H_mass_jesRelativeFSR_Down;   //!
   TBranch        *b_H_mass_jesRelativeStatFSR_Up;   //!
   TBranch        *b_H_mass_jesRelativeStatFSR_Down;   //!
   TBranch        *b_H_mass_jesRelativeStatEC_Up;   //!
   TBranch        *b_H_mass_jesRelativeStatEC_Down;   //!
   TBranch        *b_H_mass_jesRelativeStatHF_Up;   //!
   TBranch        *b_H_mass_jesRelativeStatHF_Down;   //!
   TBranch        *b_H_mass_jesPileUpDataMC_Up;   //!
   TBranch        *b_H_mass_jesPileUpDataMC_Down;   //!
   TBranch        *b_H_mass_jesPileUpPtRef_Up;   //!
   TBranch        *b_H_mass_jesPileUpPtRef_Down;   //!
   TBranch        *b_H_mass_jesPileUpPtBB_Up;   //!
   TBranch        *b_H_mass_jesPileUpPtBB_Down;   //!
   TBranch        *b_H_mass_jesPileUpPtEC1_Up;   //!
   TBranch        *b_H_mass_jesPileUpPtEC1_Down;   //!
   TBranch        *b_H_mass_jesPileUpPtEC2_Up;   //!
   TBranch        *b_H_mass_jesPileUpPtEC2_Down;   //!
   TBranch        *b_H_mass_jesPileUpPtHF_Up;   //!
   TBranch        *b_H_mass_jesPileUpPtHF_Down;   //!
   TBranch        *b_H_mass_jesPileUpMuZero_Up;   //!
   TBranch        *b_H_mass_jesPileUpMuZero_Down;   //!
   TBranch        *b_H_mass_jesPileUpEnvelope_Up;   //!
   TBranch        *b_H_mass_jesPileUpEnvelope_Down;   //!
   TBranch        *b_H_mass_jesTotal_Up;   //!
   TBranch        *b_H_mass_jesTotal_Down;   //!
   TBranch        *b_H_mass_minmax_Up;   //!
   TBranch        *b_H_mass_minmax_Down;   //!
   TBranch        *b_Jet_pt_minmaxUp;   //!
   TBranch        *b_Jet_pt_minmaxDown;   //!
   TBranch        *b_Jet_mass_minmaxUp;   //!
   TBranch        *b_Jet_mass_minmaxDown;   //!
   TBranch        *b_isSignal;   //!
   TBranch        *b_isWH;   //!
   TBranch        *b_isData;   //!
   TBranch        *b_nGenVbosons;   //!
   TBranch        *b_GenVbosons_pt;   //!
   TBranch        *b_GenVbosons_pdgId;   //!
   TBranch        *b_GenVbosons_GenPartIdx;   //!
   TBranch        *b_nGenTop;   //!
   TBranch        *b_GenTop_pt;   //!
   TBranch        *b_GenTop_GenPartIdx;   //!
   TBranch        *b_nGenHiggsBoson;   //!
   TBranch        *b_GenHiggsBoson_pt;   //!
   TBranch        *b_GenHiggsBoson_GenPartIdx;   //!
   TBranch        *b_VtypeSim;   //!
   TBranch        *b_FitCorr;   //!
   TBranch        *b_top_mass;   //!
   TBranch        *b_V_mt;   //!

   myclass(TTree *tree=0);
   virtual ~myclass();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef myclass_cxx
myclass::myclass(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("root://t3dcachedb03.psi.ch//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/VHbbPostNano2016/Wlv/sys_v2/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/tree_arizzi-RunIIMoriond17-DeepAndR148_180517_170415_0000_7_c65a9993f5ddd46b3c2a8e157ec02743f21cb1f963092c580b77243b.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("root://t3dcachedb03.psi.ch//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/VHbbPostNano2016/Wlv/sys_v2/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/tree_arizzi-RunIIMoriond17-DeepAndR148_180517_170415_0000_7_c65a9993f5ddd46b3c2a8e157ec02743f21cb1f963092c580b77243b.root");
      }
      f->GetObject("Events",tree);

   }
   Init(tree);
}

myclass::~myclass()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t myclass::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t myclass::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void myclass::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("luminosityBlock", &luminosityBlock, &b_luminosityBlock);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("btagWeight_CSVV2", &btagWeight_CSVV2, &b_btagWeight_CSVV2);
   fChain->SetBranchAddress("btagWeight_CMVA", &btagWeight_CMVA, &b_btagWeight_CMVA);
   fChain->SetBranchAddress("CaloMET_phi", &CaloMET_phi, &b_CaloMET_phi);
   fChain->SetBranchAddress("CaloMET_pt", &CaloMET_pt, &b_CaloMET_pt);
   fChain->SetBranchAddress("CaloMET_sumEt", &CaloMET_sumEt, &b_CaloMET_sumEt);
   fChain->SetBranchAddress("nElectron", &nElectron, &b_nElectron);
   fChain->SetBranchAddress("Electron_deltaEtaSC", Electron_deltaEtaSC, &b_Electron_deltaEtaSC);
   fChain->SetBranchAddress("Electron_dr03EcalRecHitSumEt", Electron_dr03EcalRecHitSumEt, &b_Electron_dr03EcalRecHitSumEt);
   fChain->SetBranchAddress("Electron_dr03HcalDepth1TowerSumEt", Electron_dr03HcalDepth1TowerSumEt, &b_Electron_dr03HcalDepth1TowerSumEt);
   fChain->SetBranchAddress("Electron_dr03TkSumPt", Electron_dr03TkSumPt, &b_Electron_dr03TkSumPt);
   fChain->SetBranchAddress("Electron_dxy", Electron_dxy, &b_Electron_dxy);
   fChain->SetBranchAddress("Electron_dxyErr", Electron_dxyErr, &b_Electron_dxyErr);
   fChain->SetBranchAddress("Electron_dz", Electron_dz, &b_Electron_dz);
   fChain->SetBranchAddress("Electron_dzErr", Electron_dzErr, &b_Electron_dzErr);
   fChain->SetBranchAddress("Electron_eCorr", Electron_eCorr, &b_Electron_eCorr);
   fChain->SetBranchAddress("Electron_eInvMinusPInv", Electron_eInvMinusPInv, &b_Electron_eInvMinusPInv);
   fChain->SetBranchAddress("Electron_energyErr", Electron_energyErr, &b_Electron_energyErr);
   fChain->SetBranchAddress("Electron_eta", Electron_eta, &b_Electron_eta);
   fChain->SetBranchAddress("Electron_hoe", Electron_hoe, &b_Electron_hoe);
   fChain->SetBranchAddress("Electron_ip3d", Electron_ip3d, &b_Electron_ip3d);
   fChain->SetBranchAddress("Electron_mass", Electron_mass, &b_Electron_mass);
   fChain->SetBranchAddress("Electron_miniPFRelIso_all", Electron_miniPFRelIso_all, &b_Electron_miniPFRelIso_all);
   fChain->SetBranchAddress("Electron_miniPFRelIso_chg", Electron_miniPFRelIso_chg, &b_Electron_miniPFRelIso_chg);
   fChain->SetBranchAddress("Electron_mvaSpring16GP", Electron_mvaSpring16GP, &b_Electron_mvaSpring16GP);
   fChain->SetBranchAddress("Electron_mvaSpring16HZZ", Electron_mvaSpring16HZZ, &b_Electron_mvaSpring16HZZ);
   fChain->SetBranchAddress("Electron_pfRelIso03_all", Electron_pfRelIso03_all, &b_Electron_pfRelIso03_all);
   fChain->SetBranchAddress("Electron_pfRelIso03_chg", Electron_pfRelIso03_chg, &b_Electron_pfRelIso03_chg);
   fChain->SetBranchAddress("Electron_phi", Electron_phi, &b_Electron_phi);
   fChain->SetBranchAddress("Electron_pt", Electron_pt, &b_Electron_pt);
   fChain->SetBranchAddress("Electron_r9", Electron_r9, &b_Electron_r9);
   fChain->SetBranchAddress("Electron_sieie", Electron_sieie, &b_Electron_sieie);
   fChain->SetBranchAddress("Electron_sip3d", Electron_sip3d, &b_Electron_sip3d);
   fChain->SetBranchAddress("Electron_mvaTTH", Electron_mvaTTH, &b_Electron_mvaTTH);
   fChain->SetBranchAddress("Electron_charge", Electron_charge, &b_Electron_charge);
   fChain->SetBranchAddress("Electron_cutBased", Electron_cutBased, &b_Electron_cutBased);
   fChain->SetBranchAddress("Electron_cutBased_HLTPreSel", Electron_cutBased_HLTPreSel, &b_Electron_cutBased_HLTPreSel);
   fChain->SetBranchAddress("Electron_jetIdx", Electron_jetIdx, &b_Electron_jetIdx);
   fChain->SetBranchAddress("Electron_pdgId", Electron_pdgId, &b_Electron_pdgId);
   fChain->SetBranchAddress("Electron_photonIdx", Electron_photonIdx, &b_Electron_photonIdx);
   fChain->SetBranchAddress("Electron_tightCharge", Electron_tightCharge, &b_Electron_tightCharge);
   fChain->SetBranchAddress("Electron_vidNestedWPBitmap", Electron_vidNestedWPBitmap, &b_Electron_vidNestedWPBitmap);
   fChain->SetBranchAddress("Electron_convVeto", Electron_convVeto, &b_Electron_convVeto);
   fChain->SetBranchAddress("Electron_cutBased_HEEP", Electron_cutBased_HEEP, &b_Electron_cutBased_HEEP);
   fChain->SetBranchAddress("Electron_isPFcand", Electron_isPFcand, &b_Electron_isPFcand);
   fChain->SetBranchAddress("Electron_lostHits", Electron_lostHits, &b_Electron_lostHits);
   fChain->SetBranchAddress("Electron_mvaSpring16GP_WP80", Electron_mvaSpring16GP_WP80, &b_Electron_mvaSpring16GP_WP80);
   fChain->SetBranchAddress("Electron_mvaSpring16GP_WP90", Electron_mvaSpring16GP_WP90, &b_Electron_mvaSpring16GP_WP90);
   fChain->SetBranchAddress("Electron_mvaSpring16HZZ_WPL", Electron_mvaSpring16HZZ_WPL, &b_Electron_mvaSpring16HZZ_WPL);
   fChain->SetBranchAddress("Flag_BadChargedCandidateFilter", &Flag_BadChargedCandidateFilter, &b_Flag_BadChargedCandidateFilter);
   fChain->SetBranchAddress("Flag_BadGlobalMuon", &Flag_BadGlobalMuon, &b_Flag_BadGlobalMuon);
   fChain->SetBranchAddress("Flag_BadPFMuonFilter", &Flag_BadPFMuonFilter, &b_Flag_BadPFMuonFilter);
   fChain->SetBranchAddress("Flag_CloneGlobalMuon", &Flag_CloneGlobalMuon, &b_Flag_CloneGlobalMuon);
   fChain->SetBranchAddress("nGenJetAK8", &nGenJetAK8, &b_nGenJetAK8);
   fChain->SetBranchAddress("GenJetAK8_eta", GenJetAK8_eta, &b_GenJetAK8_eta);
   fChain->SetBranchAddress("GenJetAK8_mass", GenJetAK8_mass, &b_GenJetAK8_mass);
   fChain->SetBranchAddress("GenJetAK8_phi", GenJetAK8_phi, &b_GenJetAK8_phi);
   fChain->SetBranchAddress("GenJetAK8_pt", GenJetAK8_pt, &b_GenJetAK8_pt);
   fChain->SetBranchAddress("nGenJet", &nGenJet, &b_nGenJet);
   fChain->SetBranchAddress("GenJet_eta", GenJet_eta, &b_GenJet_eta);
   fChain->SetBranchAddress("GenJet_mass", GenJet_mass, &b_GenJet_mass);
   fChain->SetBranchAddress("GenJet_phi", GenJet_phi, &b_GenJet_phi);
   fChain->SetBranchAddress("GenJet_pt", GenJet_pt, &b_GenJet_pt);
   fChain->SetBranchAddress("nGenPart", &nGenPart, &b_nGenPart);
   fChain->SetBranchAddress("GenPart_eta", GenPart_eta, &b_GenPart_eta);
   fChain->SetBranchAddress("GenPart_mass", GenPart_mass, &b_GenPart_mass);
   fChain->SetBranchAddress("GenPart_phi", GenPart_phi, &b_GenPart_phi);
   fChain->SetBranchAddress("GenPart_pt", GenPart_pt, &b_GenPart_pt);
   fChain->SetBranchAddress("GenPart_genPartIdxMother", GenPart_genPartIdxMother, &b_GenPart_genPartIdxMother);
   fChain->SetBranchAddress("GenPart_pdgId", GenPart_pdgId, &b_GenPart_pdgId);
   fChain->SetBranchAddress("GenPart_status", GenPart_status, &b_GenPart_status);
   fChain->SetBranchAddress("GenPart_statusFlags", GenPart_statusFlags, &b_GenPart_statusFlags);
   fChain->SetBranchAddress("Generator_binvar", &Generator_binvar, &b_Generator_binvar);
   fChain->SetBranchAddress("Generator_scalePDF", &Generator_scalePDF, &b_Generator_scalePDF);
   fChain->SetBranchAddress("Generator_weight", &Generator_weight, &b_Generator_weight);
   fChain->SetBranchAddress("Generator_x1", &Generator_x1, &b_Generator_x1);
   fChain->SetBranchAddress("Generator_x2", &Generator_x2, &b_Generator_x2);
   fChain->SetBranchAddress("Generator_xpdf1", &Generator_xpdf1, &b_Generator_xpdf1);
   fChain->SetBranchAddress("Generator_xpdf2", &Generator_xpdf2, &b_Generator_xpdf2);
   fChain->SetBranchAddress("Generator_id1", &Generator_id1, &b_Generator_id1);
   fChain->SetBranchAddress("Generator_id2", &Generator_id2, &b_Generator_id2);
   fChain->SetBranchAddress("genWeight", &genWeight, &b_genWeight);
   fChain->SetBranchAddress("LHEWeight_originalXWGTUP", &LHEWeight_originalXWGTUP, &b_LHEWeight_originalXWGTUP);
   fChain->SetBranchAddress("nLHEPdfWeight", &nLHEPdfWeight, &b_nLHEPdfWeight);
   fChain->SetBranchAddress("LHEPdfWeight", LHEPdfWeight, &b_LHEPdfWeight);
   fChain->SetBranchAddress("nLHEScaleWeight", &nLHEScaleWeight, &b_nLHEScaleWeight);
   fChain->SetBranchAddress("LHEScaleWeight", LHEScaleWeight, &b_LHEScaleWeight);
   fChain->SetBranchAddress("nJet", &nJet, &b_nJet);
   fChain->SetBranchAddress("Jet_area", Jet_area, &b_Jet_area);
   fChain->SetBranchAddress("Jet_btagCMVA", Jet_btagCMVA, &b_Jet_btagCMVA);
   fChain->SetBranchAddress("Jet_btagCSVV2", Jet_btagCSVV2, &b_Jet_btagCSVV2);
   fChain->SetBranchAddress("Jet_btagDeepB", Jet_btagDeepB, &b_Jet_btagDeepB);
   fChain->SetBranchAddress("Jet_btagDeepC", Jet_btagDeepC, &b_Jet_btagDeepC);
   fChain->SetBranchAddress("Jet_btagDeepFlavB", Jet_btagDeepFlavB, &b_Jet_btagDeepFlavB);
   fChain->SetBranchAddress("Jet_chEmEF", Jet_chEmEF, &b_Jet_chEmEF);
   fChain->SetBranchAddress("Jet_chHEF", Jet_chHEF, &b_Jet_chHEF);
   fChain->SetBranchAddress("Jet_eta", Jet_eta, &b_Jet_eta);
   fChain->SetBranchAddress("Jet_mass", Jet_mass, &b_Jet_mass);
   fChain->SetBranchAddress("Jet_neEmEF", Jet_neEmEF, &b_Jet_neEmEF);
   fChain->SetBranchAddress("Jet_neHEF", Jet_neHEF, &b_Jet_neHEF);
   fChain->SetBranchAddress("Jet_phi", Jet_phi, &b_Jet_phi);
   fChain->SetBranchAddress("Jet_pt", Jet_pt, &b_Jet_pt);
   fChain->SetBranchAddress("Jet_qgl", Jet_qgl, &b_Jet_qgl);
   fChain->SetBranchAddress("Jet_rawFactor", Jet_rawFactor, &b_Jet_rawFactor);
   fChain->SetBranchAddress("Jet_bReg", Jet_bReg, &b_Jet_bReg);
   fChain->SetBranchAddress("Jet_bRegOld", Jet_bRegOld, &b_Jet_bRegOld);
   fChain->SetBranchAddress("Jet_bRegRes", Jet_bRegRes, &b_Jet_bRegRes);
   fChain->SetBranchAddress("Jet_electronIdx1", Jet_electronIdx1, &b_Jet_electronIdx1);
   fChain->SetBranchAddress("Jet_electronIdx2", Jet_electronIdx2, &b_Jet_electronIdx2);
   fChain->SetBranchAddress("Jet_jetId", Jet_jetId, &b_Jet_jetId);
   fChain->SetBranchAddress("Jet_muonIdx1", Jet_muonIdx1, &b_Jet_muonIdx1);
   fChain->SetBranchAddress("Jet_muonIdx2", Jet_muonIdx2, &b_Jet_muonIdx2);
   fChain->SetBranchAddress("Jet_nConstituents", Jet_nConstituents, &b_Jet_nConstituents);
   fChain->SetBranchAddress("Jet_nElectrons", Jet_nElectrons, &b_Jet_nElectrons);
   fChain->SetBranchAddress("Jet_nMuons", Jet_nMuons, &b_Jet_nMuons);
   fChain->SetBranchAddress("Jet_puId", Jet_puId, &b_Jet_puId);
   fChain->SetBranchAddress("LHE_HT", &LHE_HT, &b_LHE_HT);
   fChain->SetBranchAddress("LHE_HTIncoming", &LHE_HTIncoming, &b_LHE_HTIncoming);
   fChain->SetBranchAddress("LHE_Vpt", &LHE_Vpt, &b_LHE_Vpt);
   fChain->SetBranchAddress("LHE_Njets", &LHE_Njets, &b_LHE_Njets);
   fChain->SetBranchAddress("LHE_Nb", &LHE_Nb, &b_LHE_Nb);
   fChain->SetBranchAddress("LHE_Nc", &LHE_Nc, &b_LHE_Nc);
   fChain->SetBranchAddress("LHE_Nuds", &LHE_Nuds, &b_LHE_Nuds);
   fChain->SetBranchAddress("LHE_Nglu", &LHE_Nglu, &b_LHE_Nglu);
   fChain->SetBranchAddress("LHE_NpNLO", &LHE_NpNLO, &b_LHE_NpNLO);
   fChain->SetBranchAddress("LHE_NpLO", &LHE_NpLO, &b_LHE_NpLO);
   fChain->SetBranchAddress("nLHEPart", &nLHEPart, &b_nLHEPart);
   fChain->SetBranchAddress("LHEPart_pt", LHEPart_pt, &b_LHEPart_pt);
   fChain->SetBranchAddress("LHEPart_eta", LHEPart_eta, &b_LHEPart_eta);
   fChain->SetBranchAddress("LHEPart_phi", LHEPart_phi, &b_LHEPart_phi);
   fChain->SetBranchAddress("LHEPart_mass", LHEPart_mass, &b_LHEPart_mass);
   fChain->SetBranchAddress("LHEPart_pdgId", LHEPart_pdgId, &b_LHEPart_pdgId);
   fChain->SetBranchAddress("GenMET_phi", &GenMET_phi, &b_GenMET_phi);
   fChain->SetBranchAddress("GenMET_pt", &GenMET_pt, &b_GenMET_pt);
   fChain->SetBranchAddress("MET_MetUnclustEnUpDeltaX", &MET_MetUnclustEnUpDeltaX, &b_MET_MetUnclustEnUpDeltaX);
   fChain->SetBranchAddress("MET_MetUnclustEnUpDeltaY", &MET_MetUnclustEnUpDeltaY, &b_MET_MetUnclustEnUpDeltaY);
   fChain->SetBranchAddress("MET_covXX", &MET_covXX, &b_MET_covXX);
   fChain->SetBranchAddress("MET_covXY", &MET_covXY, &b_MET_covXY);
   fChain->SetBranchAddress("MET_covYY", &MET_covYY, &b_MET_covYY);
   fChain->SetBranchAddress("MET_phi", &MET_phi, &b_MET_phi);
   fChain->SetBranchAddress("MET_pt", &MET_pt, &b_MET_pt);
   fChain->SetBranchAddress("MET_significance", &MET_significance, &b_MET_significance);
   fChain->SetBranchAddress("MET_sumEt", &MET_sumEt, &b_MET_sumEt);
   fChain->SetBranchAddress("nMuon", &nMuon, &b_nMuon);
   fChain->SetBranchAddress("Muon_dxy", Muon_dxy, &b_Muon_dxy);
   fChain->SetBranchAddress("Muon_dxyErr", Muon_dxyErr, &b_Muon_dxyErr);
   fChain->SetBranchAddress("Muon_dz", Muon_dz, &b_Muon_dz);
   fChain->SetBranchAddress("Muon_dzErr", Muon_dzErr, &b_Muon_dzErr);
   fChain->SetBranchAddress("Muon_eta", Muon_eta, &b_Muon_eta);
   fChain->SetBranchAddress("Muon_ip3d", Muon_ip3d, &b_Muon_ip3d);
   fChain->SetBranchAddress("Muon_mass", Muon_mass, &b_Muon_mass);
   fChain->SetBranchAddress("Muon_miniPFRelIso_all", Muon_miniPFRelIso_all, &b_Muon_miniPFRelIso_all);
   fChain->SetBranchAddress("Muon_miniPFRelIso_chg", Muon_miniPFRelIso_chg, &b_Muon_miniPFRelIso_chg);
   fChain->SetBranchAddress("Muon_pfRelIso03_all", Muon_pfRelIso03_all, &b_Muon_pfRelIso03_all);
   fChain->SetBranchAddress("Muon_pfRelIso03_chg", Muon_pfRelIso03_chg, &b_Muon_pfRelIso03_chg);
   fChain->SetBranchAddress("Muon_pfRelIso04_all", Muon_pfRelIso04_all, &b_Muon_pfRelIso04_all);
   fChain->SetBranchAddress("Muon_phi", Muon_phi, &b_Muon_phi);
   fChain->SetBranchAddress("Muon_pt", Muon_pt, &b_Muon_pt);
   fChain->SetBranchAddress("Muon_ptErr", Muon_ptErr, &b_Muon_ptErr);
   fChain->SetBranchAddress("Muon_segmentComp", Muon_segmentComp, &b_Muon_segmentComp);
   fChain->SetBranchAddress("Muon_sip3d", Muon_sip3d, &b_Muon_sip3d);
   fChain->SetBranchAddress("Muon_mvaTTH", Muon_mvaTTH, &b_Muon_mvaTTH);
   fChain->SetBranchAddress("Muon_charge", Muon_charge, &b_Muon_charge);
   fChain->SetBranchAddress("Muon_jetIdx", Muon_jetIdx, &b_Muon_jetIdx);
   fChain->SetBranchAddress("Muon_nStations", Muon_nStations, &b_Muon_nStations);
   fChain->SetBranchAddress("Muon_nTrackerLayers", Muon_nTrackerLayers, &b_Muon_nTrackerLayers);
   fChain->SetBranchAddress("Muon_pdgId", Muon_pdgId, &b_Muon_pdgId);
   fChain->SetBranchAddress("Muon_tightCharge", Muon_tightCharge, &b_Muon_tightCharge);
   fChain->SetBranchAddress("Muon_highPtId", Muon_highPtId, &b_Muon_highPtId);
   fChain->SetBranchAddress("Muon_isPFcand", Muon_isPFcand, &b_Muon_isPFcand);
   fChain->SetBranchAddress("Muon_mediumId", Muon_mediumId, &b_Muon_mediumId);
   fChain->SetBranchAddress("Muon_softId", Muon_softId, &b_Muon_softId);
   fChain->SetBranchAddress("Muon_tightId", Muon_tightId, &b_Muon_tightId);
   fChain->SetBranchAddress("Pileup_nTrueInt", &Pileup_nTrueInt, &b_Pileup_nTrueInt);
   fChain->SetBranchAddress("Pileup_nPU", &Pileup_nPU, &b_Pileup_nPU);
   fChain->SetBranchAddress("Pileup_sumEOOT", &Pileup_sumEOOT, &b_Pileup_sumEOOT);
   fChain->SetBranchAddress("Pileup_sumLOOT", &Pileup_sumLOOT, &b_Pileup_sumLOOT);
   fChain->SetBranchAddress("PuppiMET_phi", &PuppiMET_phi, &b_PuppiMET_phi);
   fChain->SetBranchAddress("PuppiMET_pt", &PuppiMET_pt, &b_PuppiMET_pt);
   fChain->SetBranchAddress("PuppiMET_sumEt", &PuppiMET_sumEt, &b_PuppiMET_sumEt);
   fChain->SetBranchAddress("RawMET_phi", &RawMET_phi, &b_RawMET_phi);
   fChain->SetBranchAddress("RawMET_pt", &RawMET_pt, &b_RawMET_pt);
   fChain->SetBranchAddress("RawMET_sumEt", &RawMET_sumEt, &b_RawMET_sumEt);
   fChain->SetBranchAddress("fixedGridRhoFastjetAll", &fixedGridRhoFastjetAll, &b_fixedGridRhoFastjetAll);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralCalo", &fixedGridRhoFastjetCentralCalo, &b_fixedGridRhoFastjetCentralCalo);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralNeutral", &fixedGridRhoFastjetCentralNeutral, &b_fixedGridRhoFastjetCentralNeutral);
   fChain->SetBranchAddress("nGenDressedLepton", &nGenDressedLepton, &b_nGenDressedLepton);
   fChain->SetBranchAddress("GenDressedLepton_eta", GenDressedLepton_eta, &b_GenDressedLepton_eta);
   fChain->SetBranchAddress("GenDressedLepton_mass", GenDressedLepton_mass, &b_GenDressedLepton_mass);
   fChain->SetBranchAddress("GenDressedLepton_phi", GenDressedLepton_phi, &b_GenDressedLepton_phi);
   fChain->SetBranchAddress("GenDressedLepton_pt", GenDressedLepton_pt, &b_GenDressedLepton_pt);
   fChain->SetBranchAddress("GenDressedLepton_pdgId", GenDressedLepton_pdgId, &b_GenDressedLepton_pdgId);
   fChain->SetBranchAddress("nSoftActivityJet", &nSoftActivityJet, &b_nSoftActivityJet);
   fChain->SetBranchAddress("SoftActivityJet_eta", SoftActivityJet_eta, &b_SoftActivityJet_eta);
   fChain->SetBranchAddress("SoftActivityJet_phi", SoftActivityJet_phi, &b_SoftActivityJet_phi);
   fChain->SetBranchAddress("SoftActivityJet_pt", SoftActivityJet_pt, &b_SoftActivityJet_pt);
   fChain->SetBranchAddress("SoftActivityJetHT", &SoftActivityJetHT, &b_SoftActivityJetHT);
   fChain->SetBranchAddress("SoftActivityJetHT10", &SoftActivityJetHT10, &b_SoftActivityJetHT10);
   fChain->SetBranchAddress("SoftActivityJetHT2", &SoftActivityJetHT2, &b_SoftActivityJetHT2);
   fChain->SetBranchAddress("SoftActivityJetHT5", &SoftActivityJetHT5, &b_SoftActivityJetHT5);
   fChain->SetBranchAddress("SoftActivityJetNjets10", &SoftActivityJetNjets10, &b_SoftActivityJetNjets10);
   fChain->SetBranchAddress("SoftActivityJetNjets2", &SoftActivityJetNjets2, &b_SoftActivityJetNjets2);
   fChain->SetBranchAddress("SoftActivityJetNjets5", &SoftActivityJetNjets5, &b_SoftActivityJetNjets5);
   fChain->SetBranchAddress("TkMET_phi", &TkMET_phi, &b_TkMET_phi);
   fChain->SetBranchAddress("TkMET_pt", &TkMET_pt, &b_TkMET_pt);
   fChain->SetBranchAddress("TkMET_sumEt", &TkMET_sumEt, &b_TkMET_sumEt);
   fChain->SetBranchAddress("genTtbarId", &genTtbarId, &b_genTtbarId);
   fChain->SetBranchAddress("nOtherPV", &nOtherPV, &b_nOtherPV);
   fChain->SetBranchAddress("OtherPV_z", OtherPV_z, &b_OtherPV_z);
   fChain->SetBranchAddress("PV_ndof", &PV_ndof, &b_PV_ndof);
   fChain->SetBranchAddress("PV_x", &PV_x, &b_PV_x);
   fChain->SetBranchAddress("PV_y", &PV_y, &b_PV_y);
   fChain->SetBranchAddress("PV_z", &PV_z, &b_PV_z);
   fChain->SetBranchAddress("PV_chi2", &PV_chi2, &b_PV_chi2);
   fChain->SetBranchAddress("PV_score", &PV_score, &b_PV_score);
   fChain->SetBranchAddress("PV_npvs", &PV_npvs, &b_PV_npvs);
   fChain->SetBranchAddress("PV_npvsGood", &PV_npvsGood, &b_PV_npvsGood);
   fChain->SetBranchAddress("nSV", &nSV, &b_nSV);
   fChain->SetBranchAddress("SV_dlen", SV_dlen, &b_SV_dlen);
   fChain->SetBranchAddress("SV_dlenSig", SV_dlenSig, &b_SV_dlenSig);
   fChain->SetBranchAddress("SV_pAngle", SV_pAngle, &b_SV_pAngle);
   fChain->SetBranchAddress("Electron_genPartIdx", Electron_genPartIdx, &b_Electron_genPartIdx);
   fChain->SetBranchAddress("Electron_genPartFlav", Electron_genPartFlav, &b_Electron_genPartFlav);
   fChain->SetBranchAddress("GenJetAK8_partonFlavour", GenJetAK8_partonFlavour, &b_GenJetAK8_partonFlavour);
   fChain->SetBranchAddress("GenJetAK8_hadronFlavour", GenJetAK8_hadronFlavour, &b_GenJetAK8_hadronFlavour);
   fChain->SetBranchAddress("GenJet_partonFlavour", GenJet_partonFlavour, &b_GenJet_partonFlavour);
   fChain->SetBranchAddress("GenJet_hadronFlavour", GenJet_hadronFlavour, &b_GenJet_hadronFlavour);
   fChain->SetBranchAddress("Jet_genJetIdx", Jet_genJetIdx, &b_Jet_genJetIdx);
   fChain->SetBranchAddress("Jet_hadronFlavour", Jet_hadronFlavour, &b_Jet_hadronFlavour);
   fChain->SetBranchAddress("Jet_partonFlavour", Jet_partonFlavour, &b_Jet_partonFlavour);
   fChain->SetBranchAddress("Muon_genPartIdx", Muon_genPartIdx, &b_Muon_genPartIdx);
   fChain->SetBranchAddress("Muon_genPartFlav", Muon_genPartFlav, &b_Muon_genPartFlav);
   fChain->SetBranchAddress("MET_fiducialGenPhi", &MET_fiducialGenPhi, &b_MET_fiducialGenPhi);
   fChain->SetBranchAddress("MET_fiducialGenPt", &MET_fiducialGenPt, &b_MET_fiducialGenPt);
   fChain->SetBranchAddress("Electron_cleanmask", Electron_cleanmask, &b_Electron_cleanmask);
   fChain->SetBranchAddress("Jet_cleanmask", Jet_cleanmask, &b_Jet_cleanmask);
   fChain->SetBranchAddress("Muon_cleanmask", Muon_cleanmask, &b_Muon_cleanmask);
   fChain->SetBranchAddress("SV_chi2", SV_chi2, &b_SV_chi2);
   fChain->SetBranchAddress("SV_eta", SV_eta, &b_SV_eta);
   fChain->SetBranchAddress("SV_mass", SV_mass, &b_SV_mass);
   fChain->SetBranchAddress("SV_ndof", SV_ndof, &b_SV_ndof);
   fChain->SetBranchAddress("SV_phi", SV_phi, &b_SV_phi);
   fChain->SetBranchAddress("SV_pt", SV_pt, &b_SV_pt);
   fChain->SetBranchAddress("SV_x", SV_x, &b_SV_x);
   fChain->SetBranchAddress("SV_y", SV_y, &b_SV_y);
   fChain->SetBranchAddress("SV_z", SV_z, &b_SV_z);
   fChain->SetBranchAddress("L1simulation_step", &L1simulation_step, &b_L1simulation_step);
   fChain->SetBranchAddress("HLTriggerFirstPath", &HLTriggerFirstPath, &b_HLTriggerFirstPath);
   fChain->SetBranchAddress("HLT_Mu7p5_L2Mu2_Jpsi", &HLT_Mu7p5_L2Mu2_Jpsi, &b_HLT_Mu7p5_L2Mu2_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_L2Mu2_Upsilon", &HLT_Mu7p5_L2Mu2_Upsilon, &b_HLT_Mu7p5_L2Mu2_Upsilon);
   fChain->SetBranchAddress("HLT_Mu7p5_Track2_Jpsi", &HLT_Mu7p5_Track2_Jpsi, &b_HLT_Mu7p5_Track2_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_Track3p5_Jpsi", &HLT_Mu7p5_Track3p5_Jpsi, &b_HLT_Mu7p5_Track3p5_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_Track7_Jpsi", &HLT_Mu7p5_Track7_Jpsi, &b_HLT_Mu7p5_Track7_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_Track2_Upsilon", &HLT_Mu7p5_Track2_Upsilon, &b_HLT_Mu7p5_Track2_Upsilon);
   fChain->SetBranchAddress("HLT_Mu7p5_Track3p5_Upsilon", &HLT_Mu7p5_Track3p5_Upsilon, &b_HLT_Mu7p5_Track3p5_Upsilon);
   fChain->SetBranchAddress("HLT_Mu7p5_Track7_Upsilon", &HLT_Mu7p5_Track7_Upsilon, &b_HLT_Mu7p5_Track7_Upsilon);
   fChain->SetBranchAddress("HLT_Ele17_Ele8_Gsf", &HLT_Ele17_Ele8_Gsf, &b_HLT_Ele17_Ele8_Gsf);
   fChain->SetBranchAddress("HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28", &HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28, &b_HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28);
   fChain->SetBranchAddress("HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29", &HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29, &b_HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29);
   fChain->SetBranchAddress("HLT_Ele22_eta2p1_WPLoose_Gsf", &HLT_Ele22_eta2p1_WPLoose_Gsf, &b_HLT_Ele22_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1", &HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1, &b_HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_Ele23_WPLoose_Gsf", &HLT_Ele23_WPLoose_Gsf, &b_HLT_Ele23_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele23_WPLoose_Gsf_WHbbBoost", &HLT_Ele23_WPLoose_Gsf_WHbbBoost, &b_HLT_Ele23_WPLoose_Gsf_WHbbBoost);
   fChain->SetBranchAddress("HLT_Ele24_eta2p1_WPLoose_Gsf", &HLT_Ele24_eta2p1_WPLoose_Gsf, &b_HLT_Ele24_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20", &HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20, &b_HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20);
   fChain->SetBranchAddress("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1", &HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1, &b_HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30", &HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30, &b_HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30);
   fChain->SetBranchAddress("HLT_Ele25_WPTight_Gsf", &HLT_Ele25_WPTight_Gsf, &b_HLT_Ele25_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele25_eta2p1_WPLoose_Gsf", &HLT_Ele25_eta2p1_WPLoose_Gsf, &b_HLT_Ele25_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele25_eta2p1_WPTight_Gsf", &HLT_Ele25_eta2p1_WPTight_Gsf, &b_HLT_Ele25_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele27_WPLoose_Gsf", &HLT_Ele27_WPLoose_Gsf, &b_HLT_Ele27_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele27_WPLoose_Gsf_WHbbBoost", &HLT_Ele27_WPLoose_Gsf_WHbbBoost, &b_HLT_Ele27_WPLoose_Gsf_WHbbBoost);
   fChain->SetBranchAddress("HLT_Ele27_WPTight_Gsf", &HLT_Ele27_WPTight_Gsf, &b_HLT_Ele27_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele27_WPTight_Gsf_L1JetTauSeeded", &HLT_Ele27_WPTight_Gsf_L1JetTauSeeded, &b_HLT_Ele27_WPTight_Gsf_L1JetTauSeeded);
   fChain->SetBranchAddress("HLT_Ele27_eta2p1_WPLoose_Gsf", &HLT_Ele27_eta2p1_WPLoose_Gsf, &b_HLT_Ele27_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1", &HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1, &b_HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_Ele27_eta2p1_WPTight_Gsf", &HLT_Ele27_eta2p1_WPTight_Gsf, &b_HLT_Ele27_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele30_WPTight_Gsf", &HLT_Ele30_WPTight_Gsf, &b_HLT_Ele30_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele30_eta2p1_WPLoose_Gsf", &HLT_Ele30_eta2p1_WPLoose_Gsf, &b_HLT_Ele30_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele30_eta2p1_WPTight_Gsf", &HLT_Ele30_eta2p1_WPTight_Gsf, &b_HLT_Ele30_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele32_WPTight_Gsf", &HLT_Ele32_WPTight_Gsf, &b_HLT_Ele32_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele32_eta2p1_WPLoose_Gsf", &HLT_Ele32_eta2p1_WPLoose_Gsf, &b_HLT_Ele32_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1", &HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1, &b_HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_Ele32_eta2p1_WPTight_Gsf", &HLT_Ele32_eta2p1_WPTight_Gsf, &b_HLT_Ele32_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele35_WPLoose_Gsf", &HLT_Ele35_WPLoose_Gsf, &b_HLT_Ele35_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50", &HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50, &b_HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50);
   fChain->SetBranchAddress("HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1", &HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1, &b_HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_Ele45_WPLoose_Gsf", &HLT_Ele45_WPLoose_Gsf, &b_HLT_Ele45_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded", &HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded, &b_HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded);
   fChain->SetBranchAddress("HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50", &HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50, &b_HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50);
   fChain->SetBranchAddress("HLT_Ele105_CaloIdVT_GsfTrkIdT", &HLT_Ele105_CaloIdVT_GsfTrkIdT, &b_HLT_Ele105_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_Ele30WP60_SC4_Mass55", &HLT_Ele30WP60_SC4_Mass55, &b_HLT_Ele30WP60_SC4_Mass55);
   fChain->SetBranchAddress("HLT_Ele30WP60_Ele8_Mass55", &HLT_Ele30WP60_Ele8_Mass55, &b_HLT_Ele30WP60_Ele8_Mass55);
   fChain->SetBranchAddress("HLT_Mu16_eta2p1_MET30", &HLT_Mu16_eta2p1_MET30, &b_HLT_Mu16_eta2p1_MET30);
   fChain->SetBranchAddress("HLT_IsoMu16_eta2p1_MET30", &HLT_IsoMu16_eta2p1_MET30, &b_HLT_IsoMu16_eta2p1_MET30);
   fChain->SetBranchAddress("HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1", &HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1, &b_HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu17_eta2p1", &HLT_IsoMu17_eta2p1, &b_HLT_IsoMu17_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu17_eta2p1_LooseIsoPFTau20", &HLT_IsoMu17_eta2p1_LooseIsoPFTau20, &b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20);
   fChain->SetBranchAddress("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1", &HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1, &b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_IsoMu18", &HLT_IsoMu18, &b_HLT_IsoMu18);
   fChain->SetBranchAddress("HLT_IsoMu19_eta2p1_LooseIsoPFTau20", &HLT_IsoMu19_eta2p1_LooseIsoPFTau20, &b_HLT_IsoMu19_eta2p1_LooseIsoPFTau20);
   fChain->SetBranchAddress("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1", &HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1, &b_HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg", &HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg, &b_HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20", &HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20, &b_HLT_IsoMu19_eta2p1_LooseCombinedIsoPFTau20);
   fChain->SetBranchAddress("HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg", &HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg, &b_HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg", &HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg, &b_HLT_IsoMu19_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg", &HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg, &b_HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg", &HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg, &b_HLT_IsoMu21_eta2p1_TightCombinedIsoPFTau32_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_IsoMu20", &HLT_IsoMu20, &b_HLT_IsoMu20);
   fChain->SetBranchAddress("HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1", &HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1, &b_HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1", &HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1, &b_HLT_IsoMu21_eta2p1_LooseIsoPFTau50_Trk30_eta2p1_SingleL1);
   fChain->SetBranchAddress("HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg", &HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg, &b_HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_IsoMu22", &HLT_IsoMu22, &b_HLT_IsoMu22);
   fChain->SetBranchAddress("HLT_IsoMu22_eta2p1", &HLT_IsoMu22_eta2p1, &b_HLT_IsoMu22_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu24", &HLT_IsoMu24, &b_HLT_IsoMu24);
   fChain->SetBranchAddress("HLT_IsoMu27", &HLT_IsoMu27, &b_HLT_IsoMu27);
   fChain->SetBranchAddress("HLT_IsoTkMu18", &HLT_IsoTkMu18, &b_HLT_IsoTkMu18);
   fChain->SetBranchAddress("HLT_IsoTkMu20", &HLT_IsoTkMu20, &b_HLT_IsoTkMu20);
   fChain->SetBranchAddress("HLT_IsoTkMu22", &HLT_IsoTkMu22, &b_HLT_IsoTkMu22);
   fChain->SetBranchAddress("HLT_IsoTkMu22_eta2p1", &HLT_IsoTkMu22_eta2p1, &b_HLT_IsoTkMu22_eta2p1);
   fChain->SetBranchAddress("HLT_IsoTkMu24", &HLT_IsoTkMu24, &b_HLT_IsoTkMu24);
   fChain->SetBranchAddress("HLT_IsoTkMu27", &HLT_IsoTkMu27, &b_HLT_IsoTkMu27);
   fChain->SetBranchAddress("HLT_JetE30_NoBPTX3BX", &HLT_JetE30_NoBPTX3BX, &b_HLT_JetE30_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_JetE30_NoBPTX", &HLT_JetE30_NoBPTX, &b_HLT_JetE30_NoBPTX);
   fChain->SetBranchAddress("HLT_JetE50_NoBPTX3BX", &HLT_JetE50_NoBPTX3BX, &b_HLT_JetE50_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_JetE70_NoBPTX3BX", &HLT_JetE70_NoBPTX3BX, &b_HLT_JetE70_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L2Mu10", &HLT_L2Mu10, &b_HLT_L2Mu10);
   fChain->SetBranchAddress("HLT_L2DoubleMu23_NoVertex", &HLT_L2DoubleMu23_NoVertex, &b_HLT_L2DoubleMu23_NoVertex);
   fChain->SetBranchAddress("HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10", &HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10, &b_HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10);
   fChain->SetBranchAddress("HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10", &HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10, &b_HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10);
   fChain->SetBranchAddress("HLT_L2Mu10_NoVertex_NoBPTX3BX", &HLT_L2Mu10_NoVertex_NoBPTX3BX, &b_HLT_L2Mu10_NoVertex_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L2Mu10_NoVertex_NoBPTX", &HLT_L2Mu10_NoVertex_NoBPTX, &b_HLT_L2Mu10_NoVertex_NoBPTX);
   fChain->SetBranchAddress("HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX", &HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX, &b_HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX", &HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX, &b_HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_LooseIsoPFTau50_Trk30_eta2p1", &HLT_LooseIsoPFTau50_Trk30_eta2p1, &b_HLT_LooseIsoPFTau50_Trk30_eta2p1);
   fChain->SetBranchAddress("HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80", &HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80, &b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80);
   fChain->SetBranchAddress("HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90", &HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90, &b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90);
   fChain->SetBranchAddress("HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110", &HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110, &b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110);
   fChain->SetBranchAddress("HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120", &HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120, &b_HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120);
   fChain->SetBranchAddress("HLT_VLooseIsoPFTau120_Trk50_eta2p1", &HLT_VLooseIsoPFTau120_Trk50_eta2p1, &b_HLT_VLooseIsoPFTau120_Trk50_eta2p1);
   fChain->SetBranchAddress("HLT_VLooseIsoPFTau140_Trk50_eta2p1", &HLT_VLooseIsoPFTau140_Trk50_eta2p1, &b_HLT_VLooseIsoPFTau140_Trk50_eta2p1);
   fChain->SetBranchAddress("HLT_Mu17_Mu8", &HLT_Mu17_Mu8, &b_HLT_Mu17_Mu8);
   fChain->SetBranchAddress("HLT_Mu17_Mu8_DZ", &HLT_Mu17_Mu8_DZ, &b_HLT_Mu17_Mu8_DZ);
   fChain->SetBranchAddress("HLT_Mu17_Mu8_SameSign", &HLT_Mu17_Mu8_SameSign, &b_HLT_Mu17_Mu8_SameSign);
   fChain->SetBranchAddress("HLT_Mu17_Mu8_SameSign_DZ", &HLT_Mu17_Mu8_SameSign_DZ, &b_HLT_Mu17_Mu8_SameSign_DZ);
   fChain->SetBranchAddress("HLT_Mu20_Mu10", &HLT_Mu20_Mu10, &b_HLT_Mu20_Mu10);
   fChain->SetBranchAddress("HLT_Mu20_Mu10_DZ", &HLT_Mu20_Mu10_DZ, &b_HLT_Mu20_Mu10_DZ);
   fChain->SetBranchAddress("HLT_Mu20_Mu10_SameSign", &HLT_Mu20_Mu10_SameSign, &b_HLT_Mu20_Mu10_SameSign);
   fChain->SetBranchAddress("HLT_Mu20_Mu10_SameSign_DZ", &HLT_Mu20_Mu10_SameSign_DZ, &b_HLT_Mu20_Mu10_SameSign_DZ);
   fChain->SetBranchAddress("HLT_Mu17_TkMu8_DZ", &HLT_Mu17_TkMu8_DZ, &b_HLT_Mu17_TkMu8_DZ);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", &HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL, &b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", &HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ, &b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL", &HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL, &b_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ", &HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ, &b_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ);
   fChain->SetBranchAddress("HLT_Mu25_TkMu0_dEta18_Onia", &HLT_Mu25_TkMu0_dEta18_Onia, &b_HLT_Mu25_TkMu0_dEta18_Onia);
   fChain->SetBranchAddress("HLT_Mu27_TkMu8", &HLT_Mu27_TkMu8, &b_HLT_Mu27_TkMu8);
   fChain->SetBranchAddress("HLT_Mu30_TkMu11", &HLT_Mu30_TkMu11, &b_HLT_Mu30_TkMu11);
   fChain->SetBranchAddress("HLT_Mu30_eta2p1_PFJet150_PFJet50", &HLT_Mu30_eta2p1_PFJet150_PFJet50, &b_HLT_Mu30_eta2p1_PFJet150_PFJet50);
   fChain->SetBranchAddress("HLT_Mu40_TkMu11", &HLT_Mu40_TkMu11, &b_HLT_Mu40_TkMu11);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_PFJet200_PFJet50", &HLT_Mu40_eta2p1_PFJet200_PFJet50, &b_HLT_Mu40_eta2p1_PFJet200_PFJet50);
   fChain->SetBranchAddress("HLT_Mu20", &HLT_Mu20, &b_HLT_Mu20);
   fChain->SetBranchAddress("HLT_TkMu17", &HLT_TkMu17, &b_HLT_TkMu17);
   fChain->SetBranchAddress("HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL", &HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL, &b_HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ", &HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ, &b_HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ);
   fChain->SetBranchAddress("HLT_TkMu20", &HLT_TkMu20, &b_HLT_TkMu20);
   fChain->SetBranchAddress("HLT_Mu24_eta2p1", &HLT_Mu24_eta2p1, &b_HLT_Mu24_eta2p1);
   fChain->SetBranchAddress("HLT_TkMu24_eta2p1", &HLT_TkMu24_eta2p1, &b_HLT_TkMu24_eta2p1);
   fChain->SetBranchAddress("HLT_Mu27", &HLT_Mu27, &b_HLT_Mu27);
   fChain->SetBranchAddress("HLT_TkMu27", &HLT_TkMu27, &b_HLT_TkMu27);
   fChain->SetBranchAddress("HLT_Mu45_eta2p1", &HLT_Mu45_eta2p1, &b_HLT_Mu45_eta2p1);
   fChain->SetBranchAddress("HLT_Mu50", &HLT_Mu50, &b_HLT_Mu50);
   fChain->SetBranchAddress("HLT_TkMu50", &HLT_TkMu50, &b_HLT_TkMu50);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL", &HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL, &b_HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL", &HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL, &b_HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL", &HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL, &b_HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL", &HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL, &b_HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL", &HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL, &b_HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight", &HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight, &b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight);
   fChain->SetBranchAddress("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose", &HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose, &b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose);
   fChain->SetBranchAddress("HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose", &HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose, &b_HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight", &HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight, &b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose", &HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose, &b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose", &HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose, &b_HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose);
   fChain->SetBranchAddress("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40", &HLT_Mu28NoFiltersNoVtx_CentralCaloJet40, &b_HLT_Mu28NoFiltersNoVtx_CentralCaloJet40);
   fChain->SetBranchAddress("HLT_SingleCentralPFJet170_CFMax0p1", &HLT_SingleCentralPFJet170_CFMax0p1, &b_HLT_SingleCentralPFJet170_CFMax0p1);
   fChain->SetBranchAddress("HLT_MET60_IsoTrk35_Loose", &HLT_MET60_IsoTrk35_Loose, &b_HLT_MET60_IsoTrk35_Loose);
   fChain->SetBranchAddress("HLT_MET75_IsoTrk50", &HLT_MET75_IsoTrk50, &b_HLT_MET75_IsoTrk50);
   fChain->SetBranchAddress("HLT_MET90_IsoTrk50", &HLT_MET90_IsoTrk50, &b_HLT_MET90_IsoTrk50);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL", &HLT_Mu8_TrkIsoVVL, &b_HLT_Mu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL", &HLT_Mu17_TrkIsoVVL, &b_HLT_Mu17_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded", &HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded, &b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_L1JetTauSeeded);
   fChain->SetBranchAddress("HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL", &HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL, &b_HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL", &HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", &HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", &HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL", &HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL, &b_HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL", &HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL, &b_HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL", &HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL, &b_HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL", &HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL, &b_HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_Mu8_DiEle12_CaloIdL_TrackIdL", &HLT_Mu8_DiEle12_CaloIdL_TrackIdL, &b_HLT_Mu8_DiEle12_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_Mu12_Photon25_CaloIdL", &HLT_Mu12_Photon25_CaloIdL, &b_HLT_Mu12_Photon25_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu12_Photon25_CaloIdL_L1ISO", &HLT_Mu12_Photon25_CaloIdL_L1ISO, &b_HLT_Mu12_Photon25_CaloIdL_L1ISO);
   fChain->SetBranchAddress("HLT_Mu12_Photon25_CaloIdL_L1OR", &HLT_Mu12_Photon25_CaloIdL_L1OR, &b_HLT_Mu12_Photon25_CaloIdL_L1OR);
   fChain->SetBranchAddress("HLT_Mu17_Photon22_CaloIdL_L1ISO", &HLT_Mu17_Photon22_CaloIdL_L1ISO, &b_HLT_Mu17_Photon22_CaloIdL_L1ISO);
   fChain->SetBranchAddress("HLT_Mu17_Photon30_CaloIdL_L1ISO", &HLT_Mu17_Photon30_CaloIdL_L1ISO, &b_HLT_Mu17_Photon30_CaloIdL_L1ISO);
   fChain->SetBranchAddress("HLT_Mu17_Photon35_CaloIdL_L1ISO", &HLT_Mu17_Photon35_CaloIdL_L1ISO, &b_HLT_Mu17_Photon35_CaloIdL_L1ISO);
   fChain->SetBranchAddress("HLT_Mu3er_PFHT140_PFMET125", &HLT_Mu3er_PFHT140_PFMET125, &b_HLT_Mu3er_PFHT140_PFMET125);
   fChain->SetBranchAddress("HLT_Mu6_PFHT200_PFMET80_BTagCSV_p067", &HLT_Mu6_PFHT200_PFMET80_BTagCSV_p067, &b_HLT_Mu6_PFHT200_PFMET80_BTagCSV_p067);
   fChain->SetBranchAddress("HLT_Mu6_PFHT200_PFMET100", &HLT_Mu6_PFHT200_PFMET100, &b_HLT_Mu6_PFHT200_PFMET100);
   fChain->SetBranchAddress("HLT_Mu14er_PFMET100", &HLT_Mu14er_PFMET100, &b_HLT_Mu14er_PFMET100);
   fChain->SetBranchAddress("HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Ele17_CaloIdL_GsfTrkIdVL", &HLT_Ele17_CaloIdL_GsfTrkIdVL, &b_HLT_Ele17_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_Ele17_CaloIdL_TrackIdL_IsoVL", &HLT_Ele17_CaloIdL_TrackIdL_IsoVL, &b_HLT_Ele17_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Ele23_CaloIdL_TrackIdL_IsoVL", &HLT_Ele23_CaloIdL_TrackIdL_IsoVL, &b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Ele27_eta2p1_WPLoose_Gsf_HT200", &HLT_Ele27_eta2p1_WPLoose_Gsf_HT200, &b_HLT_Ele27_eta2p1_WPLoose_Gsf_HT200);
   fChain->SetBranchAddress("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250", &HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250, &b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250);
   fChain->SetBranchAddress("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300", &HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300, &b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300);
   fChain->SetBranchAddress("HLT_Mu10_CentralPFJet30_BTagCSV_p13", &HLT_Mu10_CentralPFJet30_BTagCSV_p13, &b_HLT_Mu10_CentralPFJet30_BTagCSV_p13);
   fChain->SetBranchAddress("HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13", &HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13, &b_HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV_p13);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400", &HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400, &b_HLT_Ele15_IsoVVVL_BTagCSV_p067_PFHT400);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT350_PFMET50", &HLT_Ele15_IsoVVVL_PFHT350_PFMET50, &b_HLT_Ele15_IsoVVVL_PFHT350_PFMET50);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT600", &HLT_Ele15_IsoVVVL_PFHT600, &b_HLT_Ele15_IsoVVVL_PFHT600);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT350", &HLT_Ele15_IsoVVVL_PFHT350, &b_HLT_Ele15_IsoVVVL_PFHT350);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT400_PFMET50", &HLT_Ele15_IsoVVVL_PFHT400_PFMET50, &b_HLT_Ele15_IsoVVVL_PFHT400_PFMET50);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT400", &HLT_Ele15_IsoVVVL_PFHT400, &b_HLT_Ele15_IsoVVVL_PFHT400);
   fChain->SetBranchAddress("HLT_Ele50_IsoVVVL_PFHT400", &HLT_Ele50_IsoVVVL_PFHT400, &b_HLT_Ele50_IsoVVVL_PFHT400);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60", &HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60, &b_HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60);
   fChain->SetBranchAddress("HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60", &HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60, &b_HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400", &HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400, &b_HLT_Mu15_IsoVVVL_BTagCSV_p067_PFHT400);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT350_PFMET50", &HLT_Mu15_IsoVVVL_PFHT350_PFMET50, &b_HLT_Mu15_IsoVVVL_PFHT350_PFMET50);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT600", &HLT_Mu15_IsoVVVL_PFHT600, &b_HLT_Mu15_IsoVVVL_PFHT600);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT350", &HLT_Mu15_IsoVVVL_PFHT350, &b_HLT_Mu15_IsoVVVL_PFHT350);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT400_PFMET50", &HLT_Mu15_IsoVVVL_PFHT400_PFMET50, &b_HLT_Mu15_IsoVVVL_PFHT400_PFMET50);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT400", &HLT_Mu15_IsoVVVL_PFHT400, &b_HLT_Mu15_IsoVVVL_PFHT400);
   fChain->SetBranchAddress("HLT_Mu50_IsoVVVL_PFHT400", &HLT_Mu50_IsoVVVL_PFHT400, &b_HLT_Mu50_IsoVVVL_PFHT400);
   fChain->SetBranchAddress("HLT_Mu16_TkMu0_dEta18_Onia", &HLT_Mu16_TkMu0_dEta18_Onia, &b_HLT_Mu16_TkMu0_dEta18_Onia);
   fChain->SetBranchAddress("HLT_Mu16_TkMu0_dEta18_Phi", &HLT_Mu16_TkMu0_dEta18_Phi, &b_HLT_Mu16_TkMu0_dEta18_Phi);
   fChain->SetBranchAddress("HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx", &HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx, &b_HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx", &HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx, &b_HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_Mu8", &HLT_Mu8, &b_HLT_Mu8);
   fChain->SetBranchAddress("HLT_Mu17", &HLT_Mu17, &b_HLT_Mu17);
   fChain->SetBranchAddress("HLT_Mu3_PFJet40", &HLT_Mu3_PFJet40, &b_HLT_Mu3_PFJet40);
   fChain->SetBranchAddress("HLT_Ele8_CaloIdM_TrackIdM_PFJet30", &HLT_Ele8_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele8_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele12_CaloIdM_TrackIdM_PFJet30", &HLT_Ele12_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele12_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele17_CaloIdM_TrackIdM_PFJet30", &HLT_Ele17_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele17_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele23_CaloIdM_TrackIdM_PFJet30", &HLT_Ele23_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele23_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140", &HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165", &HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165);
   fChain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT", &HLT_Ele115_CaloIdVT_GsfTrkIdT, &b_HLT_Ele115_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_Mu55", &HLT_Mu55, &b_HLT_Mu55);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity60ForEndOfFill", &HLT_PixelTracks_Multiplicity60ForEndOfFill, &b_HLT_PixelTracks_Multiplicity60ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity85ForEndOfFill", &HLT_PixelTracks_Multiplicity85ForEndOfFill, &b_HLT_PixelTracks_Multiplicity85ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity110ForEndOfFill", &HLT_PixelTracks_Multiplicity110ForEndOfFill, &b_HLT_PixelTracks_Multiplicity110ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity135ForEndOfFill", &HLT_PixelTracks_Multiplicity135ForEndOfFill, &b_HLT_PixelTracks_Multiplicity135ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity160ForEndOfFill", &HLT_PixelTracks_Multiplicity160ForEndOfFill, &b_HLT_PixelTracks_Multiplicity160ForEndOfFill);
   fChain->SetBranchAddress("HLT_ECALHT800", &HLT_ECALHT800, &b_HLT_ECALHT800);
   fChain->SetBranchAddress("HLT_MET100", &HLT_MET100, &b_HLT_MET100);
   fChain->SetBranchAddress("HLT_MET150", &HLT_MET150, &b_HLT_MET150);
   fChain->SetBranchAddress("HLT_MET200", &HLT_MET200, &b_HLT_MET200);
   fChain->SetBranchAddress("HLT_Ele27_HighEta_Ele20_Mass55", &HLT_Ele27_HighEta_Ele20_Mass55, &b_HLT_Ele27_HighEta_Ele20_Mass55);
   fChain->SetBranchAddress("HLT_Random", &HLT_Random, &b_HLT_Random);
   fChain->SetBranchAddress("HLT_EcalCalibration", &HLT_EcalCalibration, &b_HLT_EcalCalibration);
   fChain->SetBranchAddress("HLT_HcalCalibration", &HLT_HcalCalibration, &b_HLT_HcalCalibration);
   fChain->SetBranchAddress("HLT_GlobalRunHPDNoise", &HLT_GlobalRunHPDNoise, &b_HLT_GlobalRunHPDNoise);
   fChain->SetBranchAddress("HLT_HcalNZS", &HLT_HcalNZS, &b_HLT_HcalNZS);
   fChain->SetBranchAddress("HLT_HcalPhiSym", &HLT_HcalPhiSym, &b_HLT_HcalPhiSym);
   fChain->SetBranchAddress("HLT_HcalIsolatedbunch", &HLT_HcalIsolatedbunch, &b_HLT_HcalIsolatedbunch);
   fChain->SetBranchAddress("HLT_Mu300", &HLT_Mu300, &b_HLT_Mu300);
   fChain->SetBranchAddress("HLT_Mu350", &HLT_Mu350, &b_HLT_Mu350);
   fChain->SetBranchAddress("HLT_MET250", &HLT_MET250, &b_HLT_MET250);
   fChain->SetBranchAddress("HLT_MET300", &HLT_MET300, &b_HLT_MET300);
   fChain->SetBranchAddress("HLT_MET600", &HLT_MET600, &b_HLT_MET600);
   fChain->SetBranchAddress("HLT_MET700", &HLT_MET700, &b_HLT_MET700);
   fChain->SetBranchAddress("HLT_Ele250_CaloIdVT_GsfTrkIdT", &HLT_Ele250_CaloIdVT_GsfTrkIdT, &b_HLT_Ele250_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_Ele300_CaloIdVT_GsfTrkIdT", &HLT_Ele300_CaloIdVT_GsfTrkIdT, &b_HLT_Ele300_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_IsoTrackHE", &HLT_IsoTrackHE, &b_HLT_IsoTrackHE);
   fChain->SetBranchAddress("HLT_IsoTrackHB", &HLT_IsoTrackHB, &b_HLT_IsoTrackHB);
   fChain->SetBranchAddress("HLTriggerFinalPath", &HLTriggerFinalPath, &b_HLTriggerFinalPath);
   fChain->SetBranchAddress("Flag_HBHENoiseFilter", &Flag_HBHENoiseFilter, &b_Flag_HBHENoiseFilter);
   fChain->SetBranchAddress("Flag_HBHENoiseIsoFilter", &Flag_HBHENoiseIsoFilter, &b_Flag_HBHENoiseIsoFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloFilter", &Flag_CSCTightHaloFilter, &b_Flag_CSCTightHaloFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloTrkMuUnvetoFilter", &Flag_CSCTightHaloTrkMuUnvetoFilter, &b_Flag_CSCTightHaloTrkMuUnvetoFilter);
   fChain->SetBranchAddress("Flag_CSCTightHalo2015Filter", &Flag_CSCTightHalo2015Filter, &b_Flag_CSCTightHalo2015Filter);
   fChain->SetBranchAddress("Flag_globalTightHalo2016Filter", &Flag_globalTightHalo2016Filter, &b_Flag_globalTightHalo2016Filter);
   fChain->SetBranchAddress("Flag_globalSuperTightHalo2016Filter", &Flag_globalSuperTightHalo2016Filter, &b_Flag_globalSuperTightHalo2016Filter);
   fChain->SetBranchAddress("Flag_HcalStripHaloFilter", &Flag_HcalStripHaloFilter, &b_Flag_HcalStripHaloFilter);
   fChain->SetBranchAddress("Flag_hcalLaserEventFilter", &Flag_hcalLaserEventFilter, &b_Flag_hcalLaserEventFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellTriggerPrimitiveFilter", &Flag_EcalDeadCellTriggerPrimitiveFilter, &b_Flag_EcalDeadCellTriggerPrimitiveFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellBoundaryEnergyFilter", &Flag_EcalDeadCellBoundaryEnergyFilter, &b_Flag_EcalDeadCellBoundaryEnergyFilter);
   fChain->SetBranchAddress("Flag_goodVertices", &Flag_goodVertices, &b_Flag_goodVertices);
   fChain->SetBranchAddress("Flag_eeBadScFilter", &Flag_eeBadScFilter, &b_Flag_eeBadScFilter);
   fChain->SetBranchAddress("Flag_ecalLaserCorrFilter", &Flag_ecalLaserCorrFilter, &b_Flag_ecalLaserCorrFilter);
   fChain->SetBranchAddress("Flag_trkPOGFilters", &Flag_trkPOGFilters, &b_Flag_trkPOGFilters);
   fChain->SetBranchAddress("Flag_chargedHadronTrackResolutionFilter", &Flag_chargedHadronTrackResolutionFilter, &b_Flag_chargedHadronTrackResolutionFilter);
   fChain->SetBranchAddress("Flag_muonBadTrackFilter", &Flag_muonBadTrackFilter, &b_Flag_muonBadTrackFilter);
   fChain->SetBranchAddress("Flag_trkPOG_manystripclus53X", &Flag_trkPOG_manystripclus53X, &b_Flag_trkPOG_manystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_toomanystripclus53X", &Flag_trkPOG_toomanystripclus53X, &b_Flag_trkPOG_toomanystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_logErrorTooManyClusters", &Flag_trkPOG_logErrorTooManyClusters, &b_Flag_trkPOG_logErrorTooManyClusters);
   fChain->SetBranchAddress("Flag_METFilters", &Flag_METFilters, &b_Flag_METFilters);
   fChain->SetBranchAddress("puWeight", &puWeight, &b_puWeight);
   fChain->SetBranchAddress("puWeightUp", &puWeightUp, &b_puWeightUp);
   fChain->SetBranchAddress("puWeightDown", &puWeightDown, &b_puWeightDown);
   fChain->SetBranchAddress("Jet_pt_nom", Jet_pt_nom, &b_Jet_pt_nom);
   fChain->SetBranchAddress("Jet_mass_nom", Jet_mass_nom, &b_Jet_mass_nom);
   fChain->SetBranchAddress("MET_pt_nom", &MET_pt_nom, &b_MET_pt_nom);
   fChain->SetBranchAddress("MET_phi_nom", &MET_phi_nom, &b_MET_phi_nom);
   fChain->SetBranchAddress("Jet_pt_jerUp", Jet_pt_jerUp, &b_Jet_pt_jerUp);
   fChain->SetBranchAddress("Jet_mass_jerUp", Jet_mass_jerUp, &b_Jet_mass_jerUp);
   fChain->SetBranchAddress("Jet_mass_jmrUp", Jet_mass_jmrUp, &b_Jet_mass_jmrUp);
   fChain->SetBranchAddress("Jet_mass_jmsUp", Jet_mass_jmsUp, &b_Jet_mass_jmsUp);
   fChain->SetBranchAddress("MET_pt_jerUp", &MET_pt_jerUp, &b_MET_pt_jerUp);
   fChain->SetBranchAddress("MET_phi_jerUp", &MET_phi_jerUp, &b_MET_phi_jerUp);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteStatUp", Jet_pt_jesAbsoluteStatUp, &b_Jet_pt_jesAbsoluteStatUp);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteStatUp", Jet_mass_jesAbsoluteStatUp, &b_Jet_mass_jesAbsoluteStatUp);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteStatUp", &MET_pt_jesAbsoluteStatUp, &b_MET_pt_jesAbsoluteStatUp);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteStatUp", &MET_phi_jesAbsoluteStatUp, &b_MET_phi_jesAbsoluteStatUp);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteScaleUp", Jet_pt_jesAbsoluteScaleUp, &b_Jet_pt_jesAbsoluteScaleUp);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteScaleUp", Jet_mass_jesAbsoluteScaleUp, &b_Jet_mass_jesAbsoluteScaleUp);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteScaleUp", &MET_pt_jesAbsoluteScaleUp, &b_MET_pt_jesAbsoluteScaleUp);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteScaleUp", &MET_phi_jesAbsoluteScaleUp, &b_MET_phi_jesAbsoluteScaleUp);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteFlavMapUp", Jet_pt_jesAbsoluteFlavMapUp, &b_Jet_pt_jesAbsoluteFlavMapUp);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteFlavMapUp", Jet_mass_jesAbsoluteFlavMapUp, &b_Jet_mass_jesAbsoluteFlavMapUp);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteFlavMapUp", &MET_pt_jesAbsoluteFlavMapUp, &b_MET_pt_jesAbsoluteFlavMapUp);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteFlavMapUp", &MET_phi_jesAbsoluteFlavMapUp, &b_MET_phi_jesAbsoluteFlavMapUp);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteMPFBiasUp", Jet_pt_jesAbsoluteMPFBiasUp, &b_Jet_pt_jesAbsoluteMPFBiasUp);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteMPFBiasUp", Jet_mass_jesAbsoluteMPFBiasUp, &b_Jet_mass_jesAbsoluteMPFBiasUp);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteMPFBiasUp", &MET_pt_jesAbsoluteMPFBiasUp, &b_MET_pt_jesAbsoluteMPFBiasUp);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteMPFBiasUp", &MET_phi_jesAbsoluteMPFBiasUp, &b_MET_phi_jesAbsoluteMPFBiasUp);
   fChain->SetBranchAddress("Jet_pt_jesFragmentationUp", Jet_pt_jesFragmentationUp, &b_Jet_pt_jesFragmentationUp);
   fChain->SetBranchAddress("Jet_mass_jesFragmentationUp", Jet_mass_jesFragmentationUp, &b_Jet_mass_jesFragmentationUp);
   fChain->SetBranchAddress("MET_pt_jesFragmentationUp", &MET_pt_jesFragmentationUp, &b_MET_pt_jesFragmentationUp);
   fChain->SetBranchAddress("MET_phi_jesFragmentationUp", &MET_phi_jesFragmentationUp, &b_MET_phi_jesFragmentationUp);
   fChain->SetBranchAddress("Jet_pt_jesSinglePionECALUp", Jet_pt_jesSinglePionECALUp, &b_Jet_pt_jesSinglePionECALUp);
   fChain->SetBranchAddress("Jet_mass_jesSinglePionECALUp", Jet_mass_jesSinglePionECALUp, &b_Jet_mass_jesSinglePionECALUp);
   fChain->SetBranchAddress("MET_pt_jesSinglePionECALUp", &MET_pt_jesSinglePionECALUp, &b_MET_pt_jesSinglePionECALUp);
   fChain->SetBranchAddress("MET_phi_jesSinglePionECALUp", &MET_phi_jesSinglePionECALUp, &b_MET_phi_jesSinglePionECALUp);
   fChain->SetBranchAddress("Jet_pt_jesSinglePionHCALUp", Jet_pt_jesSinglePionHCALUp, &b_Jet_pt_jesSinglePionHCALUp);
   fChain->SetBranchAddress("Jet_mass_jesSinglePionHCALUp", Jet_mass_jesSinglePionHCALUp, &b_Jet_mass_jesSinglePionHCALUp);
   fChain->SetBranchAddress("MET_pt_jesSinglePionHCALUp", &MET_pt_jesSinglePionHCALUp, &b_MET_pt_jesSinglePionHCALUp);
   fChain->SetBranchAddress("MET_phi_jesSinglePionHCALUp", &MET_phi_jesSinglePionHCALUp, &b_MET_phi_jesSinglePionHCALUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorQCDUp", Jet_pt_jesFlavorQCDUp, &b_Jet_pt_jesFlavorQCDUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorQCDUp", Jet_mass_jesFlavorQCDUp, &b_Jet_mass_jesFlavorQCDUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorQCDUp", &MET_pt_jesFlavorQCDUp, &b_MET_pt_jesFlavorQCDUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorQCDUp", &MET_phi_jesFlavorQCDUp, &b_MET_phi_jesFlavorQCDUp);
   fChain->SetBranchAddress("Jet_pt_jesTimePtEtaUp", Jet_pt_jesTimePtEtaUp, &b_Jet_pt_jesTimePtEtaUp);
   fChain->SetBranchAddress("Jet_mass_jesTimePtEtaUp", Jet_mass_jesTimePtEtaUp, &b_Jet_mass_jesTimePtEtaUp);
   fChain->SetBranchAddress("MET_pt_jesTimePtEtaUp", &MET_pt_jesTimePtEtaUp, &b_MET_pt_jesTimePtEtaUp);
   fChain->SetBranchAddress("MET_phi_jesTimePtEtaUp", &MET_phi_jesTimePtEtaUp, &b_MET_phi_jesTimePtEtaUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativeJEREC1Up", Jet_pt_jesRelativeJEREC1Up, &b_Jet_pt_jesRelativeJEREC1Up);
   fChain->SetBranchAddress("Jet_mass_jesRelativeJEREC1Up", Jet_mass_jesRelativeJEREC1Up, &b_Jet_mass_jesRelativeJEREC1Up);
   fChain->SetBranchAddress("MET_pt_jesRelativeJEREC1Up", &MET_pt_jesRelativeJEREC1Up, &b_MET_pt_jesRelativeJEREC1Up);
   fChain->SetBranchAddress("MET_phi_jesRelativeJEREC1Up", &MET_phi_jesRelativeJEREC1Up, &b_MET_phi_jesRelativeJEREC1Up);
   fChain->SetBranchAddress("Jet_pt_jesRelativeJEREC2Up", Jet_pt_jesRelativeJEREC2Up, &b_Jet_pt_jesRelativeJEREC2Up);
   fChain->SetBranchAddress("Jet_mass_jesRelativeJEREC2Up", Jet_mass_jesRelativeJEREC2Up, &b_Jet_mass_jesRelativeJEREC2Up);
   fChain->SetBranchAddress("MET_pt_jesRelativeJEREC2Up", &MET_pt_jesRelativeJEREC2Up, &b_MET_pt_jesRelativeJEREC2Up);
   fChain->SetBranchAddress("MET_phi_jesRelativeJEREC2Up", &MET_phi_jesRelativeJEREC2Up, &b_MET_phi_jesRelativeJEREC2Up);
   fChain->SetBranchAddress("Jet_pt_jesRelativeJERHFUp", Jet_pt_jesRelativeJERHFUp, &b_Jet_pt_jesRelativeJERHFUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativeJERHFUp", Jet_mass_jesRelativeJERHFUp, &b_Jet_mass_jesRelativeJERHFUp);
   fChain->SetBranchAddress("MET_pt_jesRelativeJERHFUp", &MET_pt_jesRelativeJERHFUp, &b_MET_pt_jesRelativeJERHFUp);
   fChain->SetBranchAddress("MET_phi_jesRelativeJERHFUp", &MET_phi_jesRelativeJERHFUp, &b_MET_phi_jesRelativeJERHFUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtBBUp", Jet_pt_jesRelativePtBBUp, &b_Jet_pt_jesRelativePtBBUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtBBUp", Jet_mass_jesRelativePtBBUp, &b_Jet_mass_jesRelativePtBBUp);
   fChain->SetBranchAddress("MET_pt_jesRelativePtBBUp", &MET_pt_jesRelativePtBBUp, &b_MET_pt_jesRelativePtBBUp);
   fChain->SetBranchAddress("MET_phi_jesRelativePtBBUp", &MET_phi_jesRelativePtBBUp, &b_MET_phi_jesRelativePtBBUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtEC1Up", Jet_pt_jesRelativePtEC1Up, &b_Jet_pt_jesRelativePtEC1Up);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtEC1Up", Jet_mass_jesRelativePtEC1Up, &b_Jet_mass_jesRelativePtEC1Up);
   fChain->SetBranchAddress("MET_pt_jesRelativePtEC1Up", &MET_pt_jesRelativePtEC1Up, &b_MET_pt_jesRelativePtEC1Up);
   fChain->SetBranchAddress("MET_phi_jesRelativePtEC1Up", &MET_phi_jesRelativePtEC1Up, &b_MET_phi_jesRelativePtEC1Up);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtEC2Up", Jet_pt_jesRelativePtEC2Up, &b_Jet_pt_jesRelativePtEC2Up);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtEC2Up", Jet_mass_jesRelativePtEC2Up, &b_Jet_mass_jesRelativePtEC2Up);
   fChain->SetBranchAddress("MET_pt_jesRelativePtEC2Up", &MET_pt_jesRelativePtEC2Up, &b_MET_pt_jesRelativePtEC2Up);
   fChain->SetBranchAddress("MET_phi_jesRelativePtEC2Up", &MET_phi_jesRelativePtEC2Up, &b_MET_phi_jesRelativePtEC2Up);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtHFUp", Jet_pt_jesRelativePtHFUp, &b_Jet_pt_jesRelativePtHFUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtHFUp", Jet_mass_jesRelativePtHFUp, &b_Jet_mass_jesRelativePtHFUp);
   fChain->SetBranchAddress("MET_pt_jesRelativePtHFUp", &MET_pt_jesRelativePtHFUp, &b_MET_pt_jesRelativePtHFUp);
   fChain->SetBranchAddress("MET_phi_jesRelativePtHFUp", &MET_phi_jesRelativePtHFUp, &b_MET_phi_jesRelativePtHFUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativeBalUp", Jet_pt_jesRelativeBalUp, &b_Jet_pt_jesRelativeBalUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativeBalUp", Jet_mass_jesRelativeBalUp, &b_Jet_mass_jesRelativeBalUp);
   fChain->SetBranchAddress("MET_pt_jesRelativeBalUp", &MET_pt_jesRelativeBalUp, &b_MET_pt_jesRelativeBalUp);
   fChain->SetBranchAddress("MET_phi_jesRelativeBalUp", &MET_phi_jesRelativeBalUp, &b_MET_phi_jesRelativeBalUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativeFSRUp", Jet_pt_jesRelativeFSRUp, &b_Jet_pt_jesRelativeFSRUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativeFSRUp", Jet_mass_jesRelativeFSRUp, &b_Jet_mass_jesRelativeFSRUp);
   fChain->SetBranchAddress("MET_pt_jesRelativeFSRUp", &MET_pt_jesRelativeFSRUp, &b_MET_pt_jesRelativeFSRUp);
   fChain->SetBranchAddress("MET_phi_jesRelativeFSRUp", &MET_phi_jesRelativeFSRUp, &b_MET_phi_jesRelativeFSRUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativeStatFSRUp", Jet_pt_jesRelativeStatFSRUp, &b_Jet_pt_jesRelativeStatFSRUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativeStatFSRUp", Jet_mass_jesRelativeStatFSRUp, &b_Jet_mass_jesRelativeStatFSRUp);
   fChain->SetBranchAddress("MET_pt_jesRelativeStatFSRUp", &MET_pt_jesRelativeStatFSRUp, &b_MET_pt_jesRelativeStatFSRUp);
   fChain->SetBranchAddress("MET_phi_jesRelativeStatFSRUp", &MET_phi_jesRelativeStatFSRUp, &b_MET_phi_jesRelativeStatFSRUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativeStatECUp", Jet_pt_jesRelativeStatECUp, &b_Jet_pt_jesRelativeStatECUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativeStatECUp", Jet_mass_jesRelativeStatECUp, &b_Jet_mass_jesRelativeStatECUp);
   fChain->SetBranchAddress("MET_pt_jesRelativeStatECUp", &MET_pt_jesRelativeStatECUp, &b_MET_pt_jesRelativeStatECUp);
   fChain->SetBranchAddress("MET_phi_jesRelativeStatECUp", &MET_phi_jesRelativeStatECUp, &b_MET_phi_jesRelativeStatECUp);
   fChain->SetBranchAddress("Jet_pt_jesRelativeStatHFUp", Jet_pt_jesRelativeStatHFUp, &b_Jet_pt_jesRelativeStatHFUp);
   fChain->SetBranchAddress("Jet_mass_jesRelativeStatHFUp", Jet_mass_jesRelativeStatHFUp, &b_Jet_mass_jesRelativeStatHFUp);
   fChain->SetBranchAddress("MET_pt_jesRelativeStatHFUp", &MET_pt_jesRelativeStatHFUp, &b_MET_pt_jesRelativeStatHFUp);
   fChain->SetBranchAddress("MET_phi_jesRelativeStatHFUp", &MET_phi_jesRelativeStatHFUp, &b_MET_phi_jesRelativeStatHFUp);
   fChain->SetBranchAddress("Jet_pt_jesPileUpDataMCUp", Jet_pt_jesPileUpDataMCUp, &b_Jet_pt_jesPileUpDataMCUp);
   fChain->SetBranchAddress("Jet_mass_jesPileUpDataMCUp", Jet_mass_jesPileUpDataMCUp, &b_Jet_mass_jesPileUpDataMCUp);
   fChain->SetBranchAddress("MET_pt_jesPileUpDataMCUp", &MET_pt_jesPileUpDataMCUp, &b_MET_pt_jesPileUpDataMCUp);
   fChain->SetBranchAddress("MET_phi_jesPileUpDataMCUp", &MET_phi_jesPileUpDataMCUp, &b_MET_phi_jesPileUpDataMCUp);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtRefUp", Jet_pt_jesPileUpPtRefUp, &b_Jet_pt_jesPileUpPtRefUp);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtRefUp", Jet_mass_jesPileUpPtRefUp, &b_Jet_mass_jesPileUpPtRefUp);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtRefUp", &MET_pt_jesPileUpPtRefUp, &b_MET_pt_jesPileUpPtRefUp);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtRefUp", &MET_phi_jesPileUpPtRefUp, &b_MET_phi_jesPileUpPtRefUp);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtBBUp", Jet_pt_jesPileUpPtBBUp, &b_Jet_pt_jesPileUpPtBBUp);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtBBUp", Jet_mass_jesPileUpPtBBUp, &b_Jet_mass_jesPileUpPtBBUp);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtBBUp", &MET_pt_jesPileUpPtBBUp, &b_MET_pt_jesPileUpPtBBUp);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtBBUp", &MET_phi_jesPileUpPtBBUp, &b_MET_phi_jesPileUpPtBBUp);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtEC1Up", Jet_pt_jesPileUpPtEC1Up, &b_Jet_pt_jesPileUpPtEC1Up);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtEC1Up", Jet_mass_jesPileUpPtEC1Up, &b_Jet_mass_jesPileUpPtEC1Up);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtEC1Up", &MET_pt_jesPileUpPtEC1Up, &b_MET_pt_jesPileUpPtEC1Up);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtEC1Up", &MET_phi_jesPileUpPtEC1Up, &b_MET_phi_jesPileUpPtEC1Up);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtEC2Up", Jet_pt_jesPileUpPtEC2Up, &b_Jet_pt_jesPileUpPtEC2Up);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtEC2Up", Jet_mass_jesPileUpPtEC2Up, &b_Jet_mass_jesPileUpPtEC2Up);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtEC2Up", &MET_pt_jesPileUpPtEC2Up, &b_MET_pt_jesPileUpPtEC2Up);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtEC2Up", &MET_phi_jesPileUpPtEC2Up, &b_MET_phi_jesPileUpPtEC2Up);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtHFUp", Jet_pt_jesPileUpPtHFUp, &b_Jet_pt_jesPileUpPtHFUp);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtHFUp", Jet_mass_jesPileUpPtHFUp, &b_Jet_mass_jesPileUpPtHFUp);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtHFUp", &MET_pt_jesPileUpPtHFUp, &b_MET_pt_jesPileUpPtHFUp);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtHFUp", &MET_phi_jesPileUpPtHFUp, &b_MET_phi_jesPileUpPtHFUp);
   fChain->SetBranchAddress("Jet_pt_jesPileUpMuZeroUp", Jet_pt_jesPileUpMuZeroUp, &b_Jet_pt_jesPileUpMuZeroUp);
   fChain->SetBranchAddress("Jet_mass_jesPileUpMuZeroUp", Jet_mass_jesPileUpMuZeroUp, &b_Jet_mass_jesPileUpMuZeroUp);
   fChain->SetBranchAddress("MET_pt_jesPileUpMuZeroUp", &MET_pt_jesPileUpMuZeroUp, &b_MET_pt_jesPileUpMuZeroUp);
   fChain->SetBranchAddress("MET_phi_jesPileUpMuZeroUp", &MET_phi_jesPileUpMuZeroUp, &b_MET_phi_jesPileUpMuZeroUp);
   fChain->SetBranchAddress("Jet_pt_jesPileUpEnvelopeUp", Jet_pt_jesPileUpEnvelopeUp, &b_Jet_pt_jesPileUpEnvelopeUp);
   fChain->SetBranchAddress("Jet_mass_jesPileUpEnvelopeUp", Jet_mass_jesPileUpEnvelopeUp, &b_Jet_mass_jesPileUpEnvelopeUp);
   fChain->SetBranchAddress("MET_pt_jesPileUpEnvelopeUp", &MET_pt_jesPileUpEnvelopeUp, &b_MET_pt_jesPileUpEnvelopeUp);
   fChain->SetBranchAddress("MET_phi_jesPileUpEnvelopeUp", &MET_phi_jesPileUpEnvelopeUp, &b_MET_phi_jesPileUpEnvelopeUp);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalPileUpUp", Jet_pt_jesSubTotalPileUpUp, &b_Jet_pt_jesSubTotalPileUpUp);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalPileUpUp", Jet_mass_jesSubTotalPileUpUp, &b_Jet_mass_jesSubTotalPileUpUp);
   fChain->SetBranchAddress("MET_pt_jesSubTotalPileUpUp", &MET_pt_jesSubTotalPileUpUp, &b_MET_pt_jesSubTotalPileUpUp);
   fChain->SetBranchAddress("MET_phi_jesSubTotalPileUpUp", &MET_phi_jesSubTotalPileUpUp, &b_MET_phi_jesSubTotalPileUpUp);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalRelativeUp", Jet_pt_jesSubTotalRelativeUp, &b_Jet_pt_jesSubTotalRelativeUp);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalRelativeUp", Jet_mass_jesSubTotalRelativeUp, &b_Jet_mass_jesSubTotalRelativeUp);
   fChain->SetBranchAddress("MET_pt_jesSubTotalRelativeUp", &MET_pt_jesSubTotalRelativeUp, &b_MET_pt_jesSubTotalRelativeUp);
   fChain->SetBranchAddress("MET_phi_jesSubTotalRelativeUp", &MET_phi_jesSubTotalRelativeUp, &b_MET_phi_jesSubTotalRelativeUp);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalPtUp", Jet_pt_jesSubTotalPtUp, &b_Jet_pt_jesSubTotalPtUp);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalPtUp", Jet_mass_jesSubTotalPtUp, &b_Jet_mass_jesSubTotalPtUp);
   fChain->SetBranchAddress("MET_pt_jesSubTotalPtUp", &MET_pt_jesSubTotalPtUp, &b_MET_pt_jesSubTotalPtUp);
   fChain->SetBranchAddress("MET_phi_jesSubTotalPtUp", &MET_phi_jesSubTotalPtUp, &b_MET_phi_jesSubTotalPtUp);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalScaleUp", Jet_pt_jesSubTotalScaleUp, &b_Jet_pt_jesSubTotalScaleUp);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalScaleUp", Jet_mass_jesSubTotalScaleUp, &b_Jet_mass_jesSubTotalScaleUp);
   fChain->SetBranchAddress("MET_pt_jesSubTotalScaleUp", &MET_pt_jesSubTotalScaleUp, &b_MET_pt_jesSubTotalScaleUp);
   fChain->SetBranchAddress("MET_phi_jesSubTotalScaleUp", &MET_phi_jesSubTotalScaleUp, &b_MET_phi_jesSubTotalScaleUp);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalAbsoluteUp", Jet_pt_jesSubTotalAbsoluteUp, &b_Jet_pt_jesSubTotalAbsoluteUp);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalAbsoluteUp", Jet_mass_jesSubTotalAbsoluteUp, &b_Jet_mass_jesSubTotalAbsoluteUp);
   fChain->SetBranchAddress("MET_pt_jesSubTotalAbsoluteUp", &MET_pt_jesSubTotalAbsoluteUp, &b_MET_pt_jesSubTotalAbsoluteUp);
   fChain->SetBranchAddress("MET_phi_jesSubTotalAbsoluteUp", &MET_phi_jesSubTotalAbsoluteUp, &b_MET_phi_jesSubTotalAbsoluteUp);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalMCUp", Jet_pt_jesSubTotalMCUp, &b_Jet_pt_jesSubTotalMCUp);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalMCUp", Jet_mass_jesSubTotalMCUp, &b_Jet_mass_jesSubTotalMCUp);
   fChain->SetBranchAddress("MET_pt_jesSubTotalMCUp", &MET_pt_jesSubTotalMCUp, &b_MET_pt_jesSubTotalMCUp);
   fChain->SetBranchAddress("MET_phi_jesSubTotalMCUp", &MET_phi_jesSubTotalMCUp, &b_MET_phi_jesSubTotalMCUp);
   fChain->SetBranchAddress("Jet_pt_jesTotalUp", Jet_pt_jesTotalUp, &b_Jet_pt_jesTotalUp);
   fChain->SetBranchAddress("Jet_mass_jesTotalUp", Jet_mass_jesTotalUp, &b_Jet_mass_jesTotalUp);
   fChain->SetBranchAddress("MET_pt_jesTotalUp", &MET_pt_jesTotalUp, &b_MET_pt_jesTotalUp);
   fChain->SetBranchAddress("MET_phi_jesTotalUp", &MET_phi_jesTotalUp, &b_MET_phi_jesTotalUp);
   fChain->SetBranchAddress("Jet_pt_jesTotalNoFlavorUp", Jet_pt_jesTotalNoFlavorUp, &b_Jet_pt_jesTotalNoFlavorUp);
   fChain->SetBranchAddress("Jet_mass_jesTotalNoFlavorUp", Jet_mass_jesTotalNoFlavorUp, &b_Jet_mass_jesTotalNoFlavorUp);
   fChain->SetBranchAddress("MET_pt_jesTotalNoFlavorUp", &MET_pt_jesTotalNoFlavorUp, &b_MET_pt_jesTotalNoFlavorUp);
   fChain->SetBranchAddress("MET_phi_jesTotalNoFlavorUp", &MET_phi_jesTotalNoFlavorUp, &b_MET_phi_jesTotalNoFlavorUp);
   fChain->SetBranchAddress("Jet_pt_jesTotalNoTimeUp", Jet_pt_jesTotalNoTimeUp, &b_Jet_pt_jesTotalNoTimeUp);
   fChain->SetBranchAddress("Jet_mass_jesTotalNoTimeUp", Jet_mass_jesTotalNoTimeUp, &b_Jet_mass_jesTotalNoTimeUp);
   fChain->SetBranchAddress("MET_pt_jesTotalNoTimeUp", &MET_pt_jesTotalNoTimeUp, &b_MET_pt_jesTotalNoTimeUp);
   fChain->SetBranchAddress("MET_phi_jesTotalNoTimeUp", &MET_phi_jesTotalNoTimeUp, &b_MET_phi_jesTotalNoTimeUp);
   fChain->SetBranchAddress("Jet_pt_jesTotalNoFlavorNoTimeUp", Jet_pt_jesTotalNoFlavorNoTimeUp, &b_Jet_pt_jesTotalNoFlavorNoTimeUp);
   fChain->SetBranchAddress("Jet_mass_jesTotalNoFlavorNoTimeUp", Jet_mass_jesTotalNoFlavorNoTimeUp, &b_Jet_mass_jesTotalNoFlavorNoTimeUp);
   fChain->SetBranchAddress("MET_pt_jesTotalNoFlavorNoTimeUp", &MET_pt_jesTotalNoFlavorNoTimeUp, &b_MET_pt_jesTotalNoFlavorNoTimeUp);
   fChain->SetBranchAddress("MET_phi_jesTotalNoFlavorNoTimeUp", &MET_phi_jesTotalNoFlavorNoTimeUp, &b_MET_phi_jesTotalNoFlavorNoTimeUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorZJetUp", Jet_pt_jesFlavorZJetUp, &b_Jet_pt_jesFlavorZJetUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorZJetUp", Jet_mass_jesFlavorZJetUp, &b_Jet_mass_jesFlavorZJetUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorZJetUp", &MET_pt_jesFlavorZJetUp, &b_MET_pt_jesFlavorZJetUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorZJetUp", &MET_phi_jesFlavorZJetUp, &b_MET_phi_jesFlavorZJetUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPhotonJetUp", Jet_pt_jesFlavorPhotonJetUp, &b_Jet_pt_jesFlavorPhotonJetUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPhotonJetUp", Jet_mass_jesFlavorPhotonJetUp, &b_Jet_mass_jesFlavorPhotonJetUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorPhotonJetUp", &MET_pt_jesFlavorPhotonJetUp, &b_MET_pt_jesFlavorPhotonJetUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorPhotonJetUp", &MET_phi_jesFlavorPhotonJetUp, &b_MET_phi_jesFlavorPhotonJetUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureGluonUp", Jet_pt_jesFlavorPureGluonUp, &b_Jet_pt_jesFlavorPureGluonUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureGluonUp", Jet_mass_jesFlavorPureGluonUp, &b_Jet_mass_jesFlavorPureGluonUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureGluonUp", &MET_pt_jesFlavorPureGluonUp, &b_MET_pt_jesFlavorPureGluonUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureGluonUp", &MET_phi_jesFlavorPureGluonUp, &b_MET_phi_jesFlavorPureGluonUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureQuarkUp", Jet_pt_jesFlavorPureQuarkUp, &b_Jet_pt_jesFlavorPureQuarkUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureQuarkUp", Jet_mass_jesFlavorPureQuarkUp, &b_Jet_mass_jesFlavorPureQuarkUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureQuarkUp", &MET_pt_jesFlavorPureQuarkUp, &b_MET_pt_jesFlavorPureQuarkUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureQuarkUp", &MET_phi_jesFlavorPureQuarkUp, &b_MET_phi_jesFlavorPureQuarkUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureCharmUp", Jet_pt_jesFlavorPureCharmUp, &b_Jet_pt_jesFlavorPureCharmUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureCharmUp", Jet_mass_jesFlavorPureCharmUp, &b_Jet_mass_jesFlavorPureCharmUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureCharmUp", &MET_pt_jesFlavorPureCharmUp, &b_MET_pt_jesFlavorPureCharmUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureCharmUp", &MET_phi_jesFlavorPureCharmUp, &b_MET_phi_jesFlavorPureCharmUp);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureBottomUp", Jet_pt_jesFlavorPureBottomUp, &b_Jet_pt_jesFlavorPureBottomUp);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureBottomUp", Jet_mass_jesFlavorPureBottomUp, &b_Jet_mass_jesFlavorPureBottomUp);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureBottomUp", &MET_pt_jesFlavorPureBottomUp, &b_MET_pt_jesFlavorPureBottomUp);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureBottomUp", &MET_phi_jesFlavorPureBottomUp, &b_MET_phi_jesFlavorPureBottomUp);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunBCDUp", Jet_pt_jesTimeRunBCDUp, &b_Jet_pt_jesTimeRunBCDUp);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunBCDUp", Jet_mass_jesTimeRunBCDUp, &b_Jet_mass_jesTimeRunBCDUp);
   fChain->SetBranchAddress("MET_pt_jesTimeRunBCDUp", &MET_pt_jesTimeRunBCDUp, &b_MET_pt_jesTimeRunBCDUp);
   fChain->SetBranchAddress("MET_phi_jesTimeRunBCDUp", &MET_phi_jesTimeRunBCDUp, &b_MET_phi_jesTimeRunBCDUp);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunEFUp", Jet_pt_jesTimeRunEFUp, &b_Jet_pt_jesTimeRunEFUp);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunEFUp", Jet_mass_jesTimeRunEFUp, &b_Jet_mass_jesTimeRunEFUp);
   fChain->SetBranchAddress("MET_pt_jesTimeRunEFUp", &MET_pt_jesTimeRunEFUp, &b_MET_pt_jesTimeRunEFUp);
   fChain->SetBranchAddress("MET_phi_jesTimeRunEFUp", &MET_phi_jesTimeRunEFUp, &b_MET_phi_jesTimeRunEFUp);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunGUp", Jet_pt_jesTimeRunGUp, &b_Jet_pt_jesTimeRunGUp);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunGUp", Jet_mass_jesTimeRunGUp, &b_Jet_mass_jesTimeRunGUp);
   fChain->SetBranchAddress("MET_pt_jesTimeRunGUp", &MET_pt_jesTimeRunGUp, &b_MET_pt_jesTimeRunGUp);
   fChain->SetBranchAddress("MET_phi_jesTimeRunGUp", &MET_phi_jesTimeRunGUp, &b_MET_phi_jesTimeRunGUp);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunHUp", Jet_pt_jesTimeRunHUp, &b_Jet_pt_jesTimeRunHUp);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunHUp", Jet_mass_jesTimeRunHUp, &b_Jet_mass_jesTimeRunHUp);
   fChain->SetBranchAddress("MET_pt_jesTimeRunHUp", &MET_pt_jesTimeRunHUp, &b_MET_pt_jesTimeRunHUp);
   fChain->SetBranchAddress("MET_phi_jesTimeRunHUp", &MET_phi_jesTimeRunHUp, &b_MET_phi_jesTimeRunHUp);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupMPFInSituUp", Jet_pt_jesCorrelationGroupMPFInSituUp, &b_Jet_pt_jesCorrelationGroupMPFInSituUp);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupMPFInSituUp", Jet_mass_jesCorrelationGroupMPFInSituUp, &b_Jet_mass_jesCorrelationGroupMPFInSituUp);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupMPFInSituUp", &MET_pt_jesCorrelationGroupMPFInSituUp, &b_MET_pt_jesCorrelationGroupMPFInSituUp);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupMPFInSituUp", &MET_phi_jesCorrelationGroupMPFInSituUp, &b_MET_phi_jesCorrelationGroupMPFInSituUp);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupIntercalibrationUp", Jet_pt_jesCorrelationGroupIntercalibrationUp, &b_Jet_pt_jesCorrelationGroupIntercalibrationUp);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupIntercalibrationUp", Jet_mass_jesCorrelationGroupIntercalibrationUp, &b_Jet_mass_jesCorrelationGroupIntercalibrationUp);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupIntercalibrationUp", &MET_pt_jesCorrelationGroupIntercalibrationUp, &b_MET_pt_jesCorrelationGroupIntercalibrationUp);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupIntercalibrationUp", &MET_phi_jesCorrelationGroupIntercalibrationUp, &b_MET_phi_jesCorrelationGroupIntercalibrationUp);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupbJESUp", Jet_pt_jesCorrelationGroupbJESUp, &b_Jet_pt_jesCorrelationGroupbJESUp);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupbJESUp", Jet_mass_jesCorrelationGroupbJESUp, &b_Jet_mass_jesCorrelationGroupbJESUp);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupbJESUp", &MET_pt_jesCorrelationGroupbJESUp, &b_MET_pt_jesCorrelationGroupbJESUp);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupbJESUp", &MET_phi_jesCorrelationGroupbJESUp, &b_MET_phi_jesCorrelationGroupbJESUp);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupFlavorUp", Jet_pt_jesCorrelationGroupFlavorUp, &b_Jet_pt_jesCorrelationGroupFlavorUp);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupFlavorUp", Jet_mass_jesCorrelationGroupFlavorUp, &b_Jet_mass_jesCorrelationGroupFlavorUp);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupFlavorUp", &MET_pt_jesCorrelationGroupFlavorUp, &b_MET_pt_jesCorrelationGroupFlavorUp);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupFlavorUp", &MET_phi_jesCorrelationGroupFlavorUp, &b_MET_phi_jesCorrelationGroupFlavorUp);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupUncorrelatedUp", Jet_pt_jesCorrelationGroupUncorrelatedUp, &b_Jet_pt_jesCorrelationGroupUncorrelatedUp);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupUncorrelatedUp", Jet_mass_jesCorrelationGroupUncorrelatedUp, &b_Jet_mass_jesCorrelationGroupUncorrelatedUp);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupUncorrelatedUp", &MET_pt_jesCorrelationGroupUncorrelatedUp, &b_MET_pt_jesCorrelationGroupUncorrelatedUp);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupUncorrelatedUp", &MET_phi_jesCorrelationGroupUncorrelatedUp, &b_MET_phi_jesCorrelationGroupUncorrelatedUp);
   fChain->SetBranchAddress("MET_pt_unclustEnUp", &MET_pt_unclustEnUp, &b_MET_pt_unclustEnUp);
   fChain->SetBranchAddress("MET_phi_unclustEnUp", &MET_phi_unclustEnUp, &b_MET_phi_unclustEnUp);
   fChain->SetBranchAddress("Jet_pt_jerDown", Jet_pt_jerDown, &b_Jet_pt_jerDown);
   fChain->SetBranchAddress("Jet_mass_jerDown", Jet_mass_jerDown, &b_Jet_mass_jerDown);
   fChain->SetBranchAddress("Jet_mass_jmrDown", Jet_mass_jmrDown, &b_Jet_mass_jmrDown);
   fChain->SetBranchAddress("Jet_mass_jmsDown", Jet_mass_jmsDown, &b_Jet_mass_jmsDown);
   fChain->SetBranchAddress("MET_pt_jerDown", &MET_pt_jerDown, &b_MET_pt_jerDown);
   fChain->SetBranchAddress("MET_phi_jerDown", &MET_phi_jerDown, &b_MET_phi_jerDown);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteStatDown", Jet_pt_jesAbsoluteStatDown, &b_Jet_pt_jesAbsoluteStatDown);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteStatDown", Jet_mass_jesAbsoluteStatDown, &b_Jet_mass_jesAbsoluteStatDown);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteStatDown", &MET_pt_jesAbsoluteStatDown, &b_MET_pt_jesAbsoluteStatDown);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteStatDown", &MET_phi_jesAbsoluteStatDown, &b_MET_phi_jesAbsoluteStatDown);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteScaleDown", Jet_pt_jesAbsoluteScaleDown, &b_Jet_pt_jesAbsoluteScaleDown);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteScaleDown", Jet_mass_jesAbsoluteScaleDown, &b_Jet_mass_jesAbsoluteScaleDown);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteScaleDown", &MET_pt_jesAbsoluteScaleDown, &b_MET_pt_jesAbsoluteScaleDown);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteScaleDown", &MET_phi_jesAbsoluteScaleDown, &b_MET_phi_jesAbsoluteScaleDown);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteFlavMapDown", Jet_pt_jesAbsoluteFlavMapDown, &b_Jet_pt_jesAbsoluteFlavMapDown);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteFlavMapDown", Jet_mass_jesAbsoluteFlavMapDown, &b_Jet_mass_jesAbsoluteFlavMapDown);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteFlavMapDown", &MET_pt_jesAbsoluteFlavMapDown, &b_MET_pt_jesAbsoluteFlavMapDown);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteFlavMapDown", &MET_phi_jesAbsoluteFlavMapDown, &b_MET_phi_jesAbsoluteFlavMapDown);
   fChain->SetBranchAddress("Jet_pt_jesAbsoluteMPFBiasDown", Jet_pt_jesAbsoluteMPFBiasDown, &b_Jet_pt_jesAbsoluteMPFBiasDown);
   fChain->SetBranchAddress("Jet_mass_jesAbsoluteMPFBiasDown", Jet_mass_jesAbsoluteMPFBiasDown, &b_Jet_mass_jesAbsoluteMPFBiasDown);
   fChain->SetBranchAddress("MET_pt_jesAbsoluteMPFBiasDown", &MET_pt_jesAbsoluteMPFBiasDown, &b_MET_pt_jesAbsoluteMPFBiasDown);
   fChain->SetBranchAddress("MET_phi_jesAbsoluteMPFBiasDown", &MET_phi_jesAbsoluteMPFBiasDown, &b_MET_phi_jesAbsoluteMPFBiasDown);
   fChain->SetBranchAddress("Jet_pt_jesFragmentationDown", Jet_pt_jesFragmentationDown, &b_Jet_pt_jesFragmentationDown);
   fChain->SetBranchAddress("Jet_mass_jesFragmentationDown", Jet_mass_jesFragmentationDown, &b_Jet_mass_jesFragmentationDown);
   fChain->SetBranchAddress("MET_pt_jesFragmentationDown", &MET_pt_jesFragmentationDown, &b_MET_pt_jesFragmentationDown);
   fChain->SetBranchAddress("MET_phi_jesFragmentationDown", &MET_phi_jesFragmentationDown, &b_MET_phi_jesFragmentationDown);
   fChain->SetBranchAddress("Jet_pt_jesSinglePionECALDown", Jet_pt_jesSinglePionECALDown, &b_Jet_pt_jesSinglePionECALDown);
   fChain->SetBranchAddress("Jet_mass_jesSinglePionECALDown", Jet_mass_jesSinglePionECALDown, &b_Jet_mass_jesSinglePionECALDown);
   fChain->SetBranchAddress("MET_pt_jesSinglePionECALDown", &MET_pt_jesSinglePionECALDown, &b_MET_pt_jesSinglePionECALDown);
   fChain->SetBranchAddress("MET_phi_jesSinglePionECALDown", &MET_phi_jesSinglePionECALDown, &b_MET_phi_jesSinglePionECALDown);
   fChain->SetBranchAddress("Jet_pt_jesSinglePionHCALDown", Jet_pt_jesSinglePionHCALDown, &b_Jet_pt_jesSinglePionHCALDown);
   fChain->SetBranchAddress("Jet_mass_jesSinglePionHCALDown", Jet_mass_jesSinglePionHCALDown, &b_Jet_mass_jesSinglePionHCALDown);
   fChain->SetBranchAddress("MET_pt_jesSinglePionHCALDown", &MET_pt_jesSinglePionHCALDown, &b_MET_pt_jesSinglePionHCALDown);
   fChain->SetBranchAddress("MET_phi_jesSinglePionHCALDown", &MET_phi_jesSinglePionHCALDown, &b_MET_phi_jesSinglePionHCALDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorQCDDown", Jet_pt_jesFlavorQCDDown, &b_Jet_pt_jesFlavorQCDDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorQCDDown", Jet_mass_jesFlavorQCDDown, &b_Jet_mass_jesFlavorQCDDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorQCDDown", &MET_pt_jesFlavorQCDDown, &b_MET_pt_jesFlavorQCDDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorQCDDown", &MET_phi_jesFlavorQCDDown, &b_MET_phi_jesFlavorQCDDown);
   fChain->SetBranchAddress("Jet_pt_jesTimePtEtaDown", Jet_pt_jesTimePtEtaDown, &b_Jet_pt_jesTimePtEtaDown);
   fChain->SetBranchAddress("Jet_mass_jesTimePtEtaDown", Jet_mass_jesTimePtEtaDown, &b_Jet_mass_jesTimePtEtaDown);
   fChain->SetBranchAddress("MET_pt_jesTimePtEtaDown", &MET_pt_jesTimePtEtaDown, &b_MET_pt_jesTimePtEtaDown);
   fChain->SetBranchAddress("MET_phi_jesTimePtEtaDown", &MET_phi_jesTimePtEtaDown, &b_MET_phi_jesTimePtEtaDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativeJEREC1Down", Jet_pt_jesRelativeJEREC1Down, &b_Jet_pt_jesRelativeJEREC1Down);
   fChain->SetBranchAddress("Jet_mass_jesRelativeJEREC1Down", Jet_mass_jesRelativeJEREC1Down, &b_Jet_mass_jesRelativeJEREC1Down);
   fChain->SetBranchAddress("MET_pt_jesRelativeJEREC1Down", &MET_pt_jesRelativeJEREC1Down, &b_MET_pt_jesRelativeJEREC1Down);
   fChain->SetBranchAddress("MET_phi_jesRelativeJEREC1Down", &MET_phi_jesRelativeJEREC1Down, &b_MET_phi_jesRelativeJEREC1Down);
   fChain->SetBranchAddress("Jet_pt_jesRelativeJEREC2Down", Jet_pt_jesRelativeJEREC2Down, &b_Jet_pt_jesRelativeJEREC2Down);
   fChain->SetBranchAddress("Jet_mass_jesRelativeJEREC2Down", Jet_mass_jesRelativeJEREC2Down, &b_Jet_mass_jesRelativeJEREC2Down);
   fChain->SetBranchAddress("MET_pt_jesRelativeJEREC2Down", &MET_pt_jesRelativeJEREC2Down, &b_MET_pt_jesRelativeJEREC2Down);
   fChain->SetBranchAddress("MET_phi_jesRelativeJEREC2Down", &MET_phi_jesRelativeJEREC2Down, &b_MET_phi_jesRelativeJEREC2Down);
   fChain->SetBranchAddress("Jet_pt_jesRelativeJERHFDown", Jet_pt_jesRelativeJERHFDown, &b_Jet_pt_jesRelativeJERHFDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativeJERHFDown", Jet_mass_jesRelativeJERHFDown, &b_Jet_mass_jesRelativeJERHFDown);
   fChain->SetBranchAddress("MET_pt_jesRelativeJERHFDown", &MET_pt_jesRelativeJERHFDown, &b_MET_pt_jesRelativeJERHFDown);
   fChain->SetBranchAddress("MET_phi_jesRelativeJERHFDown", &MET_phi_jesRelativeJERHFDown, &b_MET_phi_jesRelativeJERHFDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtBBDown", Jet_pt_jesRelativePtBBDown, &b_Jet_pt_jesRelativePtBBDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtBBDown", Jet_mass_jesRelativePtBBDown, &b_Jet_mass_jesRelativePtBBDown);
   fChain->SetBranchAddress("MET_pt_jesRelativePtBBDown", &MET_pt_jesRelativePtBBDown, &b_MET_pt_jesRelativePtBBDown);
   fChain->SetBranchAddress("MET_phi_jesRelativePtBBDown", &MET_phi_jesRelativePtBBDown, &b_MET_phi_jesRelativePtBBDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtEC1Down", Jet_pt_jesRelativePtEC1Down, &b_Jet_pt_jesRelativePtEC1Down);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtEC1Down", Jet_mass_jesRelativePtEC1Down, &b_Jet_mass_jesRelativePtEC1Down);
   fChain->SetBranchAddress("MET_pt_jesRelativePtEC1Down", &MET_pt_jesRelativePtEC1Down, &b_MET_pt_jesRelativePtEC1Down);
   fChain->SetBranchAddress("MET_phi_jesRelativePtEC1Down", &MET_phi_jesRelativePtEC1Down, &b_MET_phi_jesRelativePtEC1Down);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtEC2Down", Jet_pt_jesRelativePtEC2Down, &b_Jet_pt_jesRelativePtEC2Down);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtEC2Down", Jet_mass_jesRelativePtEC2Down, &b_Jet_mass_jesRelativePtEC2Down);
   fChain->SetBranchAddress("MET_pt_jesRelativePtEC2Down", &MET_pt_jesRelativePtEC2Down, &b_MET_pt_jesRelativePtEC2Down);
   fChain->SetBranchAddress("MET_phi_jesRelativePtEC2Down", &MET_phi_jesRelativePtEC2Down, &b_MET_phi_jesRelativePtEC2Down);
   fChain->SetBranchAddress("Jet_pt_jesRelativePtHFDown", Jet_pt_jesRelativePtHFDown, &b_Jet_pt_jesRelativePtHFDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativePtHFDown", Jet_mass_jesRelativePtHFDown, &b_Jet_mass_jesRelativePtHFDown);
   fChain->SetBranchAddress("MET_pt_jesRelativePtHFDown", &MET_pt_jesRelativePtHFDown, &b_MET_pt_jesRelativePtHFDown);
   fChain->SetBranchAddress("MET_phi_jesRelativePtHFDown", &MET_phi_jesRelativePtHFDown, &b_MET_phi_jesRelativePtHFDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativeBalDown", Jet_pt_jesRelativeBalDown, &b_Jet_pt_jesRelativeBalDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativeBalDown", Jet_mass_jesRelativeBalDown, &b_Jet_mass_jesRelativeBalDown);
   fChain->SetBranchAddress("MET_pt_jesRelativeBalDown", &MET_pt_jesRelativeBalDown, &b_MET_pt_jesRelativeBalDown);
   fChain->SetBranchAddress("MET_phi_jesRelativeBalDown", &MET_phi_jesRelativeBalDown, &b_MET_phi_jesRelativeBalDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativeFSRDown", Jet_pt_jesRelativeFSRDown, &b_Jet_pt_jesRelativeFSRDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativeFSRDown", Jet_mass_jesRelativeFSRDown, &b_Jet_mass_jesRelativeFSRDown);
   fChain->SetBranchAddress("MET_pt_jesRelativeFSRDown", &MET_pt_jesRelativeFSRDown, &b_MET_pt_jesRelativeFSRDown);
   fChain->SetBranchAddress("MET_phi_jesRelativeFSRDown", &MET_phi_jesRelativeFSRDown, &b_MET_phi_jesRelativeFSRDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativeStatFSRDown", Jet_pt_jesRelativeStatFSRDown, &b_Jet_pt_jesRelativeStatFSRDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativeStatFSRDown", Jet_mass_jesRelativeStatFSRDown, &b_Jet_mass_jesRelativeStatFSRDown);
   fChain->SetBranchAddress("MET_pt_jesRelativeStatFSRDown", &MET_pt_jesRelativeStatFSRDown, &b_MET_pt_jesRelativeStatFSRDown);
   fChain->SetBranchAddress("MET_phi_jesRelativeStatFSRDown", &MET_phi_jesRelativeStatFSRDown, &b_MET_phi_jesRelativeStatFSRDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativeStatECDown", Jet_pt_jesRelativeStatECDown, &b_Jet_pt_jesRelativeStatECDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativeStatECDown", Jet_mass_jesRelativeStatECDown, &b_Jet_mass_jesRelativeStatECDown);
   fChain->SetBranchAddress("MET_pt_jesRelativeStatECDown", &MET_pt_jesRelativeStatECDown, &b_MET_pt_jesRelativeStatECDown);
   fChain->SetBranchAddress("MET_phi_jesRelativeStatECDown", &MET_phi_jesRelativeStatECDown, &b_MET_phi_jesRelativeStatECDown);
   fChain->SetBranchAddress("Jet_pt_jesRelativeStatHFDown", Jet_pt_jesRelativeStatHFDown, &b_Jet_pt_jesRelativeStatHFDown);
   fChain->SetBranchAddress("Jet_mass_jesRelativeStatHFDown", Jet_mass_jesRelativeStatHFDown, &b_Jet_mass_jesRelativeStatHFDown);
   fChain->SetBranchAddress("MET_pt_jesRelativeStatHFDown", &MET_pt_jesRelativeStatHFDown, &b_MET_pt_jesRelativeStatHFDown);
   fChain->SetBranchAddress("MET_phi_jesRelativeStatHFDown", &MET_phi_jesRelativeStatHFDown, &b_MET_phi_jesRelativeStatHFDown);
   fChain->SetBranchAddress("Jet_pt_jesPileUpDataMCDown", Jet_pt_jesPileUpDataMCDown, &b_Jet_pt_jesPileUpDataMCDown);
   fChain->SetBranchAddress("Jet_mass_jesPileUpDataMCDown", Jet_mass_jesPileUpDataMCDown, &b_Jet_mass_jesPileUpDataMCDown);
   fChain->SetBranchAddress("MET_pt_jesPileUpDataMCDown", &MET_pt_jesPileUpDataMCDown, &b_MET_pt_jesPileUpDataMCDown);
   fChain->SetBranchAddress("MET_phi_jesPileUpDataMCDown", &MET_phi_jesPileUpDataMCDown, &b_MET_phi_jesPileUpDataMCDown);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtRefDown", Jet_pt_jesPileUpPtRefDown, &b_Jet_pt_jesPileUpPtRefDown);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtRefDown", Jet_mass_jesPileUpPtRefDown, &b_Jet_mass_jesPileUpPtRefDown);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtRefDown", &MET_pt_jesPileUpPtRefDown, &b_MET_pt_jesPileUpPtRefDown);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtRefDown", &MET_phi_jesPileUpPtRefDown, &b_MET_phi_jesPileUpPtRefDown);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtBBDown", Jet_pt_jesPileUpPtBBDown, &b_Jet_pt_jesPileUpPtBBDown);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtBBDown", Jet_mass_jesPileUpPtBBDown, &b_Jet_mass_jesPileUpPtBBDown);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtBBDown", &MET_pt_jesPileUpPtBBDown, &b_MET_pt_jesPileUpPtBBDown);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtBBDown", &MET_phi_jesPileUpPtBBDown, &b_MET_phi_jesPileUpPtBBDown);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtEC1Down", Jet_pt_jesPileUpPtEC1Down, &b_Jet_pt_jesPileUpPtEC1Down);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtEC1Down", Jet_mass_jesPileUpPtEC1Down, &b_Jet_mass_jesPileUpPtEC1Down);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtEC1Down", &MET_pt_jesPileUpPtEC1Down, &b_MET_pt_jesPileUpPtEC1Down);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtEC1Down", &MET_phi_jesPileUpPtEC1Down, &b_MET_phi_jesPileUpPtEC1Down);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtEC2Down", Jet_pt_jesPileUpPtEC2Down, &b_Jet_pt_jesPileUpPtEC2Down);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtEC2Down", Jet_mass_jesPileUpPtEC2Down, &b_Jet_mass_jesPileUpPtEC2Down);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtEC2Down", &MET_pt_jesPileUpPtEC2Down, &b_MET_pt_jesPileUpPtEC2Down);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtEC2Down", &MET_phi_jesPileUpPtEC2Down, &b_MET_phi_jesPileUpPtEC2Down);
   fChain->SetBranchAddress("Jet_pt_jesPileUpPtHFDown", Jet_pt_jesPileUpPtHFDown, &b_Jet_pt_jesPileUpPtHFDown);
   fChain->SetBranchAddress("Jet_mass_jesPileUpPtHFDown", Jet_mass_jesPileUpPtHFDown, &b_Jet_mass_jesPileUpPtHFDown);
   fChain->SetBranchAddress("MET_pt_jesPileUpPtHFDown", &MET_pt_jesPileUpPtHFDown, &b_MET_pt_jesPileUpPtHFDown);
   fChain->SetBranchAddress("MET_phi_jesPileUpPtHFDown", &MET_phi_jesPileUpPtHFDown, &b_MET_phi_jesPileUpPtHFDown);
   fChain->SetBranchAddress("Jet_pt_jesPileUpMuZeroDown", Jet_pt_jesPileUpMuZeroDown, &b_Jet_pt_jesPileUpMuZeroDown);
   fChain->SetBranchAddress("Jet_mass_jesPileUpMuZeroDown", Jet_mass_jesPileUpMuZeroDown, &b_Jet_mass_jesPileUpMuZeroDown);
   fChain->SetBranchAddress("MET_pt_jesPileUpMuZeroDown", &MET_pt_jesPileUpMuZeroDown, &b_MET_pt_jesPileUpMuZeroDown);
   fChain->SetBranchAddress("MET_phi_jesPileUpMuZeroDown", &MET_phi_jesPileUpMuZeroDown, &b_MET_phi_jesPileUpMuZeroDown);
   fChain->SetBranchAddress("Jet_pt_jesPileUpEnvelopeDown", Jet_pt_jesPileUpEnvelopeDown, &b_Jet_pt_jesPileUpEnvelopeDown);
   fChain->SetBranchAddress("Jet_mass_jesPileUpEnvelopeDown", Jet_mass_jesPileUpEnvelopeDown, &b_Jet_mass_jesPileUpEnvelopeDown);
   fChain->SetBranchAddress("MET_pt_jesPileUpEnvelopeDown", &MET_pt_jesPileUpEnvelopeDown, &b_MET_pt_jesPileUpEnvelopeDown);
   fChain->SetBranchAddress("MET_phi_jesPileUpEnvelopeDown", &MET_phi_jesPileUpEnvelopeDown, &b_MET_phi_jesPileUpEnvelopeDown);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalPileUpDown", Jet_pt_jesSubTotalPileUpDown, &b_Jet_pt_jesSubTotalPileUpDown);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalPileUpDown", Jet_mass_jesSubTotalPileUpDown, &b_Jet_mass_jesSubTotalPileUpDown);
   fChain->SetBranchAddress("MET_pt_jesSubTotalPileUpDown", &MET_pt_jesSubTotalPileUpDown, &b_MET_pt_jesSubTotalPileUpDown);
   fChain->SetBranchAddress("MET_phi_jesSubTotalPileUpDown", &MET_phi_jesSubTotalPileUpDown, &b_MET_phi_jesSubTotalPileUpDown);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalRelativeDown", Jet_pt_jesSubTotalRelativeDown, &b_Jet_pt_jesSubTotalRelativeDown);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalRelativeDown", Jet_mass_jesSubTotalRelativeDown, &b_Jet_mass_jesSubTotalRelativeDown);
   fChain->SetBranchAddress("MET_pt_jesSubTotalRelativeDown", &MET_pt_jesSubTotalRelativeDown, &b_MET_pt_jesSubTotalRelativeDown);
   fChain->SetBranchAddress("MET_phi_jesSubTotalRelativeDown", &MET_phi_jesSubTotalRelativeDown, &b_MET_phi_jesSubTotalRelativeDown);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalPtDown", Jet_pt_jesSubTotalPtDown, &b_Jet_pt_jesSubTotalPtDown);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalPtDown", Jet_mass_jesSubTotalPtDown, &b_Jet_mass_jesSubTotalPtDown);
   fChain->SetBranchAddress("MET_pt_jesSubTotalPtDown", &MET_pt_jesSubTotalPtDown, &b_MET_pt_jesSubTotalPtDown);
   fChain->SetBranchAddress("MET_phi_jesSubTotalPtDown", &MET_phi_jesSubTotalPtDown, &b_MET_phi_jesSubTotalPtDown);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalScaleDown", Jet_pt_jesSubTotalScaleDown, &b_Jet_pt_jesSubTotalScaleDown);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalScaleDown", Jet_mass_jesSubTotalScaleDown, &b_Jet_mass_jesSubTotalScaleDown);
   fChain->SetBranchAddress("MET_pt_jesSubTotalScaleDown", &MET_pt_jesSubTotalScaleDown, &b_MET_pt_jesSubTotalScaleDown);
   fChain->SetBranchAddress("MET_phi_jesSubTotalScaleDown", &MET_phi_jesSubTotalScaleDown, &b_MET_phi_jesSubTotalScaleDown);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalAbsoluteDown", Jet_pt_jesSubTotalAbsoluteDown, &b_Jet_pt_jesSubTotalAbsoluteDown);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalAbsoluteDown", Jet_mass_jesSubTotalAbsoluteDown, &b_Jet_mass_jesSubTotalAbsoluteDown);
   fChain->SetBranchAddress("MET_pt_jesSubTotalAbsoluteDown", &MET_pt_jesSubTotalAbsoluteDown, &b_MET_pt_jesSubTotalAbsoluteDown);
   fChain->SetBranchAddress("MET_phi_jesSubTotalAbsoluteDown", &MET_phi_jesSubTotalAbsoluteDown, &b_MET_phi_jesSubTotalAbsoluteDown);
   fChain->SetBranchAddress("Jet_pt_jesSubTotalMCDown", Jet_pt_jesSubTotalMCDown, &b_Jet_pt_jesSubTotalMCDown);
   fChain->SetBranchAddress("Jet_mass_jesSubTotalMCDown", Jet_mass_jesSubTotalMCDown, &b_Jet_mass_jesSubTotalMCDown);
   fChain->SetBranchAddress("MET_pt_jesSubTotalMCDown", &MET_pt_jesSubTotalMCDown, &b_MET_pt_jesSubTotalMCDown);
   fChain->SetBranchAddress("MET_phi_jesSubTotalMCDown", &MET_phi_jesSubTotalMCDown, &b_MET_phi_jesSubTotalMCDown);
   fChain->SetBranchAddress("Jet_pt_jesTotalDown", Jet_pt_jesTotalDown, &b_Jet_pt_jesTotalDown);
   fChain->SetBranchAddress("Jet_mass_jesTotalDown", Jet_mass_jesTotalDown, &b_Jet_mass_jesTotalDown);
   fChain->SetBranchAddress("MET_pt_jesTotalDown", &MET_pt_jesTotalDown, &b_MET_pt_jesTotalDown);
   fChain->SetBranchAddress("MET_phi_jesTotalDown", &MET_phi_jesTotalDown, &b_MET_phi_jesTotalDown);
   fChain->SetBranchAddress("Jet_pt_jesTotalNoFlavorDown", Jet_pt_jesTotalNoFlavorDown, &b_Jet_pt_jesTotalNoFlavorDown);
   fChain->SetBranchAddress("Jet_mass_jesTotalNoFlavorDown", Jet_mass_jesTotalNoFlavorDown, &b_Jet_mass_jesTotalNoFlavorDown);
   fChain->SetBranchAddress("MET_pt_jesTotalNoFlavorDown", &MET_pt_jesTotalNoFlavorDown, &b_MET_pt_jesTotalNoFlavorDown);
   fChain->SetBranchAddress("MET_phi_jesTotalNoFlavorDown", &MET_phi_jesTotalNoFlavorDown, &b_MET_phi_jesTotalNoFlavorDown);
   fChain->SetBranchAddress("Jet_pt_jesTotalNoTimeDown", Jet_pt_jesTotalNoTimeDown, &b_Jet_pt_jesTotalNoTimeDown);
   fChain->SetBranchAddress("Jet_mass_jesTotalNoTimeDown", Jet_mass_jesTotalNoTimeDown, &b_Jet_mass_jesTotalNoTimeDown);
   fChain->SetBranchAddress("MET_pt_jesTotalNoTimeDown", &MET_pt_jesTotalNoTimeDown, &b_MET_pt_jesTotalNoTimeDown);
   fChain->SetBranchAddress("MET_phi_jesTotalNoTimeDown", &MET_phi_jesTotalNoTimeDown, &b_MET_phi_jesTotalNoTimeDown);
   fChain->SetBranchAddress("Jet_pt_jesTotalNoFlavorNoTimeDown", Jet_pt_jesTotalNoFlavorNoTimeDown, &b_Jet_pt_jesTotalNoFlavorNoTimeDown);
   fChain->SetBranchAddress("Jet_mass_jesTotalNoFlavorNoTimeDown", Jet_mass_jesTotalNoFlavorNoTimeDown, &b_Jet_mass_jesTotalNoFlavorNoTimeDown);
   fChain->SetBranchAddress("MET_pt_jesTotalNoFlavorNoTimeDown", &MET_pt_jesTotalNoFlavorNoTimeDown, &b_MET_pt_jesTotalNoFlavorNoTimeDown);
   fChain->SetBranchAddress("MET_phi_jesTotalNoFlavorNoTimeDown", &MET_phi_jesTotalNoFlavorNoTimeDown, &b_MET_phi_jesTotalNoFlavorNoTimeDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorZJetDown", Jet_pt_jesFlavorZJetDown, &b_Jet_pt_jesFlavorZJetDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorZJetDown", Jet_mass_jesFlavorZJetDown, &b_Jet_mass_jesFlavorZJetDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorZJetDown", &MET_pt_jesFlavorZJetDown, &b_MET_pt_jesFlavorZJetDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorZJetDown", &MET_phi_jesFlavorZJetDown, &b_MET_phi_jesFlavorZJetDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPhotonJetDown", Jet_pt_jesFlavorPhotonJetDown, &b_Jet_pt_jesFlavorPhotonJetDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPhotonJetDown", Jet_mass_jesFlavorPhotonJetDown, &b_Jet_mass_jesFlavorPhotonJetDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorPhotonJetDown", &MET_pt_jesFlavorPhotonJetDown, &b_MET_pt_jesFlavorPhotonJetDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorPhotonJetDown", &MET_phi_jesFlavorPhotonJetDown, &b_MET_phi_jesFlavorPhotonJetDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureGluonDown", Jet_pt_jesFlavorPureGluonDown, &b_Jet_pt_jesFlavorPureGluonDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureGluonDown", Jet_mass_jesFlavorPureGluonDown, &b_Jet_mass_jesFlavorPureGluonDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureGluonDown", &MET_pt_jesFlavorPureGluonDown, &b_MET_pt_jesFlavorPureGluonDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureGluonDown", &MET_phi_jesFlavorPureGluonDown, &b_MET_phi_jesFlavorPureGluonDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureQuarkDown", Jet_pt_jesFlavorPureQuarkDown, &b_Jet_pt_jesFlavorPureQuarkDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureQuarkDown", Jet_mass_jesFlavorPureQuarkDown, &b_Jet_mass_jesFlavorPureQuarkDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureQuarkDown", &MET_pt_jesFlavorPureQuarkDown, &b_MET_pt_jesFlavorPureQuarkDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureQuarkDown", &MET_phi_jesFlavorPureQuarkDown, &b_MET_phi_jesFlavorPureQuarkDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureCharmDown", Jet_pt_jesFlavorPureCharmDown, &b_Jet_pt_jesFlavorPureCharmDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureCharmDown", Jet_mass_jesFlavorPureCharmDown, &b_Jet_mass_jesFlavorPureCharmDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureCharmDown", &MET_pt_jesFlavorPureCharmDown, &b_MET_pt_jesFlavorPureCharmDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureCharmDown", &MET_phi_jesFlavorPureCharmDown, &b_MET_phi_jesFlavorPureCharmDown);
   fChain->SetBranchAddress("Jet_pt_jesFlavorPureBottomDown", Jet_pt_jesFlavorPureBottomDown, &b_Jet_pt_jesFlavorPureBottomDown);
   fChain->SetBranchAddress("Jet_mass_jesFlavorPureBottomDown", Jet_mass_jesFlavorPureBottomDown, &b_Jet_mass_jesFlavorPureBottomDown);
   fChain->SetBranchAddress("MET_pt_jesFlavorPureBottomDown", &MET_pt_jesFlavorPureBottomDown, &b_MET_pt_jesFlavorPureBottomDown);
   fChain->SetBranchAddress("MET_phi_jesFlavorPureBottomDown", &MET_phi_jesFlavorPureBottomDown, &b_MET_phi_jesFlavorPureBottomDown);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunBCDDown", Jet_pt_jesTimeRunBCDDown, &b_Jet_pt_jesTimeRunBCDDown);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunBCDDown", Jet_mass_jesTimeRunBCDDown, &b_Jet_mass_jesTimeRunBCDDown);
   fChain->SetBranchAddress("MET_pt_jesTimeRunBCDDown", &MET_pt_jesTimeRunBCDDown, &b_MET_pt_jesTimeRunBCDDown);
   fChain->SetBranchAddress("MET_phi_jesTimeRunBCDDown", &MET_phi_jesTimeRunBCDDown, &b_MET_phi_jesTimeRunBCDDown);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunEFDown", Jet_pt_jesTimeRunEFDown, &b_Jet_pt_jesTimeRunEFDown);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunEFDown", Jet_mass_jesTimeRunEFDown, &b_Jet_mass_jesTimeRunEFDown);
   fChain->SetBranchAddress("MET_pt_jesTimeRunEFDown", &MET_pt_jesTimeRunEFDown, &b_MET_pt_jesTimeRunEFDown);
   fChain->SetBranchAddress("MET_phi_jesTimeRunEFDown", &MET_phi_jesTimeRunEFDown, &b_MET_phi_jesTimeRunEFDown);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunGDown", Jet_pt_jesTimeRunGDown, &b_Jet_pt_jesTimeRunGDown);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunGDown", Jet_mass_jesTimeRunGDown, &b_Jet_mass_jesTimeRunGDown);
   fChain->SetBranchAddress("MET_pt_jesTimeRunGDown", &MET_pt_jesTimeRunGDown, &b_MET_pt_jesTimeRunGDown);
   fChain->SetBranchAddress("MET_phi_jesTimeRunGDown", &MET_phi_jesTimeRunGDown, &b_MET_phi_jesTimeRunGDown);
   fChain->SetBranchAddress("Jet_pt_jesTimeRunHDown", Jet_pt_jesTimeRunHDown, &b_Jet_pt_jesTimeRunHDown);
   fChain->SetBranchAddress("Jet_mass_jesTimeRunHDown", Jet_mass_jesTimeRunHDown, &b_Jet_mass_jesTimeRunHDown);
   fChain->SetBranchAddress("MET_pt_jesTimeRunHDown", &MET_pt_jesTimeRunHDown, &b_MET_pt_jesTimeRunHDown);
   fChain->SetBranchAddress("MET_phi_jesTimeRunHDown", &MET_phi_jesTimeRunHDown, &b_MET_phi_jesTimeRunHDown);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupMPFInSituDown", Jet_pt_jesCorrelationGroupMPFInSituDown, &b_Jet_pt_jesCorrelationGroupMPFInSituDown);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupMPFInSituDown", Jet_mass_jesCorrelationGroupMPFInSituDown, &b_Jet_mass_jesCorrelationGroupMPFInSituDown);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupMPFInSituDown", &MET_pt_jesCorrelationGroupMPFInSituDown, &b_MET_pt_jesCorrelationGroupMPFInSituDown);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupMPFInSituDown", &MET_phi_jesCorrelationGroupMPFInSituDown, &b_MET_phi_jesCorrelationGroupMPFInSituDown);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupIntercalibrationDown", Jet_pt_jesCorrelationGroupIntercalibrationDown, &b_Jet_pt_jesCorrelationGroupIntercalibrationDown);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupIntercalibrationDown", Jet_mass_jesCorrelationGroupIntercalibrationDown, &b_Jet_mass_jesCorrelationGroupIntercalibrationDown);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupIntercalibrationDown", &MET_pt_jesCorrelationGroupIntercalibrationDown, &b_MET_pt_jesCorrelationGroupIntercalibrationDown);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupIntercalibrationDown", &MET_phi_jesCorrelationGroupIntercalibrationDown, &b_MET_phi_jesCorrelationGroupIntercalibrationDown);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupbJESDown", Jet_pt_jesCorrelationGroupbJESDown, &b_Jet_pt_jesCorrelationGroupbJESDown);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupbJESDown", Jet_mass_jesCorrelationGroupbJESDown, &b_Jet_mass_jesCorrelationGroupbJESDown);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupbJESDown", &MET_pt_jesCorrelationGroupbJESDown, &b_MET_pt_jesCorrelationGroupbJESDown);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupbJESDown", &MET_phi_jesCorrelationGroupbJESDown, &b_MET_phi_jesCorrelationGroupbJESDown);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupFlavorDown", Jet_pt_jesCorrelationGroupFlavorDown, &b_Jet_pt_jesCorrelationGroupFlavorDown);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupFlavorDown", Jet_mass_jesCorrelationGroupFlavorDown, &b_Jet_mass_jesCorrelationGroupFlavorDown);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupFlavorDown", &MET_pt_jesCorrelationGroupFlavorDown, &b_MET_pt_jesCorrelationGroupFlavorDown);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupFlavorDown", &MET_phi_jesCorrelationGroupFlavorDown, &b_MET_phi_jesCorrelationGroupFlavorDown);
   fChain->SetBranchAddress("Jet_pt_jesCorrelationGroupUncorrelatedDown", Jet_pt_jesCorrelationGroupUncorrelatedDown, &b_Jet_pt_jesCorrelationGroupUncorrelatedDown);
   fChain->SetBranchAddress("Jet_mass_jesCorrelationGroupUncorrelatedDown", Jet_mass_jesCorrelationGroupUncorrelatedDown, &b_Jet_mass_jesCorrelationGroupUncorrelatedDown);
   fChain->SetBranchAddress("MET_pt_jesCorrelationGroupUncorrelatedDown", &MET_pt_jesCorrelationGroupUncorrelatedDown, &b_MET_pt_jesCorrelationGroupUncorrelatedDown);
   fChain->SetBranchAddress("MET_phi_jesCorrelationGroupUncorrelatedDown", &MET_phi_jesCorrelationGroupUncorrelatedDown, &b_MET_phi_jesCorrelationGroupUncorrelatedDown);
   fChain->SetBranchAddress("MET_pt_unclustEnDown", &MET_pt_unclustEnDown, &b_MET_pt_unclustEnDown);
   fChain->SetBranchAddress("MET_phi_unclustEnDown", &MET_phi_unclustEnDown, &b_MET_phi_unclustEnDown);
   fChain->SetBranchAddress("Muon_pt_corrected", Muon_pt_corrected, &b_Muon_pt_corrected);
   fChain->SetBranchAddress("MHT_pt", &MHT_pt, &b_MHT_pt);
   fChain->SetBranchAddress("MHT_phi", &MHT_phi, &b_MHT_phi);
   fChain->SetBranchAddress("Jet_mhtCleaning", Jet_mhtCleaning, &b_Jet_mhtCleaning);
   fChain->SetBranchAddress("Jet_btagSF", Jet_btagSF, &b_Jet_btagSF);
   fChain->SetBranchAddress("Jet_btagSF_up", Jet_btagSF_up, &b_Jet_btagSF_up);
   fChain->SetBranchAddress("Jet_btagSF_down", Jet_btagSF_down, &b_Jet_btagSF_down);
   fChain->SetBranchAddress("Jet_btagSF_shape", Jet_btagSF_shape, &b_Jet_btagSF_shape);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_jes", Jet_btagSF_shape_up_jes, &b_Jet_btagSF_shape_up_jes);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_jes", Jet_btagSF_shape_down_jes, &b_Jet_btagSF_shape_down_jes);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_lf", Jet_btagSF_shape_up_lf, &b_Jet_btagSF_shape_up_lf);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_lf", Jet_btagSF_shape_down_lf, &b_Jet_btagSF_shape_down_lf);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_hf", Jet_btagSF_shape_up_hf, &b_Jet_btagSF_shape_up_hf);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_hf", Jet_btagSF_shape_down_hf, &b_Jet_btagSF_shape_down_hf);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_hfstats1", Jet_btagSF_shape_up_hfstats1, &b_Jet_btagSF_shape_up_hfstats1);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_hfstats1", Jet_btagSF_shape_down_hfstats1, &b_Jet_btagSF_shape_down_hfstats1);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_hfstats2", Jet_btagSF_shape_up_hfstats2, &b_Jet_btagSF_shape_up_hfstats2);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_hfstats2", Jet_btagSF_shape_down_hfstats2, &b_Jet_btagSF_shape_down_hfstats2);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_lfstats1", Jet_btagSF_shape_up_lfstats1, &b_Jet_btagSF_shape_up_lfstats1);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_lfstats1", Jet_btagSF_shape_down_lfstats1, &b_Jet_btagSF_shape_down_lfstats1);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_lfstats2", Jet_btagSF_shape_up_lfstats2, &b_Jet_btagSF_shape_up_lfstats2);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_lfstats2", Jet_btagSF_shape_down_lfstats2, &b_Jet_btagSF_shape_down_lfstats2);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_cferr1", Jet_btagSF_shape_up_cferr1, &b_Jet_btagSF_shape_up_cferr1);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_cferr1", Jet_btagSF_shape_down_cferr1, &b_Jet_btagSF_shape_down_cferr1);
   fChain->SetBranchAddress("Jet_btagSF_shape_up_cferr2", Jet_btagSF_shape_up_cferr2, &b_Jet_btagSF_shape_up_cferr2);
   fChain->SetBranchAddress("Jet_btagSF_shape_down_cferr2", Jet_btagSF_shape_down_cferr2, &b_Jet_btagSF_shape_down_cferr2);
   fChain->SetBranchAddress("Vtype", &Vtype, &b_Vtype);
   fChain->SetBranchAddress("V_pt", &V_pt, &b_V_pt);
   fChain->SetBranchAddress("V_eta", &V_eta, &b_V_eta);
   fChain->SetBranchAddress("V_phi", &V_phi, &b_V_phi);
   fChain->SetBranchAddress("V_mass", &V_mass, &b_V_mass);
   fChain->SetBranchAddress("Jet_lepFilter", Jet_lepFilter, &b_Jet_lepFilter);
   fChain->SetBranchAddress("vLidx", vLidx, &b_vLidx);
   fChain->SetBranchAddress("hJidx", hJidx, &b_hJidx);
   fChain->SetBranchAddress("hJidxCMVA", hJidxCMVA, &b_hJidxCMVA);
   fChain->SetBranchAddress("HCMVA_pt", &HCMVA_pt, &b_HCMVA_pt);
   fChain->SetBranchAddress("HCMVA_eta", &HCMVA_eta, &b_HCMVA_eta);
   fChain->SetBranchAddress("HCMVA_phi", &HCMVA_phi, &b_HCMVA_phi);
   fChain->SetBranchAddress("HCMVA_mass", &HCMVA_mass, &b_HCMVA_mass);
   fChain->SetBranchAddress("HFSR_pt", &HFSR_pt, &b_HFSR_pt);
   fChain->SetBranchAddress("HFSR_eta", &HFSR_eta, &b_HFSR_eta);
   fChain->SetBranchAddress("HFSR_phi", &HFSR_phi, &b_HFSR_phi);
   fChain->SetBranchAddress("HFSR_mass", &HFSR_mass, &b_HFSR_mass);
   fChain->SetBranchAddress("SA_Ht", &SA_Ht, &b_SA_Ht);
   fChain->SetBranchAddress("SA5", &SA5, &b_SA5);
   fChain->SetBranchAddress("Jet_Pt", Jet_Pt, &b_Jet_Pt);
   fChain->SetBranchAddress("Jet_PtReg", Jet_PtReg, &b_Jet_PtReg);
   fChain->SetBranchAddress("MET_Pt", &MET_Pt, &b_MET_Pt);
   fChain->SetBranchAddress("MET_Phi", &MET_Phi, &b_MET_Phi);
   fChain->SetBranchAddress("Pt_fjidx", &Pt_fjidx, &b_Pt_fjidx);
   fChain->SetBranchAddress("Msd_fjidx", &Msd_fjidx, &b_Msd_fjidx);
   fChain->SetBranchAddress("Hbb_fjidx", &Hbb_fjidx, &b_Hbb_fjidx);
   fChain->SetBranchAddress("SAptfj_HT", &SAptfj_HT, &b_SAptfj_HT);
   fChain->SetBranchAddress("SAptfj5", &SAptfj5, &b_SAptfj5);
   fChain->SetBranchAddress("SAmfj_HT", &SAmfj_HT, &b_SAmfj_HT);
   fChain->SetBranchAddress("SAmfj5", &SAmfj5, &b_SAmfj5);
   fChain->SetBranchAddress("SAhbbfj_HT", &SAhbbfj_HT, &b_SAhbbfj_HT);
   fChain->SetBranchAddress("SAhbbfj5", &SAhbbfj5, &b_SAhbbfj5);
   fChain->SetBranchAddress("nVMuonIdx", &nVMuonIdx, &b_nVMuonIdx);
   fChain->SetBranchAddress("nVElectronIdx", &nVElectronIdx, &b_nVElectronIdx);
   fChain->SetBranchAddress("VMuonIdx", VMuonIdx, &b_VMuonIdx);
   fChain->SetBranchAddress("VElectronIdx", VElectronIdx, &b_VElectronIdx);
   fChain->SetBranchAddress("nVetoLeptons", &nVetoLeptons, &b_nVetoLeptons);
   fChain->SetBranchAddress("nAddLeptons", &nAddLeptons, &b_nAddLeptons);
   fChain->SetBranchAddress("TTW", &TTW, &b_TTW);
   fChain->SetBranchAddress("weight_SF_TightID", weight_SF_TightID, &b_weight_SF_TightID);
   fChain->SetBranchAddress("weight_SF_TightISO", weight_SF_TightISO, &b_weight_SF_TightISO);
   fChain->SetBranchAddress("weight_SF_TightIDnISO", weight_SF_TightIDnISO, &b_weight_SF_TightIDnISO);
   fChain->SetBranchAddress("weight_SF_TRK", weight_SF_TRK, &b_weight_SF_TRK);
   fChain->SetBranchAddress("weight_SF_Lepton", weight_SF_Lepton, &b_weight_SF_Lepton);
   fChain->SetBranchAddress("eTrigSFWeight_singleEle80", eTrigSFWeight_singleEle80, &b_eTrigSFWeight_singleEle80);
   fChain->SetBranchAddress("muTrigSFWeight_singlemu", muTrigSFWeight_singlemu, &b_muTrigSFWeight_singlemu);
   fChain->SetBranchAddress("NLOw", &NLOw, &b_NLOw);
   fChain->SetBranchAddress("DYw", &DYw, &b_DYw);
   fChain->SetBranchAddress("EWKw", EWKw, &b_EWKw);
   fChain->SetBranchAddress("EWKwSIG", EWKwSIG, &b_EWKwSIG);
   fChain->SetBranchAddress("EWKwVJets", EWKwVJets, &b_EWKwVJets);
   fChain->SetBranchAddress("bTagWeightCMVAV2", &bTagWeightCMVAV2, &b_bTagWeightCMVAV2);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JESUp", &bTagWeightCMVAV2_JESUp, &b_bTagWeightCMVAV2_JESUp);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JESDown", &bTagWeightCMVAV2_JESDown, &b_bTagWeightCMVAV2_JESDown);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFUp", &bTagWeightCMVAV2_LFUp, &b_bTagWeightCMVAV2_LFUp);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFDown", &bTagWeightCMVAV2_LFDown, &b_bTagWeightCMVAV2_LFDown);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFUp", &bTagWeightCMVAV2_HFUp, &b_bTagWeightCMVAV2_HFUp);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFDown", &bTagWeightCMVAV2_HFDown, &b_bTagWeightCMVAV2_HFDown);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1Up", &bTagWeightCMVAV2_LFStats1Up, &b_bTagWeightCMVAV2_LFStats1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1Down", &bTagWeightCMVAV2_LFStats1Down, &b_bTagWeightCMVAV2_LFStats1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2Up", &bTagWeightCMVAV2_LFStats2Up, &b_bTagWeightCMVAV2_LFStats2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2Down", &bTagWeightCMVAV2_LFStats2Down, &b_bTagWeightCMVAV2_LFStats2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1Up", &bTagWeightCMVAV2_HFStats1Up, &b_bTagWeightCMVAV2_HFStats1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1Down", &bTagWeightCMVAV2_HFStats1Down, &b_bTagWeightCMVAV2_HFStats1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2Up", &bTagWeightCMVAV2_HFStats2Up, &b_bTagWeightCMVAV2_HFStats2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2Down", &bTagWeightCMVAV2_HFStats2Down, &b_bTagWeightCMVAV2_HFStats2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1Up", &bTagWeightCMVAV2_cErr1Up, &b_bTagWeightCMVAV2_cErr1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1Down", &bTagWeightCMVAV2_cErr1Down, &b_bTagWeightCMVAV2_cErr1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2Up", &bTagWeightCMVAV2_cErr2Up, &b_bTagWeightCMVAV2_cErr2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2Down", &bTagWeightCMVAV2_cErr2Down, &b_bTagWeightCMVAV2_cErr2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt0_eta1Up", &bTagWeightCMVAV2_JES_pt0_eta1Up, &b_bTagWeightCMVAV2_JES_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt0_eta2Up", &bTagWeightCMVAV2_JES_pt0_eta2Up, &b_bTagWeightCMVAV2_JES_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt0_eta3Up", &bTagWeightCMVAV2_JES_pt0_eta3Up, &b_bTagWeightCMVAV2_JES_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt1_eta1Up", &bTagWeightCMVAV2_JES_pt1_eta1Up, &b_bTagWeightCMVAV2_JES_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt1_eta2Up", &bTagWeightCMVAV2_JES_pt1_eta2Up, &b_bTagWeightCMVAV2_JES_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt1_eta3Up", &bTagWeightCMVAV2_JES_pt1_eta3Up, &b_bTagWeightCMVAV2_JES_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt2_eta1Up", &bTagWeightCMVAV2_JES_pt2_eta1Up, &b_bTagWeightCMVAV2_JES_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt2_eta2Up", &bTagWeightCMVAV2_JES_pt2_eta2Up, &b_bTagWeightCMVAV2_JES_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt2_eta3Up", &bTagWeightCMVAV2_JES_pt2_eta3Up, &b_bTagWeightCMVAV2_JES_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt3_eta1Up", &bTagWeightCMVAV2_JES_pt3_eta1Up, &b_bTagWeightCMVAV2_JES_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt3_eta2Up", &bTagWeightCMVAV2_JES_pt3_eta2Up, &b_bTagWeightCMVAV2_JES_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt3_eta3Up", &bTagWeightCMVAV2_JES_pt3_eta3Up, &b_bTagWeightCMVAV2_JES_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt4_eta1Up", &bTagWeightCMVAV2_JES_pt4_eta1Up, &b_bTagWeightCMVAV2_JES_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt4_eta2Up", &bTagWeightCMVAV2_JES_pt4_eta2Up, &b_bTagWeightCMVAV2_JES_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt4_eta3Up", &bTagWeightCMVAV2_JES_pt4_eta3Up, &b_bTagWeightCMVAV2_JES_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt0_eta1Down", &bTagWeightCMVAV2_JES_pt0_eta1Down, &b_bTagWeightCMVAV2_JES_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt0_eta2Down", &bTagWeightCMVAV2_JES_pt0_eta2Down, &b_bTagWeightCMVAV2_JES_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt0_eta3Down", &bTagWeightCMVAV2_JES_pt0_eta3Down, &b_bTagWeightCMVAV2_JES_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt1_eta1Down", &bTagWeightCMVAV2_JES_pt1_eta1Down, &b_bTagWeightCMVAV2_JES_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt1_eta2Down", &bTagWeightCMVAV2_JES_pt1_eta2Down, &b_bTagWeightCMVAV2_JES_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt1_eta3Down", &bTagWeightCMVAV2_JES_pt1_eta3Down, &b_bTagWeightCMVAV2_JES_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt2_eta1Down", &bTagWeightCMVAV2_JES_pt2_eta1Down, &b_bTagWeightCMVAV2_JES_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt2_eta2Down", &bTagWeightCMVAV2_JES_pt2_eta2Down, &b_bTagWeightCMVAV2_JES_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt2_eta3Down", &bTagWeightCMVAV2_JES_pt2_eta3Down, &b_bTagWeightCMVAV2_JES_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt3_eta1Down", &bTagWeightCMVAV2_JES_pt3_eta1Down, &b_bTagWeightCMVAV2_JES_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt3_eta2Down", &bTagWeightCMVAV2_JES_pt3_eta2Down, &b_bTagWeightCMVAV2_JES_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt3_eta3Down", &bTagWeightCMVAV2_JES_pt3_eta3Down, &b_bTagWeightCMVAV2_JES_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt4_eta1Down", &bTagWeightCMVAV2_JES_pt4_eta1Down, &b_bTagWeightCMVAV2_JES_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt4_eta2Down", &bTagWeightCMVAV2_JES_pt4_eta2Down, &b_bTagWeightCMVAV2_JES_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_JES_pt4_eta3Down", &bTagWeightCMVAV2_JES_pt4_eta3Down, &b_bTagWeightCMVAV2_JES_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt0_eta1Up", &bTagWeightCMVAV2_LF_pt0_eta1Up, &b_bTagWeightCMVAV2_LF_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt0_eta2Up", &bTagWeightCMVAV2_LF_pt0_eta2Up, &b_bTagWeightCMVAV2_LF_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt0_eta3Up", &bTagWeightCMVAV2_LF_pt0_eta3Up, &b_bTagWeightCMVAV2_LF_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt1_eta1Up", &bTagWeightCMVAV2_LF_pt1_eta1Up, &b_bTagWeightCMVAV2_LF_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt1_eta2Up", &bTagWeightCMVAV2_LF_pt1_eta2Up, &b_bTagWeightCMVAV2_LF_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt1_eta3Up", &bTagWeightCMVAV2_LF_pt1_eta3Up, &b_bTagWeightCMVAV2_LF_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt2_eta1Up", &bTagWeightCMVAV2_LF_pt2_eta1Up, &b_bTagWeightCMVAV2_LF_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt2_eta2Up", &bTagWeightCMVAV2_LF_pt2_eta2Up, &b_bTagWeightCMVAV2_LF_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt2_eta3Up", &bTagWeightCMVAV2_LF_pt2_eta3Up, &b_bTagWeightCMVAV2_LF_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt3_eta1Up", &bTagWeightCMVAV2_LF_pt3_eta1Up, &b_bTagWeightCMVAV2_LF_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt3_eta2Up", &bTagWeightCMVAV2_LF_pt3_eta2Up, &b_bTagWeightCMVAV2_LF_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt3_eta3Up", &bTagWeightCMVAV2_LF_pt3_eta3Up, &b_bTagWeightCMVAV2_LF_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt4_eta1Up", &bTagWeightCMVAV2_LF_pt4_eta1Up, &b_bTagWeightCMVAV2_LF_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt4_eta2Up", &bTagWeightCMVAV2_LF_pt4_eta2Up, &b_bTagWeightCMVAV2_LF_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt4_eta3Up", &bTagWeightCMVAV2_LF_pt4_eta3Up, &b_bTagWeightCMVAV2_LF_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt0_eta1Down", &bTagWeightCMVAV2_LF_pt0_eta1Down, &b_bTagWeightCMVAV2_LF_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt0_eta2Down", &bTagWeightCMVAV2_LF_pt0_eta2Down, &b_bTagWeightCMVAV2_LF_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt0_eta3Down", &bTagWeightCMVAV2_LF_pt0_eta3Down, &b_bTagWeightCMVAV2_LF_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt1_eta1Down", &bTagWeightCMVAV2_LF_pt1_eta1Down, &b_bTagWeightCMVAV2_LF_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt1_eta2Down", &bTagWeightCMVAV2_LF_pt1_eta2Down, &b_bTagWeightCMVAV2_LF_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt1_eta3Down", &bTagWeightCMVAV2_LF_pt1_eta3Down, &b_bTagWeightCMVAV2_LF_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt2_eta1Down", &bTagWeightCMVAV2_LF_pt2_eta1Down, &b_bTagWeightCMVAV2_LF_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt2_eta2Down", &bTagWeightCMVAV2_LF_pt2_eta2Down, &b_bTagWeightCMVAV2_LF_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt2_eta3Down", &bTagWeightCMVAV2_LF_pt2_eta3Down, &b_bTagWeightCMVAV2_LF_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt3_eta1Down", &bTagWeightCMVAV2_LF_pt3_eta1Down, &b_bTagWeightCMVAV2_LF_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt3_eta2Down", &bTagWeightCMVAV2_LF_pt3_eta2Down, &b_bTagWeightCMVAV2_LF_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt3_eta3Down", &bTagWeightCMVAV2_LF_pt3_eta3Down, &b_bTagWeightCMVAV2_LF_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt4_eta1Down", &bTagWeightCMVAV2_LF_pt4_eta1Down, &b_bTagWeightCMVAV2_LF_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt4_eta2Down", &bTagWeightCMVAV2_LF_pt4_eta2Down, &b_bTagWeightCMVAV2_LF_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LF_pt4_eta3Down", &bTagWeightCMVAV2_LF_pt4_eta3Down, &b_bTagWeightCMVAV2_LF_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt0_eta1Up", &bTagWeightCMVAV2_HF_pt0_eta1Up, &b_bTagWeightCMVAV2_HF_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt0_eta2Up", &bTagWeightCMVAV2_HF_pt0_eta2Up, &b_bTagWeightCMVAV2_HF_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt0_eta3Up", &bTagWeightCMVAV2_HF_pt0_eta3Up, &b_bTagWeightCMVAV2_HF_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt1_eta1Up", &bTagWeightCMVAV2_HF_pt1_eta1Up, &b_bTagWeightCMVAV2_HF_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt1_eta2Up", &bTagWeightCMVAV2_HF_pt1_eta2Up, &b_bTagWeightCMVAV2_HF_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt1_eta3Up", &bTagWeightCMVAV2_HF_pt1_eta3Up, &b_bTagWeightCMVAV2_HF_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt2_eta1Up", &bTagWeightCMVAV2_HF_pt2_eta1Up, &b_bTagWeightCMVAV2_HF_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt2_eta2Up", &bTagWeightCMVAV2_HF_pt2_eta2Up, &b_bTagWeightCMVAV2_HF_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt2_eta3Up", &bTagWeightCMVAV2_HF_pt2_eta3Up, &b_bTagWeightCMVAV2_HF_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt3_eta1Up", &bTagWeightCMVAV2_HF_pt3_eta1Up, &b_bTagWeightCMVAV2_HF_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt3_eta2Up", &bTagWeightCMVAV2_HF_pt3_eta2Up, &b_bTagWeightCMVAV2_HF_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt3_eta3Up", &bTagWeightCMVAV2_HF_pt3_eta3Up, &b_bTagWeightCMVAV2_HF_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt4_eta1Up", &bTagWeightCMVAV2_HF_pt4_eta1Up, &b_bTagWeightCMVAV2_HF_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt4_eta2Up", &bTagWeightCMVAV2_HF_pt4_eta2Up, &b_bTagWeightCMVAV2_HF_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt4_eta3Up", &bTagWeightCMVAV2_HF_pt4_eta3Up, &b_bTagWeightCMVAV2_HF_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt0_eta1Down", &bTagWeightCMVAV2_HF_pt0_eta1Down, &b_bTagWeightCMVAV2_HF_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt0_eta2Down", &bTagWeightCMVAV2_HF_pt0_eta2Down, &b_bTagWeightCMVAV2_HF_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt0_eta3Down", &bTagWeightCMVAV2_HF_pt0_eta3Down, &b_bTagWeightCMVAV2_HF_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt1_eta1Down", &bTagWeightCMVAV2_HF_pt1_eta1Down, &b_bTagWeightCMVAV2_HF_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt1_eta2Down", &bTagWeightCMVAV2_HF_pt1_eta2Down, &b_bTagWeightCMVAV2_HF_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt1_eta3Down", &bTagWeightCMVAV2_HF_pt1_eta3Down, &b_bTagWeightCMVAV2_HF_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt2_eta1Down", &bTagWeightCMVAV2_HF_pt2_eta1Down, &b_bTagWeightCMVAV2_HF_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt2_eta2Down", &bTagWeightCMVAV2_HF_pt2_eta2Down, &b_bTagWeightCMVAV2_HF_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt2_eta3Down", &bTagWeightCMVAV2_HF_pt2_eta3Down, &b_bTagWeightCMVAV2_HF_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt3_eta1Down", &bTagWeightCMVAV2_HF_pt3_eta1Down, &b_bTagWeightCMVAV2_HF_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt3_eta2Down", &bTagWeightCMVAV2_HF_pt3_eta2Down, &b_bTagWeightCMVAV2_HF_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt3_eta3Down", &bTagWeightCMVAV2_HF_pt3_eta3Down, &b_bTagWeightCMVAV2_HF_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt4_eta1Down", &bTagWeightCMVAV2_HF_pt4_eta1Down, &b_bTagWeightCMVAV2_HF_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt4_eta2Down", &bTagWeightCMVAV2_HF_pt4_eta2Down, &b_bTagWeightCMVAV2_HF_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HF_pt4_eta3Down", &bTagWeightCMVAV2_HF_pt4_eta3Down, &b_bTagWeightCMVAV2_HF_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt0_eta1Up", &bTagWeightCMVAV2_LFStats1_pt0_eta1Up, &b_bTagWeightCMVAV2_LFStats1_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt0_eta2Up", &bTagWeightCMVAV2_LFStats1_pt0_eta2Up, &b_bTagWeightCMVAV2_LFStats1_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt0_eta3Up", &bTagWeightCMVAV2_LFStats1_pt0_eta3Up, &b_bTagWeightCMVAV2_LFStats1_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt1_eta1Up", &bTagWeightCMVAV2_LFStats1_pt1_eta1Up, &b_bTagWeightCMVAV2_LFStats1_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt1_eta2Up", &bTagWeightCMVAV2_LFStats1_pt1_eta2Up, &b_bTagWeightCMVAV2_LFStats1_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt1_eta3Up", &bTagWeightCMVAV2_LFStats1_pt1_eta3Up, &b_bTagWeightCMVAV2_LFStats1_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt2_eta1Up", &bTagWeightCMVAV2_LFStats1_pt2_eta1Up, &b_bTagWeightCMVAV2_LFStats1_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt2_eta2Up", &bTagWeightCMVAV2_LFStats1_pt2_eta2Up, &b_bTagWeightCMVAV2_LFStats1_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt2_eta3Up", &bTagWeightCMVAV2_LFStats1_pt2_eta3Up, &b_bTagWeightCMVAV2_LFStats1_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt3_eta1Up", &bTagWeightCMVAV2_LFStats1_pt3_eta1Up, &b_bTagWeightCMVAV2_LFStats1_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt3_eta2Up", &bTagWeightCMVAV2_LFStats1_pt3_eta2Up, &b_bTagWeightCMVAV2_LFStats1_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt3_eta3Up", &bTagWeightCMVAV2_LFStats1_pt3_eta3Up, &b_bTagWeightCMVAV2_LFStats1_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt4_eta1Up", &bTagWeightCMVAV2_LFStats1_pt4_eta1Up, &b_bTagWeightCMVAV2_LFStats1_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt4_eta2Up", &bTagWeightCMVAV2_LFStats1_pt4_eta2Up, &b_bTagWeightCMVAV2_LFStats1_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt4_eta3Up", &bTagWeightCMVAV2_LFStats1_pt4_eta3Up, &b_bTagWeightCMVAV2_LFStats1_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt0_eta1Down", &bTagWeightCMVAV2_LFStats1_pt0_eta1Down, &b_bTagWeightCMVAV2_LFStats1_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt0_eta2Down", &bTagWeightCMVAV2_LFStats1_pt0_eta2Down, &b_bTagWeightCMVAV2_LFStats1_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt0_eta3Down", &bTagWeightCMVAV2_LFStats1_pt0_eta3Down, &b_bTagWeightCMVAV2_LFStats1_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt1_eta1Down", &bTagWeightCMVAV2_LFStats1_pt1_eta1Down, &b_bTagWeightCMVAV2_LFStats1_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt1_eta2Down", &bTagWeightCMVAV2_LFStats1_pt1_eta2Down, &b_bTagWeightCMVAV2_LFStats1_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt1_eta3Down", &bTagWeightCMVAV2_LFStats1_pt1_eta3Down, &b_bTagWeightCMVAV2_LFStats1_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt2_eta1Down", &bTagWeightCMVAV2_LFStats1_pt2_eta1Down, &b_bTagWeightCMVAV2_LFStats1_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt2_eta2Down", &bTagWeightCMVAV2_LFStats1_pt2_eta2Down, &b_bTagWeightCMVAV2_LFStats1_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt2_eta3Down", &bTagWeightCMVAV2_LFStats1_pt2_eta3Down, &b_bTagWeightCMVAV2_LFStats1_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt3_eta1Down", &bTagWeightCMVAV2_LFStats1_pt3_eta1Down, &b_bTagWeightCMVAV2_LFStats1_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt3_eta2Down", &bTagWeightCMVAV2_LFStats1_pt3_eta2Down, &b_bTagWeightCMVAV2_LFStats1_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt3_eta3Down", &bTagWeightCMVAV2_LFStats1_pt3_eta3Down, &b_bTagWeightCMVAV2_LFStats1_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt4_eta1Down", &bTagWeightCMVAV2_LFStats1_pt4_eta1Down, &b_bTagWeightCMVAV2_LFStats1_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt4_eta2Down", &bTagWeightCMVAV2_LFStats1_pt4_eta2Down, &b_bTagWeightCMVAV2_LFStats1_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats1_pt4_eta3Down", &bTagWeightCMVAV2_LFStats1_pt4_eta3Down, &b_bTagWeightCMVAV2_LFStats1_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt0_eta1Up", &bTagWeightCMVAV2_LFStats2_pt0_eta1Up, &b_bTagWeightCMVAV2_LFStats2_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt0_eta2Up", &bTagWeightCMVAV2_LFStats2_pt0_eta2Up, &b_bTagWeightCMVAV2_LFStats2_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt0_eta3Up", &bTagWeightCMVAV2_LFStats2_pt0_eta3Up, &b_bTagWeightCMVAV2_LFStats2_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt1_eta1Up", &bTagWeightCMVAV2_LFStats2_pt1_eta1Up, &b_bTagWeightCMVAV2_LFStats2_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt1_eta2Up", &bTagWeightCMVAV2_LFStats2_pt1_eta2Up, &b_bTagWeightCMVAV2_LFStats2_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt1_eta3Up", &bTagWeightCMVAV2_LFStats2_pt1_eta3Up, &b_bTagWeightCMVAV2_LFStats2_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt2_eta1Up", &bTagWeightCMVAV2_LFStats2_pt2_eta1Up, &b_bTagWeightCMVAV2_LFStats2_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt2_eta2Up", &bTagWeightCMVAV2_LFStats2_pt2_eta2Up, &b_bTagWeightCMVAV2_LFStats2_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt2_eta3Up", &bTagWeightCMVAV2_LFStats2_pt2_eta3Up, &b_bTagWeightCMVAV2_LFStats2_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt3_eta1Up", &bTagWeightCMVAV2_LFStats2_pt3_eta1Up, &b_bTagWeightCMVAV2_LFStats2_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt3_eta2Up", &bTagWeightCMVAV2_LFStats2_pt3_eta2Up, &b_bTagWeightCMVAV2_LFStats2_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt3_eta3Up", &bTagWeightCMVAV2_LFStats2_pt3_eta3Up, &b_bTagWeightCMVAV2_LFStats2_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt4_eta1Up", &bTagWeightCMVAV2_LFStats2_pt4_eta1Up, &b_bTagWeightCMVAV2_LFStats2_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt4_eta2Up", &bTagWeightCMVAV2_LFStats2_pt4_eta2Up, &b_bTagWeightCMVAV2_LFStats2_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt4_eta3Up", &bTagWeightCMVAV2_LFStats2_pt4_eta3Up, &b_bTagWeightCMVAV2_LFStats2_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt0_eta1Down", &bTagWeightCMVAV2_LFStats2_pt0_eta1Down, &b_bTagWeightCMVAV2_LFStats2_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt0_eta2Down", &bTagWeightCMVAV2_LFStats2_pt0_eta2Down, &b_bTagWeightCMVAV2_LFStats2_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt0_eta3Down", &bTagWeightCMVAV2_LFStats2_pt0_eta3Down, &b_bTagWeightCMVAV2_LFStats2_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt1_eta1Down", &bTagWeightCMVAV2_LFStats2_pt1_eta1Down, &b_bTagWeightCMVAV2_LFStats2_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt1_eta2Down", &bTagWeightCMVAV2_LFStats2_pt1_eta2Down, &b_bTagWeightCMVAV2_LFStats2_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt1_eta3Down", &bTagWeightCMVAV2_LFStats2_pt1_eta3Down, &b_bTagWeightCMVAV2_LFStats2_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt2_eta1Down", &bTagWeightCMVAV2_LFStats2_pt2_eta1Down, &b_bTagWeightCMVAV2_LFStats2_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt2_eta2Down", &bTagWeightCMVAV2_LFStats2_pt2_eta2Down, &b_bTagWeightCMVAV2_LFStats2_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt2_eta3Down", &bTagWeightCMVAV2_LFStats2_pt2_eta3Down, &b_bTagWeightCMVAV2_LFStats2_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt3_eta1Down", &bTagWeightCMVAV2_LFStats2_pt3_eta1Down, &b_bTagWeightCMVAV2_LFStats2_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt3_eta2Down", &bTagWeightCMVAV2_LFStats2_pt3_eta2Down, &b_bTagWeightCMVAV2_LFStats2_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt3_eta3Down", &bTagWeightCMVAV2_LFStats2_pt3_eta3Down, &b_bTagWeightCMVAV2_LFStats2_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt4_eta1Down", &bTagWeightCMVAV2_LFStats2_pt4_eta1Down, &b_bTagWeightCMVAV2_LFStats2_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt4_eta2Down", &bTagWeightCMVAV2_LFStats2_pt4_eta2Down, &b_bTagWeightCMVAV2_LFStats2_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_LFStats2_pt4_eta3Down", &bTagWeightCMVAV2_LFStats2_pt4_eta3Down, &b_bTagWeightCMVAV2_LFStats2_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt0_eta1Up", &bTagWeightCMVAV2_HFStats1_pt0_eta1Up, &b_bTagWeightCMVAV2_HFStats1_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt0_eta2Up", &bTagWeightCMVAV2_HFStats1_pt0_eta2Up, &b_bTagWeightCMVAV2_HFStats1_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt0_eta3Up", &bTagWeightCMVAV2_HFStats1_pt0_eta3Up, &b_bTagWeightCMVAV2_HFStats1_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt1_eta1Up", &bTagWeightCMVAV2_HFStats1_pt1_eta1Up, &b_bTagWeightCMVAV2_HFStats1_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt1_eta2Up", &bTagWeightCMVAV2_HFStats1_pt1_eta2Up, &b_bTagWeightCMVAV2_HFStats1_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt1_eta3Up", &bTagWeightCMVAV2_HFStats1_pt1_eta3Up, &b_bTagWeightCMVAV2_HFStats1_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt2_eta1Up", &bTagWeightCMVAV2_HFStats1_pt2_eta1Up, &b_bTagWeightCMVAV2_HFStats1_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt2_eta2Up", &bTagWeightCMVAV2_HFStats1_pt2_eta2Up, &b_bTagWeightCMVAV2_HFStats1_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt2_eta3Up", &bTagWeightCMVAV2_HFStats1_pt2_eta3Up, &b_bTagWeightCMVAV2_HFStats1_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt3_eta1Up", &bTagWeightCMVAV2_HFStats1_pt3_eta1Up, &b_bTagWeightCMVAV2_HFStats1_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt3_eta2Up", &bTagWeightCMVAV2_HFStats1_pt3_eta2Up, &b_bTagWeightCMVAV2_HFStats1_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt3_eta3Up", &bTagWeightCMVAV2_HFStats1_pt3_eta3Up, &b_bTagWeightCMVAV2_HFStats1_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt4_eta1Up", &bTagWeightCMVAV2_HFStats1_pt4_eta1Up, &b_bTagWeightCMVAV2_HFStats1_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt4_eta2Up", &bTagWeightCMVAV2_HFStats1_pt4_eta2Up, &b_bTagWeightCMVAV2_HFStats1_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt4_eta3Up", &bTagWeightCMVAV2_HFStats1_pt4_eta3Up, &b_bTagWeightCMVAV2_HFStats1_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt0_eta1Down", &bTagWeightCMVAV2_HFStats1_pt0_eta1Down, &b_bTagWeightCMVAV2_HFStats1_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt0_eta2Down", &bTagWeightCMVAV2_HFStats1_pt0_eta2Down, &b_bTagWeightCMVAV2_HFStats1_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt0_eta3Down", &bTagWeightCMVAV2_HFStats1_pt0_eta3Down, &b_bTagWeightCMVAV2_HFStats1_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt1_eta1Down", &bTagWeightCMVAV2_HFStats1_pt1_eta1Down, &b_bTagWeightCMVAV2_HFStats1_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt1_eta2Down", &bTagWeightCMVAV2_HFStats1_pt1_eta2Down, &b_bTagWeightCMVAV2_HFStats1_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt1_eta3Down", &bTagWeightCMVAV2_HFStats1_pt1_eta3Down, &b_bTagWeightCMVAV2_HFStats1_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt2_eta1Down", &bTagWeightCMVAV2_HFStats1_pt2_eta1Down, &b_bTagWeightCMVAV2_HFStats1_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt2_eta2Down", &bTagWeightCMVAV2_HFStats1_pt2_eta2Down, &b_bTagWeightCMVAV2_HFStats1_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt2_eta3Down", &bTagWeightCMVAV2_HFStats1_pt2_eta3Down, &b_bTagWeightCMVAV2_HFStats1_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt3_eta1Down", &bTagWeightCMVAV2_HFStats1_pt3_eta1Down, &b_bTagWeightCMVAV2_HFStats1_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt3_eta2Down", &bTagWeightCMVAV2_HFStats1_pt3_eta2Down, &b_bTagWeightCMVAV2_HFStats1_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt3_eta3Down", &bTagWeightCMVAV2_HFStats1_pt3_eta3Down, &b_bTagWeightCMVAV2_HFStats1_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt4_eta1Down", &bTagWeightCMVAV2_HFStats1_pt4_eta1Down, &b_bTagWeightCMVAV2_HFStats1_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt4_eta2Down", &bTagWeightCMVAV2_HFStats1_pt4_eta2Down, &b_bTagWeightCMVAV2_HFStats1_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats1_pt4_eta3Down", &bTagWeightCMVAV2_HFStats1_pt4_eta3Down, &b_bTagWeightCMVAV2_HFStats1_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt0_eta1Up", &bTagWeightCMVAV2_HFStats2_pt0_eta1Up, &b_bTagWeightCMVAV2_HFStats2_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt0_eta2Up", &bTagWeightCMVAV2_HFStats2_pt0_eta2Up, &b_bTagWeightCMVAV2_HFStats2_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt0_eta3Up", &bTagWeightCMVAV2_HFStats2_pt0_eta3Up, &b_bTagWeightCMVAV2_HFStats2_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt1_eta1Up", &bTagWeightCMVAV2_HFStats2_pt1_eta1Up, &b_bTagWeightCMVAV2_HFStats2_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt1_eta2Up", &bTagWeightCMVAV2_HFStats2_pt1_eta2Up, &b_bTagWeightCMVAV2_HFStats2_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt1_eta3Up", &bTagWeightCMVAV2_HFStats2_pt1_eta3Up, &b_bTagWeightCMVAV2_HFStats2_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt2_eta1Up", &bTagWeightCMVAV2_HFStats2_pt2_eta1Up, &b_bTagWeightCMVAV2_HFStats2_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt2_eta2Up", &bTagWeightCMVAV2_HFStats2_pt2_eta2Up, &b_bTagWeightCMVAV2_HFStats2_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt2_eta3Up", &bTagWeightCMVAV2_HFStats2_pt2_eta3Up, &b_bTagWeightCMVAV2_HFStats2_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt3_eta1Up", &bTagWeightCMVAV2_HFStats2_pt3_eta1Up, &b_bTagWeightCMVAV2_HFStats2_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt3_eta2Up", &bTagWeightCMVAV2_HFStats2_pt3_eta2Up, &b_bTagWeightCMVAV2_HFStats2_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt3_eta3Up", &bTagWeightCMVAV2_HFStats2_pt3_eta3Up, &b_bTagWeightCMVAV2_HFStats2_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt4_eta1Up", &bTagWeightCMVAV2_HFStats2_pt4_eta1Up, &b_bTagWeightCMVAV2_HFStats2_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt4_eta2Up", &bTagWeightCMVAV2_HFStats2_pt4_eta2Up, &b_bTagWeightCMVAV2_HFStats2_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt4_eta3Up", &bTagWeightCMVAV2_HFStats2_pt4_eta3Up, &b_bTagWeightCMVAV2_HFStats2_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt0_eta1Down", &bTagWeightCMVAV2_HFStats2_pt0_eta1Down, &b_bTagWeightCMVAV2_HFStats2_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt0_eta2Down", &bTagWeightCMVAV2_HFStats2_pt0_eta2Down, &b_bTagWeightCMVAV2_HFStats2_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt0_eta3Down", &bTagWeightCMVAV2_HFStats2_pt0_eta3Down, &b_bTagWeightCMVAV2_HFStats2_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt1_eta1Down", &bTagWeightCMVAV2_HFStats2_pt1_eta1Down, &b_bTagWeightCMVAV2_HFStats2_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt1_eta2Down", &bTagWeightCMVAV2_HFStats2_pt1_eta2Down, &b_bTagWeightCMVAV2_HFStats2_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt1_eta3Down", &bTagWeightCMVAV2_HFStats2_pt1_eta3Down, &b_bTagWeightCMVAV2_HFStats2_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt2_eta1Down", &bTagWeightCMVAV2_HFStats2_pt2_eta1Down, &b_bTagWeightCMVAV2_HFStats2_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt2_eta2Down", &bTagWeightCMVAV2_HFStats2_pt2_eta2Down, &b_bTagWeightCMVAV2_HFStats2_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt2_eta3Down", &bTagWeightCMVAV2_HFStats2_pt2_eta3Down, &b_bTagWeightCMVAV2_HFStats2_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt3_eta1Down", &bTagWeightCMVAV2_HFStats2_pt3_eta1Down, &b_bTagWeightCMVAV2_HFStats2_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt3_eta2Down", &bTagWeightCMVAV2_HFStats2_pt3_eta2Down, &b_bTagWeightCMVAV2_HFStats2_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt3_eta3Down", &bTagWeightCMVAV2_HFStats2_pt3_eta3Down, &b_bTagWeightCMVAV2_HFStats2_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt4_eta1Down", &bTagWeightCMVAV2_HFStats2_pt4_eta1Down, &b_bTagWeightCMVAV2_HFStats2_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt4_eta2Down", &bTagWeightCMVAV2_HFStats2_pt4_eta2Down, &b_bTagWeightCMVAV2_HFStats2_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_HFStats2_pt4_eta3Down", &bTagWeightCMVAV2_HFStats2_pt4_eta3Down, &b_bTagWeightCMVAV2_HFStats2_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt0_eta1Up", &bTagWeightCMVAV2_cErr1_pt0_eta1Up, &b_bTagWeightCMVAV2_cErr1_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt0_eta2Up", &bTagWeightCMVAV2_cErr1_pt0_eta2Up, &b_bTagWeightCMVAV2_cErr1_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt0_eta3Up", &bTagWeightCMVAV2_cErr1_pt0_eta3Up, &b_bTagWeightCMVAV2_cErr1_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt1_eta1Up", &bTagWeightCMVAV2_cErr1_pt1_eta1Up, &b_bTagWeightCMVAV2_cErr1_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt1_eta2Up", &bTagWeightCMVAV2_cErr1_pt1_eta2Up, &b_bTagWeightCMVAV2_cErr1_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt1_eta3Up", &bTagWeightCMVAV2_cErr1_pt1_eta3Up, &b_bTagWeightCMVAV2_cErr1_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt2_eta1Up", &bTagWeightCMVAV2_cErr1_pt2_eta1Up, &b_bTagWeightCMVAV2_cErr1_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt2_eta2Up", &bTagWeightCMVAV2_cErr1_pt2_eta2Up, &b_bTagWeightCMVAV2_cErr1_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt2_eta3Up", &bTagWeightCMVAV2_cErr1_pt2_eta3Up, &b_bTagWeightCMVAV2_cErr1_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt3_eta1Up", &bTagWeightCMVAV2_cErr1_pt3_eta1Up, &b_bTagWeightCMVAV2_cErr1_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt3_eta2Up", &bTagWeightCMVAV2_cErr1_pt3_eta2Up, &b_bTagWeightCMVAV2_cErr1_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt3_eta3Up", &bTagWeightCMVAV2_cErr1_pt3_eta3Up, &b_bTagWeightCMVAV2_cErr1_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt4_eta1Up", &bTagWeightCMVAV2_cErr1_pt4_eta1Up, &b_bTagWeightCMVAV2_cErr1_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt4_eta2Up", &bTagWeightCMVAV2_cErr1_pt4_eta2Up, &b_bTagWeightCMVAV2_cErr1_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt4_eta3Up", &bTagWeightCMVAV2_cErr1_pt4_eta3Up, &b_bTagWeightCMVAV2_cErr1_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt0_eta1Down", &bTagWeightCMVAV2_cErr1_pt0_eta1Down, &b_bTagWeightCMVAV2_cErr1_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt0_eta2Down", &bTagWeightCMVAV2_cErr1_pt0_eta2Down, &b_bTagWeightCMVAV2_cErr1_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt0_eta3Down", &bTagWeightCMVAV2_cErr1_pt0_eta3Down, &b_bTagWeightCMVAV2_cErr1_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt1_eta1Down", &bTagWeightCMVAV2_cErr1_pt1_eta1Down, &b_bTagWeightCMVAV2_cErr1_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt1_eta2Down", &bTagWeightCMVAV2_cErr1_pt1_eta2Down, &b_bTagWeightCMVAV2_cErr1_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt1_eta3Down", &bTagWeightCMVAV2_cErr1_pt1_eta3Down, &b_bTagWeightCMVAV2_cErr1_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt2_eta1Down", &bTagWeightCMVAV2_cErr1_pt2_eta1Down, &b_bTagWeightCMVAV2_cErr1_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt2_eta2Down", &bTagWeightCMVAV2_cErr1_pt2_eta2Down, &b_bTagWeightCMVAV2_cErr1_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt2_eta3Down", &bTagWeightCMVAV2_cErr1_pt2_eta3Down, &b_bTagWeightCMVAV2_cErr1_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt3_eta1Down", &bTagWeightCMVAV2_cErr1_pt3_eta1Down, &b_bTagWeightCMVAV2_cErr1_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt3_eta2Down", &bTagWeightCMVAV2_cErr1_pt3_eta2Down, &b_bTagWeightCMVAV2_cErr1_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt3_eta3Down", &bTagWeightCMVAV2_cErr1_pt3_eta3Down, &b_bTagWeightCMVAV2_cErr1_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt4_eta1Down", &bTagWeightCMVAV2_cErr1_pt4_eta1Down, &b_bTagWeightCMVAV2_cErr1_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt4_eta2Down", &bTagWeightCMVAV2_cErr1_pt4_eta2Down, &b_bTagWeightCMVAV2_cErr1_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr1_pt4_eta3Down", &bTagWeightCMVAV2_cErr1_pt4_eta3Down, &b_bTagWeightCMVAV2_cErr1_pt4_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt0_eta1Up", &bTagWeightCMVAV2_cErr2_pt0_eta1Up, &b_bTagWeightCMVAV2_cErr2_pt0_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt0_eta2Up", &bTagWeightCMVAV2_cErr2_pt0_eta2Up, &b_bTagWeightCMVAV2_cErr2_pt0_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt0_eta3Up", &bTagWeightCMVAV2_cErr2_pt0_eta3Up, &b_bTagWeightCMVAV2_cErr2_pt0_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt1_eta1Up", &bTagWeightCMVAV2_cErr2_pt1_eta1Up, &b_bTagWeightCMVAV2_cErr2_pt1_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt1_eta2Up", &bTagWeightCMVAV2_cErr2_pt1_eta2Up, &b_bTagWeightCMVAV2_cErr2_pt1_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt1_eta3Up", &bTagWeightCMVAV2_cErr2_pt1_eta3Up, &b_bTagWeightCMVAV2_cErr2_pt1_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt2_eta1Up", &bTagWeightCMVAV2_cErr2_pt2_eta1Up, &b_bTagWeightCMVAV2_cErr2_pt2_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt2_eta2Up", &bTagWeightCMVAV2_cErr2_pt2_eta2Up, &b_bTagWeightCMVAV2_cErr2_pt2_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt2_eta3Up", &bTagWeightCMVAV2_cErr2_pt2_eta3Up, &b_bTagWeightCMVAV2_cErr2_pt2_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt3_eta1Up", &bTagWeightCMVAV2_cErr2_pt3_eta1Up, &b_bTagWeightCMVAV2_cErr2_pt3_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt3_eta2Up", &bTagWeightCMVAV2_cErr2_pt3_eta2Up, &b_bTagWeightCMVAV2_cErr2_pt3_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt3_eta3Up", &bTagWeightCMVAV2_cErr2_pt3_eta3Up, &b_bTagWeightCMVAV2_cErr2_pt3_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt4_eta1Up", &bTagWeightCMVAV2_cErr2_pt4_eta1Up, &b_bTagWeightCMVAV2_cErr2_pt4_eta1Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt4_eta2Up", &bTagWeightCMVAV2_cErr2_pt4_eta2Up, &b_bTagWeightCMVAV2_cErr2_pt4_eta2Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt4_eta3Up", &bTagWeightCMVAV2_cErr2_pt4_eta3Up, &b_bTagWeightCMVAV2_cErr2_pt4_eta3Up);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt0_eta1Down", &bTagWeightCMVAV2_cErr2_pt0_eta1Down, &b_bTagWeightCMVAV2_cErr2_pt0_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt0_eta2Down", &bTagWeightCMVAV2_cErr2_pt0_eta2Down, &b_bTagWeightCMVAV2_cErr2_pt0_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt0_eta3Down", &bTagWeightCMVAV2_cErr2_pt0_eta3Down, &b_bTagWeightCMVAV2_cErr2_pt0_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt1_eta1Down", &bTagWeightCMVAV2_cErr2_pt1_eta1Down, &b_bTagWeightCMVAV2_cErr2_pt1_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt1_eta2Down", &bTagWeightCMVAV2_cErr2_pt1_eta2Down, &b_bTagWeightCMVAV2_cErr2_pt1_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt1_eta3Down", &bTagWeightCMVAV2_cErr2_pt1_eta3Down, &b_bTagWeightCMVAV2_cErr2_pt1_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt2_eta1Down", &bTagWeightCMVAV2_cErr2_pt2_eta1Down, &b_bTagWeightCMVAV2_cErr2_pt2_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt2_eta2Down", &bTagWeightCMVAV2_cErr2_pt2_eta2Down, &b_bTagWeightCMVAV2_cErr2_pt2_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt2_eta3Down", &bTagWeightCMVAV2_cErr2_pt2_eta3Down, &b_bTagWeightCMVAV2_cErr2_pt2_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt3_eta1Down", &bTagWeightCMVAV2_cErr2_pt3_eta1Down, &b_bTagWeightCMVAV2_cErr2_pt3_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt3_eta2Down", &bTagWeightCMVAV2_cErr2_pt3_eta2Down, &b_bTagWeightCMVAV2_cErr2_pt3_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt3_eta3Down", &bTagWeightCMVAV2_cErr2_pt3_eta3Down, &b_bTagWeightCMVAV2_cErr2_pt3_eta3Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt4_eta1Down", &bTagWeightCMVAV2_cErr2_pt4_eta1Down, &b_bTagWeightCMVAV2_cErr2_pt4_eta1Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt4_eta2Down", &bTagWeightCMVAV2_cErr2_pt4_eta2Down, &b_bTagWeightCMVAV2_cErr2_pt4_eta2Down);
   fChain->SetBranchAddress("bTagWeightCMVAV2_cErr2_pt4_eta3Down", &bTagWeightCMVAV2_cErr2_pt4_eta3Down, &b_bTagWeightCMVAV2_cErr2_pt4_eta3Down);
   fChain->SetBranchAddress("minDphiJetMet", &minDphiJetMet, &b_minDphiJetMet);
   fChain->SetBranchAddress("nAddJetQCD", &nAddJetQCD, &b_nAddJetQCD);
   fChain->SetBranchAddress("hJets_pt_reg_max", &hJets_pt_reg_max, &b_hJets_pt_reg_max);
   fChain->SetBranchAddress("nAddJet30", &nAddJet30, &b_nAddJet30);
   fChain->SetBranchAddress("hJets_pt_reg_min", &hJets_pt_reg_min, &b_hJets_pt_reg_min);
   fChain->SetBranchAddress("dPhiMetTkMet", &dPhiMetTkMet, &b_dPhiMetTkMet);
   fChain->SetBranchAddress("dPhiVH", &dPhiVH, &b_dPhiVH);
   fChain->SetBranchAddress("hJets_pt_reg_1", &hJets_pt_reg_1, &b_hJets_pt_reg_1);
   fChain->SetBranchAddress("hJets_pt_reg_0", &hJets_pt_reg_0, &b_hJets_pt_reg_0);
   fChain->SetBranchAddress("H_pt", &H_pt, &b_H_pt);
   fChain->SetBranchAddress("H_pt_jer_Up", &H_pt_jer_Up, &b_H_pt_jer_Up);
   fChain->SetBranchAddress("H_pt_jer_Down", &H_pt_jer_Down, &b_H_pt_jer_Down);
   fChain->SetBranchAddress("H_pt_jesAbsoluteStat_Up", &H_pt_jesAbsoluteStat_Up, &b_H_pt_jesAbsoluteStat_Up);
   fChain->SetBranchAddress("H_pt_jesAbsoluteStat_Down", &H_pt_jesAbsoluteStat_Down, &b_H_pt_jesAbsoluteStat_Down);
   fChain->SetBranchAddress("H_pt_jesAbsoluteScale_Up", &H_pt_jesAbsoluteScale_Up, &b_H_pt_jesAbsoluteScale_Up);
   fChain->SetBranchAddress("H_pt_jesAbsoluteScale_Down", &H_pt_jesAbsoluteScale_Down, &b_H_pt_jesAbsoluteScale_Down);
   fChain->SetBranchAddress("H_pt_jesAbsoluteFlavMap_Up", &H_pt_jesAbsoluteFlavMap_Up, &b_H_pt_jesAbsoluteFlavMap_Up);
   fChain->SetBranchAddress("H_pt_jesAbsoluteFlavMap_Down", &H_pt_jesAbsoluteFlavMap_Down, &b_H_pt_jesAbsoluteFlavMap_Down);
   fChain->SetBranchAddress("H_pt_jesAbsoluteMPFBias_Up", &H_pt_jesAbsoluteMPFBias_Up, &b_H_pt_jesAbsoluteMPFBias_Up);
   fChain->SetBranchAddress("H_pt_jesAbsoluteMPFBias_Down", &H_pt_jesAbsoluteMPFBias_Down, &b_H_pt_jesAbsoluteMPFBias_Down);
   fChain->SetBranchAddress("H_pt_jesFragmentation_Up", &H_pt_jesFragmentation_Up, &b_H_pt_jesFragmentation_Up);
   fChain->SetBranchAddress("H_pt_jesFragmentation_Down", &H_pt_jesFragmentation_Down, &b_H_pt_jesFragmentation_Down);
   fChain->SetBranchAddress("H_pt_jesSinglePionECAL_Up", &H_pt_jesSinglePionECAL_Up, &b_H_pt_jesSinglePionECAL_Up);
   fChain->SetBranchAddress("H_pt_jesSinglePionECAL_Down", &H_pt_jesSinglePionECAL_Down, &b_H_pt_jesSinglePionECAL_Down);
   fChain->SetBranchAddress("H_pt_jesSinglePionHCAL_Up", &H_pt_jesSinglePionHCAL_Up, &b_H_pt_jesSinglePionHCAL_Up);
   fChain->SetBranchAddress("H_pt_jesSinglePionHCAL_Down", &H_pt_jesSinglePionHCAL_Down, &b_H_pt_jesSinglePionHCAL_Down);
   fChain->SetBranchAddress("H_pt_jesFlavorQCD_Up", &H_pt_jesFlavorQCD_Up, &b_H_pt_jesFlavorQCD_Up);
   fChain->SetBranchAddress("H_pt_jesFlavorQCD_Down", &H_pt_jesFlavorQCD_Down, &b_H_pt_jesFlavorQCD_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeJEREC1_Up", &H_pt_jesRelativeJEREC1_Up, &b_H_pt_jesRelativeJEREC1_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeJEREC1_Down", &H_pt_jesRelativeJEREC1_Down, &b_H_pt_jesRelativeJEREC1_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeJEREC2_Up", &H_pt_jesRelativeJEREC2_Up, &b_H_pt_jesRelativeJEREC2_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeJEREC2_Down", &H_pt_jesRelativeJEREC2_Down, &b_H_pt_jesRelativeJEREC2_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeJERHF_Up", &H_pt_jesRelativeJERHF_Up, &b_H_pt_jesRelativeJERHF_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeJERHF_Down", &H_pt_jesRelativeJERHF_Down, &b_H_pt_jesRelativeJERHF_Down);
   fChain->SetBranchAddress("H_pt_jesRelativePtBB_Up", &H_pt_jesRelativePtBB_Up, &b_H_pt_jesRelativePtBB_Up);
   fChain->SetBranchAddress("H_pt_jesRelativePtBB_Down", &H_pt_jesRelativePtBB_Down, &b_H_pt_jesRelativePtBB_Down);
   fChain->SetBranchAddress("H_pt_jesRelativePtEC1_Up", &H_pt_jesRelativePtEC1_Up, &b_H_pt_jesRelativePtEC1_Up);
   fChain->SetBranchAddress("H_pt_jesRelativePtEC1_Down", &H_pt_jesRelativePtEC1_Down, &b_H_pt_jesRelativePtEC1_Down);
   fChain->SetBranchAddress("H_pt_jesRelativePtEC2_Up", &H_pt_jesRelativePtEC2_Up, &b_H_pt_jesRelativePtEC2_Up);
   fChain->SetBranchAddress("H_pt_jesRelativePtEC2_Down", &H_pt_jesRelativePtEC2_Down, &b_H_pt_jesRelativePtEC2_Down);
   fChain->SetBranchAddress("H_pt_jesRelativePtHF_Up", &H_pt_jesRelativePtHF_Up, &b_H_pt_jesRelativePtHF_Up);
   fChain->SetBranchAddress("H_pt_jesRelativePtHF_Down", &H_pt_jesRelativePtHF_Down, &b_H_pt_jesRelativePtHF_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeBal_Up", &H_pt_jesRelativeBal_Up, &b_H_pt_jesRelativeBal_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeBal_Down", &H_pt_jesRelativeBal_Down, &b_H_pt_jesRelativeBal_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeFSR_Up", &H_pt_jesRelativeFSR_Up, &b_H_pt_jesRelativeFSR_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeFSR_Down", &H_pt_jesRelativeFSR_Down, &b_H_pt_jesRelativeFSR_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeStatFSR_Up", &H_pt_jesRelativeStatFSR_Up, &b_H_pt_jesRelativeStatFSR_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeStatFSR_Down", &H_pt_jesRelativeStatFSR_Down, &b_H_pt_jesRelativeStatFSR_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeStatEC_Up", &H_pt_jesRelativeStatEC_Up, &b_H_pt_jesRelativeStatEC_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeStatEC_Down", &H_pt_jesRelativeStatEC_Down, &b_H_pt_jesRelativeStatEC_Down);
   fChain->SetBranchAddress("H_pt_jesRelativeStatHF_Up", &H_pt_jesRelativeStatHF_Up, &b_H_pt_jesRelativeStatHF_Up);
   fChain->SetBranchAddress("H_pt_jesRelativeStatHF_Down", &H_pt_jesRelativeStatHF_Down, &b_H_pt_jesRelativeStatHF_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpDataMC_Up", &H_pt_jesPileUpDataMC_Up, &b_H_pt_jesPileUpDataMC_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpDataMC_Down", &H_pt_jesPileUpDataMC_Down, &b_H_pt_jesPileUpDataMC_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpPtRef_Up", &H_pt_jesPileUpPtRef_Up, &b_H_pt_jesPileUpPtRef_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpPtRef_Down", &H_pt_jesPileUpPtRef_Down, &b_H_pt_jesPileUpPtRef_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpPtBB_Up", &H_pt_jesPileUpPtBB_Up, &b_H_pt_jesPileUpPtBB_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpPtBB_Down", &H_pt_jesPileUpPtBB_Down, &b_H_pt_jesPileUpPtBB_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpPtEC1_Up", &H_pt_jesPileUpPtEC1_Up, &b_H_pt_jesPileUpPtEC1_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpPtEC1_Down", &H_pt_jesPileUpPtEC1_Down, &b_H_pt_jesPileUpPtEC1_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpPtEC2_Up", &H_pt_jesPileUpPtEC2_Up, &b_H_pt_jesPileUpPtEC2_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpPtEC2_Down", &H_pt_jesPileUpPtEC2_Down, &b_H_pt_jesPileUpPtEC2_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpPtHF_Up", &H_pt_jesPileUpPtHF_Up, &b_H_pt_jesPileUpPtHF_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpPtHF_Down", &H_pt_jesPileUpPtHF_Down, &b_H_pt_jesPileUpPtHF_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpMuZero_Up", &H_pt_jesPileUpMuZero_Up, &b_H_pt_jesPileUpMuZero_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpMuZero_Down", &H_pt_jesPileUpMuZero_Down, &b_H_pt_jesPileUpMuZero_Down);
   fChain->SetBranchAddress("H_pt_jesPileUpEnvelope_Up", &H_pt_jesPileUpEnvelope_Up, &b_H_pt_jesPileUpEnvelope_Up);
   fChain->SetBranchAddress("H_pt_jesPileUpEnvelope_Down", &H_pt_jesPileUpEnvelope_Down, &b_H_pt_jesPileUpEnvelope_Down);
   fChain->SetBranchAddress("H_pt_jesTotal_Up", &H_pt_jesTotal_Up, &b_H_pt_jesTotal_Up);
   fChain->SetBranchAddress("H_pt_jesTotal_Down", &H_pt_jesTotal_Down, &b_H_pt_jesTotal_Down);
   fChain->SetBranchAddress("H_pt_minmax_Up", &H_pt_minmax_Up, &b_H_pt_minmax_Up);
   fChain->SetBranchAddress("H_pt_minmax_Down", &H_pt_minmax_Down, &b_H_pt_minmax_Down);
   fChain->SetBranchAddress("H_eta", &H_eta, &b_H_eta);
   fChain->SetBranchAddress("H_eta_jer_Up", &H_eta_jer_Up, &b_H_eta_jer_Up);
   fChain->SetBranchAddress("H_eta_jer_Down", &H_eta_jer_Down, &b_H_eta_jer_Down);
   fChain->SetBranchAddress("H_eta_jesAbsoluteStat_Up", &H_eta_jesAbsoluteStat_Up, &b_H_eta_jesAbsoluteStat_Up);
   fChain->SetBranchAddress("H_eta_jesAbsoluteStat_Down", &H_eta_jesAbsoluteStat_Down, &b_H_eta_jesAbsoluteStat_Down);
   fChain->SetBranchAddress("H_eta_jesAbsoluteScale_Up", &H_eta_jesAbsoluteScale_Up, &b_H_eta_jesAbsoluteScale_Up);
   fChain->SetBranchAddress("H_eta_jesAbsoluteScale_Down", &H_eta_jesAbsoluteScale_Down, &b_H_eta_jesAbsoluteScale_Down);
   fChain->SetBranchAddress("H_eta_jesAbsoluteFlavMap_Up", &H_eta_jesAbsoluteFlavMap_Up, &b_H_eta_jesAbsoluteFlavMap_Up);
   fChain->SetBranchAddress("H_eta_jesAbsoluteFlavMap_Down", &H_eta_jesAbsoluteFlavMap_Down, &b_H_eta_jesAbsoluteFlavMap_Down);
   fChain->SetBranchAddress("H_eta_jesAbsoluteMPFBias_Up", &H_eta_jesAbsoluteMPFBias_Up, &b_H_eta_jesAbsoluteMPFBias_Up);
   fChain->SetBranchAddress("H_eta_jesAbsoluteMPFBias_Down", &H_eta_jesAbsoluteMPFBias_Down, &b_H_eta_jesAbsoluteMPFBias_Down);
   fChain->SetBranchAddress("H_eta_jesFragmentation_Up", &H_eta_jesFragmentation_Up, &b_H_eta_jesFragmentation_Up);
   fChain->SetBranchAddress("H_eta_jesFragmentation_Down", &H_eta_jesFragmentation_Down, &b_H_eta_jesFragmentation_Down);
   fChain->SetBranchAddress("H_eta_jesSinglePionECAL_Up", &H_eta_jesSinglePionECAL_Up, &b_H_eta_jesSinglePionECAL_Up);
   fChain->SetBranchAddress("H_eta_jesSinglePionECAL_Down", &H_eta_jesSinglePionECAL_Down, &b_H_eta_jesSinglePionECAL_Down);
   fChain->SetBranchAddress("H_eta_jesSinglePionHCAL_Up", &H_eta_jesSinglePionHCAL_Up, &b_H_eta_jesSinglePionHCAL_Up);
   fChain->SetBranchAddress("H_eta_jesSinglePionHCAL_Down", &H_eta_jesSinglePionHCAL_Down, &b_H_eta_jesSinglePionHCAL_Down);
   fChain->SetBranchAddress("H_eta_jesFlavorQCD_Up", &H_eta_jesFlavorQCD_Up, &b_H_eta_jesFlavorQCD_Up);
   fChain->SetBranchAddress("H_eta_jesFlavorQCD_Down", &H_eta_jesFlavorQCD_Down, &b_H_eta_jesFlavorQCD_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeJEREC1_Up", &H_eta_jesRelativeJEREC1_Up, &b_H_eta_jesRelativeJEREC1_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeJEREC1_Down", &H_eta_jesRelativeJEREC1_Down, &b_H_eta_jesRelativeJEREC1_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeJEREC2_Up", &H_eta_jesRelativeJEREC2_Up, &b_H_eta_jesRelativeJEREC2_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeJEREC2_Down", &H_eta_jesRelativeJEREC2_Down, &b_H_eta_jesRelativeJEREC2_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeJERHF_Up", &H_eta_jesRelativeJERHF_Up, &b_H_eta_jesRelativeJERHF_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeJERHF_Down", &H_eta_jesRelativeJERHF_Down, &b_H_eta_jesRelativeJERHF_Down);
   fChain->SetBranchAddress("H_eta_jesRelativePtBB_Up", &H_eta_jesRelativePtBB_Up, &b_H_eta_jesRelativePtBB_Up);
   fChain->SetBranchAddress("H_eta_jesRelativePtBB_Down", &H_eta_jesRelativePtBB_Down, &b_H_eta_jesRelativePtBB_Down);
   fChain->SetBranchAddress("H_eta_jesRelativePtEC1_Up", &H_eta_jesRelativePtEC1_Up, &b_H_eta_jesRelativePtEC1_Up);
   fChain->SetBranchAddress("H_eta_jesRelativePtEC1_Down", &H_eta_jesRelativePtEC1_Down, &b_H_eta_jesRelativePtEC1_Down);
   fChain->SetBranchAddress("H_eta_jesRelativePtEC2_Up", &H_eta_jesRelativePtEC2_Up, &b_H_eta_jesRelativePtEC2_Up);
   fChain->SetBranchAddress("H_eta_jesRelativePtEC2_Down", &H_eta_jesRelativePtEC2_Down, &b_H_eta_jesRelativePtEC2_Down);
   fChain->SetBranchAddress("H_eta_jesRelativePtHF_Up", &H_eta_jesRelativePtHF_Up, &b_H_eta_jesRelativePtHF_Up);
   fChain->SetBranchAddress("H_eta_jesRelativePtHF_Down", &H_eta_jesRelativePtHF_Down, &b_H_eta_jesRelativePtHF_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeBal_Up", &H_eta_jesRelativeBal_Up, &b_H_eta_jesRelativeBal_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeBal_Down", &H_eta_jesRelativeBal_Down, &b_H_eta_jesRelativeBal_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeFSR_Up", &H_eta_jesRelativeFSR_Up, &b_H_eta_jesRelativeFSR_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeFSR_Down", &H_eta_jesRelativeFSR_Down, &b_H_eta_jesRelativeFSR_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeStatFSR_Up", &H_eta_jesRelativeStatFSR_Up, &b_H_eta_jesRelativeStatFSR_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeStatFSR_Down", &H_eta_jesRelativeStatFSR_Down, &b_H_eta_jesRelativeStatFSR_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeStatEC_Up", &H_eta_jesRelativeStatEC_Up, &b_H_eta_jesRelativeStatEC_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeStatEC_Down", &H_eta_jesRelativeStatEC_Down, &b_H_eta_jesRelativeStatEC_Down);
   fChain->SetBranchAddress("H_eta_jesRelativeStatHF_Up", &H_eta_jesRelativeStatHF_Up, &b_H_eta_jesRelativeStatHF_Up);
   fChain->SetBranchAddress("H_eta_jesRelativeStatHF_Down", &H_eta_jesRelativeStatHF_Down, &b_H_eta_jesRelativeStatHF_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpDataMC_Up", &H_eta_jesPileUpDataMC_Up, &b_H_eta_jesPileUpDataMC_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpDataMC_Down", &H_eta_jesPileUpDataMC_Down, &b_H_eta_jesPileUpDataMC_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpPtRef_Up", &H_eta_jesPileUpPtRef_Up, &b_H_eta_jesPileUpPtRef_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpPtRef_Down", &H_eta_jesPileUpPtRef_Down, &b_H_eta_jesPileUpPtRef_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpPtBB_Up", &H_eta_jesPileUpPtBB_Up, &b_H_eta_jesPileUpPtBB_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpPtBB_Down", &H_eta_jesPileUpPtBB_Down, &b_H_eta_jesPileUpPtBB_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpPtEC1_Up", &H_eta_jesPileUpPtEC1_Up, &b_H_eta_jesPileUpPtEC1_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpPtEC1_Down", &H_eta_jesPileUpPtEC1_Down, &b_H_eta_jesPileUpPtEC1_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpPtEC2_Up", &H_eta_jesPileUpPtEC2_Up, &b_H_eta_jesPileUpPtEC2_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpPtEC2_Down", &H_eta_jesPileUpPtEC2_Down, &b_H_eta_jesPileUpPtEC2_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpPtHF_Up", &H_eta_jesPileUpPtHF_Up, &b_H_eta_jesPileUpPtHF_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpPtHF_Down", &H_eta_jesPileUpPtHF_Down, &b_H_eta_jesPileUpPtHF_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpMuZero_Up", &H_eta_jesPileUpMuZero_Up, &b_H_eta_jesPileUpMuZero_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpMuZero_Down", &H_eta_jesPileUpMuZero_Down, &b_H_eta_jesPileUpMuZero_Down);
   fChain->SetBranchAddress("H_eta_jesPileUpEnvelope_Up", &H_eta_jesPileUpEnvelope_Up, &b_H_eta_jesPileUpEnvelope_Up);
   fChain->SetBranchAddress("H_eta_jesPileUpEnvelope_Down", &H_eta_jesPileUpEnvelope_Down, &b_H_eta_jesPileUpEnvelope_Down);
   fChain->SetBranchAddress("H_eta_jesTotal_Up", &H_eta_jesTotal_Up, &b_H_eta_jesTotal_Up);
   fChain->SetBranchAddress("H_eta_jesTotal_Down", &H_eta_jesTotal_Down, &b_H_eta_jesTotal_Down);
   fChain->SetBranchAddress("H_eta_minmax_Up", &H_eta_minmax_Up, &b_H_eta_minmax_Up);
   fChain->SetBranchAddress("H_eta_minmax_Down", &H_eta_minmax_Down, &b_H_eta_minmax_Down);
   fChain->SetBranchAddress("H_phi", &H_phi, &b_H_phi);
   fChain->SetBranchAddress("H_phi_jer_Up", &H_phi_jer_Up, &b_H_phi_jer_Up);
   fChain->SetBranchAddress("H_phi_jer_Down", &H_phi_jer_Down, &b_H_phi_jer_Down);
   fChain->SetBranchAddress("H_phi_jesAbsoluteStat_Up", &H_phi_jesAbsoluteStat_Up, &b_H_phi_jesAbsoluteStat_Up);
   fChain->SetBranchAddress("H_phi_jesAbsoluteStat_Down", &H_phi_jesAbsoluteStat_Down, &b_H_phi_jesAbsoluteStat_Down);
   fChain->SetBranchAddress("H_phi_jesAbsoluteScale_Up", &H_phi_jesAbsoluteScale_Up, &b_H_phi_jesAbsoluteScale_Up);
   fChain->SetBranchAddress("H_phi_jesAbsoluteScale_Down", &H_phi_jesAbsoluteScale_Down, &b_H_phi_jesAbsoluteScale_Down);
   fChain->SetBranchAddress("H_phi_jesAbsoluteFlavMap_Up", &H_phi_jesAbsoluteFlavMap_Up, &b_H_phi_jesAbsoluteFlavMap_Up);
   fChain->SetBranchAddress("H_phi_jesAbsoluteFlavMap_Down", &H_phi_jesAbsoluteFlavMap_Down, &b_H_phi_jesAbsoluteFlavMap_Down);
   fChain->SetBranchAddress("H_phi_jesAbsoluteMPFBias_Up", &H_phi_jesAbsoluteMPFBias_Up, &b_H_phi_jesAbsoluteMPFBias_Up);
   fChain->SetBranchAddress("H_phi_jesAbsoluteMPFBias_Down", &H_phi_jesAbsoluteMPFBias_Down, &b_H_phi_jesAbsoluteMPFBias_Down);
   fChain->SetBranchAddress("H_phi_jesFragmentation_Up", &H_phi_jesFragmentation_Up, &b_H_phi_jesFragmentation_Up);
   fChain->SetBranchAddress("H_phi_jesFragmentation_Down", &H_phi_jesFragmentation_Down, &b_H_phi_jesFragmentation_Down);
   fChain->SetBranchAddress("H_phi_jesSinglePionECAL_Up", &H_phi_jesSinglePionECAL_Up, &b_H_phi_jesSinglePionECAL_Up);
   fChain->SetBranchAddress("H_phi_jesSinglePionECAL_Down", &H_phi_jesSinglePionECAL_Down, &b_H_phi_jesSinglePionECAL_Down);
   fChain->SetBranchAddress("H_phi_jesSinglePionHCAL_Up", &H_phi_jesSinglePionHCAL_Up, &b_H_phi_jesSinglePionHCAL_Up);
   fChain->SetBranchAddress("H_phi_jesSinglePionHCAL_Down", &H_phi_jesSinglePionHCAL_Down, &b_H_phi_jesSinglePionHCAL_Down);
   fChain->SetBranchAddress("H_phi_jesFlavorQCD_Up", &H_phi_jesFlavorQCD_Up, &b_H_phi_jesFlavorQCD_Up);
   fChain->SetBranchAddress("H_phi_jesFlavorQCD_Down", &H_phi_jesFlavorQCD_Down, &b_H_phi_jesFlavorQCD_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeJEREC1_Up", &H_phi_jesRelativeJEREC1_Up, &b_H_phi_jesRelativeJEREC1_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeJEREC1_Down", &H_phi_jesRelativeJEREC1_Down, &b_H_phi_jesRelativeJEREC1_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeJEREC2_Up", &H_phi_jesRelativeJEREC2_Up, &b_H_phi_jesRelativeJEREC2_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeJEREC2_Down", &H_phi_jesRelativeJEREC2_Down, &b_H_phi_jesRelativeJEREC2_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeJERHF_Up", &H_phi_jesRelativeJERHF_Up, &b_H_phi_jesRelativeJERHF_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeJERHF_Down", &H_phi_jesRelativeJERHF_Down, &b_H_phi_jesRelativeJERHF_Down);
   fChain->SetBranchAddress("H_phi_jesRelativePtBB_Up", &H_phi_jesRelativePtBB_Up, &b_H_phi_jesRelativePtBB_Up);
   fChain->SetBranchAddress("H_phi_jesRelativePtBB_Down", &H_phi_jesRelativePtBB_Down, &b_H_phi_jesRelativePtBB_Down);
   fChain->SetBranchAddress("H_phi_jesRelativePtEC1_Up", &H_phi_jesRelativePtEC1_Up, &b_H_phi_jesRelativePtEC1_Up);
   fChain->SetBranchAddress("H_phi_jesRelativePtEC1_Down", &H_phi_jesRelativePtEC1_Down, &b_H_phi_jesRelativePtEC1_Down);
   fChain->SetBranchAddress("H_phi_jesRelativePtEC2_Up", &H_phi_jesRelativePtEC2_Up, &b_H_phi_jesRelativePtEC2_Up);
   fChain->SetBranchAddress("H_phi_jesRelativePtEC2_Down", &H_phi_jesRelativePtEC2_Down, &b_H_phi_jesRelativePtEC2_Down);
   fChain->SetBranchAddress("H_phi_jesRelativePtHF_Up", &H_phi_jesRelativePtHF_Up, &b_H_phi_jesRelativePtHF_Up);
   fChain->SetBranchAddress("H_phi_jesRelativePtHF_Down", &H_phi_jesRelativePtHF_Down, &b_H_phi_jesRelativePtHF_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeBal_Up", &H_phi_jesRelativeBal_Up, &b_H_phi_jesRelativeBal_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeBal_Down", &H_phi_jesRelativeBal_Down, &b_H_phi_jesRelativeBal_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeFSR_Up", &H_phi_jesRelativeFSR_Up, &b_H_phi_jesRelativeFSR_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeFSR_Down", &H_phi_jesRelativeFSR_Down, &b_H_phi_jesRelativeFSR_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeStatFSR_Up", &H_phi_jesRelativeStatFSR_Up, &b_H_phi_jesRelativeStatFSR_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeStatFSR_Down", &H_phi_jesRelativeStatFSR_Down, &b_H_phi_jesRelativeStatFSR_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeStatEC_Up", &H_phi_jesRelativeStatEC_Up, &b_H_phi_jesRelativeStatEC_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeStatEC_Down", &H_phi_jesRelativeStatEC_Down, &b_H_phi_jesRelativeStatEC_Down);
   fChain->SetBranchAddress("H_phi_jesRelativeStatHF_Up", &H_phi_jesRelativeStatHF_Up, &b_H_phi_jesRelativeStatHF_Up);
   fChain->SetBranchAddress("H_phi_jesRelativeStatHF_Down", &H_phi_jesRelativeStatHF_Down, &b_H_phi_jesRelativeStatHF_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpDataMC_Up", &H_phi_jesPileUpDataMC_Up, &b_H_phi_jesPileUpDataMC_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpDataMC_Down", &H_phi_jesPileUpDataMC_Down, &b_H_phi_jesPileUpDataMC_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpPtRef_Up", &H_phi_jesPileUpPtRef_Up, &b_H_phi_jesPileUpPtRef_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpPtRef_Down", &H_phi_jesPileUpPtRef_Down, &b_H_phi_jesPileUpPtRef_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpPtBB_Up", &H_phi_jesPileUpPtBB_Up, &b_H_phi_jesPileUpPtBB_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpPtBB_Down", &H_phi_jesPileUpPtBB_Down, &b_H_phi_jesPileUpPtBB_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpPtEC1_Up", &H_phi_jesPileUpPtEC1_Up, &b_H_phi_jesPileUpPtEC1_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpPtEC1_Down", &H_phi_jesPileUpPtEC1_Down, &b_H_phi_jesPileUpPtEC1_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpPtEC2_Up", &H_phi_jesPileUpPtEC2_Up, &b_H_phi_jesPileUpPtEC2_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpPtEC2_Down", &H_phi_jesPileUpPtEC2_Down, &b_H_phi_jesPileUpPtEC2_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpPtHF_Up", &H_phi_jesPileUpPtHF_Up, &b_H_phi_jesPileUpPtHF_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpPtHF_Down", &H_phi_jesPileUpPtHF_Down, &b_H_phi_jesPileUpPtHF_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpMuZero_Up", &H_phi_jesPileUpMuZero_Up, &b_H_phi_jesPileUpMuZero_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpMuZero_Down", &H_phi_jesPileUpMuZero_Down, &b_H_phi_jesPileUpMuZero_Down);
   fChain->SetBranchAddress("H_phi_jesPileUpEnvelope_Up", &H_phi_jesPileUpEnvelope_Up, &b_H_phi_jesPileUpEnvelope_Up);
   fChain->SetBranchAddress("H_phi_jesPileUpEnvelope_Down", &H_phi_jesPileUpEnvelope_Down, &b_H_phi_jesPileUpEnvelope_Down);
   fChain->SetBranchAddress("H_phi_jesTotal_Up", &H_phi_jesTotal_Up, &b_H_phi_jesTotal_Up);
   fChain->SetBranchAddress("H_phi_jesTotal_Down", &H_phi_jesTotal_Down, &b_H_phi_jesTotal_Down);
   fChain->SetBranchAddress("H_phi_minmax_Up", &H_phi_minmax_Up, &b_H_phi_minmax_Up);
   fChain->SetBranchAddress("H_phi_minmax_Down", &H_phi_minmax_Down, &b_H_phi_minmax_Down);
   fChain->SetBranchAddress("H_mass", &H_mass, &b_H_mass);
   fChain->SetBranchAddress("H_mass_jer_Up", &H_mass_jer_Up, &b_H_mass_jer_Up);
   fChain->SetBranchAddress("H_mass_jer_Down", &H_mass_jer_Down, &b_H_mass_jer_Down);
   fChain->SetBranchAddress("H_mass_jesAbsoluteStat_Up", &H_mass_jesAbsoluteStat_Up, &b_H_mass_jesAbsoluteStat_Up);
   fChain->SetBranchAddress("H_mass_jesAbsoluteStat_Down", &H_mass_jesAbsoluteStat_Down, &b_H_mass_jesAbsoluteStat_Down);
   fChain->SetBranchAddress("H_mass_jesAbsoluteScale_Up", &H_mass_jesAbsoluteScale_Up, &b_H_mass_jesAbsoluteScale_Up);
   fChain->SetBranchAddress("H_mass_jesAbsoluteScale_Down", &H_mass_jesAbsoluteScale_Down, &b_H_mass_jesAbsoluteScale_Down);
   fChain->SetBranchAddress("H_mass_jesAbsoluteFlavMap_Up", &H_mass_jesAbsoluteFlavMap_Up, &b_H_mass_jesAbsoluteFlavMap_Up);
   fChain->SetBranchAddress("H_mass_jesAbsoluteFlavMap_Down", &H_mass_jesAbsoluteFlavMap_Down, &b_H_mass_jesAbsoluteFlavMap_Down);
   fChain->SetBranchAddress("H_mass_jesAbsoluteMPFBias_Up", &H_mass_jesAbsoluteMPFBias_Up, &b_H_mass_jesAbsoluteMPFBias_Up);
   fChain->SetBranchAddress("H_mass_jesAbsoluteMPFBias_Down", &H_mass_jesAbsoluteMPFBias_Down, &b_H_mass_jesAbsoluteMPFBias_Down);
   fChain->SetBranchAddress("H_mass_jesFragmentation_Up", &H_mass_jesFragmentation_Up, &b_H_mass_jesFragmentation_Up);
   fChain->SetBranchAddress("H_mass_jesFragmentation_Down", &H_mass_jesFragmentation_Down, &b_H_mass_jesFragmentation_Down);
   fChain->SetBranchAddress("H_mass_jesSinglePionECAL_Up", &H_mass_jesSinglePionECAL_Up, &b_H_mass_jesSinglePionECAL_Up);
   fChain->SetBranchAddress("H_mass_jesSinglePionECAL_Down", &H_mass_jesSinglePionECAL_Down, &b_H_mass_jesSinglePionECAL_Down);
   fChain->SetBranchAddress("H_mass_jesSinglePionHCAL_Up", &H_mass_jesSinglePionHCAL_Up, &b_H_mass_jesSinglePionHCAL_Up);
   fChain->SetBranchAddress("H_mass_jesSinglePionHCAL_Down", &H_mass_jesSinglePionHCAL_Down, &b_H_mass_jesSinglePionHCAL_Down);
   fChain->SetBranchAddress("H_mass_jesFlavorQCD_Up", &H_mass_jesFlavorQCD_Up, &b_H_mass_jesFlavorQCD_Up);
   fChain->SetBranchAddress("H_mass_jesFlavorQCD_Down", &H_mass_jesFlavorQCD_Down, &b_H_mass_jesFlavorQCD_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeJEREC1_Up", &H_mass_jesRelativeJEREC1_Up, &b_H_mass_jesRelativeJEREC1_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeJEREC1_Down", &H_mass_jesRelativeJEREC1_Down, &b_H_mass_jesRelativeJEREC1_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeJEREC2_Up", &H_mass_jesRelativeJEREC2_Up, &b_H_mass_jesRelativeJEREC2_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeJEREC2_Down", &H_mass_jesRelativeJEREC2_Down, &b_H_mass_jesRelativeJEREC2_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeJERHF_Up", &H_mass_jesRelativeJERHF_Up, &b_H_mass_jesRelativeJERHF_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeJERHF_Down", &H_mass_jesRelativeJERHF_Down, &b_H_mass_jesRelativeJERHF_Down);
   fChain->SetBranchAddress("H_mass_jesRelativePtBB_Up", &H_mass_jesRelativePtBB_Up, &b_H_mass_jesRelativePtBB_Up);
   fChain->SetBranchAddress("H_mass_jesRelativePtBB_Down", &H_mass_jesRelativePtBB_Down, &b_H_mass_jesRelativePtBB_Down);
   fChain->SetBranchAddress("H_mass_jesRelativePtEC1_Up", &H_mass_jesRelativePtEC1_Up, &b_H_mass_jesRelativePtEC1_Up);
   fChain->SetBranchAddress("H_mass_jesRelativePtEC1_Down", &H_mass_jesRelativePtEC1_Down, &b_H_mass_jesRelativePtEC1_Down);
   fChain->SetBranchAddress("H_mass_jesRelativePtEC2_Up", &H_mass_jesRelativePtEC2_Up, &b_H_mass_jesRelativePtEC2_Up);
   fChain->SetBranchAddress("H_mass_jesRelativePtEC2_Down", &H_mass_jesRelativePtEC2_Down, &b_H_mass_jesRelativePtEC2_Down);
   fChain->SetBranchAddress("H_mass_jesRelativePtHF_Up", &H_mass_jesRelativePtHF_Up, &b_H_mass_jesRelativePtHF_Up);
   fChain->SetBranchAddress("H_mass_jesRelativePtHF_Down", &H_mass_jesRelativePtHF_Down, &b_H_mass_jesRelativePtHF_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeBal_Up", &H_mass_jesRelativeBal_Up, &b_H_mass_jesRelativeBal_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeBal_Down", &H_mass_jesRelativeBal_Down, &b_H_mass_jesRelativeBal_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeFSR_Up", &H_mass_jesRelativeFSR_Up, &b_H_mass_jesRelativeFSR_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeFSR_Down", &H_mass_jesRelativeFSR_Down, &b_H_mass_jesRelativeFSR_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeStatFSR_Up", &H_mass_jesRelativeStatFSR_Up, &b_H_mass_jesRelativeStatFSR_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeStatFSR_Down", &H_mass_jesRelativeStatFSR_Down, &b_H_mass_jesRelativeStatFSR_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeStatEC_Up", &H_mass_jesRelativeStatEC_Up, &b_H_mass_jesRelativeStatEC_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeStatEC_Down", &H_mass_jesRelativeStatEC_Down, &b_H_mass_jesRelativeStatEC_Down);
   fChain->SetBranchAddress("H_mass_jesRelativeStatHF_Up", &H_mass_jesRelativeStatHF_Up, &b_H_mass_jesRelativeStatHF_Up);
   fChain->SetBranchAddress("H_mass_jesRelativeStatHF_Down", &H_mass_jesRelativeStatHF_Down, &b_H_mass_jesRelativeStatHF_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpDataMC_Up", &H_mass_jesPileUpDataMC_Up, &b_H_mass_jesPileUpDataMC_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpDataMC_Down", &H_mass_jesPileUpDataMC_Down, &b_H_mass_jesPileUpDataMC_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpPtRef_Up", &H_mass_jesPileUpPtRef_Up, &b_H_mass_jesPileUpPtRef_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpPtRef_Down", &H_mass_jesPileUpPtRef_Down, &b_H_mass_jesPileUpPtRef_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpPtBB_Up", &H_mass_jesPileUpPtBB_Up, &b_H_mass_jesPileUpPtBB_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpPtBB_Down", &H_mass_jesPileUpPtBB_Down, &b_H_mass_jesPileUpPtBB_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpPtEC1_Up", &H_mass_jesPileUpPtEC1_Up, &b_H_mass_jesPileUpPtEC1_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpPtEC1_Down", &H_mass_jesPileUpPtEC1_Down, &b_H_mass_jesPileUpPtEC1_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpPtEC2_Up", &H_mass_jesPileUpPtEC2_Up, &b_H_mass_jesPileUpPtEC2_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpPtEC2_Down", &H_mass_jesPileUpPtEC2_Down, &b_H_mass_jesPileUpPtEC2_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpPtHF_Up", &H_mass_jesPileUpPtHF_Up, &b_H_mass_jesPileUpPtHF_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpPtHF_Down", &H_mass_jesPileUpPtHF_Down, &b_H_mass_jesPileUpPtHF_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpMuZero_Up", &H_mass_jesPileUpMuZero_Up, &b_H_mass_jesPileUpMuZero_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpMuZero_Down", &H_mass_jesPileUpMuZero_Down, &b_H_mass_jesPileUpMuZero_Down);
   fChain->SetBranchAddress("H_mass_jesPileUpEnvelope_Up", &H_mass_jesPileUpEnvelope_Up, &b_H_mass_jesPileUpEnvelope_Up);
   fChain->SetBranchAddress("H_mass_jesPileUpEnvelope_Down", &H_mass_jesPileUpEnvelope_Down, &b_H_mass_jesPileUpEnvelope_Down);
   fChain->SetBranchAddress("H_mass_jesTotal_Up", &H_mass_jesTotal_Up, &b_H_mass_jesTotal_Up);
   fChain->SetBranchAddress("H_mass_jesTotal_Down", &H_mass_jesTotal_Down, &b_H_mass_jesTotal_Down);
   fChain->SetBranchAddress("H_mass_minmax_Up", &H_mass_minmax_Up, &b_H_mass_minmax_Up);
   fChain->SetBranchAddress("H_mass_minmax_Down", &H_mass_minmax_Down, &b_H_mass_minmax_Down);
   fChain->SetBranchAddress("Jet_pt_minmaxUp", Jet_pt_minmaxUp, &b_Jet_pt_minmaxUp);
   fChain->SetBranchAddress("Jet_pt_minmaxDown", Jet_pt_minmaxDown, &b_Jet_pt_minmaxDown);
   fChain->SetBranchAddress("Jet_mass_minmaxUp", Jet_mass_minmaxUp, &b_Jet_mass_minmaxUp);
   fChain->SetBranchAddress("Jet_mass_minmaxDown", Jet_mass_minmaxDown, &b_Jet_mass_minmaxDown);
   fChain->SetBranchAddress("isSignal", &isSignal, &b_isSignal);
   fChain->SetBranchAddress("isWH", &isWH, &b_isWH);
   fChain->SetBranchAddress("isData", &isData, &b_isData);
   fChain->SetBranchAddress("nGenVbosons", &nGenVbosons, &b_nGenVbosons);
   fChain->SetBranchAddress("GenVbosons_pt", GenVbosons_pt, &b_GenVbosons_pt);
   fChain->SetBranchAddress("GenVbosons_pdgId", GenVbosons_pdgId, &b_GenVbosons_pdgId);
   fChain->SetBranchAddress("GenVbosons_GenPartIdx", GenVbosons_GenPartIdx, &b_GenVbosons_GenPartIdx);
   fChain->SetBranchAddress("nGenTop", &nGenTop, &b_nGenTop);
   fChain->SetBranchAddress("GenTop_pt", &GenTop_pt, &b_GenTop_pt);
   fChain->SetBranchAddress("GenTop_GenPartIdx", &GenTop_GenPartIdx, &b_GenTop_GenPartIdx);
   fChain->SetBranchAddress("nGenHiggsBoson", &nGenHiggsBoson, &b_nGenHiggsBoson);
   fChain->SetBranchAddress("GenHiggsBoson_pt", &GenHiggsBoson_pt, &b_GenHiggsBoson_pt);
   fChain->SetBranchAddress("GenHiggsBoson_GenPartIdx", &GenHiggsBoson_GenPartIdx, &b_GenHiggsBoson_GenPartIdx);
   fChain->SetBranchAddress("VtypeSim", &VtypeSim, &b_VtypeSim);
   fChain->SetBranchAddress("FitCorr", FitCorr, &b_FitCorr);
   fChain->SetBranchAddress("top_mass", &top_mass, &b_top_mass);
   fChain->SetBranchAddress("V_mt", &V_mt, &b_V_mt);
   Notify();
}

Bool_t myclass::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void myclass::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t myclass::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef myclass_cxx
