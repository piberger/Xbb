#!/usr/bin/env python
from optparse import OptionParser
import sys
import pickle
import ROOT
import zlib
import base64
ROOT.gROOT.SetBatch(True)
from myutils import BetterConfigParser, mvainfo, ParseInfo, TreeCache

import os
if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

# samples folder
samplesPath = "/scratch/p/"

#load config
config = BetterConfigParser()
config.read('PirminZllHbb13TeV2016config/paths.ini')
config.read('PirminZllHbb13TeV2016config/samples_nosplit.ini')

samplesinfo = "PirminZllHbb13TeV2016config/samples_nosplit.ini"
info = ParseInfo(samplesinfo, samplesPath)

print info

samples = []
samples = info.get_samples(['DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8', 'Pt100to250ZJetsNLO_udscg', 'Pt100to250ZJetsNLO_1b', 'Pt100to250ZJetsNLO_2b'])

for sample in samples:
    print sample.name, "\x1b[31m", sample.subcut, "\x1b[0m"

