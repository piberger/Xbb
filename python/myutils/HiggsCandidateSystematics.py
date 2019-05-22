#!/usr/bin/env python
import ROOT
import array
import os
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule

# propagate JES/JER systematics from jets to higgs candidate dijet pair 
class HiggsCandidateSystematics(AddCollectionsModule):
    
    def __init__(self, addSystematics=True, prefix="H", addBoostSystematics=False):
        super(HiggsCandidateSystematics, self).__init__()
        self.debug = 'XBBDEBUG' in os.environ
        self.lastEntry = -1
        self.nJet = -1
        self.nJetMax = 100
        self.addSystematics = addSystematics
        self.prefix = prefix
        self.addBoostSystematics = addBoostSystematics

        self.jetSystematics = ['jer','jerReg','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesTotal']

        # corrected dijet (Higgs candidate) properties
        self.higgsProperties = [self.prefix + '_' + x for x in ['pt','eta', 'phi', 'mass','pt_noFSR','eta_noFSR','phi_noFSR','mass_noFSR']]

        # included JEC and JER systematic for msoftdrop
        if self.addBoostSystematics: 
            self.higgsProperties +=['FatJet_msoftdrop_sys']

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']

        #jerReg systematics not included in nanoAOD v4 for 2016 dataset.
        self.dataset = self.config.get('General', 'dataset')
        if self.dataset == '2016':
            self.jetSystematics.remove('jerReg')

        if self.addBoostSystematics:
            self.boosttagidx = 'Hbb_fjidx'
            self.msoftdrop = 'FatJet_msoftdrop'


        self.tagidx = self.config.get('General', 'hJidx')
        if self.debug:
            print "DEBUG: HiggsCandidateSystematics::__init__(), with idx=", self.tagidx, " prefix=", self.prefix

        self.higgsPropertiesWithSys = self.higgsProperties if self.sample.type != 'DATA' else []
        for higgsProperty in self.higgsProperties: 
            self.addBranch(higgsProperty)
            
            # for data only include the min/max (set to nominal) to simplify cutting
            systList = self.jetSystematics + ['minmax'] if higgsProperty in self.higgsPropertiesWithSys else ['minmax']

            for syst in systList:
                for Q in ['Up', 'Down']:
                    higgsPropertySyst = "{p}_{s}_{q}".format(p=higgsProperty, s=syst, q=Q)
                    self.addBranch(higgsPropertySyst)

        self.addBranch('hJets_0_pt_noFSR')
        self.addBranch('hJets_1_pt_noFSR')
        self.addBranch('hJets_0_pt_FSRrecovered')
        self.addBranch('hJets_1_pt_FSRrecovered')
        self.addIntegerBranch('nFSRrecovered')

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
                    msoftdrop   = getattr(tree, self.msoftdrop)[boosttagidx]
                    self.branchBuffers['FatJet_msoftdrop_sys'][0] = msoftdrop

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

                hJ0.SetPtEtaPhiM(treeJet_PtReg[hJidx0], treeJet_eta[hJidx0], treeJet_phi[hJidx0], treeJet_mass[hJidx0] * treeJet_PtReg[hJidx0]/treeJet_Pt[hJidx0])
                hJ1.SetPtEtaPhiM(treeJet_PtReg[hJidx1], treeJet_eta[hJidx1], treeJet_phi[hJidx1], treeJet_mass[hJidx1] * treeJet_PtReg[hJidx1]/treeJet_Pt[hJidx1])

                dijet_Nominal_noFSR = hJ0 + hJ1
                
                self.branchBuffers['hJets_0_pt_noFSR'][0] = hJ0.Pt()
                self.branchBuffers['hJets_1_pt_noFSR'][0] = hJ1.Pt()
                
                self.branchBuffers[self.prefix + '_pt_noFSR'][0] = dijet_Nominal_noFSR.Pt()
                self.branchBuffers[self.prefix + '_eta_noFSR'][0] = dijet_Nominal_noFSR.Eta()
                self.branchBuffers[self.prefix + '_phi_noFSR'][0] = dijet_Nominal_noFSR.Phi()
                self.branchBuffers[self.prefix + '_mass_noFSR'][0] = dijet_Nominal_noFSR.M()
                
                # save information which FSR jets have been added for nominal
                fsrIndices0 = []
                fsrIndices1 = []
                
                # FSR recovery
                for i in range(len(treeJet_PtReg)):
                    if i not in [hJidx0, hJidx1] and treeJet_Pt[i]>20 and abs(tree.Jet_eta[i])<3.0 and tree.Jet_puId[i]>0 and tree.Jet_lepFilter[i] > 0:
                        FSR = ROOT.TLorentzVector()
                        FSR.SetPtEtaPhiM(treeJet_PtReg[i],treeJet_eta[i],treeJet_phi[i],treeJet_mass[i] * treeJet_PtReg[i]/treeJet_Pt[i])
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
                self.branchBuffers['nFSRrecovered'][0] = len(fsrIndices0) + len(fsrIndices1)

            # systematics
            valueList = {x:[self.branchBuffers[x][0]] for x in self.higgsProperties}
            if self.addSystematics and self.sample.type != 'DATA':
                for syst in self.jetSystematics:
                    for Q in ['Up', 'Down']:
                        if self.sample.type != 'DATA':
                            # included JEC and JER systematic for msoftdrop
                            if self.addBoostSystematics  and boosttagidx > -1: 
                                msoftdrop_sys = msoftdrop*getattr(tree, 'FatJet_pt_{s}{d}'.format(s=syst, d=Q))[boosttagidx]/getattr(tree, 'FatJet_pt_nom')[boosttagidx]
                            # nothing to compute if no resolved jet
                            if not (hJidx0 > -1 and hJidx1 > -1):
                                pass
                            else:
                                hJ0 = ROOT.TLorentzVector()
                                hJ1 = ROOT.TLorentzVector()

                                if syst == 'jerReg':
                                    treeJet_PtRegSys = getattr(tree,'Jet_PtReg'+Q)
                                    # vary the regression for the regression systematic
                                    #  pt_reg_var   = pt_reg_var 
                                    #  mass_reg_var = mass_nom * pt_reg_var / pt_nom
                                    hJ0.SetPtEtaPhiM(treeJet_PtRegSys[hJidx0], treeJet_eta[hJidx0], treeJet_phi[hJidx0], treeJet_mass[hJidx0]*treeJet_PtRegSys[hJidx0]/treeJet_Pt[hJidx0])
                                    hJ1.SetPtEtaPhiM(treeJet_PtRegSys[hJidx1], treeJet_eta[hJidx1], treeJet_phi[hJidx1], treeJet_mass[hJidx1]*treeJet_PtRegSys[hJidx1]/treeJet_Pt[hJidx1])
                                else:
                                    treeJet_mass_sys = getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))
                                    treeJet_pt_sys   = getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))

                                    # vary unregressed pt
                                    #  pt_reg_var   = pt_reg * pt_var / pt_nom
                                    #  mass_reg_var = mass_var * pt_reg / pt_nom
                                    # SYNC with AT: added * treeJet_mass[hJidx0]/treeJet_mass_nom[hJidx0] to have nominal value at Jet_mass instead of Jet_mass_nom

                                    hJ0mass = treeJet_mass_sys[hJidx0] * treeJet_PtReg[hJidx0]/treeJet_Pt[hJidx0] * (treeJet_mass[hJidx0]/treeJet_mass_nom[hJidx0] if treeJet_mass_nom[hJidx0] > 0 else 1)
                                    hJ1mass = treeJet_mass_sys[hJidx1] * treeJet_PtReg[hJidx1]/treeJet_Pt[hJidx1] * (treeJet_mass[hJidx1]/treeJet_mass_nom[hJidx1] if treeJet_mass_nom[hJidx1] > 0 else 1)

                                    hJ0.SetPtEtaPhiM(treeJet_PtReg[hJidx0]*treeJet_pt_sys[hJidx0]/treeJet_Pt[hJidx0], treeJet_eta[hJidx0], treeJet_phi[hJidx0], hJ0mass) 
                                    hJ1.SetPtEtaPhiM(treeJet_PtReg[hJidx1]*treeJet_pt_sys[hJidx1]/treeJet_Pt[hJidx1], treeJet_eta[hJidx1], treeJet_phi[hJidx1], hJ1mass)

                                dijet_noFSR = hJ0 + hJ1

                                # FSR recovery for systematic variations
                                #  the same jets are recovered as for nominal, but with variation applied
                                for i in fsrIndices0:
                                    FSR = ROOT.TLorentzVector()
                                    if syst == 'jerReg':
                                        FSR.SetPtEtaPhiM(treeJet_PtRegSys[i], treeJet_eta[i], treeJet_phi[i], treeJet_mass[i] * treeJet_PtRegSys[i]/treeJet_Pt[i])
                                    else:
                                        FSR_pt_reg_factor = treeJet_PtReg[i]/treeJet_Pt[i] 
                                        FSR_pt_reg_sys    = FSR_pt_reg_factor * treeJet_pt_sys[i]
                                        FSR_mass_reg_sys  = (treeJet_mass[i]/treeJet_mass_nom[i] if treeJet_mass_nom[i] > 0 else 1.0) * treeJet_mass_sys[i] * FSR_pt_reg_factor
                                        FSR.SetPtEtaPhiM(FSR_pt_reg_sys, treeJet_eta[i], treeJet_phi[i], FSR_mass_reg_sys)
                                    hJ0 = hJ0 + FSR
                                for i in fsrIndices1:
                                    FSR = ROOT.TLorentzVector()
                                    if syst == 'jerReg':
                                        FSR.SetPtEtaPhiM(treeJet_PtRegSys[i], treeJet_eta[i], treeJet_phi[i], treeJet_mass[i] * treeJet_PtRegSys[i]/treeJet_Pt[i])
                                    else:
                                        FSR_pt_reg_factor = treeJet_PtReg[i]/treeJet_Pt[i]
                                        FSR_pt_reg_sys    = FSR_pt_reg_factor * treeJet_pt_sys[i]
                                        FSR_mass_reg_sys  = (treeJet_mass[i]/treeJet_mass_nom[i] if treeJet_mass_nom[i] > 0 else 1.0) * treeJet_mass_sys[i] * FSR_pt_reg_factor
                                        FSR.SetPtEtaPhiM(FSR_pt_reg_sys, treeJet_eta[i], treeJet_phi[i], FSR_mass_reg_sys)
                                    hJ1 = hJ1 + FSR
                                
                                dijet = hJ0 + hJ1
                        else:
                            dijet_noFSR = dijet_Nominal_noFSR
                            dijet = dijet_Nominal

                        if self.addBoostSystematics  and boosttagidx > -1: 
                            self.branchBuffers['FatJet_msoftdrop_sys_{s}_{d}'.format(s=syst, d=Q)][0] = msoftdrop_sys
                            valueList['FatJet_msoftdrop_sys'].append(msoftdrop_sys)

                        if not (hJidx0 > -1 and hJidx1 > -1):
                            pass
                        else:
                            self.branchBuffers[self.prefix + '_pt_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.Pt()
                            self.branchBuffers[self.prefix + '_eta_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.Eta()
                            self.branchBuffers[self.prefix + '_phi_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.Phi()
                            self.branchBuffers[self.prefix + '_mass_{s}_{d}'.format(s=syst, d=Q)][0] = dijet.M()
                            
                            self.branchBuffers[self.prefix + '_pt_noFSR_{s}_{d}'.format(s=syst, d=Q)][0] = dijet_noFSR.Pt()
                            self.branchBuffers[self.prefix + '_eta_noFSR_{s}_{d}'.format(s=syst, d=Q)][0] = dijet_noFSR.Eta()
                            self.branchBuffers[self.prefix + '_phi_noFSR_{s}_{d}'.format(s=syst, d=Q)][0] = dijet_noFSR.Phi()
                            self.branchBuffers[self.prefix + '_mass_noFSR_{s}_{d}'.format(s=syst, d=Q)][0] = dijet_noFSR.M()

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

            # get minimum and maximum variation
            for syst in ['minmax']:
                for Q in ['Up', 'Down']:
                    for p in self.higgsProperties:
                        self.branchBuffers['{p}_{s}_{d}'.format(p=p, s=syst, d=Q)][0] = min(valueList[p]) if Q=='Down' else max(valueList[p])

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

                # compute maximum/minimum
                self.branchBuffers['Jet_pt_minmaxUp'][i] = max(ptList)
                self.branchBuffers['Jet_pt_minmaxDown'][i] = min(ptList)
                self.branchBuffers['Jet_mass_minmaxUp'][i] = max(massList)
                self.branchBuffers['Jet_mass_minmaxDown'][i] = min(massList)

        return True




