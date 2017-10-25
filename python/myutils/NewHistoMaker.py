from __future__ import print_function
import sys,os
import ROOT 
from array import array
from printcolor import printc
from BetterConfigParser import BetterConfigParser
from copy import copy
import time

from NewTreeCache import TreeCache as TreeCache
from sampleTree import SampleTree

class NewHistoMaker:
    def __init__(self, config, sample, sampleTree, histogramOptions):
        self.config = config
        self.sample = sample
        self.sampleTree = sampleTree
        self.histogramOptions = histogramOptions
        self.histogram = None

    def initializeHistogram(self):
        self.histogramName = self.sample.name + '_' + self.histogramOptions['var']
        self.histogram = ROOT.TH1F(self.histogramName, self.histogramName, self.histogramOptions['nBins'], self.histogramOptions['xMin'], self.histogramOptions['xMax'])

    def scaleHistogram(self):
        TrainFlag = False
        if self.sample.type != 'DATA':
            if 'BDT' in self.histogramOptions['treeVar'] or 'bdt' in self.histogramOptions['treeVar'] or 'OPT' in self.histogramOptions['treeVar']:
                if TrainFlag:
                    if 'ZJets_amc' in self.sample.name:
                        print ('No rescale applied for the sample', self.sample.name)
                        MC_rescale_factor = 1.
                    else:
                        MC_rescale_factor=2. ##FIXME## only dataset used for training must be rescaled!!
                else: 
                    MC_rescale_factor = 1.

                ScaleFactor = self.sampleTree.getScale(self.sample) * MC_rescale_factor
            else: 
                ScaleFactor = self.sampleTree.getScale(self.sample)

            if ScaleFactor != 0:
                self.histogram.Scale(ScaleFactor)

    def getHistogram(self):
        self.initializeHistogram()
        if self.histogram:

            # apply weights only to MC and not to DATA
            if 'group' in self.histogramOptions and self.histogramOptions['group'] == 'DATA':
                weightF = '1'
            else:
                weightF = "({weight})*({specialweight})".format(weight=self.histogramOptions['weight'] if ('weight' in self.histogramOptions and self.histogramOptions['weight']) else '1', specialweight=self.sample.specialweight) 
            # add tree cut, todo: add sample cut again, which should not matter but to be safe
            selection = "({weight})*({cut})".format(weight=weightF, cut='1') 
            nEvents = self.sampleTree.tree.Draw('{var}>>{histogramName}'.format(var=self.histogramOptions['treeVar'], histogramName=self.histogramName), selection)
            if nEvents < 0:
                print ("\x1b[31mERROR: error in TTree:Draw!\x1b[0m")
            self.scaleHistogram()
        else:
            print ("ERROR: initialization of histogram failed!")
        return self.histogram



