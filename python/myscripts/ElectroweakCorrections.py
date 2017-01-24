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
#  apply corrections text file
# **********************************************************************************************************************
class CorrectionFromFile:
    def __init__(self):
        self.corrections = {}

    def loadCSV(self, name, csvFileName):
        self.corrections[name] = np.genfromtxt(open(csvFileName, "rb"), delimiter="  ", comments='#')

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


# **********************************************************************************************************************
#  load correction text files
# **********************************************************************************************************************
EWK = CorrectionFromFile()

ewkCorrections = [
    {'name': 'V_pt', 'inputTreeBranch': 'V_pt', 'outputTreeBranch': 'EWKandQCD_corrWeight', 'file': '../weights/Zll/distributions/dat.ptv'},
]

for ewkCorrection in ewkCorrections:
    EWK.loadCSV(ewkCorrection['name'], ewkCorrection['file'])


# ----------------------------------------------------------------------------------------------------------------------
# load input/output ROOT files
# ----------------------------------------------------------------------------------------------------------------------
ifile = ROOT.TFile.Open(sys.argv[1], "READ")
ofile = ROOT.TFile(sys.argv[2], "RECREATE")

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
inputTreeVariables = {}
for ewkCorrection in ewkCorrections:
    inputTreeVariables[ewkCorrection['inputTreeBranch']] = np.array([0], dtype='f')
    tree.SetBranchAddress(ewkCorrection['inputTreeBranch'], inputTreeVariables[ewkCorrection['inputTreeBranch']])

# define additional output branches
ewkCorrectionBranches = {}
for ewkCorrection in ewkCorrections:
    ewkCorrectionBranches[ewkCorrection['outputTreeBranch']] = np.array([0], dtype=float)
    obranch = otree.Branch(ewkCorrection['outputTreeBranch'], ewkCorrectionBranches[ewkCorrection['outputTreeBranch']], ewkCorrection['outputTreeBranch'] + '/D')

# ----------------------------------------------------------------------------------------------------------------------
# apply corrections
# ----------------------------------------------------------------------------------------------------------------------
nEntries = tree.GetEntries()
print "nEntries = ", nEntries
for entry in range(nEntries):
    tree.GetEntry(entry)
    for ewkCorrection in ewkCorrections:
        ewkCorrectionBranches[ewkCorrection['outputTreeBranch']][0] = EWK.getCorrection(ewkCorrection['inputTreeBranch'], inputTreeVariables[ewkCorrection['inputTreeBranch']][0])
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