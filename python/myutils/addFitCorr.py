#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np
import array
from BranchTools import Collection
from BranchTools import AddCollectionsModule

class addFitCorr(AddCollectionsModule):

    # AT behavior is to correct W+jets AND ST only in the 1-lepton channel.
    def __init__(self, sample=None, nano=False, branchName='FitCorr', correctWjetsOnlyInOneLepton=False):
        self.nano = nano
        self.branchName = branchName
        self.correctWjetsOnlyInOneLepton = correctWjetsOnlyInOneLepton
        super(addFitCorr, self).__init__()

    def customInit(self, initVars):
        self.sample = initVars['sample']
        self.config = initVars['config']
        self.dataset = self.config.get('General', 'dataset')

        if not self.sample.isData():
            self.addVectorBranch(self.branchName, 1.0, length=3)
            
            self.corr = {
                    '2016': {
                        'TT':  lambda V_pt: [1.064 - 0.000380*V_pt, 1.064 - 0.000469*V_pt, 1.064 - 0.000291*V_pt],
                        'WHF': lambda V_pt: [1.259 - 0.00167*V_pt, 1.259 - 0.00180*V_pt, 1.259 - 0.00154*V_pt],
                        'WLF': lambda V_pt: [1.097 - 0.000575*V_pt, 1.097 - 0.000621*V_pt, 1.097 - 0.000529*V_pt],
                        },
                    '2017': {
                        'TT':  lambda V_pt: [1.103 - 0.00061*V_pt, 1.103 - 0.00069*V_pt, 1.103 - 0.00053*V_pt],
                        'WHF': lambda V_pt: [1.337 - 0.0016*V_pt, 1.337 - 0.0017*V_pt, 1.337 - 0.0015*V_pt],
                        'WLF': lambda V_pt: [1.115 - 0.00064*V_pt, 1.115 - 0.00068*V_pt, 1.115 - 0.00060*V_pt],
                        },
                    '2018': {
                        'TT':  lambda V_pt: [1.103 - 0.00061*V_pt, 1.103 - 0.00069*V_pt, 1.103 - 0.00053*V_pt],
                        'WHF': lambda V_pt: [1.337 - 0.0016*V_pt, 1.337 - 0.0017*V_pt, 1.337 - 0.0015*V_pt],
                        'WLF': lambda V_pt: [1.115 - 0.00064*V_pt, 1.115 - 0.00068*V_pt, 1.115 - 0.00060*V_pt],
                        }
                }

            if self.dataset not in self.corr:
                print('\x1b[31mERROR: unknown dataset:', self.dataset, '\x1b[0m')
                raise Exception('UnknownDataset')

    def countBs(self, tree):
        count = 0
        if not self.nano:
            for i in range(tree.nGenJet):
                if tree.GenJet_pt[i]>20 and abs(tree.GenJet_eta[i])<2.4 and  tree.GenJet_numBHadrons[i] > 0:
                    count += 1
        else:
            for i in range(tree.nGenJet):
                if tree.GenJet_pt[i]>20 and abs(tree.GenJet_eta[i])<2.4 and  tree.GenJet_hadronFlavour[i]==5:
                    count += 1
        return count


    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree) and not self.sample.isData():
            self.markProcessed(tree)

            V_pt = tree.V_pt if self.nano else tree.V_new_pt

            cat = None
            if self.sample.identifier.startswith('TT'):
                cat = 'TT'
            elif (not self.correctWjetsOnlyInOneLepton or (tree.isWmunu or tree.isWenu)):
                if self.sample.identifier.startswith('WJets') or self.sample.identifier.startswith('WBJets'):
                    cat = 'WLF' if self.countBs(tree) < 1 else 'WHF'
                elif self.sample.identifier.startswith('ST'):
                    # no dedicated ST category, use W+HF
                    cat = 'WHF'

            self._b(self.branchName)[:] = array.array('d', self.corr[self.dataset][cat](V_pt) if cat else [1.0, 1.0, 1.0])

        return True 
