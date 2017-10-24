#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo
from myutils.NewStackMaker import NewStackMaker as StackMaker
from myutils.samplesclass import Sample
import os,sys

class PlotHelper(object):

    def __init__(self, config, region, vars = None):
        self.config = config
        self.region = region
        self.vars = vars

        # additional blinding cut:
        self.addBlindingCut = None
        if self.config.has_option('Plot_general','addBlindingCut'): #contained in plots, cut on the event number
            self.addBlindingCut = self.config.get('Plot_general','addBlindingCut')
            print ('adding add. blinding cut:', self.addBlindingCut)

        self.samplesPath = config.get('Directories', 'plottingSamples')
        self.samplesDefinitions = config.get('Directories','samplesinfo') 
        self.samplesInfo = ParseInfo(self.samplesDefinitions, self.samplesPath)
        self.sampleFilesFolder = config.get('Directories', 'samplefiles')

        self.cachedPath = config.get('Directories', 'tmpSamples')
        self.tmpPath = config.get('Directories', 'scratch')
        self.plotPath = config.get('Directories', 'plotpath')

        # plot regions
        self.configSection='Plot:%s'%region
        if self.vars and type(self.vars) == list:
            self.vars = [x.strip() for x in self.vars if len(x.strip()) > 0] 
        
        if not self.vars or len(self.vars) < 1:
            varListFromConfig = self.config.get(self.configSection, 'vars').split(',')
            print ("VARS::", self.configSection, " => ", varListFromConfig)
            self.vars = [x.strip() for x in varListFromConfig if len(x.strip()) > 0]

        # load samples
        self.data = eval(self.config.get(self.configSection, 'Datas')) # read the data corresponding to each CR (section)
        self.mc = eval(self.config.get('Plot_general', 'samples')) # read the list of mc samples
        self.total_lumi = eval(self.config.get('Plot_general', 'lumi'))
        self.signalRegion = False
        if self.config.has_option(self.configSection, 'Signal'):
            self.mc.append(self.config.get(self.configSection, 'Signal'))
            self.signalRegion = True
        self.dataSamples = self.samplesInfo.get_samples(self.data)
        self.mcSamples = self.samplesInfo.get_samples(self.mc)

        self.groupDict = eval(self.config.get('Plot_general', 'Group'))
        self.subcutPlotName = ''
        self.histogramStacks = {}


    def prepare(self):

        print ("INFO: starting plot for region \x1b[34m{region}\x1b[0m, variables:".format(region=region))
        for var in self.vars:
            print ("  > {var}".format(var=var))

        self.histogramStacks = {}
        for var in self.vars:
            self.histogramStacks[var] = StackMaker(self.config, var, self.region, self.signalRegion, None, '_'+self.subcutPlotName)
        
        # add DATA + MC samples
        for sample in self.dataSamples + self.mcSamples:
            
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
                    tmpFolder=self.tmpPath,
                    outputFolder=self.cachedPath,
                    debug=True
                )
            sampleTree = tc.getTree()

            if sampleTree:
                groupName = self.groupDict[sample.name]  
                print (" > found the tree, #entries = ", sampleTree.tree.GetEntries())
                print ("   > group =", groupName)
                print (" > now adding the tree for vars=", self.vars)
                
                # add the sample tree for all the variables
                for var in self.vars:
                    self.histogramStacks[var].addSampleTree(sample=sample, sampleTree=sampleTree, groupName=groupName)
            else:
                print ("\x1b[31mERROR: sampleTree not available for ", sample,", run caching again!!\x1b[0m")
                raise Exception("CachedTreeMissing")
        return self

    def run(self):
        # draw
        for var in self.vars:
            outputFolder = self.plotPath + 'plot_{region}_{var}'.format(region=self.region, var=var)
            self.histogramStacks[var].Draw(outputFolder=outputFolder)

        return self

    def getHistogramStack(self, var):
        if var in self.vars and var in self.histogramStacks:
            return self.histogramStacks[var]
        else:
            return None

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
    parser.add_option("-p","--vars", dest="vars", default='',
                          help="plot variables, separated by comma")
    (opts, args) = parser.parse_args(argv)
    if opts.config == "":
            opts.config = ["config"]

    # Import after configure to get help message
    from myutils import BetterConfigParser, mvainfo, ParseInfo

    # load config
    config = BetterConfigParser()
    vhbbPlotDef = opts.config[0].split('/')[0]+'/vhbbPlotDef.ini'
    opts.config.append(vhbbPlotDef)
    config.read(opts.config)

    # run plotter
    regions = opts.regions.split(',')
    vars = opts.vars.split(',')
    for region in regions:
        plotter = PlotHelper(config=config, region=region, vars=vars)
        plotter.prepare()
        plotter.run()

