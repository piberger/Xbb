#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo

import os,sys

class MvaTrainingHelper(object):

    def __init__(self, config, mvaName):
        self.factoryname = config.get('factory', 'factoryname')
        self.factorysettings = config.get('factory', 'factorysettings')
        self.samplesPath = config.get('Directories', 'MVAin')
        self.samplesDefinitions = config.get('Directories','samplesinfo') 
        self.samplesInfo = ParseInfo(self.samplesDefinitions, self.samplesPath)

        self.sampleFilesFolder = config.get('Directories', 'samplefiles')

        self.treeVarSet = config.get(mvaName, 'treeVarSet')
        self.MVAtype = config.get(mvaName, 'MVAtype')
        self.MVAsettings = config.get(mvaName,'MVAsettings')
        self.mvaName = mvaName

        VHbbNameSpace = config.get('VHbbNameSpace', 'library')
        ROOT.gSystem.Load(VHbbNameSpace)

        # variables
        self.MVA_Vars = {}
        self.MVA_Vars['Nominal'] = config.get(self.treeVarSet, 'Nominal').strip().split(' ')

        # samples
        backgroundSampleNames = eval(config.get(mvaName, 'backgrounds'))
        signalSampleNames = eval(config.get(mvaName, 'signals'))
        self.samples = {
            'BKG': self.samplesInfo.get_samples(backgroundSampleNames),
            'SIG': self.samplesInfo.get_samples(signalSampleNames),
        }

        self.cachedPath = config.get('Directories', 'tmpSamples')
        self.tmpPath = config.get('Directories', 'scratch')

        self.treeCutName = config.get(mvaName, 'treeCut')
        self.treeCut = config.get('Cuts', self.treeCutName)

        self.TrainCut = config.get('Cuts', 'TrainCut') 
        self.EvalCut = config.get('Cuts', 'EvalCut')

        self.globalRescale = 2.0
        
        self.trainingOutputFileName = 'mvatraining_{factoryname}_{region}.root'.format(factoryname=self.factoryname, region=mvaName)
        self.trainingOutputFile = ROOT.TFile.Open(self.trainingOutputFileName, "RECREATE")

        # ----------------------------------------------------------------------------------------------------------------------
        # create TMVA factory
        # ----------------------------------------------------------------------------------------------------------------------
        self.factory = ROOT.TMVA.Factory(self.factoryname, self.trainingOutputFile, self.factorysettings)
        if self.trainingOutputFile and self.factory:
            print ("INFO: initialized MvaTrainingHelper.") 
        else:
            print ("\x1b[31mERROR: initialization of MvaTrainingHelper failed!\x1b[0m") 


    def prepare(self):
        # ----------------------------------------------------------------------------------------------------------------------
        # add sig/bkg x training/eval trees
        # ----------------------------------------------------------------------------------------------------------------------
        for addTreeFcn, samples in [
                    [self.factory.AddBackgroundTree, self.samples['BKG']],
                    [self.factory.AddSignalTree, self.samples['SIG']]
                ]:
            for sample in samples:
                print ('*'*80,'\n%s\n'%sample,'*'*80)
                for additionalCut in [self.TrainCut, self.EvalCut]:
                    # cuts
                    sampleCuts = [sample.subcut]
                    if additionalCut:
                        sampleCuts.append(additionalCut)
                    # cut from the mva region
                    if self.treeCut:
                        sampleCuts.append(self.treeCut)
                    cutList = '&&'.join(['(%s)'%x for x in sorted(sampleCuts)])

                    # count number of chunks the cached data is split into
                    splitFiles = sample.mergeCachingSize 
                    nParts = SampleTree({'name': sample.identifier, 'folder': self.samplesPath}, countOnly=True, splitFiles=splitFiles).getNumberOfParts()
                    
                    tc = TreeCache.TreeCache(
                            sample=sample.name,
                            cutList=cutList,
                            inputFolder=self.samplesPath,
                            tmpFolder=self.tmpPath,
                            outputFolder=self.cachedPath,
                            cacheParts=nParts,
                            splitFiles=splitFiles,
                            debug=True
                        )
                    sampleTree = tc.getTree()
                    if sampleTree:
                        treeScale = sampleTree.getScale(sample) * self.globalRescale
                        if sampleTree.tree.GetEntries() > 0:
                            addTreeFcn(sampleTree.tree, treeScale, ROOT.TMVA.Types.kTraining if additionalCut == self.TrainCut else ROOT.TMVA.Types.kTesting)
                    else:
                        print ("\x1b[31mERROR: TREE NOT FOUND:", sample.name, " -> not cached??\x1b[0m")
                        raise Exception("CachedTreeMissing")

        for var in self.MVA_Vars['Nominal']:
            self.factory.AddVariable(var, 'D')

        return self

    def run(self):
        # ----------------------------------------------------------------------------------------------------------------------
        # Execute TMVA
        # ----------------------------------------------------------------------------------------------------------------------
        self.factory.Verbose()
        print ('Execute TMVA: factory.BookMethod("%s", "%s", "%s")'%(self.MVAtype, self.mvaName, self.MVAsettings))
        self.factory.BookMethod(self.MVAtype, self.mvaName, self.MVAsettings)
        print ('Execute TMVA: TrainAllMethods')
        self.factory.TrainAllMethods()
        print ('Execute TMVA: TestAllMethods')
        self.factory.TestAllMethods()
        print ('Execute TMVA: EvaluateAllMethods')
        self.factory.EvaluateAllMethods()
        print ('Execute TMVA: output.Write')
        self.trainingOutputFile.Close()

# read arguments
argv = sys.argv
parser = OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                          help="Verbose mode.")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration file")
parser.add_option("-t","--trainingRegions", dest="trainingRegions", default='',
                      help="cut region identifier")
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
if len(trainingRegions) > 1:
    print ("ERROR: not implemented!")
    exit(1)
for trainingRegion in trainingRegions:
    th = MvaTrainingHelper(config=config, mvaName=trainingRegion)
    th.prepare().run()

