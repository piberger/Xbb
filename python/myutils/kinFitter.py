#!/usr/bin/env python
import ROOT
import numpy as np
import array
import os
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys

ak4pfchs_ptres = None

# make AT importable from python
if not os.path.isfile('AnalysisTools/python/__init__.py'):
    open('AnalysisTools/python/__init__.py', 'w').close()
if not os.path.isfile('AnalysisTools/__init__.py'):
    open('AnalysisTools/__init__.py', 'w').close()

sys.path.append("..")
# lets hope for no name conflicts...
from AnalysisTools.python.kinfitter import *

class NullTree(object):
    def GetListOfBranches(self):
        return []

    def __getattr__(self, name):
        def method(*args):
            pass
        return method

class AnalysisToolsTree(object):
    def __init__(self, sampleTree, isData=False, translationDict=None):
        self.outputBuffers = {}

        if sampleTree.treeName == 'tree':
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
        else:
            # NANOAOD default
            self.formulas = {
                    'hJetInd1': 'hJidxCMVA[0]',
                    'hJetInd2': 'hJidxCMVA[1]',
                    'hj1_pt': 'Jet_Pt[hJidxCMVA[0]]',
                    'hj1_eta': 'Jet_eta[hJidxCMVA[0]]',
                    'hj1_phi': 'Jet_phi[hJidxCMVA[0]]',
                    'hj1_mass': 'Jet_mass[hJidxCMVA[0]]',
                    'hj2_pt': 'Jet_Pt[hJidxCMVA[1]]',
                    'hj2_eta': 'Jet_eta[hJidxCMVA[1]]',
                    'hj2_phi': 'Jet_phi[hJidxCMVA[1]]',
                    'hj2_mass': 'Jet_mass[hJidxCMVA[1]]',
                    'hj1_reg_pt': 'Jet_PtReg[hJidxCMVA[0]]',
                    'hj1_reg_eta': 'Jet_eta[hJidxCMVA[0]]',
                    'hj1_reg_phi': 'Jet_phi[hJidxCMVA[0]]',
                    'hj1_reg_mass': 'Jet_mass[hJidxCMVA[0]]',
                    'hj2_reg_pt': 'Jet_PtReg[hJidxCMVA[1]]',
                    'hj2_reg_eta': 'Jet_eta[hJidxCMVA[1]]',
                    'hj2_reg_phi': 'Jet_phi[hJidxCMVA[1]]',
                    'hj2_reg_mass': 'Jet_mass[hJidxCMVA[1]]',
                    'hj12_pt': 'H_pt',
                    'hj12_eta': 'H_eta',
                    'hj12_phi': 'H_phi',
                    'hj12_mass': 'H_mass',
                    'hj12_reg_pt': 'H_pt',
                    'hj12_reg_eta': 'H_eta',
                    'hj12_reg_phi': 'H_phi',
                    'hj12_reg_mass': 'H_mass',
                    'n_hj_matched': '0',
                    'HVdPhi': 'abs(TVector2::Phi_mpi_pi(H_phi-V_phi))',
                    'jjVPtRatio': 'V_pt/H_pt',
                    'GenBJ1_eta': '-1' if isData else '-1', #'GenJet_eta[Jet_genJetIdx[hJidxCMVA[0]]]',
                    'GenBJ2_eta': '-1' if isData else '-1', #'GenJet_eta[Jet_genJetIdx[hJidxCMVA[1]]]',
                    'GenBJ1_phi': '-1' if isData else '-1', #'GenJet_phi[Jet_genJetIdx[hJidxCMVA[0]]]',
                    'GenBJ2_phi': '-1' if isData else '-1', #'GenJet_phi[Jet_genJetIdx[hJidxCMVA[1]]]',
                    'GenBJ1_pt': '-1' if isData else '-1', #'GenJet_pt[Jet_genJetIdx[hJidxCMVA[0]]]',
                    'GenBJ2_pt': '-1' if isData else '-1', #'GenJet_pt[Jet_genJetIdx[hJidxCMVA[1]]]',
                    'GenBJ1_mass': '-1' if isData else '-1', #'GenJet_mass[Jet_genJetIdx[hJidxCMVA[0]]]',
                    'GenBJ2_mass': '-1' if isData else '-1', #'GenJet_mass[Jet_genJetIdx[hJidxCMVA[1]]]',
                    'isZmm': '(Vtype==0)',
                    'lepInd1': 'vLidx[0]',
                    'lepInd2': 'vLidx[1]',
                    'GenLepIndex1': '-1',
                    'GenLepIndex2': '-1',
                    'n_fsr_jets': '0',
                    }
            if translationDict:
                self.formulas.update(translationDict)
            self.aliases = {
                    }
            self.castToInt = {'hJetInd1': True, 'hJetInd2': True, 'lepInd1': True, 'lepInd2':True, 'GenLepIndex1': True, 'GenLepIndex2': True}
            self.constantArray = {}
            self.castToArray = {'hj1_pt': True, 'hj1_eta':True, 'hj1_phi':True, 'hj1_mass':True, 'hj2_pt': True, 'hj2_eta':True, 'hj2_phi':True, 'hj2_mass':True, 'hj12_pt': True, 'hj12_eta':True, 'hj12_phi':True, 'hj12_mass':True, 'n_fsr_jets': True,'hj1_reg_pt': True, 'hj1_reg_eta':True, 'hj1_reg_phi':True, 'hj1_reg_mass':True, 'hj2_reg_pt': True, 'hj2_reg_eta':True, 'hj2_reg_phi':True, 'hj2_reg_mass':True, 'hj12_reg_pt': True, 'hj12_reg_eta':True, 'hj12_reg_phi':True, 'hj12_reg_mass':True, 'n_hj_matched': True, 'V_eta': True}

            self.branchesToFill = ['hj1_jme_res', 'hj2_jme_res', 'hj1_hh4b_res', 'hj2_hh4b_res']
            for br in self.branchesToFill:
                setattr(self, br, array.array('d', [0.0]))
        
        self.sampleTree = sampleTree
        for alias, target in self.aliases.iteritems():
            self.sampleTree.tree.SetAlias(alias, target)
        for formula, target in self.formulas.iteritems():
            self.sampleTree.addFormula(formula, target)
        self.sysVariations = {}
    
    def createOutputBranch(self, name):
        self.outputBuffers[name] = array.array('d', [0.0])

    def overwriteWithVariation(self, name, formula):
        self.sampleTree.addFormula(formula)
        self.sysVariations[name] = formula

    def __getattr__(self, name):
        if name in self.sysVariations:
            value = array.array('d', [0.0]*self.sampleTree.tree.nJet)
            self.sampleTree.evaluateArray(self.sysVariations[name], value)
            print "==> overwritten with sys variation ", name, " -> ", self.sysVariations[name], " ==>", value
        elif hasattr(self.sampleTree.tree, name):
            value = getattr(self.sampleTree.tree, name)
        elif name in self.sampleTree.formulas:
            value = self.sampleTree.evaluate(name)
        elif name in self.outputBuffers:
            value = self.outputBuffers[name]
        else:
            raise AttributeError

        if name in self.castToInt:
            if name in self.castToArray:
                value = array.array('i', [int(value)])
            else:
                value = int(value)
        else:
            if name in self.castToArray:
                value = array.array('d', [value])
        return value

