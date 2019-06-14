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
from myutils.VHbbSelection import VHbbSelection
#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <string
from ROOT import TFile
from ROOT import TTree
from ROOT import TString
from ROOT import TSystem
from ROOT import TROOT
from ROOT import TStopwatch
#from ROOT import TMVA/Tools
#from ROOT import TMVA/Reader
#from ROOT import TMVA/MethodCuts
#include <cstring>
#include <sstream>
#include <stdlib.h
from ROOT import TH1
from ROOT import TF1
from ROOT import TStyle
from ROOT import TCanvas
from ROOT import TString
from ROOT import TLatex
from ROOT import TColor
from ROOT import TAxis
from ROOT import TColor
from ROOT import TAxis
from ROOT import TLorentzVector
from ROOT import TMath
from ROOT import TLegend
#from ROOT import cmath

from ROOT import gStyle
from ROOT import gPad

from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad
from ROOT import kBlack, kBlue, kRed, kViolet
   

# load configuration and list of used samples
config = XbbConfigReader.read('Zll2018')
path = "Zll2018config/samples_nosplit.ini"
sampleInfo = ParseInfo(config,path,config=config)

usedSamples = sampleInfo.get_samples(XbbConfigTools(config).getMC())
#usedSamples = sampleInfo.get_samples(['ZJetsHT100', 'ZH_Znunu'])

usedSampleIdentifiers = list(set([x.identifier for x in usedSamples])) 
print('usedSampleIdentifiers', usedSampleIdentifiers)

# some samples come from same set of ROOT trees (=have same identifier)
# -> find list of unique identifiers to avoid to process same tree file twice
#sampleIdentifiers = sampleInfo.getSampleIdentifiers()
#usedSampleIdentifiers = ParseInfo.filterIdentifiers(sampleIdentifiers, usedSamples)

# from which step to take the root trees
directory = config.get('Directories', 'sysOUT4')

signalRegionSelection = config.get('Cuts', 'ZllBDT_highpt')
signalRegionSelection_roc = config.get('Cuts', 'ZllBDT_highpt_roc')

#signalRegionSelection = config.get('Cuts', 'ZllBDT_lowpt')
#signalRegionSelection_roc = config.get('Cuts', 'ZllBDT_lowpt_roc')



signalNames = eval(config.get('Plot_general', 'allSIG'))
print(config.get('Plot_general', 'allSIG'))
print('signalNames', signalNames)

weightExpression_DeepCSV = config.get('Weights','weightF_DeepCSV') 
weightExpression_DeepJet = config.get('Weights','weightF_DeepJet' )

weightExpression_DeepCSV_nosf = config.get('Weights','weightF_DeepCSV_nosf')
weightExpression_DeepJet_nosf = config.get('Weights','weightF_DeepJet_nosf' )

taggerExpression_DeepCSV = "Jet_btagDeepB[hJidx[1]]"
taggerExpression_DeepJet = "Jet_btagDeepFlavB[hJidx_DeepJet[1]]"

# process all samples
roc_data_DeepCSV = []
roc_data_DeepJet = []
#roc_data_DeepCSV_nosf = []
#roc_data_DeepJet_nosf = []


