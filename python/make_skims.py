#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo
from myutils.samplesclass import Sample
from myutils.FileLocator import FileLocator
import os,sys
import datetime

class SkimsHelper(object):

    def __init__(self, config, region, sampleIdentifier=None, opts=None):
        self.config = config
        self.region = region
        self.sampleIdentifiers = sampleIdentifier.split(',') if sampleIdentifier and len(sampleIdentifier) > 0 else None

        # VHbb namespace
        VHbbNameSpace=config.get('VHbbNameSpace','library')
        returnCode = ROOT.gSystem.Load(VHbbNameSpace)
        if returnCode != 0:
            print ("\x1b[31mERROR: loading VHbbNameSpace failed with code %d\x1b[0m"%returnCode)
        else:
            print ("INFO: loaded VHbbNameSpace: %s"%VHbbNameSpace)

        # input/output paths
        self.fileLocator = FileLocator(config=self.config)
        self.pathIN = self.config.get('Directories', opts.inputDir)
        self.pathOUT = self.config.get('Directories', opts.outputDir)
        self.tmpDir = self.config.get('Directories', 'scratch')

        self.samplesPath = config.get('Directories', 'plottingSamples')
        self.samplesInfo = ParseInfo(samples_path=self.samplesPath, config=self.config) 
        self.sampleFilesFolder = config.get('Directories', 'samplefiles')
        self.plotPath = config.get('Directories', 'plotpath')

        # plot regions
        self.configSection='Plot:%s'%region

        # additional cut to only plot a subset of the region
        self.subcut = None
        if self.config.has_option(self.configSection, 'subcut'):
            self.subcut = self.config.get(self.configSection, 'subcut')
            print("INFO: use cut:", self.subcut)

        # additional global blinding cut:
        self.addBlindingCut = None
        if self.config.has_option('Plot_general','addBlindingCut'): #contained in plots, cut on the event number
            self.addBlindingCut = self.config.get('Plot_general','addBlindingCut')
            print ('adding add. blinding cut:', self.addBlindingCut)

        # load samples
        self.data = eval(self.config.get(self.configSection, 'Datas')) # read the data corresponding to each CR (section)
        self.mc = eval(self.config.get('Plot_general', 'samples')) # read the list of mc samples
        self.total_lumi = eval(self.config.get('General', 'lumi'))
        self.signalRegion = False
        if self.config.has_option(self.configSection, 'Signal'):
            self.mc.append(self.config.get(self.configSection, 'Signal'))
            self.signalRegion = True
        self.dataSamples = self.samplesInfo.get_samples(self.data)
        self.mcSamples = self.samplesInfo.get_samples(self.mc)

        # filter samples used in the plot
        if self.sampleIdentifiers:
            self.dataSamples = [x for x in self.dataSamples if x.identifier in self.sampleIdentifiers]
            self.mcSamples =   [x for x in self.mcSamples   if x.identifier in self.sampleIdentifiers]

    def prepare(self):
        # add DATA + MC samples
        self.fileNames = []
        for sample in self.dataSamples + self.mcSamples:
            print(sample.identifier)
            
            # cuts
            sampleCuts = [sample.subcut]
            if self.config.has_option('Cuts', self.region):
                sampleCuts.append(self.config.get('Cuts', self.region))
            if self.config.has_option(self.configSection, 'Datacut'):
                sampleCuts.append(self.config.get(self.configSection, 'Datacut'))
            if self.addBlindingCut:
                sampleCuts.append(self.addBlindingCut)
            
            # get sample tree from cache
            tc = TreeCache.TreeCache(
                    sample=sample,
                    cutList=sampleCuts,
                    inputFolder=self.samplesPath,
                    config=config
                )
            if tc.isCached():
                self.fileNames += tc.findCachedFileNames()
            else:
                print("ERROR: not cached, run cacheplot again")
                raise Exception("NotCached")
        if len(self.fileNames) < 1:
            print("\x1b[31mERROR: no files found, run cacheplot!\x1b[0m")
        return self

    def run(self):
        name = self.config.get('Configuration', 'channel') if self.config.has_option('Configuration', 'channel') else '_'
        timestamp = datetime.datetime.now().strftime("%y%m%d")
        tmpName = self.tmpDir + '/skim_' + name + '_' + region + '_' + timestamp + '_tmp.root'
        destName = self.pathOUT + '/skim_' + name + '_' + region + '_' + timestamp + '.root'

        sampleTree = SampleTree(self.fileNames, config=self.config) 

        if self.config.has_option('Plot_general', 'controlSample'):
            controlSampleDict = eval(self.config.get('Plot_general', 'controlSample'))
            controlSample = controlSampleDict[self.region] if self.region in controlSampleDict else -1
            sampleTree.addOutputBranch("controlSample", lambda x: controlSample, branchType="i")
            print("INFO: setting controlSample to", controlSample)

        sampleTree.addOutputTree(tmpName, cut='1', branches='*', friend=False)
        sampleTree.process()

        # copy to final destination
        if sampleTree.getNumberOfOutputTrees() > 0:
            try:
                self.fileLocator.cp(tmpName, destName, force=True)
                print('copy ', tmpName, destName)

                if not self.fileLocator.isValidRootFile(destName):
                    print("\x1b[31mERROR: copy failed, output is broken!\x1b[0m")
                else:
                    try:
                        self.fileLocator.rm(tmpName)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print("\x1b[31mERROR: copy failed!", e, "\x1b[0m")


if __name__ == "__main__":
    # read arguments
    argv = sys.argv
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                              help="Verbose mode.")
    parser.add_option("-C", "--config", dest="config", default=[], action="append",
                          help="configuration file")
    parser.add_option("-r","--regions", dest="regions", default='',
                          help="cut region identifiers, separated by comma")
    parser.add_option("-s","--sampleIdentifier", dest="sampleIdentifier", default='',
                                      help="sample identifier (no subsample!)")
    parser.add_option("-I", "--inputDir", dest="inputDir", default="SYSin", help="name of input folder in config, e.g. SYSin")
    parser.add_option("-O", "--outputDir", dest="outputDir", default="SYSout", help="name of output folder in config, e.g. SYSout")

    (opts, args) = parser.parse_args(argv)
    if opts.config == "":
            opts.config = ["config"]

    # Import after configure to get help message
    from myutils import BetterConfigParser, mvainfo, ParseInfo

    # load config
    config = BetterConfigParser()
    config.read(opts.config)

    # run plotter
    regions = opts.regions.split(',')
    for region in regions:
        plotter = SkimsHelper(config=config, region=region, sampleIdentifier=opts.sampleIdentifier, opts=opts)
        plotter.prepare()
        plotter.run()

