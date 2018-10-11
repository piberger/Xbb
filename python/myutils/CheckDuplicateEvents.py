#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array

class CheckDuplicateEvents(AddCollectionsModule):

    def __init__(self, majorIndex='run', minorIndex='event', debug=False):
        self.eventDict = {}
        self.debug = debug
        self.majorIndex = majorIndex
        self.minorIndex = minorIndex
        self.duplicates = 0
        self.eventsProcessed = 0
        super(CheckDuplicateEvents, self).__init__()

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
    
    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self.eventsProcessed += 1

            major = getattr(tree, self.majorIndex)
            minor = getattr(tree, self.minorIndex)

            if major not in self.eventDict:
                self.eventDict[major] = {}
            if minor in self.eventDict[major]:
                self.duplicates += 1
            else:
                self.eventDict[major][minor] = True

    def beforeProcessing(self):
        self.sampleTree.disableOutput()
        self.sampleTree.enableBranches([self.majorIndex, self.minorIndex])
        print("\x1b[31mINFO: CheckDuplicateEvents(): output disabled and input forced to be event and run only - don't use this together with other modules!\x1b[0m")

    def afterProcessing(self):
        print("-"*80)
        print(" duplicate event check statistics:")
        print("   events:", self.eventsProcessed)
        print("   duplicate:", self.duplicates)
        print("     fraction:", "%1.4f"%(100.0*self.duplicates/self.eventsProcessed))
        print("-"*80)

