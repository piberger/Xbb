#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils import BetterConfigParser, ParseInfo

import os

if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

# ----------------------------------------------------------------------------------------------------------------------
# configuration
# ----------------------------------------------------------------------------------------------------------------------
testConfiguration = 'TestZll2016config/'
mvaName = 'ZllBDTVV_highpt'
backgroundSampleNames = ['HT100to200ZJets_udscg_ext1', 'HT100to200ZJets_1b_ext1', 'HT100to200ZJets_2b_ext1']
signalSampleNames = ['ZH_HToBB_ZToLL_M125_pow_ext1']
TrainCut = '!((evt%2)==0||isData)'
EvalCut = '((evt%2)==0||isData)'

# ----------------------------------------------------------------------------------------------------------------------
# output file
# ----------------------------------------------------------------------------------------------------------------------
trainingOutputFile = ROOT.TFile.Open('test_training.root', "RECREATE")

# ----------------------------------------------------------------------------------------------------------------------
# load config
# ----------------------------------------------------------------------------------------------------------------------
config = BetterConfigParser()
config.read(testConfiguration + '/paths.ini')
config.read(testConfiguration + '/general.ini')
config.read(testConfiguration + '/samples_nosplit.ini')
config.read(testConfiguration + '/training.ini')

factoryname = config.get('factory', 'factoryname')
factorysettings = config.get('factory', 'factorysettings')
samplesPath = config.get('Directories', 'MVAin')
samplesinfo = testConfiguration + '/samples_nosplit.ini'
info = ParseInfo(samplesinfo, samplesPath)

sampleFilesFolder = config.get('Directories', 'samplefiles')

treeVarSet = config.get(mvaName, 'treeVarSet')
MVAtype = config.get(mvaName, 'MVAtype')
MVAsettings=config.get(mvaName,'MVAsettings')

VHbbNameSpace = config.get('VHbbNameSpace', 'library')
ROOT.gSystem.Load(VHbbNameSpace)

# variables
MVA_Vars = {}
MVA_Vars['Nominal'] = config.get(treeVarSet, 'Nominal')
MVA_Vars['Nominal'] = MVA_Vars['Nominal'].split(' ')

samples = {
    'BKG': info.get_samples(backgroundSampleNames),
    'SIG': info.get_samples(signalSampleNames),
}

cachedPath = config.get('Directories', 'tmpSamples')
tmpPath = config.get('Directories', 'scratch')

globalRescale = 2.0

# ----------------------------------------------------------------------------------------------------------------------
# create TMVA factory
# ----------------------------------------------------------------------------------------------------------------------
factory = ROOT.TMVA.Factory(factoryname, trainingOutputFile, factorysettings)

# ----------------------------------------------------------------------------------------------------------------------
# add sig/bkg x training/eval trees
# ----------------------------------------------------------------------------------------------------------------------
for addTreeFcn, samples in [
            [factory.AddBackgroundTree, samples['BKG']],
            [factory.AddSignalTree, samples['SIG']]
        ]:
    for sample in samples:
        for additionalCut in [TrainCut, EvalCut]:
            tc = TreeCache.TreeCache(
                    sample=sample.name,
                    cutList=('(%s)&&(%s)'%(sample.subcut, additionalCut)) if additionalCut else sample.subcut,
                    inputFolder=samplesPath,
                    tmpFolder=tmpPath,
                    outputFolder=cachedPath,
                    debug=True
                )
            sampleTree = tc.getTree()
            treeScale = sampleTree.getScale(sample) * globalRescale
            addTreeFcn(sampleTree.tree, treeScale, ROOT.TMVA.Types.kTraining if additionalCut == TrainCut else ROOT.TMVA.Types.kTesting)

for var in MVA_Vars['Nominal']:
    factory.AddVariable(var, 'D')

# ----------------------------------------------------------------------------------------------------------------------
# Execute TMVA
# ----------------------------------------------------------------------------------------------------------------------
factory.Verbose()
print 'Execute TMVA: factory.BookMethod("%s", "%s", "%s")'%(MVAtype, mvaName, MVAsettings)
factory.BookMethod(MVAtype, mvaName, MVAsettings)
print 'Execute TMVA: TrainAllMethods'
factory.TrainAllMethods()
print 'Execute TMVA: TestAllMethods'
factory.TestAllMethods()
print 'Execute TMVA: EvaluateAllMethods'
factory.EvaluateAllMethods()
print 'Execute TMVA: output.Write'
trainingOutputFile.Close()
