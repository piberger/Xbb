#!/usr/bin/env python
from __future__ import print_function
import ROOT
ROOT.gROOT.SetBatch(True)
import glob
import sys
import subprocess
import os
import hashlib
import subprocess
from time import sleep

def get_files(sampleName):
    files= subprocess.check_output(['dasgoclient --query="file dataset=' + sampleName + '"'], shell=True).strip('\n').split('\n')
    #print "LIST OF FILES:", files
    return ['root://xrootd-cms.infn.it/' + x for x in files]

def get_output_file_name(sampleName, fileName, cut=None):
    sampleIdentifier = sampleName.strip('/').split('/')[0]
    if cut is None:
        return sampleIdentifier + '_' + hashlib.sha224(fileName).hexdigest() + '.root'
    else:
        return sampleIdentifier + '_' + hashlib.sha224(fileName).hexdigest() + '_' +  hashlib.sha224(cut).hexdigest() + '.root'

def cutAnd(cut1,cut2):
    return "(" + cut1 + ")&&(" + cut2 + ")"

if len(sys.argv) < 4:
    print("usage: ./reweight_lo_to_nlo.py mode sample flav type")
    print(" mode: - submit: submit jobs")
    print("       - run: make plots and run the fits")
    print(" sample: sample group, e.g. ZJets, DYJets, DYJetsPtBinned, ...")
    print(" flav: 0b, 1b, 2b")
    print(" type: Vpt, deltaEta")
    exit(0)
#####

# NLO samples can have single events with huge negative weights
# this will filter out a known case
filterBadFiles = ['164f29771e2a5da53c00895618b64b30f5d9d458a8a38d3b8c924f56']

#sample = "DYJets"
#sample = "WJets"
#sample = "ZJets"
sample = sys.argv[2]

#binName = "incl"
#binName = "0b"
#binName = "1b"
#binName = "2b"
binName = sys.argv[3]

reweightType = sys.argv[4] if len(sys.argv)>4 else "Vpt"

if reweightType == "Vpt":
    applyVptNLOweight    = False
    reweightVar          = 'LHE_Vpt'
    nloWeightVersionName = "nlo_Vpt_V2b"

    reweightVarNbins = 100
    reweightVarMin   = 0.0
    reweightVarMax   = 1000.0

    fitModel    = "[0]+[1]*x"
    fitRangeMin = 100
    fitRangeMax = 400

elif reweightType == "deltaEta":
    applyVptNLOweight    = True
    nloWeightVersionName = "nlo_deltaEtaJJ"
    reweightVar = 'abs(GenJet_eta[0]-GenJet_eta[1])'

    reweightVarNbins = 60
    reweightVarMin   = 0.0
    reweightVarMax   = 6.0
    fitRangeMin = 0.0
    fitRangeMax = 6.0

    fitModel = "[0]+[1]*x+[2]*x**2+[3]*x**3"
elif reweightType == "deltaEtaStandalone":
    applyVptNLOweight    = False
    nloWeightVersionName = "nlo_deltaEtaJJstandalone"
    reweightVar = 'abs(GenJet_eta[0]-GenJet_eta[1])'

    reweightVarNbins = 60
    reweightVarMin   = 0.0
    reweightVarMax   = 6.0
    fitRangeMin = 0.0
    fitRangeMax = 6.0

    fitModel = "[0]+[1]*x+[2]*x**2+[3]*x**3"
else:
    raise Exception("Unknown weight type")

weightLO = "1.0"

#####
submissionCommand = "sbatch --account=t3 --time=0-01:00 --job-name wNLO --partition=quick "

