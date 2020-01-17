# Copied from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/TopQuarkAnalysis/SingleTop/src/TopProducer.cc?revision=1.9&view=markup
# and converted from C++ to Python

import numpy as np
import array
from pdgId import pdgId
import sys
from ROOT import *
from math import pow
from math import sqrt
from math import acos
from math import cos
from math import sin
import sys
import numpy as np

class GetTopMass(object):

    def __init__(self, sample=None, nano=False, propagateJES = False, METmethod = 2, useHJets = 0, minbTag = 0.5, branchName='top_mass', addBoostSystematics=False, addMinMax=False):
        self.nano = nano
        self.lastEntry = -1
        self.branchName = branchName
        self.METmethod = METmethod #Check the getJetPtMass function for the different methods
        self.useHJets = useHJets # Using only H jets if useHJets == 1
        self.minbTag = minbTag
        self.propagateJES = propagateJES

        self.branchBuffers = {}
        self.branches = []

        self.branches.append({'name': self.branchName, 'formula': self.getBranch, 'arguments': self.branchName})
        self.branchBuffers[self.branchName] = array.array('f', [0])

        self.branches.append({'name': 'closestJidx', 'formula': self.getBranch, 'arguments': 'closestJidx'})
        self.branchBuffers['closestJidx'] = array.array('f', [0])

        self.branches.append({'name': 'closestHJidx', 'formula': self.getBranch, 'arguments': 'closestHJidx'})
        self.branchBuffers['closestHJidx'] = array.array('f', [0]) 

        self.addBoostSystematics = addBoostSystematics
        self.addMinMax = addMinMax

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']

        # Branch names from config
        self.brJetPtReg = "Jet_PtReg"
        self.brJetPtNom = "Jet_Pt"

        self.Jet_btag = self.config.get('General', 'Jet_btag')
        self.tagidx = self.config.get('General', 'hJidx')

        if self.config.has_option('General', 'eIdx') and  self.config.has_option('General', 'muIdx'):
           self.eIdx = self.config.get('General', 'eIdx')
           self.muIdx = self.config.get('General', 'muIdx')
        else:
           print "WARNING: eIdx and muIdx not defined in [General]! Using default lepton index: \'vLidx\' "
           self.eIdx = "vLidx"
           self.muIdx = "vLidx" 

        self.dataset = self.config.get('General','dataset')

        self.METpt = 'MET_Pt' 
        self.METphi = 'MET_Phi' 


        if self.sample.type != 'DATA':
            self.brJetMassNom = "Jet_mass_nom"
        else:
            self.brJetMassNom = "Jet_mass"


        ##########
        # add JES/JER systematics
        ##########
        # only defined for nano at the moment

        if self.propagateJES and self.nano:
            self.jetSystematics = ['jer','jerReg','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesTotal','unclustEn'] 

            if self.dataset == '2016':
                self.jetSystematics.remove('jerReg')

            if self.addBoostSystematics:
                self.jetSystematics+= ['jms']
                self.jetSystematics+= ['jmr']


            if self.sample.type != 'DATA':
                systList = self.jetSystematics
            else:
                systList = []
            if self.addMinMax:
                systList += ['minmax']
            for syst in systList:
                for Q in ['Up', 'Down']:
                    top_massSyst = "{p}_{s}_{q}".format(p=self.branchName, s=syst, q=Q)
                    self.branchBuffers[top_massSyst] = array.array('f', [0.0])
                    self.branches.append({'name': top_massSyst, 'formula': self.getBranch, 'arguments': top_massSyst})

    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getBranches(self):
        return self.branches

    # read from buffers which have been filled in processEvent()
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        if currentEntry != self.lastEntry:
            self.lastEntry = currentEntry

            #############
            # Nominal top mass
            #############

            # Select branches from tree

            self.hJidx0 = getattr(tree,self.tagidx)[0] 
            self.hJidx1 = getattr(tree,self.tagidx)[1]


            treeMETpt, treeMETphi = self.getMET(tree)


            lep = TLorentzVector()
            met = TLorentzVector()



            if not self.nano:
                lep.SetPtEtaPhiM(tree.vLeptons_new_pt[0], tree.vLeptons_new_eta[0], tree.vLeptons_new_phi[0], tree.vLeptons_new_mass[0])
                met.SetPtEtaPhiM(tree.met_pt, tree.met_eta, tree.met_phi, tree.met_mass)
            else: 
                if tree.Vtype == 2:
                    mu1Idx = getattr(tree,self.muIdx)[0]
                    lep.SetPtEtaPhiM(tree.Muon_pt[mu1Idx], tree.Muon_eta[mu1Idx], tree.Muon_phi[mu1Idx], tree.Muon_mass[mu1Idx])
                if tree.Vtype == 3:
                    e1Idx = getattr(tree,self.eIdx)[0]
                    lep.SetPtEtaPhiM(tree.Electron_pt[e1Idx], tree.Electron_eta[e1Idx], tree.Electron_phi[e1Idx], tree.Electron_mass[e1Idx])
                met.SetPtEtaPhiM(treeMETpt, 0, treeMETphi, 0)

            #Index of the closest jet to the lepton (cJidx/cHJidx among all/H jets ) 
            cJidx, cHJidx = self.clossestJetIdx(tree, lep)

            self.branchBuffers['closestJidx'][0] = cJidx 
            self.branchBuffers['closestHJidx'][0] = cHJidx 

            closestIdx = cJidx if self.useHJets == 0 else cHJidx 
           
            if closestIdx != - 1: 
               cJet = TLorentzVector()
               JetPt , JetMass = self.getJetPtMass(tree, closestIdx) 
