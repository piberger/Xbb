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
mvaName = 'ZllBDT_highpt'
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
config.read(testConfiguration + '/training.ini')
config.read(testConfiguration + '/cuts.ini')
config.read(testConfiguration + '/samples_nosplit.ini')

samplesPath = config.get('Directories', 'MVAin')
samplesinfo = testConfiguration + '/samples_nosplit.ini'
info = ParseInfo(samplesinfo, samplesPath)

cachedPath = config.get('Directories', 'tmpSamples')
tmpPath = config.get('Directories', 'scratch')

sampleFilesFolder = config.get('Directories', 'samplefiles')

backgroundSampleNames = eval(config.get(mvaName, 'backgrounds'))
signalSampleNames = eval(config.get(mvaName, 'signals'))

samples = info.get_samples(backgroundSampleNames + signalSampleNames)

treeCutName = config.get(mvaName, 'treeCut')
treeCut = config.get('Cuts', treeCutName)

samplesToCache = []
for sample in samples:
    if sample.identifier not in samplesToCache:
        samplesToCache.append(sample.identifier)

print "--samples to cache------"
for sampleToCache in samplesToCache:
    print " > ",sampleToCache


# ----------------------------------------------------------------------------------------------------------------------
# cache samples
# ----------------------------------------------------------------------------------------------------------------------
# for this test run caching for all samples sequentially
for sampleToCache in samplesToCache:
    print '*'*80
    print ' ', sampleToCache
    print '*'*80
    # prepare caches for training and evaluation samples
    treeCaches = []
    sampleTree = None
    for sample in samples:

        if sample.identifier == sampleToCache:
            # for the first sample which comes from this files, load the tree
            if not sampleTree:
                sampleTree = SampleTree({'name': sample.identifier, 'folder': samplesPath})
            for additionalCut in [TrainCut, EvalCut]:

                # cuts
                sampleCuts = [sample.subcut]
                if additionalCut:
                    sampleCuts.append(additionalCut)
                if treeCut:
                    sampleCuts.append(treeCut)
                cutList = '&&'.join(['(%s)'%x for x in sorted(sampleCuts)])

                treeCaches.append(
                    TreeCache.TreeCache(
                        sample=sample.name,
                        cutList=cutList,
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
