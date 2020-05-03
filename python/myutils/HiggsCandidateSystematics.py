#!/usr/bin/env python
import ROOT
import array
import os
import math
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule

# propagate JES/JER systematics from jets to higgs candidate dijet pair 
class HiggsCandidateSystematics(AddCollectionsModule):
    
    def __init__(self, addSystematics=True, prefix="H", addBoostSystematics=False, addMinMax=False, puIdCut=6, jetIdCut=4):
        super(HiggsCandidateSystematics, self).__init__()
        self.version = 1
        self.debug = 'XBBDEBUG' in os.environ
        self.nJet = -1
        self.nJetMax = 100
        self.addSystematics = addSystematics
        self.addMinMax = addMinMax
        self.prefix = prefix
        self.addBoostSystematics = addBoostSystematics
        self.puIdCut = puIdCut
        self.jetIdCut = jetIdCut

        self.jetSystematicsResolved = ['jer','jerReg','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesTotal']

        self.jetSystematics = self.jetSystematicsResolved[:]

        # corrected dijet (Higgs candidate) properties
        self.higgsProperties = [self.prefix + '_' + x for x in ['pt','eta', 'phi', 'mass','pt_noFSR','eta_noFSR','phi_noFSR','mass_noFSR']]

        # included JEC and JER systematic for msoftdrop
        if self.addBoostSystematics: 
            self.higgsProperties +=['FatJet_msoftdrop_sys', 'FatJet_pt_sys']
            #self.higgsProperties +=['FatJet_msoftdrop_sys']
            # adding mass scale and resolution systematics
            self.rnd = ROOT.TRandom3(12345)

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']

        #jerReg systematics not included in nanoAOD v4 for 2016 dataset.
        self.dataset = self.config.get('General', 'dataset')
        #if self.dataset == '2016':
        #    self.jetSystematics.remove('jerReg')

        if self.addBoostSystematics:
            self.boosttagidx = 'Hbb_fjidx'
            self.msoftdrop = 'FatJet_msoftdrop'
            if self.sample.type != 'DATA':
                self.FatJet_pt= 'FatJet_pt_nom'
            else: 
                self.FatJet_pt= 'FatJet_pt'
            # get all the info for scale and smearing
            self.Snom   = eval(self.config.get('Sys', 'Snom'))
            self.Sdown  = eval(self.config.get('Sys', 'Sdown'))
            self.Sup    = eval(self.config.get('Sys', 'Sup'))
            self.Rnom   = eval(self.config.get('Sys', 'Rnom'))
            self.Rdown  = eval(self.config.get('Sys', 'Rdown'))
            self.Rup    = eval(self.config.get('Sys', 'Rup'))

            #Load .root file with resolution.
            self.jetSystematics+= ['jms']
            self.jetSystematics+= ['jmr']
            self.config = initVars['config']
            wdir = self.config.get('Directories', 'vhbbpath')
            filejmr = ROOT.TFile.Open(wdir+"/python/data/softdrop/puppiSoftdropResol.root","READ")
            self.puppisd_resolution_cen = filejmr.Get("massResolution_0eta1v3")
            self.puppisd_resolution_for = filejmr.Get("massResolution_1v3eta2v5")

            ## adding jms and jmr to FatJet pt
            for syst in ['_jmr','_jms']:
                for p in ['Jet_pt', 'Jet_mass']:
                    for q in ['Up', 'Down']:
                        print 'name is',p+syst+q
                        self.branchBuffers[p+syst+q] = array.array('f', [0.0]*self.nJetMax)
                        self.branches.append({'name': p+syst+q, 'formula': self.getVectorBranch, 'arguments': {'branch': p+syst+q}, 'length': self.nJetMax, 'leaflist': p+syst+q+'[nJet]/F'})

        # they will be filled with the nominal... 
        for syst in ['jmr','jms','jerReg']:
            for Q in ['Up', 'Down']:
                self.addBranch('MET_pt_{s}{d}'.format(s=syst, d=Q))
                self.addBranch('MET_phi_{s}{d}'.format(s=syst, d=Q))

        ## adding dummy MET branches with jer and jes
        if self.addMinMax:
            self.addBranch('MET_pt_minmaxUp')
            self.addBranch('MET_pt_minmaxDown')
            self.addBranch('MET_phi_minmaxUp')
            self.addBranch('MET_phi_minmaxDown')

        self.tagidx = self.config.get('General', 'hJidx')
        if self.debug:
            print "DEBUG: HiggsCandidateSystematics::__init__(), with idx=", self.tagidx, " prefix=", self.prefix

        # nominal + systematic variations
        self.systematicsResolved = [None]
        if self.sample.isMC():
            self.systematicsResolved += self.jetSystematicsResolved

        # dijet H candidate branches
        for higgsProperty in self.higgsProperties: 
            for syst in self.systematicsResolved:
                for Q in self._variations(syst):
                    self.addBranch(self._v(higgsProperty, syst, Q))

        # additional jet branches
        fBranches = ['hJets_0_pt_noFSR','hJets_1_pt_noFSR','hJets_0_pt_FSRrecovered','hJets_1_pt_FSRrecovered','hJets_FSRrecovered_dEta','hJets_FSRrecovered_dPhi']
        for syst in self.systematicsResolved:
            for Q in self._variations(syst):
                for branchName in fBranches:
                    self.addBranch(self._v(branchName, syst, Q))
                self.addIntegerBranch(self._v('nFSRrecovered', syst, Q))

    # read from buffers which have been filled in processEvent()    
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        length = min(self.nJet, self.nJetMax)
        destinationArray[:length] = self.branchBuffers[arguments['branch']][:length]

    def getResolvedJetIndicesFromTree(self, tree, syst=None, UD=None):
        indexNameSyst = (self.tagidx + '_' + syst + UD) if not self._isnominal(syst) else self.tagidx
        if hasattr(tree, indexNameSyst):
            self.count('_debug_resolved_idx_syst_exists')
            return getattr(tree, indexNameSyst)
        else:
            self.count('_debug_resolved_idx_fallback_nom')
            return getattr(tree, self.tagidx)

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            # ----------------------------------------------------------------------------------------------------
            # RESOLVED 
            # ----------------------------------------------------------------------------------------------------

            # select branches from tree
            # for 2016 nano >= v5 needed!
            Jet_PtReg_nom = tree.Jet_PtReg 
            Jet_pt_nom    = tree.Jet_Pt
            Jet_phi       = tree.Jet_phi
            Jet_eta       = tree.Jet_eta
            Jet_puId      = tree.Jet_puId
            Jet_jetId     = tree.Jet_jetId
            Jet_lepFilter = tree.Jet_lepFilter
            nJet          = tree.nJet

            # alias for jet mass
            if self.sample.isMC():
                Jet_mass_nom = tree.Jet_mass_nom
            else:
