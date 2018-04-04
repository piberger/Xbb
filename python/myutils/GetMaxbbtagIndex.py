#!/usr/bin/env python
import ROOT
import sys
import array

class GetMaxbbtagIndex(object):

    def __init__(self):

        self.branchBuffers = {}
        self.branches = []

        self.branchBuffers['Maxbbtagidx'] = array.array('f', [0])
        self.branches.append({'name': 'Maxbbtagidx', 'formula': self.getBranch, 'arguments': 'Maxbbtagidx'})

        self.branchBuffers['Maxptidx'] = array.array('f', [0])
        self.branches.append({'name': 'Maxptidx', 'formula': self.getBranch, 'arguments': 'Maxptidx'})

    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):

        bbtagindex = -1
        bbtag = -99

        ptindex = -1
        pt = -99

        for i in range(tree.nFatjetAK08ungroomed):
            bbtag_new = tree.FatjetAK08ungroomed_bbtag[i]
            pt_new = tree.FatjetAK08ungroomed_pt[i]
            if bbtag_new > bbtag:
                bbtag = bbtag_new
                bbtagindex = i

            if pt_new > pt:
                pt = pt_new
                ptindex = i

        #In case no minimal bbtagindex was found, put it to 0
        if bbtagindex == -1 or ptindex == -1:
            if not tree.nFatjetAK08ungroomed == 0:
                print "@ERROR: bbtagindex or ptindex not maximised. Exiting"
                sys.exit()
            else:
                bbtagindex = 0
                ptindex = 0

        self.branchBuffers['Maxbbtagidx'][0] = bbtagindex
        self.branchBuffers['Maxptidx'][0] = ptindex

        return True






