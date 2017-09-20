#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo

import os,sys

class CacheTraining(object):

    def __init__(self, config, sampleIdentifier, trainingRegions, cacheParts=1, cachePart=1, splitFiles=-1):
        self.config = config
        self.sampleIdentifier = sampleIdentifier
        self.trainingRegions = trainingRegions

        self.sampleTree = None
        self.samplesPath = self.config.get('Directories', 'MVAin')
        self.samplesDefinitions = self.config.get('Directories','samplesinfo') 
        self.samplesInfo = ParseInfo(self.samplesDefinitions, self.samplesPath)

        self.cachedPath = self.config.get('Directories', 'tmpSamples')
        self.tmpPath = self.config.get('Directories', 'scratch')
        self.sampleFilesFolder = self.config.get('Directories', 'samplefiles')

        self.backgroundSampleNames = list(set(sum([eval(self.config.get(trainingRegion, 'backgrounds')) for trainingRegion in self.trainingRegions], [])))
        self.signalSampleNames = list(set(sum([eval(self.config.get(trainingRegion, 'signals')) for trainingRegion in self.trainingRegions], [])))
        self.samples = self.samplesInfo.get_samples(self.backgroundSampleNames + self.signalSampleNames)

        self.trainingRegionsDict = {}
        for trainingRegion in self.trainingRegions:
            treeCutName = config.get(trainingRegion, 'treeCut')
            treeCut = config.get('Cuts', treeCutName)
            self.trainingRegionsDict[trainingRegion] = {'cut': treeCut}

        self.TrainCut = config.get('Cuts', 'TrainCut') 
        self.EvalCut = config.get('Cuts', 'EvalCut')

        self.cacheParts = cacheParts
        self.cachePart = cachePart
        self.splitFiles = splitFiles
    
    def printInfo(self):
        print ("REGION:".ljust(24),"CUT:")
        for trainingRegion,trainingRegionInfo in self.trainingRegionsDict.iteritems():
            print (" > ",trainingRegion.ljust(20), trainingRegionInfo['cut'])

    def run(self):
        # ----------------------------------------------------------------------------------------------------------------------
        # cache samples
        # ----------------------------------------------------------------------------------------------------------------------
        # for this test run caching for all samples sequentially
        for sampleToCache in [self.sampleIdentifier]:
            print ('*'*80)
            print (' ',sampleToCache)
            print ('*'*80)
            # prepare caches for training and evaluation samples
            treeCaches = []
            sampleTree = None

            # for all (sub)samples which come from the same files (sampleIdentifier)
            subsamples = [x for x in self.samples if x.identifier == sampleToCache]
            for sample in subsamples:

                # add cuts for all training regions
                for trainingRegion,trainingRegionInfo in self.trainingRegionsDict.iteritems():

                    # add cuts for training and evaluation
                    for additionalCut in [self.TrainCut, self.EvalCut]:

                        # cuts
                        sampleCuts = [sample.subcut]
                        if additionalCut:
                            sampleCuts.append(additionalCut)
                        if trainingRegionInfo['cut']:
                            sampleCuts.append(trainingRegionInfo['cut'])
                        cutList = '&&'.join(['(%s)'%x for x in sorted(sampleCuts)])

                        # add cache object
                        tc = TreeCache.TreeCache(
                            sample=sample.name,
                            cutList=cutList,
                            inputFolder=self.samplesPath,
                            tmpFolder=self.tmpPath,
                            outputFolder=self.cachedPath,
                            cacheParts=self.cacheParts,
                            cachePart=self.cachePart,
                            splitFiles=self.splitFiles,
                            debug=True
                        )

                        # check if this part of the sample is already cached
                        if not tc.partIsCached():
                            # for the first sample which comes from this files, load the tree
                            if not self.sampleTree:
                                self.sampleTree = SampleTree({'name': sample.identifier, 'folder': self.samplesPath}, splitFiles=self.splitFiles, splitFilesPart=self.cachePart)
                            treeCaches.append(tc.setSampleTree(self.sampleTree).cache())

            if len(treeCaches) > 0:
                # run on the tree
                self.sampleTree.process()
            else:
                print ("noting to do!")

# read arguments
argv = sys.argv
parser = OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                          help="Verbose mode.")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration file")
parser.add_option("-t","--trainingRegions", dest="trainingRegions", default='',
                      help="cut region identifier")
parser.add_option("-s","--sampleIdentifier", dest="sampleIdentifier", default='',
                      help="sample identifier (no subsample!)")
parser.add_option("-n","--cacheParts", dest="cacheParts", default='',
                      help="number of parts")
parser.add_option("-i","--cachePart", dest="cachePart", default='',
                      help="number of part to cache")
parser.add_option("-p","--splitFiles", dest="splitFiles", default='',
                      help="number of files per part")
(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = "config"

# Import after configure to get help message
from myutils import BetterConfigParser, mvainfo, ParseInfo

# load config
config = BetterConfigParser()
config.read(opts.config)

# initialize
trainingRegions = opts.trainingRegions.split(',')
cacheParts = int(opts.cacheParts) if len(opts.cacheParts) > 0 else 1
cachePart = int(opts.cachePart) if len(opts.cachePart) > 0 else 1
splitFiles = int(opts.splitFiles) if len(opts.splitFiles) > 0 else -1
ct = CacheTraining(config=config, sampleIdentifier=opts.sampleIdentifier, trainingRegions=trainingRegions, cachePart=cachePart, cacheParts=cacheParts, splitFiles=splitFiles)
ct.printInfo()

# run training
ct.run()
