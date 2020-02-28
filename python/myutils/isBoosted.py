#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
from XbbTools import XbbTools

class isBoosted(AddCollectionsModule):

    def __init__(self, branchName='isBoosted'):
        super(isBoosted, self).__init__()
        self.branchName = branchName
        self.version = 1
        self.variations = ['Up','Down']

    def getBranchName(self, syst=None, UD=None):
        if syst is None or len(syst.strip()) < 1:
            return self.branchName
        else:
            return self.branchName + '_' + syst + '_' + UD

    def getSystVarCut(self, cut, syst, UD):
        replacementRulesList = XbbTools.getReplacementRulesList(self.config, syst)
        systVarCut           = XbbTools.getSystematicsVariationTemplate(cut, replacementRulesList)
        systVarCut           = systVarCut.replace('{syst}', syst).replace('{UD}', UD)
        return systVarCut

    def customInit(self, initVars):
        self.sample     = initVars['sample']
        self.sampleTree = initVars['sampleTree']
        self.config     = initVars['config']

        self.boostedCut = self.config.get('Cuts', 'all_BOOST') 
        self.systVarCuts = {}

        self.systematics = sorted(list(set(sum([eval(self.config.get('LimitGeneral', x)) for x in ['sys_cr', 'sys_BDT', 'sys_Mjj']], []))))

        # Nominal
        self.addIntegerBranch(self.branchName)
        self.sampleTree.addFormula(self.boostedCut)

        # systematic variations
        if self.sample.isMC():
            for syst in self.systematics:
                for UD in self.variations: 
                    systVarBranchName = self.getBranchName(syst=syst, UD=UD)
                    self.addIntegerBranch(systVarBranchName)
                    self.systVarCuts[systVarBranchName] = self.getSystVarCut(self.boostedCut, syst=syst, UD=UD)
                    self.sampleTree.addFormula(self.systVarCuts[systVarBranchName])

    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            # Nominal
            b = int(self.sampleTree.evaluate(self.boostedCut))
            self._b(self.getBranchName())[0] = 1 if b > 0 else 0 

            # systematic variations
            if self.sample.isMC():
                for syst in self.systematics:
                    for UD in self.variations: 
                        systVarBranchName = self.getBranchName(syst=syst, UD=UD)
                        b = int(self.sampleTree.evaluate(self.systVarCuts[systVarBranchName]))
                        self._b(systVarBranchName)[0] = 1 if b > 0 else 0 