for i, sampleIdentifier in enumerate(usedSampleIdentifiers):
    print(sampleIdentifier)
    #subsamples = [x for x in usedSamples if x.identifier==sampleIdentifier and x.subsample==True]
    sample     = [x for x in sampleInfo if x.identifier==sampleIdentifier and x.subsample==False]

    #print("\x1b[41m\x1b[32m")
    #print('subsample_krunal', subsamples)
    print('sample_krunal', sample)
               
    if len(sample)==1:
        sample = sample[0]
        #print('sample', sample[0])
    else:
        sample = []
        print("LENGTH NOT 1")

    #print("\x1b[41m\x1b[32m")
  
    # in case the distinction between subsamples is needed, one could access the cut definitions for the subsamples
    # with: subsample.subcut for subsample in subsamples
    #sample     = sampleInfo.getFullSample(sampleIdentifier)
    #subsamples = sampleInfo.getSubsamples(sampleIdentifier)

    #print('subsample_pirmin', subsamples)
    #print('sample_pirmin', sample)
    #print("\x1b[41m\x1b[0m")
      
    sampleTree = SampleTree({'sample': sample, 'folder': directory}, config=config)
    #raw_input()

    # since we load all trees, we can compute the factor to scale cross section to luminosity directly (otherwise write it to ntuples 
    # first and then use it as branch, or compute it with full set of trees before)
    scaleXStoLumi = sampleTree.getScale(sample)

    # enable only used branches!
    # this will speed up processing a lot
    sampleTree.enableBranches(BranchList([signalRegionSelection, weightExpression_DeepCSV, weightExpression_DeepJet, taggerExpression_DeepCSV, taggerExpression_DeepJet]).getListOfBranches()+['Jet*'])

    # this will create the TTreeformula objects
    sampleTree.addFormula(signalRegionSelection)
    sampleTree.addFormula(signalRegionSelection_roc)
    sampleTree.addFormula(weightExpression_DeepCSV)
    sampleTree.addFormula(weightExpression_DeepJet)
    sampleTree.addFormula(weightExpression_DeepCSV_nosf)
    sampleTree.addFormula(weightExpression_DeepJet_nosf)
    sampleTree.addFormula(taggerExpression_DeepCSV)
    sampleTree.addFormula(taggerExpression_DeepJet)

    isSignal = 1 if sample.name in signalNames else 0

    for event in sampleTree:

        #bselection = VHbbSelection(channels=["Zll"])
        #sortb = bselection.HighestTaggerValueBJets(event, 20, 20, 'Jet_btagDeepFlavB')

        ##print('----------------------event start ', i)
        #print('len(tree.nJet)', event.nJet)
        #for i in range(event.nJet):

            #print('Jet No.', i)
            #print('Jet_lepFilter', event.Jet_lepFilter[i])
            #print('Jet_puId', event.Jet_puId[i])
            #print('Jet_PtReg', event.Jet_PtReg[i])
            #print('Jet_eta', abs(event.Jet_eta[i]))
            #print(hasattr(event,'Jet_PtReg'))
            #print('------------------------')

        #print('sortb', sortb)
        #print('(getattr(event,Jet_btagDeepFlavB)', (getattr(event,'Jet_btagDeepFlavB')))

        #if len(sortb)>1:
        if (sampleTree.evaluate(signalRegionSelection_roc)):
            # for all events passing the signal selection
            if (event.Jet_btagDeepFlavB[event.hJidx_DeepJet[0]]>0.0494 and event.Jet_btagDeepFlavB[event.hJidx_DeepJet[1]]>0.0494):

                # evaluate quantity (tagger, weight etc.)
                #roc_data_DeepCSV.append([sampleTree.evaluate(taggerExpression_DeepCSV), sampleTree.evaluate(weightExpression_DeepCSV) * scaleXStoLumi, isSignal])
                roc_data_DeepJet.append([sampleTree.evaluate(taggerExpression_DeepJet), sampleTree.evaluate(weightExpression_DeepJet) * scaleXStoLumi, isSignal, sampleTree.evaluate(weightExpression_DeepJet_nosf) * scaleXStoLumi])
                #roc_data_DeepJet_nosf.append([sampleTree.evaluate(taggerExpression_DeepJet), sampleTree.evaluate(weightExpression_DeepJet_nosf) * scaleXStoLumi, isSignal])


        if (sampleTree.evaluate(signalRegionSelection)):
            roc_data_DeepCSV.append([sampleTree.evaluate(taggerExpression_DeepCSV), sampleTree.evaluate(weightExpression_DeepCSV) * scaleXStoLumi, isSignal, sampleTree.evaluate(weightExpression_DeepCSV_nosf) * scaleXStoLumi])
            #roc_data_DeepCSV_nosf.append([sampleTree.evaluate(taggerExpression_DeepCSV), sampleTree.evaluate(weightExpression_DeepCSV_nosf) * scaleXStoLumi, isSignal])