#####
globalCut = "1"
rebinning = None
if sample == "WJets":
    rebinning = 5
    NLOsampleName = 'WJetsToLNu_*J_TuneCP5_13TeV-amcatnloFXFX-pythia8'
    sampleTable = {
            'NLO': [
                ['/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 54601.0],
                ['/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 8939.0],
                ['/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3511.0]
                ],
            'LO': [
                ['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM',52940.0 * 1.21,'LHE_HT<100'],
                ['/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1395.0 * 1.21],
                ['/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 407.9 * 1.21],
                ['/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 57.48 * 1.21],
                ['/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 12.87 * 1.21],
                ['/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5.366 *1.21],
                ['/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.074 * 1.21],
                ['/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.03216 * 1.21],
                ]
            }
elif sample == "ZJets":
    NLOsampleName = "Z*JetsToNuNu_M-50_LHEZpT_*_TuneCP5_13TeV-amcnloFXFX-pythia8"
    globalCut = "(LHE_HT>100&&LHE_Vpt>100&&LHE_Vpt<400)"
    sampleTable = {
            'NLO': [
                ['/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM' , 596.4],
                ['/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM' , 18.0],
                ['/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM' , 2.057],
                ['/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM' , 325.7],
                ['/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM' , 29.76],
                ['/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM' , 5.164],
                ],
            'LO': [
                ['/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 304.5 * 1.23],
                ['/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 91.85 * 1.23],
                ['/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 13.11 * 1.23],
                ['/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3.257 * 1.23],
                ['/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.49 * 1.23],
                ['/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.3419 * 1.23],
                ['/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.005146 * 1.23],
                ]
            }

    # apply weight in first variable!
    if applyVptNLOweight:

        # remove range  Vpt < 100
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>100)"

        # apply Vpt weight to LO samples
        if sys.argv[3] == '2b':
            weightLO = "(1.150 - 1.222e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '1b':
            weightLO = "(1.273 - 1.401e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '0b':
            weightLO = "(1.365 - 1.425e-3*min(LHE_Vpt,500.0))"

elif sample == "DYJets":
    NLOsampleName = "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8"
    sampleTable = {
            'NLO': [
                ['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 6529.0],
                ],
            'LO': [
                ['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017RECOSIMstep_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5343.0*1.23, '(LHE_HT<100)'],
                ['/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 161.1*1.23],
                ['/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 48.66*1.23],
                ['/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM', 6.968*1.23],
                ['/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.743*1.23],
                ['/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.8052*1.23],
                ['/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.1933*1.23],
                ['/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.00347*1.23],
                ]
            }
elif sample == "DYJetsPtBinned":
    NLOsampleName = "DYJetsToLL_Pt-*_TuneCP5_13TeV-amcatnloFXFX-pythia8" 
    sampleTable = {
            'NLO': [
                ['/DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 97.36],
                ['/DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3.774],
                ['/DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.5148],
                ['/DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.04814],
                ],
            'LO': [
                ['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017RECOSIMstep_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5343.0*1.23, '(LHE_HT<100)'],
                ['/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 161.1*1.23],
                ['/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 48.66*1.23],
                ['/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM', 6.968*1.23],
                ['/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.743*1.23],
                ['/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.8052*1.23],
                ['/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.1933*1.23],
                ['/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.00347*1.23],
                ]
            }
elif sample == "WJetsPtBinned":
    NLOsampleName = "WJetsToLNu_Pt-*_TuneCP5_13TeV-amcatnloFXFX-pythia8"
    sampleTable = {
            'NLO': [
                ['/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3567],
                ['/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 772.7],
                ['/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 27.98],
                ['/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3.591],
                ['/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.5505],
                ],
            'LO': [
                ['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM',52940.0 * 1.21,'LHE_HT<100'],
                ['/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1395.0 * 1.21],
                ['/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 407.9 * 1.21],
                ['/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 57.48 * 1.21],
                ['/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 12.87 * 1.21],
                ['/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5.366 *1.21],
                ['/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.074 * 1.21],
                ['/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.03216 * 1.21],
                ]
            }


if binName.startswith("0b"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)<1")
elif binName.startswith("1b"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)==1")
elif binName.startswith("2b"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)>1")
elif binName == "incl":
    pass
else:
    raise Exception("Unknown bin definition")

binNameParts = binName.split('_')
if len(binNameParts) > 1:
    if "dEta0to0p5" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>0.0&&abs(GenJet_eta[0]-GenJet_eta[1])<0.5")
    elif "dEta0p5to1" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>0.5&&abs(GenJet_eta[0]-GenJet_eta[1])<1.0")
    elif "dEta1to1p5" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>1.0&&abs(GenJet_eta[0]-GenJet_eta[1])<1.5")
    elif "dEta1p5to2" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>1.5&&abs(GenJet_eta[0]-GenJet_eta[1])<2.0")
    elif "dEta2to2p5" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>2.0&&abs(GenJet_eta[0]-GenJet_eta[1])<2.5")
    elif "dEta2p5to3" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>2.5&&abs(GenJet_eta[0]-GenJet_eta[1])<3.0")
    elif "dEta3to6" in binNameParts:
        globalCut = cutAnd(globalCut, "abs(GenJet_eta[0]-GenJet_eta[1])>3.0&&abs(GenJet_eta[0]-GenJet_eta[1])<6.0")

tmpFolder = "tmp_" + nloWeightVersionName + "/" + sample
try:
    os.makedirs(tmpFolder)
except:
    pass

outFileName = "nloweight_histograms_" + sample + "_V2b_" + binName + ".root"
if sys.argv[1] != "submit":
    outfile = ROOT.TFile.Open(outFileName, "RECREATE")
else:
    outfile = None

jobs = []
histograms = {}
genEventSumw = {}
allSamplesNonEmpty = True
for cat in sampleTable.keys():
    histograms[cat] = {}
    genEventSumw[cat] = {}
    for sampleData in sampleTable[cat]:
        sampleName   = sampleData[0]
        crossSection = sampleData[1]
        cut          = sampleData[2] if len(sampleData) > 2 else "1"
        fileNames = get_files(sampleName)
        histograms[cat][sampleName] = ROOT.TH1D(sampleName,sampleName,reweightVarNbins,reweightVarMin,reweightVarMax)
        histograms[cat][sampleName].Sumw2()
        genEventSumw[cat][sampleName] = 0
        if outfile is not None:
            histograms[cat][sampleName].SetDirectory(outfile)
        nFilesAdded = 0
        for fileName in fileNames:
            totalCut = cutAnd(cut,globalCut)
            outputFileName = tmpFolder + '/' + get_output_file_name(sampleName, fileName, totalCut)
            if sys.argv[1] == "submit":
                if not os.path.isfile(outputFileName):
                    wlo = weightLO if cat == 'LO' else '1.0'
                    #jobString = submissionCommand + "./nano_to_histogram.py --cut='{cut}' --var 'LHE_Vpt' --min 0 --max 1000 --nbins 100 --input='{input}' --output='{output}'".format(input=fileName, output=outputFileName, cut=totalCut)
                    jobString = submissionCommand + "./nano_to_histogram.py --cut='({cut})*{wlo}' --var '{reweightVar}' --min {reweightVarMin} --max {reweightVarMax} --nbins {reweightVarNbins} --input='{input}' --output='{output}'".format(input=fileName, output=outputFileName, cut=totalCut,wlo=wlo,reweightVar=reweightVar, reweightVarMin=reweightVarMin, reweightVarMax=reweightVarMax, reweightVarNbins=reweightVarNbins)
                    print(jobString)
                    stdOutput = subprocess.check_output([jobString], shell=True)
                    print("=>", stdOutput)
                    sleep(0.1)
                    jobs.append(jobString)
                else:
                    print("=> file exists")

            elif sys.argv[1] == "run":
                if os.path.isfile(outputFileName):
                    print("\x1b[32m",outputFileName,"\x1b[0m")

                    if not any([x in outputFileName for x in filterBadFiles]):
                        f1 = ROOT.TFile.Open(outputFileName, "READ")
                        if f1 is not None:
                            try:
                                isValid = not (f1.IsZombie() or f1.GetNkeys() == 0 or f1.TestBit(ROOT.TFile.kRecovered))
                            except:
                                isValid = False
                            if isValid:
                                genEventSumwHistogram = f1.Get("genEventSumw")
                                h1c = f1.Get('h1').Clone()
                                c1 = ROOT.TCanvas("c1","c1",500,500)
                                h1c.Draw()
                                c1.SaveAs(outputFileName.replace('.root','.png'))
                                genEventSumw[cat][sampleName] += genEventSumwHistogram.GetBinContent(1)
                                histograms[cat][sampleName].Add(h1c)
                                f1.Close()
                            else:
                                try:
                                    f1.Close()
                                except:
                                    pass
                    else:
                        print("\x1b[33m ignore:",outputFileName,"\x1b[0m")
                else:
                    print("\x1b[31m",outputFileName,"\x1b[0m")
        if sys.argv[1] == "run":
            if genEventSumw[cat][sampleName] < 1: 
                print("EMPTY:", cat, sampleName)
                allSamplesNonEmpty = False
            else:
                print("OK:", cat, sampleName)

totalHistograms = {}
if not allSamplesNonEmpty and sys.argv[1] == "run":
    print("\x1b[31mERROR: some samples have 0 events, can't run the fit.\x1b[0m")
    exit(1)

if allSamplesNonEmpty and sys.argv[1] == "run":
    # scale to cross section
    for cat in sampleTable.keys():
        for sampleData in sampleTable[cat]:
            sampleName   = sampleData[0]
            crossSection = sampleData[1]
            histograms[cat][sampleName].Scale(crossSection/genEventSumw[cat][sampleName])

    # sum up histograms
    for cat in sampleTable.keys():
        totalHistograms[cat] = ROOT.TH1D(cat,cat,reweightVarNbins,reweightVarMin,reweightVarMax)
        totalHistograms[cat].Sumw2()
        totalHistograms[cat].SetDirectory(outfile)
        for sampleData in sampleTable[cat]:
            sampleName   = sampleData[0]
            totalHistograms[cat].Add(histograms[cat][sampleName])

    # make ratio   
    c1 = ROOT.TCanvas("c1","c1",500,500)
    hist_ratio = ROOT.TH1D("ratio","ratio",reweightVarNbins,reweightVarMin,reweightVarMax)
    hist_ratio.Add(totalHistograms['NLO'])
    hist_ratio.Divide(totalHistograms['LO'])
    if rebinning is not None:
        hist_ratio.Rebin(rebinning)
        hist_ratio.Scale(1.0/rebinning)
    hist_ratio.SetDirectory(outfile)
    hist_ratio.SetStats(0)
    hist_ratio.GetXaxis().SetTitle(reweightVar)
    hist_ratio.GetYaxis().SetTitle("NLO/LO")
    hist_ratio.GetYaxis().SetRangeUser(0,2)
    hist_ratio.Draw()
    
    pol1 = ROOT.TF1("f1",fitModel, fitRangeMin, fitRangeMax)
    hist_ratio.Fit(pol1, "R")
    fitResult = hist_ratio.Fit(pol1, "RS")

    fitParListWithErrors = sum([ [pol1.GetParameter(i), pol1.GetParError(i)] for i in range(pol1.GetNpar())], [])
    print("\x1b[32mFIT RESULT:", fitParListWithErrors, "\x1b[0m") 

    fitFormulaString = fitModel
    for i in range(pol1.GetNpar()):
        fitFormulaString = fitFormulaString.replace("[%i]"%i, "(%1.3e + var%i*%1.3e)"%(pol1.GetParameter(i), i,  pol1.GetParError(i)))
    fitFormulaString = fitFormulaString.replace("x","(" + reweightVar + ")")
    print(fitFormulaString)
    
    latex = ROOT.TLatex()
    latex.SetTextSize(0.021)
    latex.SetTextAlign(13)
    latex.DrawLatexNDC(.14,.23,NLOsampleName)
    latex.SetTextSize(0.025)
    latex.DrawLatexNDC(.14,.19,binName)
    latex.SetTextSize(0.015)
    latex.DrawLatexNDC(.14,.15,fitFormulaString)

    c1.SaveAs(outFileName.replace('.root',nloWeightVersionName + '.pdf'))
    c1.SaveAs(outFileName.replace('.root',nloWeightVersionName + '.png'))
    cov = fitResult.GetCovarianceMatrix() 
    with open("results_" + sample + "_" + binName + ".txt", "w") as of1:
        of1.write("%1.5e,%1.5e,%1.5e,%1.5e\n"%(pol1.GetParameter(0),pol1.GetParError(0),pol1.GetParameter(1),pol1.GetParError(1)))
        for i in range(2):
            of1.write(' '.join(["%1.5f"%cov[i][j] for j in range(2)]) + '\n')


if sys.argv[1] != "submit":
    outfile.Write()
    outfile.Close()
else:
    print(len(jobs), " jobs")

