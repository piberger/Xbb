#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo

import os

# ----------------------------------------------------------------------------------------------------------------------
# configuration
# ----------------------------------------------------------------------------------------------------------------------
testConfiguration = 'TestZll2016config/'
backgroundSampleNames = ['HT100to200ZJets_udscg_ext1', 'HT100to200ZJets_1b_ext1', 'HT100to200ZJets_2b_ext1', 'HT200to400ZJets_udscg', 'HT200to400ZJets_1b', 'HT200to400ZJets_2b']
signalSampleNames = ['ZH_HToBB_ZToLL_M125_pow_ext1']
samplesToCache = [
    'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1',
    'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
]
TrainCut = '!((evt%2)==0||isData)'
EvalCut = '((evt%2)==0||isData)'

if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

# ----------------------------------------------------------------------------------------------------------------------
# load config
# ----------------------------------------------------------------------------------------------------------------------
config = BetterConfigParser()
config.read(testConfiguration + '/paths.ini')
config.read(testConfiguration + '/general.ini')
config.read(testConfiguration + '/samples_nosplit.ini')

samplesPath = config.get('Directories', 'MVAin')
samplesinfo = testConfiguration + '/samples_nosplit.ini'
info = ParseInfo(samplesinfo, samplesPath)

cachedPath = config.get('Directories', 'tmpSamples')
tmpPath = config.get('Directories', 'scratch')

sampleFilesFolder = config.get('Directories', 'samplefiles')

samples = info.get_samples(backgroundSampleNames + signalSampleNames)

# ----------------------------------------------------------------------------------------------------------------------
# cache samples
# ----------------------------------------------------------------------------------------------------------------------
# for this test run caching for all samples sequentially
for sampleToCache in samplesToCache:

    sampleFilesListFileName = sampleFilesFolder + sampleToCache + '.txt'
    sampleTree = SampleTree(sampleFilesListFileName)

    # prepare caches for training and evaluation samples
    treeCaches = []
    for sample in samples:

        if sample.identifier == sampleToCache:
            print sample.name, "\x1b[31m", sample.subcut, "\x1b[0m"
            print " =>", sample.identifier

            for additionalCut in [TrainCut, EvalCut, None]:
                treeCaches.append(
                    TreeCache.TreeCache(
                        sample=sample.name,
                        cutList=('(%s)&&(%s)'%(sample.subcut, additionalCut)) if additionalCut else sample.subcut,
                        inputFolder=samplesPath,
                        tmpFolder=tmpPath,
                        outputFolder=cachedPath,
                        debug=True
                    ).setSampleTree(sampleTree).cache()
                )

    if len(treeCaches) > 0:
        # run on the tree
        sampleTree.process()

    else:
        print "noting to do!"
