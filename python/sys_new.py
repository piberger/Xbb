#!/usr/bin/env python
import sys
import os
import subprocess
import ROOT 
ROOT.gROOT.SetBatch(True)
from array import array
from optparse import OptionParser
from myutils.FileList import FileList
from myutils import BetterConfigParser, ParseInfo, LeptonSF
from myutils.FileLocator import FileLocator
from myutils.sampleTree import SampleTree
from myutils.VtypeCorrector import VtypeCorrector
from myutils.AdditionalJetIndex import AdditionalJetIndex
from myutils.TTWeights import TTWeights
from myutils.EWKweights import EWKweights
from myutils.BTagWeights import BTagWeights
from myutils.LeptonWeights import LeptonWeights
from myutils.JetEnergySystematics import JetEnergySystematics
from myutils.WPtReweight import WPtReweight

argv = sys.argv
parser = OptionParser()
parser.add_option("-S", "--sampleIdentifier", dest="sampleIdentifier", default="", 
                      help="samples you want to run on")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration defining the plots to make")
parser.add_option("-f", "--fileList", dest="fileList", default="",
                              help="list of files you want to run on")
parser.add_option("-b", "--addCollections", dest="addCollections", default="",
                              help="collections to add: vtype")
parser.add_option("-F", "--force", dest="force", action="store_true", help="overwrite existing files", default=False)
(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = "config"

filelist = FileList.decompress(opts.fileList) if len(opts.fileList)>0 else None
print "len(filelist)",len(filelist),
if len(filelist)>0:
    print "filelist[0]:",filelist[0];
else:
    print ''

config = BetterConfigParser()
config.read(opts.config)
anaTag = config.get("Analysis","tag")
TrainFlag = eval(config.get('Analysis','TrainFlag'))
btagLibrary = config.get('BTagReshaping','library')
samplesinfo=config.get('Directories','samplesinfo')
channel=config.get('Configuration','channel')
VHbbNameSpace=config.get('VHbbNameSpace','library')
ROOT.gSystem.Load(VHbbNameSpace)
pathIN = config.get('Directories','SYSin')
pathOUT = config.get('Directories','SYSout')
tmpDir = config.get('Directories','scratch')
try:
   remove_useless_branch = config.get('Analysis', 'remove_useless_branch').lower().strip() == 'true'
except:
   remove_useless_branch = False
print 'INput samples:\t%s'%pathIN
print 'OUTput samples:\t%s'%pathOUT

fileLocator = FileLocator(config=config)

# samples
info = ParseInfo(samplesinfo, pathIN)
matchingSamples = [x for x in info if x.identifier==opts.sampleIdentifier and not x.subsample]
if len(matchingSamples) != 1:
    print "need exactly 1 sample identifier as input with -S !!"
    print matchingSamples
    exit(1)
sample = matchingSamples[0]

# TODO: 
print 'collections to add:', opts.addCollections
collections = [x.strip() for x in opts.addCollections.split(',') if len(x.strip()) > 0]
if len(collections) < 1:
    print "no collection selected, adding 'vtype'..."
    collections.append('vtype')

for fileName in filelist:
    localFileName = fileLocator.getFilenameAfterPrep(fileName)
    
    inputFileName = "{path}/{subfolder}/{filename}".format(path=pathIN, subfolder=sample.identifier, filename=localFileName)
    outputFileName = "{path}/{subfolder}/{filename}".format(path=pathOUT, subfolder=sample.identifier, filename=localFileName)
    tmpFileName = "{path}/{subfolder}/{filename}".format(path=tmpDir, subfolder=sample.identifier, filename=localFileName)
    outputFolder = '/'.join(outputFileName.split('/')[:-1])
    tmpFolder = '/'.join(tmpFileName.split('/')[:-1])
    fileLocator.makedirs(tmpFolder)
    fileLocator.makedirs(outputFolder)

    if not fileLocator.exists(outputFileName) or opts.force:
        # load sample tree and initialize vtype corrector
        sampleTree = SampleTree([inputFileName], config=config)
        if not sampleTree.tree:
            print "\x1b[31mERROR: file does not exist or is broken, will be SKIPPED!\x1b[0m"
            continue
        
        # ------------------------------------------------------------------------------------------
        # correct Vtype for V25 HEPPY ntuples
        # ------------------------------------------------------------------------------------------
        if 'vtype' in collections:
            vTypeCorrector = VtypeCorrector(tree=sampleTree.tree, channel=channel)

            # (optional) allows the event to be skipped if recomputed vtype does not match 
            sampleTree.addCallback('event', vTypeCorrector.processEvent)

            # get list of new branches to add
            newBranches = vTypeCorrector.getBranches()

            # add the new list of branches
            sampleTree.addOutputBranches(newBranches)

        # ------------------------------------------------------------------------------------------
        # this is just a TEST 
        # ------------------------------------------------------------------------------------------
        if 'ajidx' in collections:
            ajIndexCalculator = AdditionalJetIndex()
            sampleTree.addOutputBranches(ajIndexCalculator.getBranches())

        # ------------------------------------------------------------------------------------------
        # add variables defined in the config 
        # ------------------------------------------------------------------------------------------
        if 'addbranches' in collections:
            writeNewVariables = eval(config.get("Regression", "writeNewVariablesDict"))
            sampleTree.addOutputBranches(writeNewVariables)
        
        # ------------------------------------------------------------------------------------------
        # weights 
        # ------------------------------------------------------------------------------------------
        if 'ttw' in collections or 'weights' in collections:
            if sample.type != 'DATA':
                ttWeights = TTWeights()
                sampleTree.addOutputBranches(ttWeights.getBranches())
        if 'ewkw' in collections or 'weights' in collections:
            if sample.type != 'DATA':
                ewkWeights = EWKweights(tree=sampleTree.tree, sample=sample)
                sampleTree.addOutputBranches(ewkWeights.getBranches())
        if 'btag' in collections or 'weights' in collections:
            if sample.type != 'DATA':
                btagWeights = BTagWeights(tree=sampleTree.tree, sample=sample)
                sampleTree.addOutputBranches(btagWeights.getBranches())
        if 'leptonsf' in collections or 'weights' in collections:
            if sample.type != 'DATA':
                leptonWeights = LeptonWeights(tree=sampleTree.tree, sample=sample, config=config, channel=channel)
                sampleTree.addOutputBranches(leptonWeights.getBranches())
        if 'jes' in collections or 'weights' in collections:
            jetEnergySystematics = JetEnergySystematics(tree=sampleTree.tree, sample=sample, config=config, channel=channel)
            sampleTree.addOutputBranches(jetEnergySystematics.getBranches())
        if 'wptreweight' in collections or 'weights' in collections:
            wptReweight = WPtReweight(tree=sampleTree.tree, sample=sample, channel=channel)
            sampleTree.addOutputBranches(wptReweight.getBranches())

        if remove_useless_branch:
            bl_branch = eval(config.get('Branches', 'useless_branch'))
            for br in bl_branch:
                sampleTree.addBranchToBlacklist(br)

        # define output file 
        sampleTree.addOutputTree(tmpFileName, cut='1', branches='*')
        sampleTree.process()

        # copy temporary file to output folder
        if opts.force and fileLocator.exists(outputFileName):
            fileLocator.rm(outputFileName) 

        fileLocator.cp(tmpFileName, outputFileName)
        fileLocator.rm(tmpFileName)

        print 'copy ', tmpFileName, outputFileName

        if 'vtype' in collections:
            vTypeCorrector.printStatistics()
    else:
        print 'SKIP:', localFileName
    
