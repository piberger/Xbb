#!/usr/bin/env python
import ROOT
import sys
ROOT.gROOT.SetBatch(True)
from myutils import BetterConfigParser, ParseInfo
import glob
from multiprocessing import Process
from myutils.sampleTree import SampleTree as SampleTree
import argparse
import itertools
from myutils.BranchList import BranchList

parser = argparse.ArgumentParser(description='getExtWeightsNew: compute stitching coefficients for samples with overlap')
parser.add_argument('--samples', dest='samples', help='list of sample identifiers')
parser.add_argument('--cuts', dest='cuts', help='cuts', default='')
parser.add_argument('--from', dest='fromFolder', help='folder name to use, e.g. PREPout', default='PREPout')
parser.add_argument('--fc', dest='fc', help='fc', default='')
parser.add_argument('--prune', dest='prune', help='remove contributions with fraction lower than this', default='0.0')
parser.add_argument('-T', dest='tag', help='config tag')
args = parser.parse_args()

# 1) ./getExtWeights.py configname
# 2) ./getExtWeight.py configname verify

def getEventCount(config, sampleIdentifier, cut="1", sampleTree=None):
    if not sampleTree:
        sampleTree = SampleTree({'name': sampleIdentifier, 'folder': config.get('Directories',args.fromFolder).strip()}, config=config)
    h1 = ROOT.TH1D("h1","h1",1,0,2)
    nEvents = sampleTree.tree.Draw("1>>h1", "(" + cut + ")*genWeight")
    nEventsWeighted = h1.GetBinContent(1)
    h1.Delete()
    return nEventsWeighted


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

pruneThreshold = float(args.prune)

sampleGroups = []
for x in args.samples.split(','):
    sampleGroups.append(x.split('+'))

sampleCuts = args.cuts.strip().split(',')
if args.fc != '':
    cutGroups = [x.strip(',').split(',') for x in args.fc.strip(';').split(';')]
    # cartesian product
    sampleCuts = list(set(['&&'.join(x) for x in itertools.product(*cutGroups)]))
    print sampleCuts
    print "=> len=",len(sampleCuts)

countDict = {}
for sampleGroup in sampleGroups:
    count = 0
    for sample in sampleGroup:
        countDict[sample] = {}

        sampleTree = SampleTree({'name': sample, 'folder': config.get('Directories',args.fromFolder).strip()}, config=config)
        print "CUT=",sampleCuts,":"
        for sampleCut in sampleCuts:
            sampleCount = getEventCount(config, sample, sampleCut, sampleTree=sampleTree)
            print sample,sampleCut,"\x1b[34m=>",sampleCount,"\x1b[0m"
            if sampleCut in countDict[sample]:
                print "duplicate!!", sample, sampleCut, countDict[sample][sampleCut]
                raise Exception("duplicate")
            countDict[sample][sampleCut] = sampleCount

# pruning
for sampleIdentifier,counts in countDict.iteritems():
    specialweight = ''
    for cut,cutCount in counts.iteritems():
        totalCount = 0
        for sample,sampleCounts in countDict.iteritems():
            totalCount += sampleCounts[cut]

        if cutCount>0 and totalCount>0:
            fraction = 1.0*cutCount/totalCount
            if fraction < pruneThreshold:
                print "\x1b[31mfor "+sampleIdentifier + " set count("+cut+") from %d"%counts[cut] + " to 0\x1b[0m"
                counts[cut] = 0

print "result:"
print countDict
print "-"*80

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

print "-"*80

