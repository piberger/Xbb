#!/usr/bin/env python
from __future__ import print_function
from myutils import sampleTree.SampleTree as SampleTree
import ROOT
import argparse
import os
import sys
import time

#------------------------------------------------------------------------------
# calculate efficiency of HLT
#------------------------------------------------------------------------------
class TriggerEfficiencies(object):

    def __init__(self, sampleTree = None):
        self.sampleTree = sampleTree

    def calculateEfficiency(self, variable, range=[0, 1000, 100], tightCut='1', looseCut='1', outputFileName='trigeff.root'):
       
        # add formulas for cuts
        self.sampleTree.addFormula('variable', variable)
        self.sampleTree.addFormula('tight', tightCut)
        self.sampleTree.addFormula('loose', looseCut)

        # prepare output file and histograms
        outputFile = ROOT.TFile(outputFileName,'recreate')
        histogramPassLoose = ROOT.TH1D('histogramPassLoose','passed cut: ' + looseCut, range[2], range[0], range[1])
        histogramPassTight = ROOT.TH1D('histogramPassTight','passed cut: ' + tightCut, range[2], range[0], range[1])
        histogramEfficiency = ROOT.TH1D('histogramEfficiency','Trigger efficiency', range[2], range[0], range[1])
        histogramPassLoose.Sumw2()
        histogramPassTight.Sumw2()

        if self.sampleTree:
            # count events passing the loose/tight cuts
            nEntry = 0
            for event in self.sampleTree:
                passLoose = self.sampleTree.evaluate('loose')
                passTight = self.sampleTree.evaluate('tight')
                var = self.sampleTree.evaluate('variable')
                if passLoose:
                    histogramPassLoose.Fill(var)
                if passTight:
                    histogramPassTight.Fill(var)
                nEntry += 1
            
            # calculate efficiency
            # divide histograms with binomial errors
            histogramEfficiency.Divide(histogramPassTight, histogramPassLoose, 1, 1, "B")

        outputFile.Write()
        outputFile.Close()

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
# example how to call
# ./trigger_efficiencies.py -S ... -v '(nJet>0)*Max$(Jet_pt)' -r 300,800,100 -o trig_eff_500.root -l HLT_BIT_HLT_PFJet400_v -t HLT_BIT_HLT_PFJet500_v
#------------------------------------------------------------------------------
if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', action='store', dest='sample', help='sample textfile(s) with dataset names')
    parser.add_argument('-v', action='store', dest='variable', default='(nJet>0)*Max$(Jet_pt)', help='variable to computer the efficiency differentially of')
    parser.add_argument('-r', action='store', dest='range', default='0,1000,100', help='min,max,nbins of variable to create histogram')
    parser.add_argument('-o', action='store', dest='output', default='trigeff.root', help='output .root file')
    parser.add_argument('-l', action='store', dest='loose', default='HLT_BIT_HLT_PFJet400_v', help='loose cut')
    parser.add_argument('-t', action='store', dest='tight', default='HLT_BIT_HLT_PFJet500_v', help='loose cut')
    args = parser.parse_args()

    # read samples
    sampleTree = SampleTree(args.sample)
    if not sampleTree:
        print ('creating sample tree failed!')
        exit(0)

    # calculate efficiency
    triggerEfficienciesCalculator = TriggerEfficiencies(sampleTree)
    r = [x.strip() for x in args.range.split(',')]    
    histogramRange = [float(r[0]), float(r[1]), int(r[2])]
    triggerEfficienciesCalculator.calculateEfficiency(variable=args.variable, range=histogramRange, tightCut=args.tight, looseCut=args.loose, outputFileName=args.output)

    print ("done. Knowing the efficiency you triggered with fills you with determination.")

