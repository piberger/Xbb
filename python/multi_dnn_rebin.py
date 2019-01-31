#!/usr/bin/env python
from __future__ import print_function
import ROOT
import array
from optparse import OptionParser
import sys
from myutils.sampleTree import SampleTree
from myutils.readConfig import readConfig

# parse options
parser = OptionParser()
parser.add_option("-s","--sampleIdentifier", dest="sampleIdentifier", default="DoubleMuon", help="sample identifier (no subsample!)")
parser.add_option("-b","--branch", dest="branch", default="ZllBDT_highpt_Multi_DNN2017", help="multi-DNN branch prefix, see example")
parser.add_option("-T","--tag", dest="tag", default="Zll2017")
parser.add_option("-n","--nBins", dest="nBins", default="7")
(opts, args) = parser.parse_args(sys.argv)

# read config
config = readConfig.fromTag(opts.tag)

# read samples
sampleTree = SampleTree({'name': opts.sampleIdentifier, 'folder': config.get('Directories', 'MVAout')}, splitFilesChunkSize=-1, config=config)

# speed up processing by enabling only used branches
sampleTree.enableBranches([opts.branch + "*"])
sampleTree.addFormula("argmax", opts.branch + "_argmax.Nominal")
sampleTree.addFormula("max", opts.branch + "_max.Nominal")

# fill histograms
nBins = int(opts.nBins)
histograms = [ROOT.TH1F("h%d"%i, "h%d"%i, 1000, 0.0, 1.0) for i in range(nBins)]
for event in sampleTree:
    nBin = int(sampleTree.evaluate("argmax"))
    if nBin < nBins:
        histograms[nBin].Fill(sampleTree.evaluate("max"))

# compute quantiles
binListCR = []
for i in range(nBins):
    nq = 100
    xq = array.array('d',[j/100.0+0.0001 for j in range(100)]) 
    yq = array.array('d', [0.0]*nq)
    histograms[i].GetQuantiles(nq-1, yq, xq)

    print("bin",i,"mean=",histograms[i].GetMean(),"rms=",histograms[i].GetRMS(),"int=",histograms[i].Integral(),"q60=",yq[60],"q90=",yq[90])
    binListCR += [i*1.0, i+yq[60], i+yq[90]]

print("CR bins:")
print(", ".join(["%1.6f"%x for x in binListCR]))


