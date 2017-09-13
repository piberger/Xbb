#!/usr/bin/env python
import sys
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree

def test_mincut():
    cuts = ['pt>0', '(phi > 0)', 'eta>0&&phi>1']
    tc = TreeCache.TreeCache("", cuts)
    print ('CUTS:', cuts)
    print ('MINCUT:', tc.minCut)

test_mincut()


tc = TreeCache.TreeCache(
    sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
    cutList='V_pt>100',
    inputFolder='/scratch/p/',
    outputFolder='/scratch/p/tmp/',
    debug=True
)


tc2 = TreeCache.TreeCache(
    sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
    cutList='V_pt>80&&V_pt<90',
    inputFolder='/scratch/p/',
    outputFolder='/scratch/p/tmp/',
    debug=True
)

isCached = tc.isCached() and tc2.isCached()
print ('is cached? ', isCached)

if not isCached:

    sampleTreeBkg = SampleTree('test/bkg.txt')

    tc.setSampleTree(sampleTreeBkg)
    tc.cache()

    tc2.setSampleTree(sampleTreeBkg)
    tc2.cache()

    sampleTreeBkg.process()

else:
    sampleTree = tc2.getTree()

    print ('from cache:', sampleTree)
    i=0
    for event in sampleTree:
        i += 1
        if i>100:
            break
        print ('V_pt:', event.V_pt)

    print ('delete cache now!')
    tc.deleteCachedFiles()
    tc2.deleteCachedFiles()