<<<<<<< HEAD
                treeJet_mass_nom = tree.Jet_mass
                treeJet_mass = tree.Jet_mass

            # in case of boosted analysis (there aren't two resolved jets)
            if not (hJidx0 > -1 and hJidx1 > -1):
                pass
            else:
                # nominal value
                hJ0 = ROOT.TLorentzVector()
                hJ1 = ROOT.TLorentzVector()

                # for Higgs candidate jets use b-regression
                hJ0.SetPtEtaPhiM(treeJet_PtReg[hJidx0], treeJet_eta[hJidx0], treeJet_phi[hJidx0], treeJet_mass_nom[hJidx0] * treeJet_PtReg[hJidx0]/treeJet_Pt[hJidx0])
                hJ1.SetPtEtaPhiM(treeJet_PtReg[hJidx1], treeJet_eta[hJidx1], treeJet_phi[hJidx1], treeJet_mass_nom[hJidx1] * treeJet_PtReg[hJidx1]/treeJet_Pt[hJidx1])

                dijet_Nominal_noFSR = hJ0 + hJ1

                self.branchBuffers['hJets_0_pt_noFSR'][0] = hJ0.Pt()
                self.branchBuffers['hJets_1_pt_noFSR'][0] = hJ1.Pt()
                
                self.branchBuffers[self.prefix + '_pt_noFSR'][0]   = dijet_Nominal_noFSR.Pt()
                self.branchBuffers[self.prefix + '_eta_noFSR'][0]  = dijet_Nominal_noFSR.Eta()
                self.branchBuffers[self.prefix + '_phi_noFSR'][0]  = dijet_Nominal_noFSR.Phi()
                self.branchBuffers[self.prefix + '_mass_noFSR'][0] = dijet_Nominal_noFSR.M()
                
                # save information which FSR jets have been added for nominal
                fsrIndices0 = []
                fsrIndices1 = []

                # FSR recovery
                for i in range(len(treeJet_PtReg)):
                    if i not in [hJidx0, hJidx1] and treeJet_Pt[i]>20 and abs(tree.Jet_eta[i])<3.0 and (tree.Jet_puId[i]>self.puIdCut or tree.Jet_Pt[i]>50.0) and tree.Jet_lepFilter[i] > 0 and tree.Jet_jetId[i] > self.jetIdCut:
                        FSR = ROOT.TLorentzVector()
                        FSR.SetPtEtaPhiM(treeJet_Pt[i],treeJet_eta[i],treeJet_phi[i],treeJet_mass_nom[i])
                        deltaR0 = FSR.DeltaR(hJ0)
                        deltaR1 = FSR.DeltaR(hJ1)
                        if min(deltaR0,deltaR1) < 0.8:
                            if deltaR0<deltaR1:
                                hJ0 = hJ0 + FSR
                                fsrIndices0.append(i)
                            else:
                                hJ1 = hJ1 + FSR
                                fsrIndices1.append(i)

                dijet_Nominal = hJ0 + hJ1
                self.branchBuffers[self.prefix + '_pt'][0] = dijet_Nominal.Pt()
                self.branchBuffers[self.prefix + '_eta'][0] = dijet_Nominal.Eta()
                self.branchBuffers[self.prefix + '_phi'][0] = dijet_Nominal.Phi()
                self.branchBuffers[self.prefix + '_mass'][0] = dijet_Nominal.M()

                self.branchBuffers['hJets_0_pt_FSRrecovered'][0] = hJ0.Pt()
                self.branchBuffers['hJets_1_pt_FSRrecovered'][0] = hJ1.Pt()
                self.branchBuffers['hJets_FSRrecovered_dEta'][0] = abs(hJ0.Eta()-hJ1.Eta())
                self.branchBuffers['hJets_FSRrecovered_dPhi'][0] = abs(hJ0.DeltaPhi(hJ1))
                self.branchBuffers['nFSRrecovered'][0] = len(fsrIndices0) + len(fsrIndices1)

            # systematics
            valueList = {x:[self.branchBuffers[x][0]] for x in self.higgsProperties}
            if self.addSystematics and self.sample.type != 'DATA':
                for syst in self.jetSystematics:
                    for Q in ['Up', 'Down']:
                        if self.sample.type != 'DATA':
                            # included JEC and JER systematic for msoftdrop
                            if self.addBoostSystematics  and boosttagidx > -1: 
                                if syst == 'jmr' or syst == 'jms':
                                    pass
                                else:
                                    msoftdrop_sys = msoftdrop*getattr(tree, 'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx]/getattr(tree, 'FatJet_pt_nom')[boosttagidx]
                                    FatJet_pt_sys = getattr(tree, 'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx]
                            if tree.Hbb_fjidx > -1:
                                if syst == 'jmr':
                                    self.jmr_sys = self.get_msoftdrop_smear(tree.FatJet_pt[tree.Hbb_fjidx], tree.FatJet_eta[tree.Hbb_fjidx])
                                elif syst == 'jms':
                                    pass
                            # nothing to compute if no resolved jet
                            if not (hJidx0 > -1 and hJidx1 > -1):
                                pass
                            else:
                                hJ0 = ROOT.TLorentzVector()
                                hJ1 = ROOT.TLorentzVector()

                                if syst == 'jmr' or syst == 'jms':
                                    pass
                                elif syst == 'jerReg':
                                    treeJet_PtRegSys = getattr(tree,'Jet_PtReg'+Q)
                                    # vary the regression for the regression systematic
                                    #  pt_reg_var   = pt_reg_var 
                                    #  mass_reg_var = mass_nom * pt_reg_var / pt_nom
                                    hJ0.SetPtEtaPhiM(treeJet_PtRegSys[hJidx0], treeJet_eta[hJidx0], treeJet_phi[hJidx0], treeJet_mass_nom[hJidx0]*treeJet_PtRegSys[hJidx0]/treeJet_Pt[hJidx0])
                                    hJ1.SetPtEtaPhiM(treeJet_PtRegSys[hJidx1], treeJet_eta[hJidx1], treeJet_phi[hJidx1], treeJet_mass_nom[hJidx1]*treeJet_PtRegSys[hJidx1]/treeJet_Pt[hJidx1])
                                else:
                                    treeJet_mass_sys = getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))
                                    treeJet_pt_sys   = getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))

                                    regressionFactor0 = treeJet_PtReg[hJidx0]/treeJet_Pt[hJidx0]
                                    regressionFactor1 = treeJet_PtReg[hJidx1]/treeJet_Pt[hJidx1]

                                    hJ0.SetPtEtaPhiM(treeJet_pt_sys[hJidx0]*regressionFactor0, treeJet_eta[hJidx0], treeJet_phi[hJidx0], treeJet_mass_sys[hJidx0]*regressionFactor0) 
                                    hJ1.SetPtEtaPhiM(treeJet_pt_sys[hJidx1]*regressionFactor1, treeJet_eta[hJidx1], treeJet_phi[hJidx1], treeJet_mass_sys[hJidx1]*regressionFactor1)

                                dijet_noFSR = hJ0 + hJ1

                                # FSR recovery for systematic variations
                                #  the same jets are recovered as for nominal, but with variation applied
                                for i in fsrIndices0:
                                    FSR = ROOT.TLorentzVector()
                                    if syst == 'jmr' or syst == 'jms':
                                        pass
                                    elif syst == 'jerReg':
                                        FSR.SetPtEtaPhiM(treeJet_Pt[i], treeJet_eta[i], treeJet_phi[i], treeJet_mass_nom[i])
                                    else:
                                        FSR.SetPtEtaPhiM(treeJet_pt_sys[i], treeJet_eta[i], treeJet_phi[i], treeJet_mass_sys[i])
                                    hJ0 = hJ0 + FSR
                                for i in fsrIndices1:
                                    FSR = ROOT.TLorentzVector()
                                    if syst == 'jmr' or syst == 'jms':
                                        pass
                                    elif syst == 'jerReg':
                                        FSR.SetPtEtaPhiM(treeJet_Pt[i], treeJet_eta[i], treeJet_phi[i], treeJet_mass_nom[i])
                                    else:
                                        FSR.SetPtEtaPhiM(treeJet_pt_sys[i], treeJet_eta[i], treeJet_phi[i], treeJet_mass_sys[i])
                                    hJ1 = hJ1 + FSR
                                
                                dijet = hJ0 + hJ1
                        else:
                            dijet_noFSR = dijet_Nominal_noFSR
                            dijet = dijet_Nominal

                        if self.addBoostSystematics  and boosttagidx > -1: 
                            #print FatJet_pt
                            #import sys
                            #sys.exit()
                            if syst == 'jmr':
                                if Q == 'Up':
                                    self.branchBuffers['FatJet_msoftdrop_sys_jmr_Down'][0]   = msoftdrop*self.jmr_sys[0]
                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.jmr_sys[0])

                                    # no sys variation on pT (put nominal value)
                                    self.branchBuffers['FatJet_pt_sys_jmr_Down'][0]   = FatJet_pt
                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
                                elif Q == 'Down':
                                    self.branchBuffers['FatJet_msoftdrop_sys_jmr_Up'][0]     = msoftdrop*self.jmr_sys[1]
                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.jmr_sys[1])

                                    # no sys variation on pT (put nominal value)
                                    self.branchBuffers['FatJet_pt_sys_jmr_Up'][0]     = FatJet_pt
                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
                            elif syst == 'jms':
                                if Q == 'Up':
                                    self.branchBuffers['FatJet_msoftdrop_sys_jms_Up'][0]     = msoftdrop*self.Sup
                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.Sup)

                                    # no sys variation on pT (put nominal value)
                                    self.branchBuffers['FatJet_pt_sys_jms_Up'][0]     = FatJet_pt
                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
                                elif Q == 'Down':
                                    self.branchBuffers['FatJet_msoftdrop_sys_jms_Down'][0]   = msoftdrop*self.Sdown
                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.Sdown)

                                    # no sys variation on pT (put nominal value)
                                    self.branchBuffers['FatJet_pt_sys_jms_Down'][0]   = FatJet_pt
                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
                            else:
                                self.branchBuffers['FatJet_msoftdrop_sys_{s}_{d}'.format(s=syst, d=Q)][0] = msoftdrop_sys
                                valueList['FatJet_msoftdrop_sys'].append(msoftdrop_sys)

                                ##valueList['FatJet_pt_sys'].append(getattr(tree,'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx])
                                #print 'FatJet_pt_sys', FatJet_pt_sys
                                #import sys
                                #sys.exit()
                                self.branchBuffers['FatJet_pt_sys_{s}_{d}'.format(s=syst, d=Q)][0] = FatJet_pt_sys
                                valueList['FatJet_pt_sys'].append(FatJet_pt_sys)


                        if not (hJidx0 > -1 and hJidx1 > -1):
                            pass
