#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo

import os,sys,pickle

class MvaTrainingHelper(object):

    def __init__(self, config, mvaName):
        self.config = config
        self.factoryname = config.get('factory', 'factoryname')
        self.factorysettings = config.get('factory', 'factorysettings')
        self.samplesPath = config.get('Directories', 'MVAin')
        self.samplesDefinitions = config.get('Directories','samplesinfo') 
        self.samplesInfo = ParseInfo(self.samplesDefinitions, self.samplesPath)

        self.sampleFilesFolder = config.get('Directories', 'samplefiles')

        self.treeVarSet = config.get(mvaName, 'treeVarSet')
        self.MVAtype = config.get(mvaName, 'MVAtype')
        self.MVAsettings = config.get(mvaName,'MVAsettings')
        self.mvaName = mvaName

        VHbbNameSpace = config.get('VHbbNameSpace', 'library')
        ROOT.gSystem.Load(VHbbNameSpace)

        # variables
        self.MVA_Vars = {}
        self.MVA_Vars['Nominal'] = config.get(self.treeVarSet, 'Nominal').strip().split(' ')

        # samples
        backgroundSampleNames = eval(config.get(mvaName, 'backgrounds'))
        signalSampleNames = eval(config.get(mvaName, 'signals'))
        self.samples = {
            'BKG': self.samplesInfo.get_samples(backgroundSampleNames),
            'SIG': self.samplesInfo.get_samples(signalSampleNames),
        }

        self.treeCutName = config.get(mvaName, 'treeCut')
        self.treeCut = config.get('Cuts', self.treeCutName)

        self.TrainCut = config.get('Cuts', 'TrainCut') 
        self.EvalCut = config.get('Cuts', 'EvalCut')
        print("TRAINING CUT:", self.TrainCut)
        print("EVAL CUT:", self.EvalCut)

        self.globalRescale = 2.0
        
        self.trainingOutputFileName = 'mvatraining_{factoryname}_{region}.root'.format(factoryname=self.factoryname, region=mvaName)
        self.trainingOutputFile = ROOT.TFile.Open(self.trainingOutputFileName, "RECREATE")

        # ----------------------------------------------------------------------------------------------------------------------
        # create TMVA factory
        # ----------------------------------------------------------------------------------------------------------------------
        self.factory = ROOT.TMVA.Factory(self.factoryname, self.trainingOutputFile, self.factorysettings)
        if self.trainingOutputFile and self.factory:
            print ("INFO: initialized MvaTrainingHelper.", self.factory) 
        else:
            print ("\x1b[31mERROR: initialization of MvaTrainingHelper failed!\x1b[0m") 


    def prepare(self):
        # ----------------------------------------------------------------------------------------------------------------------
        # add sig/bkg x training/eval trees
        # ----------------------------------------------------------------------------------------------------------------------
        try:
            addBackgroundTreeMethod = self.factory.AddBackgroundTree
            addSignalTreeMethod = self.factory.AddSignalTree
            self.dataLoader = None
        except:
            print("oh no..")
            self.dataLoader = ROOT.TMVA.DataLoader("someDataLoaderThingy")
            addBackgroundTreeMethod = self.dataLoader.AddBackgroundTree
            addSignalTreeMethod = self.dataLoader.AddSignalTree

        for addTreeFcn, samples in [
                    [addBackgroundTreeMethod, self.samples['BKG']],
                    [addSignalTreeMethod, self.samples['SIG']]
                ]:
            for sample in samples:
                print ('*'*80,'\n%s\n'%sample,'*'*80)
                for additionalCut in [self.TrainCut, self.EvalCut]:
                    # cuts
                    sampleCuts = [sample.subcut]
                    if additionalCut:
                        sampleCuts.append(additionalCut)
                    # cut from the mva region
                    if self.treeCut:
                        sampleCuts.append(self.treeCut)

                    tc = TreeCache.TreeCache(
                            sample=sample,
                            cutList=sampleCuts,
                            inputFolder=self.samplesPath,
                            config=self.config,
                            debug=True
                        )
                    sampleTree = tc.getTree()
                    if sampleTree:
                        treeScale = sampleTree.getScale(sample) * self.globalRescale
                        if sampleTree.tree.GetEntries() > 0:
                            addTreeFcn(sampleTree.tree, treeScale, ROOT.TMVA.Types.kTraining if additionalCut == self.TrainCut else ROOT.TMVA.Types.kTesting)
                        # HCMVAV2_reg_mass HCMVAV2_reg_pt VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi) Jet_btagCMVAV2[hJCMVAV2idx[0]] Jet_btagCMVAV2[hJCMVAV2idx[1]] hJetCMVAV2_pt_reg_0 hJetCMVAV2_pt_reg_1 V_new_mass Sum$(hJetCMVAV2_pt_reg>30&&abs(Jet_eta)<2.4&&Jet_puId==7&&Jet_id>0&&aJCidx!=(hJCMVAV2idx[0])&&(aJCidx!=(hJCMVAV2idx[1]))) V_new_pt (HCMVAV2_reg_pt/V_new_pt) abs(Jet_eta[hJCMVAV2idx[0]]-Jet_eta[hJCMVAV2idx[1]]) softActivityVH_njets5 VHbb::deltaR(HCMVAV2_reg_eta,HCMVAV2_reg_phi,V_new_eta,V_new_phi) met_pt

                        #sampleTree.addOutputBranches([
                        #        {'name': 'deltaPhiVH' , 'formula': 'VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)'},
                        #        {'name': 'btag0', 'formula': 'Jet_btagCMVAV2[hJCMVAV2idx[0]]'},
                        #        {'name': 'btag1', 'formula': 'Jet_btagCMVAV2[hJCMVAV2idx[1]]'},
                        #        {'name': 'najets', 'formula': 'Sum$(hJetCMVAV2_pt_reg>30&&abs(Jet_eta)<2.4&&Jet_puId==7&&Jet_id>0&&aJCidx!=(hJCMVAV2idx[0])&&(aJCidx!=(hJCMVAV2idx[1])))'},
                        #        {'name': 'ptRatio', 'formula': 'HCMVAV2_reg_pt/V_new_pt'},
                        #        {'name': 'ptBalance', 'formula': 'HCMVAV2_reg_pt-V_new_pt'},
                        #        {'name': 'deltaEtaBB', 'formula': 'abs(Jet_eta[hJCMVAV2idx[0]]-Jet_eta[hJCMVAV2idx[1]])'},
                        #        {'name': 'deltaRVH', 'formula': 'VHbb::deltaR(HCMVAV2_reg_eta,HCMVAV2_reg_phi,V_new_eta,V_new_phi)'},
                        #        {'name': 'deltaEtaVH', 'formula': 'abs(HCMVAV2_reg_eta-V_new_eta)'},
                        #        {'name': 'deltaRBB', 'formula': 'VHbb::deltaR(Jet_eta[hJCMVAV2idx[0]],Jet_phi[hJCMVAV2idx[0]],Jet_eta[hJCMVAV2idx[1]],Jet_phi[hJCMVAV2idx[1]])'},
                        #    ])
                        #sampleTree.addOutputTree('/scratch/berger_p2/'+ ('training_' if additionalCut == self.TrainCut else 'evaluation_' ) + sample.identifier + '.root', cut='1', branches='*')
                        #sampleTree.process()
                    else:
                        print ("\x1b[31mERROR: TREE NOT FOUND:", sample.name, " -> not cached??\x1b[0m")
                        raise Exception("CachedTreeMissing")

        if self.dataLoader:
            for var in self.MVA_Vars['Nominal']:
                self.dataLoader.AddVariable(var, 'D')
        else:
            for var in self.MVA_Vars['Nominal']:
                self.factory.AddVariable(var, 'D')

        return self

    def run(self):
        # ----------------------------------------------------------------------------------------------------------------------
        # Execute TMVA
        # ----------------------------------------------------------------------------------------------------------------------
        self.factory.Verbose()
        print ('Execute TMVA: factory.BookMethod("%s", "%s", "%s")'%(self.MVAtype, self.mvaName, self.MVAsettings))
        try:
            self.factory.BookMethod(self.MVAtype, self.mvaName, self.MVAsettings)
        except:
            print(">_<")
            self.factory.BookMethod(self.dataLoader, self.MVAtype, self.mvaName, self.MVAsettings)
        print ('Execute TMVA: TrainAllMethods')
        self.factory.TrainAllMethods()
        print ('Execute TMVA: TestAllMethods')
        self.factory.TestAllMethods()
        print ('Execute TMVA: EvaluateAllMethods')
        self.factory.EvaluateAllMethods()
        print ('Execute TMVA: output.Write')
        self.trainingOutputFile.Close()
        return self

    def printInfo(self):
        #WRITE INFOFILE
        MVAdir = self.config.get('Directories','vhbbpath')+'/python/weights/'
        infofile = open(MVAdir+self.factoryname+'_'+self.mvaName+'.info','w')
        print ('@DEBUG: output infofile name')
        print (infofile)

        info=mvainfo(self.mvaName)
        info.factoryname=self.factoryname
        info.factorysettings=self.factorysettings
        info.MVAtype=self.MVAtype
        info.MVAsettings=self.MVAsettings
        info.weightfilepath=MVAdir
        info.path=self.samplesPath
        info.varset=self.treeVarSet
        info.vars=self.MVA_Vars['Nominal']
        pickle.dump(info,infofile)
        infofile.close()

# read arguments
argv = sys.argv
parser = OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                          help="Verbose mode.")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration file")
parser.add_option("-t","--trainingRegions", dest="trainingRegions", default='',
                      help="cut region identifier")
(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = ["config"]

# Import after configure to get help message
from myutils import BetterConfigParser, mvainfo, ParseInfo

# load config
config = BetterConfigParser()
config.read(opts.config)

# initialize
trainingRegions = opts.trainingRegions.split(',')
if len(trainingRegions) > 1:
    print ("ERROR: not implemented!")
    exit(1)
for trainingRegion in trainingRegions:
    th = MvaTrainingHelper(config=config, mvaName=trainingRegion)
    th.prepare().run()
    th.printInfo()

