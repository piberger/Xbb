#!/usr/bin/env python
import ROOT
import numpy as np
import array
from pdgId import pdgId
import sys

class QCDweights(object):

    def __init__(self, sample=None):
        self.lastEntry = -1
        self.branchBuffers = {}
        self.branches = []
        self.branches.append({'name': 'QCDw', 'formula': self.getBranch, 'arguments': 'QCDw'})
        self.branchBuffers['QCDw'] = array.array('f', [0])
        if sample:
            self.customInit(sample=sample)

    def customInit(self, initVars):
        #print 'Doing customIni'
        sample = initVars['sample']
        self.sys_sample = None
        if 'WJetsToLNu' in sample.identifier or 'WBJetsToLNu' in sample.identifier:
            self.sys_sample = 'WJet'
        #QCD weight is not applied for DY sample with mass between 10-50 GeV
        elif 'DY' in sample.identifier and not '10to50' in sample.identifier:
            self.sys_sample = 'DY'
        self.isData = sample.type == 'DATA'
        if self.isData:
            self.branches = []

    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getBranches(self):
        return self.branches

    # read from buffers which have been filled in processEvent()    
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        if currentEntry != self.lastEntry and not self.isData:
            self.lastEntry = currentEntry
            if self.sys_sample != None:
                num = 1.
                HT = tree.lheHT
                if HT < 100:
                    num = 1.
                elif HT > 100 and HT < 200:
                    num = 1.58
                elif HT > 200 and HT < 400:
                    num = 1.438
                elif HT > 400 and HT < 600:
                    num = 1.494
                elif HT > 600:
                    num = 1.139

                den = 1.

                if self.sys_sample == 'DY':
                    den = 1.23
                elif self.sys_sample == 'WJet':
                    den = 1.21

                self.branchBuffers['QCDw'][0] = num/den
            else: 
                self.branchBuffers['QCDw'][0] = 1.

            return True
