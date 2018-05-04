#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
import random
sys.path.append('../')
from myutils.sampleTree import SampleTree as SampleTree
import os


class TestSampleTreeCallbacksMethods(unittest.TestCase):

    scratchDirectory = os.environ['SCRATCH_DIR'] if 'SCRATCH_DIR' in os.environ else '.'

    def setUp(self):
        self.nEventsFound = 0

    def getTree(self):
        fileNames = [TestSampleTreeCallbacksMethods.scratchDirectory + '/tree_%d.root'%i for i in range(2)]
        return SampleTree(fileNames)

    def callback_after_write(self):
        print("HELLO from callback after loop")

    def callback_before_loop(self):
        print("HELLO from callback before loop")

    def event_callback(self, tree):
        if tree.b>444.4 and tree.b<444.5:
            print("event found:", tree.event, tree.b)
            self.nEventsFound += 1
        return True

    def test_SampleTree_Callback_1(self):
        sampleTree = self.getTree()

        # define some random cuts
        cuts = [
            "b>444.4&&b<444.5",
            "nJet==5&&Sum$(Jet)>500",
            "nJet==6&&Sum$(Jet)>600",
            "nJet==7&&Sum$(Jet)>700",
            "nJet==8&&Sum$(Jet)>800",
        ]
        # write skimmed subtrees to file
        for i, cut in enumerate(cuts):
            sampleTree.addOutputTree(
                outputFileName=TestSampleTreeCallbacksMethods.scratchDirectory + '/tree_test_%d.root'%i,
                cut=cut,
                callbacks={
                    'beforeLoop': self.callback_before_loop,
                    'afterWrite': self.callback_after_write,
                },
                branches='*',
            )
        sampleTree.setCallback('event', self.event_callback)
        sampleTree.process()

        # check otuput
        sampleTree2 = SampleTree([TestSampleTreeCallbacksMethods.scratchDirectory + '/tree_test_0.root'])
        resultsMethodB = sampleTree2.tree.GetEntries()
        print(sampleTree2.tree)
        print("events which triggered callback:", self.nEventsFound)
        print("events in tree 0:", resultsMethodB)
        self.assertEqual(self.nEventsFound, resultsMethodB)
        self.assertTrue(self.nEventsFound > 0)

if __name__ == '__main__':
    unittest.main()
