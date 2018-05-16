#!/usr/bin/env python
import ROOT
from myutils import tensorflowEvaluator
from myutils.sampleTree import SampleTree
from myutils.BetterConfigParser import BetterConfigParser
from myutils.samplesclass import Sample
from myutils.FileLocator import FileLocator


# load libraries
ROOT.gSystem.Load("../interface/VHbbNameSpace_h.so")

scratch = '/scratch/berger_p2/'
xrootdRedirector = "root://t3dcachedb03.psi.ch:1094/"

inputFile = xrootdRedirector + "/pnfs/psi.ch/cms/trivcat/store/user/berger_p2/ZllHbb13TeV_V25/sys/v8_retrainedBDT_dnn15highLow_incl_highBtag_XEhigh//ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/tree_5c48971819b660ba032ddb5d310b031cb10f7cd12f9b7ae8f598e03f_22_9cfe22473e48a8331f087c9e97dc9cfa958f53389229873b937cd9c7.root"
outputFolder = xrootdRedirector + "/pnfs/psi.ch/cms/trivcat/store/user/berger_p2/ZllHbb13TeV_V25/sys/test_standalone/"
tensorflowConfig = "tfZllDNN/export/Zll2016lowpt_15_xe_v1/Zll2016lowpt_15_xe_v2.cfg"
scalerDump = "tfZllDNN/export/Zll2016lowpt_15_xe_v1/scaler.dmp"
checkpoint = "tfZllDNN/export/Zll2016lowpt_15_xe_v1/checkpoints/model.ckpt"
mvaName = "tfZllDNN_lowpt15xe"
branchName = "dnn15LowXE"
sample = Sample("whateversample", "MC") # or "DATA"

systematics = ['Nominal']
treeVarSet = {'Nominal': 'HCMVAV2_reg_mass HCMVAV2_reg_pt abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) Jet_btagCMVAV2[hJCMVAV2idx[0]] Jet_btagCMVAV2[hJCMVAV2idx[1]] hJetCMVAV2_pt_reg_0 hJetCMVAV2_pt_reg_1 V_new_mass Sum$(hJetCMVAV2_pt_reg>30&&abs(Jet_eta)<2.4&&Jet_puId==7&&Jet_id>0&&aJCidx!=(hJCMVAV2idx[0])&&(aJCidx!=(hJCMVAV2idx[1]))) V_new_pt (HCMVAV2_reg_pt/V_new_pt) abs(Jet_eta[hJCMVAV2idx[0]]-Jet_eta[hJCMVAV2idx[1]]) softActivityVH_njets5 VHbb::deltaR(HCMVAV2_reg_eta,HCMVAV2_reg_phi,V_new_eta,V_new_phi) met_pt'}

# create minimal Xbb config
config = BetterConfigParser()
config.add_section(mvaName)
config.set(mvaName, "tensorflowConfig", tensorflowConfig)
config.set(mvaName, "scalerDump", scalerDump) 
config.set(mvaName, "checkpoint", checkpoint) 
config.set(mvaName, "branchName", branchName)
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
sampleTree = SampleTree([inputFile], treeName="tree", xrootdRedirector=xrootdRedirector)

# load tensorflow evaluator
tfe = tensorflowEvaluator.tensorflowEvaluator(mvaName)
tfe.customInit({'config': config, 'sample': sample, 'sampleTree': sampleTree})

# register callbacks for processing
sampleTree.addCallback('event', tfe.processEvent)

# define new branches to add
sampleTree.addOutputBranches(tfe.getBranches())

# define output file 
tmpFileName = scratch + '/' + inputFile.split('/')[-1]
outputFileName = outputFolder + '/' + inputFile.split('/')[-1]
sampleTree.addOutputTree(tmpFileName, cut='1', branches='*')

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
