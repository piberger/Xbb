#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import ROOT
ROOT.gROOT.SetBatch(True)
from myutils.FileList import FileList
from myutils import BetterConfigParser, ParseInfo, LeptonSF
from myutils.sampleTree import SampleTree
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools
from myutils.samplesclass import Sample
from myutils.BranchList import BranchList

# load configuration and list of used samples
config = XbbConfigReader.read('Zvv2017')
sampleInfo = ParseInfo(config=config)

usedSamples = sampleInfo.get_samples(XbbConfigTools(config).getMC())
#usedSamples = sampleInfo.get_samples(['ZJetsHT100', 'ZH_Znunu'])

# some samples come from same set of ROOT trees (=have same identifier)
# -> find list of unique identifiers to avoid to process same tree file twice
sampleIdentifiers = sampleInfo.getSampleIdentifiers()
usedSampleIdentifiers = ParseInfo.filterIdentifiers(sampleIdentifiers, usedSamples)

# from which step to take the root trees
directory = config.get('Directories', 'MVAout')

signalRegionSelection = config.get('Cuts', 'Sig') 
signalNames = eval(config.get('Plot_general', 'allSIG'))

#weightExpression = "weight"
weightExpression = config.get('Weights','weightF') 

taggerExpression = "Jet_btagDeepB[hJidx[1]]"
#taggerExpression = "BDT_DNN_XBB_2017_October31_Znn_v1.Nominal"

# process all samples
roc_data = []
for i, sampleIdentifier in enumerate(usedSampleIdentifiers):
    print("\x1b[42mSAMPLE", i, "/", len(usedSampleIdentifiers),"\x1b[0m")

    # in case the distinction between subsamples is needed, one could access the cut definitions for the subsamples
    # with: subsample.subcut for subsample in subsamples
    sample     = sampleInfo.getFullSample(sampleIdentifier)
    subsamples = sampleInfo.getSubsamples(sampleIdentifier)

    sampleTree = SampleTree({'sample': sample, 'folder': directory}, config=config)

    # since we load all trees, we can compute the factor to scale cross section to luminosity directly (otherwise write it to ntuples 
    # first and then use it as branch, or compute it with full set of trees before)
    scaleXStoLumi = sampleTree.getScale(sample)

    # enable only used branches!
    # this will speed up processing a lot
    sampleTree.enableBranches(BranchList([signalRegionSelection, weightExpression, taggerExpression]).getListOfBranches())

    # this will create the TTreeformula objects
    sampleTree.addFormula(signalRegionSelection)
    sampleTree.addFormula(weightExpression)
    sampleTree.addFormula(taggerExpression)

    isSignal = 1 if sample.name in signalNames else 0

    for event in sampleTree:

        # for all events passing the signal selection
        if sampleTree.evaluate(signalRegionSelection):

            # evaluate quantity (tagger, weight etc.)
            roc_data.append([sampleTree.evaluate(taggerExpression), sampleTree.evaluate(weightExpression) * scaleXStoLumi, isSignal])

# compute something, e.g. ROC curve

print("# MC events:", len(roc_data))
roc_data.sort(key=lambda x: x[0], reverse=True)
print("sorted!")

roc_histo   = ROOT.TH1D('roc','',100,0.0,1.0)
roc_histo_n = ROOT.TH1D('roc_n','',100,0.0,1.0)
roc_histo.Sumw2()
roc_histo_n.Sumw2()

roc_curve = [[0.0, 0.0]]
nSig      = 0.0
nBkg      = 0.0
for d in roc_data:
    if d[2] == 1:
        nSig += d[1]
    else:
        nBkg += d[1]
    roc_curve.append([nSig,nBkg])

for d in roc_curve:
    sEff = d[0]/roc_curve[-1][0]
    bRej = 1.0 - d[1]/roc_curve[-1][1]

    roc_histo.Fill(sEff, bRej)
    roc_histo_n.Fill(sEff, 1.0)

roc_histo.Divide(roc_histo_n)

c1 = ROOT.TCanvas("c1","",500,500)
roc_histo.Draw("HIST")
c1.SaveAs("roc_curve.png")

