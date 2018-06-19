#!/usr/bin/env python
import ROOT

# DY stitching weight
#  defined as 'specialweight' in samples_nosplit.ini
class DYspecialWeight(object):

    def __init__(self, branchName='DY_specialWeight'):
        self.branches = [{'name': branchName, 'formula': self.getDYspecialWeight}]
        self.branches += [{'name': 'isDY', 'formula': self.getDY}]

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.sampleTree = initVars['sampleTree']
        self.sampleTree.addFormula(self.sample.specialweight)

    def getBranches(self):
        return self.branches

    def getDYspecialWeight(self, tree=None):
        specialWeight = 1.0
        if self.sample.specialweight:
            specialWeight = self.sampleTree.evaluate(self.sample.specialweight) 
        return specialWeight

    def getDY(self, tree=None):
        return 'DY' in self.sample.identifier

