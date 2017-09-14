#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, mvainfo, ParseInfo

import os

user = os.popen('whoami').read().strip('\n').strip('\r')
testConfiguration = 'TestZll2016config/'

if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

#load config
config = BetterConfigParser()
config.read(testConfiguration + '/paths.ini')
config.read(testConfiguration + '/general.ini')
config.read(testConfiguration + '/samples_nosplit.ini')
config.read(testConfiguration + '/training.ini')


factoryname = config.get('factory', 'factoryname')
trainingOutputFile = ROOT.TFile.Open('test_training.root', "RECREATE")
factorysettings = config.get('factory', 'factorysettings')

samplesPath = '/scratch/{user}/'.format(user=user)
samplesinfo = testConfiguration + '/samples_nosplit.ini'
info = ParseInfo(samplesinfo, samplesPath)

sampleFilesFolder = config.get('Directories', 'samplefiles')

mvaName = 'ZllBDTVV_highpt'
treeVarSet = config.get(mvaName, 'treeVarSet')
MVAtype = config.get(mvaName, 'MVAtype')

VHbbNameSpace = config.get('VHbbNameSpace', 'library')
ROOT.gSystem.Load(VHbbNameSpace)

# variables
# TreeVar Array
MVA_Vars = {}
MVA_Vars['Nominal'] = config.get(treeVarSet, 'Nominal')
MVA_Vars['Nominal'] = MVA_Vars['Nominal'].split(' ')

factory = ROOT.TMVA.Factory(factoryname, trainingOutputFile, factorysettings)

samples = {}
samples['BKG'] = info.get_samples(['HT100to200ZJets_udscg_ext1', 'HT100to200ZJets_1b_ext1', 'HT100to200ZJets_2b_ext1'])
samples['SIG'] = info.get_samples(['ZH_HToBB_ZToLL_M125_pow_ext1'])


TrainCut = '!((evt%2)==0||isData)'
EvalCut = '((evt%2)==0||isData)'

for sample in samples['BKG']:
    print sample.name, "\x1b[31m", sample.subcut, "\x1b[0m"
    print " =>", sample.identifier

    # training tree
    tc = TreeCache.TreeCache(
            sample=sample.name,
            cutList=('(%s)&&(%s)'%(sample.subcut, TrainCut)) if TrainCut else sample.subcut,
            inputFolder='/scratch/' + user + '/',
            tmpFolder='/scratch/' + user + '/tmp/',
            outputFolder='/scratch/' + user + '/cache/',
            debug=True
        )
    factory.AddBackgroundTree(tc.getTree().tree, 1.0, ROOT.TMVA.Types.kTraining)

    # training tree
    tc = TreeCache.TreeCache(
        sample=sample.name,
        cutList=('(%s)&&(%s)' % (sample.subcut, EvalCut)) if EvalCut else sample.subcut,
        inputFolder='/scratch/' + user + '/',
        tmpFolder='/scratch/' + user + '/tmp/',
        outputFolder='/scratch/' + user + '/cache/',
        debug=True
    )
    factory.AddBackgroundTree(tc.getTree().tree, 1.0, ROOT.TMVA.Types.kTesting)


for sample in samples['SIG']:
    print sample.name, "\x1b[31m", sample.subcut, "\x1b[0m"
    print " SIGNAL =>", sample.identifier

    # training tree
    tc = TreeCache.TreeCache(
            sample=sample.name,
            cutList=('(%s)&&(%s)'%(sample.subcut, TrainCut)) if TrainCut else sample.subcut,
            inputFolder='/scratch/' + user + '/',
            tmpFolder='/scratch/' + user + '/tmp/',
            outputFolder='/scratch/' + user + '/cache/',
            debug=True
        )
    factory.AddSignalTree(tc.getTree().tree, 1.0, ROOT.TMVA.Types.kTraining)

    # training tree
    tc = TreeCache.TreeCache(
        sample=sample.name,
        cutList=('(%s)&&(%s)' % (sample.subcut, EvalCut)) if EvalCut else sample.subcut,
        inputFolder='/scratch/' + user + '/',
        tmpFolder='/scratch/' + user + '/tmp/',
        outputFolder='/scratch/' + user + '/cache/',
        debug=True
    )
    factory.AddSignalTree(tc.getTree().tree, 1.0, ROOT.TMVA.Types.kTesting)

# print 'add the variables'
for var in MVA_Vars['Nominal']:
    factory.AddVariable(var,'D') # add the variables


#Execute TMVA
factory.Verbose()
print 'Execute TMVA: factory.BookMethod(%s, %s)'%(MVAtype, mvaName)
factory.BookMethod(MVAtype, mvaName, '')
print 'Execute TMVA: TrainMethod'
#my_methodBase_bdt.TrainAllMethod()
factory.TrainAllMethods()
#factory.TrainAllMethods()
print 'Execute TMVA: TestAllMethods'
factory.TestAllMethods()
print 'Execute TMVA: EvaluateAllMethods'
factory.EvaluateAllMethods()
print 'Execute TMVA: output.Write'
trainingOutputFile.Close()
