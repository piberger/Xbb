#!/usr/bin/env python
import ROOT

class Drop(object):
    def __init__(self, dropBranches, keepBranches=None):
        self.dropBranches = dropBranches
        self.keepBranches = keepBranches

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        for dropBranch in self.dropBranches:
            self.sampleTree.SetBranchStatus(dropBranch, 0)
        if self.keepBranches:
            for keepBranch in self.keepBranches:
                self.sampleTree.SetBranchStatus(keepBranch, 1)

    def getBranches(self):
        return []