# compute something, e.g. ROC curve
print("# MC events:", len(roc_data_DeepCSV))
print("# MC events:", len(roc_data_DeepJet))

roc_data_DeepCSV.sort(key=lambda x: x[0], reverse=True)
roc_data_DeepJet.sort(key=lambda x: x[0], reverse=True)

#roc_data = []
#roc_data.append(roc_data_DeepCSV)
#roc_data.append(roc_data_DeepJet)
print("sorted!")

roc_histo_DeepCSV = ROOT.TH1D('roc_DeepCSV','',100,0.0,1.0)
roc_histo_DeepJet = ROOT.TH1D('roc_DeepJet','',100,0.0,1.0)
roc_histo_DeepCSV_n = ROOT.TH1D('roc_DeepCSV_n','',100,0.0,1.0)
roc_histo_DeepJet_n = ROOT.TH1D('roc_DeepJet_n','',100,0.0,1.0)

roc_histo_DeepCSV.Sumw2()
roc_histo_DeepJet.Sumw2()

roc_histo_DeepCSV_nosf = ROOT.TH1D('roc_DeepCSV_nosf','',100,0.0,1.0)
roc_histo_DeepJet_nosf = ROOT.TH1D('roc_DeepJet_nosf','',100,0.0,1.0)
roc_histo_DeepCSV_n_nosf = ROOT.TH1D('roc_DeepCSV_n_nosf','',100,0.0,1.0)
roc_histo_DeepJet_n_nosf = ROOT.TH1D('roc_DeepJet_n_nosf','',100,0.0,1.0)

roc_histo_DeepCSV_nosf.Sumw2()
roc_histo_DeepJet_nosf.Sumw2()

roc_curve_DeepCSV = [[0.0, 0.0]]
roc_curve_DeepJet = [[0.0, 0.0]]
nSig_DeepCSV      = 0.0
nSig_DeepJet      = 0.0
nBkg_DeepCSV      = 0.0
nBkg_DeepJet      = 0.0

roc_curve_DeepCSV_nosf = [[0.0, 0.0]]
roc_curve_DeepJet_nosf = [[0.0, 0.0]]
nSig_DeepCSV_nosf      = 0.0
nSig_DeepJet_nosf      = 0.0
nBkg_DeepCSV_nosf      = 0.0
nBkg_DeepJet_nosf      = 0.0


for d in range(len(roc_data_DeepCSV)):
    if roc_data_DeepCSV[d][2] == 1:
        nSig_DeepCSV += roc_data_DeepCSV[d][1]
        nSig_DeepCSV_nosf += roc_data_DeepCSV[d][3]
    else:
        nBkg_DeepCSV += roc_data_DeepCSV[d][1]
        nBkg_DeepCSV_nosf += roc_data_DeepCSV[d][3]
    roc_curve_DeepCSV.append([nSig_DeepCSV,nBkg_DeepCSV])
    roc_curve_DeepCSV_nosf.append([nSig_DeepCSV_nosf,nBkg_DeepCSV_nosf])


for d in range(len(roc_data_DeepJet)):
    if roc_data_DeepJet[d][2] == 1:
        nSig_DeepJet += roc_data_DeepJet[d][1]
        nSig_DeepJet_nosf += roc_data_DeepJet[d][3]
    else:
        nBkg_DeepJet += roc_data_DeepJet[d][1]
        nBkg_DeepJet_nosf += roc_data_DeepJet[d][3]
    roc_curve_DeepJet.append([nSig_DeepJet,nBkg_DeepJet])
    roc_curve_DeepJet_nosf.append([nSig_DeepJet_nosf,nBkg_DeepJet_nosf])




