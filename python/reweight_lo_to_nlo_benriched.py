#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import ROOT
ROOT.gROOT.SetBatch(True)
import glob
import sys
import subprocess
import os
import hashlib
import subprocess
from time import sleep

ROOT.Math.MinimizerOptions.SetDefaultMaxFunctionCalls(100000)

def get_files(sampleName):
    if type(sampleName) == str:
        sampleNames = [sampleName]
    else:
        sampleNames = sampleName

    files = []
    for sampleName in sampleNames:
        command = 'dasgoclient --query="file dataset=' + sampleName + '"'
        #command = 'dasgoclient --query="file dataset=' + sampleName + ' instance=prod/phys03  system=phedex"'
        print("running:", command)
        files += subprocess.check_output([command], shell=True).strip('\n').split('\n')
    print(files)
    #raw_input()
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
    print(" flav: 0b, 1b, 2b, udsg, c")
    print(" type: Vpt, deltaEta")
    exit(0)
#####

nGenStatus2bHad = "Sum$((int(abs(GenPart_pdgId)/100)==5||int(abs(GenPart_pdgId)/1000)==5)&&GenPart_status==2)"

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
nloWeightVersion = "V7"
fitParLimits = None

if reweightType == "Vpt":
    applyVptNLOweight    = False
    reweightVar          = 'LHE_Vpt'
    nloWeightVersionName = "nlo_Vpt_V7"

    reweightVarNbins = 100
    reweightVarMin   = 0.0
    reweightVarMax   = 1000.0

    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,400.0),100.0)"
    # default model V6
    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,600.0),[5])+[2]*TMath::Max(TMath::Min(x,600.0),[5])**2+[3]*TMath::Exp([4]*TMath::Max(TMath::Min(x,600.0),[5]))"
    # V6, if [5] get pushed to 50 and error matrix is not pos. def.
    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,600.0),50.0)+[2]*TMath::Max(TMath::Min(x,600.0),50.0)**2+[3]*TMath::Exp([4]*TMath::Max(TMath::Min(x,600.0),50.0))"
    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,400.0),50.0)+[2]*TMath::Max(TMath::Min(x,400.0),50.0)**2+[3]*TMath::Exp([4]*TMath::Max(TMath::Min(x,400.0),50.0))"
    fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,400.0),50.0)+[2]*TMath::Max(TMath::Min(x,400.0),50.0)**2"

    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[5]),50.0)+[2]*TMath::Max(TMath::Min(x,[5]),50.0)**2+[3]*TMath::Exp([4]*TMath::Max(TMath::Min(x,[5]),50.0))"
    fitRangeMin = 50
    fitRangeMax = 1000
    #fitParLimits = [[5,50.0,150.0]]
    #fitParLimits = [[5,500.0,900.0]]

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

    if sample == "DYJetsPtBinned" and binName == "0b":
        fitModel = "[0]+[1]*x+[2]*x**2+[3]*x**3+[4]*x**4"
    
    if sample == "WJetsPtBinned" and binName == "0b":
        fitModel = "[0]+[1]*x+[2]*x**2+[3]*x**3+[4]*x**4"


elif reweightType == "deltaR":
    applyVptNLOweight    = True
    nloWeightVersionName = "nlo_deltaRJJ"
    reweightVar = 'TMath::Sqrt((GenJet_eta[0]-GenJet_eta[1])**2+TVector2::Phi_mpi_pi(GenJet_phi[0]-GenJet_phi[1])**2)'

    reweightVarNbins = 80
    reweightVarMin   = 0.0
    reweightVarMax   = 8.0
    fitRangeMin = 0.0
    fitRangeMax = 8.0

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
elif reweightType == "muonPt":
    applyVptNLOweight    = True
    reweightVar = "-99.0+MaxIf$(99.0+GenPart_pt,abs(GenPart_pdgId)==13&&GenPart_status==1&&abs(GenPart_pdgId[GenPart_genPartIdxMother])==24)"
    nloWeightVersionName = "nlo_residualMuonPt"
    
    reweightVarNbins = 50
    reweightVarMin   = 0.0
    reweightVarMax   = 500.0
    fitRangeMin = 25.0
    fitRangeMax = 500.0

    fitModel = "[0]+[1]*x+[2]*x**2+[3]*x**3"
