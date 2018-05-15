#!/usr/bin/env python
import ROOT
import sys
ROOT.gROOT.SetBatch(True)
from myutils import BetterConfigParser, ParseInfo
import glob
from multiprocessing import Process
from myutils.sampleTree import SampleTree as SampleTree
import argparse
from myutils.BranchList import BranchList

parser = argparse.ArgumentParser(description='getExtWeightsNew: compute stitching coefficients for samples with overlap')
parser.add_argument('--samples', dest='samples', help='list of sample identifiers')
parser.add_argument('--cuts', dest='cuts', help='cuts')
parser.add_argument('-T', dest='tag', help='config tag')
args = parser.parse_args()

# 1) ./getExtWeights.py configname
# 2) ./getExtWeight.py configname verify

def getEventCount(config, sampleIdentifier, cut="1"):
    sampleTree = SampleTree({'name': sampleIdentifier, 'folder': config.get('Directories','PREPout').strip()}, config=config)
    nEvents = sampleTree.tree.Draw("1", cut, "goff")
    print sampleIdentifier," =>",nEvents
    return nEvents


# load config
config = BetterConfigParser()
configFolder = args.tag + 'config/'
print "config folder:", configFolder
config.read(configFolder + '/paths.ini')
configFiles = [x for x in config.get('Configuration','List').strip().split(' ') if len(x.strip()) > 0]
config = BetterConfigParser()
for configFile in configFiles:
    config.read(configFolder + configFile)
    print "read config ", configFile

sampleGroups = []
for x in args.samples.split(','):
    sampleGroups.append(x.split('+'))

sampleCuts = args.cuts.strip().split(',')

countDict = {}
for sampleGroup in sampleGroups:
    for sampleIdentifier in sampleGroup:
        countDict[sampleIdentifier] = {}
        for sampleCut in sampleCuts:
            countDict[sampleIdentifier][sampleCut] = -1

for sampleCut in sampleCuts:
    print "CUT=",sampleCuts,":"
    for sampleGroup in sampleGroups:
        count = 0
        for sample in sampleGroup:
            sampleCount = getEventCount(config, sample, sampleCut)
            print sample,sampleCut,"\x1b[34m=>",sampleCount,"\x1b[0m"
            count += sampleCount
        for sample in sampleGroup:
            countDict[sample][sampleCut] = count

print countDict

for sampleIdentifier,counts in countDict.iteritems():
    specialweight = ''
    for cut,cutCount in counts.iteritems():
        totalCount = 0
        for sample,sampleCounts in countDict.iteritems():
            totalCount += sampleCounts[cut]

        if cutCount>0:
            if cutCount==totalCount:
                if len(specialweight) > 0:
                    specialweight += ' + '
                specialweight += '(' + cut + ')'
            else:
                if len(specialweight) > 0:
                    specialweight += ' + '
                specialweight += '(' + cut + ')*%1.5f'%(1.0*cutCount/totalCount)
    print sampleIdentifier, specialweight


