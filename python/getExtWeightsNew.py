#!/usr/bin/env python
import ROOT
import sys
ROOT.gROOT.SetBatch(True)
from myutils import BetterConfigParser, ParseInfo
import glob
from multiprocessing import Process
from myutils.sampleTree import SampleTree as SampleTree

# 1) ./getExtWeights.py configname
# 2) ./getExtWeight.py configname verify

def countEvents(rootFileName, cut = "1"):

    f = ROOT.TFile.Open(rootFileName)
    if not f or f.IsZombie():
        print "\x1b[31mnot found:",rootFileName,"\x1b[0m"
    tree = f.Get("tree")
    nevents = 1.* tree.Draw("1",cut,"goff")
    f.Close()
    return nevents

def getEventCount(config, sampleIdentifier, cut="1"):
    sysOut = config.get('Directories','SYSout').strip()
    t3proto = 'root://t3dcachedb.psi.ch:1094'
    sysOutMountedPath = sysOut.replace(t3proto,'').replace('root://t3dcachedb03.psi.ch:1094','')
    fileMask = "{path}/{sample}/{tree}.root".format(path=sysOutMountedPath, sample=sampleIdentifier, tree='*')
    sampleFiles = [t3proto + x for x in glob.glob(fileMask)]

    sampleTree = SampleTree(sampleFiles, config=config)
    nEvents = sampleTree.tree.Draw("1", cut, "goff")
    print sampleIdentifier,"(",len(sampleFiles),"files) =>",nEvents
    return nEvents

configFolder = sys.argv[1]

# load config
config = BetterConfigParser()
config.read(configFolder + '/paths.ini')
config.read(configFolder + '/general.ini')
config.read(configFolder + '/cuts.ini')
config.read(configFolder + '/training.ini')
config.read(configFolder + '/datacards.ini')
config.read(configFolder + '/plots.ini')
config.read(configFolder + '/lhe_weights.ini')
config.read(configFolder + '/samples_nosplit.ini')

samples = ['DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1', 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2']
sampleCut = '(lheHT<100)'

eventCounts = {sample: getEventCount(config, sample, sampleCut) for sample in samples}
totalCount = sum([v for k,v in eventCounts.iteritems()])*1.0

print '-'*160
print "CUT:", sampleCut
print '-'*160
for i, sample in enumerate(samples):
    print sample.ljust(100),('%d'%eventCounts[sample]).ljust(30),('%1.5f'%(1.0 * eventCounts[sample] / totalCount)).ljust(30)
print '-'*160




