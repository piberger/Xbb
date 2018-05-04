#!/usr/bin/env python
import ROOT
import numpy as np
import array

class AdditionalJetIndex(object):

    def __init__(self):
        self.branches = []
        self.branches.append({'name': 'myAddJetIdx0', 'formula': self.getAJidx, 'type': 'i'})
    
    def getBranches(self):
        return self.branches
    
    def getAJidx(self, tree):
        myAddJetIdx0 = -99
        for i in range(tree.nJet):
            # nonsense cut! replace by something useful!
            if tree.Jet_btagCMVAV2[i] < 0.5:
                myAddJetIdx0 = i
                break
        return myAddJetIdx0
