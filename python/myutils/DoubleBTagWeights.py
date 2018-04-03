#!/usr/bin/env python
import ROOT
import sys
import numpy as np

class DoubleBTagWeights(object):

    def __init__(self):
        #print 'CREATING DoubleBTagWeights'
        self.branchBuffers = {}
        self.branches = []

        self.bname = [
                'DoubleBLWeight',
                'DoubleBM1Weight',
                'DoubleBM2Weight',
                'DoubleBTWeight'
                ]

        for b in self.bname:
            self.branchBuffers[b] = np.ones(3, dtype=np.float32) #all Fat jets (6 in total)
            self.branches.append({'name': b, 'formula': self.getVectorBranch, 'arguments': {'branch': b, 'length':3}, 'length': 3})

    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):

        #First step: get index of jet with largest bbtag
        index = -1
        bbtag = -99

        for i in range(tree.nFatjetAK08ungroomed):
            bbtag_new = tree.FatjetAK08ungroomed_bbtag[i]
            if bbtag_new > bbtag:
                bbtag = bbtag_new
                index = i

        if index == -1:
            if not tree.nFatjetAK08ungroomed == 0:
                print "@ERROR: index not maximised. Exiting"
                sys.exit()

        #Fill the double b tagger
        for b in self.bname:
            bbWeight = self.getBBtagSF(b, tree.FatjetAK08ungroomed_pt[index])
            self.branchBuffers[b][0] = bbWeight[0]
            self.branchBuffers[b][1] = bbWeight[1]
            self.branchBuffers[b][2] = bbWeight[2]

        #print 'self.branchBuffers[b][2] is', self.branchBuffers[b][2] = bbWeight[2]
        return True

    def getBBtagSF(self, Wp, pt):
        index = -1
        if pt > 250 and pt < 350:
            index = 0
        elif pt > 350 and pt < 430:
            index = 1
        elif pt > 350:
            index = 2
        elif pt < 250:
            index = 0
        #print'index in getBBtagSF is', index

        SFnom   = []
        SFup    = []
        SFdown  = []

        if Wp == 'DoubleBLWeight':
            SFnom       = [0.96, 1., 1.01]
            SFup        = [0.99, 1.04, 1.03]
            SFdown      = [0.94, 0.97, 0.97]
        elif Wp == 'DoubleBM1Weight':
            SFnom       = [0.93, 1.01, 0.99]
            SFup        = [0.96, 1.04, 1.01]
            SFdown      = [0.91, 0.98, 0.95]
        elif Wp == 'DoubleBM2Weight':
            SFnom       = [0.92, 1.01, 0.92]
            SFup        = [0.95, 1.04, 0.95]
            SFdown      = [0.89, 0.97, 0.87]
        elif Wp == 'DoubleBTWeight':
            SFnom       = [0.85, 0.91, 0.91]
            SFup        = [0.88, 0.94, 0.94]
            SFdown      = [0.82, 0.87, 0.87]

        return [SFnom[index], SFup[index], SFdown[index]]

