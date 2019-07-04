#!/usr/bin/env python
from __future__ import print_function
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule

class removeFriendTree(AddCollectionsModule):
    def __init__(self):
        super(removeFriendTree, self).__init__()

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.sampleTree.addCallback('prepareOutput', self.removeFriendTrees)

    def removeFriendTrees(self):
        print("friend trees:")
        print(self.sampleTree.tree.GetEntries())
        print(self.sampleTree.tree.GetListOfFriends())
        fl = self.sampleTree.tree.GetListOfFriends()
        if fl:
            fl.Print()
            fl.Delete()

    def finish(self):
        for t in self.sampleTree.outputTrees:
            t['tree'].GetListOfFriends().Delete()

