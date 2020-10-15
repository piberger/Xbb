#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np
from BranchTools import Collection
from BranchTools import AddCollectionsModule


class TestModule2(AddCollectionsModule):

    def __init__(self):
        super(TestModule2, self).__init__()
        print("\x1b[31mINFO: technical test only, do not use outputs of this module, they are garbage!\x1b[0m")

    def customInit(self, initVars):
        super(TestModule2, self).customInit(initVars)
        
        self.addBranch("debug__test2")
        self.addBranch("debug__test3")
        self.addBranch("debug__test4")
        self.addBranch("debug__test5")

    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            self._b("debug__test2")[0] = self._r("debug__test1") + 1000.0
            self._b("debug__test3")[0] = self._r("MET_Pt")
            self._b("debug__test4")[0] = self._r("MET_Phi")

            s = 0.0
            jetStuff = self._r("Jet__debug")
            for i in range(tree.nJet):
                s += jetStuff[i]
            self._b("debug__test5")[0] = s
            print("N=",tree.nJet, jetStuff, " => WRITE:",s)

