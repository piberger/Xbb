#!/usr/bin/env python
import ROOT
import numpy as np
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule

from JMEres2017 import JMEres

# resolution functions from HH4b analysis
# https://github.com/cvernier/HH4b2016/blob/master/HbbHbb_Component_KinFit.cc
def ErrpT_Signal(pT, eta):
    if abs(eta)<1.4:
        pT = 40 if pT<40 else 550 if pT > 550 else pT
        sigmapT = 22.26 - 0.01*pT + 0.00018*pT*pT
    else:
        pT = 40 if pT<40 else 350 if pT > 350 else pT
        sigmapT = 17.11 + 0.058 * pT
    return sigmapT*sigmapT

def ErrEta_Signal(pT):
    pT = 40 if pT<40 else 500 if pT > 500 else pT
    sigmaEta = 0.033 + (4.1/pT) + (-0.17/pow(pT,0.5))
    return sigmaEta*sigmaEta

def ErrPhi_Signal(pT):
    pT = 40 if pT<40 else 500 if pT > 500 else pT
    sigmaPhi = 0.038 + (4.1/pT) + (-0.19/pow(pT,0.5))
    return sigmaPhi*sigmaPhi

def fourvector(pt, eta, phi, m, ind=-1):
    if ind == -1:
        v = ROOT.TLorentzVector()
        v.SetPtEtaPhiM(pt, eta, phi, m)
    else:
        v = ROOT.TLorentzVector()
        v.SetPtEtaPhiM(pt[ind], eta[ind], phi[ind], m[ind])
    return v

def fit_jet(v, resScale=1.0):
    cov = ROOT.TMatrixD(3, 3)
    cov.Zero()
    cov[0][0] = ErrpT_Signal(v.Et(), v.Eta()) * resScale**2
    cov[1][1] = ErrEta_Signal(v.Et())
    cov[2][2] = ErrPhi_Signal(v.Et())
    return ROOT.TFitParticleEtEtaPhi(v, cov)

def fit_lepton(v, ptErr):    
    cov = ROOT.TMatrixD(3, 3)
    cov.Zero()
    cov[0][0] = ptErr**2 
    cov[1][1] = 0.0001 # eta: too small
    cov[2][2] = 0.0001 # phi: too small
    return ROOT.TFitParticleEtEtaPhi(v, cov) 

