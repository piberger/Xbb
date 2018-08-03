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

class GetTopMass(object):

    def __init__(self, sample=None, nano=False, propagateJES = False, tagidx = ""):
        self.nano = nano
        self.lastEntry = -1
        self.tagidx = tagidx
        self.branchBuffers = {}
        self.branches = []
        self.branches.append({'name': 'top_mass', 'formula': self.getBranch, 'arguments': 'top_mass'})
        self.branchBuffers['top_mass'] = array.array('f', [0])


        self.propagateJES = propagateJES


    def customInit(self, initVars):
        self.sample = initVars['sample']
        ##########
        # add JES/JER systematics
        ##########
        # only defined for nano at the moment

        if self.propagateJES and self.nano:
            self.jetSystematics = ['jer','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesTotal']

            if self.sample.type != 'DATA': systList = self.jetSystematics + ['minmax']
            else: systList = ['minmax']
            for syst in systList:
                for Q in ['Up', 'Down']:
                    top_massSyst = "{p}_{s}_{q}".format(p='top_mass', s=syst, q=Q)
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

            lep = TLorentzVector()
            met = TLorentzVector()

            hJidx0 = getattr(tree,self.tagidx)[0] 
            hJidx1 = getattr(tree,self.tagidx)[1]

            # select branches from tree
            # for 2016 nano v5
            treeJet_PtReg = tree.Jet_PtReg 
            treeJet_pt = tree.Jet_pt
            treeJet_Pt = tree.Jet_Pt
            treeJet_bReg = tree.Jet_bReg

            treeJet_phi = tree.Jet_phi
            treeJet_eta = tree.Jet_eta

            if self.sample.type != 'DATA':
                treeJet_mass = tree.Jet_mass_nom
            else:
                treeJet_mass = tree.Jet_mass

            if not self.nano:
                lep.SetPtEtaPhiM(tree.vLeptons_new_pt[0], tree.vLeptons_new_eta[0], tree.vLeptons_new_phi[0], tree.vLeptons_new_mass[0])
                met.SetPtEtaPhiM(tree.met_pt, tree.met_eta, tree.met_phi, tree.met_mass)
            else: 
                if len(getattr(tree,'VMuonIdx')) == 1:
                    lep.SetPtEtaPhiM(tree.Muon_pt[tree.VMuonIdx[0]], tree.Muon_eta[tree.VMuonIdx[0]], tree.Muon_phi[tree.VMuonIdx[0]], tree.Muon_mass[tree.VMuonIdx[0]])
                if len(getattr(tree,'VElectronIdx')) == 1:
                    lep.SetPtEtaPhiM(tree.Electron_pt[tree.VElectronIdx[0]], tree.Electron_eta[tree.VElectronIdx[0]], tree.Electron_phi[tree.VElectronIdx[0]], tree.Electron_mass[tree.VElectronIdx[0]])
                met.SetPtEtaPhiM(tree.MET_pt, 0, tree.MET_phi, 0)
            bjet1 = TLorentzVector()
            bjet2 = TLorentzVector()
            if not self.nano:
                bjet1.SetPtEtaPhiM(tree.hJetCMVAV2_pt_reg_0, tree.Jet_eta[tree.hJCMVAV2idx[0]], tree.Jet_phi[tree.hJCMVAV2idx[0]], tree.Jet_mass[tree.hJCMVAV2idx[0]])
                bjet2.SetPtEtaPhiM(tree.hJetCMVAV2_pt_reg_1, tree.Jet_eta[tree.hJCMVAV2idx[1]], tree.Jet_phi[tree.hJCMVAV2idx[1]], tree.Jet_mass[tree.hJCMVAV2idx[1]])
            else:
                bjet1.SetPtEtaPhiM(tree.Jet_PtReg[hJidx0], tree.Jet_eta[hJidx0], tree.Jet_phi[hJidx0], treeJet_mass[hJidx0]*tree.Jet_bReg[hJidx0])
                bjet2.SetPtEtaPhiM(tree.Jet_PtReg[hJidx1], tree.Jet_eta[hJidx1], tree.Jet_phi[hJidx1], treeJet_mass[hJidx1]*tree.Jet_bReg[hJidx1])
            jets = [bjet1, bjet2]
            tmp = self.computeTopMass(lep,met,jets)
            self.branchBuffers['top_mass'][0] = tmp

            ##########
            # add JES/JER systematics
            ##########

            top_mass_min = -99
            top_mass_max = -99
            if self.propagateJES and self.nano and self.sample.type != 'DATA':

                systList = self.jetSystematics 
                for syst in systList:
                    for Q in ['Up', 'Down']:

                        top_massSyst = "{p}_{s}_{q}".format(p='top_mass', s=syst, q=Q)

                        bjet1 = TLorentzVector()
                        bjet2 = TLorentzVector()

                        bjet1.SetPtEtaPhiM(treeJet_PtReg[hJidx0]*getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))[hJidx0]/treeJet_Pt[hJidx0],treeJet_eta[hJidx0],treeJet_phi[hJidx0],getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))[hJidx0] * treeJet_bReg[hJidx0])
                        bjet2.SetPtEtaPhiM(treeJet_PtReg[hJidx1]*getattr(tree, 'Jet_pt_{s}{d}'.format(s=syst, d=Q))[hJidx1]/treeJet_Pt[hJidx1],treeJet_eta[hJidx1],treeJet_phi[hJidx1],getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))[hJidx1] * treeJet_bReg[hJidx1])

                        # to avoid large systematic difference because of 30 GeV threshold in top mass reconstruction
                        if (tree.Jet_PtReg[tree.hJidxCMVA[0]] < 30 and bjet1.Pt() > 30) or (tree.Jet_PtReg[tree.hJidxCMVA[0]] > 30 and bjet1.Pt() < 30):
                            bjet1.SetPtEtaPhiM(tree.Jet_PtReg[tree.hJidxCMVA[0]],treeJet_eta[hJidx0],treeJet_phi[hJidx0],getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))[hJidx0] * treeJet_bReg[hJidx0])
                        if (tree.Jet_PtReg[tree.hJidxCMVA[1]] < 30 and bjet2.Pt() > 30) or (tree.Jet_PtReg[tree.hJidxCMVA[1]] > 30 and bjet2.Pt() < 30):
                            bjet2.SetPtEtaPhiM(tree.Jet_PtReg[tree.hJidxCMVA[1]],treeJet_eta[hJidx1],treeJet_phi[hJidx1],getattr(tree, 'Jet_mass_{s}{d}'.format(s=syst, d=Q))[hJidx1] * treeJet_bReg[hJidx1])
                        

                        jets = [bjet1, bjet2]
                        tmp = self.computeTopMass(lep,met,jets)
                        
                        ########
                        # fill systematics
                        ########

                        # in cases sys is broken, set it to nominal value
                        if tmp == -99:
                            tmp = self.branchBuffers['top_mass'][0]


                        self.branchBuffers[top_massSyst][0] = tmp


                        if top_mass_min == -99:
                            top_mass_min = tmp
                            top_mass_max = tmp
                        else:
                            top_mass_min = min(top_mass_min,tmp)
                            top_mass_max = max(top_mass_max,tmp)
            elif self.propagateJES and self.nano and self.sample.type == 'DATA':
                top_mass_min = tmp
                top_mass_max = tmp
                print 'top_mass_min is', top_mass_min

            self.branchBuffers['top_mass_minmax_Down'][0] = top_mass_min
            self.branchBuffers['top_mass_minmax_Up'][0] = top_mass_max

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

    def computeTopMass(self, lep, met, jets):
        #neutrino = self.getNu4Momentum(lep, met)
        bjet = TLorentzVector()
        minDR = 99
        for jet in jets:
            if (jet.Pt() > 30): # and jet.bTagCSV > CSVL and jet.puID > 0 and jet.Id > 0? how?
                dR = jet.DeltaR(lep)
                if (dR < minDR):
                    minDR = dR
                    bjet = jet
        if (bjet.Pt() <= 0):
            return -99
        top = lep + met + bjet
        return top.M()
