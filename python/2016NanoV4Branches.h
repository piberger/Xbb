//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Jul 29 17:45:05 2018 by ROOT version 5.34/36
// from TTree Events/Events
// found on file: root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/hbb/ntuples/VHbbPostNano/2016/V4/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/arizzi-RunIIMoriond17-DeepAndR98/180517_163627/0000/tree_1.root
//////////////////////////////////////////////////////////

#ifndef Myclass_h
#define Myclass_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class Myclass {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

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
   Float_t         Electron_deltaEtaSC[7];   //[nElectron]
   Float_t         Electron_dr03EcalRecHitSumEt[7];   //[nElectron]
   Float_t         Electron_dr03HcalDepth1TowerSumEt[7];   //[nElectron]
   Float_t         Electron_dr03TkSumPt[7];   //[nElectron]
   Float_t         Electron_dxy[7];   //[nElectron]
   Float_t         Electron_dxyErr[7];   //[nElectron]
   Float_t         Electron_dz[7];   //[nElectron]
   Float_t         Electron_dzErr[7];   //[nElectron]
   Float_t         Electron_eCorr[7];   //[nElectron]
   Float_t         Electron_eInvMinusPInv[7];   //[nElectron]
   Float_t         Electron_energyErr[7];   //[nElectron]
   Float_t         Electron_eta[7];   //[nElectron]
   Float_t         Electron_hoe[7];   //[nElectron]
   Float_t         Electron_ip3d[7];   //[nElectron]
   Float_t         Electron_mass[7];   //[nElectron]
   Float_t         Electron_miniPFRelIso_all[7];   //[nElectron]
   Float_t         Electron_miniPFRelIso_chg[7];   //[nElectron]
   Float_t         Electron_mvaSpring16GP[7];   //[nElectron]
   Float_t         Electron_mvaSpring16HZZ[7];   //[nElectron]
   Float_t         Electron_pfRelIso03_all[7];   //[nElectron]
   Float_t         Electron_pfRelIso03_chg[7];   //[nElectron]
   Float_t         Electron_phi[7];   //[nElectron]
   Float_t         Electron_pt[7];   //[nElectron]
   Float_t         Electron_r9[7];   //[nElectron]
   Float_t         Electron_sieie[7];   //[nElectron]
   Float_t         Electron_sip3d[7];   //[nElectron]
   Float_t         Electron_mvaTTH[7];   //[nElectron]
   Int_t           Electron_charge[7];   //[nElectron]
   Int_t           Electron_cutBased[7];   //[nElectron]
   Int_t           Electron_cutBased_HLTPreSel[7];   //[nElectron]
   Int_t           Electron_jetIdx[7];   //[nElectron]
   Int_t           Electron_pdgId[7];   //[nElectron]
   Int_t           Electron_photonIdx[7];   //[nElectron]
   Int_t           Electron_tightCharge[7];   //[nElectron]
   Int_t           Electron_vidNestedWPBitmap[7];   //[nElectron]
   Bool_t          Electron_convVeto[7];   //[nElectron]
   Bool_t          Electron_cutBased_HEEP[7];   //[nElectron]
   Bool_t          Electron_isPFcand[7];   //[nElectron]
   UChar_t         Electron_lostHits[7];   //[nElectron]
   Bool_t          Electron_mvaSpring16GP_WP80[7];   //[nElectron]
   Bool_t          Electron_mvaSpring16GP_WP90[7];   //[nElectron]
   Bool_t          Electron_mvaSpring16HZZ_WPL[7];   //[nElectron]
   UChar_t         Flag_BadChargedCandidateFilter;
   UChar_t         Flag_BadGlobalMuon;
   UChar_t         Flag_BadPFMuonFilter;
   UChar_t         Flag_CloneGlobalMuon;
   UInt_t          nFatJet;
   Float_t         FatJet_area[3];   //[nFatJet]
   Float_t         FatJet_btagCMVA[3];   //[nFatJet]
   Float_t         FatJet_btagCSVV2[3];   //[nFatJet]
   Float_t         FatJet_btagDeepB[3];   //[nFatJet]
   Float_t         FatJet_btagHbb[3];   //[nFatJet]
   Float_t         FatJet_eta[3];   //[nFatJet]
   Float_t         FatJet_mass[3];   //[nFatJet]
   Float_t         FatJet_msoftdrop[3];   //[nFatJet]
   Float_t         FatJet_msoftdrop_chs[3];   //[nFatJet]
   Float_t         FatJet_n2b1[3];   //[nFatJet]
   Float_t         FatJet_n3b1[3];   //[nFatJet]
   Float_t         FatJet_phi[3];   //[nFatJet]
   Float_t         FatJet_pt[3];   //[nFatJet]
   Float_t         FatJet_tau1[3];   //[nFatJet]
   Float_t         FatJet_tau2[3];   //[nFatJet]
   Float_t         FatJet_tau3[3];   //[nFatJet]
   Float_t         FatJet_tau4[3];   //[nFatJet]
   Int_t           FatJet_jetId[3];   //[nFatJet]
   Int_t           FatJet_subJetIdx1[3];   //[nFatJet]
   Int_t           FatJet_subJetIdx2[3];   //[nFatJet]
   UInt_t          nGenJetAK8;
   Float_t         GenJetAK8_eta[3];   //[nGenJetAK8]
   Float_t         GenJetAK8_mass[3];   //[nGenJetAK8]
   Float_t         GenJetAK8_phi[3];   //[nGenJetAK8]
   Float_t         GenJetAK8_pt[3];   //[nGenJetAK8]
   UInt_t          nGenJet;
   Float_t         GenJet_eta[21];   //[nGenJet]
   Float_t         GenJet_mass[21];   //[nGenJet]
   Float_t         GenJet_phi[21];   //[nGenJet]
   Float_t         GenJet_pt[21];   //[nGenJet]
   UInt_t          nGenPart;
   Float_t         GenPart_eta[123];   //[nGenPart]
   Float_t         GenPart_mass[123];   //[nGenPart]
   Float_t         GenPart_phi[123];   //[nGenPart]
   Float_t         GenPart_pt[123];   //[nGenPart]
   Int_t           GenPart_genPartIdxMother[123];   //[nGenPart]
   Int_t           GenPart_pdgId[123];   //[nGenPart]
   Int_t           GenPart_status[123];   //[nGenPart]
   Int_t           GenPart_statusFlags[123];   //[nGenPart]
   Float_t         Generator_binvar;
   Float_t         Generator_scalePDF;
   Float_t         Generator_weight;
   Float_t         Generator_x1;
   Float_t         Generator_x2;
   Float_t         Generator_xpdf1;
   Float_t         Generator_xpdf2;
   Int_t           Generator_id1;
   Int_t           Generator_id2;
   UInt_t          nGenVisTau;
   Float_t         GenVisTau_eta[3];   //[nGenVisTau]
   Float_t         GenVisTau_mass[3];   //[nGenVisTau]
   Float_t         GenVisTau_phi[3];   //[nGenVisTau]
   Float_t         GenVisTau_pt[3];   //[nGenVisTau]
   Int_t           GenVisTau_charge[3];   //[nGenVisTau]
   Int_t           GenVisTau_genPartIdxMother[3];   //[nGenVisTau]
   Int_t           GenVisTau_status[3];   //[nGenVisTau]
   Float_t         genWeight;
   Float_t         LHEWeight_originalXWGTUP;
   UInt_t          nLHEPdfWeight;
   Float_t         LHEPdfWeight[101];   //[nLHEPdfWeight]
   UInt_t          nLHEScaleWeight;
   Float_t         LHEScaleWeight[9];   //[nLHEScaleWeight]
   UInt_t          nJet;
   Float_t         Jet_area[33];   //[nJet]
   Float_t         Jet_btagCMVA[33];   //[nJet]
   Float_t         Jet_btagCSVV2[33];   //[nJet]
   Float_t         Jet_btagDeepB[33];   //[nJet]
   Float_t         Jet_btagDeepC[33];   //[nJet]
   Float_t         Jet_btagDeepFlavB[33];   //[nJet]
   Float_t         Jet_chEmEF[33];   //[nJet]
   Float_t         Jet_chHEF[33];   //[nJet]
   Float_t         Jet_eta[33];   //[nJet]
   Float_t         Jet_mass[33];   //[nJet]
   Float_t         Jet_neEmEF[33];   //[nJet]
   Float_t         Jet_neHEF[33];   //[nJet]
   Float_t         Jet_phi[33];   //[nJet]
   Float_t         Jet_pt[33];   //[nJet]
   Float_t         Jet_qgl[33];   //[nJet]
   Float_t         Jet_rawFactor[33];   //[nJet]
   Float_t         Jet_bReg[33];   //[nJet]
   Float_t         Jet_bRegOld[33];   //[nJet]
   Float_t         Jet_bRegRes[33];   //[nJet]
   Int_t           Jet_electronIdx1[33];   //[nJet]
   Int_t           Jet_electronIdx2[33];   //[nJet]
   Int_t           Jet_jetId[33];   //[nJet]
   Int_t           Jet_muonIdx1[33];   //[nJet]
   Int_t           Jet_muonIdx2[33];   //[nJet]
   Int_t           Jet_nConstituents[33];   //[nJet]
   Int_t           Jet_nElectrons[33];   //[nJet]
   Int_t           Jet_nMuons[33];   //[nJet]
   Int_t           Jet_puId[33];   //[nJet]
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
   UInt_t          nPhoton;
   Float_t         Photon_eCorr[8];   //[nPhoton]
   Float_t         Photon_energyErr[8];   //[nPhoton]
   Float_t         Photon_eta[8];   //[nPhoton]
   Float_t         Photon_hoe[8];   //[nPhoton]
   Float_t         Photon_mass[8];   //[nPhoton]
   Float_t         Photon_mvaID[8];   //[nPhoton]
   Float_t         Photon_pfRelIso03_all[8];   //[nPhoton]
   Float_t         Photon_pfRelIso03_chg[8];   //[nPhoton]
   Float_t         Photon_phi[8];   //[nPhoton]
   Float_t         Photon_pt[8];   //[nPhoton]
   Float_t         Photon_r9[8];   //[nPhoton]
   Float_t         Photon_sieie[8];   //[nPhoton]
   Int_t           Photon_charge[8];   //[nPhoton]
   Int_t           Photon_cutBased[8];   //[nPhoton]
   Int_t           Photon_electronIdx[8];   //[nPhoton]
   Int_t           Photon_jetIdx[8];   //[nPhoton]
   Int_t           Photon_pdgId[8];   //[nPhoton]
   Int_t           Photon_vidNestedWPBitmap[8];   //[nPhoton]
   Bool_t          Photon_electronVeto[8];   //[nPhoton]
   Bool_t          Photon_isScEtaEB[8];   //[nPhoton]
   Bool_t          Photon_isScEtaEE[8];   //[nPhoton]
   Bool_t          Photon_mvaID_WP80[8];   //[nPhoton]
   Bool_t          Photon_mvaID_WP90[8];   //[nPhoton]
   Bool_t          Photon_pixelSeed[8];   //[nPhoton]
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
   Float_t         GenDressedLepton_eta[4];   //[nGenDressedLepton]
   Float_t         GenDressedLepton_mass[4];   //[nGenDressedLepton]
   Float_t         GenDressedLepton_phi[4];   //[nGenDressedLepton]
   Float_t         GenDressedLepton_pt[4];   //[nGenDressedLepton]
   Int_t           GenDressedLepton_pdgId[4];   //[nGenDressedLepton]
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
   UInt_t          nSubJet;
   Float_t         SubJet_btagCMVA[4];   //[nSubJet]
   Float_t         SubJet_btagCSVV2[4];   //[nSubJet]
   Float_t         SubJet_btagDeepB[4];   //[nSubJet]
   Float_t         SubJet_eta[4];   //[nSubJet]
   Float_t         SubJet_mass[4];   //[nSubJet]
   Float_t         SubJet_n2b1[4];   //[nSubJet]
   Float_t         SubJet_n3b1[4];   //[nSubJet]
   Float_t         SubJet_phi[4];   //[nSubJet]
   Float_t         SubJet_pt[4];   //[nSubJet]
   Float_t         SubJet_tau1[4];   //[nSubJet]
   Float_t         SubJet_tau2[4];   //[nSubJet]
   Float_t         SubJet_tau3[4];   //[nSubJet]
   Float_t         SubJet_tau4[4];   //[nSubJet]
   UInt_t          nTau;
   Float_t         Tau_chargedIso[6];   //[nTau]
   Float_t         Tau_dxy[6];   //[nTau]
   Float_t         Tau_dz[6];   //[nTau]
   Float_t         Tau_eta[6];   //[nTau]
   Float_t         Tau_leadTkDeltaEta[6];   //[nTau]
   Float_t         Tau_leadTkDeltaPhi[6];   //[nTau]
   Float_t         Tau_leadTkPtOverTauPt[6];   //[nTau]
   Float_t         Tau_mass[6];   //[nTau]
   Float_t         Tau_neutralIso[6];   //[nTau]
   Float_t         Tau_phi[6];   //[nTau]
   Float_t         Tau_photonsOutsideSignalCone[6];   //[nTau]
   Float_t         Tau_pt[6];   //[nTau]
   Float_t         Tau_puCorr[6];   //[nTau]
   Float_t         Tau_rawAntiEle[6];   //[nTau]
   Float_t         Tau_rawIso[6];   //[nTau]
   Float_t         Tau_rawIsodR03[6];   //[nTau]
   Float_t         Tau_rawMVAnewDM[6];   //[nTau]
   Float_t         Tau_rawMVAoldDM[6];   //[nTau]
   Float_t         Tau_rawMVAoldDMdR03[6];   //[nTau]
   Int_t           Tau_charge[6];   //[nTau]
   Int_t           Tau_decayMode[6];   //[nTau]
   Int_t           Tau_jetIdx[6];   //[nTau]
   Int_t           Tau_rawAntiEleCat[6];   //[nTau]
   UChar_t         Tau_idAntiEle[6];   //[nTau]
   UChar_t         Tau_idAntiMu[6];   //[nTau]
   Bool_t          Tau_idDecayMode[6];   //[nTau]
   Bool_t          Tau_idDecayModeNewDMs[6];   //[nTau]
   UChar_t         Tau_idMVAnew[6];   //[nTau]
   UChar_t         Tau_idMVAoldDM[6];   //[nTau]
   UChar_t         Tau_idMVAoldDMdR03[6];   //[nTau]
   Float_t         TkMET_phi;
   Float_t         TkMET_pt;
   Float_t         TkMET_sumEt;
   UInt_t          nTrigObj;
   Float_t         TrigObj_pt[30];   //[nTrigObj]
   Float_t         TrigObj_eta[30];   //[nTrigObj]
   Float_t         TrigObj_phi[30];   //[nTrigObj]
   Float_t         TrigObj_l1pt[30];   //[nTrigObj]
   Float_t         TrigObj_l1pt_2[30];   //[nTrigObj]
   Float_t         TrigObj_l2pt[30];   //[nTrigObj]
   Int_t           TrigObj_id[30];   //[nTrigObj]
   Int_t           TrigObj_l1iso[30];   //[nTrigObj]
   Int_t           TrigObj_l1charge[30];   //[nTrigObj]
   Int_t           TrigObj_filterBits[30];   //[nTrigObj]
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
   Float_t         SV_dlen[9];   //[nSV]
   Float_t         SV_dlenSig[9];   //[nSV]
   Float_t         SV_pAngle[9];   //[nSV]
   Int_t           Electron_genPartIdx[7];   //[nElectron]
   UChar_t         Electron_genPartFlav[7];   //[nElectron]
   Int_t           GenJetAK8_partonFlavour[3];   //[nGenJetAK8]
   UChar_t         GenJetAK8_hadronFlavour[3];   //[nGenJetAK8]
   Int_t           GenJet_partonFlavour[21];   //[nGenJet]
   UChar_t         GenJet_hadronFlavour[21];   //[nGenJet]
   Int_t           Jet_genJetIdx[33];   //[nJet]
   Int_t           Jet_hadronFlavour[33];   //[nJet]
   Int_t           Jet_partonFlavour[33];   //[nJet]
   Int_t           Muon_genPartIdx[6];   //[nMuon]
   UChar_t         Muon_genPartFlav[6];   //[nMuon]
   Int_t           Photon_genPartIdx[8];   //[nPhoton]
   UChar_t         Photon_genPartFlav[8];   //[nPhoton]
   Float_t         MET_fiducialGenPhi;
   Float_t         MET_fiducialGenPt;
   UChar_t         Electron_cleanmask[7];   //[nElectron]
   UChar_t         Jet_cleanmask[33];   //[nJet]
   UChar_t         Muon_cleanmask[6];   //[nMuon]
   UChar_t         Photon_cleanmask[8];   //[nPhoton]
   UChar_t         Tau_cleanmask[6];   //[nTau]
   Float_t         SV_chi2[9];   //[nSV]
   Float_t         SV_eta[9];   //[nSV]
   Float_t         SV_mass[9];   //[nSV]
   Float_t         SV_ndof[9];   //[nSV]
   Float_t         SV_phi[9];   //[nSV]
   Float_t         SV_pt[9];   //[nSV]
   Float_t         SV_x[9];   //[nSV]
   Float_t         SV_y[9];   //[nSV]
   Float_t         SV_z[9];   //[nSV]
   Int_t           Tau_genPartIdx[6];   //[nTau]
   UChar_t         Tau_genPartFlav[6];   //[nTau]
   Bool_t          L1simulation_step;
   Bool_t          HLTriggerFirstPath;
   Bool_t          HLT_AK8PFJet360_TrimMass30;
   Bool_t          HLT_AK8PFJet400_TrimMass30;
   Bool_t          HLT_AK8PFHT750_TrimMass50;
   Bool_t          HLT_AK8PFHT800_TrimMass50;
   Bool_t          HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20;
   Bool_t          HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087;
   Bool_t          HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087;
   Bool_t          HLT_AK8DiPFJet300_200_TrimMass30;
   Bool_t          HLT_AK8PFHT700_TrimR0p1PT0p03Mass50;
   Bool_t          HLT_AK8PFHT650_TrimR0p1PT0p03Mass50;
   Bool_t          HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20;
   Bool_t          HLT_AK8DiPFJet280_200_TrimMass30;
   Bool_t          HLT_AK8DiPFJet250_200_TrimMass30;
   Bool_t          HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20;
   Bool_t          HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20;
   Bool_t          HLT_CaloJet260;
   Bool_t          HLT_CaloJet500_NoJetID;
   Bool_t          HLT_Dimuon13_PsiPrime;
   Bool_t          HLT_Dimuon13_Upsilon;
   Bool_t          HLT_Dimuon20_Jpsi;
   Bool_t          HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf;
   Bool_t          HLT_DoubleEle25_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_DoubleEle33_CaloIdL;
   Bool_t          HLT_DoubleEle33_CaloIdL_MW;
   Bool_t          HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW;
   Bool_t          HLT_DoubleEle33_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg;
   Bool_t          HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg;
   Bool_t          HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg;
   Bool_t          HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg;
   Bool_t          HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1;
   Bool_t          HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1;
   Bool_t          HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg;
   Bool_t          HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg;
   Bool_t          HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1;
   Bool_t          HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL;
   Bool_t          HLT_DoubleMu33NoFiltersNoVtx;
   Bool_t          HLT_DoubleMu38NoFiltersNoVtx;
   Bool_t          HLT_DoubleMu23NoFiltersNoVtxDisplaced;
   Bool_t          HLT_DoubleMu28NoFiltersNoVtxDisplaced;
   Bool_t          HLT_DoubleMu0;
   Bool_t          HLT_DoubleMu4_3_Bs;
   Bool_t          HLT_DoubleMu4_3_Jpsi_Displaced;
   Bool_t          HLT_DoubleMu4_JpsiTrk_Displaced;
   Bool_t          HLT_DoubleMu4_LowMassNonResonantTrk_Displaced;
   Bool_t          HLT_DoubleMu3_Trk_Tau3mu;
   Bool_t          HLT_DoubleMu4_PsiPrimeTrk_Displaced;
   Bool_t          HLT_Mu7p5_L2Mu2_Jpsi;
   Bool_t          HLT_Mu7p5_L2Mu2_Upsilon;
   Bool_t          HLT_Mu7p5_Track2_Jpsi;
   Bool_t          HLT_Mu7p5_Track3p5_Jpsi;
   Bool_t          HLT_Mu7p5_Track7_Jpsi;
   Bool_t          HLT_Mu7p5_Track2_Upsilon;
   Bool_t          HLT_Mu7p5_Track3p5_Upsilon;
   Bool_t          HLT_Mu7p5_Track7_Upsilon;
   Bool_t          HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing;
   Bool_t          HLT_Dimuon0er16_Jpsi_NoVertexing;
   Bool_t          HLT_Dimuon6_Jpsi_NoVertexing;
   Bool_t          HLT_Photon150;
   Bool_t          HLT_Photon90_CaloIdL_HT300;
   Bool_t          HLT_HT250_CaloMET70;
   Bool_t          HLT_DoublePhoton60;
   Bool_t          HLT_DoublePhoton85;
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
   Bool_t          HLT_HT200;
   Bool_t          HLT_HT275;
   Bool_t          HLT_HT325;
   Bool_t          HLT_HT425;
   Bool_t          HLT_HT575;
   Bool_t          HLT_HT410to430;
   Bool_t          HLT_HT430to450;
   Bool_t          HLT_HT450to470;
   Bool_t          HLT_HT470to500;
   Bool_t          HLT_HT500to550;
   Bool_t          HLT_HT550to650;
   Bool_t          HLT_HT650;
   Bool_t          HLT_Mu16_eta2p1_MET30;
   Bool_t          HLT_IsoMu16_eta2p1_MET30;
   Bool_t          HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1;
   Bool_t          HLT_IsoMu17_eta2p1;
   Bool_t          HLT_IsoMu17_eta2p1_LooseIsoPFTau20;
   Bool_t          HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1;
   Bool_t          HLT_DoubleIsoMu17_eta2p1;
   Bool_t          HLT_DoubleIsoMu17_eta2p1_noDzCut;
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
   Bool_t          HLT_L1SingleMu18;
   Bool_t          HLT_L2Mu10;
   Bool_t          HLT_L1SingleMuOpen;
   Bool_t          HLT_L1SingleMuOpen_DT;
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
   Bool_t          HLT_PFTau120_eta2p1;
   Bool_t          HLT_PFTau140_eta2p1;
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
   Bool_t          HLT_DoubleMu18NoFiltersNoVtx;
   Bool_t          HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight;
   Bool_t          HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose;
   Bool_t          HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose;
   Bool_t          HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight;
   Bool_t          HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose;
   Bool_t          HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose;
   Bool_t          HLT_Mu28NoFiltersNoVtx_CentralCaloJet40;
   Bool_t          HLT_PFHT300_PFMET100;
   Bool_t          HLT_PFHT300_PFMET110;
   Bool_t          HLT_PFHT550_4JetPt50;
   Bool_t          HLT_PFHT650_4JetPt50;
   Bool_t          HLT_PFHT750_4JetPt50;
   Bool_t          HLT_PFHT750_4JetPt70;
   Bool_t          HLT_PFHT750_4JetPt80;
   Bool_t          HLT_PFHT800_4JetPt50;
   Bool_t          HLT_PFHT850_4JetPt50;
   Bool_t          HLT_PFJet15_NoCaloMatched;
   Bool_t          HLT_PFJet25_NoCaloMatched;
   Bool_t          HLT_DiPFJet15_NoCaloMatched;
   Bool_t          HLT_DiPFJet25_NoCaloMatched;
   Bool_t          HLT_DiPFJet15_FBEta3_NoCaloMatched;
   Bool_t          HLT_DiPFJet25_FBEta3_NoCaloMatched;
   Bool_t          HLT_DiPFJetAve15_HFJEC;
   Bool_t          HLT_DiPFJetAve25_HFJEC;
   Bool_t          HLT_DiPFJetAve35_HFJEC;
   Bool_t          HLT_AK8PFJet40;
   Bool_t          HLT_AK8PFJet60;
   Bool_t          HLT_AK8PFJet80;
   Bool_t          HLT_AK8PFJet140;
   Bool_t          HLT_AK8PFJet200;
   Bool_t          HLT_AK8PFJet260;
   Bool_t          HLT_AK8PFJet320;
   Bool_t          HLT_AK8PFJet400;
   Bool_t          HLT_AK8PFJet450;
   Bool_t          HLT_AK8PFJet500;
   Bool_t          HLT_PFJet40;
   Bool_t          HLT_PFJet60;
   Bool_t          HLT_PFJet80;
   Bool_t          HLT_PFJet140;
   Bool_t          HLT_PFJet200;
   Bool_t          HLT_PFJet260;
   Bool_t          HLT_PFJet320;
   Bool_t          HLT_PFJet400;
   Bool_t          HLT_PFJet450;
   Bool_t          HLT_PFJet500;
   Bool_t          HLT_DiPFJetAve40;
   Bool_t          HLT_DiPFJetAve60;
   Bool_t          HLT_DiPFJetAve80;
   Bool_t          HLT_DiPFJetAve140;
   Bool_t          HLT_DiPFJetAve200;
   Bool_t          HLT_DiPFJetAve260;
   Bool_t          HLT_DiPFJetAve320;
   Bool_t          HLT_DiPFJetAve400;
   Bool_t          HLT_DiPFJetAve500;
   Bool_t          HLT_DiPFJetAve60_HFJEC;
   Bool_t          HLT_DiPFJetAve80_HFJEC;
   Bool_t          HLT_DiPFJetAve100_HFJEC;
   Bool_t          HLT_DiPFJetAve160_HFJEC;
   Bool_t          HLT_DiPFJetAve220_HFJEC;
   Bool_t          HLT_DiPFJetAve300_HFJEC;
   Bool_t          HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140;
   Bool_t          HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80;
   Bool_t          HLT_DiCentralPFJet170;
   Bool_t          HLT_SingleCentralPFJet170_CFMax0p1;
   Bool_t          HLT_DiCentralPFJet170_CFMax0p1;
   Bool_t          HLT_DiCentralPFJet220_CFMax0p3;
   Bool_t          HLT_DiCentralPFJet330_CFMax0p5;
   Bool_t          HLT_DiCentralPFJet430;
   Bool_t          HLT_PFHT125;
   Bool_t          HLT_PFHT200;
   Bool_t          HLT_PFHT250;
   Bool_t          HLT_PFHT300;
   Bool_t          HLT_PFHT350;
   Bool_t          HLT_PFHT400;
   Bool_t          HLT_PFHT475;
   Bool_t          HLT_PFHT600;
   Bool_t          HLT_PFHT650;
   Bool_t          HLT_PFHT800;
   Bool_t          HLT_PFHT900;
   Bool_t          HLT_PFHT200_PFAlphaT0p51;
   Bool_t          HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57;
   Bool_t          HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63;
   Bool_t          HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55;
   Bool_t          HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58;
   Bool_t          HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53;
   Bool_t          HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54;
   Bool_t          HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52;
   Bool_t          HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53;
   Bool_t          HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51;
   Bool_t          HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52;
   Bool_t          HLT_MET60_IsoTrk35_Loose;
   Bool_t          HLT_MET75_IsoTrk50;
   Bool_t          HLT_MET90_IsoTrk50;
   Bool_t          HLT_PFMET120_BTagCSV_p067;
   Bool_t          HLT_PFMET120_Mu5;
   Bool_t          HLT_PFMET170_NotCleaned;
   Bool_t          HLT_PFMET170_NoiseCleaned;
   Bool_t          HLT_PFMET170_HBHECleaned;
   Bool_t          HLT_PFMET170_JetIdCleaned;
   Bool_t          HLT_PFMET170_BeamHaloCleaned;
   Bool_t          HLT_PFMET170_HBHE_BeamHaloCleaned;
   Bool_t          HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned;
   Bool_t          HLT_PFMET90_PFMHT90_IDTight;
   Bool_t          HLT_PFMET100_PFMHT100_IDTight;
   Bool_t          HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned;
   Bool_t          HLT_PFMET110_PFMHT110_IDTight;
   Bool_t          HLT_PFMET120_PFMHT120_IDTight;
   Bool_t          HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067;
   Bool_t          HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight;
   Bool_t          HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200;
   Bool_t          HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460;
   Bool_t          HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240;
   Bool_t          HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500;
   Bool_t          HLT_QuadPFJet_VBF;
   Bool_t          HLT_L1_TripleJet_VBF;
   Bool_t          HLT_QuadJet45_TripleBTagCSV_p087;
   Bool_t          HLT_QuadJet45_DoubleBTagCSV_p087;
   Bool_t          HLT_DoubleJet90_Double30_TripleBTagCSV_p087;
   Bool_t          HLT_DoubleJet90_Double30_DoubleBTagCSV_p087;
   Bool_t          HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160;
   Bool_t          HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6;
   Bool_t          HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172;
   Bool_t          HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6;
   Bool_t          HLT_DoubleJetsC100_SingleBTagCSV_p026;
   Bool_t          HLT_DoubleJetsC100_SingleBTagCSV_p014;
   Bool_t          HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350;
   Bool_t          HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350;
   Bool_t          HLT_Photon135_PFMET100;
   Bool_t          HLT_Photon20_CaloIdVL_IsoL;
   Bool_t          HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40;
   Bool_t          HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF;
   Bool_t          HLT_Photon250_NoHE;
   Bool_t          HLT_Photon300_NoHE;
   Bool_t          HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60;
   Bool_t          HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15;
   Bool_t          HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40;
   Bool_t          HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF;
   Bool_t          HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40;
   Bool_t          HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF;
   Bool_t          HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40;
   Bool_t          HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF;
   Bool_t          HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40;
   Bool_t          HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF;
   Bool_t          HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40;
   Bool_t          HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF;
   Bool_t          HLT_Mu8_TrkIsoVVL;
   Bool_t          HLT_Mu17_TrkIsoVVL;
   Bool_t          HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_BTagMu_DiJet20_Mu5;
   Bool_t          HLT_BTagMu_DiJet40_Mu5;
   Bool_t          HLT_BTagMu_DiJet70_Mu5;
   Bool_t          HLT_BTagMu_DiJet110_Mu5;
   Bool_t          HLT_BTagMu_DiJet170_Mu5;
   Bool_t          HLT_BTagMu_Jet300_Mu5;
   Bool_t          HLT_BTagMu_AK8Jet300_Mu5;
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
   Bool_t          HLT_DiMu9_Ele9_CaloIdL_TrackIdL;
   Bool_t          HLT_TripleMu_5_3_3;
   Bool_t          HLT_TripleMu_12_10_5;
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
   Bool_t          HLT_PFHT650_WideJetMJJ900DEtaJJ1p5;
   Bool_t          HLT_PFHT650_WideJetMJJ950DEtaJJ1p5;
   Bool_t          HLT_Photon22;
   Bool_t          HLT_Photon30;
   Bool_t          HLT_Photon36;
   Bool_t          HLT_Photon50;
   Bool_t          HLT_Photon75;
   Bool_t          HLT_Photon90;
   Bool_t          HLT_Photon120;
   Bool_t          HLT_Photon175;
   Bool_t          HLT_Photon165_HE10;
   Bool_t          HLT_Photon22_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon30_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon36_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon50_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon75_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon90_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon120_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon165_R9Id90_HE10_IsoM;
   Bool_t          HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90;
   Bool_t          HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70;
   Bool_t          HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55;
   Bool_t          HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55;
   Bool_t          HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55;
   Bool_t          HLT_Dimuon0_Jpsi_Muon;
   Bool_t          HLT_Dimuon0_Upsilon_Muon;
   Bool_t          HLT_QuadMuon0_Dimuon0_Jpsi;
   Bool_t          HLT_QuadMuon0_Dimuon0_Upsilon;
   Bool_t          HLT_Rsq0p25_Calo;
   Bool_t          HLT_RsqMR240_Rsq0p09_MR200_4jet_Calo;
   Bool_t          HLT_RsqMR240_Rsq0p09_MR200_Calo;
   Bool_t          HLT_Rsq0p25;
   Bool_t          HLT_Rsq0p30;
   Bool_t          HLT_RsqMR240_Rsq0p09_MR200;
   Bool_t          HLT_RsqMR240_Rsq0p09_MR200_4jet;
   Bool_t          HLT_RsqMR270_Rsq0p09_MR200;
   Bool_t          HLT_RsqMR270_Rsq0p09_MR200_4jet;
   Bool_t          HLT_Rsq0p02_MR300_TriPFJet80_60_40_BTagCSV_p063_p20_Mbb60_200;
   Bool_t          HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;
   Bool_t          HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;
   Bool_t          HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;
   Bool_t          HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;
   Bool_t          HLT_HT200_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT250_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT350_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT350_DisplacedDijet80_DisplacedTrack;
   Bool_t          HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack;
   Bool_t          HLT_HT350_DisplacedDijet40_Inclusive;
   Bool_t          HLT_HT400_DisplacedDijet40_Inclusive;
   Bool_t          HLT_HT500_DisplacedDijet40_Inclusive;
   Bool_t          HLT_HT550_DisplacedDijet40_Inclusive;
   Bool_t          HLT_HT550_DisplacedDijet80_Inclusive;
   Bool_t          HLT_HT650_DisplacedDijet80_Inclusive;
   Bool_t          HLT_HT750_DisplacedDijet80_Inclusive;
   Bool_t          HLT_VBF_DisplacedJet40_DisplacedTrack;
   Bool_t          HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5;
   Bool_t          HLT_VBF_DisplacedJet40_TightID_DisplacedTrack;
   Bool_t          HLT_VBF_DisplacedJet40_Hadronic;
   Bool_t          HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack;
   Bool_t          HLT_VBF_DisplacedJet40_TightID_Hadronic;
   Bool_t          HLT_VBF_DisplacedJet40_VTightID_Hadronic;
   Bool_t          HLT_VBF_DisplacedJet40_VVTightID_Hadronic;
   Bool_t          HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack;
   Bool_t          HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack;
   Bool_t          HLT_PFMETNoMu90_PFMHTNoMu90_IDTight;
   Bool_t          HLT_PFMETNoMu100_PFMHTNoMu100_IDTight;
   Bool_t          HLT_PFMETNoMu110_PFMHTNoMu110_IDTight;
   Bool_t          HLT_PFMETNoMu120_PFMHTNoMu120_IDTight;
   Bool_t          HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight;
   Bool_t          HLT_MonoCentralPFJet80_PFMETNoMu100_PFMHTNoMu100_IDTight;
   Bool_t          HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight;
   Bool_t          HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight;
   Bool_t          HLT_Ele27_eta2p1_WPLoose_Gsf_HT200;
   Bool_t          HLT_Photon90_CaloIdL_PFHT500;
   Bool_t          HLT_DoubleMu8_Mass8_PFHT250;
   Bool_t          HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250;
   Bool_t          HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250;
   Bool_t          HLT_DoubleMu8_Mass8_PFHT300;
   Bool_t          HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300;
   Bool_t          HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300;
   Bool_t          HLT_Mu10_CentralPFJet30_BTagCSV_p13;
   Bool_t          HLT_DoubleMu3_PFMET50;
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
   Bool_t          HLT_Dimuon16_Jpsi;
   Bool_t          HLT_Dimuon10_Jpsi_Barrel;
   Bool_t          HLT_Dimuon8_PsiPrime_Barrel;
   Bool_t          HLT_Dimuon8_Upsilon_Barrel;
   Bool_t          HLT_Dimuon0_Phi_Barrel;
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
   Bool_t          HLT_PFHT400_SixJet30_DoubleBTagCSV_p056;
   Bool_t          HLT_PFHT450_SixJet40_BTagCSV_p056;
   Bool_t          HLT_PFHT400_SixJet30;
   Bool_t          HLT_PFHT450_SixJet40;
   Bool_t          HLT_Ele115_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_Mu55;
   Bool_t          HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15;
   Bool_t          HLT_Photon90_CaloIdL_PFHT600;
   Bool_t          HLT_PixelTracks_Multiplicity60ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity85ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity110ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity135ForEndOfFill;
   Bool_t          HLT_PixelTracks_Multiplicity160ForEndOfFill;
   Bool_t          HLT_FullTracks_Multiplicity80;
   Bool_t          HLT_FullTracks_Multiplicity100;
   Bool_t          HLT_FullTracks_Multiplicity130;
   Bool_t          HLT_FullTracks_Multiplicity150;
   Bool_t          HLT_ECALHT800;
   Bool_t          HLT_DiSC30_18_EIso_AND_HE_Mass70;
   Bool_t          HLT_Photon125;
   Bool_t          HLT_MET100;
   Bool_t          HLT_MET150;
   Bool_t          HLT_MET200;
   Bool_t          HLT_Ele27_HighEta_Ele20_Mass55;
   Bool_t          HLT_L1FatEvents;
   Bool_t          HLT_Physics;
   Bool_t          HLT_L1FatEvents_part0;
   Bool_t          HLT_L1FatEvents_part1;
   Bool_t          HLT_L1FatEvents_part2;
   Bool_t          HLT_L1FatEvents_part3;
   Bool_t          HLT_Random;
   Bool_t          HLT_ZeroBias;
   Bool_t          HLT_AK4CaloJet30;
   Bool_t          HLT_AK4CaloJet40;
   Bool_t          HLT_AK4CaloJet50;
   Bool_t          HLT_AK4CaloJet80;
   Bool_t          HLT_AK4CaloJet100;
   Bool_t          HLT_AK4PFJet30;
   Bool_t          HLT_AK4PFJet50;
   Bool_t          HLT_AK4PFJet80;
   Bool_t          HLT_AK4PFJet100;
   Bool_t          HLT_HISinglePhoton10;
   Bool_t          HLT_HISinglePhoton15;
   Bool_t          HLT_HISinglePhoton20;
   Bool_t          HLT_HISinglePhoton40;
   Bool_t          HLT_HISinglePhoton60;
   Bool_t          HLT_EcalCalibration;
   Bool_t          HLT_HcalCalibration;
   Bool_t          HLT_GlobalRunHPDNoise;
   Bool_t          HLT_L1BptxMinus;
   Bool_t          HLT_L1BptxPlus;
   Bool_t          HLT_L1NotBptxOR;
   Bool_t          HLT_L1BeamGasMinus;
   Bool_t          HLT_L1BeamGasPlus;
   Bool_t          HLT_L1BptxXOR;
   Bool_t          HLT_L1MinimumBiasHF_OR;
   Bool_t          HLT_L1MinimumBiasHF_AND;
   Bool_t          HLT_HcalNZS;
   Bool_t          HLT_HcalPhiSym;
   Bool_t          HLT_HcalIsolatedbunch;
   Bool_t          HLT_ZeroBias_FirstCollisionAfterAbortGap;
   Bool_t          HLT_ZeroBias_FirstCollisionAfterAbortGap_copy;
   Bool_t          HLT_ZeroBias_FirstCollisionAfterAbortGap_TCDS;
   Bool_t          HLT_ZeroBias_IsolatedBunches;
   Bool_t          HLT_ZeroBias_FirstCollisionInTrain;
   Bool_t          HLT_ZeroBias_FirstBXAfterTrain;
   Bool_t          HLT_Photon500;
   Bool_t          HLT_Photon600;
   Bool_t          HLT_Mu300;
   Bool_t          HLT_Mu350;
   Bool_t          HLT_MET250;
   Bool_t          HLT_MET300;
   Bool_t          HLT_MET600;
   Bool_t          HLT_MET700;
   Bool_t          HLT_PFMET300;
   Bool_t          HLT_PFMET400;
   Bool_t          HLT_PFMET500;
   Bool_t          HLT_PFMET600;
   Bool_t          HLT_Ele250_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_Ele300_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_HT2000;
   Bool_t          HLT_HT2500;
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
   Float_t         Jet_pt_nom[33];   //[nJet]
   Float_t         Jet_mass_nom[33];   //[nJet]
   Float_t         MET_pt_nom;
   Float_t         MET_phi_nom;
   Float_t         Jet_pt_jerUp[33];   //[nJet]
   Float_t         Jet_mass_jerUp[33];   //[nJet]
   Float_t         Jet_mass_jmrUp[33];   //[nJet]
   Float_t         Jet_mass_jmsUp[33];   //[nJet]
   Float_t         MET_pt_jerUp;
   Float_t         MET_phi_jerUp;
   Float_t         Jet_pt_jesAbsoluteStatUp[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteStatUp[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteStatUp;
   Float_t         MET_phi_jesAbsoluteStatUp;
   Float_t         Jet_pt_jesAbsoluteScaleUp[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteScaleUp[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteScaleUp;
   Float_t         MET_phi_jesAbsoluteScaleUp;
   Float_t         Jet_pt_jesAbsoluteFlavMapUp[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteFlavMapUp[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteFlavMapUp;
   Float_t         MET_phi_jesAbsoluteFlavMapUp;
   Float_t         Jet_pt_jesAbsoluteMPFBiasUp[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteMPFBiasUp[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteMPFBiasUp;
   Float_t         MET_phi_jesAbsoluteMPFBiasUp;
   Float_t         Jet_pt_jesFragmentationUp[33];   //[nJet]
   Float_t         Jet_mass_jesFragmentationUp[33];   //[nJet]
   Float_t         MET_pt_jesFragmentationUp;
   Float_t         MET_phi_jesFragmentationUp;
   Float_t         Jet_pt_jesSinglePionECALUp[33];   //[nJet]
   Float_t         Jet_mass_jesSinglePionECALUp[33];   //[nJet]
   Float_t         MET_pt_jesSinglePionECALUp;
   Float_t         MET_phi_jesSinglePionECALUp;
   Float_t         Jet_pt_jesSinglePionHCALUp[33];   //[nJet]
   Float_t         Jet_mass_jesSinglePionHCALUp[33];   //[nJet]
   Float_t         MET_pt_jesSinglePionHCALUp;
   Float_t         MET_phi_jesSinglePionHCALUp;
   Float_t         Jet_pt_jesFlavorQCDUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorQCDUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorQCDUp;
   Float_t         MET_phi_jesFlavorQCDUp;
   Float_t         Jet_pt_jesTimePtEtaUp[33];   //[nJet]
   Float_t         Jet_mass_jesTimePtEtaUp[33];   //[nJet]
   Float_t         MET_pt_jesTimePtEtaUp;
   Float_t         MET_phi_jesTimePtEtaUp;
   Float_t         Jet_pt_jesRelativeJEREC1Up[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC1Up[33];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC1Up;
   Float_t         MET_phi_jesRelativeJEREC1Up;
   Float_t         Jet_pt_jesRelativeJEREC2Up[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC2Up[33];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC2Up;
   Float_t         MET_phi_jesRelativeJEREC2Up;
   Float_t         Jet_pt_jesRelativeJERHFUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeJERHFUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativeJERHFUp;
   Float_t         MET_phi_jesRelativeJERHFUp;
   Float_t         Jet_pt_jesRelativePtBBUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtBBUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtBBUp;
   Float_t         MET_phi_jesRelativePtBBUp;
   Float_t         Jet_pt_jesRelativePtEC1Up[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC1Up[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC1Up;
   Float_t         MET_phi_jesRelativePtEC1Up;
   Float_t         Jet_pt_jesRelativePtEC2Up[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC2Up[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC2Up;
   Float_t         MET_phi_jesRelativePtEC2Up;
   Float_t         Jet_pt_jesRelativePtHFUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtHFUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtHFUp;
   Float_t         MET_phi_jesRelativePtHFUp;
   Float_t         Jet_pt_jesRelativeBalUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeBalUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativeBalUp;
   Float_t         MET_phi_jesRelativeBalUp;
   Float_t         Jet_pt_jesRelativeFSRUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeFSRUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativeFSRUp;
   Float_t         MET_phi_jesRelativeFSRUp;
   Float_t         Jet_pt_jesRelativeStatFSRUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatFSRUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativeStatFSRUp;
   Float_t         MET_phi_jesRelativeStatFSRUp;
   Float_t         Jet_pt_jesRelativeStatECUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatECUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativeStatECUp;
   Float_t         MET_phi_jesRelativeStatECUp;
   Float_t         Jet_pt_jesRelativeStatHFUp[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatHFUp[33];   //[nJet]
   Float_t         MET_pt_jesRelativeStatHFUp;
   Float_t         MET_phi_jesRelativeStatHFUp;
   Float_t         Jet_pt_jesPileUpDataMCUp[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpDataMCUp[33];   //[nJet]
   Float_t         MET_pt_jesPileUpDataMCUp;
   Float_t         MET_phi_jesPileUpDataMCUp;
   Float_t         Jet_pt_jesPileUpPtRefUp[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtRefUp[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtRefUp;
   Float_t         MET_phi_jesPileUpPtRefUp;
   Float_t         Jet_pt_jesPileUpPtBBUp[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtBBUp[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtBBUp;
   Float_t         MET_phi_jesPileUpPtBBUp;
   Float_t         Jet_pt_jesPileUpPtEC1Up[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC1Up[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC1Up;
   Float_t         MET_phi_jesPileUpPtEC1Up;
   Float_t         Jet_pt_jesPileUpPtEC2Up[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC2Up[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC2Up;
   Float_t         MET_phi_jesPileUpPtEC2Up;
   Float_t         Jet_pt_jesPileUpPtHFUp[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtHFUp[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtHFUp;
   Float_t         MET_phi_jesPileUpPtHFUp;
   Float_t         Jet_pt_jesPileUpMuZeroUp[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpMuZeroUp[33];   //[nJet]
   Float_t         MET_pt_jesPileUpMuZeroUp;
   Float_t         MET_phi_jesPileUpMuZeroUp;
   Float_t         Jet_pt_jesPileUpEnvelopeUp[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpEnvelopeUp[33];   //[nJet]
   Float_t         MET_pt_jesPileUpEnvelopeUp;
   Float_t         MET_phi_jesPileUpEnvelopeUp;
   Float_t         Jet_pt_jesSubTotalPileUpUp[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPileUpUp[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalPileUpUp;
   Float_t         MET_phi_jesSubTotalPileUpUp;
   Float_t         Jet_pt_jesSubTotalRelativeUp[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalRelativeUp[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalRelativeUp;
   Float_t         MET_phi_jesSubTotalRelativeUp;
   Float_t         Jet_pt_jesSubTotalPtUp[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPtUp[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalPtUp;
   Float_t         MET_phi_jesSubTotalPtUp;
   Float_t         Jet_pt_jesSubTotalScaleUp[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalScaleUp[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalScaleUp;
   Float_t         MET_phi_jesSubTotalScaleUp;
   Float_t         Jet_pt_jesSubTotalAbsoluteUp[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalAbsoluteUp[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalAbsoluteUp;
   Float_t         MET_phi_jesSubTotalAbsoluteUp;
   Float_t         Jet_pt_jesSubTotalMCUp[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalMCUp[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalMCUp;
   Float_t         MET_phi_jesSubTotalMCUp;
   Float_t         Jet_pt_jesTotalUp[33];   //[nJet]
   Float_t         Jet_mass_jesTotalUp[33];   //[nJet]
   Float_t         MET_pt_jesTotalUp;
   Float_t         MET_phi_jesTotalUp;
   Float_t         Jet_pt_jesTotalNoFlavorUp[33];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorUp[33];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorUp;
   Float_t         MET_phi_jesTotalNoFlavorUp;
   Float_t         Jet_pt_jesTotalNoTimeUp[33];   //[nJet]
   Float_t         Jet_mass_jesTotalNoTimeUp[33];   //[nJet]
   Float_t         MET_pt_jesTotalNoTimeUp;
   Float_t         MET_phi_jesTotalNoTimeUp;
   Float_t         Jet_pt_jesTotalNoFlavorNoTimeUp[33];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorNoTimeUp[33];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorNoTimeUp;
   Float_t         MET_phi_jesTotalNoFlavorNoTimeUp;
   Float_t         Jet_pt_jesFlavorZJetUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorZJetUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorZJetUp;
   Float_t         MET_phi_jesFlavorZJetUp;
   Float_t         Jet_pt_jesFlavorPhotonJetUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPhotonJetUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPhotonJetUp;
   Float_t         MET_phi_jesFlavorPhotonJetUp;
   Float_t         Jet_pt_jesFlavorPureGluonUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureGluonUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureGluonUp;
   Float_t         MET_phi_jesFlavorPureGluonUp;
   Float_t         Jet_pt_jesFlavorPureQuarkUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureQuarkUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureQuarkUp;
   Float_t         MET_phi_jesFlavorPureQuarkUp;
   Float_t         Jet_pt_jesFlavorPureCharmUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureCharmUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureCharmUp;
   Float_t         MET_phi_jesFlavorPureCharmUp;
   Float_t         Jet_pt_jesFlavorPureBottomUp[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureBottomUp[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureBottomUp;
   Float_t         MET_phi_jesFlavorPureBottomUp;
   Float_t         Jet_pt_jesTimeRunBCDUp[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunBCDUp[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunBCDUp;
   Float_t         MET_phi_jesTimeRunBCDUp;
   Float_t         Jet_pt_jesTimeRunEFUp[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunEFUp[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunEFUp;
   Float_t         MET_phi_jesTimeRunEFUp;
   Float_t         Jet_pt_jesTimeRunGUp[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunGUp[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunGUp;
   Float_t         MET_phi_jesTimeRunGUp;
   Float_t         Jet_pt_jesTimeRunHUp[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunHUp[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunHUp;
   Float_t         MET_phi_jesTimeRunHUp;
   Float_t         Jet_pt_jesCorrelationGroupMPFInSituUp[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupMPFInSituUp[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupMPFInSituUp;
   Float_t         MET_phi_jesCorrelationGroupMPFInSituUp;
   Float_t         Jet_pt_jesCorrelationGroupIntercalibrationUp[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupIntercalibrationUp[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupIntercalibrationUp;
   Float_t         MET_phi_jesCorrelationGroupIntercalibrationUp;
   Float_t         Jet_pt_jesCorrelationGroupbJESUp[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupbJESUp[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupbJESUp;
   Float_t         MET_phi_jesCorrelationGroupbJESUp;
   Float_t         Jet_pt_jesCorrelationGroupFlavorUp[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupFlavorUp[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupFlavorUp;
   Float_t         MET_phi_jesCorrelationGroupFlavorUp;
   Float_t         Jet_pt_jesCorrelationGroupUncorrelatedUp[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupUncorrelatedUp[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupUncorrelatedUp;
   Float_t         MET_phi_jesCorrelationGroupUncorrelatedUp;
   Float_t         MET_pt_unclustEnUp;
   Float_t         MET_phi_unclustEnUp;
   Float_t         Jet_pt_jerDown[33];   //[nJet]
   Float_t         Jet_mass_jerDown[33];   //[nJet]
   Float_t         Jet_mass_jmrDown[33];   //[nJet]
   Float_t         Jet_mass_jmsDown[33];   //[nJet]
   Float_t         MET_pt_jerDown;
   Float_t         MET_phi_jerDown;
   Float_t         Jet_pt_jesAbsoluteStatDown[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteStatDown[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteStatDown;
   Float_t         MET_phi_jesAbsoluteStatDown;
   Float_t         Jet_pt_jesAbsoluteScaleDown[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteScaleDown[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteScaleDown;
   Float_t         MET_phi_jesAbsoluteScaleDown;
   Float_t         Jet_pt_jesAbsoluteFlavMapDown[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteFlavMapDown[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteFlavMapDown;
   Float_t         MET_phi_jesAbsoluteFlavMapDown;
   Float_t         Jet_pt_jesAbsoluteMPFBiasDown[33];   //[nJet]
   Float_t         Jet_mass_jesAbsoluteMPFBiasDown[33];   //[nJet]
   Float_t         MET_pt_jesAbsoluteMPFBiasDown;
   Float_t         MET_phi_jesAbsoluteMPFBiasDown;
   Float_t         Jet_pt_jesFragmentationDown[33];   //[nJet]
   Float_t         Jet_mass_jesFragmentationDown[33];   //[nJet]
   Float_t         MET_pt_jesFragmentationDown;
   Float_t         MET_phi_jesFragmentationDown;
   Float_t         Jet_pt_jesSinglePionECALDown[33];   //[nJet]
   Float_t         Jet_mass_jesSinglePionECALDown[33];   //[nJet]
   Float_t         MET_pt_jesSinglePionECALDown;
   Float_t         MET_phi_jesSinglePionECALDown;
   Float_t         Jet_pt_jesSinglePionHCALDown[33];   //[nJet]
   Float_t         Jet_mass_jesSinglePionHCALDown[33];   //[nJet]
   Float_t         MET_pt_jesSinglePionHCALDown;
   Float_t         MET_phi_jesSinglePionHCALDown;
   Float_t         Jet_pt_jesFlavorQCDDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorQCDDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorQCDDown;
   Float_t         MET_phi_jesFlavorQCDDown;
   Float_t         Jet_pt_jesTimePtEtaDown[33];   //[nJet]
   Float_t         Jet_mass_jesTimePtEtaDown[33];   //[nJet]
   Float_t         MET_pt_jesTimePtEtaDown;
   Float_t         MET_phi_jesTimePtEtaDown;
   Float_t         Jet_pt_jesRelativeJEREC1Down[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC1Down[33];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC1Down;
   Float_t         MET_phi_jesRelativeJEREC1Down;
   Float_t         Jet_pt_jesRelativeJEREC2Down[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeJEREC2Down[33];   //[nJet]
   Float_t         MET_pt_jesRelativeJEREC2Down;
   Float_t         MET_phi_jesRelativeJEREC2Down;
   Float_t         Jet_pt_jesRelativeJERHFDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeJERHFDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativeJERHFDown;
   Float_t         MET_phi_jesRelativeJERHFDown;
   Float_t         Jet_pt_jesRelativePtBBDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtBBDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtBBDown;
   Float_t         MET_phi_jesRelativePtBBDown;
   Float_t         Jet_pt_jesRelativePtEC1Down[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC1Down[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC1Down;
   Float_t         MET_phi_jesRelativePtEC1Down;
   Float_t         Jet_pt_jesRelativePtEC2Down[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtEC2Down[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtEC2Down;
   Float_t         MET_phi_jesRelativePtEC2Down;
   Float_t         Jet_pt_jesRelativePtHFDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativePtHFDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativePtHFDown;
   Float_t         MET_phi_jesRelativePtHFDown;
   Float_t         Jet_pt_jesRelativeBalDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeBalDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativeBalDown;
   Float_t         MET_phi_jesRelativeBalDown;
   Float_t         Jet_pt_jesRelativeFSRDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeFSRDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativeFSRDown;
   Float_t         MET_phi_jesRelativeFSRDown;
   Float_t         Jet_pt_jesRelativeStatFSRDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatFSRDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativeStatFSRDown;
   Float_t         MET_phi_jesRelativeStatFSRDown;
   Float_t         Jet_pt_jesRelativeStatECDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatECDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativeStatECDown;
   Float_t         MET_phi_jesRelativeStatECDown;
   Float_t         Jet_pt_jesRelativeStatHFDown[33];   //[nJet]
   Float_t         Jet_mass_jesRelativeStatHFDown[33];   //[nJet]
   Float_t         MET_pt_jesRelativeStatHFDown;
   Float_t         MET_phi_jesRelativeStatHFDown;
   Float_t         Jet_pt_jesPileUpDataMCDown[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpDataMCDown[33];   //[nJet]
   Float_t         MET_pt_jesPileUpDataMCDown;
   Float_t         MET_phi_jesPileUpDataMCDown;
   Float_t         Jet_pt_jesPileUpPtRefDown[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtRefDown[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtRefDown;
   Float_t         MET_phi_jesPileUpPtRefDown;
   Float_t         Jet_pt_jesPileUpPtBBDown[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtBBDown[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtBBDown;
   Float_t         MET_phi_jesPileUpPtBBDown;
   Float_t         Jet_pt_jesPileUpPtEC1Down[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC1Down[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC1Down;
   Float_t         MET_phi_jesPileUpPtEC1Down;
   Float_t         Jet_pt_jesPileUpPtEC2Down[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtEC2Down[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtEC2Down;
   Float_t         MET_phi_jesPileUpPtEC2Down;
   Float_t         Jet_pt_jesPileUpPtHFDown[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpPtHFDown[33];   //[nJet]
   Float_t         MET_pt_jesPileUpPtHFDown;
   Float_t         MET_phi_jesPileUpPtHFDown;
   Float_t         Jet_pt_jesPileUpMuZeroDown[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpMuZeroDown[33];   //[nJet]
   Float_t         MET_pt_jesPileUpMuZeroDown;
   Float_t         MET_phi_jesPileUpMuZeroDown;
   Float_t         Jet_pt_jesPileUpEnvelopeDown[33];   //[nJet]
   Float_t         Jet_mass_jesPileUpEnvelopeDown[33];   //[nJet]
   Float_t         MET_pt_jesPileUpEnvelopeDown;
   Float_t         MET_phi_jesPileUpEnvelopeDown;
   Float_t         Jet_pt_jesSubTotalPileUpDown[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPileUpDown[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalPileUpDown;
   Float_t         MET_phi_jesSubTotalPileUpDown;
   Float_t         Jet_pt_jesSubTotalRelativeDown[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalRelativeDown[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalRelativeDown;
   Float_t         MET_phi_jesSubTotalRelativeDown;
   Float_t         Jet_pt_jesSubTotalPtDown[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalPtDown[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalPtDown;
   Float_t         MET_phi_jesSubTotalPtDown;
   Float_t         Jet_pt_jesSubTotalScaleDown[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalScaleDown[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalScaleDown;
   Float_t         MET_phi_jesSubTotalScaleDown;
   Float_t         Jet_pt_jesSubTotalAbsoluteDown[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalAbsoluteDown[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalAbsoluteDown;
   Float_t         MET_phi_jesSubTotalAbsoluteDown;
   Float_t         Jet_pt_jesSubTotalMCDown[33];   //[nJet]
   Float_t         Jet_mass_jesSubTotalMCDown[33];   //[nJet]
   Float_t         MET_pt_jesSubTotalMCDown;
   Float_t         MET_phi_jesSubTotalMCDown;
   Float_t         Jet_pt_jesTotalDown[33];   //[nJet]
   Float_t         Jet_mass_jesTotalDown[33];   //[nJet]
   Float_t         MET_pt_jesTotalDown;
   Float_t         MET_phi_jesTotalDown;
   Float_t         Jet_pt_jesTotalNoFlavorDown[33];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorDown[33];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorDown;
   Float_t         MET_phi_jesTotalNoFlavorDown;
   Float_t         Jet_pt_jesTotalNoTimeDown[33];   //[nJet]
   Float_t         Jet_mass_jesTotalNoTimeDown[33];   //[nJet]
   Float_t         MET_pt_jesTotalNoTimeDown;
   Float_t         MET_phi_jesTotalNoTimeDown;
   Float_t         Jet_pt_jesTotalNoFlavorNoTimeDown[33];   //[nJet]
   Float_t         Jet_mass_jesTotalNoFlavorNoTimeDown[33];   //[nJet]
   Float_t         MET_pt_jesTotalNoFlavorNoTimeDown;
   Float_t         MET_phi_jesTotalNoFlavorNoTimeDown;
   Float_t         Jet_pt_jesFlavorZJetDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorZJetDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorZJetDown;
   Float_t         MET_phi_jesFlavorZJetDown;
   Float_t         Jet_pt_jesFlavorPhotonJetDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPhotonJetDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPhotonJetDown;
   Float_t         MET_phi_jesFlavorPhotonJetDown;
   Float_t         Jet_pt_jesFlavorPureGluonDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureGluonDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureGluonDown;
   Float_t         MET_phi_jesFlavorPureGluonDown;
   Float_t         Jet_pt_jesFlavorPureQuarkDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureQuarkDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureQuarkDown;
   Float_t         MET_phi_jesFlavorPureQuarkDown;
   Float_t         Jet_pt_jesFlavorPureCharmDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureCharmDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureCharmDown;
   Float_t         MET_phi_jesFlavorPureCharmDown;
   Float_t         Jet_pt_jesFlavorPureBottomDown[33];   //[nJet]
   Float_t         Jet_mass_jesFlavorPureBottomDown[33];   //[nJet]
   Float_t         MET_pt_jesFlavorPureBottomDown;
   Float_t         MET_phi_jesFlavorPureBottomDown;
   Float_t         Jet_pt_jesTimeRunBCDDown[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunBCDDown[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunBCDDown;
   Float_t         MET_phi_jesTimeRunBCDDown;
   Float_t         Jet_pt_jesTimeRunEFDown[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunEFDown[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunEFDown;
   Float_t         MET_phi_jesTimeRunEFDown;
   Float_t         Jet_pt_jesTimeRunGDown[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunGDown[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunGDown;
   Float_t         MET_phi_jesTimeRunGDown;
   Float_t         Jet_pt_jesTimeRunHDown[33];   //[nJet]
   Float_t         Jet_mass_jesTimeRunHDown[33];   //[nJet]
   Float_t         MET_pt_jesTimeRunHDown;
   Float_t         MET_phi_jesTimeRunHDown;
   Float_t         Jet_pt_jesCorrelationGroupMPFInSituDown[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupMPFInSituDown[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupMPFInSituDown;
   Float_t         MET_phi_jesCorrelationGroupMPFInSituDown;
   Float_t         Jet_pt_jesCorrelationGroupIntercalibrationDown[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupIntercalibrationDown[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupIntercalibrationDown;
   Float_t         MET_phi_jesCorrelationGroupIntercalibrationDown;
   Float_t         Jet_pt_jesCorrelationGroupbJESDown[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupbJESDown[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupbJESDown;
   Float_t         MET_phi_jesCorrelationGroupbJESDown;
   Float_t         Jet_pt_jesCorrelationGroupFlavorDown[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupFlavorDown[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupFlavorDown;
   Float_t         MET_phi_jesCorrelationGroupFlavorDown;
   Float_t         Jet_pt_jesCorrelationGroupUncorrelatedDown[33];   //[nJet]
   Float_t         Jet_mass_jesCorrelationGroupUncorrelatedDown[33];   //[nJet]
   Float_t         MET_pt_jesCorrelationGroupUncorrelatedDown;
   Float_t         MET_phi_jesCorrelationGroupUncorrelatedDown;
   Float_t         MET_pt_unclustEnDown;
   Float_t         MET_phi_unclustEnDown;
   Float_t         FatJet_pt_nom[3];   //[nFatJet]
   Float_t         FatJet_mass_nom[3];   //[nFatJet]
   Float_t         FatJet_pt_jerUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jerUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jmrUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jmsUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteStatUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteStatUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteScaleUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteScaleUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteFlavMapUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteFlavMapUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteMPFBiasUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteMPFBiasUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFragmentationUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFragmentationUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSinglePionECALUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSinglePionECALUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSinglePionHCALUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSinglePionHCALUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorQCDUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorQCDUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimePtEtaUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimePtEtaUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeJEREC1Up[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeJEREC1Up[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeJEREC2Up[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeJEREC2Up[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeJERHFUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeJERHFUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtBBUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtBBUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtEC1Up[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtEC1Up[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtEC2Up[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtEC2Up[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtHFUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtHFUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeBalUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeBalUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeFSRUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeFSRUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeStatFSRUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeStatFSRUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeStatECUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeStatECUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeStatHFUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeStatHFUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpDataMCUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpDataMCUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtRefUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtRefUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtBBUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtBBUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtEC1Up[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtEC1Up[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtEC2Up[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtEC2Up[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtHFUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtHFUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpMuZeroUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpMuZeroUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpEnvelopeUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpEnvelopeUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalPileUpUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalPileUpUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalRelativeUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalRelativeUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalPtUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalPtUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalScaleUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalScaleUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalAbsoluteUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalAbsoluteUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalMCUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalMCUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalNoFlavorUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalNoFlavorUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalNoTimeUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalNoTimeUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalNoFlavorNoTimeUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalNoFlavorNoTimeUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorZJetUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorZJetUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPhotonJetUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPhotonJetUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureGluonUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureGluonUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureQuarkUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureQuarkUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureCharmUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureCharmUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureBottomUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureBottomUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunBCDUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunBCDUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunEFUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunEFUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunGUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunGUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunHUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunHUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupMPFInSituUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupMPFInSituUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupIntercalibrationUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupIntercalibrationUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupbJESUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupbJESUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupFlavorUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupFlavorUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupUncorrelatedUp[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupUncorrelatedUp[3];   //[nFatJet]
   Float_t         FatJet_pt_jerDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jerDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jmrDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jmsDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteStatDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteStatDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteScaleDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteScaleDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteFlavMapDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteFlavMapDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesAbsoluteMPFBiasDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesAbsoluteMPFBiasDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFragmentationDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFragmentationDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSinglePionECALDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSinglePionECALDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSinglePionHCALDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSinglePionHCALDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorQCDDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorQCDDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimePtEtaDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimePtEtaDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeJEREC1Down[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeJEREC1Down[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeJEREC2Down[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeJEREC2Down[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeJERHFDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeJERHFDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtBBDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtBBDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtEC1Down[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtEC1Down[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtEC2Down[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtEC2Down[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativePtHFDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativePtHFDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeBalDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeBalDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeFSRDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeFSRDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeStatFSRDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeStatFSRDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeStatECDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeStatECDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesRelativeStatHFDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesRelativeStatHFDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpDataMCDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpDataMCDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtRefDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtRefDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtBBDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtBBDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtEC1Down[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtEC1Down[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtEC2Down[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtEC2Down[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpPtHFDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpPtHFDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpMuZeroDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpMuZeroDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesPileUpEnvelopeDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesPileUpEnvelopeDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalPileUpDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalPileUpDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalRelativeDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalRelativeDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalPtDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalPtDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalScaleDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalScaleDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalAbsoluteDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalAbsoluteDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesSubTotalMCDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesSubTotalMCDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalNoFlavorDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalNoFlavorDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalNoTimeDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalNoTimeDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTotalNoFlavorNoTimeDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTotalNoFlavorNoTimeDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorZJetDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorZJetDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPhotonJetDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPhotonJetDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureGluonDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureGluonDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureQuarkDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureQuarkDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureCharmDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureCharmDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesFlavorPureBottomDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesFlavorPureBottomDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunBCDDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunBCDDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunEFDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunEFDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunGDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunGDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesTimeRunHDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesTimeRunHDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupMPFInSituDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupMPFInSituDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupIntercalibrationDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupIntercalibrationDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupbJESDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupbJESDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupFlavorDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupFlavorDown[3];   //[nFatJet]
   Float_t         FatJet_pt_jesCorrelationGroupUncorrelatedDown[3];   //[nFatJet]
   Float_t         FatJet_mass_jesCorrelationGroupUncorrelatedDown[3];   //[nFatJet]
   Float_t         Muon_pt_corrected[6];   //[nMuon]
   Float_t         MHT_pt;
   Float_t         MHT_phi;
   UChar_t         Jet_mhtCleaning[33];   //[nJet]
   Float_t         Jet_btagSF[33];   //[nJet]
   Float_t         Jet_btagSF_up[33];   //[nJet]
   Float_t         Jet_btagSF_down[33];   //[nJet]
   Float_t         Jet_btagSF_shape[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_jes[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_jes[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_lf[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_lf[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_hf[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_hf[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_hfstats1[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_hfstats1[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_hfstats2[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_hfstats2[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_lfstats1[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_lfstats1[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_lfstats2[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_lfstats2[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_cferr1[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_cferr1[33];   //[nJet]
   Float_t         Jet_btagSF_shape_up_cferr2[33];   //[nJet]
   Float_t         Jet_btagSF_shape_down_cferr2[33];   //[nJet]
   Int_t           Vtype;
   Float_t         V_pt;
   Float_t         V_eta;
   Float_t         V_phi;
   Float_t         V_mass;
   Float_t         V_mt;
   Bool_t          Jet_lepFilter[33];   //[nJet]
   Int_t           vLidx[2];
   Int_t           hJidx[2];
   Int_t           hJidxCMVA[2];
   Float_t         H_pt;
   Float_t         H_eta;
   Float_t         H_phi;
   Float_t         H_mass;
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
   Float_t         Jet_Pt[33];   //[nJet]
   Float_t         Jet_PtReg[33];   //[nJet]
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
   Bool_t          FatJet_lepFilter[3];   //[nFatJet]
   Float_t         FatJet_Pt[3];   //[nFatJet]
   Float_t         FatJet_Msoftdrop[3];   //[nFatJet]
   Int_t           FatJet_FlavourComposition[3];   //[nFatJet]
   Bool_t          FatJet_HiggsProducts[3];   //[nFatJet]
   Bool_t          FatJet_WProducts[3];   //[nFatJet]
   Bool_t          FatJet_ZProducts[3];   //[nFatJet]

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
   TBranch        *b_nFatJet;   //!
   TBranch        *b_FatJet_area;   //!
   TBranch        *b_FatJet_btagCMVA;   //!
   TBranch        *b_FatJet_btagCSVV2;   //!
   TBranch        *b_FatJet_btagDeepB;   //!
   TBranch        *b_FatJet_btagHbb;   //!
   TBranch        *b_FatJet_eta;   //!
   TBranch        *b_FatJet_mass;   //!
   TBranch        *b_FatJet_msoftdrop;   //!
   TBranch        *b_FatJet_msoftdrop_chs;   //!
   TBranch        *b_FatJet_n2b1;   //!
   TBranch        *b_FatJet_n3b1;   //!
   TBranch        *b_FatJet_phi;   //!
   TBranch        *b_FatJet_pt;   //!
   TBranch        *b_FatJet_tau1;   //!
   TBranch        *b_FatJet_tau2;   //!
   TBranch        *b_FatJet_tau3;   //!
   TBranch        *b_FatJet_tau4;   //!
   TBranch        *b_FatJet_jetId;   //!
   TBranch        *b_FatJet_subJetIdx1;   //!
   TBranch        *b_FatJet_subJetIdx2;   //!
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
   TBranch        *b_nGenVisTau;   //!
   TBranch        *b_GenVisTau_eta;   //!
   TBranch        *b_GenVisTau_mass;   //!
   TBranch        *b_GenVisTau_phi;   //!
   TBranch        *b_GenVisTau_pt;   //!
   TBranch        *b_GenVisTau_charge;   //!
   TBranch        *b_GenVisTau_genPartIdxMother;   //!
   TBranch        *b_GenVisTau_status;   //!
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
   TBranch        *b_nPhoton;   //!
   TBranch        *b_Photon_eCorr;   //!
   TBranch        *b_Photon_energyErr;   //!
   TBranch        *b_Photon_eta;   //!
   TBranch        *b_Photon_hoe;   //!
   TBranch        *b_Photon_mass;   //!
   TBranch        *b_Photon_mvaID;   //!
   TBranch        *b_Photon_pfRelIso03_all;   //!
   TBranch        *b_Photon_pfRelIso03_chg;   //!
   TBranch        *b_Photon_phi;   //!
   TBranch        *b_Photon_pt;   //!
   TBranch        *b_Photon_r9;   //!
   TBranch        *b_Photon_sieie;   //!
   TBranch        *b_Photon_charge;   //!
   TBranch        *b_Photon_cutBased;   //!
   TBranch        *b_Photon_electronIdx;   //!
   TBranch        *b_Photon_jetIdx;   //!
   TBranch        *b_Photon_pdgId;   //!
   TBranch        *b_Photon_vidNestedWPBitmap;   //!
   TBranch        *b_Photon_electronVeto;   //!
   TBranch        *b_Photon_isScEtaEB;   //!
   TBranch        *b_Photon_isScEtaEE;   //!
   TBranch        *b_Photon_mvaID_WP80;   //!
   TBranch        *b_Photon_mvaID_WP90;   //!
   TBranch        *b_Photon_pixelSeed;   //!
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
   TBranch        *b_nSubJet;   //!
   TBranch        *b_SubJet_btagCMVA;   //!
   TBranch        *b_SubJet_btagCSVV2;   //!
   TBranch        *b_SubJet_btagDeepB;   //!
   TBranch        *b_SubJet_eta;   //!
   TBranch        *b_SubJet_mass;   //!
   TBranch        *b_SubJet_n2b1;   //!
   TBranch        *b_SubJet_n3b1;   //!
   TBranch        *b_SubJet_phi;   //!
   TBranch        *b_SubJet_pt;   //!
   TBranch        *b_SubJet_tau1;   //!
   TBranch        *b_SubJet_tau2;   //!
   TBranch        *b_SubJet_tau3;   //!
   TBranch        *b_SubJet_tau4;   //!
   TBranch        *b_nTau;   //!
   TBranch        *b_Tau_chargedIso;   //!
   TBranch        *b_Tau_dxy;   //!
   TBranch        *b_Tau_dz;   //!
   TBranch        *b_Tau_eta;   //!
   TBranch        *b_Tau_leadTkDeltaEta;   //!
   TBranch        *b_Tau_leadTkDeltaPhi;   //!
   TBranch        *b_Tau_leadTkPtOverTauPt;   //!
   TBranch        *b_Tau_mass;   //!
   TBranch        *b_Tau_neutralIso;   //!
   TBranch        *b_Tau_phi;   //!
   TBranch        *b_Tau_photonsOutsideSignalCone;   //!
   TBranch        *b_Tau_pt;   //!
   TBranch        *b_Tau_puCorr;   //!
   TBranch        *b_Tau_rawAntiEle;   //!
   TBranch        *b_Tau_rawIso;   //!
   TBranch        *b_Tau_rawIsodR03;   //!
   TBranch        *b_Tau_rawMVAnewDM;   //!
   TBranch        *b_Tau_rawMVAoldDM;   //!
   TBranch        *b_Tau_rawMVAoldDMdR03;   //!
   TBranch        *b_Tau_charge;   //!
   TBranch        *b_Tau_decayMode;   //!
   TBranch        *b_Tau_jetIdx;   //!
   TBranch        *b_Tau_rawAntiEleCat;   //!
   TBranch        *b_Tau_idAntiEle;   //!
   TBranch        *b_Tau_idAntiMu;   //!
   TBranch        *b_Tau_idDecayMode;   //!
   TBranch        *b_Tau_idDecayModeNewDMs;   //!
   TBranch        *b_Tau_idMVAnew;   //!
   TBranch        *b_Tau_idMVAoldDM;   //!
   TBranch        *b_Tau_idMVAoldDMdR03;   //!
   TBranch        *b_TkMET_phi;   //!
   TBranch        *b_TkMET_pt;   //!
   TBranch        *b_TkMET_sumEt;   //!
   TBranch        *b_nTrigObj;   //!
   TBranch        *b_TrigObj_pt;   //!
   TBranch        *b_TrigObj_eta;   //!
   TBranch        *b_TrigObj_phi;   //!
   TBranch        *b_TrigObj_l1pt;   //!
   TBranch        *b_TrigObj_l1pt_2;   //!
   TBranch        *b_TrigObj_l2pt;   //!
   TBranch        *b_TrigObj_id;   //!
   TBranch        *b_TrigObj_l1iso;   //!
   TBranch        *b_TrigObj_l1charge;   //!
   TBranch        *b_TrigObj_filterBits;   //!
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
   TBranch        *b_Photon_genPartIdx;   //!
   TBranch        *b_Photon_genPartFlav;   //!
   TBranch        *b_MET_fiducialGenPhi;   //!
   TBranch        *b_MET_fiducialGenPt;   //!
   TBranch        *b_Electron_cleanmask;   //!
   TBranch        *b_Jet_cleanmask;   //!
   TBranch        *b_Muon_cleanmask;   //!
   TBranch        *b_Photon_cleanmask;   //!
   TBranch        *b_Tau_cleanmask;   //!
   TBranch        *b_SV_chi2;   //!
   TBranch        *b_SV_eta;   //!
   TBranch        *b_SV_mass;   //!
   TBranch        *b_SV_ndof;   //!
   TBranch        *b_SV_phi;   //!
   TBranch        *b_SV_pt;   //!
   TBranch        *b_SV_x;   //!
   TBranch        *b_SV_y;   //!
   TBranch        *b_SV_z;   //!
   TBranch        *b_Tau_genPartIdx;   //!
   TBranch        *b_Tau_genPartFlav;   //!
   TBranch        *b_L1simulation_step;   //!
   TBranch        *b_HLTriggerFirstPath;   //!
   TBranch        *b_HLT_AK8PFJet360_TrimMass30;   //!
   TBranch        *b_HLT_AK8PFJet400_TrimMass30;   //!
   TBranch        *b_HLT_AK8PFHT750_TrimMass50;   //!
   TBranch        *b_HLT_AK8PFHT800_TrimMass50;   //!
   TBranch        *b_HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20;   //!
   TBranch        *b_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087;   //!
   TBranch        *b_HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087;   //!
   TBranch        *b_HLT_AK8DiPFJet300_200_TrimMass30;   //!
   TBranch        *b_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50;   //!
   TBranch        *b_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50;   //!
   TBranch        *b_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20;   //!
   TBranch        *b_HLT_AK8DiPFJet280_200_TrimMass30;   //!
   TBranch        *b_HLT_AK8DiPFJet250_200_TrimMass30;   //!
   TBranch        *b_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20;   //!
   TBranch        *b_HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20;   //!
   TBranch        *b_HLT_CaloJet260;   //!
   TBranch        *b_HLT_CaloJet500_NoJetID;   //!
   TBranch        *b_HLT_Dimuon13_PsiPrime;   //!
   TBranch        *b_HLT_Dimuon13_Upsilon;   //!
   TBranch        *b_HLT_Dimuon20_Jpsi;   //!
   TBranch        *b_HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf;   //!
   TBranch        *b_HLT_DoubleEle25_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_DoubleEle33_CaloIdL;   //!
   TBranch        *b_HLT_DoubleEle33_CaloIdL_MW;   //!
   TBranch        *b_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW;   //!
   TBranch        *b_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1;   //!
   TBranch        *b_HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1;   //!
   TBranch        *b_HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg;   //!
   TBranch        *b_HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1;   //!
   TBranch        *b_HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL;   //!
   TBranch        *b_HLT_DoubleMu33NoFiltersNoVtx;   //!
   TBranch        *b_HLT_DoubleMu38NoFiltersNoVtx;   //!
   TBranch        *b_HLT_DoubleMu23NoFiltersNoVtxDisplaced;   //!
   TBranch        *b_HLT_DoubleMu28NoFiltersNoVtxDisplaced;   //!
   TBranch        *b_HLT_DoubleMu0;   //!
   TBranch        *b_HLT_DoubleMu4_3_Bs;   //!
   TBranch        *b_HLT_DoubleMu4_3_Jpsi_Displaced;   //!
   TBranch        *b_HLT_DoubleMu4_JpsiTrk_Displaced;   //!
   TBranch        *b_HLT_DoubleMu4_LowMassNonResonantTrk_Displaced;   //!
   TBranch        *b_HLT_DoubleMu3_Trk_Tau3mu;   //!
   TBranch        *b_HLT_DoubleMu4_PsiPrimeTrk_Displaced;   //!
   TBranch        *b_HLT_Mu7p5_L2Mu2_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_L2Mu2_Upsilon;   //!
   TBranch        *b_HLT_Mu7p5_Track2_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_Track3p5_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_Track7_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_Track2_Upsilon;   //!
   TBranch        *b_HLT_Mu7p5_Track3p5_Upsilon;   //!
   TBranch        *b_HLT_Mu7p5_Track7_Upsilon;   //!
   TBranch        *b_HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing;   //!
   TBranch        *b_HLT_Dimuon0er16_Jpsi_NoVertexing;   //!
   TBranch        *b_HLT_Dimuon6_Jpsi_NoVertexing;   //!
   TBranch        *b_HLT_Photon150;   //!
   TBranch        *b_HLT_Photon90_CaloIdL_HT300;   //!
   TBranch        *b_HLT_HT250_CaloMET70;   //!
   TBranch        *b_HLT_DoublePhoton60;   //!
   TBranch        *b_HLT_DoublePhoton85;   //!
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
   TBranch        *b_HLT_HT200;   //!
   TBranch        *b_HLT_HT275;   //!
   TBranch        *b_HLT_HT325;   //!
   TBranch        *b_HLT_HT425;   //!
   TBranch        *b_HLT_HT575;   //!
   TBranch        *b_HLT_HT410to430;   //!
   TBranch        *b_HLT_HT430to450;   //!
   TBranch        *b_HLT_HT450to470;   //!
   TBranch        *b_HLT_HT470to500;   //!
   TBranch        *b_HLT_HT500to550;   //!
   TBranch        *b_HLT_HT550to650;   //!
   TBranch        *b_HLT_HT650;   //!
   TBranch        *b_HLT_Mu16_eta2p1_MET30;   //!
   TBranch        *b_HLT_IsoMu16_eta2p1_MET30;   //!
   TBranch        *b_HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1;   //!
   TBranch        *b_HLT_IsoMu17_eta2p1;   //!
   TBranch        *b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20;   //!
   TBranch        *b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1;   //!
   TBranch        *b_HLT_DoubleIsoMu17_eta2p1;   //!
   TBranch        *b_HLT_DoubleIsoMu17_eta2p1_noDzCut;   //!
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
   TBranch        *b_HLT_L1SingleMu18;   //!
   TBranch        *b_HLT_L2Mu10;   //!
   TBranch        *b_HLT_L1SingleMuOpen;   //!
   TBranch        *b_HLT_L1SingleMuOpen_DT;   //!
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
   TBranch        *b_HLT_PFTau120_eta2p1;   //!
   TBranch        *b_HLT_PFTau140_eta2p1;   //!
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
   TBranch        *b_HLT_DoubleMu18NoFiltersNoVtx;   //!
   TBranch        *b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight;   //!
   TBranch        *b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose;   //!
   TBranch        *b_HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose;   //!
   TBranch        *b_HLT_Mu28NoFiltersNoVtx_CentralCaloJet40;   //!
   TBranch        *b_HLT_PFHT300_PFMET100;   //!
   TBranch        *b_HLT_PFHT300_PFMET110;   //!
   TBranch        *b_HLT_PFHT550_4JetPt50;   //!
   TBranch        *b_HLT_PFHT650_4JetPt50;   //!
   TBranch        *b_HLT_PFHT750_4JetPt50;   //!
   TBranch        *b_HLT_PFHT750_4JetPt70;   //!
   TBranch        *b_HLT_PFHT750_4JetPt80;   //!
   TBranch        *b_HLT_PFHT800_4JetPt50;   //!
   TBranch        *b_HLT_PFHT850_4JetPt50;   //!
   TBranch        *b_HLT_PFJet15_NoCaloMatched;   //!
   TBranch        *b_HLT_PFJet25_NoCaloMatched;   //!
   TBranch        *b_HLT_DiPFJet15_NoCaloMatched;   //!
   TBranch        *b_HLT_DiPFJet25_NoCaloMatched;   //!
   TBranch        *b_HLT_DiPFJet15_FBEta3_NoCaloMatched;   //!
   TBranch        *b_HLT_DiPFJet25_FBEta3_NoCaloMatched;   //!
   TBranch        *b_HLT_DiPFJetAve15_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve25_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve35_HFJEC;   //!
   TBranch        *b_HLT_AK8PFJet40;   //!
   TBranch        *b_HLT_AK8PFJet60;   //!
   TBranch        *b_HLT_AK8PFJet80;   //!
   TBranch        *b_HLT_AK8PFJet140;   //!
   TBranch        *b_HLT_AK8PFJet200;   //!
   TBranch        *b_HLT_AK8PFJet260;   //!
   TBranch        *b_HLT_AK8PFJet320;   //!
   TBranch        *b_HLT_AK8PFJet400;   //!
   TBranch        *b_HLT_AK8PFJet450;   //!
   TBranch        *b_HLT_AK8PFJet500;   //!
   TBranch        *b_HLT_PFJet40;   //!
   TBranch        *b_HLT_PFJet60;   //!
   TBranch        *b_HLT_PFJet80;   //!
   TBranch        *b_HLT_PFJet140;   //!
   TBranch        *b_HLT_PFJet200;   //!
   TBranch        *b_HLT_PFJet260;   //!
   TBranch        *b_HLT_PFJet320;   //!
   TBranch        *b_HLT_PFJet400;   //!
   TBranch        *b_HLT_PFJet450;   //!
   TBranch        *b_HLT_PFJet500;   //!
   TBranch        *b_HLT_DiPFJetAve40;   //!
   TBranch        *b_HLT_DiPFJetAve60;   //!
   TBranch        *b_HLT_DiPFJetAve80;   //!
   TBranch        *b_HLT_DiPFJetAve140;   //!
   TBranch        *b_HLT_DiPFJetAve200;   //!
   TBranch        *b_HLT_DiPFJetAve260;   //!
   TBranch        *b_HLT_DiPFJetAve320;   //!
   TBranch        *b_HLT_DiPFJetAve400;   //!
   TBranch        *b_HLT_DiPFJetAve500;   //!
   TBranch        *b_HLT_DiPFJetAve60_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve80_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve100_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve160_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve220_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve300_HFJEC;   //!
   TBranch        *b_HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140;   //!
   TBranch        *b_HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80;   //!
   TBranch        *b_HLT_DiCentralPFJet170;   //!
   TBranch        *b_HLT_SingleCentralPFJet170_CFMax0p1;   //!
   TBranch        *b_HLT_DiCentralPFJet170_CFMax0p1;   //!
   TBranch        *b_HLT_DiCentralPFJet220_CFMax0p3;   //!
   TBranch        *b_HLT_DiCentralPFJet330_CFMax0p5;   //!
   TBranch        *b_HLT_DiCentralPFJet430;   //!
   TBranch        *b_HLT_PFHT125;   //!
   TBranch        *b_HLT_PFHT200;   //!
   TBranch        *b_HLT_PFHT250;   //!
   TBranch        *b_HLT_PFHT300;   //!
   TBranch        *b_HLT_PFHT350;   //!
   TBranch        *b_HLT_PFHT400;   //!
   TBranch        *b_HLT_PFHT475;   //!
   TBranch        *b_HLT_PFHT600;   //!
   TBranch        *b_HLT_PFHT650;   //!
   TBranch        *b_HLT_PFHT800;   //!
   TBranch        *b_HLT_PFHT900;   //!
   TBranch        *b_HLT_PFHT200_PFAlphaT0p51;   //!
   TBranch        *b_HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57;   //!
   TBranch        *b_HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63;   //!
   TBranch        *b_HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55;   //!
   TBranch        *b_HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58;   //!
   TBranch        *b_HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53;   //!
   TBranch        *b_HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54;   //!
   TBranch        *b_HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52;   //!
   TBranch        *b_HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53;   //!
   TBranch        *b_HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51;   //!
   TBranch        *b_HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52;   //!
   TBranch        *b_HLT_MET60_IsoTrk35_Loose;   //!
   TBranch        *b_HLT_MET75_IsoTrk50;   //!
   TBranch        *b_HLT_MET90_IsoTrk50;   //!
   TBranch        *b_HLT_PFMET120_BTagCSV_p067;   //!
   TBranch        *b_HLT_PFMET120_Mu5;   //!
   TBranch        *b_HLT_PFMET170_NotCleaned;   //!
   TBranch        *b_HLT_PFMET170_NoiseCleaned;   //!
   TBranch        *b_HLT_PFMET170_HBHECleaned;   //!
   TBranch        *b_HLT_PFMET170_JetIdCleaned;   //!
   TBranch        *b_HLT_PFMET170_BeamHaloCleaned;   //!
   TBranch        *b_HLT_PFMET170_HBHE_BeamHaloCleaned;   //!
   TBranch        *b_HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned;   //!
   TBranch        *b_HLT_PFMET90_PFMHT90_IDTight;   //!
   TBranch        *b_HLT_PFMET100_PFMHT100_IDTight;   //!
   TBranch        *b_HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned;   //!
   TBranch        *b_HLT_PFMET110_PFMHT110_IDTight;   //!
   TBranch        *b_HLT_PFMET120_PFMHT120_IDTight;   //!
   TBranch        *b_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067;   //!
   TBranch        *b_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight;   //!
   TBranch        *b_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200;   //!
   TBranch        *b_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460;   //!
   TBranch        *b_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240;   //!
   TBranch        *b_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500;   //!
   TBranch        *b_HLT_QuadPFJet_VBF;   //!
   TBranch        *b_HLT_L1_TripleJet_VBF;   //!
   TBranch        *b_HLT_QuadJet45_TripleBTagCSV_p087;   //!
   TBranch        *b_HLT_QuadJet45_DoubleBTagCSV_p087;   //!
   TBranch        *b_HLT_DoubleJet90_Double30_TripleBTagCSV_p087;   //!
   TBranch        *b_HLT_DoubleJet90_Double30_DoubleBTagCSV_p087;   //!
   TBranch        *b_HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160;   //!
   TBranch        *b_HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6;   //!
   TBranch        *b_HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172;   //!
   TBranch        *b_HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6;   //!
   TBranch        *b_HLT_DoubleJetsC100_SingleBTagCSV_p026;   //!
   TBranch        *b_HLT_DoubleJetsC100_SingleBTagCSV_p014;   //!
   TBranch        *b_HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350;   //!
   TBranch        *b_HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350;   //!
   TBranch        *b_HLT_Photon135_PFMET100;   //!
   TBranch        *b_HLT_Photon20_CaloIdVL_IsoL;   //!
   TBranch        *b_HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40;   //!
   TBranch        *b_HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF;   //!
   TBranch        *b_HLT_Photon250_NoHE;   //!
   TBranch        *b_HLT_Photon300_NoHE;   //!
   TBranch        *b_HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60;   //!
   TBranch        *b_HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15;   //!
   TBranch        *b_HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40;   //!
   TBranch        *b_HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF;   //!
   TBranch        *b_HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40;   //!
   TBranch        *b_HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF;   //!
   TBranch        *b_HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40;   //!
   TBranch        *b_HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF;   //!
   TBranch        *b_HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40;   //!
   TBranch        *b_HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF;   //!
   TBranch        *b_HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40;   //!
   TBranch        *b_HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL;   //!
   TBranch        *b_HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_BTagMu_DiJet20_Mu5;   //!
   TBranch        *b_HLT_BTagMu_DiJet40_Mu5;   //!
   TBranch        *b_HLT_BTagMu_DiJet70_Mu5;   //!
   TBranch        *b_HLT_BTagMu_DiJet110_Mu5;   //!
   TBranch        *b_HLT_BTagMu_DiJet170_Mu5;   //!
   TBranch        *b_HLT_BTagMu_Jet300_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK8Jet300_Mu5;   //!
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
   TBranch        *b_HLT_DiMu9_Ele9_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_TripleMu_5_3_3;   //!
   TBranch        *b_HLT_TripleMu_12_10_5;   //!
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
   TBranch        *b_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5;   //!
   TBranch        *b_HLT_PFHT650_WideJetMJJ950DEtaJJ1p5;   //!
   TBranch        *b_HLT_Photon22;   //!
   TBranch        *b_HLT_Photon30;   //!
   TBranch        *b_HLT_Photon36;   //!
   TBranch        *b_HLT_Photon50;   //!
   TBranch        *b_HLT_Photon75;   //!
   TBranch        *b_HLT_Photon90;   //!
   TBranch        *b_HLT_Photon120;   //!
   TBranch        *b_HLT_Photon175;   //!
   TBranch        *b_HLT_Photon165_HE10;   //!
   TBranch        *b_HLT_Photon22_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon30_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon36_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon50_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon75_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon90_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon120_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon165_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90;   //!
   TBranch        *b_HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70;   //!
   TBranch        *b_HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55;   //!
   TBranch        *b_HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55;   //!
   TBranch        *b_HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi_Muon;   //!
   TBranch        *b_HLT_Dimuon0_Upsilon_Muon;   //!
   TBranch        *b_HLT_QuadMuon0_Dimuon0_Jpsi;   //!
   TBranch        *b_HLT_QuadMuon0_Dimuon0_Upsilon;   //!
   TBranch        *b_HLT_Rsq0p25_Calo;   //!
   TBranch        *b_HLT_RsqMR240_Rsq0p09_MR200_4jet_Calo;   //!
   TBranch        *b_HLT_RsqMR240_Rsq0p09_MR200_Calo;   //!
   TBranch        *b_HLT_Rsq0p25;   //!
   TBranch        *b_HLT_Rsq0p30;   //!
   TBranch        *b_HLT_RsqMR240_Rsq0p09_MR200;   //!
   TBranch        *b_HLT_RsqMR240_Rsq0p09_MR200_4jet;   //!
   TBranch        *b_HLT_RsqMR270_Rsq0p09_MR200;   //!
   TBranch        *b_HLT_RsqMR270_Rsq0p09_MR200_4jet;   //!
   TBranch        *b_HLT_Rsq0p02_MR300_TriPFJet80_60_40_BTagCSV_p063_p20_Mbb60_200;   //!
   TBranch        *b_HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;   //!
   TBranch        *b_HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;   //!
   TBranch        *b_HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;   //!
   TBranch        *b_HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200;   //!
   TBranch        *b_HLT_HT200_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT250_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT350_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT350_DisplacedDijet80_DisplacedTrack;   //!
   TBranch        *b_HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack;   //!
   TBranch        *b_HLT_HT350_DisplacedDijet40_Inclusive;   //!
   TBranch        *b_HLT_HT400_DisplacedDijet40_Inclusive;   //!
   TBranch        *b_HLT_HT500_DisplacedDijet40_Inclusive;   //!
   TBranch        *b_HLT_HT550_DisplacedDijet40_Inclusive;   //!
   TBranch        *b_HLT_HT550_DisplacedDijet80_Inclusive;   //!
   TBranch        *b_HLT_HT650_DisplacedDijet80_Inclusive;   //!
   TBranch        *b_HLT_HT750_DisplacedDijet80_Inclusive;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_DisplacedTrack;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_TightID_DisplacedTrack;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_Hadronic;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_TightID_Hadronic;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_VTightID_Hadronic;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_VVTightID_Hadronic;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack;   //!
   TBranch        *b_HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack;   //!
   TBranch        *b_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight;   //!
   TBranch        *b_HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight;   //!
   TBranch        *b_HLT_MonoCentralPFJet80_PFMETNoMu100_PFMHTNoMu100_IDTight;   //!
   TBranch        *b_HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight;   //!
   TBranch        *b_HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight;   //!
   TBranch        *b_HLT_Ele27_eta2p1_WPLoose_Gsf_HT200;   //!
   TBranch        *b_HLT_Photon90_CaloIdL_PFHT500;   //!
   TBranch        *b_HLT_DoubleMu8_Mass8_PFHT250;   //!
   TBranch        *b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250;   //!
   TBranch        *b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250;   //!
   TBranch        *b_HLT_DoubleMu8_Mass8_PFHT300;   //!
   TBranch        *b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300;   //!
   TBranch        *b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300;   //!
   TBranch        *b_HLT_Mu10_CentralPFJet30_BTagCSV_p13;   //!
   TBranch        *b_HLT_DoubleMu3_PFMET50;   //!
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
   TBranch        *b_HLT_Dimuon16_Jpsi;   //!
   TBranch        *b_HLT_Dimuon10_Jpsi_Barrel;   //!
   TBranch        *b_HLT_Dimuon8_PsiPrime_Barrel;   //!
   TBranch        *b_HLT_Dimuon8_Upsilon_Barrel;   //!
   TBranch        *b_HLT_Dimuon0_Phi_Barrel;   //!
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
   TBranch        *b_HLT_PFHT400_SixJet30_DoubleBTagCSV_p056;   //!
   TBranch        *b_HLT_PFHT450_SixJet40_BTagCSV_p056;   //!
   TBranch        *b_HLT_PFHT400_SixJet30;   //!
   TBranch        *b_HLT_PFHT450_SixJet40;   //!
   TBranch        *b_HLT_Ele115_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_Mu55;   //!
   TBranch        *b_HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15;   //!
   TBranch        *b_HLT_Photon90_CaloIdL_PFHT600;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity60ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity85ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity110ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity135ForEndOfFill;   //!
   TBranch        *b_HLT_PixelTracks_Multiplicity160ForEndOfFill;   //!
   TBranch        *b_HLT_FullTracks_Multiplicity80;   //!
   TBranch        *b_HLT_FullTracks_Multiplicity100;   //!
   TBranch        *b_HLT_FullTracks_Multiplicity130;   //!
   TBranch        *b_HLT_FullTracks_Multiplicity150;   //!
   TBranch        *b_HLT_ECALHT800;   //!
   TBranch        *b_HLT_DiSC30_18_EIso_AND_HE_Mass70;   //!
   TBranch        *b_HLT_Photon125;   //!
   TBranch        *b_HLT_MET100;   //!
   TBranch        *b_HLT_MET150;   //!
   TBranch        *b_HLT_MET200;   //!
   TBranch        *b_HLT_Ele27_HighEta_Ele20_Mass55;   //!
   TBranch        *b_HLT_L1FatEvents;   //!
   TBranch        *b_HLT_Physics;   //!
   TBranch        *b_HLT_L1FatEvents_part0;   //!
   TBranch        *b_HLT_L1FatEvents_part1;   //!
   TBranch        *b_HLT_L1FatEvents_part2;   //!
   TBranch        *b_HLT_L1FatEvents_part3;   //!
   TBranch        *b_HLT_Random;   //!
   TBranch        *b_HLT_ZeroBias;   //!
   TBranch        *b_HLT_AK4CaloJet30;   //!
   TBranch        *b_HLT_AK4CaloJet40;   //!
   TBranch        *b_HLT_AK4CaloJet50;   //!
   TBranch        *b_HLT_AK4CaloJet80;   //!
   TBranch        *b_HLT_AK4CaloJet100;   //!
   TBranch        *b_HLT_AK4PFJet30;   //!
   TBranch        *b_HLT_AK4PFJet50;   //!
   TBranch        *b_HLT_AK4PFJet80;   //!
   TBranch        *b_HLT_AK4PFJet100;   //!
   TBranch        *b_HLT_HISinglePhoton10;   //!
   TBranch        *b_HLT_HISinglePhoton15;   //!
   TBranch        *b_HLT_HISinglePhoton20;   //!
   TBranch        *b_HLT_HISinglePhoton40;   //!
   TBranch        *b_HLT_HISinglePhoton60;   //!
   TBranch        *b_HLT_EcalCalibration;   //!
   TBranch        *b_HLT_HcalCalibration;   //!
   TBranch        *b_HLT_GlobalRunHPDNoise;   //!
   TBranch        *b_HLT_L1BptxMinus;   //!
   TBranch        *b_HLT_L1BptxPlus;   //!
   TBranch        *b_HLT_L1NotBptxOR;   //!
   TBranch        *b_HLT_L1BeamGasMinus;   //!
   TBranch        *b_HLT_L1BeamGasPlus;   //!
   TBranch        *b_HLT_L1BptxXOR;   //!
   TBranch        *b_HLT_L1MinimumBiasHF_OR;   //!
   TBranch        *b_HLT_L1MinimumBiasHF_AND;   //!
   TBranch        *b_HLT_HcalNZS;   //!
   TBranch        *b_HLT_HcalPhiSym;   //!
   TBranch        *b_HLT_HcalIsolatedbunch;   //!
   TBranch        *b_HLT_ZeroBias_FirstCollisionAfterAbortGap;   //!
   TBranch        *b_HLT_ZeroBias_FirstCollisionAfterAbortGap_copy;   //!
   TBranch        *b_HLT_ZeroBias_FirstCollisionAfterAbortGap_TCDS;   //!
   TBranch        *b_HLT_ZeroBias_IsolatedBunches;   //!
   TBranch        *b_HLT_ZeroBias_FirstCollisionInTrain;   //!
   TBranch        *b_HLT_ZeroBias_FirstBXAfterTrain;   //!
   TBranch        *b_HLT_Photon500;   //!
   TBranch        *b_HLT_Photon600;   //!
   TBranch        *b_HLT_Mu300;   //!
   TBranch        *b_HLT_Mu350;   //!
   TBranch        *b_HLT_MET250;   //!
   TBranch        *b_HLT_MET300;   //!
   TBranch        *b_HLT_MET600;   //!
   TBranch        *b_HLT_MET700;   //!
   TBranch        *b_HLT_PFMET300;   //!
   TBranch        *b_HLT_PFMET400;   //!
   TBranch        *b_HLT_PFMET500;   //!
   TBranch        *b_HLT_PFMET600;   //!
   TBranch        *b_HLT_Ele250_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_Ele300_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_HT2000;   //!
   TBranch        *b_HLT_HT2500;   //!
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
   TBranch        *b_FatJet_pt_nom;   //!
   TBranch        *b_FatJet_mass_nom;   //!
   TBranch        *b_FatJet_pt_jerUp;   //!
   TBranch        *b_FatJet_mass_jerUp;   //!
   TBranch        *b_FatJet_mass_jmrUp;   //!
   TBranch        *b_FatJet_mass_jmsUp;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteStatUp;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteStatUp;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteScaleUp;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteScaleUp;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteFlavMapUp;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteFlavMapUp;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteMPFBiasUp;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteMPFBiasUp;   //!
   TBranch        *b_FatJet_pt_jesFragmentationUp;   //!
   TBranch        *b_FatJet_mass_jesFragmentationUp;   //!
   TBranch        *b_FatJet_pt_jesSinglePionECALUp;   //!
   TBranch        *b_FatJet_mass_jesSinglePionECALUp;   //!
   TBranch        *b_FatJet_pt_jesSinglePionHCALUp;   //!
   TBranch        *b_FatJet_mass_jesSinglePionHCALUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorQCDUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorQCDUp;   //!
   TBranch        *b_FatJet_pt_jesTimePtEtaUp;   //!
   TBranch        *b_FatJet_mass_jesTimePtEtaUp;   //!
   TBranch        *b_FatJet_pt_jesRelativeJEREC1Up;   //!
   TBranch        *b_FatJet_mass_jesRelativeJEREC1Up;   //!
   TBranch        *b_FatJet_pt_jesRelativeJEREC2Up;   //!
   TBranch        *b_FatJet_mass_jesRelativeJEREC2Up;   //!
   TBranch        *b_FatJet_pt_jesRelativeJERHFUp;   //!
   TBranch        *b_FatJet_mass_jesRelativeJERHFUp;   //!
   TBranch        *b_FatJet_pt_jesRelativePtBBUp;   //!
   TBranch        *b_FatJet_mass_jesRelativePtBBUp;   //!
   TBranch        *b_FatJet_pt_jesRelativePtEC1Up;   //!
   TBranch        *b_FatJet_mass_jesRelativePtEC1Up;   //!
   TBranch        *b_FatJet_pt_jesRelativePtEC2Up;   //!
   TBranch        *b_FatJet_mass_jesRelativePtEC2Up;   //!
   TBranch        *b_FatJet_pt_jesRelativePtHFUp;   //!
   TBranch        *b_FatJet_mass_jesRelativePtHFUp;   //!
   TBranch        *b_FatJet_pt_jesRelativeBalUp;   //!
   TBranch        *b_FatJet_mass_jesRelativeBalUp;   //!
   TBranch        *b_FatJet_pt_jesRelativeFSRUp;   //!
   TBranch        *b_FatJet_mass_jesRelativeFSRUp;   //!
   TBranch        *b_FatJet_pt_jesRelativeStatFSRUp;   //!
   TBranch        *b_FatJet_mass_jesRelativeStatFSRUp;   //!
   TBranch        *b_FatJet_pt_jesRelativeStatECUp;   //!
   TBranch        *b_FatJet_mass_jesRelativeStatECUp;   //!
   TBranch        *b_FatJet_pt_jesRelativeStatHFUp;   //!
   TBranch        *b_FatJet_mass_jesRelativeStatHFUp;   //!
   TBranch        *b_FatJet_pt_jesPileUpDataMCUp;   //!
   TBranch        *b_FatJet_mass_jesPileUpDataMCUp;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtRefUp;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtRefUp;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtBBUp;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtBBUp;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtEC1Up;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtEC1Up;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtEC2Up;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtEC2Up;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtHFUp;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtHFUp;   //!
   TBranch        *b_FatJet_pt_jesPileUpMuZeroUp;   //!
   TBranch        *b_FatJet_mass_jesPileUpMuZeroUp;   //!
   TBranch        *b_FatJet_pt_jesPileUpEnvelopeUp;   //!
   TBranch        *b_FatJet_mass_jesPileUpEnvelopeUp;   //!
   TBranch        *b_FatJet_pt_jesSubTotalPileUpUp;   //!
   TBranch        *b_FatJet_mass_jesSubTotalPileUpUp;   //!
   TBranch        *b_FatJet_pt_jesSubTotalRelativeUp;   //!
   TBranch        *b_FatJet_mass_jesSubTotalRelativeUp;   //!
   TBranch        *b_FatJet_pt_jesSubTotalPtUp;   //!
   TBranch        *b_FatJet_mass_jesSubTotalPtUp;   //!
   TBranch        *b_FatJet_pt_jesSubTotalScaleUp;   //!
   TBranch        *b_FatJet_mass_jesSubTotalScaleUp;   //!
   TBranch        *b_FatJet_pt_jesSubTotalAbsoluteUp;   //!
   TBranch        *b_FatJet_mass_jesSubTotalAbsoluteUp;   //!
   TBranch        *b_FatJet_pt_jesSubTotalMCUp;   //!
   TBranch        *b_FatJet_mass_jesSubTotalMCUp;   //!
   TBranch        *b_FatJet_pt_jesTotalUp;   //!
   TBranch        *b_FatJet_mass_jesTotalUp;   //!
   TBranch        *b_FatJet_pt_jesTotalNoFlavorUp;   //!
   TBranch        *b_FatJet_mass_jesTotalNoFlavorUp;   //!
   TBranch        *b_FatJet_pt_jesTotalNoTimeUp;   //!
   TBranch        *b_FatJet_mass_jesTotalNoTimeUp;   //!
   TBranch        *b_FatJet_pt_jesTotalNoFlavorNoTimeUp;   //!
   TBranch        *b_FatJet_mass_jesTotalNoFlavorNoTimeUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorZJetUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorZJetUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorPhotonJetUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorPhotonJetUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureGluonUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureGluonUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureQuarkUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureQuarkUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureCharmUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureCharmUp;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureBottomUp;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureBottomUp;   //!
   TBranch        *b_FatJet_pt_jesTimeRunBCDUp;   //!
   TBranch        *b_FatJet_mass_jesTimeRunBCDUp;   //!
   TBranch        *b_FatJet_pt_jesTimeRunEFUp;   //!
   TBranch        *b_FatJet_mass_jesTimeRunEFUp;   //!
   TBranch        *b_FatJet_pt_jesTimeRunGUp;   //!
   TBranch        *b_FatJet_mass_jesTimeRunGUp;   //!
   TBranch        *b_FatJet_pt_jesTimeRunHUp;   //!
   TBranch        *b_FatJet_mass_jesTimeRunHUp;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupMPFInSituUp;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupMPFInSituUp;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupIntercalibrationUp;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupIntercalibrationUp;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupbJESUp;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupbJESUp;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupFlavorUp;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupFlavorUp;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupUncorrelatedUp;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupUncorrelatedUp;   //!
   TBranch        *b_FatJet_pt_jerDown;   //!
   TBranch        *b_FatJet_mass_jerDown;   //!
   TBranch        *b_FatJet_mass_jmrDown;   //!
   TBranch        *b_FatJet_mass_jmsDown;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteStatDown;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteStatDown;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteScaleDown;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteScaleDown;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteFlavMapDown;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteFlavMapDown;   //!
   TBranch        *b_FatJet_pt_jesAbsoluteMPFBiasDown;   //!
   TBranch        *b_FatJet_mass_jesAbsoluteMPFBiasDown;   //!
   TBranch        *b_FatJet_pt_jesFragmentationDown;   //!
   TBranch        *b_FatJet_mass_jesFragmentationDown;   //!
   TBranch        *b_FatJet_pt_jesSinglePionECALDown;   //!
   TBranch        *b_FatJet_mass_jesSinglePionECALDown;   //!
   TBranch        *b_FatJet_pt_jesSinglePionHCALDown;   //!
   TBranch        *b_FatJet_mass_jesSinglePionHCALDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorQCDDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorQCDDown;   //!
   TBranch        *b_FatJet_pt_jesTimePtEtaDown;   //!
   TBranch        *b_FatJet_mass_jesTimePtEtaDown;   //!
   TBranch        *b_FatJet_pt_jesRelativeJEREC1Down;   //!
   TBranch        *b_FatJet_mass_jesRelativeJEREC1Down;   //!
   TBranch        *b_FatJet_pt_jesRelativeJEREC2Down;   //!
   TBranch        *b_FatJet_mass_jesRelativeJEREC2Down;   //!
   TBranch        *b_FatJet_pt_jesRelativeJERHFDown;   //!
   TBranch        *b_FatJet_mass_jesRelativeJERHFDown;   //!
   TBranch        *b_FatJet_pt_jesRelativePtBBDown;   //!
   TBranch        *b_FatJet_mass_jesRelativePtBBDown;   //!
   TBranch        *b_FatJet_pt_jesRelativePtEC1Down;   //!
   TBranch        *b_FatJet_mass_jesRelativePtEC1Down;   //!
   TBranch        *b_FatJet_pt_jesRelativePtEC2Down;   //!
   TBranch        *b_FatJet_mass_jesRelativePtEC2Down;   //!
   TBranch        *b_FatJet_pt_jesRelativePtHFDown;   //!
   TBranch        *b_FatJet_mass_jesRelativePtHFDown;   //!
   TBranch        *b_FatJet_pt_jesRelativeBalDown;   //!
   TBranch        *b_FatJet_mass_jesRelativeBalDown;   //!
   TBranch        *b_FatJet_pt_jesRelativeFSRDown;   //!
   TBranch        *b_FatJet_mass_jesRelativeFSRDown;   //!
   TBranch        *b_FatJet_pt_jesRelativeStatFSRDown;   //!
   TBranch        *b_FatJet_mass_jesRelativeStatFSRDown;   //!
   TBranch        *b_FatJet_pt_jesRelativeStatECDown;   //!
   TBranch        *b_FatJet_mass_jesRelativeStatECDown;   //!
   TBranch        *b_FatJet_pt_jesRelativeStatHFDown;   //!
   TBranch        *b_FatJet_mass_jesRelativeStatHFDown;   //!
   TBranch        *b_FatJet_pt_jesPileUpDataMCDown;   //!
   TBranch        *b_FatJet_mass_jesPileUpDataMCDown;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtRefDown;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtRefDown;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtBBDown;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtBBDown;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtEC1Down;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtEC1Down;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtEC2Down;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtEC2Down;   //!
   TBranch        *b_FatJet_pt_jesPileUpPtHFDown;   //!
   TBranch        *b_FatJet_mass_jesPileUpPtHFDown;   //!
   TBranch        *b_FatJet_pt_jesPileUpMuZeroDown;   //!
   TBranch        *b_FatJet_mass_jesPileUpMuZeroDown;   //!
   TBranch        *b_FatJet_pt_jesPileUpEnvelopeDown;   //!
   TBranch        *b_FatJet_mass_jesPileUpEnvelopeDown;   //!
   TBranch        *b_FatJet_pt_jesSubTotalPileUpDown;   //!
   TBranch        *b_FatJet_mass_jesSubTotalPileUpDown;   //!
   TBranch        *b_FatJet_pt_jesSubTotalRelativeDown;   //!
   TBranch        *b_FatJet_mass_jesSubTotalRelativeDown;   //!
   TBranch        *b_FatJet_pt_jesSubTotalPtDown;   //!
   TBranch        *b_FatJet_mass_jesSubTotalPtDown;   //!
   TBranch        *b_FatJet_pt_jesSubTotalScaleDown;   //!
   TBranch        *b_FatJet_mass_jesSubTotalScaleDown;   //!
   TBranch        *b_FatJet_pt_jesSubTotalAbsoluteDown;   //!
   TBranch        *b_FatJet_mass_jesSubTotalAbsoluteDown;   //!
   TBranch        *b_FatJet_pt_jesSubTotalMCDown;   //!
   TBranch        *b_FatJet_mass_jesSubTotalMCDown;   //!
   TBranch        *b_FatJet_pt_jesTotalDown;   //!
   TBranch        *b_FatJet_mass_jesTotalDown;   //!
   TBranch        *b_FatJet_pt_jesTotalNoFlavorDown;   //!
   TBranch        *b_FatJet_mass_jesTotalNoFlavorDown;   //!
   TBranch        *b_FatJet_pt_jesTotalNoTimeDown;   //!
   TBranch        *b_FatJet_mass_jesTotalNoTimeDown;   //!
   TBranch        *b_FatJet_pt_jesTotalNoFlavorNoTimeDown;   //!
   TBranch        *b_FatJet_mass_jesTotalNoFlavorNoTimeDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorZJetDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorZJetDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorPhotonJetDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorPhotonJetDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureGluonDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureGluonDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureQuarkDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureQuarkDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureCharmDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureCharmDown;   //!
   TBranch        *b_FatJet_pt_jesFlavorPureBottomDown;   //!
   TBranch        *b_FatJet_mass_jesFlavorPureBottomDown;   //!
   TBranch        *b_FatJet_pt_jesTimeRunBCDDown;   //!
   TBranch        *b_FatJet_mass_jesTimeRunBCDDown;   //!
   TBranch        *b_FatJet_pt_jesTimeRunEFDown;   //!
   TBranch        *b_FatJet_mass_jesTimeRunEFDown;   //!
   TBranch        *b_FatJet_pt_jesTimeRunGDown;   //!
   TBranch        *b_FatJet_mass_jesTimeRunGDown;   //!
   TBranch        *b_FatJet_pt_jesTimeRunHDown;   //!
   TBranch        *b_FatJet_mass_jesTimeRunHDown;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupMPFInSituDown;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupMPFInSituDown;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupIntercalibrationDown;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupIntercalibrationDown;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupbJESDown;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupbJESDown;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupFlavorDown;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupFlavorDown;   //!
   TBranch        *b_FatJet_pt_jesCorrelationGroupUncorrelatedDown;   //!
   TBranch        *b_FatJet_mass_jesCorrelationGroupUncorrelatedDown;   //!
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
   TBranch        *b_V_mt;   //!
   TBranch        *b_Jet_lepFilter;   //!
   TBranch        *b_vLidx;   //!
   TBranch        *b_hJidx;   //!
   TBranch        *b_hJidxCMVA;   //!
   TBranch        *b_H_pt;   //!
   TBranch        *b_H_eta;   //!
   TBranch        *b_H_phi;   //!
   TBranch        *b_H_mass;   //!
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
   TBranch        *b_FatJet_lepFilter;   //!
   TBranch        *b_FatJet_Pt;   //!
   TBranch        *b_FatJet_Msoftdrop;   //!
   TBranch        *b_FatJet_FlavourComposition;   //!
   TBranch        *b_FatJet_HiggsProducts;   //!
   TBranch        *b_FatJet_WProducts;   //!
   TBranch        *b_FatJet_ZProducts;   //!

   Myclass(TTree *tree=0);
   virtual ~Myclass();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef Myclass_cxx
Myclass::Myclass(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/hbb/ntuples/VHbbPostNano/2016/V4/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/arizzi-RunIIMoriond17-DeepAndR98/180517_163627/0000/tree_1.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/hbb/ntuples/VHbbPostNano/2016/V4/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/arizzi-RunIIMoriond17-DeepAndR98/180517_163627/0000/tree_1.root");
      }
      f->GetObject("Events",tree);

   }
   Init(tree);
}

Myclass::~Myclass()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t Myclass::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Myclass::LoadTree(Long64_t entry)
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

void Myclass::Init(TTree *tree)
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
   fChain->SetBranchAddress("nFatJet", &nFatJet, &b_nFatJet);
   fChain->SetBranchAddress("FatJet_area", FatJet_area, &b_FatJet_area);
   fChain->SetBranchAddress("FatJet_btagCMVA", FatJet_btagCMVA, &b_FatJet_btagCMVA);
   fChain->SetBranchAddress("FatJet_btagCSVV2", FatJet_btagCSVV2, &b_FatJet_btagCSVV2);
   fChain->SetBranchAddress("FatJet_btagDeepB", FatJet_btagDeepB, &b_FatJet_btagDeepB);
   fChain->SetBranchAddress("FatJet_btagHbb", FatJet_btagHbb, &b_FatJet_btagHbb);
   fChain->SetBranchAddress("FatJet_eta", FatJet_eta, &b_FatJet_eta);
   fChain->SetBranchAddress("FatJet_mass", FatJet_mass, &b_FatJet_mass);
   fChain->SetBranchAddress("FatJet_msoftdrop", FatJet_msoftdrop, &b_FatJet_msoftdrop);
   fChain->SetBranchAddress("FatJet_msoftdrop_chs", FatJet_msoftdrop_chs, &b_FatJet_msoftdrop_chs);
   fChain->SetBranchAddress("FatJet_n2b1", FatJet_n2b1, &b_FatJet_n2b1);
   fChain->SetBranchAddress("FatJet_n3b1", FatJet_n3b1, &b_FatJet_n3b1);
   fChain->SetBranchAddress("FatJet_phi", FatJet_phi, &b_FatJet_phi);
   fChain->SetBranchAddress("FatJet_pt", FatJet_pt, &b_FatJet_pt);
   fChain->SetBranchAddress("FatJet_tau1", FatJet_tau1, &b_FatJet_tau1);
   fChain->SetBranchAddress("FatJet_tau2", FatJet_tau2, &b_FatJet_tau2);
   fChain->SetBranchAddress("FatJet_tau3", FatJet_tau3, &b_FatJet_tau3);
   fChain->SetBranchAddress("FatJet_tau4", FatJet_tau4, &b_FatJet_tau4);
   fChain->SetBranchAddress("FatJet_jetId", FatJet_jetId, &b_FatJet_jetId);
   fChain->SetBranchAddress("FatJet_subJetIdx1", FatJet_subJetIdx1, &b_FatJet_subJetIdx1);
   fChain->SetBranchAddress("FatJet_subJetIdx2", FatJet_subJetIdx2, &b_FatJet_subJetIdx2);
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
   fChain->SetBranchAddress("nGenVisTau", &nGenVisTau, &b_nGenVisTau);
   fChain->SetBranchAddress("GenVisTau_eta", GenVisTau_eta, &b_GenVisTau_eta);
   fChain->SetBranchAddress("GenVisTau_mass", GenVisTau_mass, &b_GenVisTau_mass);
   fChain->SetBranchAddress("GenVisTau_phi", GenVisTau_phi, &b_GenVisTau_phi);
   fChain->SetBranchAddress("GenVisTau_pt", GenVisTau_pt, &b_GenVisTau_pt);
   fChain->SetBranchAddress("GenVisTau_charge", GenVisTau_charge, &b_GenVisTau_charge);
   fChain->SetBranchAddress("GenVisTau_genPartIdxMother", GenVisTau_genPartIdxMother, &b_GenVisTau_genPartIdxMother);
   fChain->SetBranchAddress("GenVisTau_status", GenVisTau_status, &b_GenVisTau_status);
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
   fChain->SetBranchAddress("nPhoton", &nPhoton, &b_nPhoton);
   fChain->SetBranchAddress("Photon_eCorr", Photon_eCorr, &b_Photon_eCorr);
   fChain->SetBranchAddress("Photon_energyErr", Photon_energyErr, &b_Photon_energyErr);
   fChain->SetBranchAddress("Photon_eta", Photon_eta, &b_Photon_eta);
   fChain->SetBranchAddress("Photon_hoe", Photon_hoe, &b_Photon_hoe);
   fChain->SetBranchAddress("Photon_mass", Photon_mass, &b_Photon_mass);
   fChain->SetBranchAddress("Photon_mvaID", Photon_mvaID, &b_Photon_mvaID);
   fChain->SetBranchAddress("Photon_pfRelIso03_all", Photon_pfRelIso03_all, &b_Photon_pfRelIso03_all);
   fChain->SetBranchAddress("Photon_pfRelIso03_chg", Photon_pfRelIso03_chg, &b_Photon_pfRelIso03_chg);
   fChain->SetBranchAddress("Photon_phi", Photon_phi, &b_Photon_phi);
   fChain->SetBranchAddress("Photon_pt", Photon_pt, &b_Photon_pt);
   fChain->SetBranchAddress("Photon_r9", Photon_r9, &b_Photon_r9);
   fChain->SetBranchAddress("Photon_sieie", Photon_sieie, &b_Photon_sieie);
   fChain->SetBranchAddress("Photon_charge", Photon_charge, &b_Photon_charge);
   fChain->SetBranchAddress("Photon_cutBased", Photon_cutBased, &b_Photon_cutBased);
   fChain->SetBranchAddress("Photon_electronIdx", Photon_electronIdx, &b_Photon_electronIdx);
   fChain->SetBranchAddress("Photon_jetIdx", Photon_jetIdx, &b_Photon_jetIdx);
   fChain->SetBranchAddress("Photon_pdgId", Photon_pdgId, &b_Photon_pdgId);
   fChain->SetBranchAddress("Photon_vidNestedWPBitmap", Photon_vidNestedWPBitmap, &b_Photon_vidNestedWPBitmap);
   fChain->SetBranchAddress("Photon_electronVeto", Photon_electronVeto, &b_Photon_electronVeto);
   fChain->SetBranchAddress("Photon_isScEtaEB", Photon_isScEtaEB, &b_Photon_isScEtaEB);
   fChain->SetBranchAddress("Photon_isScEtaEE", Photon_isScEtaEE, &b_Photon_isScEtaEE);
   fChain->SetBranchAddress("Photon_mvaID_WP80", Photon_mvaID_WP80, &b_Photon_mvaID_WP80);
   fChain->SetBranchAddress("Photon_mvaID_WP90", Photon_mvaID_WP90, &b_Photon_mvaID_WP90);
   fChain->SetBranchAddress("Photon_pixelSeed", Photon_pixelSeed, &b_Photon_pixelSeed);
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
   fChain->SetBranchAddress("nSubJet", &nSubJet, &b_nSubJet);
   fChain->SetBranchAddress("SubJet_btagCMVA", SubJet_btagCMVA, &b_SubJet_btagCMVA);
   fChain->SetBranchAddress("SubJet_btagCSVV2", SubJet_btagCSVV2, &b_SubJet_btagCSVV2);
   fChain->SetBranchAddress("SubJet_btagDeepB", SubJet_btagDeepB, &b_SubJet_btagDeepB);
   fChain->SetBranchAddress("SubJet_eta", SubJet_eta, &b_SubJet_eta);
   fChain->SetBranchAddress("SubJet_mass", SubJet_mass, &b_SubJet_mass);
   fChain->SetBranchAddress("SubJet_n2b1", SubJet_n2b1, &b_SubJet_n2b1);
   fChain->SetBranchAddress("SubJet_n3b1", SubJet_n3b1, &b_SubJet_n3b1);
   fChain->SetBranchAddress("SubJet_phi", SubJet_phi, &b_SubJet_phi);
   fChain->SetBranchAddress("SubJet_pt", SubJet_pt, &b_SubJet_pt);
   fChain->SetBranchAddress("SubJet_tau1", SubJet_tau1, &b_SubJet_tau1);
   fChain->SetBranchAddress("SubJet_tau2", SubJet_tau2, &b_SubJet_tau2);
   fChain->SetBranchAddress("SubJet_tau3", SubJet_tau3, &b_SubJet_tau3);
   fChain->SetBranchAddress("SubJet_tau4", SubJet_tau4, &b_SubJet_tau4);
   fChain->SetBranchAddress("nTau", &nTau, &b_nTau);
   fChain->SetBranchAddress("Tau_chargedIso", Tau_chargedIso, &b_Tau_chargedIso);
   fChain->SetBranchAddress("Tau_dxy", Tau_dxy, &b_Tau_dxy);
   fChain->SetBranchAddress("Tau_dz", Tau_dz, &b_Tau_dz);
   fChain->SetBranchAddress("Tau_eta", Tau_eta, &b_Tau_eta);
   fChain->SetBranchAddress("Tau_leadTkDeltaEta", Tau_leadTkDeltaEta, &b_Tau_leadTkDeltaEta);
   fChain->SetBranchAddress("Tau_leadTkDeltaPhi", Tau_leadTkDeltaPhi, &b_Tau_leadTkDeltaPhi);
   fChain->SetBranchAddress("Tau_leadTkPtOverTauPt", Tau_leadTkPtOverTauPt, &b_Tau_leadTkPtOverTauPt);
   fChain->SetBranchAddress("Tau_mass", Tau_mass, &b_Tau_mass);
   fChain->SetBranchAddress("Tau_neutralIso", Tau_neutralIso, &b_Tau_neutralIso);
   fChain->SetBranchAddress("Tau_phi", Tau_phi, &b_Tau_phi);
   fChain->SetBranchAddress("Tau_photonsOutsideSignalCone", Tau_photonsOutsideSignalCone, &b_Tau_photonsOutsideSignalCone);
   fChain->SetBranchAddress("Tau_pt", Tau_pt, &b_Tau_pt);
   fChain->SetBranchAddress("Tau_puCorr", Tau_puCorr, &b_Tau_puCorr);
   fChain->SetBranchAddress("Tau_rawAntiEle", Tau_rawAntiEle, &b_Tau_rawAntiEle);
   fChain->SetBranchAddress("Tau_rawIso", Tau_rawIso, &b_Tau_rawIso);
   fChain->SetBranchAddress("Tau_rawIsodR03", Tau_rawIsodR03, &b_Tau_rawIsodR03);
   fChain->SetBranchAddress("Tau_rawMVAnewDM", Tau_rawMVAnewDM, &b_Tau_rawMVAnewDM);
   fChain->SetBranchAddress("Tau_rawMVAoldDM", Tau_rawMVAoldDM, &b_Tau_rawMVAoldDM);
   fChain->SetBranchAddress("Tau_rawMVAoldDMdR03", Tau_rawMVAoldDMdR03, &b_Tau_rawMVAoldDMdR03);
   fChain->SetBranchAddress("Tau_charge", Tau_charge, &b_Tau_charge);
   fChain->SetBranchAddress("Tau_decayMode", Tau_decayMode, &b_Tau_decayMode);
   fChain->SetBranchAddress("Tau_jetIdx", Tau_jetIdx, &b_Tau_jetIdx);
   fChain->SetBranchAddress("Tau_rawAntiEleCat", Tau_rawAntiEleCat, &b_Tau_rawAntiEleCat);
   fChain->SetBranchAddress("Tau_idAntiEle", Tau_idAntiEle, &b_Tau_idAntiEle);
   fChain->SetBranchAddress("Tau_idAntiMu", Tau_idAntiMu, &b_Tau_idAntiMu);
   fChain->SetBranchAddress("Tau_idDecayMode", Tau_idDecayMode, &b_Tau_idDecayMode);
   fChain->SetBranchAddress("Tau_idDecayModeNewDMs", Tau_idDecayModeNewDMs, &b_Tau_idDecayModeNewDMs);
   fChain->SetBranchAddress("Tau_idMVAnew", Tau_idMVAnew, &b_Tau_idMVAnew);
   fChain->SetBranchAddress("Tau_idMVAoldDM", Tau_idMVAoldDM, &b_Tau_idMVAoldDM);
   fChain->SetBranchAddress("Tau_idMVAoldDMdR03", Tau_idMVAoldDMdR03, &b_Tau_idMVAoldDMdR03);
   fChain->SetBranchAddress("TkMET_phi", &TkMET_phi, &b_TkMET_phi);
   fChain->SetBranchAddress("TkMET_pt", &TkMET_pt, &b_TkMET_pt);
   fChain->SetBranchAddress("TkMET_sumEt", &TkMET_sumEt, &b_TkMET_sumEt);
   fChain->SetBranchAddress("nTrigObj", &nTrigObj, &b_nTrigObj);
   fChain->SetBranchAddress("TrigObj_pt", TrigObj_pt, &b_TrigObj_pt);
   fChain->SetBranchAddress("TrigObj_eta", TrigObj_eta, &b_TrigObj_eta);
   fChain->SetBranchAddress("TrigObj_phi", TrigObj_phi, &b_TrigObj_phi);
   fChain->SetBranchAddress("TrigObj_l1pt", TrigObj_l1pt, &b_TrigObj_l1pt);
   fChain->SetBranchAddress("TrigObj_l1pt_2", TrigObj_l1pt_2, &b_TrigObj_l1pt_2);
   fChain->SetBranchAddress("TrigObj_l2pt", TrigObj_l2pt, &b_TrigObj_l2pt);
   fChain->SetBranchAddress("TrigObj_id", TrigObj_id, &b_TrigObj_id);
   fChain->SetBranchAddress("TrigObj_l1iso", TrigObj_l1iso, &b_TrigObj_l1iso);
   fChain->SetBranchAddress("TrigObj_l1charge", TrigObj_l1charge, &b_TrigObj_l1charge);
   fChain->SetBranchAddress("TrigObj_filterBits", TrigObj_filterBits, &b_TrigObj_filterBits);
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
   fChain->SetBranchAddress("Photon_genPartIdx", Photon_genPartIdx, &b_Photon_genPartIdx);
   fChain->SetBranchAddress("Photon_genPartFlav", Photon_genPartFlav, &b_Photon_genPartFlav);
   fChain->SetBranchAddress("MET_fiducialGenPhi", &MET_fiducialGenPhi, &b_MET_fiducialGenPhi);
   fChain->SetBranchAddress("MET_fiducialGenPt", &MET_fiducialGenPt, &b_MET_fiducialGenPt);
   fChain->SetBranchAddress("Electron_cleanmask", Electron_cleanmask, &b_Electron_cleanmask);
   fChain->SetBranchAddress("Jet_cleanmask", Jet_cleanmask, &b_Jet_cleanmask);
   fChain->SetBranchAddress("Muon_cleanmask", Muon_cleanmask, &b_Muon_cleanmask);
   fChain->SetBranchAddress("Photon_cleanmask", Photon_cleanmask, &b_Photon_cleanmask);
   fChain->SetBranchAddress("Tau_cleanmask", Tau_cleanmask, &b_Tau_cleanmask);
   fChain->SetBranchAddress("SV_chi2", SV_chi2, &b_SV_chi2);
   fChain->SetBranchAddress("SV_eta", SV_eta, &b_SV_eta);
   fChain->SetBranchAddress("SV_mass", SV_mass, &b_SV_mass);
   fChain->SetBranchAddress("SV_ndof", SV_ndof, &b_SV_ndof);
   fChain->SetBranchAddress("SV_phi", SV_phi, &b_SV_phi);
   fChain->SetBranchAddress("SV_pt", SV_pt, &b_SV_pt);
   fChain->SetBranchAddress("SV_x", SV_x, &b_SV_x);
   fChain->SetBranchAddress("SV_y", SV_y, &b_SV_y);
   fChain->SetBranchAddress("SV_z", SV_z, &b_SV_z);
   fChain->SetBranchAddress("Tau_genPartIdx", Tau_genPartIdx, &b_Tau_genPartIdx);
   fChain->SetBranchAddress("Tau_genPartFlav", Tau_genPartFlav, &b_Tau_genPartFlav);
   fChain->SetBranchAddress("L1simulation_step", &L1simulation_step, &b_L1simulation_step);
   fChain->SetBranchAddress("HLTriggerFirstPath", &HLTriggerFirstPath, &b_HLTriggerFirstPath);
   fChain->SetBranchAddress("HLT_AK8PFJet360_TrimMass30", &HLT_AK8PFJet360_TrimMass30, &b_HLT_AK8PFJet360_TrimMass30);
   fChain->SetBranchAddress("HLT_AK8PFJet400_TrimMass30", &HLT_AK8PFJet400_TrimMass30, &b_HLT_AK8PFJet400_TrimMass30);
   fChain->SetBranchAddress("HLT_AK8PFHT750_TrimMass50", &HLT_AK8PFHT750_TrimMass50, &b_HLT_AK8PFHT750_TrimMass50);
   fChain->SetBranchAddress("HLT_AK8PFHT800_TrimMass50", &HLT_AK8PFHT800_TrimMass50, &b_HLT_AK8PFHT800_TrimMass50);
   fChain->SetBranchAddress("HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20", &HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20, &b_HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p20);
   fChain->SetBranchAddress("HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087", &HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087, &b_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p087);
   fChain->SetBranchAddress("HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087", &HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087, &b_HLT_AK8DiPFJet300_200_TrimMass30_BTagCSV_p087);
   fChain->SetBranchAddress("HLT_AK8DiPFJet300_200_TrimMass30", &HLT_AK8DiPFJet300_200_TrimMass30, &b_HLT_AK8DiPFJet300_200_TrimMass30);
   fChain->SetBranchAddress("HLT_AK8PFHT700_TrimR0p1PT0p03Mass50", &HLT_AK8PFHT700_TrimR0p1PT0p03Mass50, &b_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50);
   fChain->SetBranchAddress("HLT_AK8PFHT650_TrimR0p1PT0p03Mass50", &HLT_AK8PFHT650_TrimR0p1PT0p03Mass50, &b_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50);
   fChain->SetBranchAddress("HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20", &HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20, &b_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20);
   fChain->SetBranchAddress("HLT_AK8DiPFJet280_200_TrimMass30", &HLT_AK8DiPFJet280_200_TrimMass30, &b_HLT_AK8DiPFJet280_200_TrimMass30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet250_200_TrimMass30", &HLT_AK8DiPFJet250_200_TrimMass30, &b_HLT_AK8DiPFJet250_200_TrimMass30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20", &HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20, &b_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20);
   fChain->SetBranchAddress("HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20", &HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20, &b_HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20);
   fChain->SetBranchAddress("HLT_CaloJet260", &HLT_CaloJet260, &b_HLT_CaloJet260);
   fChain->SetBranchAddress("HLT_CaloJet500_NoJetID", &HLT_CaloJet500_NoJetID, &b_HLT_CaloJet500_NoJetID);
   fChain->SetBranchAddress("HLT_Dimuon13_PsiPrime", &HLT_Dimuon13_PsiPrime, &b_HLT_Dimuon13_PsiPrime);
   fChain->SetBranchAddress("HLT_Dimuon13_Upsilon", &HLT_Dimuon13_Upsilon, &b_HLT_Dimuon13_Upsilon);
   fChain->SetBranchAddress("HLT_Dimuon20_Jpsi", &HLT_Dimuon20_Jpsi, &b_HLT_Dimuon20_Jpsi);
   fChain->SetBranchAddress("HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf", &HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf, &b_HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf);
   fChain->SetBranchAddress("HLT_DoubleEle25_CaloIdL_GsfTrkIdVL", &HLT_DoubleEle25_CaloIdL_GsfTrkIdVL, &b_HLT_DoubleEle25_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_DoubleEle33_CaloIdL", &HLT_DoubleEle33_CaloIdL, &b_HLT_DoubleEle33_CaloIdL);
   fChain->SetBranchAddress("HLT_DoubleEle33_CaloIdL_MW", &HLT_DoubleEle33_CaloIdL_MW, &b_HLT_DoubleEle33_CaloIdL_MW);
   fChain->SetBranchAddress("HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW", &HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW, &b_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW);
   fChain->SetBranchAddress("HLT_DoubleEle33_CaloIdL_GsfTrkIdVL", &HLT_DoubleEle33_CaloIdL_GsfTrkIdVL, &b_HLT_DoubleEle33_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg", &HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg, &b_HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg", &HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg, &b_HLT_DoubleTightCombinedIsoPFTau35_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg", &HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg, &b_HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg", &HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg, &b_HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1", &HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1, &b_HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1);
   fChain->SetBranchAddress("HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1", &HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1, &b_HLT_DoubleTightCombinedIsoPFTau40_Trk1_eta2p1);
   fChain->SetBranchAddress("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg", &HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg, &b_HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg", &HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg, &b_HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg);
   fChain->SetBranchAddress("HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1", &HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1, &b_HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1);
   fChain->SetBranchAddress("HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL", &HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL, &b_HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL);
   fChain->SetBranchAddress("HLT_DoubleMu33NoFiltersNoVtx", &HLT_DoubleMu33NoFiltersNoVtx, &b_HLT_DoubleMu33NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_DoubleMu38NoFiltersNoVtx", &HLT_DoubleMu38NoFiltersNoVtx, &b_HLT_DoubleMu38NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_DoubleMu23NoFiltersNoVtxDisplaced", &HLT_DoubleMu23NoFiltersNoVtxDisplaced, &b_HLT_DoubleMu23NoFiltersNoVtxDisplaced);
   fChain->SetBranchAddress("HLT_DoubleMu28NoFiltersNoVtxDisplaced", &HLT_DoubleMu28NoFiltersNoVtxDisplaced, &b_HLT_DoubleMu28NoFiltersNoVtxDisplaced);
   fChain->SetBranchAddress("HLT_DoubleMu0", &HLT_DoubleMu0, &b_HLT_DoubleMu0);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_Bs", &HLT_DoubleMu4_3_Bs, &b_HLT_DoubleMu4_3_Bs);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_Jpsi_Displaced", &HLT_DoubleMu4_3_Jpsi_Displaced, &b_HLT_DoubleMu4_3_Jpsi_Displaced);
   fChain->SetBranchAddress("HLT_DoubleMu4_JpsiTrk_Displaced", &HLT_DoubleMu4_JpsiTrk_Displaced, &b_HLT_DoubleMu4_JpsiTrk_Displaced);
   fChain->SetBranchAddress("HLT_DoubleMu4_LowMassNonResonantTrk_Displaced", &HLT_DoubleMu4_LowMassNonResonantTrk_Displaced, &b_HLT_DoubleMu4_LowMassNonResonantTrk_Displaced);
   fChain->SetBranchAddress("HLT_DoubleMu3_Trk_Tau3mu", &HLT_DoubleMu3_Trk_Tau3mu, &b_HLT_DoubleMu3_Trk_Tau3mu);
   fChain->SetBranchAddress("HLT_DoubleMu4_PsiPrimeTrk_Displaced", &HLT_DoubleMu4_PsiPrimeTrk_Displaced, &b_HLT_DoubleMu4_PsiPrimeTrk_Displaced);
   fChain->SetBranchAddress("HLT_Mu7p5_L2Mu2_Jpsi", &HLT_Mu7p5_L2Mu2_Jpsi, &b_HLT_Mu7p5_L2Mu2_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_L2Mu2_Upsilon", &HLT_Mu7p5_L2Mu2_Upsilon, &b_HLT_Mu7p5_L2Mu2_Upsilon);
   fChain->SetBranchAddress("HLT_Mu7p5_Track2_Jpsi", &HLT_Mu7p5_Track2_Jpsi, &b_HLT_Mu7p5_Track2_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_Track3p5_Jpsi", &HLT_Mu7p5_Track3p5_Jpsi, &b_HLT_Mu7p5_Track3p5_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_Track7_Jpsi", &HLT_Mu7p5_Track7_Jpsi, &b_HLT_Mu7p5_Track7_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_Track2_Upsilon", &HLT_Mu7p5_Track2_Upsilon, &b_HLT_Mu7p5_Track2_Upsilon);
   fChain->SetBranchAddress("HLT_Mu7p5_Track3p5_Upsilon", &HLT_Mu7p5_Track3p5_Upsilon, &b_HLT_Mu7p5_Track3p5_Upsilon);
   fChain->SetBranchAddress("HLT_Mu7p5_Track7_Upsilon", &HLT_Mu7p5_Track7_Upsilon, &b_HLT_Mu7p5_Track7_Upsilon);
   fChain->SetBranchAddress("HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing", &HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing, &b_HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing);
   fChain->SetBranchAddress("HLT_Dimuon0er16_Jpsi_NoVertexing", &HLT_Dimuon0er16_Jpsi_NoVertexing, &b_HLT_Dimuon0er16_Jpsi_NoVertexing);
   fChain->SetBranchAddress("HLT_Dimuon6_Jpsi_NoVertexing", &HLT_Dimuon6_Jpsi_NoVertexing, &b_HLT_Dimuon6_Jpsi_NoVertexing);
   fChain->SetBranchAddress("HLT_Photon150", &HLT_Photon150, &b_HLT_Photon150);
   fChain->SetBranchAddress("HLT_Photon90_CaloIdL_HT300", &HLT_Photon90_CaloIdL_HT300, &b_HLT_Photon90_CaloIdL_HT300);
   fChain->SetBranchAddress("HLT_HT250_CaloMET70", &HLT_HT250_CaloMET70, &b_HLT_HT250_CaloMET70);
   fChain->SetBranchAddress("HLT_DoublePhoton60", &HLT_DoublePhoton60, &b_HLT_DoublePhoton60);
   fChain->SetBranchAddress("HLT_DoublePhoton85", &HLT_DoublePhoton85, &b_HLT_DoublePhoton85);
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
   fChain->SetBranchAddress("HLT_HT200", &HLT_HT200, &b_HLT_HT200);
   fChain->SetBranchAddress("HLT_HT275", &HLT_HT275, &b_HLT_HT275);
   fChain->SetBranchAddress("HLT_HT325", &HLT_HT325, &b_HLT_HT325);
   fChain->SetBranchAddress("HLT_HT425", &HLT_HT425, &b_HLT_HT425);
   fChain->SetBranchAddress("HLT_HT575", &HLT_HT575, &b_HLT_HT575);
   fChain->SetBranchAddress("HLT_HT410to430", &HLT_HT410to430, &b_HLT_HT410to430);
   fChain->SetBranchAddress("HLT_HT430to450", &HLT_HT430to450, &b_HLT_HT430to450);
   fChain->SetBranchAddress("HLT_HT450to470", &HLT_HT450to470, &b_HLT_HT450to470);
   fChain->SetBranchAddress("HLT_HT470to500", &HLT_HT470to500, &b_HLT_HT470to500);
   fChain->SetBranchAddress("HLT_HT500to550", &HLT_HT500to550, &b_HLT_HT500to550);
   fChain->SetBranchAddress("HLT_HT550to650", &HLT_HT550to650, &b_HLT_HT550to650);
   fChain->SetBranchAddress("HLT_HT650", &HLT_HT650, &b_HLT_HT650);
   fChain->SetBranchAddress("HLT_Mu16_eta2p1_MET30", &HLT_Mu16_eta2p1_MET30, &b_HLT_Mu16_eta2p1_MET30);
   fChain->SetBranchAddress("HLT_IsoMu16_eta2p1_MET30", &HLT_IsoMu16_eta2p1_MET30, &b_HLT_IsoMu16_eta2p1_MET30);
   fChain->SetBranchAddress("HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1", &HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1, &b_HLT_IsoMu16_eta2p1_MET30_LooseIsoPFTau50_Trk30_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu17_eta2p1", &HLT_IsoMu17_eta2p1, &b_HLT_IsoMu17_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu17_eta2p1_LooseIsoPFTau20", &HLT_IsoMu17_eta2p1_LooseIsoPFTau20, &b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20);
   fChain->SetBranchAddress("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1", &HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1, &b_HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1);
   fChain->SetBranchAddress("HLT_DoubleIsoMu17_eta2p1", &HLT_DoubleIsoMu17_eta2p1, &b_HLT_DoubleIsoMu17_eta2p1);
   fChain->SetBranchAddress("HLT_DoubleIsoMu17_eta2p1_noDzCut", &HLT_DoubleIsoMu17_eta2p1_noDzCut, &b_HLT_DoubleIsoMu17_eta2p1_noDzCut);
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
   fChain->SetBranchAddress("HLT_L1SingleMu18", &HLT_L1SingleMu18, &b_HLT_L1SingleMu18);
   fChain->SetBranchAddress("HLT_L2Mu10", &HLT_L2Mu10, &b_HLT_L2Mu10);
   fChain->SetBranchAddress("HLT_L1SingleMuOpen", &HLT_L1SingleMuOpen, &b_HLT_L1SingleMuOpen);
   fChain->SetBranchAddress("HLT_L1SingleMuOpen_DT", &HLT_L1SingleMuOpen_DT, &b_HLT_L1SingleMuOpen_DT);
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
   fChain->SetBranchAddress("HLT_PFTau120_eta2p1", &HLT_PFTau120_eta2p1, &b_HLT_PFTau120_eta2p1);
   fChain->SetBranchAddress("HLT_PFTau140_eta2p1", &HLT_PFTau140_eta2p1, &b_HLT_PFTau140_eta2p1);
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
   fChain->SetBranchAddress("HLT_DoubleMu18NoFiltersNoVtx", &HLT_DoubleMu18NoFiltersNoVtx, &b_HLT_DoubleMu18NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight", &HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight, &b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight);
   fChain->SetBranchAddress("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose", &HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose, &b_HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose);
   fChain->SetBranchAddress("HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose", &HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose, &b_HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight", &HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight, &b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose", &HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose, &b_HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose", &HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose, &b_HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose);
   fChain->SetBranchAddress("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40", &HLT_Mu28NoFiltersNoVtx_CentralCaloJet40, &b_HLT_Mu28NoFiltersNoVtx_CentralCaloJet40);
   fChain->SetBranchAddress("HLT_PFHT300_PFMET100", &HLT_PFHT300_PFMET100, &b_HLT_PFHT300_PFMET100);
   fChain->SetBranchAddress("HLT_PFHT300_PFMET110", &HLT_PFHT300_PFMET110, &b_HLT_PFHT300_PFMET110);
   fChain->SetBranchAddress("HLT_PFHT550_4JetPt50", &HLT_PFHT550_4JetPt50, &b_HLT_PFHT550_4JetPt50);
   fChain->SetBranchAddress("HLT_PFHT650_4JetPt50", &HLT_PFHT650_4JetPt50, &b_HLT_PFHT650_4JetPt50);
   fChain->SetBranchAddress("HLT_PFHT750_4JetPt50", &HLT_PFHT750_4JetPt50, &b_HLT_PFHT750_4JetPt50);
   fChain->SetBranchAddress("HLT_PFHT750_4JetPt70", &HLT_PFHT750_4JetPt70, &b_HLT_PFHT750_4JetPt70);
   fChain->SetBranchAddress("HLT_PFHT750_4JetPt80", &HLT_PFHT750_4JetPt80, &b_HLT_PFHT750_4JetPt80);
   fChain->SetBranchAddress("HLT_PFHT800_4JetPt50", &HLT_PFHT800_4JetPt50, &b_HLT_PFHT800_4JetPt50);
   fChain->SetBranchAddress("HLT_PFHT850_4JetPt50", &HLT_PFHT850_4JetPt50, &b_HLT_PFHT850_4JetPt50);
   fChain->SetBranchAddress("HLT_PFJet15_NoCaloMatched", &HLT_PFJet15_NoCaloMatched, &b_HLT_PFJet15_NoCaloMatched);
   fChain->SetBranchAddress("HLT_PFJet25_NoCaloMatched", &HLT_PFJet25_NoCaloMatched, &b_HLT_PFJet25_NoCaloMatched);
   fChain->SetBranchAddress("HLT_DiPFJet15_NoCaloMatched", &HLT_DiPFJet15_NoCaloMatched, &b_HLT_DiPFJet15_NoCaloMatched);
   fChain->SetBranchAddress("HLT_DiPFJet25_NoCaloMatched", &HLT_DiPFJet25_NoCaloMatched, &b_HLT_DiPFJet25_NoCaloMatched);
   fChain->SetBranchAddress("HLT_DiPFJet15_FBEta3_NoCaloMatched", &HLT_DiPFJet15_FBEta3_NoCaloMatched, &b_HLT_DiPFJet15_FBEta3_NoCaloMatched);
   fChain->SetBranchAddress("HLT_DiPFJet25_FBEta3_NoCaloMatched", &HLT_DiPFJet25_FBEta3_NoCaloMatched, &b_HLT_DiPFJet25_FBEta3_NoCaloMatched);
   fChain->SetBranchAddress("HLT_DiPFJetAve15_HFJEC", &HLT_DiPFJetAve15_HFJEC, &b_HLT_DiPFJetAve15_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve25_HFJEC", &HLT_DiPFJetAve25_HFJEC, &b_HLT_DiPFJetAve25_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve35_HFJEC", &HLT_DiPFJetAve35_HFJEC, &b_HLT_DiPFJetAve35_HFJEC);
   fChain->SetBranchAddress("HLT_AK8PFJet40", &HLT_AK8PFJet40, &b_HLT_AK8PFJet40);
   fChain->SetBranchAddress("HLT_AK8PFJet60", &HLT_AK8PFJet60, &b_HLT_AK8PFJet60);
   fChain->SetBranchAddress("HLT_AK8PFJet80", &HLT_AK8PFJet80, &b_HLT_AK8PFJet80);
   fChain->SetBranchAddress("HLT_AK8PFJet140", &HLT_AK8PFJet140, &b_HLT_AK8PFJet140);
   fChain->SetBranchAddress("HLT_AK8PFJet200", &HLT_AK8PFJet200, &b_HLT_AK8PFJet200);
   fChain->SetBranchAddress("HLT_AK8PFJet260", &HLT_AK8PFJet260, &b_HLT_AK8PFJet260);
   fChain->SetBranchAddress("HLT_AK8PFJet320", &HLT_AK8PFJet320, &b_HLT_AK8PFJet320);
   fChain->SetBranchAddress("HLT_AK8PFJet400", &HLT_AK8PFJet400, &b_HLT_AK8PFJet400);
   fChain->SetBranchAddress("HLT_AK8PFJet450", &HLT_AK8PFJet450, &b_HLT_AK8PFJet450);
   fChain->SetBranchAddress("HLT_AK8PFJet500", &HLT_AK8PFJet500, &b_HLT_AK8PFJet500);
   fChain->SetBranchAddress("HLT_PFJet40", &HLT_PFJet40, &b_HLT_PFJet40);
   fChain->SetBranchAddress("HLT_PFJet60", &HLT_PFJet60, &b_HLT_PFJet60);
   fChain->SetBranchAddress("HLT_PFJet80", &HLT_PFJet80, &b_HLT_PFJet80);
   fChain->SetBranchAddress("HLT_PFJet140", &HLT_PFJet140, &b_HLT_PFJet140);
   fChain->SetBranchAddress("HLT_PFJet200", &HLT_PFJet200, &b_HLT_PFJet200);
   fChain->SetBranchAddress("HLT_PFJet260", &HLT_PFJet260, &b_HLT_PFJet260);
   fChain->SetBranchAddress("HLT_PFJet320", &HLT_PFJet320, &b_HLT_PFJet320);
   fChain->SetBranchAddress("HLT_PFJet400", &HLT_PFJet400, &b_HLT_PFJet400);
   fChain->SetBranchAddress("HLT_PFJet450", &HLT_PFJet450, &b_HLT_PFJet450);
   fChain->SetBranchAddress("HLT_PFJet500", &HLT_PFJet500, &b_HLT_PFJet500);
   fChain->SetBranchAddress("HLT_DiPFJetAve40", &HLT_DiPFJetAve40, &b_HLT_DiPFJetAve40);
   fChain->SetBranchAddress("HLT_DiPFJetAve60", &HLT_DiPFJetAve60, &b_HLT_DiPFJetAve60);
   fChain->SetBranchAddress("HLT_DiPFJetAve80", &HLT_DiPFJetAve80, &b_HLT_DiPFJetAve80);
   fChain->SetBranchAddress("HLT_DiPFJetAve140", &HLT_DiPFJetAve140, &b_HLT_DiPFJetAve140);
   fChain->SetBranchAddress("HLT_DiPFJetAve200", &HLT_DiPFJetAve200, &b_HLT_DiPFJetAve200);
   fChain->SetBranchAddress("HLT_DiPFJetAve260", &HLT_DiPFJetAve260, &b_HLT_DiPFJetAve260);
   fChain->SetBranchAddress("HLT_DiPFJetAve320", &HLT_DiPFJetAve320, &b_HLT_DiPFJetAve320);
   fChain->SetBranchAddress("HLT_DiPFJetAve400", &HLT_DiPFJetAve400, &b_HLT_DiPFJetAve400);
   fChain->SetBranchAddress("HLT_DiPFJetAve500", &HLT_DiPFJetAve500, &b_HLT_DiPFJetAve500);
   fChain->SetBranchAddress("HLT_DiPFJetAve60_HFJEC", &HLT_DiPFJetAve60_HFJEC, &b_HLT_DiPFJetAve60_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve80_HFJEC", &HLT_DiPFJetAve80_HFJEC, &b_HLT_DiPFJetAve80_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve100_HFJEC", &HLT_DiPFJetAve100_HFJEC, &b_HLT_DiPFJetAve100_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve160_HFJEC", &HLT_DiPFJetAve160_HFJEC, &b_HLT_DiPFJetAve160_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve220_HFJEC", &HLT_DiPFJetAve220_HFJEC, &b_HLT_DiPFJetAve220_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve300_HFJEC", &HLT_DiPFJetAve300_HFJEC, &b_HLT_DiPFJetAve300_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140", &HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140, &b_HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140);
   fChain->SetBranchAddress("HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80", &HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80, &b_HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80);
   fChain->SetBranchAddress("HLT_DiCentralPFJet170", &HLT_DiCentralPFJet170, &b_HLT_DiCentralPFJet170);
   fChain->SetBranchAddress("HLT_SingleCentralPFJet170_CFMax0p1", &HLT_SingleCentralPFJet170_CFMax0p1, &b_HLT_SingleCentralPFJet170_CFMax0p1);
   fChain->SetBranchAddress("HLT_DiCentralPFJet170_CFMax0p1", &HLT_DiCentralPFJet170_CFMax0p1, &b_HLT_DiCentralPFJet170_CFMax0p1);
   fChain->SetBranchAddress("HLT_DiCentralPFJet220_CFMax0p3", &HLT_DiCentralPFJet220_CFMax0p3, &b_HLT_DiCentralPFJet220_CFMax0p3);
   fChain->SetBranchAddress("HLT_DiCentralPFJet330_CFMax0p5", &HLT_DiCentralPFJet330_CFMax0p5, &b_HLT_DiCentralPFJet330_CFMax0p5);
   fChain->SetBranchAddress("HLT_DiCentralPFJet430", &HLT_DiCentralPFJet430, &b_HLT_DiCentralPFJet430);
   fChain->SetBranchAddress("HLT_PFHT125", &HLT_PFHT125, &b_HLT_PFHT125);
   fChain->SetBranchAddress("HLT_PFHT200", &HLT_PFHT200, &b_HLT_PFHT200);
   fChain->SetBranchAddress("HLT_PFHT250", &HLT_PFHT250, &b_HLT_PFHT250);
   fChain->SetBranchAddress("HLT_PFHT300", &HLT_PFHT300, &b_HLT_PFHT300);
   fChain->SetBranchAddress("HLT_PFHT350", &HLT_PFHT350, &b_HLT_PFHT350);
   fChain->SetBranchAddress("HLT_PFHT400", &HLT_PFHT400, &b_HLT_PFHT400);
   fChain->SetBranchAddress("HLT_PFHT475", &HLT_PFHT475, &b_HLT_PFHT475);
   fChain->SetBranchAddress("HLT_PFHT600", &HLT_PFHT600, &b_HLT_PFHT600);
   fChain->SetBranchAddress("HLT_PFHT650", &HLT_PFHT650, &b_HLT_PFHT650);
   fChain->SetBranchAddress("HLT_PFHT800", &HLT_PFHT800, &b_HLT_PFHT800);
   fChain->SetBranchAddress("HLT_PFHT900", &HLT_PFHT900, &b_HLT_PFHT900);
   fChain->SetBranchAddress("HLT_PFHT200_PFAlphaT0p51", &HLT_PFHT200_PFAlphaT0p51, &b_HLT_PFHT200_PFAlphaT0p51);
   fChain->SetBranchAddress("HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57", &HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57, &b_HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57);
   fChain->SetBranchAddress("HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63", &HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63, &b_HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63);
   fChain->SetBranchAddress("HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55", &HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55, &b_HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55);
   fChain->SetBranchAddress("HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58", &HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58, &b_HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58);
   fChain->SetBranchAddress("HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53", &HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53, &b_HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53);
   fChain->SetBranchAddress("HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54", &HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54, &b_HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54);
   fChain->SetBranchAddress("HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52", &HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52, &b_HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52);
   fChain->SetBranchAddress("HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53", &HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53, &b_HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53);
   fChain->SetBranchAddress("HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51", &HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51, &b_HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51);
   fChain->SetBranchAddress("HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52", &HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52, &b_HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52);
   fChain->SetBranchAddress("HLT_MET60_IsoTrk35_Loose", &HLT_MET60_IsoTrk35_Loose, &b_HLT_MET60_IsoTrk35_Loose);
   fChain->SetBranchAddress("HLT_MET75_IsoTrk50", &HLT_MET75_IsoTrk50, &b_HLT_MET75_IsoTrk50);
   fChain->SetBranchAddress("HLT_MET90_IsoTrk50", &HLT_MET90_IsoTrk50, &b_HLT_MET90_IsoTrk50);
   fChain->SetBranchAddress("HLT_PFMET120_BTagCSV_p067", &HLT_PFMET120_BTagCSV_p067, &b_HLT_PFMET120_BTagCSV_p067);
   fChain->SetBranchAddress("HLT_PFMET120_Mu5", &HLT_PFMET120_Mu5, &b_HLT_PFMET120_Mu5);
   fChain->SetBranchAddress("HLT_PFMET170_NotCleaned", &HLT_PFMET170_NotCleaned, &b_HLT_PFMET170_NotCleaned);
   fChain->SetBranchAddress("HLT_PFMET170_NoiseCleaned", &HLT_PFMET170_NoiseCleaned, &b_HLT_PFMET170_NoiseCleaned);
   fChain->SetBranchAddress("HLT_PFMET170_HBHECleaned", &HLT_PFMET170_HBHECleaned, &b_HLT_PFMET170_HBHECleaned);
   fChain->SetBranchAddress("HLT_PFMET170_JetIdCleaned", &HLT_PFMET170_JetIdCleaned, &b_HLT_PFMET170_JetIdCleaned);
   fChain->SetBranchAddress("HLT_PFMET170_BeamHaloCleaned", &HLT_PFMET170_BeamHaloCleaned, &b_HLT_PFMET170_BeamHaloCleaned);
   fChain->SetBranchAddress("HLT_PFMET170_HBHE_BeamHaloCleaned", &HLT_PFMET170_HBHE_BeamHaloCleaned, &b_HLT_PFMET170_HBHE_BeamHaloCleaned);
   fChain->SetBranchAddress("HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned", &HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned, &b_HLT_PFMETTypeOne190_HBHE_BeamHaloCleaned);
   fChain->SetBranchAddress("HLT_PFMET90_PFMHT90_IDTight", &HLT_PFMET90_PFMHT90_IDTight, &b_HLT_PFMET90_PFMHT90_IDTight);
   fChain->SetBranchAddress("HLT_PFMET100_PFMHT100_IDTight", &HLT_PFMET100_PFMHT100_IDTight, &b_HLT_PFMET100_PFMHT100_IDTight);
   fChain->SetBranchAddress("HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned", &HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned, &b_HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned);
   fChain->SetBranchAddress("HLT_PFMET110_PFMHT110_IDTight", &HLT_PFMET110_PFMHT110_IDTight, &b_HLT_PFMET110_PFMHT110_IDTight);
   fChain->SetBranchAddress("HLT_PFMET120_PFMHT120_IDTight", &HLT_PFMET120_PFMHT120_IDTight, &b_HLT_PFMET120_PFMHT120_IDTight);
   fChain->SetBranchAddress("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067", &HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067, &b_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067);
   fChain->SetBranchAddress("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight", &HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight, &b_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight);
   fChain->SetBranchAddress("HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200", &HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200, &b_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200);
   fChain->SetBranchAddress("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460", &HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460, &b_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460);
   fChain->SetBranchAddress("HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240", &HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240, &b_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240);
   fChain->SetBranchAddress("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500", &HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500, &b_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500);
   fChain->SetBranchAddress("HLT_QuadPFJet_VBF", &HLT_QuadPFJet_VBF, &b_HLT_QuadPFJet_VBF);
   fChain->SetBranchAddress("HLT_L1_TripleJet_VBF", &HLT_L1_TripleJet_VBF, &b_HLT_L1_TripleJet_VBF);
   fChain->SetBranchAddress("HLT_QuadJet45_TripleBTagCSV_p087", &HLT_QuadJet45_TripleBTagCSV_p087, &b_HLT_QuadJet45_TripleBTagCSV_p087);
   fChain->SetBranchAddress("HLT_QuadJet45_DoubleBTagCSV_p087", &HLT_QuadJet45_DoubleBTagCSV_p087, &b_HLT_QuadJet45_DoubleBTagCSV_p087);
   fChain->SetBranchAddress("HLT_DoubleJet90_Double30_TripleBTagCSV_p087", &HLT_DoubleJet90_Double30_TripleBTagCSV_p087, &b_HLT_DoubleJet90_Double30_TripleBTagCSV_p087);
   fChain->SetBranchAddress("HLT_DoubleJet90_Double30_DoubleBTagCSV_p087", &HLT_DoubleJet90_Double30_DoubleBTagCSV_p087, &b_HLT_DoubleJet90_Double30_DoubleBTagCSV_p087);
   fChain->SetBranchAddress("HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160", &HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160, &b_HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160);
   fChain->SetBranchAddress("HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6", &HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6, &b_HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6);
   fChain->SetBranchAddress("HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172", &HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172, &b_HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172);
   fChain->SetBranchAddress("HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6", &HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6, &b_HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6);
   fChain->SetBranchAddress("HLT_DoubleJetsC100_SingleBTagCSV_p026", &HLT_DoubleJetsC100_SingleBTagCSV_p026, &b_HLT_DoubleJetsC100_SingleBTagCSV_p026);
   fChain->SetBranchAddress("HLT_DoubleJetsC100_SingleBTagCSV_p014", &HLT_DoubleJetsC100_SingleBTagCSV_p014, &b_HLT_DoubleJetsC100_SingleBTagCSV_p014);
   fChain->SetBranchAddress("HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350", &HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350, &b_HLT_DoubleJetsC100_SingleBTagCSV_p026_SinglePFJetC350);
   fChain->SetBranchAddress("HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350", &HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350, &b_HLT_DoubleJetsC100_SingleBTagCSV_p014_SinglePFJetC350);
   fChain->SetBranchAddress("HLT_Photon135_PFMET100", &HLT_Photon135_PFMET100, &b_HLT_Photon135_PFMET100);
   fChain->SetBranchAddress("HLT_Photon20_CaloIdVL_IsoL", &HLT_Photon20_CaloIdVL_IsoL, &b_HLT_Photon20_CaloIdVL_IsoL);
   fChain->SetBranchAddress("HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40", &HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40, &b_HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40);
   fChain->SetBranchAddress("HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF", &HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF, &b_HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF);
   fChain->SetBranchAddress("HLT_Photon250_NoHE", &HLT_Photon250_NoHE, &b_HLT_Photon250_NoHE);
   fChain->SetBranchAddress("HLT_Photon300_NoHE", &HLT_Photon300_NoHE, &b_HLT_Photon300_NoHE);
   fChain->SetBranchAddress("HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60", &HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60, &b_HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60);
   fChain->SetBranchAddress("HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15", &HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15, &b_HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15);
   fChain->SetBranchAddress("HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40", &HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40, &b_HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40);
   fChain->SetBranchAddress("HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF", &HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF, &b_HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF);
   fChain->SetBranchAddress("HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40", &HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40, &b_HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40);
   fChain->SetBranchAddress("HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF", &HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF, &b_HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF);
   fChain->SetBranchAddress("HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40", &HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40, &b_HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40);
   fChain->SetBranchAddress("HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF", &HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF, &b_HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF);
   fChain->SetBranchAddress("HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40", &HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40, &b_HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40);
   fChain->SetBranchAddress("HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF", &HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF, &b_HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF);
   fChain->SetBranchAddress("HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40", &HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40, &b_HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40);
   fChain->SetBranchAddress("HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF", &HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF, &b_HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL", &HLT_Mu8_TrkIsoVVL, &b_HLT_Mu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL", &HLT_Mu17_TrkIsoVVL, &b_HLT_Mu17_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_BTagMu_DiJet20_Mu5", &HLT_BTagMu_DiJet20_Mu5, &b_HLT_BTagMu_DiJet20_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_DiJet40_Mu5", &HLT_BTagMu_DiJet40_Mu5, &b_HLT_BTagMu_DiJet40_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_DiJet70_Mu5", &HLT_BTagMu_DiJet70_Mu5, &b_HLT_BTagMu_DiJet70_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_DiJet110_Mu5", &HLT_BTagMu_DiJet110_Mu5, &b_HLT_BTagMu_DiJet110_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_DiJet170_Mu5", &HLT_BTagMu_DiJet170_Mu5, &b_HLT_BTagMu_DiJet170_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_Jet300_Mu5", &HLT_BTagMu_Jet300_Mu5, &b_HLT_BTagMu_Jet300_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK8Jet300_Mu5", &HLT_BTagMu_AK8Jet300_Mu5, &b_HLT_BTagMu_AK8Jet300_Mu5);
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
   fChain->SetBranchAddress("HLT_DiMu9_Ele9_CaloIdL_TrackIdL", &HLT_DiMu9_Ele9_CaloIdL_TrackIdL, &b_HLT_DiMu9_Ele9_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_TripleMu_5_3_3", &HLT_TripleMu_5_3_3, &b_HLT_TripleMu_5_3_3);
   fChain->SetBranchAddress("HLT_TripleMu_12_10_5", &HLT_TripleMu_12_10_5, &b_HLT_TripleMu_12_10_5);
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
   fChain->SetBranchAddress("HLT_PFHT650_WideJetMJJ900DEtaJJ1p5", &HLT_PFHT650_WideJetMJJ900DEtaJJ1p5, &b_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5);
   fChain->SetBranchAddress("HLT_PFHT650_WideJetMJJ950DEtaJJ1p5", &HLT_PFHT650_WideJetMJJ950DEtaJJ1p5, &b_HLT_PFHT650_WideJetMJJ950DEtaJJ1p5);
   fChain->SetBranchAddress("HLT_Photon22", &HLT_Photon22, &b_HLT_Photon22);
   fChain->SetBranchAddress("HLT_Photon30", &HLT_Photon30, &b_HLT_Photon30);
   fChain->SetBranchAddress("HLT_Photon36", &HLT_Photon36, &b_HLT_Photon36);
   fChain->SetBranchAddress("HLT_Photon50", &HLT_Photon50, &b_HLT_Photon50);
   fChain->SetBranchAddress("HLT_Photon75", &HLT_Photon75, &b_HLT_Photon75);
   fChain->SetBranchAddress("HLT_Photon90", &HLT_Photon90, &b_HLT_Photon90);
   fChain->SetBranchAddress("HLT_Photon120", &HLT_Photon120, &b_HLT_Photon120);
   fChain->SetBranchAddress("HLT_Photon175", &HLT_Photon175, &b_HLT_Photon175);
   fChain->SetBranchAddress("HLT_Photon165_HE10", &HLT_Photon165_HE10, &b_HLT_Photon165_HE10);
   fChain->SetBranchAddress("HLT_Photon22_R9Id90_HE10_IsoM", &HLT_Photon22_R9Id90_HE10_IsoM, &b_HLT_Photon22_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon30_R9Id90_HE10_IsoM", &HLT_Photon30_R9Id90_HE10_IsoM, &b_HLT_Photon30_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon36_R9Id90_HE10_IsoM", &HLT_Photon36_R9Id90_HE10_IsoM, &b_HLT_Photon36_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon50_R9Id90_HE10_IsoM", &HLT_Photon50_R9Id90_HE10_IsoM, &b_HLT_Photon50_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon75_R9Id90_HE10_IsoM", &HLT_Photon75_R9Id90_HE10_IsoM, &b_HLT_Photon75_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon90_R9Id90_HE10_IsoM", &HLT_Photon90_R9Id90_HE10_IsoM, &b_HLT_Photon90_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon120_R9Id90_HE10_IsoM", &HLT_Photon120_R9Id90_HE10_IsoM, &b_HLT_Photon120_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon165_R9Id90_HE10_IsoM", &HLT_Photon165_R9Id90_HE10_IsoM, &b_HLT_Photon165_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90", &HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90, &b_HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90);
   fChain->SetBranchAddress("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70", &HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70, &b_HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70);
   fChain->SetBranchAddress("HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55", &HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55, &b_HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55);
   fChain->SetBranchAddress("HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55", &HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55, &b_HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55);
   fChain->SetBranchAddress("HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55", &HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55, &b_HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi_Muon", &HLT_Dimuon0_Jpsi_Muon, &b_HLT_Dimuon0_Jpsi_Muon);
   fChain->SetBranchAddress("HLT_Dimuon0_Upsilon_Muon", &HLT_Dimuon0_Upsilon_Muon, &b_HLT_Dimuon0_Upsilon_Muon);
   fChain->SetBranchAddress("HLT_QuadMuon0_Dimuon0_Jpsi", &HLT_QuadMuon0_Dimuon0_Jpsi, &b_HLT_QuadMuon0_Dimuon0_Jpsi);
   fChain->SetBranchAddress("HLT_QuadMuon0_Dimuon0_Upsilon", &HLT_QuadMuon0_Dimuon0_Upsilon, &b_HLT_QuadMuon0_Dimuon0_Upsilon);
   fChain->SetBranchAddress("HLT_Rsq0p25_Calo", &HLT_Rsq0p25_Calo, &b_HLT_Rsq0p25_Calo);
   fChain->SetBranchAddress("HLT_RsqMR240_Rsq0p09_MR200_4jet_Calo", &HLT_RsqMR240_Rsq0p09_MR200_4jet_Calo, &b_HLT_RsqMR240_Rsq0p09_MR200_4jet_Calo);
   fChain->SetBranchAddress("HLT_RsqMR240_Rsq0p09_MR200_Calo", &HLT_RsqMR240_Rsq0p09_MR200_Calo, &b_HLT_RsqMR240_Rsq0p09_MR200_Calo);
   fChain->SetBranchAddress("HLT_Rsq0p25", &HLT_Rsq0p25, &b_HLT_Rsq0p25);
   fChain->SetBranchAddress("HLT_Rsq0p30", &HLT_Rsq0p30, &b_HLT_Rsq0p30);
   fChain->SetBranchAddress("HLT_RsqMR240_Rsq0p09_MR200", &HLT_RsqMR240_Rsq0p09_MR200, &b_HLT_RsqMR240_Rsq0p09_MR200);
   fChain->SetBranchAddress("HLT_RsqMR240_Rsq0p09_MR200_4jet", &HLT_RsqMR240_Rsq0p09_MR200_4jet, &b_HLT_RsqMR240_Rsq0p09_MR200_4jet);
   fChain->SetBranchAddress("HLT_RsqMR270_Rsq0p09_MR200", &HLT_RsqMR270_Rsq0p09_MR200, &b_HLT_RsqMR270_Rsq0p09_MR200);
   fChain->SetBranchAddress("HLT_RsqMR270_Rsq0p09_MR200_4jet", &HLT_RsqMR270_Rsq0p09_MR200_4jet, &b_HLT_RsqMR270_Rsq0p09_MR200_4jet);
   fChain->SetBranchAddress("HLT_Rsq0p02_MR300_TriPFJet80_60_40_BTagCSV_p063_p20_Mbb60_200", &HLT_Rsq0p02_MR300_TriPFJet80_60_40_BTagCSV_p063_p20_Mbb60_200, &b_HLT_Rsq0p02_MR300_TriPFJet80_60_40_BTagCSV_p063_p20_Mbb60_200);
   fChain->SetBranchAddress("HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200", &HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200, &b_HLT_Rsq0p02_MR400_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200);
   fChain->SetBranchAddress("HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200", &HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200, &b_HLT_Rsq0p02_MR450_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200);
   fChain->SetBranchAddress("HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200", &HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200, &b_HLT_Rsq0p02_MR500_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200);
   fChain->SetBranchAddress("HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200", &HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200, &b_HLT_Rsq0p02_MR550_TriPFJet80_60_40_DoubleBTagCSV_p063_Mbb60_200);
   fChain->SetBranchAddress("HLT_HT200_DisplacedDijet40_DisplacedTrack", &HLT_HT200_DisplacedDijet40_DisplacedTrack, &b_HLT_HT200_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT250_DisplacedDijet40_DisplacedTrack", &HLT_HT250_DisplacedDijet40_DisplacedTrack, &b_HLT_HT250_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT350_DisplacedDijet40_DisplacedTrack", &HLT_HT350_DisplacedDijet40_DisplacedTrack, &b_HLT_HT350_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT350_DisplacedDijet80_DisplacedTrack", &HLT_HT350_DisplacedDijet80_DisplacedTrack, &b_HLT_HT350_DisplacedDijet80_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack", &HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack, &b_HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT350_DisplacedDijet40_Inclusive", &HLT_HT350_DisplacedDijet40_Inclusive, &b_HLT_HT350_DisplacedDijet40_Inclusive);
   fChain->SetBranchAddress("HLT_HT400_DisplacedDijet40_Inclusive", &HLT_HT400_DisplacedDijet40_Inclusive, &b_HLT_HT400_DisplacedDijet40_Inclusive);
   fChain->SetBranchAddress("HLT_HT500_DisplacedDijet40_Inclusive", &HLT_HT500_DisplacedDijet40_Inclusive, &b_HLT_HT500_DisplacedDijet40_Inclusive);
   fChain->SetBranchAddress("HLT_HT550_DisplacedDijet40_Inclusive", &HLT_HT550_DisplacedDijet40_Inclusive, &b_HLT_HT550_DisplacedDijet40_Inclusive);
   fChain->SetBranchAddress("HLT_HT550_DisplacedDijet80_Inclusive", &HLT_HT550_DisplacedDijet80_Inclusive, &b_HLT_HT550_DisplacedDijet80_Inclusive);
   fChain->SetBranchAddress("HLT_HT650_DisplacedDijet80_Inclusive", &HLT_HT650_DisplacedDijet80_Inclusive, &b_HLT_HT650_DisplacedDijet80_Inclusive);
   fChain->SetBranchAddress("HLT_HT750_DisplacedDijet80_Inclusive", &HLT_HT750_DisplacedDijet80_Inclusive, &b_HLT_HT750_DisplacedDijet80_Inclusive);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_DisplacedTrack", &HLT_VBF_DisplacedJet40_DisplacedTrack, &b_HLT_VBF_DisplacedJet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5", &HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5, &b_HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_TightID_DisplacedTrack", &HLT_VBF_DisplacedJet40_TightID_DisplacedTrack, &b_HLT_VBF_DisplacedJet40_TightID_DisplacedTrack);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_Hadronic", &HLT_VBF_DisplacedJet40_Hadronic, &b_HLT_VBF_DisplacedJet40_Hadronic);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack", &HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack, &b_HLT_VBF_DisplacedJet40_Hadronic_2PromptTrack);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_TightID_Hadronic", &HLT_VBF_DisplacedJet40_TightID_Hadronic, &b_HLT_VBF_DisplacedJet40_TightID_Hadronic);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_VTightID_Hadronic", &HLT_VBF_DisplacedJet40_VTightID_Hadronic, &b_HLT_VBF_DisplacedJet40_VTightID_Hadronic);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_VVTightID_Hadronic", &HLT_VBF_DisplacedJet40_VVTightID_Hadronic, &b_HLT_VBF_DisplacedJet40_VVTightID_Hadronic);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack", &HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack, &b_HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack);
   fChain->SetBranchAddress("HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack", &HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack, &b_HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack);
   fChain->SetBranchAddress("HLT_PFMETNoMu90_PFMHTNoMu90_IDTight", &HLT_PFMETNoMu90_PFMHTNoMu90_IDTight, &b_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu100_PFMHTNoMu100_IDTight", &HLT_PFMETNoMu100_PFMHTNoMu100_IDTight, &b_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu110_PFMHTNoMu110_IDTight", &HLT_PFMETNoMu110_PFMHTNoMu110_IDTight, &b_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight, &b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight);
   fChain->SetBranchAddress("HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight", &HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight, &b_HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight);
   fChain->SetBranchAddress("HLT_MonoCentralPFJet80_PFMETNoMu100_PFMHTNoMu100_IDTight", &HLT_MonoCentralPFJet80_PFMETNoMu100_PFMHTNoMu100_IDTight, &b_HLT_MonoCentralPFJet80_PFMETNoMu100_PFMHTNoMu100_IDTight);
   fChain->SetBranchAddress("HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight", &HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight, &b_HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight);
   fChain->SetBranchAddress("HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight", &HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight, &b_HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight);
   fChain->SetBranchAddress("HLT_Ele27_eta2p1_WPLoose_Gsf_HT200", &HLT_Ele27_eta2p1_WPLoose_Gsf_HT200, &b_HLT_Ele27_eta2p1_WPLoose_Gsf_HT200);
   fChain->SetBranchAddress("HLT_Photon90_CaloIdL_PFHT500", &HLT_Photon90_CaloIdL_PFHT500, &b_HLT_Photon90_CaloIdL_PFHT500);
   fChain->SetBranchAddress("HLT_DoubleMu8_Mass8_PFHT250", &HLT_DoubleMu8_Mass8_PFHT250, &b_HLT_DoubleMu8_Mass8_PFHT250);
   fChain->SetBranchAddress("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250", &HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250, &b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT250);
   fChain->SetBranchAddress("HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250", &HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250, &b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250);
   fChain->SetBranchAddress("HLT_DoubleMu8_Mass8_PFHT300", &HLT_DoubleMu8_Mass8_PFHT300, &b_HLT_DoubleMu8_Mass8_PFHT300);
   fChain->SetBranchAddress("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300", &HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300, &b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300);
   fChain->SetBranchAddress("HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300", &HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300, &b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300);
   fChain->SetBranchAddress("HLT_Mu10_CentralPFJet30_BTagCSV_p13", &HLT_Mu10_CentralPFJet30_BTagCSV_p13, &b_HLT_Mu10_CentralPFJet30_BTagCSV_p13);
   fChain->SetBranchAddress("HLT_DoubleMu3_PFMET50", &HLT_DoubleMu3_PFMET50, &b_HLT_DoubleMu3_PFMET50);
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
   fChain->SetBranchAddress("HLT_Dimuon16_Jpsi", &HLT_Dimuon16_Jpsi, &b_HLT_Dimuon16_Jpsi);
   fChain->SetBranchAddress("HLT_Dimuon10_Jpsi_Barrel", &HLT_Dimuon10_Jpsi_Barrel, &b_HLT_Dimuon10_Jpsi_Barrel);
   fChain->SetBranchAddress("HLT_Dimuon8_PsiPrime_Barrel", &HLT_Dimuon8_PsiPrime_Barrel, &b_HLT_Dimuon8_PsiPrime_Barrel);
   fChain->SetBranchAddress("HLT_Dimuon8_Upsilon_Barrel", &HLT_Dimuon8_Upsilon_Barrel, &b_HLT_Dimuon8_Upsilon_Barrel);
   fChain->SetBranchAddress("HLT_Dimuon0_Phi_Barrel", &HLT_Dimuon0_Phi_Barrel, &b_HLT_Dimuon0_Phi_Barrel);
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
   fChain->SetBranchAddress("HLT_PFHT400_SixJet30_DoubleBTagCSV_p056", &HLT_PFHT400_SixJet30_DoubleBTagCSV_p056, &b_HLT_PFHT400_SixJet30_DoubleBTagCSV_p056);
   fChain->SetBranchAddress("HLT_PFHT450_SixJet40_BTagCSV_p056", &HLT_PFHT450_SixJet40_BTagCSV_p056, &b_HLT_PFHT450_SixJet40_BTagCSV_p056);
   fChain->SetBranchAddress("HLT_PFHT400_SixJet30", &HLT_PFHT400_SixJet30, &b_HLT_PFHT400_SixJet30);
   fChain->SetBranchAddress("HLT_PFHT450_SixJet40", &HLT_PFHT450_SixJet40, &b_HLT_PFHT450_SixJet40);
   fChain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT", &HLT_Ele115_CaloIdVT_GsfTrkIdT, &b_HLT_Ele115_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_Mu55", &HLT_Mu55, &b_HLT_Mu55);
   fChain->SetBranchAddress("HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15", &HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15, &b_HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15);
   fChain->SetBranchAddress("HLT_Photon90_CaloIdL_PFHT600", &HLT_Photon90_CaloIdL_PFHT600, &b_HLT_Photon90_CaloIdL_PFHT600);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity60ForEndOfFill", &HLT_PixelTracks_Multiplicity60ForEndOfFill, &b_HLT_PixelTracks_Multiplicity60ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity85ForEndOfFill", &HLT_PixelTracks_Multiplicity85ForEndOfFill, &b_HLT_PixelTracks_Multiplicity85ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity110ForEndOfFill", &HLT_PixelTracks_Multiplicity110ForEndOfFill, &b_HLT_PixelTracks_Multiplicity110ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity135ForEndOfFill", &HLT_PixelTracks_Multiplicity135ForEndOfFill, &b_HLT_PixelTracks_Multiplicity135ForEndOfFill);
   fChain->SetBranchAddress("HLT_PixelTracks_Multiplicity160ForEndOfFill", &HLT_PixelTracks_Multiplicity160ForEndOfFill, &b_HLT_PixelTracks_Multiplicity160ForEndOfFill);
   fChain->SetBranchAddress("HLT_FullTracks_Multiplicity80", &HLT_FullTracks_Multiplicity80, &b_HLT_FullTracks_Multiplicity80);
   fChain->SetBranchAddress("HLT_FullTracks_Multiplicity100", &HLT_FullTracks_Multiplicity100, &b_HLT_FullTracks_Multiplicity100);
   fChain->SetBranchAddress("HLT_FullTracks_Multiplicity130", &HLT_FullTracks_Multiplicity130, &b_HLT_FullTracks_Multiplicity130);
   fChain->SetBranchAddress("HLT_FullTracks_Multiplicity150", &HLT_FullTracks_Multiplicity150, &b_HLT_FullTracks_Multiplicity150);
   fChain->SetBranchAddress("HLT_ECALHT800", &HLT_ECALHT800, &b_HLT_ECALHT800);
   fChain->SetBranchAddress("HLT_DiSC30_18_EIso_AND_HE_Mass70", &HLT_DiSC30_18_EIso_AND_HE_Mass70, &b_HLT_DiSC30_18_EIso_AND_HE_Mass70);
   fChain->SetBranchAddress("HLT_Photon125", &HLT_Photon125, &b_HLT_Photon125);
   fChain->SetBranchAddress("HLT_MET100", &HLT_MET100, &b_HLT_MET100);
   fChain->SetBranchAddress("HLT_MET150", &HLT_MET150, &b_HLT_MET150);
   fChain->SetBranchAddress("HLT_MET200", &HLT_MET200, &b_HLT_MET200);
   fChain->SetBranchAddress("HLT_Ele27_HighEta_Ele20_Mass55", &HLT_Ele27_HighEta_Ele20_Mass55, &b_HLT_Ele27_HighEta_Ele20_Mass55);
   fChain->SetBranchAddress("HLT_L1FatEvents", &HLT_L1FatEvents, &b_HLT_L1FatEvents);
   fChain->SetBranchAddress("HLT_Physics", &HLT_Physics, &b_HLT_Physics);
   fChain->SetBranchAddress("HLT_L1FatEvents_part0", &HLT_L1FatEvents_part0, &b_HLT_L1FatEvents_part0);
   fChain->SetBranchAddress("HLT_L1FatEvents_part1", &HLT_L1FatEvents_part1, &b_HLT_L1FatEvents_part1);
   fChain->SetBranchAddress("HLT_L1FatEvents_part2", &HLT_L1FatEvents_part2, &b_HLT_L1FatEvents_part2);
   fChain->SetBranchAddress("HLT_L1FatEvents_part3", &HLT_L1FatEvents_part3, &b_HLT_L1FatEvents_part3);
   fChain->SetBranchAddress("HLT_Random", &HLT_Random, &b_HLT_Random);
   fChain->SetBranchAddress("HLT_ZeroBias", &HLT_ZeroBias, &b_HLT_ZeroBias);
   fChain->SetBranchAddress("HLT_AK4CaloJet30", &HLT_AK4CaloJet30, &b_HLT_AK4CaloJet30);
   fChain->SetBranchAddress("HLT_AK4CaloJet40", &HLT_AK4CaloJet40, &b_HLT_AK4CaloJet40);
   fChain->SetBranchAddress("HLT_AK4CaloJet50", &HLT_AK4CaloJet50, &b_HLT_AK4CaloJet50);
   fChain->SetBranchAddress("HLT_AK4CaloJet80", &HLT_AK4CaloJet80, &b_HLT_AK4CaloJet80);
   fChain->SetBranchAddress("HLT_AK4CaloJet100", &HLT_AK4CaloJet100, &b_HLT_AK4CaloJet100);
   fChain->SetBranchAddress("HLT_AK4PFJet30", &HLT_AK4PFJet30, &b_HLT_AK4PFJet30);
   fChain->SetBranchAddress("HLT_AK4PFJet50", &HLT_AK4PFJet50, &b_HLT_AK4PFJet50);
   fChain->SetBranchAddress("HLT_AK4PFJet80", &HLT_AK4PFJet80, &b_HLT_AK4PFJet80);
   fChain->SetBranchAddress("HLT_AK4PFJet100", &HLT_AK4PFJet100, &b_HLT_AK4PFJet100);
   fChain->SetBranchAddress("HLT_HISinglePhoton10", &HLT_HISinglePhoton10, &b_HLT_HISinglePhoton10);
   fChain->SetBranchAddress("HLT_HISinglePhoton15", &HLT_HISinglePhoton15, &b_HLT_HISinglePhoton15);
   fChain->SetBranchAddress("HLT_HISinglePhoton20", &HLT_HISinglePhoton20, &b_HLT_HISinglePhoton20);
   fChain->SetBranchAddress("HLT_HISinglePhoton40", &HLT_HISinglePhoton40, &b_HLT_HISinglePhoton40);
   fChain->SetBranchAddress("HLT_HISinglePhoton60", &HLT_HISinglePhoton60, &b_HLT_HISinglePhoton60);
   fChain->SetBranchAddress("HLT_EcalCalibration", &HLT_EcalCalibration, &b_HLT_EcalCalibration);
   fChain->SetBranchAddress("HLT_HcalCalibration", &HLT_HcalCalibration, &b_HLT_HcalCalibration);
   fChain->SetBranchAddress("HLT_GlobalRunHPDNoise", &HLT_GlobalRunHPDNoise, &b_HLT_GlobalRunHPDNoise);
   fChain->SetBranchAddress("HLT_L1BptxMinus", &HLT_L1BptxMinus, &b_HLT_L1BptxMinus);
   fChain->SetBranchAddress("HLT_L1BptxPlus", &HLT_L1BptxPlus, &b_HLT_L1BptxPlus);
   fChain->SetBranchAddress("HLT_L1NotBptxOR", &HLT_L1NotBptxOR, &b_HLT_L1NotBptxOR);
   fChain->SetBranchAddress("HLT_L1BeamGasMinus", &HLT_L1BeamGasMinus, &b_HLT_L1BeamGasMinus);
   fChain->SetBranchAddress("HLT_L1BeamGasPlus", &HLT_L1BeamGasPlus, &b_HLT_L1BeamGasPlus);
   fChain->SetBranchAddress("HLT_L1BptxXOR", &HLT_L1BptxXOR, &b_HLT_L1BptxXOR);
   fChain->SetBranchAddress("HLT_L1MinimumBiasHF_OR", &HLT_L1MinimumBiasHF_OR, &b_HLT_L1MinimumBiasHF_OR);
   fChain->SetBranchAddress("HLT_L1MinimumBiasHF_AND", &HLT_L1MinimumBiasHF_AND, &b_HLT_L1MinimumBiasHF_AND);
   fChain->SetBranchAddress("HLT_HcalNZS", &HLT_HcalNZS, &b_HLT_HcalNZS);
   fChain->SetBranchAddress("HLT_HcalPhiSym", &HLT_HcalPhiSym, &b_HLT_HcalPhiSym);
   fChain->SetBranchAddress("HLT_HcalIsolatedbunch", &HLT_HcalIsolatedbunch, &b_HLT_HcalIsolatedbunch);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstCollisionAfterAbortGap", &HLT_ZeroBias_FirstCollisionAfterAbortGap, &b_HLT_ZeroBias_FirstCollisionAfterAbortGap);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstCollisionAfterAbortGap_copy", &HLT_ZeroBias_FirstCollisionAfterAbortGap_copy, &b_HLT_ZeroBias_FirstCollisionAfterAbortGap_copy);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstCollisionAfterAbortGap_TCDS", &HLT_ZeroBias_FirstCollisionAfterAbortGap_TCDS, &b_HLT_ZeroBias_FirstCollisionAfterAbortGap_TCDS);
   fChain->SetBranchAddress("HLT_ZeroBias_IsolatedBunches", &HLT_ZeroBias_IsolatedBunches, &b_HLT_ZeroBias_IsolatedBunches);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstCollisionInTrain", &HLT_ZeroBias_FirstCollisionInTrain, &b_HLT_ZeroBias_FirstCollisionInTrain);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstBXAfterTrain", &HLT_ZeroBias_FirstBXAfterTrain, &b_HLT_ZeroBias_FirstBXAfterTrain);
   fChain->SetBranchAddress("HLT_Photon500", &HLT_Photon500, &b_HLT_Photon500);
   fChain->SetBranchAddress("HLT_Photon600", &HLT_Photon600, &b_HLT_Photon600);
   fChain->SetBranchAddress("HLT_Mu300", &HLT_Mu300, &b_HLT_Mu300);
   fChain->SetBranchAddress("HLT_Mu350", &HLT_Mu350, &b_HLT_Mu350);
   fChain->SetBranchAddress("HLT_MET250", &HLT_MET250, &b_HLT_MET250);
   fChain->SetBranchAddress("HLT_MET300", &HLT_MET300, &b_HLT_MET300);
   fChain->SetBranchAddress("HLT_MET600", &HLT_MET600, &b_HLT_MET600);
   fChain->SetBranchAddress("HLT_MET700", &HLT_MET700, &b_HLT_MET700);
   fChain->SetBranchAddress("HLT_PFMET300", &HLT_PFMET300, &b_HLT_PFMET300);
   fChain->SetBranchAddress("HLT_PFMET400", &HLT_PFMET400, &b_HLT_PFMET400);
   fChain->SetBranchAddress("HLT_PFMET500", &HLT_PFMET500, &b_HLT_PFMET500);
   fChain->SetBranchAddress("HLT_PFMET600", &HLT_PFMET600, &b_HLT_PFMET600);
   fChain->SetBranchAddress("HLT_Ele250_CaloIdVT_GsfTrkIdT", &HLT_Ele250_CaloIdVT_GsfTrkIdT, &b_HLT_Ele250_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_Ele300_CaloIdVT_GsfTrkIdT", &HLT_Ele300_CaloIdVT_GsfTrkIdT, &b_HLT_Ele300_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_HT2000", &HLT_HT2000, &b_HLT_HT2000);
   fChain->SetBranchAddress("HLT_HT2500", &HLT_HT2500, &b_HLT_HT2500);
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
   fChain->SetBranchAddress("FatJet_pt_nom", FatJet_pt_nom, &b_FatJet_pt_nom);
   fChain->SetBranchAddress("FatJet_mass_nom", FatJet_mass_nom, &b_FatJet_mass_nom);
   fChain->SetBranchAddress("FatJet_pt_jerUp", FatJet_pt_jerUp, &b_FatJet_pt_jerUp);
   fChain->SetBranchAddress("FatJet_mass_jerUp", FatJet_mass_jerUp, &b_FatJet_mass_jerUp);
   fChain->SetBranchAddress("FatJet_mass_jmrUp", FatJet_mass_jmrUp, &b_FatJet_mass_jmrUp);
   fChain->SetBranchAddress("FatJet_mass_jmsUp", FatJet_mass_jmsUp, &b_FatJet_mass_jmsUp);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteStatUp", FatJet_pt_jesAbsoluteStatUp, &b_FatJet_pt_jesAbsoluteStatUp);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteStatUp", FatJet_mass_jesAbsoluteStatUp, &b_FatJet_mass_jesAbsoluteStatUp);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteScaleUp", FatJet_pt_jesAbsoluteScaleUp, &b_FatJet_pt_jesAbsoluteScaleUp);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteScaleUp", FatJet_mass_jesAbsoluteScaleUp, &b_FatJet_mass_jesAbsoluteScaleUp);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteFlavMapUp", FatJet_pt_jesAbsoluteFlavMapUp, &b_FatJet_pt_jesAbsoluteFlavMapUp);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteFlavMapUp", FatJet_mass_jesAbsoluteFlavMapUp, &b_FatJet_mass_jesAbsoluteFlavMapUp);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteMPFBiasUp", FatJet_pt_jesAbsoluteMPFBiasUp, &b_FatJet_pt_jesAbsoluteMPFBiasUp);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteMPFBiasUp", FatJet_mass_jesAbsoluteMPFBiasUp, &b_FatJet_mass_jesAbsoluteMPFBiasUp);
   fChain->SetBranchAddress("FatJet_pt_jesFragmentationUp", FatJet_pt_jesFragmentationUp, &b_FatJet_pt_jesFragmentationUp);
   fChain->SetBranchAddress("FatJet_mass_jesFragmentationUp", FatJet_mass_jesFragmentationUp, &b_FatJet_mass_jesFragmentationUp);
   fChain->SetBranchAddress("FatJet_pt_jesSinglePionECALUp", FatJet_pt_jesSinglePionECALUp, &b_FatJet_pt_jesSinglePionECALUp);
   fChain->SetBranchAddress("FatJet_mass_jesSinglePionECALUp", FatJet_mass_jesSinglePionECALUp, &b_FatJet_mass_jesSinglePionECALUp);
   fChain->SetBranchAddress("FatJet_pt_jesSinglePionHCALUp", FatJet_pt_jesSinglePionHCALUp, &b_FatJet_pt_jesSinglePionHCALUp);
   fChain->SetBranchAddress("FatJet_mass_jesSinglePionHCALUp", FatJet_mass_jesSinglePionHCALUp, &b_FatJet_mass_jesSinglePionHCALUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorQCDUp", FatJet_pt_jesFlavorQCDUp, &b_FatJet_pt_jesFlavorQCDUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorQCDUp", FatJet_mass_jesFlavorQCDUp, &b_FatJet_mass_jesFlavorQCDUp);
   fChain->SetBranchAddress("FatJet_pt_jesTimePtEtaUp", FatJet_pt_jesTimePtEtaUp, &b_FatJet_pt_jesTimePtEtaUp);
   fChain->SetBranchAddress("FatJet_mass_jesTimePtEtaUp", FatJet_mass_jesTimePtEtaUp, &b_FatJet_mass_jesTimePtEtaUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeJEREC1Up", FatJet_pt_jesRelativeJEREC1Up, &b_FatJet_pt_jesRelativeJEREC1Up);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeJEREC1Up", FatJet_mass_jesRelativeJEREC1Up, &b_FatJet_mass_jesRelativeJEREC1Up);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeJEREC2Up", FatJet_pt_jesRelativeJEREC2Up, &b_FatJet_pt_jesRelativeJEREC2Up);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeJEREC2Up", FatJet_mass_jesRelativeJEREC2Up, &b_FatJet_mass_jesRelativeJEREC2Up);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeJERHFUp", FatJet_pt_jesRelativeJERHFUp, &b_FatJet_pt_jesRelativeJERHFUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeJERHFUp", FatJet_mass_jesRelativeJERHFUp, &b_FatJet_mass_jesRelativeJERHFUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtBBUp", FatJet_pt_jesRelativePtBBUp, &b_FatJet_pt_jesRelativePtBBUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtBBUp", FatJet_mass_jesRelativePtBBUp, &b_FatJet_mass_jesRelativePtBBUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtEC1Up", FatJet_pt_jesRelativePtEC1Up, &b_FatJet_pt_jesRelativePtEC1Up);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtEC1Up", FatJet_mass_jesRelativePtEC1Up, &b_FatJet_mass_jesRelativePtEC1Up);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtEC2Up", FatJet_pt_jesRelativePtEC2Up, &b_FatJet_pt_jesRelativePtEC2Up);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtEC2Up", FatJet_mass_jesRelativePtEC2Up, &b_FatJet_mass_jesRelativePtEC2Up);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtHFUp", FatJet_pt_jesRelativePtHFUp, &b_FatJet_pt_jesRelativePtHFUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtHFUp", FatJet_mass_jesRelativePtHFUp, &b_FatJet_mass_jesRelativePtHFUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeBalUp", FatJet_pt_jesRelativeBalUp, &b_FatJet_pt_jesRelativeBalUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeBalUp", FatJet_mass_jesRelativeBalUp, &b_FatJet_mass_jesRelativeBalUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeFSRUp", FatJet_pt_jesRelativeFSRUp, &b_FatJet_pt_jesRelativeFSRUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeFSRUp", FatJet_mass_jesRelativeFSRUp, &b_FatJet_mass_jesRelativeFSRUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeStatFSRUp", FatJet_pt_jesRelativeStatFSRUp, &b_FatJet_pt_jesRelativeStatFSRUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeStatFSRUp", FatJet_mass_jesRelativeStatFSRUp, &b_FatJet_mass_jesRelativeStatFSRUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeStatECUp", FatJet_pt_jesRelativeStatECUp, &b_FatJet_pt_jesRelativeStatECUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeStatECUp", FatJet_mass_jesRelativeStatECUp, &b_FatJet_mass_jesRelativeStatECUp);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeStatHFUp", FatJet_pt_jesRelativeStatHFUp, &b_FatJet_pt_jesRelativeStatHFUp);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeStatHFUp", FatJet_mass_jesRelativeStatHFUp, &b_FatJet_mass_jesRelativeStatHFUp);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpDataMCUp", FatJet_pt_jesPileUpDataMCUp, &b_FatJet_pt_jesPileUpDataMCUp);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpDataMCUp", FatJet_mass_jesPileUpDataMCUp, &b_FatJet_mass_jesPileUpDataMCUp);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtRefUp", FatJet_pt_jesPileUpPtRefUp, &b_FatJet_pt_jesPileUpPtRefUp);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtRefUp", FatJet_mass_jesPileUpPtRefUp, &b_FatJet_mass_jesPileUpPtRefUp);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtBBUp", FatJet_pt_jesPileUpPtBBUp, &b_FatJet_pt_jesPileUpPtBBUp);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtBBUp", FatJet_mass_jesPileUpPtBBUp, &b_FatJet_mass_jesPileUpPtBBUp);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtEC1Up", FatJet_pt_jesPileUpPtEC1Up, &b_FatJet_pt_jesPileUpPtEC1Up);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtEC1Up", FatJet_mass_jesPileUpPtEC1Up, &b_FatJet_mass_jesPileUpPtEC1Up);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtEC2Up", FatJet_pt_jesPileUpPtEC2Up, &b_FatJet_pt_jesPileUpPtEC2Up);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtEC2Up", FatJet_mass_jesPileUpPtEC2Up, &b_FatJet_mass_jesPileUpPtEC2Up);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtHFUp", FatJet_pt_jesPileUpPtHFUp, &b_FatJet_pt_jesPileUpPtHFUp);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtHFUp", FatJet_mass_jesPileUpPtHFUp, &b_FatJet_mass_jesPileUpPtHFUp);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpMuZeroUp", FatJet_pt_jesPileUpMuZeroUp, &b_FatJet_pt_jesPileUpMuZeroUp);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpMuZeroUp", FatJet_mass_jesPileUpMuZeroUp, &b_FatJet_mass_jesPileUpMuZeroUp);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpEnvelopeUp", FatJet_pt_jesPileUpEnvelopeUp, &b_FatJet_pt_jesPileUpEnvelopeUp);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpEnvelopeUp", FatJet_mass_jesPileUpEnvelopeUp, &b_FatJet_mass_jesPileUpEnvelopeUp);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalPileUpUp", FatJet_pt_jesSubTotalPileUpUp, &b_FatJet_pt_jesSubTotalPileUpUp);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalPileUpUp", FatJet_mass_jesSubTotalPileUpUp, &b_FatJet_mass_jesSubTotalPileUpUp);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalRelativeUp", FatJet_pt_jesSubTotalRelativeUp, &b_FatJet_pt_jesSubTotalRelativeUp);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalRelativeUp", FatJet_mass_jesSubTotalRelativeUp, &b_FatJet_mass_jesSubTotalRelativeUp);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalPtUp", FatJet_pt_jesSubTotalPtUp, &b_FatJet_pt_jesSubTotalPtUp);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalPtUp", FatJet_mass_jesSubTotalPtUp, &b_FatJet_mass_jesSubTotalPtUp);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalScaleUp", FatJet_pt_jesSubTotalScaleUp, &b_FatJet_pt_jesSubTotalScaleUp);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalScaleUp", FatJet_mass_jesSubTotalScaleUp, &b_FatJet_mass_jesSubTotalScaleUp);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalAbsoluteUp", FatJet_pt_jesSubTotalAbsoluteUp, &b_FatJet_pt_jesSubTotalAbsoluteUp);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalAbsoluteUp", FatJet_mass_jesSubTotalAbsoluteUp, &b_FatJet_mass_jesSubTotalAbsoluteUp);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalMCUp", FatJet_pt_jesSubTotalMCUp, &b_FatJet_pt_jesSubTotalMCUp);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalMCUp", FatJet_mass_jesSubTotalMCUp, &b_FatJet_mass_jesSubTotalMCUp);
   fChain->SetBranchAddress("FatJet_pt_jesTotalUp", FatJet_pt_jesTotalUp, &b_FatJet_pt_jesTotalUp);
   fChain->SetBranchAddress("FatJet_mass_jesTotalUp", FatJet_mass_jesTotalUp, &b_FatJet_mass_jesTotalUp);
   fChain->SetBranchAddress("FatJet_pt_jesTotalNoFlavorUp", FatJet_pt_jesTotalNoFlavorUp, &b_FatJet_pt_jesTotalNoFlavorUp);
   fChain->SetBranchAddress("FatJet_mass_jesTotalNoFlavorUp", FatJet_mass_jesTotalNoFlavorUp, &b_FatJet_mass_jesTotalNoFlavorUp);
   fChain->SetBranchAddress("FatJet_pt_jesTotalNoTimeUp", FatJet_pt_jesTotalNoTimeUp, &b_FatJet_pt_jesTotalNoTimeUp);
   fChain->SetBranchAddress("FatJet_mass_jesTotalNoTimeUp", FatJet_mass_jesTotalNoTimeUp, &b_FatJet_mass_jesTotalNoTimeUp);
   fChain->SetBranchAddress("FatJet_pt_jesTotalNoFlavorNoTimeUp", FatJet_pt_jesTotalNoFlavorNoTimeUp, &b_FatJet_pt_jesTotalNoFlavorNoTimeUp);
   fChain->SetBranchAddress("FatJet_mass_jesTotalNoFlavorNoTimeUp", FatJet_mass_jesTotalNoFlavorNoTimeUp, &b_FatJet_mass_jesTotalNoFlavorNoTimeUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorZJetUp", FatJet_pt_jesFlavorZJetUp, &b_FatJet_pt_jesFlavorZJetUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorZJetUp", FatJet_mass_jesFlavorZJetUp, &b_FatJet_mass_jesFlavorZJetUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPhotonJetUp", FatJet_pt_jesFlavorPhotonJetUp, &b_FatJet_pt_jesFlavorPhotonJetUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPhotonJetUp", FatJet_mass_jesFlavorPhotonJetUp, &b_FatJet_mass_jesFlavorPhotonJetUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureGluonUp", FatJet_pt_jesFlavorPureGluonUp, &b_FatJet_pt_jesFlavorPureGluonUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureGluonUp", FatJet_mass_jesFlavorPureGluonUp, &b_FatJet_mass_jesFlavorPureGluonUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureQuarkUp", FatJet_pt_jesFlavorPureQuarkUp, &b_FatJet_pt_jesFlavorPureQuarkUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureQuarkUp", FatJet_mass_jesFlavorPureQuarkUp, &b_FatJet_mass_jesFlavorPureQuarkUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureCharmUp", FatJet_pt_jesFlavorPureCharmUp, &b_FatJet_pt_jesFlavorPureCharmUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureCharmUp", FatJet_mass_jesFlavorPureCharmUp, &b_FatJet_mass_jesFlavorPureCharmUp);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureBottomUp", FatJet_pt_jesFlavorPureBottomUp, &b_FatJet_pt_jesFlavorPureBottomUp);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureBottomUp", FatJet_mass_jesFlavorPureBottomUp, &b_FatJet_mass_jesFlavorPureBottomUp);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunBCDUp", FatJet_pt_jesTimeRunBCDUp, &b_FatJet_pt_jesTimeRunBCDUp);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunBCDUp", FatJet_mass_jesTimeRunBCDUp, &b_FatJet_mass_jesTimeRunBCDUp);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunEFUp", FatJet_pt_jesTimeRunEFUp, &b_FatJet_pt_jesTimeRunEFUp);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunEFUp", FatJet_mass_jesTimeRunEFUp, &b_FatJet_mass_jesTimeRunEFUp);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunGUp", FatJet_pt_jesTimeRunGUp, &b_FatJet_pt_jesTimeRunGUp);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunGUp", FatJet_mass_jesTimeRunGUp, &b_FatJet_mass_jesTimeRunGUp);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunHUp", FatJet_pt_jesTimeRunHUp, &b_FatJet_pt_jesTimeRunHUp);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunHUp", FatJet_mass_jesTimeRunHUp, &b_FatJet_mass_jesTimeRunHUp);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupMPFInSituUp", FatJet_pt_jesCorrelationGroupMPFInSituUp, &b_FatJet_pt_jesCorrelationGroupMPFInSituUp);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupMPFInSituUp", FatJet_mass_jesCorrelationGroupMPFInSituUp, &b_FatJet_mass_jesCorrelationGroupMPFInSituUp);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupIntercalibrationUp", FatJet_pt_jesCorrelationGroupIntercalibrationUp, &b_FatJet_pt_jesCorrelationGroupIntercalibrationUp);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupIntercalibrationUp", FatJet_mass_jesCorrelationGroupIntercalibrationUp, &b_FatJet_mass_jesCorrelationGroupIntercalibrationUp);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupbJESUp", FatJet_pt_jesCorrelationGroupbJESUp, &b_FatJet_pt_jesCorrelationGroupbJESUp);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupbJESUp", FatJet_mass_jesCorrelationGroupbJESUp, &b_FatJet_mass_jesCorrelationGroupbJESUp);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupFlavorUp", FatJet_pt_jesCorrelationGroupFlavorUp, &b_FatJet_pt_jesCorrelationGroupFlavorUp);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupFlavorUp", FatJet_mass_jesCorrelationGroupFlavorUp, &b_FatJet_mass_jesCorrelationGroupFlavorUp);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupUncorrelatedUp", FatJet_pt_jesCorrelationGroupUncorrelatedUp, &b_FatJet_pt_jesCorrelationGroupUncorrelatedUp);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupUncorrelatedUp", FatJet_mass_jesCorrelationGroupUncorrelatedUp, &b_FatJet_mass_jesCorrelationGroupUncorrelatedUp);
   fChain->SetBranchAddress("FatJet_pt_jerDown", FatJet_pt_jerDown, &b_FatJet_pt_jerDown);
   fChain->SetBranchAddress("FatJet_mass_jerDown", FatJet_mass_jerDown, &b_FatJet_mass_jerDown);
   fChain->SetBranchAddress("FatJet_mass_jmrDown", FatJet_mass_jmrDown, &b_FatJet_mass_jmrDown);
   fChain->SetBranchAddress("FatJet_mass_jmsDown", FatJet_mass_jmsDown, &b_FatJet_mass_jmsDown);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteStatDown", FatJet_pt_jesAbsoluteStatDown, &b_FatJet_pt_jesAbsoluteStatDown);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteStatDown", FatJet_mass_jesAbsoluteStatDown, &b_FatJet_mass_jesAbsoluteStatDown);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteScaleDown", FatJet_pt_jesAbsoluteScaleDown, &b_FatJet_pt_jesAbsoluteScaleDown);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteScaleDown", FatJet_mass_jesAbsoluteScaleDown, &b_FatJet_mass_jesAbsoluteScaleDown);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteFlavMapDown", FatJet_pt_jesAbsoluteFlavMapDown, &b_FatJet_pt_jesAbsoluteFlavMapDown);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteFlavMapDown", FatJet_mass_jesAbsoluteFlavMapDown, &b_FatJet_mass_jesAbsoluteFlavMapDown);
   fChain->SetBranchAddress("FatJet_pt_jesAbsoluteMPFBiasDown", FatJet_pt_jesAbsoluteMPFBiasDown, &b_FatJet_pt_jesAbsoluteMPFBiasDown);
   fChain->SetBranchAddress("FatJet_mass_jesAbsoluteMPFBiasDown", FatJet_mass_jesAbsoluteMPFBiasDown, &b_FatJet_mass_jesAbsoluteMPFBiasDown);
   fChain->SetBranchAddress("FatJet_pt_jesFragmentationDown", FatJet_pt_jesFragmentationDown, &b_FatJet_pt_jesFragmentationDown);
   fChain->SetBranchAddress("FatJet_mass_jesFragmentationDown", FatJet_mass_jesFragmentationDown, &b_FatJet_mass_jesFragmentationDown);
   fChain->SetBranchAddress("FatJet_pt_jesSinglePionECALDown", FatJet_pt_jesSinglePionECALDown, &b_FatJet_pt_jesSinglePionECALDown);
   fChain->SetBranchAddress("FatJet_mass_jesSinglePionECALDown", FatJet_mass_jesSinglePionECALDown, &b_FatJet_mass_jesSinglePionECALDown);
   fChain->SetBranchAddress("FatJet_pt_jesSinglePionHCALDown", FatJet_pt_jesSinglePionHCALDown, &b_FatJet_pt_jesSinglePionHCALDown);
   fChain->SetBranchAddress("FatJet_mass_jesSinglePionHCALDown", FatJet_mass_jesSinglePionHCALDown, &b_FatJet_mass_jesSinglePionHCALDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorQCDDown", FatJet_pt_jesFlavorQCDDown, &b_FatJet_pt_jesFlavorQCDDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorQCDDown", FatJet_mass_jesFlavorQCDDown, &b_FatJet_mass_jesFlavorQCDDown);
   fChain->SetBranchAddress("FatJet_pt_jesTimePtEtaDown", FatJet_pt_jesTimePtEtaDown, &b_FatJet_pt_jesTimePtEtaDown);
   fChain->SetBranchAddress("FatJet_mass_jesTimePtEtaDown", FatJet_mass_jesTimePtEtaDown, &b_FatJet_mass_jesTimePtEtaDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeJEREC1Down", FatJet_pt_jesRelativeJEREC1Down, &b_FatJet_pt_jesRelativeJEREC1Down);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeJEREC1Down", FatJet_mass_jesRelativeJEREC1Down, &b_FatJet_mass_jesRelativeJEREC1Down);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeJEREC2Down", FatJet_pt_jesRelativeJEREC2Down, &b_FatJet_pt_jesRelativeJEREC2Down);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeJEREC2Down", FatJet_mass_jesRelativeJEREC2Down, &b_FatJet_mass_jesRelativeJEREC2Down);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeJERHFDown", FatJet_pt_jesRelativeJERHFDown, &b_FatJet_pt_jesRelativeJERHFDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeJERHFDown", FatJet_mass_jesRelativeJERHFDown, &b_FatJet_mass_jesRelativeJERHFDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtBBDown", FatJet_pt_jesRelativePtBBDown, &b_FatJet_pt_jesRelativePtBBDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtBBDown", FatJet_mass_jesRelativePtBBDown, &b_FatJet_mass_jesRelativePtBBDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtEC1Down", FatJet_pt_jesRelativePtEC1Down, &b_FatJet_pt_jesRelativePtEC1Down);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtEC1Down", FatJet_mass_jesRelativePtEC1Down, &b_FatJet_mass_jesRelativePtEC1Down);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtEC2Down", FatJet_pt_jesRelativePtEC2Down, &b_FatJet_pt_jesRelativePtEC2Down);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtEC2Down", FatJet_mass_jesRelativePtEC2Down, &b_FatJet_mass_jesRelativePtEC2Down);
   fChain->SetBranchAddress("FatJet_pt_jesRelativePtHFDown", FatJet_pt_jesRelativePtHFDown, &b_FatJet_pt_jesRelativePtHFDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativePtHFDown", FatJet_mass_jesRelativePtHFDown, &b_FatJet_mass_jesRelativePtHFDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeBalDown", FatJet_pt_jesRelativeBalDown, &b_FatJet_pt_jesRelativeBalDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeBalDown", FatJet_mass_jesRelativeBalDown, &b_FatJet_mass_jesRelativeBalDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeFSRDown", FatJet_pt_jesRelativeFSRDown, &b_FatJet_pt_jesRelativeFSRDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeFSRDown", FatJet_mass_jesRelativeFSRDown, &b_FatJet_mass_jesRelativeFSRDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeStatFSRDown", FatJet_pt_jesRelativeStatFSRDown, &b_FatJet_pt_jesRelativeStatFSRDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeStatFSRDown", FatJet_mass_jesRelativeStatFSRDown, &b_FatJet_mass_jesRelativeStatFSRDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeStatECDown", FatJet_pt_jesRelativeStatECDown, &b_FatJet_pt_jesRelativeStatECDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeStatECDown", FatJet_mass_jesRelativeStatECDown, &b_FatJet_mass_jesRelativeStatECDown);
   fChain->SetBranchAddress("FatJet_pt_jesRelativeStatHFDown", FatJet_pt_jesRelativeStatHFDown, &b_FatJet_pt_jesRelativeStatHFDown);
   fChain->SetBranchAddress("FatJet_mass_jesRelativeStatHFDown", FatJet_mass_jesRelativeStatHFDown, &b_FatJet_mass_jesRelativeStatHFDown);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpDataMCDown", FatJet_pt_jesPileUpDataMCDown, &b_FatJet_pt_jesPileUpDataMCDown);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpDataMCDown", FatJet_mass_jesPileUpDataMCDown, &b_FatJet_mass_jesPileUpDataMCDown);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtRefDown", FatJet_pt_jesPileUpPtRefDown, &b_FatJet_pt_jesPileUpPtRefDown);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtRefDown", FatJet_mass_jesPileUpPtRefDown, &b_FatJet_mass_jesPileUpPtRefDown);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtBBDown", FatJet_pt_jesPileUpPtBBDown, &b_FatJet_pt_jesPileUpPtBBDown);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtBBDown", FatJet_mass_jesPileUpPtBBDown, &b_FatJet_mass_jesPileUpPtBBDown);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtEC1Down", FatJet_pt_jesPileUpPtEC1Down, &b_FatJet_pt_jesPileUpPtEC1Down);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtEC1Down", FatJet_mass_jesPileUpPtEC1Down, &b_FatJet_mass_jesPileUpPtEC1Down);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtEC2Down", FatJet_pt_jesPileUpPtEC2Down, &b_FatJet_pt_jesPileUpPtEC2Down);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtEC2Down", FatJet_mass_jesPileUpPtEC2Down, &b_FatJet_mass_jesPileUpPtEC2Down);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpPtHFDown", FatJet_pt_jesPileUpPtHFDown, &b_FatJet_pt_jesPileUpPtHFDown);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpPtHFDown", FatJet_mass_jesPileUpPtHFDown, &b_FatJet_mass_jesPileUpPtHFDown);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpMuZeroDown", FatJet_pt_jesPileUpMuZeroDown, &b_FatJet_pt_jesPileUpMuZeroDown);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpMuZeroDown", FatJet_mass_jesPileUpMuZeroDown, &b_FatJet_mass_jesPileUpMuZeroDown);
   fChain->SetBranchAddress("FatJet_pt_jesPileUpEnvelopeDown", FatJet_pt_jesPileUpEnvelopeDown, &b_FatJet_pt_jesPileUpEnvelopeDown);
   fChain->SetBranchAddress("FatJet_mass_jesPileUpEnvelopeDown", FatJet_mass_jesPileUpEnvelopeDown, &b_FatJet_mass_jesPileUpEnvelopeDown);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalPileUpDown", FatJet_pt_jesSubTotalPileUpDown, &b_FatJet_pt_jesSubTotalPileUpDown);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalPileUpDown", FatJet_mass_jesSubTotalPileUpDown, &b_FatJet_mass_jesSubTotalPileUpDown);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalRelativeDown", FatJet_pt_jesSubTotalRelativeDown, &b_FatJet_pt_jesSubTotalRelativeDown);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalRelativeDown", FatJet_mass_jesSubTotalRelativeDown, &b_FatJet_mass_jesSubTotalRelativeDown);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalPtDown", FatJet_pt_jesSubTotalPtDown, &b_FatJet_pt_jesSubTotalPtDown);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalPtDown", FatJet_mass_jesSubTotalPtDown, &b_FatJet_mass_jesSubTotalPtDown);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalScaleDown", FatJet_pt_jesSubTotalScaleDown, &b_FatJet_pt_jesSubTotalScaleDown);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalScaleDown", FatJet_mass_jesSubTotalScaleDown, &b_FatJet_mass_jesSubTotalScaleDown);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalAbsoluteDown", FatJet_pt_jesSubTotalAbsoluteDown, &b_FatJet_pt_jesSubTotalAbsoluteDown);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalAbsoluteDown", FatJet_mass_jesSubTotalAbsoluteDown, &b_FatJet_mass_jesSubTotalAbsoluteDown);
   fChain->SetBranchAddress("FatJet_pt_jesSubTotalMCDown", FatJet_pt_jesSubTotalMCDown, &b_FatJet_pt_jesSubTotalMCDown);
   fChain->SetBranchAddress("FatJet_mass_jesSubTotalMCDown", FatJet_mass_jesSubTotalMCDown, &b_FatJet_mass_jesSubTotalMCDown);
   fChain->SetBranchAddress("FatJet_pt_jesTotalDown", FatJet_pt_jesTotalDown, &b_FatJet_pt_jesTotalDown);
   fChain->SetBranchAddress("FatJet_mass_jesTotalDown", FatJet_mass_jesTotalDown, &b_FatJet_mass_jesTotalDown);
   fChain->SetBranchAddress("FatJet_pt_jesTotalNoFlavorDown", FatJet_pt_jesTotalNoFlavorDown, &b_FatJet_pt_jesTotalNoFlavorDown);
   fChain->SetBranchAddress("FatJet_mass_jesTotalNoFlavorDown", FatJet_mass_jesTotalNoFlavorDown, &b_FatJet_mass_jesTotalNoFlavorDown);
   fChain->SetBranchAddress("FatJet_pt_jesTotalNoTimeDown", FatJet_pt_jesTotalNoTimeDown, &b_FatJet_pt_jesTotalNoTimeDown);
   fChain->SetBranchAddress("FatJet_mass_jesTotalNoTimeDown", FatJet_mass_jesTotalNoTimeDown, &b_FatJet_mass_jesTotalNoTimeDown);
   fChain->SetBranchAddress("FatJet_pt_jesTotalNoFlavorNoTimeDown", FatJet_pt_jesTotalNoFlavorNoTimeDown, &b_FatJet_pt_jesTotalNoFlavorNoTimeDown);
   fChain->SetBranchAddress("FatJet_mass_jesTotalNoFlavorNoTimeDown", FatJet_mass_jesTotalNoFlavorNoTimeDown, &b_FatJet_mass_jesTotalNoFlavorNoTimeDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorZJetDown", FatJet_pt_jesFlavorZJetDown, &b_FatJet_pt_jesFlavorZJetDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorZJetDown", FatJet_mass_jesFlavorZJetDown, &b_FatJet_mass_jesFlavorZJetDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPhotonJetDown", FatJet_pt_jesFlavorPhotonJetDown, &b_FatJet_pt_jesFlavorPhotonJetDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPhotonJetDown", FatJet_mass_jesFlavorPhotonJetDown, &b_FatJet_mass_jesFlavorPhotonJetDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureGluonDown", FatJet_pt_jesFlavorPureGluonDown, &b_FatJet_pt_jesFlavorPureGluonDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureGluonDown", FatJet_mass_jesFlavorPureGluonDown, &b_FatJet_mass_jesFlavorPureGluonDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureQuarkDown", FatJet_pt_jesFlavorPureQuarkDown, &b_FatJet_pt_jesFlavorPureQuarkDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureQuarkDown", FatJet_mass_jesFlavorPureQuarkDown, &b_FatJet_mass_jesFlavorPureQuarkDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureCharmDown", FatJet_pt_jesFlavorPureCharmDown, &b_FatJet_pt_jesFlavorPureCharmDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureCharmDown", FatJet_mass_jesFlavorPureCharmDown, &b_FatJet_mass_jesFlavorPureCharmDown);
   fChain->SetBranchAddress("FatJet_pt_jesFlavorPureBottomDown", FatJet_pt_jesFlavorPureBottomDown, &b_FatJet_pt_jesFlavorPureBottomDown);
   fChain->SetBranchAddress("FatJet_mass_jesFlavorPureBottomDown", FatJet_mass_jesFlavorPureBottomDown, &b_FatJet_mass_jesFlavorPureBottomDown);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunBCDDown", FatJet_pt_jesTimeRunBCDDown, &b_FatJet_pt_jesTimeRunBCDDown);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunBCDDown", FatJet_mass_jesTimeRunBCDDown, &b_FatJet_mass_jesTimeRunBCDDown);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunEFDown", FatJet_pt_jesTimeRunEFDown, &b_FatJet_pt_jesTimeRunEFDown);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunEFDown", FatJet_mass_jesTimeRunEFDown, &b_FatJet_mass_jesTimeRunEFDown);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunGDown", FatJet_pt_jesTimeRunGDown, &b_FatJet_pt_jesTimeRunGDown);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunGDown", FatJet_mass_jesTimeRunGDown, &b_FatJet_mass_jesTimeRunGDown);
   fChain->SetBranchAddress("FatJet_pt_jesTimeRunHDown", FatJet_pt_jesTimeRunHDown, &b_FatJet_pt_jesTimeRunHDown);
   fChain->SetBranchAddress("FatJet_mass_jesTimeRunHDown", FatJet_mass_jesTimeRunHDown, &b_FatJet_mass_jesTimeRunHDown);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupMPFInSituDown", FatJet_pt_jesCorrelationGroupMPFInSituDown, &b_FatJet_pt_jesCorrelationGroupMPFInSituDown);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupMPFInSituDown", FatJet_mass_jesCorrelationGroupMPFInSituDown, &b_FatJet_mass_jesCorrelationGroupMPFInSituDown);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupIntercalibrationDown", FatJet_pt_jesCorrelationGroupIntercalibrationDown, &b_FatJet_pt_jesCorrelationGroupIntercalibrationDown);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupIntercalibrationDown", FatJet_mass_jesCorrelationGroupIntercalibrationDown, &b_FatJet_mass_jesCorrelationGroupIntercalibrationDown);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupbJESDown", FatJet_pt_jesCorrelationGroupbJESDown, &b_FatJet_pt_jesCorrelationGroupbJESDown);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupbJESDown", FatJet_mass_jesCorrelationGroupbJESDown, &b_FatJet_mass_jesCorrelationGroupbJESDown);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupFlavorDown", FatJet_pt_jesCorrelationGroupFlavorDown, &b_FatJet_pt_jesCorrelationGroupFlavorDown);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupFlavorDown", FatJet_mass_jesCorrelationGroupFlavorDown, &b_FatJet_mass_jesCorrelationGroupFlavorDown);
   fChain->SetBranchAddress("FatJet_pt_jesCorrelationGroupUncorrelatedDown", FatJet_pt_jesCorrelationGroupUncorrelatedDown, &b_FatJet_pt_jesCorrelationGroupUncorrelatedDown);
   fChain->SetBranchAddress("FatJet_mass_jesCorrelationGroupUncorrelatedDown", FatJet_mass_jesCorrelationGroupUncorrelatedDown, &b_FatJet_mass_jesCorrelationGroupUncorrelatedDown);
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
   fChain->SetBranchAddress("V_mt", &V_mt, &b_V_mt);
   fChain->SetBranchAddress("Jet_lepFilter", Jet_lepFilter, &b_Jet_lepFilter);
   fChain->SetBranchAddress("vLidx", vLidx, &b_vLidx);
   fChain->SetBranchAddress("hJidx", hJidx, &b_hJidx);
   fChain->SetBranchAddress("hJidxCMVA", hJidxCMVA, &b_hJidxCMVA);
   fChain->SetBranchAddress("H_pt", &H_pt, &b_H_pt);
   fChain->SetBranchAddress("H_eta", &H_eta, &b_H_eta);
   fChain->SetBranchAddress("H_phi", &H_phi, &b_H_phi);
   fChain->SetBranchAddress("H_mass", &H_mass, &b_H_mass);
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
   fChain->SetBranchAddress("FatJet_lepFilter", FatJet_lepFilter, &b_FatJet_lepFilter);
   fChain->SetBranchAddress("FatJet_Pt", FatJet_Pt, &b_FatJet_Pt);
   fChain->SetBranchAddress("FatJet_Msoftdrop", FatJet_Msoftdrop, &b_FatJet_Msoftdrop);
   fChain->SetBranchAddress("FatJet_FlavourComposition", FatJet_FlavourComposition, &b_FatJet_FlavourComposition);
   fChain->SetBranchAddress("FatJet_HiggsProducts", FatJet_HiggsProducts, &b_FatJet_HiggsProducts);
   fChain->SetBranchAddress("FatJet_WProducts", FatJet_WProducts, &b_FatJet_WProducts);
   fChain->SetBranchAddress("FatJet_ZProducts", FatJet_ZProducts, &b_FatJet_ZProducts);
   Notify();
}

Bool_t Myclass::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Myclass::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Myclass::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef Myclass_cxx
