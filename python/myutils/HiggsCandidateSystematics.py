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
        self.debug = 'XBBDEBUG' in os.environ
        self.lastEntry = -1
        self.nJet = -1
        self.nJetMax = 100
        self.addSystematics = addSystematics
        self.addMinMax = addMinMax
        self.prefix = prefix
        self.addBoostSystematics = addBoostSystematics
        self.puIdCut = puIdCut
        self.jetIdCut = jetIdCut

        #self.jetSystematics = ['jer','jerReg','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesTotal']
        self.jetSystematics = ['jerReg']

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

        self.higgsPropertiesWithSys = self.higgsProperties if self.sample.type != 'DATA' else []
        for higgsProperty in self.higgsProperties: 
            self.addBranch(higgsProperty)
            
            # for data only include the min/max (set to nominal) to simplify cutting
            systList = self.jetSystematics if higgsProperty in self.higgsPropertiesWithSys else []
            if self.addMinMax:
                systList += ['minmax']

            for syst in systList:
                for Q in ['Up', 'Down']:
                    higgsPropertySyst = "{p}_{s}_{q}".format(p=higgsProperty, s=syst, q=Q)
                    #if higgsProperty != 'FatJet_pt':
                    #    higgsPropertySyst = "{p}_{s}_{q}".format(p=higgsProperty, s=syst, q=Q)
                    #else:
                    #    higgsPropertySyst = "{p}_{s}{q}".format(p=higgsProperty, s=syst, q=Q)
                    self.addBranch(higgsPropertySyst)

        self.addBranch('hJets_0_pt_noFSR')
        self.addBranch('hJets_1_pt_noFSR')
        self.addBranch('hJets_0_pt_FSRrecovered')
        self.addBranch('hJets_1_pt_FSRrecovered')
        self.addBranch('hJets_FSRrecovered_dEta')
        self.addBranch('hJets_FSRrecovered_dPhi')
        self.addIntegerBranch('nFSRrecovered')

        for syst in self.jetSystematics:
            for Q in ['Up', 'Down']:
                self.addBranch('hJets_0_pt_FSRrecovered_{s}_{q}'.format(s=syst, q=Q))
                self.addBranch('hJets_1_pt_FSRrecovered_{s}_{q}'.format(s=syst, q=Q))
                self.addBranch('hJets_FSRrecovered_dEta_{s}_{q}'.format(s=syst, q=Q))
                self.addBranch('hJets_FSRrecovered_dPhi_{s}_{q}'.format(s=syst, q=Q))

        if self.addMinMax:
            for p in ['Jet_pt_minmax', 'Jet_mass_minmax']:
                for q in ['Up', 'Down']:
                    self.branchBuffers[p+q] = array.array('f', [0.0]*self.nJetMax)
                    self.branches.append({'name': p+q, 'formula': self.getVectorBranch, 'arguments': {'branch': p+q}, 'length': self.nJetMax, 'leaflist': p+q+'[nJet]/F'})
                    ## wrong values when using this. Use two lines above instead.
                    #self.addVectorBranch(p+q, length=self.nJetMax, leaflist=p+q+'[nJet]/F')

    # read from buffers which have been filled in processEvent()    
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        length = min(self.nJet, self.nJetMax)
        destinationArray[:length] = self.branchBuffers[arguments['branch']][:length]

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)


            if self.addBoostSystematics:
                boosttagidx = getattr(tree, self.boosttagidx)
                if boosttagidx > -1:
                    FatJet_pt = getattr(tree, self.FatJet_pt)[boosttagidx]
                    msoftdrop   = getattr(tree, self.msoftdrop)[boosttagidx]
                    self.branchBuffers['FatJet_msoftdrop_sys'][0] = msoftdrop
                    self.branchBuffers['FatJet_pt_sys'][0] = FatJet_pt
                    #print FatJet_pt
                    #print msoftdrop
                    #import sys
                    #sys.exit()

            # idx passed as an argument
            if self.tagidx:
                #print "Using the {idx}".format(idx=self.tagidx)
                hJidx0 = getattr(tree,self.tagidx)[0] 
                hJidx1 = getattr(tree,self.tagidx)[1]
                #print "tag0 {t0} and tag1 {t1}".format(t0=hJidx0,t1=hJidx1) 
            else:
                print "Missing bTag index. Check general.ini"
                raise Exception("bTagIndexNotSpecified")

            # select branches from tree
            # for 2016 nano v5
            treeJet_PtReg = tree.Jet_PtReg 
            treeJet_pt = tree.Jet_pt
            treeJet_Pt = tree.Jet_Pt
            #treeJet_bReg = tree.Jet_bReg

            treeJet_phi = tree.Jet_phi
            treeJet_eta = tree.Jet_eta

            if self.sample.type != 'DATA':
                treeJet_mass_nom = tree.Jet_mass_nom
                treeJet_mass = tree.Jet_mass
            else:
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
                        else:
                            self.branchBuffers[self.prefix + '_pt_{s}_{d}'.format(s=syst, d=Q)][0]   = dijet.Pt()
                            self.branchBuffers[self.prefix + '_eta_{s}_{d}'.format(s=syst, d=Q)][0]  = dijet.Eta()
                            self.branchBuffers[self.prefix + '_phi_{s}_{d}'.format(s=syst, d=Q)][0]  = dijet.Phi()
                            self.branchBuffers[self.prefix + '_mass_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.M()
                            
                            self.branchBuffers[self.prefix + '_pt_noFSR_{s}_{d}'.format(s=syst, d=Q)][0]   = dijet_noFSR.Pt()
                            self.branchBuffers[self.prefix + '_eta_noFSR_{s}_{d}'.format(s=syst, d=Q)][0]  = dijet_noFSR.Eta()
                            self.branchBuffers[self.prefix + '_phi_noFSR_{s}_{d}'.format(s=syst, d=Q)][0]  = dijet_noFSR.Phi()
                            self.branchBuffers[self.prefix + '_mass_noFSR_{s}_{d}'.format(s=syst, d=Q)][0] = dijet_noFSR.M()
                            
                            self.branchBuffers['hJets_0_pt_FSRrecovered_{s}_{d}'.format(s=syst, d=Q)][0] = hJ0.Pt()
                            self.branchBuffers['hJets_1_pt_FSRrecovered_{s}_{d}'.format(s=syst, d=Q)][0] = hJ1.Pt()
                            self.branchBuffers['hJets_FSRrecovered_dEta_{s}_{d}'.format(s=syst, d=Q)][0] = abs(hJ0.Eta()-hJ1.Eta())
                            self.branchBuffers['hJets_FSRrecovered_dPhi_{s}_{d}'.format(s=syst, d=Q)][0] = abs(hJ0.DeltaPhi(hJ1))

                            if self.addMinMax:
                                # add to the list for min/max
                                valueList[self.prefix + '_pt'].append(dijet.Pt())
                                valueList[self.prefix + '_eta'].append(dijet.Eta())
                                valueList[self.prefix + '_phi'].append(dijet.Phi())
                                valueList[self.prefix + '_mass'].append(dijet.M())

                                ## add to the list for min/max
                                valueList[self.prefix + '_pt_noFSR'].append(dijet.Pt())
                                valueList[self.prefix + '_eta_noFSR'].append(dijet.Eta())
                                valueList[self.prefix + '_phi_noFSR'].append(dijet.Phi())
                                valueList[self.prefix + '_mass_noFSR'].append(dijet.M())

            if self.addMinMax:
                # get minimum and maximum variation
                for syst in ['minmax']:
                    for Q in ['Up', 'Down']:
                        for p in self.higgsProperties:
                            #if p == 'FatJet_msoftdrop_sys':
                                #print valueList['FatJet_msoftdrop_sys'] 
                                self.branchBuffers['{p}_{s}_{d}'.format(p=p, s=syst, d=Q)][0] = min(valueList[p]) if Q=='Down' else max(valueList[p])
                            #if not p == 'FatJet_pt':
                            #    self.branchBuffers['{p}_{s}_{d}'.format(p=p, s=syst, d=Q)][0] = min(valueList[p]) if Q=='Down' else max(valueList[p])
                            #else:
                            #    print valueList[p]
                            #    self.branchBuffers['{p}_{s}{d}'.format(p=p, s=syst, d=Q)][0] = min(valueList[p]) if Q=='Down' else max(valueList[p])

                # min/max variations for Jet pt/mass
                self.nJet = tree.nJet
                treeJet_mass_sys = {}
                treeJet_pt_sys = {}
                if self.addSystematics and self.sample.type != 'DATA':
                    # read all the arrays once to avoid getattr in the loop over the jets
                    for syst in self.jetSystematics:
                        for Q in ['Up', 'Down']:
                            if syst == 'jerReg':
                                treeJet_mass_sys[syst+Q] = treeJet_mass 
                                treeJet_pt_sys[syst+Q] = treeJet_Pt
                            elif syst == 'jmr' or syst == 'jms':
                                # nominal values (as jmr and jms are not defined on jet)
                                treeJet_pt_sys[syst+Q] = treeJet_Pt
                                treeJet_mass_sys[syst+Q] = treeJet_mass_nom
                                # self.branchBuffers['Jet_pt_{s}{d}'.format(s=syst, d=Q)][0] = treeJet_pt_sys[syst+Q]
                                # self.branchBuffers['Jet_mass_{s}{d}'.format(s=syst, d=Q)][0] = treeJet_mass_sys[syst+Q]
                            else:
                                treeJet_mass_sys[syst+Q] = getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))
                                treeJet_pt_sys[syst+Q] = getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q)) 

                # compute min/max for each jet
                for i in range(min(self.nJet, self.nJetMax)):
                    ptList = [treeJet_Pt[i]]
                    massList = [treeJet_mass[i]]
                    if self.addSystematics and self.sample.type != 'DATA':
                        for syst in self.jetSystematics:
                            for Q in ['Up', 'Down']:
                                if syst == 'jerReg':
                                    ptList.append(treeJet_pt_sys[syst+Q][i] * getattr(tree,'Jet_PtReg'+Q)[i] / getattr(tree,'Jet_PtReg')[i])
                                    massList.append(treeJet_mass_sys[syst+Q][i] * getattr(tree,'Jet_PtReg'+Q)[i] / getattr(tree,'Jet_PtReg')[i])
                                else:
                                    ptList.append(treeJet_pt_sys[syst+Q][i])
                                    massList.append(treeJet_mass_sys[syst+Q][i])
                                if syst == 'jmr' or syst == 'jms':
                                    #print 'test'
                                    #print treeJet_pt_sys[syst+Q][i]
                                    #print 'test2'
                                    self.branchBuffers['Jet_pt_{s}{d}'.format(s=syst, d=Q)][i] = treeJet_pt_sys[syst+Q][i]
                                    self.branchBuffers['Jet_mass_{s}{d}'.format(s=syst, d=Q)][i] = treeJet_mass_sys[syst+Q][i]

                    # compute maximum/minimum
                    self.branchBuffers['Jet_pt_minmaxUp'][i] = max(ptList)
                    self.branchBuffers['Jet_pt_minmaxDown'][i] = min(ptList)
                    self.branchBuffers['Jet_mass_minmaxUp'][i] = max(massList)
                    self.branchBuffers['Jet_mass_minmaxDown'][i] = min(massList)

                # min/max variations for MET
                MET_pt_sys = {}
                MET_phi_sys = {}
                if self.addSystematics and self.sample.type != 'DATA':
                    # read all the arrays once to avoid getattr in the loop over the jets
                    for syst in self.jetSystematics:
                        for Q in ['Up', 'Down']:
                            if syst == 'jmr' or syst == 'jms' or syst == 'jerReg': # nominal values (as jmr and jms are not defined on MET)
                                MET_pt_sys[syst+Q] = getattr(tree, 'MET_Pt')
                                MET_phi_sys[syst+Q] = getattr(tree, 'MET_Phi') 
                                self.branchBuffers['MET_pt_{s}{d}'.format(s=syst, d=Q)][0] = MET_pt_sys[syst+Q]
                                self.branchBuffers['MET_phi_{s}{d}'.format(s=syst, d=Q)][0] = MET_phi_sys[syst+Q]

                            else:
                                MET_pt_sys[syst+Q] = getattr(tree, 'MET_pt_{s}{d}'.format(s=syst, d=Q))
                                MET_phi_sys[syst+Q] = getattr(tree, 'MET_phi_{s}{d}'.format(s=syst, d=Q)) 

                # compute min/max for MET
                #for i in range(min(self.nJet, self.nJetMax)):
                    #ptList = [treeJet_Pt[i]]
                    #massList = [treeJet_mass[i]]
                METptList = [getattr(tree, 'MET_Pt')]
                METphiList = [getattr(tree, 'MET_phi')]
                if self.addSystematics and self.sample.type != 'DATA':
                    for syst in self.jetSystematics:
                        for Q in ['Up', 'Down']:
                            METptList.append(MET_pt_sys[syst+Q])
                            METphiList.append(MET_phi_sys[syst+Q])


                self.branchBuffers['MET_pt_minmaxUp'][0]       = max(METptList)
                self.branchBuffers['MET_pt_minmaxDown'][0]     = min(METptList)
                self.branchBuffers['MET_phi_minmaxUp'][0]      = max(METphiList)
                self.branchBuffers['MET_phi_minmaxDown'][0]    = min(METphiList)

        return True

    def get_msoftdrop_smear(self, pt, eta):

        #get mass resolution
        massResolution = 0
        if eta <= 1.3:
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