=======
                Jet_mass_nom = tree.Jet_mass

            for syst in self.systematicsResolved:
                for Q in self._variations(syst):

                    hJ0 = ROOT.TLorentzVector()
                    hJ1 = ROOT.TLorentzVector()

                    # check if there are TWO resolved jets
                    hJidx0, hJidx1 = self.getResolvedJetIndicesFromTree(tree, syst, Q)
                    if hJidx0 > -1 and hJidx1 > -1:

                        # Pt, Mass:       with JEC, JER
                        # PtReg, MassReg: with JEC, JER, regression+smearing
                        if self._isnominal(syst):
                            Jet_Pt      = Jet_pt_nom
                            Jet_PtReg   = Jet_PtReg_nom
                            Jet_Mass    = Jet_mass_nom
                            Jet_MassReg = [Jet_Mass[i] * Jet_PtReg_nom[i]/Jet_pt_nom[i] for i in range(nJet)]
                        elif syst == 'jerReg':
                            Jet_Pt      = Jet_pt_nom
                            Jet_PtReg   = getattr(tree, 'Jet_PtReg'+Q)
                            Jet_Mass    = Jet_mass_nom
                            Jet_MassReg = [Jet_Mass[i] * Jet_PtReg[i]/Jet_pt_nom[i] for i in range(nJet)]
