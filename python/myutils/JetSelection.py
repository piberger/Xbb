#!/usr/bin/env python
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array
import os

class ATstyle(AddCollectionsModule):

    def __init__(self, pt0=20.0, pt1=20.0):
        self.debug = 'XBBDEBUG' in os.environ
        self.pt0 = pt0
        self.pt1 = pt1
        super(ATstyle, self).__init__()

    def customInit(self, initVars):
        self.branchName = "hJidx"
        self.branchBuffers[self.branchName] = array.array('i', [-1, -1])
        self.branches.append({'name': self.branchName, 'formula': self.getIndices, 'length': 2, 'type': 'i'})
    
    def processEvent(self, tree):
        keepEvent = True
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            # [ [idx, pt, btag],...]
            jets = [ [-1,-1,-1],[-1,-1,-1] ]
            # first jet

            for i in range(tree.nJet):
                if tree.Jet_lepFilter[i]>0 and tree.Jet_puId[i]>0 and tree.Jet_PtReg[i]>self.pt0 and abs(tree.Jet_eta[i])<2.4:
                    if tree.Jet_btagDeepB[i] > jets[0][2]:
                        jets[0] = [i, tree.Jet_PtReg[i], tree.Jet_btagDeepB[i]]
            
            for i in range(tree.nJet):
                if tree.Jet_lepFilter[i]>0 and tree.Jet_puId[i]>0 and tree.Jet_PtReg[i]>self.pt1 and abs(tree.Jet_eta[i])<2.4 and i != jets[0][0]:
                    if tree.Jet_btagDeepB[i] > jets[1][2]:
                        jets[1] = [i, tree.Jet_PtReg[i], tree.Jet_btagDeepB[i]]

            if jets[0][2] > jets[1][2]:
                self.branchBuffers[self.branchName][0] = jets[0][0]
                self.branchBuffers[self.branchName][1] = jets[1][0]
            else:
                self.branchBuffers[self.branchName][0] = jets[1][0]
                self.branchBuffers[self.branchName][1] = jets[0][0]

            # do pre-selection here!
            if jets[1][0]==-1 or jets[0][0]==-1:
                keepEvent = False
            elif tree.Jet_btagDeepB[jets[1][0]]<0.1522 or tree.Jet_btagDeepB[jets[0][0]]<0.1522:
                keepEvent = False

        return keepEvent
    
    def getIndices(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        destinationArray[0:2] = self.branchBuffers[self.branchName][0:2]
