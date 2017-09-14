#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, mvainfo, ParseInfo

import os

user = os.popen('whoami').read().strip('\n').strip('\r')
testConfiguration = 'TestZll2016config/'

if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

#load config
config = BetterConfigParser()
config.read(testConfiguration + '/paths.ini')
config.read(testConfiguration + '/general.ini')
config.read(testConfiguration + '/samples_nosplit.ini')

samplesPath = '/scratch/{user}/'.format(user=user)
samplesinfo = testConfiguration + '/samples_nosplit.ini'
info = ParseInfo(samplesinfo, samplesPath)
print info

#sampleToCache = 'DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'
sampleToCache = 'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'
#sampleToCache = 'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1'

sampleFilesFolder = config.get('Directories', 'samplefiles')
samples = info.get_samples(['HT100to200ZJets_udscg_ext1', 'HT100to200ZJets_1b_ext1', 'HT100to200ZJets_2b_ext1', 'ZH_HToBB_ZToLL_M125_pow_ext1'])
sampleFilesListFileName = sampleFilesFolder + sampleToCache + '.txt'


sampleTree = SampleTree(sampleFilesListFileName)

TrainCut = '!((evt%2)==0||isData)'
EvalCut = '((evt%2)==0||isData)'

# prepare caches for training and evaluation samples
treeCaches = []
for sample in samples:
    print sample.name, "\x1b[31m", sample.subcut, "\x1b[0m"
    print " =>", sample.identifier

    if sample.identifier == sampleToCache:
        for additionalCut in [TrainCut, EvalCut, None]:
            treeCaches.append(
                TreeCache.TreeCache(
                    sample=sample.name,
                    cutList=('(%s)&&(%s)'%(sample.subcut, additionalCut)) if additionalCut else sample.subcut,
                    inputFolder='/scratch/' + user + '/',
                    tmpFolder='/scratch/' + user + '/tmp/',
                    outputFolder='/scratch/' + user + '/cache/',
                    debug=True
                ).setSampleTree(sampleTree).cache()
            )

if len(treeCaches) > 0:
    # run on the tree
    sampleTree.process()

    # move files to final location
    for cache in treeCaches:
        cache.moveFilesToFinalLocation()
else:
    print "noting to do!"

