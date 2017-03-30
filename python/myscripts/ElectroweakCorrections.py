#!/usr/bin/env python
import ROOT
import sys
import numpy as np

# RUN:
# ./ElectroweakCorrections.py input.root output.root
#

# **********************************************************************************************************************
# CSV format of EWK corrections:

# column  1: kinematical quantity on x-axis
# column  2: Monte Carlo average for the Born cross-section
# column  3: Monte Carlo error   for the Born cross-section
# column  4: Monte Carlo average for the complete cross-section
# column  5: Monte Carlo error   for the complete cross-section
# column  6: Monte Carlo average for virt+real ew cross-section
# column  7: Monte Carlo error   for virt+real ew cross-section
# column  8: Monte Carlo average for virt+real QCD cross-section
# column  9: Monte Carlo error   for virt+real QCD cross-section
# column 10: Monte Carlo average for incoming photon cross-section
# column 11: Monte Carlo error   for incoming photon cross-section
# column 12: Monte Carlo average for incoming gluon cross-section
# column 13: Monte Carlo error   for incoming gluon cross-section

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
    def copy(self, inputFileName, outputFileName, applyNNLO):

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

        # set branch addresses for input variables
        inputTreeBranches = {}
        for correction in corrections:
            inputTreeBranches[correction['inputBranch']] = np.array([0], dtype='f')
            tree.SetBranchAddress(correction['inputBranch'], inputTreeBranches[correction['inputBranch']])

        # define additional output branches
        outputBranches = {}
        for correction in corrections:
            outputBranches[correction['outputBranch']] = np.array([0], dtype=float)
            obranch = otree.Branch(correction['outputBranch'], outputBranches[correction['outputBranch']],
                                   correction['outputBranch'] + '/D')

        # ----------------------------------------------------------------------------------------------------------------------
        # apply corrections
        # ----------------------------------------------------------------------------------------------------------------------
        nEntries = tree.GetEntries()
        print "nEntries = ", nEntries
        for entry in range(nEntries):
            #if entry > 100:
            #    break
            if entry % 10000 == 0:
                print "processing entry: %d"%entry

            tree.GetEntry(entry)
            for correction in corrections:
                branchName = correction['inputBranch']
                if eval(applyNNLO):
                    outputBranches[correction['outputBranch']][0] = self.getCorrection(branchName, inputTreeBranches[branchName][0])
                else:
                    outputBranches[correction['outputBranch']][0] = 1
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

corrections = [
    {'name': 'V_pt', 'inputBranch': 'V_pt', 'outputBranch': 'EWKandQCD_corrWeight', 'file': '../weights/Zll/distributions/dat.ptv'},
]

theTreeCopier.loadCorrections(corrections)

if len(sys.argv) == 4:
    theTreeCopier.copy(sys.argv[1], sys.argv[2], sys.argv[3])#sys.argv[3] should be the string "True" or "False"
else:
    print "syntax: {file} input.root output.root useNNLO".format(file=sys.argv[0] if len(sys.argv) > 0 else './file.py')
