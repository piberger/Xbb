#!/usr/bin/env python
import ROOT
import os
from myutils import tensorflowEvaluator
from myutils.sampleTree import SampleTree
from myutils.BetterConfigParser import BetterConfigParser
from myutils.samplesclass import Sample
from myutils.FileLocator import FileLocator


# load libraries
ROOT.gSystem.Load("../interface/VHbbNameSpace_h.so")

scratch = '/scratch/berger_p2/'
xrootdRedirector = "root://t3dcachedb03.psi.ch:1094/"

inputTreeName="Events"

#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June7/signal/ZH125_ZLL_powheg.root"
#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June7/background/T_tW.root"
#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June7/signal/ZH125_ZNuNu_powheg.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June7/signal/eval/" 
#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June7/signal/WplusH125_powheg.root"
#inputFile = "root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/berger_p2/VHbb/AT/sum_WminusH125_powheg.root"

#inputFile="/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2017/3/sum_WminusH125_powheg.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2017/4/" 

#inputFile = "root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/berger_p2/VHbb/AT2016/haddjobs/sum_WminusH125_powheg.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2016/"

#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June16/Tbar_tW.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/SkimForTraining_June16/eval/" 


#inputFile="root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/berger_p2/VHbb/AT/sum_ZH125_ZNuNu_powheg.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2017/1/" 

#inputFile="/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2017/4/sum_ZH125_ZNuNu_powheg.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2017/5/" 

#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/friend2017/Pirmin_checkDNNout/sum_ZH125_ZLL_powheg_0.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/friend2017/Pirmin_checkDNNout/eval/"

#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/friend2017/Pirmin_checkDNNout/sum_WplusH125_powheg_0.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/friend2017/Pirmin_checkDNNout/eval/"

#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/AT_WH/skimWHFCR_June26.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/AT_WH/eval/1/"

#inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/AT_WH/eval/8/skimWHFCR_June26.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/AT_WH/eval/9/"

inputFile = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/AT_WH/eval/2/skimCRSR.root"
outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/AT_WH/eval/3/"

mvaName = "AT_2016DeepCSV_WH_CRSR_MULTI_v2"
tensorflowConfig = "tfZllDNN/export/%s/config.cfg"%mvaName
scalerDump = "tfZllDNN/export/%s/scaler.dmp"%mvaName
checkpoint = "tfZllDNN/export/%s/checkpoints/model.ckpt"%mvaName
branchName = "DNN_%s"%mvaName
nClasses = 5
treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt Jet_btagDeepB[hJetInd1_bestDeepCSV] Jet_btagDeepB[hJetInd2_bestDeepCSV] Top1_mass_fromLepton_regPT_w4MET HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt HJ1_HJ2_dEta'}

#tensorflowConfig = "tfZllDNN/export/AT_June7_DeepCSVfor2017_ZllHigh_v1/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June7_DeepCSVfor2017_ZllHigh_v1/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June7_DeepCSVfor2017_ZllHigh_v1/checkpoints/model.ckpt"
#mvaName = "AT_June7_DeepCSVfor2017_ZllHigh_v1"
#branchName = "DNN_AT_June7_DeepCSVfor2017_ZllHigh_v1"
#treeVarSet = {'Nominal': 'H_mass_fit_fallback H_pt_fit_fallback V_pt hJets_btagged_0 hJets_btagged_1 nAddJets_2lep SA5 V_mass MET_Pt hJets_leadingPt hJets_subleadingPt jjVPtRatio_fit_fallback HJ1_HJ2_dEta HVdPhi_fit_fallback n_recoil_jets_fit H_mass_sigma_fit'}

#tensorflowConfig = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Znn_v1/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Znn_v1/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Znn_v1/checkpoints/model.ckpt"
#mvaName = "AT_June7_DeepCSVfor2017_Znn_v1"
#branchName = "DNN_AT_June7_DeepCSVfor2017_Znn_v1"
##treeVarSet = {'Nominal': 'H_mass H_pt HVdPhi V_pt HJ1_HJ2_dEta hJets_DeepCSV_0 hJets_DeepCSV_1 SA5 HJ1_HJ2_dPhi hJets_leadingPt hJets_subleadingPt otherJetsBestBtag otherJetsHighestPt minDPhiFromOtherJets'}
#treeVarSet = {'Nominal': 'H_mass H_pt HVdPhi V_pt HJ1_HJ2_dEta hJets_btagged_0 hJets_btagged_1 SA5 HJ1_HJ2_dPhi hJets_leadingPt hJets_subleadingPt otherJetsBestBtag otherJetsHighestPt minDPhiFromOtherJets'}


#inputFile = "root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/berger_p2/VHbb/AT2016/haddjobs/sum_WminusH125_powheg.root"
#outputFolder = "/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_10_1_0/src/Xbb/python/tfZllDNN/evalAT2016_Znn/"
#tensorflowConfig = "tfZllDNN/export/AT_June16_Znn_v2/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June16_Znn_v2/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June16_Znn_v2/checkpoints/model.ckpt"
#mvaName = "AT_June16_2016CMVA_Znn_v2"
#branchName = "AT_June16_2016CMVA_Znn_v2"
#treeVarSet = {'Nominal': 'H_mass H_pt HVdPhi V_pt HJ1_HJ2_dEta hJets_btagged_0 hJets_btagged_1 SA5 HJ1_HJ2_dPhi hJets_leadingPt hJets_subleadingPt otherJetsBestBtag otherJetsHighestPt minDPhiFromOtherJets'}