#abs(TVector2::Phi_mpi_pi(MaxIf$(GenPart_phi,((abs(GenPart_pdgId)==12||abs(GenPart_pdgId)==14||abs(GenPart_pdgId)==16)&&GenPart_genPartIdxMother>-1&&abs(GenPart_pdgId[GenPart_genPartIdxMother])==24))-MaxIf$(GenPart_phi,((abs(GenPart_pdgId)==11||abs(GenPart_pdgId)==13||abs(GenPart_pdgId)==15)&&GenPart_genPartIdxMother>-1&&abs(GenPart_pdgId[GenPart_genPartIdxMother])==24))))
elif reweightType == "leptonNeutrinoDphi":
    applyVptNLOweight    = True
    reweightVar = "abs(TVector2::Phi_mpi_pi(MaxIf$(GenPart_phi,((abs(GenPart_pdgId)==12||abs(GenPart_pdgId)==14||abs(GenPart_pdgId)==16)&&GenPart_genPartIdxMother>-1&&abs(GenPart_pdgId[GenPart_genPartIdxMother])==24))-MaxIf$(GenPart_phi,((abs(GenPart_pdgId)==11||abs(GenPart_pdgId)==13||abs(GenPart_pdgId)==15)&&GenPart_genPartIdxMother>-1&&abs(GenPart_pdgId[GenPart_genPartIdxMother])==24))))"
    nloWeightVersionName = "nlo_residualLeptonNeutrinoDphit"
    
    reweightVarNbins = 68
    reweightVarMin   = 0.0
    reweightVarMax   = 3.1416
    fitRangeMin = 0.2
    fitRangeMax = 3.14

    fitModel = "[0]+[1]*x+[2]*x**2+[3]*x**3"

else:
    raise Exception("Unknown weight type")

weightLO = "1.0"

#####
#submissionCommand = "sbatch --account=t3 --time=0-01:00 --job-name wNLO_{s}_{b}_{t} --partition=quick ".format(s=sample, b=binName, t=reweightType)
submissionCommand = "sbatch --account=t3 --time=0-05:00 --job-name wNLO_{s}_{b}_{t} --partition=wn ".format(s=sample, b=binName, t=reweightType)

