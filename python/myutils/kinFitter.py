#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys

ak4pfchs_ptres = None

if not os.path.isfile('AnalysisTools/python/__init__.py') or not os.path.isfile('AnalysisTools/__init__.py'):
    open('AnalysisTools/__init__.py', 'a').close()
    open('AnalysisTools/python/__init__.py', 'a').close()

sys.path.append("..")
# lets hope for no name conflicts...
from AnalysisTools.python.kinfitter import *

class NullTree(object):
    def __getattr__(self, name):
        def method(*args):
            pass
        return method

class AnalysisToolsTree(object):
    def __init__(self, sampleTree, isData=False):

        self.formulas = {
                'hJetInd1': 'hJCMVAV2idx[0]',
                'hJetInd2': 'hJCMVAV2idx[1]',
                'hj1_pt': 'Jet_pt[hJCMVAV2idx[0]]',
                'hj1_eta': 'Jet_eta[hJCMVAV2idx[0]]',
                'hj1_phi': 'Jet_phi[hJCMVAV2idx[0]]',
                'hj1_mass': 'Jet_mass[hJCMVAV2idx[0]]',
                'hj2_pt': 'Jet_pt[hJCMVAV2idx[1]]',
                'hj2_eta': 'Jet_eta[hJCMVAV2idx[1]]',
                'hj2_phi': 'Jet_phi[hJCMVAV2idx[1]]',
                'hj2_mass': 'Jet_mass[hJCMVAV2idx[1]]',
                'GenBJ1_eta': '-1' if isData else 'Jet_mcEta[hJCMVAV2idx[0]]', 
                'GenBJ2_eta': '-1' if isData else 'Jet_mcEta[hJCMVAV2idx[1]]', 
                'GenBJ1_phi': '-1' if isData else 'Jet_mcPhi[hJCMVAV2idx[0]]', 
                'GenBJ2_phi': '-1' if isData else 'Jet_mcPhi[hJCMVAV2idx[1]]', 
                'GenBJ1_pt': '-1' if isData else 'Jet_mcPt[hJCMVAV2idx[0]]', 
                'GenBJ2_pt': '-1' if isData else 'Jet_mcPt[hJCMVAV2idx[1]]', 
                'GenBJ1_mass': '-1' if isData else 'Jet_mcM[hJCMVAV2idx[0]]', 
                'GenBJ2_mass': '-1' if isData else 'Jet_mcM[hJCMVAV2idx[1]]', 
                'isZmm': '(Vtype==0)',
                'lepInd1': '0',
                'lepInd2': '1',
                }
        self.aliases = {
                'Jet_Pt': 'Jet_pt',
                'Jet_bReg': 'Jet_pt_reg',
                'n_hj_matched': 'nhJCMVAV2idx',
                'fixedGridRhoFastjetAll': 'rho',
                'Jet_jetId': 'Jet_id',
                'Jet_lepFilter': 'Jet_pt',
                'Muon_pt': 'vLeptons_new_pt',
                'Muon_eta': 'vLeptons_new_eta',
                'Muon_phi': 'vLeptons_new_phi',
                'Muon_mass': 'vLeptons_new_mass',
                'Electron_pt': 'vLeptons_new_pt',
                'Electron_eta': 'vLeptons_new_eta',
                'Electron_phi': 'vLeptons_new_phi',
                'Electron_mass': 'vLeptons_new_mass',
                }
        self.castToInt = {'hJetInd1': True, 'hJetInd2': True, 'lepInd1': True, 'lepInd2':True}
        self.constantArray = {'Muon_ptErr': [2, 9.0], 'Electron_energyErr': [2, 25.0]}
        
        self.sampleTree = sampleTree
        for alias, target in self.aliases.iteritems():
            self.sampleTree.tree.SetAlias(alias, target)
        for formula, target in self.formulas.iteritems():
            self.sampleTree.addFormula(formula, target)

    def __getattr__(self, name):
        if hasattr(self.sampleTree.tree, name):
            return getattr(self.sampleTree.tree, name)
        elif name in self.constantArray:
            return [self.constantArray[name][1]]*self.constantArray[name][0]
        else:
            if name in self.castToInt:
                return int(self.sampleTree.evaluate(name))
            else:
                return self.sampleTree.evaluate(name)


class kinFitter(AddCollectionsModule):

    def __init__(self, branchName="kinFit"):
        super(kinFitter, self).__init__()
        self.branchName = branchName
        
        self.leaves = VarContainer(NullTree()).tree_vars
        self.kinFitterCollection = Collection(self.branchName, self.leaves, leaves=True) 
        self.addCollection(self.kinFitterCollection)

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        self.wrappedTree = AnalysisToolsTree(self.sampleTree, isData=self.sample.isData())

        if self.sample.isData():
            self.ak4pfchs_ptres = ROOT.JME.JetResolution('AnalysisTools/VHbbAnalysis/aux/Spring16_25nsV6_DATA_PtResolution_AK4PFchs.txt')
        else:
            self.ak4pfchs_ptres = ROOT.JME.JetResolution('AnalysisTools/VHbbAnalysis/aux/Spring16_25nsV6_MC_PtResolution_AK4PFchs.txt')

        ak4pfchs_ptres

    def processEvent(self, tree):
        global ak4pfchs_ptres

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            # run kinematic fitter
            c = VarContainer(NullTree())
            apply_fit_to_event(self.wrappedTree, c, self.ak4pfchs_ptres)

            # write output branches
            for i, leaf in enumerate(self.leaves):
                self.kinFitterCollection[self.branchName][i] = getattr(c, leaf)
        
        return True