for d in range(len(roc_curve_DeepCSV)):
    sEff_DeepCSV = roc_curve_DeepCSV[d][0]/roc_curve_DeepCSV[-1][0]
    bRej_DeepCSV = 1.0 - roc_curve_DeepCSV[d][1]/roc_curve_DeepCSV[-1][1]

    sEff_DeepCSV_nosf = roc_curve_DeepCSV_nosf[d][0]/roc_curve_DeepCSV_nosf[-1][0]
    bRej_DeepCSV_nosf = 1.0 - roc_curve_DeepCSV_nosf[d][1]/roc_curve_DeepCSV_nosf[-1][1]

    roc_histo_DeepCSV.Fill(sEff_DeepCSV, bRej_DeepCSV)
    roc_histo_DeepCSV_n.Fill(sEff_DeepCSV, 1.0)

    roc_histo_DeepCSV_nosf.Fill(sEff_DeepCSV_nosf, bRej_DeepCSV_nosf)
    roc_histo_DeepCSV_n_nosf.Fill(sEff_DeepCSV_nosf, 1.0)


for d in range(len(roc_curve_DeepJet)):
    sEff_DeepJet = roc_curve_DeepJet[d][0]/roc_curve_DeepJet[-1][0]
    bRej_DeepJet = 1.0 - roc_curve_DeepJet[d][1]/roc_curve_DeepJet[-1][1]

    sEff_DeepJet_nosf = roc_curve_DeepJet_nosf[d][0]/roc_curve_DeepJet_nosf[-1][0]
    bRej_DeepJet_nosf = 1.0 - roc_curve_DeepJet_nosf[d][1]/roc_curve_DeepJet_nosf[-1][1]

    roc_histo_DeepJet.Fill(sEff_DeepJet, bRej_DeepJet)    
    roc_histo_DeepJet_n.Fill(sEff_DeepJet, 1.0)

    roc_histo_DeepJet_nosf.Fill(sEff_DeepJet_nosf, bRej_DeepJet_nosf)
    roc_histo_DeepJet_n_nosf.Fill(sEff_DeepJet_nosf, 1.0)


roc_histo_DeepCSV.Divide(roc_histo_DeepCSV_n)
roc_histo_DeepJet.Divide(roc_histo_DeepJet_n)

roc_histo_DeepCSV_nosf.Divide(roc_histo_DeepCSV_n_nosf)
roc_histo_DeepJet_nosf.Divide(roc_histo_DeepJet_n_nosf)


#c2 = ROOT.TCanvas("c2","",500,500)
#roc_histo_DeepJet.Draw("HIST")
#c2.SaveAs("roc_curve_DeepJet.png")

#plot_ratio(roc_histo_DeepCSV,roc_histo_DeepJet)