>>>>>>> ad31d884050ccef2ece2859278f6bc8fa51502ae
                        else:
                            Jet_Pt      = getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))
                            Jet_PtReg   = [Jet_Pt[i] * Jet_PtReg_nom[i]/Jet_pt_nom[i] for i in range(nJet)]
                            Jet_Mass    = getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))
                            Jet_MassReg = [Jet_Mass[i] * Jet_PtReg_nom[i]/Jet_pt_nom[i] for i in range(nJet)]

                        # b-jet regression is applied to H candidate jets
                        hJ0.SetPtEtaPhiM(Jet_PtReg[hJidx0], Jet_eta[hJidx0], Jet_phi[hJidx0], Jet_MassReg[hJidx0])
                        hJ1.SetPtEtaPhiM(Jet_PtReg[hJidx1], Jet_eta[hJidx1], Jet_phi[hJidx1], Jet_MassReg[hJidx1])

                        self._b(self._v('hJets_0_pt_noFSR', syst, Q))[0] = hJ0.Pt()
                        self._b(self._v('hJets_1_pt_noFSR', syst, Q))[0] = hJ1.Pt()

                        dijet_noFSR = hJ0 + hJ1
                        self._b(self._v(self.prefix + '_pt_noFSR', syst, Q))[0]   = dijet_noFSR.Pt()
                        self._b(self._v(self.prefix + '_eta_noFSR', syst, Q))[0]  = dijet_noFSR.Eta()
                        self._b(self._v(self.prefix + '_phi_noFSR', syst, Q))[0]  = dijet_noFSR.Phi()
                        self._b(self._v(self.prefix + '_mass_noFSR', syst, Q))[0] = dijet_noFSR.M()

                        # save information which FSR jets have been added
                        fsrIndices0 = []
                        fsrIndices1 = []

                        # FSR recovery
                        for i in range(nJet):
                            if i not in [hJidx0, hJidx1]:
                                if Jet_Pt[i] > 20.0 and abs(Jet_eta[i]) < 3.0 and (Jet_puId[i] > 6 or Jet_Pt[i] > 50.0) and Jet_lepFilter[i] > 0:

                                    # b-jet regression is not applied to FSR jets
                                    FSR = ROOT.TLorentzVector()
                                    FSR.SetPtEtaPhiM(Jet_Pt[i], Jet_eta[i], Jet_phi[i], Jet_Mass[i])

                                    deltaR0 = FSR.DeltaR(hJ0)
                                    deltaR1 = FSR.DeltaR(hJ1)
                                    if min(deltaR0, deltaR1) < 0.8:
                                        if deltaR0<deltaR1:
                                            hJ0 = hJ0 + FSR
                                            fsrIndices0.append(i)
                                        else:
                                            hJ1 = hJ1 + FSR
                                            fsrIndices1.append(i)

                        # H with FSR recovery
                        dijet = hJ0 + hJ1
                        self._b(self._v(self.prefix + '_pt', syst, Q))[0]   = dijet.Pt()
                        self._b(self._v(self.prefix + '_eta', syst, Q))[0]  = dijet.Eta()
                        self._b(self._v(self.prefix + '_phi', syst, Q))[0]  = dijet.Phi()
                        self._b(self._v(self.prefix + '_mass', syst, Q))[0] = dijet.M()

                        # write additional jet quantities after FSR recovery
                        self._b(self._v('hJets_0_pt_FSRrecovered', syst, Q))[0] = hJ0.Pt()
                        self._b(self._v('hJets_1_pt_FSRrecovered', syst, Q))[0] = hJ1.Pt()

                        self._b(self._v('hJets_FSRrecovered_dEta', syst, Q))[0] = abs(hJ0.Eta()-hJ1.Eta()) 
                        self._b(self._v('hJets_FSRrecovered_dPhi', syst, Q))[0] = abs(hJ0.DeltaPhi(hJ1))

                        self._b(self._v('nFSRrecovered', syst, Q))[0] = len(fsrIndices0) + len(fsrIndices1)