#               cJet.SetPtEtaPhiM(tree.Jet_PtReg[cJidx], tree.Jet_eta[cJidx], tree.Jet_phi[cJidx], tree.Jet_mass[cJidx]*tree.Jet_PtReg[cJidx]/tree.Jet_Pt[cJidx])
               cJet.SetPtEtaPhiM(JetPt, tree.Jet_eta[closestIdx], tree.Jet_phi[closestIdx], JetMass)

               top_mass = self.computeTopMass_new(lep,met,cJet,self.METmethod)

            elif closestIdx == -1 : 
               top_mass = -99

            self.branchBuffers[self.branchName][0] = top_mass
#            print "\n{}->top_mass = {}".format(closestIdx,top_mass) 


#            bjet1 = TLorentzVector()
#            bjet2 = TLorentzVector()
#            if not self.nano:
#                bjet1.SetPtEtaPhiM(tree.hJetCMVAV2_pt_reg_0, tree.Jet_eta[tree.hJCMVAV2idx[0]], tree.Jet_phi[tree.hJCMVAV2idx[0]], tree.Jet_mass[tree.hJCMVAV2idx[0]])
#                bjet2.SetPtEtaPhiM(tree.hJetCMVAV2_pt_reg_1, tree.Jet_eta[tree.hJCMVAV2idx[1]], tree.Jet_phi[tree.hJCMVAV2idx[1]], tree.Jet_mass[tree.hJCMVAV2idx[1]])
#            else:
#                bjet1.SetPtEtaPhiM(tree.Jet_PtReg[hJidx0], tree.Jet_eta[hJidx0], tree.Jet_phi[hJidx0], treeJet_mass[hJidx0]*tree.Jet_bReg[hJidx0])
#                bjet2.SetPtEtaPhiM(tree.Jet_PtReg[hJidx1], tree.Jet_eta[hJidx1], tree.Jet_phi[hJidx1], treeJet_mass[hJidx1]*tree.Jet_bReg[hJidx1])
#            jets = [bjet1, bjet2]
#            jetsIdx = [hJidx0, hJidx1]
##            tmp = self.computeTopMass(lep,met,jets,jetsIdx)
#            tmp = self.computeTopMass(lep,met,jets)
#
##            print "4. lep + jet + met (old): {}".format(tmp)
#
#            self.branchBuffers[self.branchName][0] = tmp

            ##########
            # add JES/JER systematics
            ##########

            top_mass_min = -99
            top_mass_max = -99
            if self.propagateJES and self.nano and self.sample.type != 'DATA':

                systList = self.jetSystematics 
                for syst in systList:
                    for Q in ['Up', 'Down']:

                        top_massSyst = "{p}_{s}_{q}".format(p=self.branchName, s=syst, q=Q)
                        variation = "{s}{q}".format(s=syst, q=Q)

                        treeMETpt, treeMETphi = self.getMET(tree, variation=variation)
                        met.SetPtEtaPhiM(treeMETpt, 0, treeMETphi, 0)


                        cJidx, cHJidx = self.clossestJetIdx(tree, lep, variation)
                        
                        closestIdx = cJidx if self.useHJets == 0 else cHJidx 
                       
                        if closestIdx != - 1: 
                           cJet = TLorentzVector()
                           JetPt , JetMass = self.getJetPtMass(tree, closestIdx, variation) 
            #               cJet.SetPtEtaPhiM(tree.Jet_PtReg[cJidx], tree.Jet_eta[cJidx], tree.Jet_phi[cJidx], tree.Jet_mass[cJidx]*tree.Jet_PtReg[cJidx]/tree.Jet_Pt[cJidx])
                           cJet.SetPtEtaPhiM(JetPt, tree.Jet_eta[closestIdx], tree.Jet_phi[closestIdx], JetMass)
            
                           top_mass = self.computeTopMass_new(lep,met,cJet,self.METmethod)
            
                        elif closestIdx == -1 : 
                           top_mass = -99

