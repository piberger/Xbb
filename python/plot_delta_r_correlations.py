#!/usr/bin/env python
from __future__ import print_function
from myutils.sampleTree import SampleTree as SampleTree
from myutils.CorrelationPlot import CorrelationPlot as CorrelationPlot
import ROOT
import argparse
import os
import sys
import time

#------------------------------------------------------------------------------
# plot MC correlation of deltaR(reconstructed) vs. deltaR(gen)
#------------------------------------------------------------------------------
if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', action='store', dest='sample', help='sample textfile(s) with dataset names')
    parser.add_argument('-o', action='store', dest='output', default='delta_r_correlation.root', help='output .root file')
    parser.add_argument('-c', action='store', dest='cut', default='nbbPairSystem==1', help='selection cut')
    parser.add_argument('-l', action='store', dest='limit', default=-1, help='limit number of files to chain')
    args = parser.parse_args()

    print ('ARGS:', args)

    selectionCut = 'nbbPairSystem==1'
    # define plots
    plots = [
        {
            'name': 'deltaRvv_vs_deltaRbb',
            'cut': selectionCut,
            'variableX': 'bbPairSystem_mcDeltaR[0]',
            'variableY': 'bbPairSystem_deltaR[0]',
            'rangeX': [0,4,20],
            'rangeY': [0,4,20],
            'difference': True,
            'rangeD': [-0.2, 0.2, 200],
        },
        {
            'name': 'deltaRjj_vs_deltaRbb',
            'cut': selectionCut,
            'variableX' : 'bbPairSystem_mcDeltaR[0]',
            'variableY' : 'bbPairSystem_deltaRjet[0]',
            'rangeX': [0,4,20],
            'rangeY': [0,4,20],
            'difference': True,
            'rangeD': [-0.2, 0.2, 200],
        },
        {
            'name': 'deltaRpp_vs_deltaRbb',
            'cut': selectionCut,
            'variableX' : 'bbPairSystem_mcDeltaR[0]',
            'variableY' : 'bbPairSystem_deltaRpp[0]',
            'rangeX': [0,4,20],
            'rangeY': [0,4,20],
            'difference': True,
            'rangeD': [-0.2, 0.2, 200],
        }
    ]

    # read samples
    sampleTree = SampleTree(args.sample, limitFiles=args.limit)
    if not sampleTree:
        print ('creating sample tree failed!')
        exit(0)

    # correlation/difference plotter 
    plotter = CorrelationPlot(sampleTree)
    plotter.plot(plotOptions = plots, outputFileName=args.output)

    # add additional histogram
    outputFile = ROOT.TFile(args.output,'update')
    c1 = ROOT.TCanvas("c1","deltaR_difference_comparison", 500, 500)
    
    plots[0]['histogram']= outputFile.Get('deltaRvv_vs_deltaRbb_difference')
    plots[1]['histogram']= outputFile.Get('deltaRjj_vs_deltaRbb_difference')
    plots[2]['histogram']= outputFile.Get('deltaRpp_vs_deltaRbb_difference')

    print (plots)

    plots[0]['histogram'].SetLineColor(ROOT.kGreen+2)
    plots[1]['histogram'].SetLineColor(ROOT.kBlue+1)
    plots[2]['histogram'].SetLineColor(ROOT.kRed+1)
    
    plots[0]['histogram'].Draw()
    plots[1]['histogram'].Draw("same")
    plots[2]['histogram'].Draw("same")

    leg = ROOT.TLegend(0.15,0.7,0.35,0.86)
    leg.AddEntry(plots[0]['histogram'], "{\Delta}R_{vv}-{\Delta}R_{bb}")
    leg.AddEntry(plots[1]['histogram'], "{\Delta}R_{jj}-{\Delta}R_{bb}")
    leg.AddEntry(plots[2]['histogram'], "{\Delta}R_{pp}-{\Delta}R_{bb}")
    leg.Draw()

    c1.Write() 
    
    outputFile.Write()
    outputFile.Close()

    print ("done.")
