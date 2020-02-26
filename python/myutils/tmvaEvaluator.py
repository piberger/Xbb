#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
import os
import json
import array
import pickle
from myutils.XbbTools import XbbTools
from myutils.XbbTools import XbbMvaInputsList


class tmvaEvaluator(AddCollectionsModule):

    def __init__(self, mvaName, condition=None, debug=False):
        self.mvaName = mvaName
        self.MVAinfo = None
        self.debug = debug or 'XBBDEBUG' in os.environ
        self.condition = condition
        self.stats = {'passed': 0, 'skipped': 0}
        super(tmvaEvaluator, self).__init__()

    def customInit(self, initVars):
        self.config = initVars['config']
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']

        if self.condition:
            self.sampleTree.addFormula(self.condition)

        self.tmvaOptions = self.config.get('TMVA', 'options') if (self.config.has_section('TMVA') and self.config.has_option('TMVA','Options')) else '!Color:!Silent'
        self.reader = ROOT.TMVA.Reader(self.tmvaOptions)

        # load MVA input features and systematic variations from config
        self.systematics = XbbTools.getMvaSystematics(self.mvaName,config=self.config)
        self.treeVarSet  = self.config.get(self.mvaName, 'treeVarSet')
        self.featureList = XbbMvaInputsList(XbbTools.parseList(self.config.get(self.treeVarSet, "Nominal")), config=self.config)
        self.nFeatures   = self.featureList.length()

        print("INFO: using treeVarSet: \x1b[33m", self.treeVarSet, "\x1b[0m")
        for i in range(self.nFeatures):
            print("INFO: > [%d] %s"%(i, self.featureList.get(i)))

        # create formulas for input variables
        self.inputVariables = {}
        for syst in self.systematics:
            systBase, UD              = XbbTools.splitSystVariation(syst, sample=self.sample)
            self.inputVariables[syst] = [XbbTools.sanitizeExpression(self.featureList.get(i, syst=systBase, UD=UD), config=self.config, debug=self.debug) for i in range(self.nFeatures)]
            for var in self.inputVariables[syst]:
                self.sampleTree.addFormula(var)

        # load MVA meta data (really needed?)
        try:
            MVAdir           = self.config.get('Directories', 'vhbbpath')
            factoryname      = self.config.get('factory', 'factoryname')
            MVAinfofileName = MVAdir+'/python/weights/'+factoryname+'_'+self.mvaName+'.info'
            MVAinfofile = open(MVAinfofileName, 'r')
            print("INFO: loading TMVA meta data from: \x1b[32m", MVAinfofileName, "\x1b[0m")
            self.MVAinfo = pickle.load(MVAinfofile)
            MVAinfofile.close()
            weightFileName = MVAdir+'/python/weights/'+self.MVAinfo.getweightfile()
        except Exception as e:
            print("WARNING: could not load MVA info file:", e, " trying to use default naming convention for XML file")
            weightFileName = MVAdir+'/python/weights/MVA_' + self.mvaName + '.weights.xml' 

        # TMVA weights
        print("INFO: loading TMVA weights from: \x1b[32m", weightFileName, "\x1b[0m")

        # buffer to store MVA inputs
        self.MVA_var_buffer = [array.array('f', [0.0]) for i in range(self.nFeatures)]

        # book MVA 
        for i in range(self.nFeatures):
            self.reader.AddVariable(self.featureList.get(i), self.MVA_var_buffer[i])
        self.reader.BookMVA(self.mvaName, weightFileName) 
        print("INFO: TMVA method \x1b[33m", self.mvaName, "\x1b[0m booked.")
        
        # create output branches and add them to output trees
        self.tmvaCollection = Collection(self.mvaName, self.systematics, leaves=True)
        self.addCollection(self.tmvaCollection)


    # called from main loop for every event
    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            if self.condition is None or self.sampleTree.evaluate(self.condition):
                self.stats['passed'] += 1

                for i, syst in enumerate(self.systematics):
                    systName = syst if self.sample.isMC() else 'Nominal' 
                    for j in range(self.nFeatures):
                        self.MVA_var_buffer[j][0] = self.sampleTree.evaluate(self.inputVariables[systName][j])
                    self.tmvaCollection._b()[i] = self.reader.EvaluateMVA(self.mvaName) 

            else:
                self.stats['skipped'] += 1

                for i, syst in enumerate(self.systematics):
                    self.tmvaCollection._b()[i] = -2.0 

    def afterProcessing(self):
        print("INFO: out of", self.stats['passed']+self.stats['skipped'], "events:")
        print("INFO: evaluated \x1b[33m", self.mvaName, "\x1b[0m for", self.stats['passed'], "events and put default values for others.")
 