#                        print "{}->{} = {}".format(closestIdx,top_massSyst, top_mass) 
#                        self.branchBuffers[top_massSyst][0] = top_mass
                        ########
                        # fill systematics
                        ########

                        # in cases sys is broken, set it to nominal value
                        if top_mass == -99:
                            top_mass = self.branchBuffers[self.branchName][0]

                        self.branchBuffers[top_massSyst][0] = top_mass

                        if top_mass_min == -99:
                            top_mass_min = top_mass
                            top_mass_max = top_mass
                        else:
                            top_mass_min = min(top_mass_min,top_mass)
                            top_mass_max = max(top_mass_max,top_mass)
                if self.addMinMax:
                    self.branchBuffers[self.branchName + '_minmax_Down'][0] = top_mass_min
                    self.branchBuffers[self.branchName + '_minmax_Up'][0] = top_mass_max

            elif self.propagateJES and self.nano and self.sample.type == 'DATA':
                top_mass_min = top_mass
                top_mass_max = top_mass
#                print 'top_mass_min is', top_mass_min
                if self.addMinMax:
                    self.branchBuffers[self.branchName + '_minmax_Down'][0] = top_mass_min
                    self.branchBuffers[self.branchName + '_minmax_Up'][0] = top_mass_max


            return True


    ##
    # \Function EquationSolver:
    #
    # Solves 3rd degree equations
    #
    # \Author A. Orso M. Iorio
    #
    #
    # \version  $Id: EquationSolver.h,v 1.1 2013/02/27 12:18:42 degrutto Exp $
    #
    def EquationSolve(self, a, b, c, d):


      result = []



      if (a != 0):

        q = (3*a*c-b*b)/(9*a*a)
        r = (9*a*b*c - 27*a*a*d - 2*b*b*b)/(54*a*a*a)
        Delta = q*q*q + r*r

        rho=0.
        theta=0.

        if( Delta<=0):
          rho = sqrt(-(q*q*q))

          theta = acos(r/rho)

          s = complex(sqrt(-q)*cos(theta/3.0),sqrt(-q)*sin(theta/3.0))
          t = complex(sqrt(-q)*cos(-theta/3.0),sqrt(-q)*sin(-theta/3.0))

        if(Delta>0):
          #print r, sqrt(Delta)
          if (r+sqrt(Delta) > 0):
              s = complex(pow((r+sqrt(Delta)),(1./3)),0)
          else:
              s = complex(-pow(abs((r+sqrt(Delta))),(1./3)),0)
          if (r-sqrt(Delta) > 0):
              t = complex(pow((r-sqrt(Delta)),(1./3)),0)
          else:
              t = complex(-pow(abs((r-sqrt(Delta))),(1./3)),0)

        i = complex(0.,1.0)

        x1 = s+t+complex(-b/(3.0*a),0)
        x2 = (s+t)*complex(-0.5,0)-complex(b/(3.0*a),0)+(s-t)*i*complex(sqrt(3)/2.0,0)
        x3 = (s+t)*complex(-0.5,0)-complex(b/(3.0*a),0)-(s-t)*i*complex(sqrt(3)/2.0,0)

        if(abs(x1.imag)<0.0001): result.append(x1.real)
        if(abs(x2.imag)<0.0001): result.append(x2.real)
        if(abs(x3.imag)<0.0001): result.append(x3.real)

        #print x1,x2,x3
        return result
      else:
          return result


      return result

    def getNu4Momentum(self, TLepton, TMET):

      Lepton = TLorentzVector()
      Lepton.SetPxPyPzE(TLepton.Px(), TLepton.Py(), TLepton.Pz(), TLepton.E());
      MET = TLorentzVector()
      MET.SetPxPyPzE(TMET.Px(), TMET.Py(), 0., TMET.E());

      mW = 80.38;

      result = []

      MisET2 = (MET.Px()*MET.Px() + MET.Py()*MET.Py());
      mu = (mW*mW)/2 + MET.Px()*Lepton.Px() + MET.Py()*Lepton.Py();
      a  = (mu*Lepton.Pz())/(Lepton.Energy()*Lepton.Energy() - Lepton.Pz()*Lepton.Pz());
      a2 = pow(a,2);
      b  = -10*(pow(Lepton.Energy(),2.)*(MisET2) - pow(mu,2.))/(pow(Lepton.Energy(),2) - pow(Lepton.Pz(),2));
      pz1 = 0.
      pz2 = 0.
      pznu = 0.
      nNuSol = 0

      p4nu_rec = TLorentzVector()
      p4W_rec = TLorentzVector()
      p4b_rec = TLorentzVector()
      p4Top_rec = TLorentzVector()
      p4lep_rec = TLorentzVector()

      p4lep_rec.SetPxPyPzE(Lepton.Px(),Lepton.Py(),Lepton.Pz(),Lepton.Energy());

      #print a2,b
      if(a2-b > 0 ):
        root = sqrt(a2-b);
        pz1 = a + root;
        pz2 = a - root;
        nNuSol = 2;

        pznu = pz1;

        Enu = sqrt(MisET2 + pznu*pznu);

        p4nu_rec.SetPxPyPzE(MET.Px(), MET.Py(), pznu, Enu);

        result.append(p4nu_rec);

      else:

        ptlep = Lepton.Pt()
        pxlep=Lepton.Px()
        pylep=Lepton.Py()
        metpx=MET.Px()
        metpy=MET.Py()

        EquationA = 1.
        EquationB = -3.*pylep*mW/(ptlep)
        EquationC = mW*mW*(2*pylep*pylep)/(ptlep*ptlep)+mW*mW-4*pxlep*pxlep*pxlep*metpx/(ptlep*ptlep)-4*pxlep*pxlep*pylep*metpy/(ptlep*ptlep)
        EquationD = 4.*pxlep*pxlep*mW*metpy/(ptlep)-pylep*mW*mW*mW/ptlep

        solutions = self.EquationSolve(EquationA,EquationB,EquationC,EquationD)

        solutions2 = self.EquationSolve(EquationA,EquationB,EquationC,EquationD);

        deltaMin = 14000*14000
        zeroValue = -mW*mW/(4*pxlep)
        minPx=0
        minPy=0

        for i in range(len(solutions)):
            if(solutions[i]<0 ): continue
            p_x = (solutions[i]*solutions[i]-mW*mW)/(4*pxlep)
            p_y = ( mW*mW*pylep + 2*pxlep*pylep*p_x -mW*ptlep*solutions[i])/(2*pxlep*pxlep)
            Delta2 = (p_x-metpx)*(p_x-metpx)+(p_y-metpy)*(p_y-metpy)

            if(Delta2< deltaMin and Delta2 > 0):
                deltaMin = Delta2
                minPx=p_x
                minPy=p_y

        for i in range(len(solutions2)):
            if(solutions2[i]<0 ): continue
            p_x = (solutions2[i]*solutions2[i]-mW*mW)/(4*pxlep)
            p_y = ( mW*mW*pylep + 2*pxlep*pylep*p_x +mW*ptlep*solutions2[i])/(2*pxlep*pxlep)
            Delta2 = (p_x-metpx)*(p_x-metpx)+(p_y-metpy)*(p_y-metpy)
            if(Delta2< deltaMin and Delta2 > 0):
                deltaMin = Delta2
                minPx=p_x
                minPy=p_y

        pyZeroValue= ( mW*mW*pxlep + 2*pxlep*pylep*zeroValue)
        delta2ZeroValue= (zeroValue-metpx)*(zeroValue-metpx) + (pyZeroValue-metpy)*(pyZeroValue-metpy)

        if(deltaMin==14000*14000): return TLorentzVector(0,0,0,0)

        if(delta2ZeroValue < deltaMin):
            deltaMin = delta2ZeroValue
            minPx=zeroValue
            minPy=pyZeroValue

        mu_Minimum = (mW*mW)/2 + minPx*pxlep + minPy*pylep
        a_Minimum  = (mu_Minimum*Lepton.Pz())/(Lepton.Energy()*Lepton.Energy() - Lepton.Pz()*Lepton.Pz())
        pznu = a_Minimum

        Enu = sqrt(minPx*minPx+minPy*minPy + pznu*pznu)
        p4nu_rec.SetPxPyPzE(minPx, minPy, pznu , Enu)
        result.append(p4nu_rec)
      return result[0]