# jmr/jms taken from post-processor
#            # ----------------------------------------------------------------------------------------------------
#            # BOOSTED
#            # ----------------------------------------------------------------------------------------------------
#            
#            if self.addBoostSystematics:
#                boosttagidx = getattr(tree, self.boosttagidx)
#                if boosttagidx > -1:
#                    FatJet_pt = getattr(tree, self.FatJet_pt)[boosttagidx]
#                    msoftdrop   = getattr(tree, self.msoftdrop)[boosttagidx]
#                    self._b('FatJet_msoftdrop_sys')[0] = msoftdrop
#                    self._b('FatJet_pt_sys')[0]        = FatJet_pt
#                    #print FatJet_pt
#                    #print msoftdrop
#                    #import sys
#                    #sys.exit()
#            
#            # systematics
#            valueList = {x:[self.branchBuffers[x][0]] for x in self.higgsProperties}
#            if self.addSystematics and self.sample.type != 'DATA':
#                for syst in self.jetSystematics:
#                    for Q in ['Up', 'Down']:
#                        if self.sample.type != 'DATA':
#                            # included JEC and JER systematic for msoftdrop
#                            if self.addBoostSystematics  and boosttagidx > -1: 
#                                if syst == 'jmr' or syst == 'jms':
#                                    pass
#                                else:
#                                    msoftdrop_sys = msoftdrop*getattr(tree, 'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx]/getattr(tree, 'FatJet_pt_nom')[boosttagidx]
#                                    FatJet_pt_sys = getattr(tree, 'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx]
#                            if tree.Hbb_fjidx > -1:
#                                if syst == 'jmr':
#                                    self.jmr_sys = self.get_msoftdrop_smear(tree.FatJet_pt[tree.Hbb_fjidx], tree.FatJet_eta[tree.Hbb_fjidx])
#                                elif syst == 'jms':
#                                    pass
#
#                        if self.addBoostSystematics  and boosttagidx > -1: 
#                            #print FatJet_pt
#                            #import sys
#                            #sys.exit()
#                            if syst == 'jmr':
#                                if Q == 'Up':
#                                    self.branchBuffers['FatJet_msoftdrop_sys_jmr_Down'][0]   = msoftdrop*self.jmr_sys[0]
#                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.jmr_sys[0])
#
#                                    # no sys variation on pT (put nominal value)
#                                    self.branchBuffers['FatJet_pt_sys_jmr_Down'][0]   = FatJet_pt
#                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
#                                elif Q == 'Down':
#                                    self.branchBuffers['FatJet_msoftdrop_sys_jmr_Up'][0]     = msoftdrop*self.jmr_sys[1]
#                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.jmr_sys[1])
#
#                                    # no sys variation on pT (put nominal value)
#                                    self.branchBuffers['FatJet_pt_sys_jmr_Up'][0]     = FatJet_pt
#                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
#                            elif syst == 'jms':
#                                if Q == 'Up':
#                                    self.branchBuffers['FatJet_msoftdrop_sys_jms_Up'][0]     = msoftdrop*self.Sup
#                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.Sup)
#
#                                    # no sys variation on pT (put nominal value)
#                                    self.branchBuffers['FatJet_pt_sys_jms_Up'][0]     = FatJet_pt
#                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
#                                elif Q == 'Down':
#                                    self.branchBuffers['FatJet_msoftdrop_sys_jms_Down'][0]   = msoftdrop*self.Sdown
#                                    valueList['FatJet_msoftdrop_sys'].append(msoftdrop*self.Sdown)
#
#                                    # no sys variation on pT (put nominal value)
#                                    self.branchBuffers['FatJet_pt_sys_jms_Down'][0]   = FatJet_pt
#                                    valueList['FatJet_pt_sys'].append(FatJet_pt)
#                            else:
#                                self.branchBuffers['FatJet_msoftdrop_sys_{s}_{d}'.format(s=syst, d=Q)][0] = msoftdrop_sys
#                                valueList['FatJet_msoftdrop_sys'].append(msoftdrop_sys)
#
#                                ##valueList['FatJet_pt_sys'].append(getattr(tree,'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx])
#                                #print 'FatJet_pt_sys', FatJet_pt_sys
#                                #import sys
#                                #sys.exit()
#                                self.branchBuffers['FatJet_pt_sys_{s}_{d}'.format(s=syst, d=Q)][0] = FatJet_pt_sys
#                                valueList['FatJet_pt_sys'].append(FatJet_pt_sys)

        return True

    def get_msoftdrop_smear(self, pt, eta):

        #get mass resolution
        massResolution = 0
        # version1: added abs() wrt previous version 0
        if abs(eta) <= 1.3:
            massResolution = self.puppisd_resolution_cen.Eval(pt)
        else: 
            massResolution = self.puppisd_resolution_for.Eval(pt)

        ###
        cup     = 1.
        cdown   = 1.
        r       = self.rnd.Gaus(0, massResolution - 1) 

        cup     = 1. + r*math.sqrt(max(self.Rup**2-1,0))
        cdown   = 1. + r*math.sqrt(max(self.Rdown**2-1,0))

        return [cdown, cup]




