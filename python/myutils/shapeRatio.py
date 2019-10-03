#!/usr/bin/env python
from __future__ import print_function
import ROOT
ROOT.gROOT.SetBatch(True)
import sys

f1 = ROOT.TFile.Open(sys.argv[1], "READ")
f2 = ROOT.TFile.Open(sys.argv[2], "READ")

h1 = f1.Get("summedMcHistograms")
h2 = f2.Get("summedMcHistograms")

h2.Divide(h1)
h2.SetStats(0)
c1 = ROOT.TCanvas("c1","c1",500,300)
h2.SetTitle("ratio" if len(sys.argv) < 5 else sys.argv[4])
h2.GetYaxis().SetRangeUser(0.5, 1.5)
#h2.GetYaxis().SetRangeUser(0.0, 2.0)
#h2.Rebin(4)
#h2.Scale(0.25)
h2.GetYaxis().SetRangeUser(0.0, 2.0)
h2.Draw("E")
ROOT.gPad.Modified()
ROOT.gPad.Update()
tl = ROOT.TLine(ROOT.gPad.GetUxmin(), 1, ROOT.gPad.GetUxmax(), 1)
tl.SetLineColorAlpha(ROOT.kGray+2,0.7)
tl.Draw("same")
ROOT.gPad.Modified()
ROOT.gPad.Update()
c1.SaveAs(sys.argv[3])
c1.SaveAs('.'.join(sys.argv[3].split('.')[:-1])+'.root')