#    def computeTopMass(self, lep, met, jets, jetsIdx):
    def computeTopMass(self, lep, met, jets):

        #neutrino = self.getNu4Momentum(lep, met)
        bjet = TLorentzVector()
        minDR = 99
        closeIdx = -1
        for i, jet in enumerate(jets):
            if (jet.Pt() > 30): # and jet.bTagCSV > CSVL and jet.puID > 0 and jet.Id > 0? how?
                dR = jet.DeltaR(lep)
                if (dR < minDR):
                    minDR = dR
                    bjet = jet
#                    closeIdx = jetsIdx[i]
        if (bjet.Pt() <= 0):
            return -99
#        print "Old closest idx: {}".format(closeIdx)
        top = lep + met + bjet
        return top.M()

    def getJetPtMasses(self, tree, variation=None):

        JetPtReg = np.array(getattr(tree, self.brJetPtReg))
        JetPtNom = np.array(getattr(tree,self.brJetPtNom))
        JetMassNom = np.array(getattr(tree,self.brJetMassNom))

        if variation is None or variation.startswith('unclustEn'):
           JetPt =  JetPtReg
           JetMass = JetMassNom * JetPtReg /JetPtNom

        elif 'jerReg' in variation:
           Q = "Up" if "Up" in variation else "Down"
           JetPtSys = np.array(getattr(tree,"Jet_PtReg" + Q))

           JetPt =  JetPtSys
           JetMass = JetMassNom * JetPtSys / JetPtNom

        else:
           JetPtSys = np.array(getattr(tree,"Jet_pt" + "_" + variation))
           JetMassSys = np.array(getattr(tree, "Jet_mass" + "_" + variation))

           JetPt =  JetPtSys * JetPtReg / JetPtNom
           JetMass = JetMassSys * JetPtReg / JetPtNom

        return JetPt, JetMass


    def getJetPtMass(self, tree, i, variation=None):

        JetPtReg = getattr(tree, self.brJetPtReg)[i]
        JetPtNom = getattr(tree,self.brJetPtNom)[i] 
        JetMassNom = getattr(tree,self.brJetMassNom)[i] 

        if variation is None or variation.startswith('unclustEn'):
           JetPt =  JetPtReg
           JetMass = JetMassNom * JetPtReg /JetPtNom

        elif 'jerReg' in variation:
           Q = "Up" if "Up" in variation else "Down"
           JetPtSys = getattr(tree,"Jet_PtReg" + Q)[i]

           JetPt =  JetPtSys
           JetMass = JetMassNom * JetPtSys / JetPtNom

        else:
           JetPtSys = getattr(tree,"Jet_pt" + "_" + variation)[i]
           JetMassSys = getattr(tree, "Jet_mass" + "_" + variation)[i] 

           JetPt =  JetPtSys * JetPtReg / JetPtNom
           JetMass = JetMassSys * JetPtReg / JetPtNom
