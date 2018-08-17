#!/usr/bin/env python
import ROOT
import numpy as np
import array

class addFitCorr(object):

    def __init__(self, sample=None, nano=False, dataset = 'year'):

        self.nano = nano
        self.dataset= dataset
        self.branchBuffers = {}
        self.branches = []
        self.branchBuffers['FitCorr'] = np.ones(3, dtype=np.float32)
        self.branches.append({'name': 'FitCorr', 'formula': self.getVectorBranch, 'arguments': {'branch': 'FitCorr', 'length':3}, 'length': 3})

        if sample:
            self.customInit(sample=sample)

    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'
        #print 'sample type is', sample.type
        self.identifier = sample.identifier
        #print 'sample id is', sample.identifier
        if self.isData:
            self.branches = []

    # read from buffers which have been filled in processEvent()    
    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        #print 'arguments are', arguments
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):
        if self.isData:
            return True 
        else:
            CorrFactor = [1, 1, 1]

            if not self.nano:
                V_pt = tree.V_new_pt
            else:
                V_pt = tree.V_pt

            if 'TT' in self.identifier:
                if self.dataset == '2016':
                    CorrFactor =  [1.064 - 0.000380*V_pt, 1.064 - 0.000469*V_pt, 1.064 - 0.000291*V_pt]
                elif self.dataset== '2017':
                    CorrFactor =  [1.103 - 0.00061*V_pt, 1.103 - 0.00069*V_pt, 1.103 - 0.00053*V_pt]
                    #print "Data set is 2017"
            elif ('WJets' in self.identifier or 'WBJets' in self.identifier ):
                count = 0
                if not self.nano:
                    for i in range(tree.nGenJet):
                        if tree.GenJet_pt[i]>20 and abs(tree.GenJet_eta[i])<2.4 and  tree.GenJet_numBHadrons[i] > 0:
                            count += 1
                else:
                    for i in range(tree.nGenJet):
                        #'Sum$(GenJet_pt>20 && abs(GenJet_eta)<2.4 && GenJet_hadronFlavour==5)>=2']
                        if tree.GenJet_pt[i]>20 and abs(tree.GenJet_eta[i])<2.4 and  tree.GenJet_hadronFlavour[i]==5:
                            count += 1

                # Fix
                if count >= 1:
                    if self.dataset == '2016':
                        CorrFactor = [1.259 - 0.00167*V_pt, 1.259 - 0.00180*V_pt, 1.259 - 0.00154*V_pt]
                    elif self.dataset == '2017':
                        CorrFactor = [1.337 - 0.0016*V_pt, 1.337 - 0.0018*V_pt, 1.337 - 0.0015*V_pt]
                        #print "Data set is 2017"
                else:
                    if self.dataset == '2016':
                        CorrFactor = [1.097 - 0.000575*V_pt, 1.097 - 0.000621*V_pt, 1.097 - 0.000529*V_pt]
                    elif self.dataset == '2017':
                        CorrFactor = [1.115 - 0.00064*V_pt, 1.115 - 0.00068*V_pt, 1.115 - 0.00060*V_pt]
                        #print "Data set is 2017"
                # BUG
                #if count >= 1:
                #    CorrFactor = [1.097 - 0.000575*V_pt, 1.097 - 0.000621*V_pt, 1.097 - 0.000529*V_pt]
                #else:
                #    CorrFactor = [1.259 - 0.00167*V_pt, 1.259 - 0.00180*V_pt, 1.259 - 0.00154*V_pt]
            elif 'ST' in self.identifier:

                if self.dataset == '2016':
                     CorrFactor = [1.259 - 0.00167*V_pt, 1.259 - 0.00180*V_pt, 1.259 - 0.00154*V_pt]
                elif self.dataset == '2017':
                     CorrFactor = [1.337 - 0.0016*V_pt, 1.337 - 0.0018*V_pt, 1.337 - 0.0015*V_pt]
                     #print "Data set is 2017"

            self.branchBuffers['FitCorr'][0] = CorrFactor[0]
            self.branchBuffers['FitCorr'][1] = CorrFactor[1]
            self.branchBuffers['FitCorr'][2] = CorrFactor[2]
            #print 'CorrFactor is', CorrFactor
        return True 
