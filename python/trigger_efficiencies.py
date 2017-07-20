#!/usr/bin/env python
from __future__ import print_function
from myutils.sampleTree import SampleTree as SampleTree
import ROOT
import argparse
import os
import sys
import time

#------------------------------------------------------------------------------
# calculate efficiency of HLT
#------------------------------------------------------------------------------
class EfficiencyCalculator(object):

    def __init__(self, sampleTree = None):
        self.sampleTree = sampleTree

    def calculateEfficiency(self, definitions, outputFileName='trigeff.root'):
       
        # add formulas for cuts
        outputFile = ROOT.TFile(outputFileName,'recreate')
        for histogramDefinition in definitions:
            histogramName = histogramDefinition['name']
            self.sampleTree.addFormula(histogramName + '__variable', histogramDefinition['variable'])
            self.sampleTree.addFormula(histogramName + '__tight', histogramDefinition['tight'])
            self.sampleTree.addFormula(histogramName + '__loose', histogramDefinition['loose'])
        
            range = histogramDefinition['range']
            
            # prepare output file and histograms
            histogramDefinition['histogram_loose'] = ROOT.TH1D('histogramPassLoose_'+histogramName,'passed cut: ' + histogramDefinition['loose'], range[2], range[0], range[1])
            histogramDefinition['histogram_tight'] = ROOT.TH1D('histogramPassTight_'+histogramName,'passed cut: ' + histogramDefinition['tight'], range[2], range[0], range[1])
            histogramDefinition['histogram_efficiency'] = ROOT.TH1D('histogramEfficiency_'+histogramName,'Trigger efficiency', range[2], range[0], range[1])
            histogramDefinition['histogram_loose'].Sumw2()
            histogramDefinition['histogram_tight'].Sumw2()

        if self.sampleTree:
            # count events passing the loose/tight cuts
            nEntry = 0
            for event in self.sampleTree:
                for histogramDefinition in definitions:
                    passLoose = self.sampleTree.evaluate(histogramDefinition['name'] + '__loose')
                    passTight = self.sampleTree.evaluate(histogramDefinition['name'] + '__tight')
                    var = self.sampleTree.evaluate(histogramDefinition['name'] + '__variable')
                    if passLoose:
                        histogramDefinition['histogram_loose'].Fill(var, passLoose)
                    if passTight:
                        histogramDefinition['histogram_tight'].Fill(var, passTight)
                    nEntry += 1

            # calculate efficiency
            # divide histograms with binomial errors
            for histogramDefinition in definitions:
                histogramDefinition['histogram_efficiency'].Divide(histogramDefinition['histogram_tight'], histogramDefinition['histogram_loose'], 1, 1, "B")

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
    parser.add_argument('-m', action='store', dest='limit', help='limit', default='0')
    #parser.add_argument('-v', action='store', dest='variable', default='Max$(Jet_pt)', help='variable to compute the efficiency of (differentially)')
    #parser.add_argument('-r', action='store', dest='range', default='0,1000,100', help='min,max,nbins of variable to create histogram')
    parser.add_argument('-o', action='store', dest='output', default='trigeff.root', help='output .root file')
    #parser.add_argument('-l', action='store', dest='loose', default='((nJet>0)&&HLT_BIT_HLT_PFJet80_v)*HLT_BIT_HLT_PFJet80_v_Prescale', help='loose cut')
    #parser.add_argument('-t', action='store', dest='tight', default='((nJet>0)&&HLT_BIT_HLT_PFJet140_v)*HLT_BIT_HLT_PFJet140_v_Prescale', help='tight cut')
    args = parser.parse_args()
    
    limitTrees = int(args.limit)
    print ('ARGS:', args)

    # read samples
    sampleTree = SampleTree(args.sample, limitFiles=limitTrees)
    if not sampleTree:
        print ('creating sample tree failed!')
        exit(0)
    
    # trigger efficiency histograms
    triggerEfficiencyHistograms = [
            {
                'name': 'HLT_PFJet140',
                'range': [0, 1000, 100],
                'loose': '((nJet>0)&&HLT_BIT_HLT_PFJet80_v)*HLT_BIT_HLT_PFJet80_v_Prescale',
                'tight': '((nJet>0)&&HLT_BIT_HLT_PFJet140_v)*HLT_BIT_HLT_PFJet140_v_Prescale',
                'variable': 'Max$(Jet_pt)'
            },
            {
                'name': 'HLT_PFJet500',
                'range': [0, 1000, 100],
                'loose': '((nJet>0)&&HLT_BIT_HLT_PFJet400_v)*HLT_BIT_HLT_PFJet400_v_Prescale',
                'tight': '((nJet>0)&&HLT_BIT_HLT_PFJet500_v)*HLT_BIT_HLT_PFJet500_v_Prescale',
                'variable': 'Max$(Jet_pt)'
            },

   ]
    
    # calculate efficiency
    triggerEfficienciesCalculator = EfficiencyCalculator(sampleTree)
    triggerEfficienciesCalculator.calculateEfficiency(definitions=triggerEfficiencyHistograms, outputFileName=args.output)

    print ("done. Knowing the efficiency you triggered with fills you with determination.")

