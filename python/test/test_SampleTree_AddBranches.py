#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
import random
sys.path.append('../')
from myutils.sampleTree import SampleTree as SampleTree

# this does some stuff
class BlablaCorrector(object):

    # initialize heavy stuff once
    correctionFactor = 1.0
    correctionOffset = 0.0

    # this static methods are applied to every entry and passed as a function to SampleTree class
    @staticmethod
    def applyCorrection(tree):
        return (tree.a+tree.b+tree.c) * BlablaCorrector.correctionFactor + BlablaCorrector.correctionOffset

    @staticmethod
    def applyOtherCorrection(tree):
        return (tree.a+tree.b+tree.c) * 4 + 200


class TestSampleTreeAddBranchesMethods(unittest.TestCase):

    scratchDirectory = '.'

    def getTree(self):
        fileNames = [TestSampleTreeAddBranchesMethods.scratchDirectory + '/tree_%d.root'%i for i in range(10)]
        return SampleTree(fileNames)

    def test_AddBranches(self):

        sampleTree = self.getTree()

        # you can add a string
        sampleTree.addOutputBranch('jetSum', 'Sum$(Jet)')
        sampleTree.addOutputBranch('abcSum', 'a+b+c')

        # or a function, including lambdas
        sampleTree.addOutputBranch('abcSum2', lambda tree: tree.a + tree.b + tree.c)
        sampleTree.addOutputBranch('abcSum3', BlablaCorrector.applyCorrection)
        sampleTree.addOutputBranch('stuff', BlablaCorrector.applyOtherCorrection)

        # write output tree and apply also a cut
        sampleTree.addOutputTree(
            TestSampleTreeAddBranchesMethods.scratchDirectory + '/tree_withaddedbranches.root',
            cut='(a+b+c)>400',
        )
        sampleTree.process()

if __name__ == '__main__':
    unittest.main()