#tensorflowConfig = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wmn_v1/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wmn_v1/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wmn_v1/checkpoints/model.ckpt"
#mvaName = "AT_June7_DeepCSVfor2017_Wmn_v1"
#branchName = "DNN_AT_June7_DeepCSVfor2017_Wmn_v1"
##treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt hJets_DeepCSV_0 hJets_DeepCSV_1 Top1_mass_fromLepton_regPT_w4MET HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt HJ1_HJ2_dEta'}
#treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt hJets_btagged_0 hJets_btagged_1 Top1_mass_fromLepton_regPT_w4MET HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt HJ1_HJ2_dEta'}

#tensorflowConfig = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wmn_v1/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wmn_v1/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wmn_v1/checkpoints/model.ckpt"
#mvaName = "AT_June7_DeepCSVfor2017_Wmn_crosscheckJune20"
#branchName = "DNN_AT_June7_DeepCSVfor2017_Wmn_crosscheckJune20"
##treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt hJets_DeepCSV_0 hJets_DeepCSV_1 Top1_mass_fromLepton_regPT_w4MET HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt HJ1_HJ2_dEta'}
#treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt hJets_btagged_0 hJets_btagged_1 Top1_mass_fromLepton_regPT_w4MET HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt HJ1_HJ2_dEta'}

#tensorflowConfig = "tfZllDNN/export/AT_June16_Wmn_v1/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June16_Wmn_v1/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June16_Wmn_v1/checkpoints/model.ckpt"
#mvaName = "AT_June16_2016CMVA_Wmn_v1"
#branchName = "DO_NOT_USE___DNN_AT_June16_2016CMVAon2017_Wmn_v1"
#treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt hJets_btagged_0 hJets_btagged_1 Top1_mass_fromLepton_regPT_w4MET HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt HJ1_HJ2_dEta'}

#tensorflowConfig = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wen_v1/config.cfg"
#scalerDump = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wen_v1/scaler.dmp"
#checkpoint = "tfZllDNN/export/AT_June7_DeepCSVfor2017_Wen_v1/checkpoints/model.ckpt"
#mvaName = "AT_June7_DeepCSVfor2017_Wen_v1"
#branchName = "DNN_AT_June7_DeepCSVfor2017_Wen_v1"
#treeVarSet = {'Nominal': 'H_mass H_pt jjVPtRatio V_pt hJets_DeepCSV_0 hJets_DeepCSV_1 Top1_mass_fromLepton_regPT_w4MET abs_HVdPhi nAddJets302p5_puid SA5 lepMetDPhi V_mt MET_Pt hJets_leadingPt hJets_subleadingPt abs_HJ1_HJ2_dEta'}


sample = Sample("whateversample", "MC") # or "DATA"

systematics = ['Nominal']

# create minimal Xbb config
config = BetterConfigParser()
config.add_section(mvaName)
config.set(mvaName, "tensorflowConfig", tensorflowConfig)
config.set(mvaName, "scalerDump", scalerDump) 
config.set(mvaName, "checkpoint", checkpoint) 
config.set(mvaName, "branchName", branchName)
config.set(mvaName, "nClasses", "%d"%nClasses)
config.set(mvaName, "treeVarSet", "dnnVars") 
config.add_section("systematics")
config.set("systematics", "systematics", " ".join(systematics))
config.add_section("dnnVars")
for syst in systematics:
    config.set("dnnVars", syst, treeVarSet[syst])

# helper for fs operations
fileLocator = FileLocator(config=config, xrootdRedirector=xrootdRedirector)
fileLocator.mkdir(outputFolder)

# load input files
sampleTree = SampleTree([inputFile], treeName=inputTreeName, xrootdRedirector=xrootdRedirector)

# load tensorflow evaluator
tfe = tensorflowEvaluator.tensorflowEvaluator(mvaName)
tfe.customInit({'config': config, 'sample': sample, 'sampleTree': sampleTree})

# register callbacks for processing
sampleTree.addCallback('event', tfe.processEvent)

# define new branches to add
sampleTree.addOutputBranches(tfe.getBranches())

try:
    os.makedirs(outputFolder)
except:
    pass

# define output file 
tmpFileName = scratch + '/' + inputFile.split('/')[-1]
outputFileName = outputFolder + '/' + inputFile.split('/')[-1]
sampleTree.addOutputTree(tmpFileName, cut='weight<999&&weight>-999', branches='*')

# process tree
sampleTree.process()

# copy to final location
try:
    fileLocator.cp(tmpFileName, outputFileName)
except Exception as e:
    print "\x1b[31mERROR: copy from scratch to final destination failed!!\x1b[0m"
    print e
try:
    fileLocator.rm(tmpFileName)
except Exception as e:
    print "ERROR: could not delete file on scratch!"
    print e

print 'written to ', outputFileName
