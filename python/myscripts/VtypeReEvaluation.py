#!/usr/bin/env python
import ROOT
import sys
import numpy as np

#!/usr/bin/env python
import ROOT
import sys
import numpy as np
from array import array

# RUN:
#
from array import array
#

# **********************************************************************************************************************
#

class CorrectionType:
    KINEMATIC, MC_AVERAGE_BORN, MC_ERROR_BORN, MC_AVERAGE_COMPLETE, MC_ERROR_COMPLETE,MC_AVERAGE_EW, MC_ERROR_EW, \
    MC_AVERAGE_QCD, MC_ERROR_QCD, MC_AVERAGE_INC_PHOTON, MC_ERROR_INC_PHOTON, MC_AVERAGE_INC_GLU, MC_ERROR_INC_GLU = range(13)

# **********************************************************************************************************************
#  Class to apply corrections text file
# **********************************************************************************************************************
class TreeCopierWithCorrectionFromFile:
    def __init__(self):
        self.corrections = {}
        self.delimiter = '  '
        self.commentsMarker = '#'

    def loadCorrections(self, corrections):
        for correction in corrections:
            with open(correction['file'], 'rb') as correctionFile:
                self.corrections[correction['name']] = np.genfromtxt(correctionFile, delimiter=self.delimiter, comments=self.commentsMarker)

    def getCorrection(self, name, v):
        index = self.corrections[name][:, CorrectionType.KINEMATIC].searchsorted(v)
        if index > len(self.corrections[name]) - 1:
            index = len(self.corrections[name]) - 1

        try:
            corr = self.corrections[name][index, CorrectionType.MC_AVERAGE_COMPLETE] / self.corrections[name][index, CorrectionType.MC_AVERAGE_BORN]
        except Exception as e:
            print "ERROR:", e, "=> set weight to 1"
            corr = 1

        return corr

    # ----------------------------------------------------------------------------------------------------------------------
    # copy the tree and add new branch with weight from text file
    # ----------------------------------------------------------------------------------------------------------------------
    def copy(self, inputFileName, outputFileName):

        ifile = ROOT.TFile.Open(inputFileName, "READ")
        ofile = ROOT.TFile.Open(outputFileName, "RECREATE")

        # copy other file objects
        ifile.cd()
        obj = ROOT.TObject
        for key in ROOT.gDirectory.GetListOfKeys():
            ifile.cd()
            obj = key.ReadObj()
            if obj.GetName() == 'tree':
                continue
            ofile.cd()
            obj.Write(key.GetName())

        ifile.cd()
        tree = ifile.Get('tree')
        ofile.cd()

        # clone TTree
        otree = tree.CloneTree(0)

        # ----------------------------------------------------------------------------------------------------------------------
        # set branches
        # ----------------------------------------------------------------------------------------------------------------------



        Vtype_new = array('f',[0])
        otree.Branch('Vtype_new',Vtype_new,'Vtype_new/F')

        vLeptonsBranches={}
        ##define Vleptons branch
        vLeptonsvar = ['pt', 'eta', 'phi', 'relIso03', 'relIso04']
        for var in vLeptonsvar:
            #vLeptonsBranches[var] = np.array([0]*2, dtype=float)
            vLeptonsBranches[var] = np.zeros(21, dtype=np.float32)
            obranch = otree.Branch('vLeptons_new_%s'%var, vLeptonsBranches[var], 'vLeptons_new_%s[2]/F'%var)

        #vLeptons_new_pt = array('f',[0]*2)
        #otree.Branch('vLeptons_new_pt',vLeptons_new_pt,'vLeptons_new_pt[2]/F')

        #vLeptons_new_eta = array('f',[0]*2)
        #otree.Branch('vLeptons_new_eta',vLeptons_new_eta,'vLeptons_new_eta[2]/F')

        #vLeptons_new_phi = array('f',[0]*2)
        #otree.Branch('vLeptons_new_phi',vLeptons_new_phi,'vLeptons_new_phi[2]/F')

        #vLeptons_new_relIso03 = array('f',[0]*2)
        #otree.Branch('vLeptons_new_relIso03',vLeptons_new_relIso03,'vLeptons_new_relIso03[2]/F')

        #vLeptons_new_relIso04 = array('f',[0]*2)
        #otree.Branch('vLeptons_new_relIso04',vLeptons_new_relIso04,'vLeptons_new_relIso04[2]/F')


        #do not have enough variable to do this
        #def ele_mvaEleID_Trig_preselection(x) :
            #return (tree.selLeptons_pt[x] >15 and abs(tree.selLeptons_etaSc[x]) < 1.4442 and tree.selLeptons_eleSieie[x] < 0.012 and tree.selLeptons_eleHoE[x] < 0.09 and (tree.selLeptons_eleEcalClusterIso[x]/tree.selLeptons_pt[x]) < 0.37 and (tree.selLeptons_eleHcalClusterIso[x]/tree.selLeptons_pt[x]) < 0.25 and (tree.selLeptons_dr03TkSumPt[x]/tree.selLeptons_pt[x]) < 0.18 and abs(tree.selLeptons_etaSc-tree.selLeptons_eta) < 0.0095 and abs(tree.selLeptons_phiSc-tree.selLeptons_phi) < 0.065 ) or (abs(tree.selLeptons_etaSc[x]) > 1.5660 and tree.selLeptons_eleSieie[x] < 0.033 and tree.selLeptons_eleHoE[x] <0.09 and (tree.selLeptons_eleEcalClusterIso[x]/tree.selLeptons_pt[x]) < 0.45 and (tree.selLeptons_eleHcalClusterIso[x]/tree.selLeptons_pt[x]) < 0.28 and (tree.selLeptons_dr03TkSumPt[x]/tree.selLeptons_pt[x]) < 0.18)


        # ----------------------------------------------------------------------------------------------------------------------
        # define all the lambda function
        # ----------------------------------------------------------------------------------------------------------------------

        #include the Vytpe reco here
        zEleSelection = lambda x : tree.selLeptons_pt[x] > 15 and tree.selLeptons_eleMVAIdSppring16GenPurp[x] >= 2
        zMuSelection = lambda x : tree.selLeptons_pt[x] > 15 and  tree.selLeptons_looseIdPOG[x] and tree.selLeptons_relIso04[x] < 0.25

        # ----------------------------------------------------------------------------------------------------------------------
        # apply corrections
        # ----------------------------------------------------------------------------------------------------------------------
        nEntries = tree.GetEntries()
        print "nEntries = ", nEntries
        for entry in range(nEntries):
            if entry > 100:
                break
            if entry % 10000 == 0:
                print "processing entry: %d"%entry

            tree.GetEntry(entry)

            #Variable to store Vtype and leptons info
            Vtype_new_ = -1
            V_mass_new = -1

            #lep_pt = []
            #lep_eta = []
            #lep_phi = []
            #lep_iso3 = []
            #lep_iso4 = []


            vLeptons_new = []
            #get all the lepton index
            lep_index = range(len(tree.selLeptons_pt))
            selectedElectrons = [i for i in  lep_index if abs(tree.selLeptons_pdgId[i]) == 11]
            selectedMuons =  [i for i in lep_index if abs(tree.selLeptons_pdgId[i]) == 13]

            zElectrons=[x for x in selectedElectrons if zEleSelection(x) ]
            zMuons=[x for x in selectedMuons if zMuSelection(x) ]

            zMuons.sort(key=lambda x:tree.selLeptons_pt[x],reverse=True)
            zElectrons.sort(key=lambda x:tree.selLeptons_pt[x],reverse=True)

            if len(zMuons) >=  2 :
                if tree.selLeptons_pt[zMuons[0]] > 20:
                    for i in zMuons[1:]:
                        if  tree.selLeptons_charge[zMuons[0]]*tree.selLeptons_charge[i] < 0:
                            if tree.Vtype == 1:
                                print 'problem 1'
                            Vtype_new_ = 0

                            for var in vLeptonsvar:
                                vLeptonsBranches[var][0] = getattr(tree,'vLeptons_%s'%var)[0]
                                vLeptonsBranches[var][1] = getattr(tree,'vLeptons_%s'%var)[1]

                            #lep_pt = [tree.selLeptons_pt[zMuons[0]],tree.selLeptons_pt[i]]
                            #lep_eta = [tree.selLeptons_eta[zMuons[0]],tree.selLeptons_eta[i]]
                            #lep_phi = [tree.selLeptons_phi[zMuons[0]],tree.selLeptons_phi[i]]
                            #lep_iso3 = [tree.selLeptons_relIso03[zMuons[0]],tree.selLeptons_relIso03[i]]
                            #lep_iso4 = [tree.selLeptons_relIso04[zMuons[0]],tree.selLeptons_relIso04[i]]
                            break
            elif len(zElectrons) >=  2 :
                if tree.selLeptons_pt[zElectrons[0]] > 20:
                    for i in zElectrons[1:]:
                        if  tree.selLeptons_charge[zElectrons[0]]*tree.selLeptons_charge[i] < 0:
                            if tree.Vtype == 0:
                                print 'problem 2'
                            Vtype_new_ = 1
                            for var in vLeptonsvar:
                                vLeptonsBranches[var][0] = getattr(tree,'vLeptons_%s'%var)[0]
                                vLeptonsBranches[var][1] = getattr(tree,'vLeptons_%s'%var)[1]
                            #lep_pt = [tree.selLeptons_pt[zElectrons[0]],tree.selLeptons_pt[i]]
                            #lep_eta = [tree.selLeptons_eta[zElectrons[0]],tree.selLeptons_eta[i]]
                            #lep_phi = [tree.selLeptons_phi[zElectrons[0]],tree.selLeptons_phi[i]]
                            #lep_iso3 = [tree.selLeptons_relIso03[zElectrons[0]],tree.selLeptons_relIso03[i]]
                            #lep_iso4 = [tree.selLeptons_relIso04[zElectrons[0]],tree.selLeptons_relIso04[i]]
                            break
            else:
                Vtype_new_ = tree.Vtype
                for var in vLeptonsvar:
                    vLeptonsBranches[var][0] = getattr(tree,'vLeptons_%s'%var)[0]
                    vLeptonsBranches[var][1] = getattr(tree,'vLeptons_%s'%var)[1]
                #lep_pt = [tree.vLeptons_pt[0],tree.vLeptons_pt[1]]
                #lep_eta = [tree.selLeptons_eta[0],tree.selLeptons_eta[1]]
                #lep_phi = [tree.selLeptons_phi[0],tree.selLeptons_phi[1]]
                #lep_iso3 = [tree.selLeptons_relIso03[0],tree.selLeptons_relIso03[1]]
                #lep_iso4 = [tree.selLeptons_relIso04[0],tree.selLeptons_relIso04[1]]
                #V_mass_new_ = tree.V_mass

	        #event.V=sum(map(lambda x:x.p4(), event.vLeptons),ROOT.reco.Particle.LorentzVector(0.,0.,0.,0.))
	        #if event.Vtype > 1 :
            #    event.V+=ROOT.reco.Particle.LorentzVector(event.met.p4().x(),event.met.p4().y(),0,event.met.p4().pt())
            #if event.V.Et() > event.V.pt() :
            #    event.V.goodMt = sqrt(event.V.Et()**2-event.V.pt()**2)
            #else :
            #    event.V.goodMt = -sqrt(-event.V.Et()**2+event.V.pt()**2)

            Vtype_new[0] = Vtype_new_

            #print 'debug loop'
            #for var in vLeptonsvar:
            #    print 'var is', var
            #    print vLeptonsBranches[var][0]
            #    print vLeptonsBranches[var][1]

            otree.Fill()

        # ----------------------------------------------------------------------------------------------------------------------
        # write and close files
        # ----------------------------------------------------------------------------------------------------------------------
        print "writing to file..."
        ofile.cd()
        otree.Write()

        ofile.Close()
        ifile.Close()

        print "done."

# **********************************************************************************************************************
#  main
# **********************************************************************************************************************
theTreeCopier = TreeCopierWithCorrectionFromFile()

#theTreeCopier.loadCorrections(corrections)

#if len(sys.argv) == 4:
#    theTreeCopier.copy(sys.argv[1], sys.argv[2], sys.argv[3])#sys.argv[3] should be the string "True" or "False"

theTreeCopier.copy(sys.argv[1], sys.argv[2])

#else:
#    print "syntax: {file} input.root output.root useNNLO".format(file=sys.argv[0] if len(sys.argv) > 0 else './file.py')