def plot_ratio(hist1,hist2,hist1_nosf,hist2_nosf):

    g2 = ROOT.TCanvas("c1","c1",800,800) 
    #g2.Range(0,0,1,1)
    #g2.SetFillColor(0)
    #g2.SetBorderMode(0)
    #g2.SetBorderSize(2)
    #g2.SetFrameBorderMode(0)
    #gStyle.SetPadBorderMode(0)
    gStyle.SetOptStat(0)
    #g2.Divide(1,1)
    #g2.cd(1)
    #gPad.Range(-69.03766,-0.0002509835,628.8703,0.06681207)
    g2.SetGridx()
    #gPad.SetTopMargin(0.006574267)
    #gPad.SetBottomMargin(0.001912046)
    hist1.SetLineColor(kBlack)
    hist2.SetLineColor(kRed)
    hist1_nosf.SetLineColor(kBlue)
    hist2_nosf.SetLineColor(kViolet)
    #hist1_nosf.SetLineStyle(7)
    #hist2_nosf.SetLineStyle(7)

       
    #hist1.Sumw2()
    #hist2.Sumw2()
    hs = ROOT.THStack()
    hs.Add(hist1,"E")
    hs.Add(hist2,"E")
    hs.Add(hist1_nosf,"E")
    hs.Add(hist2_nosf,"E")
    hs.Draw("nostack")
    #hs.GetHistogram().GetXaxis().SetLabelOffset(999)
    hs.GetHistogram().GetXaxis().SetTitle("Signal efficiency")
    hs.GetHistogram().GetYaxis().SetTitle("Background rejection")
    hs.GetHistogram().GetYaxis().SetTitleOffset(1.4)
    hs.GetHistogram().GetYaxis().SetTitleSize(0.03)
    hs.GetHistogram().GetYaxis().SetLabelSize(0.03)
    hs.GetHistogram().GetXaxis().SetTitleOffset(1.4)
    hs.GetHistogram().GetXaxis().SetTitleSize(0.03)
    hs.GetHistogram().GetXaxis().SetLabelSize(0.03)
    #hs.GetHistogram().GetYaxis().CenterTitle()
    hist1.SetStats(0)
    hist2.SetStats(0)
    hist1_nosf.SetStats(0)
    hist2_nosf.SetStats(0)
    la = ROOT.TLegend(0.20,0.20,0.45,0.45) #,NULL,"brNDC")
    la.AddEntry(hist1,"DeepCSV","l")
    la.AddEntry(hist1_nosf,"DeepCSV_noSF","l")
    la.AddEntry(hist2,"DeepJet","l")
    #la.AddEntry(hist1_nosf,"DeepCSV_noSF","l")
    la.AddEntry(hist2_nosf,"DeepJet_noSF","l")
    la.SetTextFont(12)
    la.SetTextSize(0.03537499)
    la.SetBorderSize(0)
    la.SetFillColor(0)
    la.Draw("same")

    #g2.Update()
    #g2.Draw()
    g2.SaveAs("roc_curve_highpt.png")



'''
def plot_kin(hist1,hist2):

    g2 = ROOT.TCanvas("c1","c1",800,800) 
    #g2.Range(0,0,1,1)
    #g2.SetFillColor(0)
    #g2.SetBorderMode(0)
    #g2.SetBorderSize(2)
    #g2.SetFrameBorderMode(0)
    #gStyle.SetPadBorderMode(0)
    gStyle.SetOptStat(0)
    #g2.Divide(1,1)
    #g2.cd(1)
    #gPad.Range(-69.03766,-0.0002509835,628.8703,0.06681207)
    g2.SetGridx()
    #gPad.SetTopMargin(0.006574267)
    #gPad.SetBottomMargin(0.001912046)
    hist1.SetLineColor(kBlack)
    hist2.SetLineColor(kRed)
       
    #hist1.Sumw2()
    #hist2.Sumw2()
    hs = ROOT.THStack()
    hs.Add(hist1,"E")
    hs.Add(hist2,"E")
    hs.Draw("nostack")
    #hs.GetHistogram().GetXaxis().SetLabelOffset(999)
    hs.GetHistogram().GetXaxis().SetTitle("cddcd")
    hs.GetHistogram().GetYaxis().SetTitle("dcd")
    hs.GetHistogram().GetYaxis().SetTitleOffset(1.4)
    hs.GetHistogram().GetYaxis().SetTitleSize(0.03)
    hs.GetHistogram().GetYaxis().SetLabelSize(0.03)
    hs.GetHistogram().GetYaxis().CenterTitle()
    hist1.SetStats(0)
    hist2.SetStats(0)
    la = ROOT.TLegend(0.60,0.72,0.9,0.87) #,NULL,"brNDC")
    la.AddEntry(hist1,"CSV","l")
    la.AddEntry(hist2,"JET","l")
    la.SetTextFont(12)
    la.SetTextSize(0.03537499)
    la.SetBorderSize(0)
    la.SetFillColor(0)
    la.Draw("same")

    #g2.Update()
    #g2.Draw()
    g2.SaveAs("roc_curve_check.png")

'''
plot_ratio(roc_histo_DeepCSV,roc_histo_DeepJet,roc_histo_DeepCSV_nosf,roc_histo_DeepJet_nosf)

#roc_histo.Draw("HIST")
#c1.SaveAs("roc_curve.png")
