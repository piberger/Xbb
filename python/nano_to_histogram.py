#!/usr/bin/env python
from __future__ import print_function
import ROOT
import glob
import sys
import subprocess
import os
import argparse

parser = argparse.ArgumentParser(description='Create histogram from NanoAOD')
parser.add_argument('--min', default="0") 
parser.add_argument('--max', default="1000") 
parser.add_argument('--nbins', default="100") 
parser.add_argument('--var')
parser.add_argument('--cut', default='1')
parser.add_argument('--input')
parser.add_argument('--output')

args = parser.parse_args()

if os.path.isfile(args.output):
    print("file exists:", args.output)
    sys.exit(1)

outFile =  ROOT.TFile.Open(args.output, "RECREATE")
genEventSumwHistogram = ROOT.TH1D("genEventSumw","genEventSumw",1,0,1)

f1 = ROOT.TFile.Open(args.input, "READ")
genEventSumw = 0.0
for run in f1.Runs:
    if hasattr(run, "genEventSumw"):
        genEventSumw += run.genEventSumw
    elif hasattr(run, "genEventSumw_"):
        # NanoAOD V6 workaround
        genEventSumw += run.genEventSumw_
    else:
        raise Exception("genEventSumw not found!")
genEventSumwHistogram.SetBinContent(1, genEventSumw)
h1 = ROOT.TH1D("h1","h1",int(args.nbins),float(args.min),float(args.max))
tree = f1.Events
n = tree.Draw("{v}>>{h}".format(v=args.var, h="h1"), "({c})*genWeight".format(c=args.cut))
h1.SetDirectory(outFile)
genEventSumwHistogram.SetDirectory(outFile)
outFile.Write()
outFile.Close()
print("done, n=", n)


