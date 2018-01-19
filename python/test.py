#!/usr/bin/env python
from __future__ import print_function
import sys, ROOT, warnings
ROOT.gROOT.SetBatch(True)
#suppres the EvalInstace conversion warning bug
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )
from optparse import OptionParser
from myutils import BetterConfigParser, mvainfo, ParseInfo
#paths.ini general.ini cuts.ini training.ini datacards.ini plots.ini lhe_weights.ini samples_nosplit.ini

# load config
config = BetterConfigParser()
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/paths.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/general.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/cuts.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/training.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/datacards.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/plots.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/lhe_weights.ini')
config.read('/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_9_4_0_pre3/src/Xbb/python/Zll2016config/samples_nosplit.ini')
print(config)
print(config.sections())
print(config.get('DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1', 'specialweight'))

