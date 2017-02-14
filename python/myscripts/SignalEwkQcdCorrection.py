#!/usr/bin/env python
import ROOT
import sys
import numpy as np

# RUN:
# ./SignalEwkQcdCorrection.py input.root output.root applyCorrection(bool)
#

# **********************************************************************************************************************
#  Class to apply corrections text file
# **********************************************************************************************************************
class TreeCopierWithCorrectionFromFile:
    def __init__(self):
        self.correctionFiles = {}
        self.correctionFileIndexColumns = {}
        self.delimiter = '  '
        self.commentsMarker = '#'
        self.outputBranches = []
        self.corrections = {}
        self.inputBranchName = None

    def loadCorrectionFiles(self, corrections):
        for correction in corrections:
            with open(correction['file'], 'rb') as correctionFile:
                self.correctionFiles[correction['name']] = np.genfromtxt(correctionFile,
                                 delimiter=correction['delimiter'] if 'delimiter' in correction else self.delimiter,
                                 comments=correction['comments'] if 'comments' in correction else self.commentsMarker)
                self.correctionFileIndexColumns[correction['name']] = self.correctionFiles[correction['name']][:, 0]

    def setInputBranch(self, inputBranchName):
        self.inputBranchName = inputBranchName

    def addOutputBranch(self, branchName, branchFormula):
        self.outputBranches.append({'name': branchName, 'formula': branchFormula})

    def getCorrection(self, v):
        corr = {}

        # select corresponding line from the table with correct Vpt
        for correctionName, correctionFile in self.correctionFiles.iteritems():
            index = self.correctionFileIndexColumns[correctionName].searchsorted(v)
            if index > len(correctionFile) - 1:
                index = len(correctionFile) - 1
            corr[correctionName] = correctionFile[index]

        return corr

    # ------------------------------------------------------------------------------------------------------------------
    # copy the tree and add new branch with weight from text file
    # ------------------------------------------------------------------------------------------------------------------
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

        # --------------------------------------------------------------------------------------------------------------
        # set branches
        # --------------------------------------------------------------------------------------------------------------

        # set branch addresses for input variable (1D at the moment!)
        inputBrancheValue = np.array([0], dtype='f')
        tree.SetBranchAddress(self.inputBranchName, inputBrancheValue)

        # define additional output branches
        outputBranchValues = {}
        for outputBranch in self.outputBranches:
            outputBranchValues[outputBranch['name']] = np.array([0], dtype=float)
            obranch = otree.Branch(outputBranch['name'], outputBranchValues[outputBranch['name']],
                                   outputBranch['name'] + '/D')

        # --------------------------------------------------------------------------------------------------------------
        # apply corrections
        # --------------------------------------------------------------------------------------------------------------
        nEntries = tree.GetEntries()
        print "nEntries = ", nEntries
        for entry in range(nEntries):
            if entry % 10000 == 0:
                print "processing entry: %d"%entry

            tree.GetEntry(entry)

            # add all output branches
            for outputBranch in self.outputBranches:
                corrData = self.getCorrection(inputBrancheValue[0])
                outputBranchValues[outputBranch['name']][0] = outputBranch['formula'](corrData) if applyNNLO else 1.0

            otree.Fill()

        # --------------------------------------------------------------------------------------------------------------
        # write and close files
        # --------------------------------------------------------------------------------------------------------------
        print "writing to file..."
        ofile.cd()
        otree.Write()

        ofile.Close()
        ifile.Close()

        print "done."

    # just print out the correction weights as function of Vpt
    def test(self, silent=False):
        outputTable = []
        for Vpt in range(0, 500):
            outputString = "%d "%Vpt
            for outputBranch in self.outputBranches:
                if not silent:
                    print "Vpt:",Vpt
                corrData = self.getCorrection(Vpt)
                if not silent:
                    print "corrdata:", corrData
                outputString += "%0.7f "%(outputBranch['formula'](corrData))
            if not silent:
                outputTable.append(outputString)

        if not silent:
            for outputString in outputTable:
                print outputString

# **********************************************************************************************************************
#  main
# **********************************************************************************************************************
theTreeCopier = TreeCopierWithCorrectionFromFile()

theTreeCopier.setInputBranch('V_pt')

# define text files which include the corrections
correctionFiles = [
    {
        'name': 'deltaEWK',
        'file': '../weights/Zll/distributions/dat.ptv',
        'delimiter': '  '  # two spaces here!
    },
    {
        'name': 'nnloQCD',
        'file': '../weights/Zll/nnlo_qcd/ze.ptv',
        'delimiter': ' '  # just one space
    }
]
theTreeCopier.loadCorrectionFiles(correctionFiles)

# define new branches
sigmaTotal = 0.10155859E+02
COLUMN_EWK_NLO = 5
COLUMN_EWK_BORN = 1
COLUMN_QCD_NNLO = 2

# see https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHXSWGVHYR4
theTreeCopier.addOutputBranch(
    branchName='SignalCorr_nloEWK_nnloQCD',
    branchFormula=lambda x: sigmaTotal * x['nnloQCD'][COLUMN_QCD_NNLO] * (1.0 + x['deltaEWK'][COLUMN_EWK_NLO] / x['deltaEWK'][COLUMN_EWK_BORN])
)

if len(sys.argv) == 4:
    applyNNLO = sys.argv[3].lower().strip() == 'true'
    theTreeCopier.copy(inputFileName=sys.argv[1], outputFileName=sys.argv[2], applyNNLO=applyNNLO)
elif len(sys.argv) == 2 and sys.argv[1] == 'test':
    print "running test:"
    theTreeCopier.test()
else:
    print "syntax: {file} input.root output.root useNNLO".format(file=sys.argv[0] if len(sys.argv) > 0 else './file.py')



