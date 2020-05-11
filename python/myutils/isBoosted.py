#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from XbbTools import XbbTools

class isBoosted(AddCollectionsModule):

    def __init__(self, branchName='isBoosted', cutName='all_BOOST'):
        super(isBoosted, self).__init__()
        self.branchName = branchName
        self.cutName = cutName
        self.version = 3
        self.variations = self._variations("isBoosted") 

    # returns cut string with variables replaced by their systematic variations
    def getSystVarCut(self, cut, syst, UD):
        replacementRulesList = XbbTools.getReplacementRulesList(self.config, syst)
        systVarCut           = XbbTools.getSystematicsVariationTemplate(cut, replacementRulesList)
        systVarCut           = systVarCut.replace('{syst}', syst).replace('{UD}', UD)
        return systVarCut

    def customInit(self, initVars):
        self.sample     = initVars['sample']
        self.sampleTree = initVars['sampleTree']
        self.config     = initVars['config']

        self.boostedCut = self.config.get('Cuts', self.cutName)
        self.systVarCuts = {}

        self.systematics = sorted(list(set(sum([eval(self.config.get('LimitGeneral', x)) for x in ['sys_cr', 'sys_BDT', 'sys_Mjj']], []))))

        # Nominal
        self.addIntegerBranch(self.branchName)
        self.sampleTree.addFormula(self.boostedCut)

        # systematic variations
        if self.sample.isMC():
            for syst in self.systematics:
                for UD in self.variations: 
                    systVarBranchName = self._v(self.branchName, syst, UD)
                    self.addIntegerBranch(systVarBranchName)
                    self.systVarCuts[systVarBranchName] = self.getSystVarCut(self.boostedCut, syst=syst, UD=UD)
                    self.sampleTree.addFormula(self.systVarCuts[systVarBranchName])

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            # Nominal
            b = int(self.sampleTree.evaluate(self.boostedCut))
            self._b(self._v(self.branchName))[0] = 1 if b > 0 else 0 

            # systematic variations
            if self.sample.isMC():
                for syst in self.systematics:
                    for UD in self.variations: 
                        systVarBranchName = self._v(self.branchName, syst, UD)
                        b = int(self.sampleTree.evaluate(self.systVarCuts[systVarBranchName]))
                        self._b(systVarBranchName)[0] = 1 if b > 0 else 0 


