#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from sampleTree import SampleTree 
from sample_parser import ParseInfo
import BetterConfigParser
from XbbConfig import XbbConfigReader

# adds the weight from General->weightF as a new branch
class WeightAsBranch(AddCollectionsModule):

    def __init__(self, branchName='weight'):
        super(WeightAsBranch, self).__init__()
        self.branchName = branchName

    def customInit(self, initVars):
        self.sample     = initVars['sample']
        self.sampleTree = initVars['sampleTree']
        self.config     = initVars['config']
        self.addBranch(self.branchName)
        self.addBranch("weightF")
        self.addBranch("weightXS")

        if not self.sample.isData():
            self.weightString = self.config.get('Weights','weightF')
            # per sample special weight
            if self.config.has_option('Weights', 'useSpecialWeight') and eval(self.config.get('Weights', 'useSpecialWeight')):
                specialweight = self.sample.specialweight
                self.weightString = "(({weight})*({specialweight}))".format(weight=self.weightString, specialweight=specialweight)
                print ("INFO: use specialweight: {specialweight}".format(specialweight=specialweight))

            self.evalCut = self.config.get('Cuts','EvalCut')
            self.sampleTree.addFormula(self.weightString)
            self.sampleTree.addFormula(self.evalCut)

            self.excludeTrainingSet = False

            # to compute the correct scale to cross-section, all trees of the sample have to be used!
            sampleTreeForCount = SampleTree({'sample': self.sample, 'folder': initVars['pathIN']}, config=self.config)
            self.weightScaleToXS = sampleTreeForCount.getScale(self.sample) * (2.0 if self.excludeTrainingSet else 1.0)
            print "scale:", self.weightScaleToXS, self.sample

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            self._b(self.branchName)[0] = 1.0
            self._b("weightF")[0] = 1.0
            self._b("weightXS")[0] = 1.0

            if not self.sample.isData():

                if not self.excludeTrainingSet or self.sampleTree.evaluate(self.evalCut):
                    weightF = self.sampleTree.evaluate(self.weightString)
                    self._b(self.branchName)[0] = weightF * self.weightScaleToXS
                    self._b("weightF")[0]       = weightF 
                    self._b("weightXS")[0]      = self.weightScaleToXS 
                else:
                    return False

if __name__ == '__main__':

    # read config

    ## this is what the XbbConfigReader module is doing:
    #pathconfig = BetterConfigParser.BetterConfigParser()
    #pathconfig.read('Zvv2017config/paths.ini')
    #configFiles = pathconfig.get('Configuration', 'List').split(' ')
    #config = BetterConfigParser.BetterConfigParser()
    #for configFile in configFiles:
    #    print(configFile)
    #    config.read('Zvv2017config/' + configFile)

    config = XbbConfigReader.read('Zvv2017')

    inputFile = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/berger_p2/VHbb/VHbbPostNano2017/V5/Zvv/rerun/v4j/eval/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/tree_aa5e971734ef4e885512748d534e6937ff03dc61feed21b6772ba943_000000_000000_0000_9_a6c5a52b56e5e0c7ad5aec31429c8926bf32cf39adbe087f05cfb323.root'
    path = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/berger_p2/VHbb/VHbbPostNano2017/V5/Zvv/rerun/v4j/eval/' 
    samplefiles = '../samples/VHbbPostNano2017_V5/merged_Zvv2017/' 
    samplesinfo = 'Zvv2017config/samples_nosplit.ini' 
    info = ParseInfo(samplesinfo, path)
    sample = [x for x in info if x.identifier == 'ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8'][0]
    #print([x.identifier for x in info])
    
    # read sample
    sampleTree = SampleTree([inputFile], config=config)
    
    # initialize module
    w = WeightAsBranch()
    w.customInit({'sampleTree': sampleTree, 'config': config, 'sample': sample, 'pathIN': path}) 

    #addAsBranch = True
    addAsBranch = False

    if addAsBranch:

        # add all new branches defined in the above module as output 
        #  this links the above module with the SampleTree class
        #  which will call the processEvent() during the loop to
        #  fill the output branches
        sampleTree.addOutputBranches(w.getBranches()) 

        # output files
        sampleTree.addOutputTree('/scratch/berger_p2/testWithWeight_MET_below_250.root', cut='MET_Pt<250', branches='*')
        sampleTree.addOutputTree('/scratch/berger_p2/testWithWeight_MET_above_250.root', cut='MET_Pt>250', branches='*')

        # loop over all events!
        sampleTree.process()

    else:
        # process the first event only
        w.processEvent(sampleTree.tree)
        print('weight:', w._b('weight')[0])
        print('weightF:',  w._b('weightF')[0])
        print('weightXS:',  w._b('weightXS')[0])
        print('product:', w._b('weightF')[0] * w._b('weightXS')[0], ' == ', w._b('weight')[0]) 


    
