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
                'DoubleBTWeight',
                'DoubleBLWeightUp',
                'DoubleBM1WeightUp',
                'DoubleBM2WeightUp',
                'DoubleBTWeightUp',
                'DoubleBLWeightDown',
                'DoubleBM1WeightDown',
                'DoubleBM2WeightDown',
                'DoubleBTWeightDown',
                ]

        for b in self.bname:
            self.branchBuffers[b] = np.ones(6, dtype=np.float32) #all Fat jets (6 in total)
            self.branches.append({'name': b, 'formula': self.getVectorBranch, 'arguments': {'branch': b, 'length':6}, 'length': 6})

    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):

        #Fill the double b tagger
        for b in self.bname:
            for i in range(tree.nFatjetAK08ungroomed):
                self.branchBuffers[b][i] = self.getBBtagSF(b, tree.FatjetAK08ungroomed_pt[i])
            for i in range(tree.nFatjetAK08ungroomed, 6):
                self.branchBuffers[b][i] = 1.0

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

        indexsys = -1

        if 'Up' in Wp:
            indexsys = 1
        elif 'Down' in Wp:
            indexsys = 2
        else: indexsys = 0

        SF = []

        if 'DoubleBLWeight' in Wp:
            SF = [[0.96, 1., 1.01], [0.99, 1.04, 1.03], [0.94, 0.97, 0.97]]
        elif 'DoubleBM1Weight' in Wp:
            SF = [[0.93, 1.01, 0.99], [0.96, 1.04, 1.01], [0.91, 0.98, 0.95]]
        elif 'DoubleBM2Weight' in Wp:
            SF = [[0.92, 1.01, 0.92], [0.95, 1.04, 0.95], [0.89, 0.97, 0.87]]
        elif 'DoubleBTWeight' in Wp:
            SF = [[0.85, 0.91, 0.91], [0.88, 0.94, 0.94], [0.82, 0.87, 0.87]]

        return SF[indexsys][index]