class kinFitter(AddCollectionsModule):

    def __init__(self, branchName="kinFit", skipBadEvents=False):
        super(kinFitter, self).__init__()
        self.branchName = branchName
        self.skipBadEvents = skipBadEvents

        ep = EventProxy()
        
        # all output vars
        self.all_TREE_VARS = TREE_VARS | set(['twoResolvedJets'])
        ep.init_output(NullTree(), self.all_TREE_VARS) 
        
        # only write those to files which are results from fit
        self.leaves = [x for x in ep.tree_vars if 'fit' in x]
        print "output vars:", self.leaves

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        self.config = initVars['config']

        translationDict = None
        if self.config.has_section('KinematicFit') and self.config.has_option('KinematicFit','translationDict'):
            translationDict = eval(self.config.get('KinematicFit','translationDict'))

        self.wrappedTree = AnalysisToolsTree(self.sampleTree, isData=self.sample.isData(), translationDict=translationDict)
        
        # add separate collection for every sys variation, leaves are the different fit outputs
        self.systematics = ['']
        if not self.sample.isData() and self.config.has_section('KinematicFit') and self.config.has_option('KinematicFit','systematics'):
            self.systematics = eval(self.config.get('KinematicFit','systematics'))

        # add collections for output variables
        self.kinFitterCollection = {}
        for syst in self.systematics:
            self.kinFitterCollection[syst] = Collection(self.branchName + ('_' + syst if syst != '' else ''), self.leaves, leaves=True)
            self.addCollection(self.kinFitterCollection[syst])

        # create buffers for output only branches which don't exist yet
        for var in self.all_TREE_VARS:
            if not hasattr(self.wrappedTree, var):
                self.wrappedTree.createOutputBranch(var)
        
        # load Jet/Met resolution files
        self.jmeResolutionData = 'AnalysisTools/VHbbAnalysis/aux/Spring16_25nsV6_DATA_PtResolution_AK4PFchs.txt'
        self.jmeResolutionMC = 'AnalysisTools/VHbbAnalysis/aux/Spring16_25nsV6_MC_PtResolution_AK4PFchs.txt'
        if self.config.has_section('KinematicFit') and self.config.has_option('KinematicFit','jmeResolutionData'):
            self.jmeResolutionData = self.config.get('KinematicFit','jmeResolutionData')
        if self.config.has_section('KinematicFit') and self.config.has_option('KinematicFit','jmeResolutionMC'):
            self.jmeResolutionData = self.config.get('KinematicFit','jmeResolutionMC')
        self.ak4pfchs_ptres = ROOT.JME.JetResolution(self.jmeResolutionData if self.sample.isData() else self.jmeResolutionMC)

        # fixes
        self.symmetrizeJER = False
        if self.config.has_section('KinematicFit') and self.config.has_option('KinematicFit','symmetrizeJER'):
            self.symmetrizeJER = eval(self.config.get('KinematicFit','symmetrizeJER'))
            print "\x1b[31mINFO: JER variation will be symmetrized!\x1b[0m"

    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            # run kinematic fitter
            c = None
            for syst in self.systematics:
                if not c:
                    c = EventProxy()
                try:
                    # add systematic variations in the tree wrapper class
                    if syst:
                        if self.symmetrizeJER and syst == 'jer_Down':
                            self.wrappedTree.overwriteWithVariation('Jet_PtReg', 'Jet_PtReg*(2.0-Jet_pt_jer_Up/Jet_Pt)')
                            self.wrappedTree.overwriteWithVariation('Jet_mass', 'Jet_mass_nom*(2.0-Jet_mass_jer_Up/Jet_mass)*Jet_bReg')
                        else:
                            self.wrappedTree.overwriteWithVariation('Jet_PtReg', 'Jet_PtReg*Jet_pt_' + syst + '/Jet_Pt')
                            self.wrappedTree.overwriteWithVariation('Jet_mass', 'Jet_mass_' + syst + '*Jet_bReg')
                    else:
                        self.wrappedTree.overwriteWithVariation('Jet_PtReg', 'Jet_PtReg')
                        self.wrappedTree.overwriteWithVariation('Jet_mass', 'Jet_mass_nom*Jet_bReg')

                    # update EventProxy with event data from wrapped tree
                    c.set_event(self.wrappedTree)

                    # run the fit
                    apply_fit_to_event(c, self.ak4pfchs_ptres)
                except Exception as e:
                    print "\x1b[31mEXCEPTION:",e,"\x1b[0m"
                    if self.skipBadEvents:
                        return False
                    else:
                        raise Exception("KinFitException")

                #print 'syst=',syst, ' H_mass', c.H_mass, "-->", c.H_mass_fit[0]

                # write output branches
                for i, leaf in enumerate(self.leaves):
                    leafValue = getattr(c, leaf)
                    self.kinFitterCollection[syst].setProperty(leaf, leafValue[0] if type(leafValue) == array.array else leafValue)

        return True
