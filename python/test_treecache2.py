#!/usr/bin/env python
import math
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree

numSampleFiles = SampleTree.countSampleFiles('test/bkg.txt')
splitFiles = 7
numParts = int(math.ceil(float(numSampleFiles) / splitFiles))
print ("found: %d files"%numSampleFiles)

user = 'berger_p2'

#
numEventsPassed = 0

# cache all parts sequentially for this test, of course one can do this in parallel...
for i in range(1, numParts+1):
    print ("cache part %d of %d"%(i, numParts))

    sampleTreeBkg = SampleTree('test/bkg.txt', splitFiles=splitFiles, splitFilesPart=i)
    tc = TreeCache.TreeCache(
        sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
        cutList='V_pt>100',
        inputFolder='/scratch/' + user + '/',
        tmpFolder='/scratch/' + user + '/tmp/',
        outputFolder='/scratch/' + user + '/cache/',
        cachePart=i,
        cacheParts=numParts,
        splitFiles=splitFiles,
        debug=True
    )

    # run caching
    tc.setSampleTree(sampleTreeBkg).cache()
    sampleTreeBkg.process()
    tc.moveFilesToFinalLocation()

    numEventsPassed += sampleTreeBkg.outputTrees[0]['passed']

# test again!
tc = TreeCache.TreeCache(
    sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
    cutList='V_pt>100',
    inputFolder='/scratch/' + user + '/',
    tmpFolder='/scratch/' + user + '/tmp/',
    outputFolder='/scratch/' + user + '/cache/',
    splitFiles=splitFiles,
    cacheParts=numParts,
    debug=True
)
isCachedAndValid = tc.isCachedAndValid()
print ('is cached and valid? ', isCachedAndValid)

if isCachedAndValid:
    cachedSampleTree = tc.getTree()
    print ("CACHE:    ", cachedSampleTree.tree.GetEntries())
    print ("EXPECTED: ", numEventsPassed)
    if (cachedSampleTree.tree.GetEntries() == numEventsPassed):
        print ('OK!')
    else:
        print ('MISMATCH!')
else:
   raise Exception("CACHE ERROR!!!")