# based on AnalysisTools code
# https://github.com/capalmer85/AnalysisTools/blob/master/python/kinfitter.py
class kinFitterXbb(AddCollectionsModule):

    def __init__(self):
        self.debug = False
        self.HH4B_RES_SCALE = 0.62
        self.LLVV_PXY_VAR = 8.0**2 
        self.Z_MASS = 91.1876
        self.Z_WIDTH = 1.7*3
        super(kinFitterXbb, self).__init__()
        
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TAbsFitConstraint_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TAbsFitParticle_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitConstraintEp_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitConstraintMGaus_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitConstraintM_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleCart_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleECart_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleEMomDev_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleEScaledMomDev_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleESpher_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleEtEtaPhi_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleEtThetaPhi_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleMCCart_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleMCMomDev_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleMCPInvSpher_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleMCSpher_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleMomDev_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TFitParticleSpher_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TKinFitter_cc.so")
        ROOT.gSystem.Load("../HelperClasses/KinFitter/TSLToyGen_cc.so")

        self.JMEres = JMEres()

    def customInit(self, initVars):
        self.branchName = "kinFit"
        self.sample = initVars['sample']
        self.config = initVars['config']
        if self.config.has_section('KinematicFit') and self.config.has_option('KinematicFit','systematics') and not self.sample.isData():
            self.systematics = [(x if x != 'Nominal' else '') for x in self.config.get('KinematicFit','systematics').strip().split(' ')]
        else:
            self.systematics = ['']
        print("INFO: computing the fit for", len(self.systematics), " variations.")

        self.bDict = {}
        for syst in self.systematics:
            self.bDict[syst] = {}
            for n in ['H_mass_fit', 'H_eta_fit', 'H_phi_fit', 'H_pt_fit', 'HVdPhi_fit', 'jjVPtRatio_fit', 'hJets_pt_0_fit', 'hJets_pt_1_fit', 'V_pt_fit', 'V_eta_fit', 'V_phi_fit', 'V_mass_fit', 'H_mass_sigma_fit']:
                branchNameFull = self.branchName + "_" + n + ('_' + syst if len(syst) > 0 else '')
                self.bDict[syst][n] = branchNameFull
                self.addBranch(branchNameFull)
            for n in ['n_recoil_jets_fit', 'status']:
                branchNameFull = self.branchName + "_" + n + ('_' + syst if len(syst) > 0 else '')
                self.bDict[syst][n] = branchNameFull
                self.addIntegerBranch(branchNameFull)

        #self.jme_res_obj = ROOT.JME.JetResolution('data/Fall17_V3_DATA_PtResolution_AK4PFchs.txt')

    def cart_cov(self, v, rho):
        #jme_par = ROOT.JME.JetParameters().setRho(rho).setJetPt(v.Pt()).setJetEta(v.Eta())
        #jme_res = self.jme_res_obj.getResolution(jme_par) * v.Pt()
        jme_res = self.JMEres.eval(v.Eta(), rho, v.Pt())
        cos_phi = np.cos(v.Phi())
        sin_phi = np.sin(v.Phi())
        cov = ROOT.TMatrixD(4, 4)
        cov.Zero()
        cov[0][0] = (jme_res*cos_phi)**2
        cov[1][0] = jme_res**2 * cos_phi * sin_phi
        cov[0][1] = cov[1][0]
        cov[1][1] = (jme_res*sin_phi)**2
        return cov

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            phi = tree.Jet_phi
            eta = tree.Jet_eta

            hJidx = tree.hJidx
            vLidx = tree.vLidx
            fsrJidx = []

            for syst in self.systematics:

                # systematic up/down variation
                if len(syst) > 0:
                    # vary regression
                    if syst == 'jerReg_Up':
                        pt = tree.Jet_Pt
                        pt_reg = tree.Jet_PtRegUp
                        mass = tree.Jet_mass_nom
                    elif syst == 'jerReg_Down':
                        pt = tree.Jet_Pt
                        pt_reg = tree.Jet_PtRegDown
                        mass = tree.Jet_mass_nom
                    # vary JEC
                    else:
                        pt = getattr(tree, 'Jet_pt_' + syst.replace('_','')) 
                        pt_reg = tree.Jet_PtReg
                        mass = getattr(tree, 'Jet_mass_' + syst.replace('_',''))
                # nominal
                else:
                    pt = tree.Jet_Pt
                    pt_reg = tree.Jet_PtReg
                    if self.sample.type != 'DATA':
                        mass = tree.Jet_mass_nom
                    else:
                        mass = tree.Jet_mass


                # higgs jets
                j1 = fourvector(pt_reg[hJidx[0]], eta[hJidx[0]], phi[hJidx[0]], mass[hJidx[0]] * pt_reg[hJidx[0]]/pt[hJidx[0]])
                j2 = fourvector(pt_reg[hJidx[1]], eta[hJidx[1]], phi[hJidx[1]], mass[hJidx[1]] * pt_reg[hJidx[1]]/pt[hJidx[1]])

                # FSR jets
                for i in range(tree.nJet):
                    if i not in hJidx and tree.Jet_lepFilter[i] > 0 and tree.Jet_puId[i] > 0 and pt[i] > 20 and abs(eta[i]) < 3.0:

                        j_fsr = fourvector(pt[i], eta[i], phi[i], mass[i])

                        delta_r1 = j_fsr.DeltaR(j1)
                        delta_r2 = j_fsr.DeltaR(j2)

                        if min(delta_r1, delta_r2) < 0.8:
                            fsrJidx.append(i)
                            if delta_r1 < delta_r2:
                                j1 += j_fsr
                            else:
                                j2 += j_fsr

                fit_j1 = fit_jet(j1, self.HH4B_RES_SCALE)
                fit_j2 = fit_jet(j2, self.HH4B_RES_SCALE)

                # recoil jets
                recoil_jets = []
                for i in range(tree.nJet):
                    if i not in hJidx and i not in fsrJidx and tree.Jet_puId[i] > 1 and tree.Jet_jetId[i] > 1 and tree.Jet_lepFilter[i] > 0 and pt[i] > 20:
                        recoil_jets.append(fourvector(pt[i], eta[i], phi[i], mass[i]))
                recoil_sum = sum(recoil_jets, ROOT.TLorentzVector())

                cov_recoil = ROOT.TMatrixD(4, 4)
                cov_recoil.Zero()
                cov_recoil[0][0] = self.LLVV_PXY_VAR
                cov_recoil[1][1] = self.LLVV_PXY_VAR
                cov_recoil[2][2] = 1
                cov_recoil[3][3] = 1e12

                for j in recoil_jets:
                    cov_recoil += self.cart_cov(j, tree.fixedGridRhoFastjetAll)
                fit_recoil = ROOT.TFitParticleECart(recoil_sum, cov_recoil)

                #leptons
                if tree.Vtype == 0:
                    fit_l1 = fit_lepton(fourvector(abs(tree.Muon_corrected_pt[vLidx[0]]), tree.Muon_eta[vLidx[0]], tree.Muon_phi[vLidx[0]], tree.Muon_mass[vLidx[0]]), tree.Muon_ptErr[vLidx[0]])
                    fit_l2 = fit_lepton(fourvector(abs(tree.Muon_corrected_pt[vLidx[1]]), tree.Muon_eta[vLidx[1]], tree.Muon_phi[vLidx[1]], tree.Muon_mass[vLidx[1]]), tree.Muon_ptErr[vLidx[1]])
                else:
                    fit_l1 = fit_lepton(fourvector(abs(tree.Electron_pt[vLidx[0]]), tree.Electron_eta[vLidx[0]], tree.Electron_phi[vLidx[0]], tree.Electron_mass[vLidx[0]]), tree.Electron_energyErr[vLidx[0]])
                    fit_l2 = fit_lepton(fourvector(abs(tree.Electron_pt[vLidx[1]]), tree.Electron_eta[vLidx[1]], tree.Electron_phi[vLidx[1]], tree.Electron_mass[vLidx[1]]), tree.Electron_energyErr[vLidx[1]])

                # constraints
                cons_MZ = ROOT.TFitConstraintMGaus('cons_MZ', '', None, None, self.Z_MASS, self.Z_WIDTH)
                cons_MZ.addParticle1(fit_l1)
                cons_MZ.addParticle1(fit_l2)

                cons_x = ROOT.TFitConstraintEp('cons_x', '', ROOT.TFitConstraintEp.pX)
                cons_x.addParticles(fit_j1, fit_j2, fit_l1, fit_l2, fit_recoil) 

                cons_y = ROOT.TFitConstraintEp('cons_y', '', ROOT.TFitConstraintEp.pY)
                cons_y.addParticles(fit_j1, fit_j2, fit_l1, fit_l2, fit_recoil) 

                # setup fitter
                fitter = ROOT.TKinFitter()
                fitter.addMeasParticles(fit_j1, fit_j2, fit_l1, fit_l2, fit_recoil)
                fitter.addConstraint(cons_MZ)
                fitter.addConstraint(cons_x)
                fitter.addConstraint(cons_y)

                fitter.setMaxNbIter(30)
                fitter.setMaxDeltaS(1e-2)
                fitter.setMaxF(1e-1)
                fitter.setVerbosity(3)

                # run the fit
                kinfit_fit = fitter.fit() + 1  # 0: not run; 1: fit converged; 2: fit didn't converge
                kinfit_getNDF = fitter.getNDF()
                kinfit_getS = fitter.getS()
                kinfit_getF = fitter.getF()
                #print("-"*10, kinfit_fit, kinfit_getNDF, kinfit_getS, kinfit_getF)

                # higgs jet output vectors
                fit_result_j1 = fitter.get4Vec(0)
                fit_result_j2 = fitter.get4Vec(1)
                fit_result_H = fit_result_j1 + fit_result_j2

                fit_result_l1 = fitter.get4Vec(2)
                fit_result_l2 = fitter.get4Vec(3)
                fit_result_V = fit_result_l1 + fit_result_l2

                self._b(self.bDict[syst]['H_pt_fit'])[0] = fit_result_H.Pt() if kinfit_fit == 1 else tree.H_pt
                self._b(self.bDict[syst]['H_eta_fit'])[0] = fit_result_H.Eta() if kinfit_fit == 1 else tree.H_eta
                self._b(self.bDict[syst]['H_phi_fit'])[0] = fit_result_H.Phi() if kinfit_fit == 1 else tree.H_phi
                self._b(self.bDict[syst]['H_mass_fit'])[0] = fit_result_H.M() if kinfit_fit == 1 else tree.H_mass
                self._b(self.bDict[syst]['V_pt_fit'])[0] = fit_result_V.Pt() if kinfit_fit == 1 else tree.V_pt
                self._b(self.bDict[syst]['V_eta_fit'])[0] = fit_result_V.Eta() if kinfit_fit == 1 else tree.V_eta
                self._b(self.bDict[syst]['V_phi_fit'])[0] = fit_result_V.Phi() if kinfit_fit == 1 else tree.V_phi
                self._b(self.bDict[syst]['V_mass_fit'])[0] = fit_result_V.M() if kinfit_fit == 1 else tree.V_mass

                self._b(self.bDict[syst]['HVdPhi_fit'])[0] = abs(fit_result_H.Phi() - fit_result_V.Phi()) if kinfit_fit == 1 else abs(tree.H_phi - tree.V_phi)
                self._b(self.bDict[syst]['jjVPtRatio_fit'])[0] = fit_result_H.Pt()/fit_result_V.Pt() if kinfit_fit == 1 else tree.H_pt/tree.V_pt
                self._b(self.bDict[syst]['hJets_pt_0_fit'])[0] = fit_result_j1.Pt()
                self._b(self.bDict[syst]['hJets_pt_1_fit'])[0] = fit_result_j2.Pt()

                self._b(self.bDict[syst]['status'])[0] = kinfit_fit
                self._b(self.bDict[syst]['n_recoil_jets_fit'])[0] = len(recoil_jets)

                # higgs mass uncertainty
                cov_fit = fitter.getCovMatrixFit()
                dmH_by_dpt1 = ( (fit_result_H.X())*np.cos(fit_result_j1.Phi()) + (fit_result_H.Y())*np.sin(fit_result_j1.Phi()) )/fit_result_H.M()
                dmH_by_dpt2 = ( (fit_result_H.X())*np.cos(fit_result_j2.Phi()) + (fit_result_H.Y())*np.sin(fit_result_j2.Phi()) )/fit_result_H.M()
                self._b(self.bDict[syst]['H_mass_sigma_fit'])[0] = ( dmH_by_dpt1**2          * cov_fit(0,0)
                                        + dmH_by_dpt2**2          * cov_fit(3,3)
                                        + dmH_by_dpt1*dmH_by_dpt2 * cov_fit(0,3) )**.5 if kinfit_fit == 1 else -1.0

