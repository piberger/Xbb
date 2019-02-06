#!/usr/bin/env python
from BranchTools import AddCollectionsModule
from myutils.sampleTree import SampleTree as SampleTree

class FilterPrimaryDatasetOverlap(AddCollectionsModule):

    def __init__(self, fileName, applyToSamples):
        super(FilterPrimaryDatasetOverlap, self).__init__()
        self.excludeTreeFileName = fileName
        self.applyToSamples = applyToSamples

    def customInit(self, initVars):
        self.n_excluded = 0
        self.n_kept = 0
        self.n_skipped = 0
        self.sample = initVars['sample']
        self.config = initVars['config']

        if self.sample.identifier in self.applyToSamples:
            self.excludedEvents = {}
            excludedSampleTree = SampleTree([self.excludeTreeFileName], config=self.config)
            excludedSampleTree.enableBranches(['run','event'])
            print "INFO: loading list of events to filter"
            n_events = 0
            for ev in excludedSampleTree:
                if ev.run not in self.excludedEvents:
                    self.excludedEvents[ev.run] = {}
                if ev.event not in self.excludedEvents[ev.run]:
                    self.excludedEvents[ev.run][ev.event] = 0
                self.excludedEvents[ev.run][ev.event] += 1
                if self.excludedEvents[ev.run][ev.event]==1:
                    n_events += 1

            intrinsicDuplicates = sum([[[event,run,count] for event,count in self.excludedEvents[run].items() if count > 1] for run in self.excludedEvents.keys()], [])
            print "INFO: done => ", n_events, "distinct events will be filtered out of", self.applyToSamples
            if len(intrinsicDuplicates) > 0:
                print "INFO: the event list provided contains",len(intrinsicDuplicates),"duplicates itself!"
        else:
            print "INFO: event number filter disdable for this sample"

    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            if self.sample.identifier in self.applyToSamples:
                if tree.run in self.excludedEvents and tree.event in self.excludedEvents[tree.run]:
                    self.n_excluded += 1
                    return False
                else:
                    self.n_kept += 1
                    return True
            else:
                self.n_skipped += 1

    def afterProcessing(self):
        print "INFO: statistics"
        print "INFO:  > events kept:    ", self.n_kept
        print "INFO:  > events excluded:", self.n_excluded
        print "INFO:  > events skipped: ", self.n_skipped, "(sample identifier is not in:", self.applyToSamples," -> skip)"