#####
globalCut = "1"
rebinning = None
if sample == "WJets":
    rebinning = np.array([0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,180.0,200.0,220.0,240.0,260.0,300.0,350.0,400.0,450.0,500.0,600.0,700.0,800.0,1000.0])

    fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[5]),50.0)+[2]*TMath::Max(TMath::Min(x,[5]),50.0)**2+[3]*TMath::Exp([4]*TMath::Max(TMath::Min(x,[5]),50.0))"
    fitParLimits = [[5,500.0,900.0]]

    if reweightType == "Vpt":
        #rebinning = 5
        fitRangeMin = 50
        #fitRangeMax = 500
    NLOsampleName = 'WJetsToLNu_*J_TuneCP5_13TeV-amcatnloFXFX-pythia8'
    sampleTable = {
            'NLO': [
                ['/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 54601.0],
                [['/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM','/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'], 8939.0],
                [['/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM','/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'], 3511.0]
                ],
            'LO': [
                ['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM',52940.0,'LHE_HT<100'],
                ['/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1395.0],
                ['/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 407.9],
                ['/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 57.48],
                ['/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 12.87],
                ['/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5.366],
                ['/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.074],
                ['/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.03216],
                ]
            }
    
    if applyVptNLOweight:

        # remove range  Vpt < 150
        globalCut = "(LHE_Vpt>150)"

#WJetsToLNu (including ext sample):
#    fit range: 100-500
#    0b: (1.628e+00 + var0*4.637e-03)+(-1.339e-03 + var1*2.052e-05)*(LHE_Vpt)
#    1b: (1.586e+00 + var0*2.657e-02)+(-1.531e-03 + var1*1.118e-04)*(LHE_Vpt)
#    2b: (1.440e+00 + var0*4.865e-02)+(-9.250e-04 + var1*2.034e-04)*(LHE_Vpt)

        # apply Vpt weight to LO samples
        if sys.argv[3] == '0b':
            weightLO = "(1.628 - 1.339e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '1b':
            weightLO = "(1.586 - 1.531e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '2b':
            weightLO = "(1.440 - 9.250e-4*min(LHE_Vpt,500.0))"


elif sample == "WBJets":
    rebinning = np.array([0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,180.0,200.0,220.0,240.0,260.0,300.0,350.0,400.0,450.0,500.0,600.0,700.0,800.0,1000.0])

    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),50.0)+[2]*TMath::Max(TMath::Min(x,[3]),50.0)**2"
    #fitParLimits = [[3,300.0,900.0]]
    fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),200.0)+[2]*TMath::Min(x,[3])+[4]*TMath::Min(TMath::Max(x,200.0),[5])"
    fitParLimits = [[3,300.0,400.0],[5,500,900]]

    if reweightType == "Vpt":
        #rebinning = 5
        fitRangeMin = 100
        #fitRangeMax = 500
    NLOsampleName = 'WJetsToLNu_*J_TuneCP5_13TeV-amcatnloFXFX-pythia8'
    sampleTable = {
            'NLO': [
                ['/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 54601.0],
                [
                    [
                        '/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM',
                        '/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'
                    ], 8939.0
                ],
                [
                    [
                        '/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM',
                        '/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'
                    ], 3511.0
                ]
                ],
            'LO': [
                ['/WBJetsToLNu_Wpt-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',5.542],
                ['/WBJetsToLNu_Wpt-200toInf_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',0.801],
                ['/WJetsToLNu_BGenFilter_Wpt-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',20.56],
                ['/WJetsToLNu_BGenFilter_Wpt-200toInf_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',2.936],
                ]
            }

    globalCut = "(LHE_Vpt>100&&(LHE_Nb>0||{nGenStatus2bHad}>0))".format(nGenStatus2bHad=nGenStatus2bHad)


    if applyVptNLOweight:
        raise Exception("not implemented")


elif sample == "ZJets":
    rebinning = np.array([0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,180.0,200.0,220.0,240.0,260.0,300.0,350.0,400.0,450.0,500.0,600.0,700.0,800.0,1000.0])
    fitRangeMin = 100
    #fitRangeMax = 400
    
    fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),200.0)+[2]*TMath::Min(x,[3])+[4]*TMath::Min(TMath::Max(x,200.0),[5])+TMath::Max(x,[5])*[6]"
    fitParLimits = [[3,300.0,400.0],[5,500,800]]

    NLOsampleName = "Z*JetsToNuNu_M-50_LHEZpT_*_TuneCP5_13TeV-amcnloFXFX-pythia8"
    globalCut = "(LHE_HT>100&&LHE_Vpt>100)"
    sampleTable = {
            'NLO': [
                ['/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 596.4],
                [
                    ['/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',
                     '/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 18.0],
                [
                    ['/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM','/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 2.057],
                [
                    ['/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM','/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 0.224], 
                ['/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 325.7],
                [
                    ['/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', '/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 29.76],
                [
                    ['/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', '/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 5.164],
                [
                    ['/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM','/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 0.8457]

                ],
            'LO': [
                ['/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 304.5],
                ['/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 91.85],
                ['/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 13.11],
                ['/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3.257],
                ['/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.49],
                ['/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.3419],
                ['/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.005146],
                ]
            }

    if reweightType == "deltaEta":
        fitRangeMin = 0.0
        fitRangeMax = 4.0

    # apply weight in first variable!
    if applyVptNLOweight:

        # remove range  Vpt < 100
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>150&&LHE_Vpt<170)"
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>170&&LHE_Vpt<200)"
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>150&&LHE_Vpt<200)"
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>200&&LHE_Vpt<250)"
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>250&&LHE_Vpt<300)"
        #globalCut = "((" + globalCut + ")&&LHE_Vpt>300&&LHE_Vpt<400)"
#ZJetsToNuNu (including ext sample):
#    0b: (1.688e+00 + var0*1.727e-03)+(-1.785e-03 + var1*7.239e-06)*(LHE_Vpt)
#    1b: (1.575e+00 + var0*6.579e-03)+(-1.754e-03 + var1*2.721e-05)*(LHE_Vpt)
#    2b: (1.424e+00 + var0*1.035e-02)+(-1.539e-03 + var1*4.161e-05)*(LHE_Vpt)

        # apply Vpt weight to LO samples
        if sys.argv[3] == '0b':
            weightLO = "(1.688 - 1.785e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '1b':
            weightLO = "(1.575 - 1.754e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '2b':
            weightLO = "(1.424 - 1.539e-3*min(LHE_Vpt,500.0))"

elif sample == "ZBJets":
    rebinning = np.array([0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,180.0,200.0,220.0,240.0,260.0,300.0,350.0,400.0,450.0,500.0,600.0,700.0,800.0,1000.0])
    fitRangeMin = 100
    #fitRangeMax = 400
    
    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,400.0),200.0)+[2]*TMath::Min(x,200.0)"
    fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),200.0)+[2]*TMath::Min(x,[3])+[4]*TMath::Min(TMath::Max(x,200.0),[5])"
    fitParLimits = [[3,300.0,400.0],[5,500,900]]

    NLOsampleName = "Z*JetsToNuNu_M-50_LHEZpT_*_TuneCP5_13TeV-amcnloFXFX-pythia8"
    globalCut = "(LHE_Vpt>100&&(LHE_Nb>0||{nGenStatus2bHad}>0))".format(nGenStatus2bHad=nGenStatus2bHad)
    sampleTable = {
            'NLO': [
                ['/Z1JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 596.4],
                [
                    ['/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',
                     '/Z1JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 18.0],
                [
                    ['/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM','/Z1JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 2.057],
                [
                    ['/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM','/Z1JetsToNuNu_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 0.224], 
                ['/Z2JetsToNuNu_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 325.7],
                [
                    ['/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', '/Z2JetsToNuNu_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 29.76],
                [
                    ['/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', '/Z2JetsToNuNu_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 5.164],
                [
                    ['/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM','/Z2JetsToNuNU_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'], 0.8457]
                ],
            'LO': [
                ['/ZBJetsToNuNu_Zpt-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',6.209],
                ['/ZBJetsToNuNu_Zpt-200toInf_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',0.6286],
                #factor 3.0 corrects that only 1 neutrino type was used
                ['/ZJetsToNuNu_BGenFilter_Zpt-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',1.689*3.0],
                ['/ZJetsToNuNu_BGenFilter_Zpt-200toInf_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',0.2476*3.0],

                ]
            }

    # apply weight in first variable!
    if applyVptNLOweight:
        raise Exception("not implemented")

elif sample == "DYJets":
    rebinning = np.array([0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,180.0,200.0,220.0,240.0,260.0,300.0,350.0,400.0,450.0,500.0,600.0,700.0,800.0,1000.0])

    if reweightType == "Vpt":
        fitRangeMin = 50
        #fitRangeMax = 500
    NLOsampleName = "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8"
    globalCut = "(LHE_Vpt>50)"
    sampleTable = {
            'NLO': [
                [['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM','/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'], 6529.0],
                ],
            'LO': [
                [['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017RECOSIMstep_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM','/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017RECOSIMstep_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'], 5343.0, '(LHE_HT<100)'],
                ['/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 161.1],
                [['/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM','/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'], 48.66],
                ['/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM', 6.968],
                ['/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.743],
                ['/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.8052],
                ['/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.1933],
                ['/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.00347],
                ]
            }
#    DYJetsToLL (including ext sample):
#        fit range: 50-500
#        0b: (1.650e+00 + var0*2.112e-03)+(-1.707e-03 + var1*1.960e-05)*(LHE_Vpt)
#        1b: (1.534e+00 + var0*9.535e-03)+(-1.485e-03 + var1*8.048e-05)*(LHE_Vpt)
#        2b: (1.519e+00 + var0*1.868e-02)+(-1.916e-03 + var1*1.396e-04)*(LHE_Vpt)
        
    if applyVptNLOweight:
        # apply Vpt weight to LO samples
        if sys.argv[3] == '0b':
            weightLO = "(1.650 - 1.707e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '1b':
            weightLO = "(1.534 - 1.485e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '2b':
            weightLO = "(1.519 - 1.916e-3*min(LHE_Vpt,500.0))"

elif sample == "DYBJets":
    rebinning = np.array([0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,180.0,200.0,220.0,240.0,260.0,300.0,350.0,400.0,450.0,500.0,600.0,700.0,800.0,1000.0])
    
    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),[4])+[2]*TMath::Min(x,[3])+[5]*TMath::Max(x,[4])"
    #fitParLimits = [[3,260.0,900.0],[4,50.0,250.0]]
    #fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),200.0)+[2]*TMath::Min(x,[3])+[4]*TMath::Max(x,200.0)"
    #fitParLimits = [[3,260.0,900.0]]
    fitModel    = "[0]+[1]*TMath::Max(TMath::Min(x,[3]),200.0)+[2]*TMath::Min(x,[3])+[4]*TMath::Min(TMath::Max(x,200.0),[5])"
    fitParLimits = [[3,300.0,400.0],[5,500,900]]

    if reweightType == "Vpt":
        fitRangeMin = 50
        #fitRangeMax = 500
    NLOsampleName = "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8"
    globalCut = "(LHE_Vpt>100&&(LHE_Nb>0||{nGenStatus2bHad}>0))".format(nGenStatus2bHad=nGenStatus2bHad) 
    sampleTable = {
            'NLO': [
                [['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM','/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM'], 6529.0],
                ],
            'LO': [
                ['/DYBJetsToLL_M-50_Zpt-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 3.224],
                ['/DYBJetsToLL_M-50_Zpt-200toInf_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 0.3298],
                ['/DYJetsToLL_BGenFilter_Zpt-100to200_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 2.671],
                ['/DYJetsToLL_BGenFilter_Zpt-200toInf_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_newgridpack/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM', 0.3934],
                ]
            }

    if applyVptNLOweight:
        raise Exception("not implemented")

elif sample == "DYJetsPtBinned":
    if reweightType == "Vpt":
        fitRangeMin = 150
        fitRangeMax = 500
    NLOsampleName = "DYJetsToLL_Pt-*_TuneCP5_13TeV-amcatnloFXFX-pythia8" 
    globalCut = "(LHE_Vpt>100)"
    sampleTable = {
            'NLO': [
                ['/DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 97.36],
                ['/DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3.774],
                ['/DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.5148],
                ['/DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.04814],
                ],
            'LO': [
                ['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017RECOSIMstep_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5343.0, '(LHE_HT<100)'],
                ['/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 161.1],
                ['/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 48.66],
                ['/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM', 6.968],
                ['/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.743],
                ['/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.8052],
                ['/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.1933],
                ['/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.00347],
                ]
            }
    
    if applyVptNLOweight:
        # apply Vpt weight to LO samples
        if sys.argv[3] == '2b':
            weightLO = "(1.177 - 1.357e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '1b':
            weightLO = "(1.257 - 1.401e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '0b':
            weightLO = "(1.360 - 1.400e-3*min(LHE_Vpt,500.0))"

elif sample == "WJetsPtBinned":
    if reweightType == "Vpt":
        fitRangeMin = 150
        fitRangeMax = 500
    NLOsampleName = "WJetsToLNu_Pt-*_TuneCP5_13TeV-amcatnloFXFX-pythia8"
    globalCut = "(LHE_Vpt>100)"
    sampleTable = {
            'NLO': [
                ['/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3567],
                ['/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 772.7],
                ['/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 27.98],
                ['/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 3.591],
                ['/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.5505],
                ],
            'LO': [
                ['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM',52940.0,'(LHE_HT<100)'],
                ['/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1395.0],
                ['/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 407.9],
                ['/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 57.48],
                ['/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 12.87],
                ['/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 5.366],
                ['/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 1.074],
                ['/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM', 0.03216],
                ]
            }
    
    if applyVptNLOweight:
        # apply Vpt weight to LO samples
        if sys.argv[3] == '2b':
            weightLO = "(1.000 - 6.495e-4*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '1b':
            weightLO = "(1.202 - 1.179e-3*min(LHE_Vpt,500.0))"
        elif sys.argv[3] == '0b':
            weightLO = "(1.374 - 1.221e-3*min(LHE_Vpt,500.0))"


if binName.startswith("0b"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)<1")
elif binName.startswith("1b"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)==1")
elif binName.startswith("2b"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)>1")
elif binName.startswith("udsg"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)<1&&Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==4)<1")
elif binName.startswith("c"):
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)<1&&Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==4)>0")
elif binName == '1b1c':
    globalCut = cutAnd(globalCut, "Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)==1&&Sum$(GenJet_pt>25 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==4)==1")
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
    elif binNameParts[1] == 'M':
        globalCut = cutAnd(globalCut, "Max$(Jet_btagDeepB)>0.4941")
    elif binNameParts[1] == 'ML':
        globalCut = cutAnd(globalCut, "Max$(Jet_btagDeepB)>0.4941&&Sum$(Jet_pt>20.0&&Jet_btagDeepB>0.1522)>1")
    elif binNameParts[1] == 'TT':
        globalCut = cutAnd(globalCut, "Sum$(Jet_pt>20.0&&Jet_btagDeepB>0.8001)>1")

tmpFolder = "tmp_" + nloWeightVersionName + "/" + sample
try:
    os.makedirs(tmpFolder)
except:
    pass

outFileName = "nloweight_histograms_" + sample + "_" + nloWeightVersion + "_" + binName + ".root"
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
        # for extension samples a list of samples can be given
        if type(sampleName) == list:
            sampleName = '_'.join(sampleName)
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
                fileExists = os.path.isfile(outputFileName)
                if fileExists:
                    fileGood = False
                    f = ROOT.TFile.Open(outputFileName, 'read')
                    if f:
                        fileGood = not (f.IsZombie() or f.GetNkeys() == 0 or f.TestBit(ROOT.TFile.kRecovered))
                        try:
                            f.Close()
                        except:
                            pass
                else:
                    fileGood = False
                if not fileExists or not fileGood: 
                    wlo = weightLO if cat == 'LO' else '1.0'
                    #jobString = submissionCommand + "./nano_to_histogram.py --cut='{cut}' --var 'LHE_Vpt' --min 0 --max 1000 --nbins 100 --input='{input}' --output='{output}'".format(input=fileName, output=outputFileName, cut=totalCut)
                    jobString = submissionCommand + "./nano_to_histogram.py --cut='({cut})*{wlo}' --var='{reweightVar}' --min {reweightVarMin} --max {reweightVarMax} --nbins {reweightVarNbins} --input='{input}' --output='{output}'".format(input=fileName, output=outputFileName, cut=totalCut,wlo=wlo,reweightVar=reweightVar, reweightVarMin=reweightVarMin, reweightVarMax=reweightVarMax, reweightVarNbins=reweightVarNbins)
                    print(jobString)
                    stdOutput = subprocess.check_output([jobString], shell=True)
                    print("=>", stdOutput)
                    sleep(0.1)
                    jobs.append(jobString)
                else:
                    print("=> file exists and it valid.")

            elif sys.argv[1] == "run":
                if os.path.isfile(outputFileName):
                    goodFile = True
                    if not any([x in outputFileName for x in filterBadFiles]):
                        f1 = ROOT.TFile.Open(outputFileName, "READ")
                        if f1 is not None:
                            try:
                                isValid = not (f1.IsZombie() or f1.GetNkeys() == 0 or f1.TestBit(ROOT.TFile.kRecovered))
                            except:
                                isValid = False
                                goodFile = False
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
                                goodFile = False
                                try:
                                    f1.Close()
                                except:
                                    pass
                    else:
                        print("\x1b[33m ignore:",outputFileName,"\x1b[0m")
                    if goodFile:
                        print("\x1b[32m",outputFileName,"\x1b[0m")
                    else:
                        print("\x1b[34m",outputFileName,"\x1b[0m")

                else:
                    print("\x1b[31m",outputFileName,"\x1b[0m")
        if sys.argv[1] == "run":
            if genEventSumw[cat][sampleName] < 1: 
                print("\x1b[31mEMPTY:", cat, sampleName,"\x1b[0m")
                allSamplesNonEmpty = False
                exit(1)
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
            if type(sampleName) == list:
                sampleName = '_'.join(sampleName)
            histograms[cat][sampleName].Scale(crossSection/genEventSumw[cat][sampleName])

    # sum up histograms
    for cat in sampleTable.keys():
        totalHistograms[cat] = ROOT.TH1D(cat,cat,reweightVarNbins,reweightVarMin,reweightVarMax)
        totalHistograms[cat].Sumw2()
        totalHistograms[cat].SetDirectory(outfile)
        for sampleData in sampleTable[cat]:
            sampleName   = sampleData[0]
            if type(sampleName) == list:
                sampleName = '_'.join(sampleName)
            totalHistograms[cat].Add(histograms[cat][sampleName])

    # make ratio   
    c1 = ROOT.TCanvas("c1","c1",500,500)
    hist_ratio = ROOT.TH1D("ratio","ratio",reweightVarNbins,reweightVarMin,reweightVarMax)
    if rebinning is not None:
        if type(rebinning)==np.ndarray:
            hNLO = totalHistograms['NLO'].Rebin(len(rebinning)-1,"hNLO",rebinning)
            hLO = totalHistograms['LO'].Rebin(len(rebinning)-1,"hLO",rebinning)
            hist_ratio = hNLO 
            hist_ratio.Divide(hLO)
            print("rebin:", rebinning)
        else:
            totalHistograms['NLO'].Rebin(rebinning)
            totalHistograms['LO'].Rebin(rebinning)
            hist_ratio = totalHistograms['NLO'].Clone()
            hist_ratio.Divide(totalHistograms['LO'])
    else:
        hist_ratio.Add(totalHistograms['NLO'])
        hist_ratio.Divide(totalHistograms['LO'])
    hist_ratio.SetDirectory(outfile)
    hist_ratio.SetStats(0)
    hist_ratio.GetXaxis().SetTitle(reweightVar)
    hist_ratio.GetYaxis().SetTitle("NLO/LO")
    hist_ratio.GetYaxis().SetRangeUser(0,2)
    hist_ratio.Draw()

    pol1 = ROOT.TF1("f1",fitModel, fitRangeMin, fitRangeMax)
    if fitParLimits is not None:
        for x in fitParLimits:
            pol1.SetParLimits(x[0],x[1],x[2])

    #hist_ratio.Fit(pol1, "RB")
    fitResult = hist_ratio.Fit(pol1, "RBS")
    if not fitResult.IsValid():
        print("ERROR: fit result invalid.")
        fitResult = hist_ratio.Fit(pol1, "RBS")
        if not fitResult.IsValid():
            print("ERROR: fit result invalid [2].")

        
    grint = ROOT.TGraphErrors(hist_ratio.GetXaxis().GetNbins())
    for i in range(hist_ratio.GetXaxis().GetNbins()):
        grint.SetPoint(i,hist_ratio.GetBinCenter(1+i), 0)
    ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint, 0.95)
    grint.SetLineColor(ROOT.kBlack)
    grint.SetFillStyle(3003)
    grint.SetFillColor(ROOT.kCyan-3)
    grint.Draw("e3 same")

    grint2 = ROOT.TGraphErrors(hist_ratio.GetXaxis().GetNbins())
    for i in range(hist_ratio.GetXaxis().GetNbins()):
        grint2.SetPoint(i,hist_ratio.GetBinCenter(1+i), 0)
    ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint2, 0.68)
    grint2.SetLineColor(ROOT.kBlue)
    grint2.SetFillStyle(3001)
    #grint2.SetFillColor(ROOT.kYellow-6)
    grint2.SetFillColor(ROOT.kMagenta-3)
    grint2.Draw("e3 same")

    hist_ratio.Draw("same")

    leg = ROOT.TLegend(0.7,0.75,0.88,0.88)
    leg.AddEntry(hist_ratio,"NLO/LO")
    leg.AddEntry(pol1,"fit")
    leg.AddEntry(grint2, "68% CI")
    leg.AddEntry(grint, "95% CI")
    leg.Draw()

    grint.SetTitle("ci95")
    outfile.cd()
    grint.Write("ci95")
    grint2.SetTitle("ci68")
    grint2.Write("ci68")
    pol1.Write("fit")

    fitParListWithErrors = sum([ [pol1.GetParameter(i), pol1.GetParError(i)] for i in range(pol1.GetNpar())], [])
    print("\x1b[32mFIT RESULT:", fitParListWithErrors, "\x1b[0m") 

    fitFormulaString = fitModel
    for i in range(pol1.GetNpar()):
        fitFormulaString = fitFormulaString.replace("[%i]"%i, "(%1.3e + var%i*%1.3e)"%(pol1.GetParameter(i), i,  pol1.GetParError(i)))
    print(fitFormulaString)

    latex = ROOT.TLatex()
    latex.SetTextSize(0.021)
    latex.SetTextAlign(13)
    latex.DrawLatexNDC(.14,.23,NLOsampleName)
    latex.SetTextSize(0.025)
    latex.DrawLatexNDC(.14,.19,binName)
    latex.SetTextSize(0.015)
    latex.DrawLatexNDC(.14,.15,fitFormulaString)
    
    fitFormulaString = fitFormulaString.replace("x","(" + reweightVar + ")")
    print(fitFormulaString)

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

