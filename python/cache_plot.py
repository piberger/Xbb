#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo

import os,sys

class CachePlot(object):

    def __init__(self, config, sampleIdentifier, regions, cacheParts=1, cachePart=1, splitFiles=-1, forceRedo=False):
        self.config = config
        self.sampleIdentifier = sampleIdentifier
        self.regions = list(set(regions))
        self.forceRedo = forceRedo

        self.sampleTree = None
        self.samplesPath = self.config.get('Directories', 'plottingSamples')
        self.samplesDefinitions = self.config.get('Directories','samplesinfo') 
        self.samplesInfo = ParseInfo(self.samplesDefinitions, self.samplesPath)

        self.cachedPath = self.config.get('Directories', 'tmpSamples')
        self.tmpPath = self.config.get('Directories', 'scratch')
        self.sampleFilesFolder = self.config.get('Directories', 'samplefiles')

        self.sampleNames = eval(self.config.get('Plot_general', 'samples'))
        self.dataNames = eval(self.config.get('Plot_general', 'Data'))
        self.samples = self.samplesInfo.get_samples(self.sampleNames + self.dataNames)

        self.regionsDict = {}
        for region in self.regions:
            treeCut = config.get('Cuts', region)
            self.regionsDict[region] = {'cut': treeCut}
        self.cacheParts = cacheParts
        self.cachePart = cachePart
        self.splitFiles = splitFiles
    
        VHbbNameSpace=config.get('VHbbNameSpace','library')
        returnCode = ROOT.gSystem.Load(VHbbNameSpace)
        if returnCode != 0:
            print ("\x1b[31mERROR: loading VHbbNameSpace failed with code %d\x1b[0m"%returnCode)
        else:
            print ("INFO: loaded VHbbNameSpace: %s"%VHbbNameSpace)

    def printInfo(self):
        print ("REGION:".ljust(24),"CUT:")
        for region,regionInfo in self.regionsDict.iteritems():
            print (" > ",region.ljust(20), regionInfo['cut'])

    def run(self):

        # ----------------------------------------------------------------------------------------------------------------------
        # cache samples
        # ----------------------------------------------------------------------------------------------------------------------
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
                for region,regionInfo in self.regionsDict.iteritems():

                    configSection = 'Plot:%s'%region
                    
                    # cuts
                    sampleCuts = [sample.subcut]
                    if regionInfo['cut']:
                        sampleCuts.append(regionInfo['cut'])
                    if self.config.has_option(configSection, 'Datacut'):
                        sampleCuts.append(self.config.get(configSection, 'Datacut'))
                    if self.config.has_option('Plot_general','addBlindingCut'):
                        sampleCuts.append(self.config.has_option('Plot_general','addBlindingCut'))

                    # add cache object
                    tc = TreeCache.TreeCache(
                        sample=sample.name,
                        cutList=sampleCuts,
                        inputFolder=self.samplesPath,
                        tmpFolder=self.tmpPath,
                        outputFolder=self.cachedPath,
                        cacheParts=self.cacheParts,
                        cachePart=self.cachePart,
                        splitFiles=self.splitFiles,
                        debug=True
                    )

                    # check if this part of the sample is already cached
                    isCached = tc.partIsCached()
                    if not isCached or self.forceRedo:
                        if isCached:
                            tc.deleteCachedFiles()

                        # for the first sample which comes from this files, load the tree
                        if not self.sampleTree:
                            self.sampleTree = SampleTree({'name': sample.identifier, 'folder': self.samplesPath}, splitFiles=self.splitFiles, splitFilesPart=self.cachePart)
                            if not self.sampleTree or not self.sampleTree.tree:
                                print ("\x1b[31mERROR: creation of sample tree failed!!\x1b[0m")
                                raise Exception("CreationOfSampleTreeFailed!")
                        treeCaches.append(tc.setSampleTree(self.sampleTree).cache())
                    else:
                        print ("INFO: already cached!",tc, "(",tc.hash,")")

            if len(treeCaches) > 0:
                # run on the tree
                self.sampleTree.process()
            else:
                print ("nothing to do!")

if __name__ == "__main__":
    # read arguments
    argv = sys.argv
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                              help="Verbose mode.")
    parser.add_option("-C", "--config", dest="config", default=[], action="append",
                          help="configuration file")
    parser.add_option("-t","--regions", dest="regions", default='',
                          help="cut regions identifier")
    parser.add_option("-s","--sampleIdentifier", dest="sampleIdentifier", default='',
                          help="sample identifier (no subsample!)")
    parser.add_option("-n","--cacheParts", dest="cacheParts", default='',
                          help="number of parts")
    parser.add_option("-i","--cachePart", dest="cachePart", default='',
                          help="number of part to cache")
    parser.add_option("-p","--splitFiles", dest="splitFiles", default='',
                          help="number of files per part")
    parser.add_option("-f","--force", action="store_true", dest="force", default=False,
                          help="force overwriting of already cached files")
    (opts, args) = parser.parse_args(argv)
    if opts.config =="":
            opts.config = "config"

    # Import after configure to get help message
    from myutils import BetterConfigParser, mvainfo, ParseInfo

    # load config
    config = BetterConfigParser()
    config.read(opts.config)

    # initialize
    regions = opts.regions.split(',')
    cacheParts = int(opts.cacheParts) if len(opts.cacheParts) > 0 else 1
    cachePart = int(opts.cachePart) if len(opts.cachePart) > 0 else 1
    splitFiles = int(opts.splitFiles) if len(opts.splitFiles) > 0 else -1
    ct = CachePlot(config=config, sampleIdentifier=opts.sampleIdentifier, regions=regions, cachePart=cachePart, cacheParts=cacheParts, splitFiles=splitFiles, forceRedo=opts.force)
    ct.printInfo()

    # run training
    ct.run()