#           print "{}: {}, {}: {}".format("Jet_pt" + "_" + variation,JetPtSys,"Jet_mass" + "_" + variation,JetMassSys)
#           print "JetPt {}, JetMass: {}".format(JetPt,JetMass)
        return JetPt, JetMass

    def getMET(self, tree, variation=None):
        if variation is not None and not variation.startswith('jerReg'):
            treeMETpt = getattr(tree, "MET_pt_" + variation)
            treeMETphi = getattr(tree, "MET_phi_" + variation)
        else:
            treeMETpt = getattr(tree,self.METpt)
            treeMETphi = getattr(tree,self.METphi)
        return treeMETpt, treeMETphi

    def clossestJetIdx(self, tree, lep, variation = None):
        #neutrino = self.getNu4Momentum(lep, met)

        JetPt = tree.Jet_PtReg
        minDR = 999
        minHDR = 999

        ClosestJIdx = -1
        ClosestHJIdx = -1

        jetPts, jetMasses = self.getJetPtMasses(tree, variation)
        jetBtags = getattr(tree,self.Jet_btag)

        for i in range(tree.nJet):

           #if temPt < 30 or tembTag < self.minbTag or not (tree.Jet_lepFilter): continue

           if jetPts[i] >= 30 and jetBtags[i] >= self.minbTag and tree.Jet_lepFilter[i] and tree.Jet_jetId[i] > 4 and (tree.Jet_puId[i]>6 or jetPts[i] >50.0):

               tempJet = TLorentzVector()
               tempJet.SetPtEtaPhiM(jetPts[i],tree.Jet_eta[i],tree.Jet_phi[i], jetMasses[i])
               dR = tempJet.DeltaR(lep)
    #           print "Jetidx: {}, dR = {}".format(i,dR)

               if dR < minDR:
                  minDR = dR
                  ClosestJIdx = i

               if (i == self.hJidx0 or i == self.hJidx1) and dR < minHDR:
                  minHDR = dR
                  ClosestHJIdx = i

#        print "hJidx0 = {}, hJidx1 = {}".format(self.hJidx0,self.hJidx1)
        return ClosestJIdx, ClosestHJIdx

            
    def computeTopMass_new(self, lep, met, jet, METmethod):
        #neutrino = self.getNu4Momentum(lep, met)

        new_top = TLorentzVector()
        jet_transverse = TLorentzVector()
        lep_transverse = TLorentzVector()

        if METmethod == 1:
           jet_transverse.SetPxPyPzE(jet.Px(),jet.Py(),0,sqrt((jet.M())**2 + (jet.Pt())**2))   
           lep_transverse.SetPxPyPzE(lep.Px(),lep.Py(),0,sqrt((lep.M())**2 + (lep.Pt())**2))   

           new_top = jet_transverse + lep_transverse + met
        elif METmethod == 2:
           neutrino = TLorentzVector()
           neutrino = self.getNu4Momentum(lep, met)
           new_top = lep + jet + neutrino
        elif METmethod == 3:
           new_top = lep + jet + met

        return new_top.M()


