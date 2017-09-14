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

user='berger_p2'
tc = TreeCache.TreeCache(
    sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
    cutList='V_pt>100',
    inputFolder='/scratch/' + user + '/',
    tmpFolder='/scratch/' + user + '/tmp/',
    outputFolder='/scratch/' + user + '/cache/',
    debug=True
)

# another cut
tc2 = TreeCache.TreeCache(
    sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
    cutList='V_pt>80&&V_pt<90',
    inputFolder='/scratch/' + user + '/',
    tmpFolder='/scratch/' + user + '/tmp/',
    outputFolder='/scratch/' + user + '/cache/',
    debug=True
)

# same cut, only cache specific branches to reduce file size
tc3 = TreeCache.TreeCache(
    sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
    cutList='V_pt>80&&V_pt<90',
    inputFolder='/scratch/' + user + '/',
    tmpFolder='/scratch/' + user + '/tmp/',
    outputFolder='/scratch/' + user + '/cache/',
    branches=['V_pt', 'Vtype', 'Vtype_new'],
    debug=True
)

isCached = tc.isCached() and tc2.isCached()
print ('is cached? ', isCached)

isCachedAndValid = tc.isCachedAndValid() and tc2.isCachedAndValid()
print ('is cached and valid? ', isCachedAndValid)

allCaches = [tc, tc2, tc3]

if not isCachedAndValid:

    sampleTreeBkg = SampleTree('test/bkg.txt')

    for cache in allCaches:
        cache.setSampleTree(sampleTreeBkg)
        cache.cache()

    sampleTreeBkg.process()

    for cache in allCaches:
        cache.moveFilesToFinalLocation()

else:
    sampleTree = tc2.getTree()

    print ('from cache:', sampleTree)
    i=0
    for event in sampleTree:
        i += 1
        if i>100:
            break
        print ('V_pt:', event.V_pt)

    # for testing purpose
    print ('delete cache now!')
    for cache in allCaches:
        cache.deleteCachedFiles()
