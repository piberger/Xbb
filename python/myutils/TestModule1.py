#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np
import array
from BranchTools import Collection
from BranchTools import AddCollectionsModule


class TestModule1(AddCollectionsModule):

    def __init__(self):
        super(TestModule1, self).__init__()
        self.maxNjet = 256
        self.counter = 0
        print("\x1b[31mINFO: technical test only, do not use outputs of this module, they are garbage!\x1b[0m")

    def customInit(self, initVars):
        super(TestModule1, self).customInit(initVars)
        
        self.addBranch("debug__test1")
        self.addVectorBranch("Jet__debug", default=0.0, branchType='f', length=self.maxNjet, leaflist="Jet__debug[nJet]/F")

        self.MET_Pt     = array.array('f', [0.0])
        self.sampleTree.tree.SetBranchAddress("MET_Pt", self.MET_Pt)

    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            self._b("debug__test1")[0] = 42.0 + self.counter
            self.counter += 1
            self.MET_Pt[0]             = 12345.6

            for i in range(tree.nJet):
                self._b("Jet__debug")[i] = 1000.0 * self.counter + i
            print("MODULE1: WRITE, counter =", self.counter)
