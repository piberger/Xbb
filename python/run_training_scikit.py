#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)
from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils import BetterConfigParser, ParseInfo
import resource
import os
import sys
import pickle
import glob
import shutil
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.ensemble import ExtraTreesClassifier 
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib
import datetime
import hashlib

class MvaTrainingHelper(object):

    def __init__(self, config, mvaName):
        self.config = config
        self.samplesPath = config.get('Directories', 'MVAin')
        self.samplesDefinitions = config.get('Directories','samplesinfo') 
        self.samplesInfo = ParseInfo(self.samplesDefinitions, self.samplesPath)
        self.sampleFilesFolder = config.get('Directories', 'samplefiles')
        self.logpath = config.get('Directories', 'logpath')
        self.treeVarSet = config.get(mvaName, 'treeVarSet')
        self.mvaName = mvaName
        self.MVAsettings = config.get(mvaName,'MVAsettings')
        self.factoryname = 'scikit-test1'

        VHbbNameSpace = config.get('VHbbNameSpace', 'library')
        ROOT.gSystem.Load(VHbbNameSpace)

        # variables
        self.MVA_Vars = {}
        self.MVA_Vars['Nominal'] = config.get(self.treeVarSet, 'Nominal').strip().split(' ')

        # samples
        self.backgroundSampleNames = eval(config.get(mvaName, 'backgrounds'))
        self.signalSampleNames = eval(config.get(mvaName, 'signals'))
        self.samples = {
            'BKG': self.samplesInfo.get_samples(self.backgroundSampleNames),
            'SIG': self.samplesInfo.get_samples(self.signalSampleNames),
        }

        self.treeCutName = config.get(mvaName, 'treeCut')
        self.treeCut = config.get('Cuts', self.treeCutName)

        self.trainCut = config.get('Cuts', 'TrainCut') 
        self.evalCut = config.get('Cuts', 'EvalCut')
        print("TRAINING CUT:", self.trainCut)
        print("TEST CUT:", self.evalCut)

        self.globalRescale = 2.0
        
        self.trainingOutputFileName = 'mvatraining_{factoryname}_{region}.root'.format(factoryname=self.factoryname, region=mvaName)
        self.trainingOutputFile = ROOT.TFile.Open(self.trainingOutputFileName, "RECREATE")

        self.parameters = {
                'factoryname': self.factoryname,
                'mvaName': self.mvaName,
                'MVAregionCut': self.treeCutName + ': ' + self.treeCut,
                #'classifier': 'GradientBoostingClassifier',
                'classifier': 'RandomForestClassifier',
                'max_depth': None,
                'max_leaf_nodes': None,
                'class_weight': 'balanced',
                #'criterion': 'friedman_mse',
                'criterion': 'gini',
                #'n_estimators': 3000,
                'n_estimators': 100,
                'learning_rate': 0.07,
                'algorithm': 'SAMME.R',
                'min_samples_leaf': 50,
                'splitter': 'best',
                'max_features': 5,
                'subsample': 0.6,
                'limit': -1,
                'additional_signal_weight': 1.0,
                'min_impurity_split': 0.3,
                'bootstrap': True,
                }

        for mvaSetting in self.MVAsettings.split(':'):
             self.parameters[mvaSetting.split('=')[0].strip()] = eval(mvaSetting.split('=')[1].strip())

    def loadCachedNumpyArrays(self, cachedFilesPath):
        cached = True
        try:
            with open(cachedFilesPath + '/scikit_inputDataTraining.dmp', 'rb') as outputFile:
                self.inputDataTraining = pickle.load(outputFile)
            with open(cachedFilesPath + '/scikit_targetsTraining.dmp', 'rb') as outputFile:
                self.targetsTraining = pickle.load(outputFile)
            with open(cachedFilesPath + '/scikit_weightsTraining.dmp', 'rb') as outputFile:
                self.weightsTraining = pickle.load(outputFile)
            with open(cachedFilesPath + '/scikit_weightsTraining.dmp', 'rb') as outputFile:
                self.weightsTrainingOriginal = pickle.load(outputFile)
            with open(cachedFilesPath + '/scikit_inputDataTest.dmp', 'rb') as outputFile:
                self.inputDataTest = pickle.load(outputFile)
            with open(cachedFilesPath + '/scikit_targetsTest.dmp', 'rb') as outputFile:
                self.targetsTest = pickle.load(outputFile)
            with open(cachedFilesPath + '/scikit_weightsTest.dmp', 'rb') as outputFile:
                self.weightsTest = pickle.load(outputFile)
            print("loaded cached files!!")
        except:
            cached = False
        return cached

    def writeNumpyArrays(self, cachedFilesPath):
        with open(cachedFilesPath + '/scikit_inputDataTraining.dmp', 'wb') as outputFile:
            pickle.dump(self.inputDataTraining, outputFile)
        with open(cachedFilesPath + '/scikit_targetsTraining.dmp', 'wb') as outputFile:
            pickle.dump(self.targetsTraining, outputFile)
        with open(cachedFilesPath + '/scikit_weightsTraining.dmp', 'wb') as outputFile:
            pickle.dump(self.weightsTraining, outputFile)
        with open(cachedFilesPath + '/scikit_inputDataTest.dmp', 'wb') as outputFile:
            pickle.dump(self.inputDataTest, outputFile)
        with open(cachedFilesPath + '/scikit_targetsTest.dmp', 'wb') as outputFile:
            pickle.dump(self.targetsTest, outputFile)
        with open(cachedFilesPath + '/scikit_weightsTest.dmp', 'wb') as outputFile:
            pickle.dump(self.weightsTest, outputFile)

    def getCachedNumpyArrayPath(self):
        identifier = self.treeCut + '__VAR:' + ' '.join(self.MVA_Vars['Nominal']) + '__SIG:' + '/'.join(self.signalSampleNames) + '__BKG:' + '/'.join(self.backgroundSampleNames)
        varsHash = hashlib.sha224(identifier).hexdigest()
        cachedFilesPath = self.logpath + '/../cache/' + varsHash + '/'
        return cachedFilesPath

    def getHash(self):
        identifier = self.treeCut + '__VAR:' + ' '.join(self.MVA_Vars['Nominal']) + '__SIG:' + '/'.join(self.signalSampleNames) + '__BKG:' + '/'.join(self.backgroundSampleNames) + '__PAR:%r'%self.parameters
        return hashlib.sha224(identifier).hexdigest()[:8]

    def prepare(self):
        # ----------------------------------------------------------------------------------------------------------------------
        # add sig/bkg x training/eval trees
        # ----------------------------------------------------------------------------------------------------------------------
        self.sampleTrees = []
        categories = ['BKG', 'SIG']
        datasetParts = {'train': self.trainCut, 'eval': self.evalCut}

        cachedFilesPath = self.getCachedNumpyArrayPath() 
        try:
            os.makedirs(cachedFilesPath)
        except:
            pass
        
        # load numpy arrays from disk if they have been already created
        if self.loadCachedNumpyArrays(cachedFilesPath):
            return self

        arrayLists = {datasetName:[] for datasetName in datasetParts.iterkeys()}
        weightLists = {datasetName:[] for datasetName in datasetParts.iterkeys()}
        targetLists = {datasetName:[] for datasetName in datasetParts.iterkeys()}

        for category in categories:

            #if len(self.samples[category]) > 10:
            #    self.samples[category] = self.samples[category][:10]
            for sample in self.samples[category]:
                print ('*'*80,'\n%s\n'%sample,'*'*80)
                for datasetName, additionalCut in datasetParts.iteritems():
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
                        print ('scale:', treeScale)
                        
                        # initialize numpy array
                        nSamples = sampleTree.GetEntries()
                        features = self.MVA_Vars['Nominal']
                        nFeatures = len(features) 
                        print('nFeatures:', nFeatures)
                        inputData = np.zeros((nSamples, nFeatures), dtype=np.float32)

                        # initialize formulas for ROOT tree
                        for feature in features:
                            sampleTree.addFormula(feature, feature)

                        # fill numpy array from ROOT tree
                        for i, event in enumerate(sampleTree):
                            for j, feature in enumerate(features):
                                inputData[i, j] = sampleTree.evaluate(feature)

                        print(inputData)
                        arrayLists[datasetName].append(inputData)

                        #TODO: below
                        for i in range(nSamples):
                            weightLists[datasetName].append(treeScale)
                            targetLists[datasetName].append(categories.index(category))
                    else:
                        print ("\x1b[31mERROR: TREE NOT FOUND:", sample.name, " -> not cached??\x1b[0m")
                        raise Exception("CachedTreeMissing")

        # TODO: store weights and data in a single structure!
        
        # concatenate all data from different samples
        self.inputDataTraining = np.concatenate(arrayLists['train'], axis=0)
        self.targetsTraining = np.array(targetLists['train'], dtype=np.float32) 
        self.weightsTraining = np.array(weightLists['train'], dtype=np.float32)
        self.weightsTrainingOriginal = np.array(weightLists['train'], dtype=np.float32)

        self.inputDataTest = np.concatenate(arrayLists['eval'], axis=0)
        self.targetsTest = np.array(targetLists['eval'], dtype=np.float32) 
        self.weightsTest = np.array(weightLists['eval'], dtype=np.float32)
        
        # write numpy arrays to disk
        self.writeNumpyArrays(cachedFilesPath)

        return self

    def run(self):

        applyClassWeights = False
        if self.parameters['classifier'] == 'GradientBoostingClassifier':
            clf = GradientBoostingClassifier(
                    min_samples_leaf=self.parameters['min_samples_leaf'], 
                    max_depth=self.parameters['max_depth'], 
                    max_leaf_nodes=self.parameters['max_leaf_nodes'],
                    criterion=self.parameters['criterion'],
                    max_features=self.parameters['max_features'],
                    n_estimators=self.parameters['n_estimators'], 
                    learning_rate=self.parameters['learning_rate'], 
                    subsample=self.parameters['subsample'],
                    min_impurity_split=self.parameters['min_impurity_split'],
                )
            if self.parameters['class_weight'] == 'balanced':
                applyClassWeights = True
        elif self.parameters['classifier'] == 'RandomForestClassifier':
            clf = RandomForestClassifier(
                    min_samples_leaf=self.parameters['min_samples_leaf'], 
                    max_depth=self.parameters['max_depth'], 
                    max_leaf_nodes=self.parameters['max_leaf_nodes'],
                    criterion=self.parameters['criterion'],
                    max_features=self.parameters['max_features'],
                    n_estimators=self.parameters['n_estimators'], 
                    bootstrap=self.parameters['bootstrap'],
                )
            if self.parameters['class_weight'] == 'balanced':
                applyClassWeights = True
        elif self.parameters['classifier'] == 'ExtraTreesClassifier':
            clf = ExtraTreesClassifier(
                    min_samples_leaf=self.parameters['min_samples_leaf'], 
                    max_depth=self.parameters['max_depth'], 
                    max_leaf_nodes=self.parameters['max_leaf_nodes'],
                    criterion=self.parameters['criterion'],
                    max_features=self.parameters['max_features'],
                    n_estimators=self.parameters['n_estimators'], 
                    bootstrap=self.parameters['bootstrap'],
                )
            if self.parameters['class_weight'] == 'balanced':
                applyClassWeights = True
        elif self.parameters['classifier'] == 'FT_GradientBoostingClassifier':
            rt = RandomTreesEmbedding(max_depth=3, n_estimators=20, random_state=0)
            clf0 = GradientBoostingClassifier(
                    min_samples_leaf=self.parameters['min_samples_leaf'], 
                    max_depth=self.parameters['max_depth'], 
                    max_leaf_nodes=self.parameters['max_leaf_nodes'],
                    criterion=self.parameters['criterion'],
                    max_features=self.parameters['max_features'],
                    n_estimators=self.parameters['n_estimators'], 
                    learning_rate=self.parameters['learning_rate'], 
                    subsample=self.parameters['subsample'],
                    min_impurity_split=self.parameters['min_impurity_split'],
                )
            if self.parameters['class_weight'] == 'balanced':
                applyClassWeights = True
            clf = make_pipeline(rt, clf0)
        else:
            clf = AdaBoostClassifier(
                    DecisionTreeClassifier(
                        min_samples_leaf=self.parameters['min_samples_leaf'], 
                        max_depth=self.parameters['max_depth'], 
                        class_weight=self.parameters['class_weight'], 
                        criterion=self.parameters['criterion'],
                        splitter=self.parameters['splitter'],
                        max_features=self.parameters['max_features'],
                        ), 
                    n_estimators=self.parameters['n_estimators'], 
                    learning_rate=self.parameters['learning_rate'], 
                    algorithm=self.parameters['algorithm'],
                )

        print("traning data shape:", self.inputDataTraining.shape)
        print("traning weights shape:", self.weightsTraining.shape)
        print("traning targets shape:", self.targetsTraining.shape)
       
        if (self.inputDataTraining.shape[0] != self.weightsTraining.shape[0] or self.weightsTraining.shape[0] != self.targetsTraining.shape[0]):
            print ("\x1b[31mERROR: training input data array shapes are incompatible!\x1b[0m")
            raise Exception("BadTrainingInputData")

        # SHUFFLE all samples before
        print("shuffle input data...")
        nSamples = self.inputDataTraining.shape[0]
        nFeatures = self.inputDataTraining.shape[1]
        randomPermutation = np.random.permutation(nSamples)
        np.take(self.inputDataTraining, randomPermutation, axis=0, out=self.inputDataTraining)
        np.take(self.weightsTraining, randomPermutation, axis=0, out=self.weightsTraining)
        np.take(self.targetsTraining, randomPermutation, axis=0, out=self.targetsTraining)

        # LIMIT number of training samples
        limitNumTrainingSamples = self.parameters['limit']
        if (limitNumTrainingSamples > 0):
            print("limit training samples to:", limitNumTrainingSamples)
            self.inputDataTraining = self.inputDataTraining[0:limitNumTrainingSamples]
            self.weightsTraining = self.weightsTraining[0:limitNumTrainingSamples]
            self.targetsTraining = self.targetsTraining[0:limitNumTrainingSamples]
        
        # calculate total weights and class_weights
        nSig = len([x for x in self.targetsTraining if x > 0.5])
        nBkg = len([x for x in self.targetsTraining if x < 0.5])
        print("#SIG:", nSig)
        print("#BKG:", nBkg)
        weightsSignal = []
        weightsBackground = []
        for i in range(len(self.weightsTraining)):
            if self.targetsTraining[i] < 0.5:
                weightsBackground.append(self.weightsTraining[i])
            else:
                weightsSignal.append(self.weightsTraining[i])
        weightsSignal.sort()
        weightsBackground.sort()
        totalWeightSignal = sum(weightsSignal)
        totalWeightBackground = sum(weightsBackground)
        signalReweight = (totalWeightSignal+totalWeightBackground)/totalWeightSignal * self.parameters['additional_signal_weight'] 
        backgroundReweight = (totalWeightSignal+totalWeightBackground)/totalWeightBackground
        print("SUM of weights for signal:", totalWeightSignal)
        print("SUM of weights for background:", totalWeightBackground)
        
        if applyClassWeights:
            print("re-weight signals by:", signalReweight) 
            print("re-weight background by:", backgroundReweight) 
            for i in range(len(self.weightsTraining)):
                if self.targetsTraining[i] < 0.5:
                    self.weightsTraining[i] *= backgroundReweight 
                else:
                    self.weightsTraining[i] *= signalReweight 
        else:
            print("DO NOT re-weight signals by:", signalReweight) 
            print("DO NOT re-weight background by:", backgroundReweight)
        
        param_grid = {'learning_rate': [0.5, 0.8, 1.0],
                      'n_estimators': [50, 200, 500, 1000],
                      'base_estimator__max_depth': [3, 4, 5],
                      'base_estimator__min_weight_fraction_leaf': [0.0, 0.01],
                      'base_estimator__criterion': ['gini', 'entropy'],
                     }
        
        #gs_clf = GridSearchCV(clf, param_grid, verbose=3, fit_params={'sample_weight': self.weightsTraining}).fit(self.inputDataTraining, self.targetsTraining)
        #print("BEST PARAMETERS:", gs_clf.best_params_)
        #print("fitting...")

        # TRAINING
        clf = clf.fit(self.inputDataTraining, self.targetsTraining, self.weightsTraining)
        print("*****")

        # TEST
        results = clf.predict_proba(self.inputDataTest)
        results_train = clf.predict_proba(self.inputDataTraining)

        # rescaling of SCORE to [0, 1]
        minProb = 2.0
        maxProb = -1.0
        for i in range(len(self.inputDataTraining)):
            if results_train[i][1] > maxProb:
                maxProb = results_train[i][1]
            if results_train[i][1] < minProb:
                minProb = results_train[i][1]
        for i in range(len(self.inputDataTest)):
            if results[i][1] > maxProb:
                maxProb = results[i][1]
            if results[i][1] < minProb:
                minProb = results[i][1]
            
        # fill TRAINING SCORE histogram (class probability)
        h1t = ROOT.TH1D("h1t","h1t",100,0.0,1.0)
        h2t = ROOT.TH1D("h2t","h2t",100,0.0,1.0)
        for i in range(len(self.inputDataTraining)):
            result = (results_train[i][1]-minProb)/(maxProb-minProb) 
            weight = self.weightsTrainingOriginal[i]
            if self.targetsTraining[i] == 0:
                h1t.Fill(result, weight)
            else:
                h2t.Fill(result, weight)

        # fill TEST SCORE histogram (class probability)
        h1 = ROOT.TH1D("h1","h1",100,0.0,1.0)
        h2 = ROOT.TH1D("h2","h2",100,0.0,1.0)
        for i in range(len(self.inputDataTest)):
            if i % 10000 == 0:
                print ("step ", i)
            try:
                result = (results[i][1]-minProb)/(maxProb-minProb) 
                weight = self.weightsTest[i]
                if self.targetsTest[i] == 0:
                    h1.Fill(result, weight)
                else:
                    h2.Fill(result, weight)
            except Exception as e:
                print(e)
                pass

        timestamp = str(datetime.datetime.now()).split('.')[0].replace(' ','_').replace(':','-') + '_' + self.getHash()
        
        # ROC curve
        print("calculating auc...")
        auc = roc_auc_score(self.targetsTest, results[:,1], sample_weight=self.weightsTest)
        print("AUC:", auc)
        try:
            fpr, tpr, thresholds = roc_curve(self.targetsTest, results[:,1], sample_weight=self.weightsTest)
            print("fpr:",fpr)
            tgr = ROOT.TGraph(len(fpr), fpr, tpr)
            c1=ROOT.TCanvas("c1","c1",500,500)
            tgr.Draw("AL")
            tgr.GetXaxis().SetTitle('false positive rate')
            tgr.GetYaxis().SetTitle('true positive rate')
            tgr.SetTitle("ROC curve (AUC=%1.3f)"%auc)

            fpr_train, tpr_train, thresholds_train = roc_curve(self.targetsTraining, results_train[:,1], sample_weight=self.weightsTraining)
            tgr_train = ROOT.TGraph(len(fpr_train), fpr_train, tpr_train)
            tgr_train.SetLineStyle(2)
            tgr_train.SetLineColor(ROOT.kOrange+2)
            tgr_train.Draw("SAME L")

            c1.SaveAs(self.logpath + '/scikit_comp_bdt_roc_' + timestamp + '.png')
            c1.SaveAs(self.logpath + '/scikit_comp_bdt_roc_' + timestamp + '.root')
        except Exception as e:
            print(e)
    

        h1.Scale(1.0/h1.Integral())
        h2.Scale(1.0/h2.Integral())
        h1t.Scale(1.0/h1t.Integral())
        h2t.Scale(1.0/h2t.Integral())
        
        maximum = max(h1.GetBinContent(h1.GetMaximumBin()), h2.GetBinContent(h2.GetMaximumBin()),h1t.GetBinContent(h1t.GetMaximumBin()),h2t.GetBinContent(h2t.GetMaximumBin()))
        h2.SetLineColor(ROOT.kRed)
        c1=ROOT.TCanvas("c1","c1",500,500)
        h1t.SetFillStyle( 3001)
        h1t.GetYaxis().SetRangeUser(0,1.1*maximum)
        h1t.SetFillColorAlpha(ROOT.kBlue-6, 0.5)
        h1t.SetLineColorAlpha(ROOT.kBlue-6, 0.5)
        h2t.SetFillStyle( 3001)
        h2t.SetFillColorAlpha(ROOT.kOrange-3, 0.5)
        h2t.SetLineColorAlpha(ROOT.kOrange-3, 0.5)
        h1t.SetTitle("Overtraining check") 
        h1t.Draw("hist")
        h2t.Draw("hist;same")
        h1.Draw("hist;same")
        h2.Draw("hist;same")

        c1.SaveAs(self.logpath + '/scikit_comp_bdt_' + timestamp + '.png')
        c1.SaveAs(self.logpath + '/scikit_comp_bdt_' + timestamp + '.root')

        html = ['<html><head></head><body>']
        html.append('<h3>' + timestamp + '</h3>')
        html.append('<img src="scikit_comp_bdt_' + timestamp + '.png' + '">')
        html.append('<img src="scikit_comp_bdt_roc_' + timestamp + '.png' + '">')
        html.append('<br>')
        for k,v in sorted(self.parameters.iteritems()):
            html.append('<b>' + k + '</b>: ' + '%r<br>'%v)
        html.append('<b>nSig</b>: ' + '%r<br>'%nSig)
        html.append('<b>nBkg</b>: ' + '%r<br>'%nBkg)
        html.append('<b>limitNumTrainingSamples</b>: ' + '%r<br>'%limitNumTrainingSamples)
        html.append('<b>AUC</b>: ' + '%r<br>'%auc)

        fprStepsForEfficiencies = [0.01, 0.05, 0.1, 0.2, 0.5]
        fprStepCounter = 0
        for i in range(len(fpr)):
            if fpr[i] > fprStepsForEfficiencies[fprStepCounter]:
                html.append('<b>FPR=%f</b>: '%fpr[i] + 'TPR=%f<br>'%tpr[i])
                fprStepCounter += 1
                if fprStepCounter>= len(fprStepsForEfficiencies):
                    break
        
        tprStepsForEfficiencies = [0.1, 0.2, 0.5, 0.75, 0.9, 0.95, 0.99]
        tprStepCounter = 0
        for i in range(len(tpr)):
            if tpr[i] > tprStepsForEfficiencies[tprStepCounter]:
                html.append('<b>TPR=%f</b>: '%tpr[i] + 'FPR=%f<br>'%fpr[i])
                tprStepCounter += 1
                if tprStepCounter>= len(tprStepsForEfficiencies):
                    break
        
        print("feature importances:")
        maxImportance = max(clf.feature_importances_)
        html.append("<h4>feature importance:</h4>")
        importanceList = []
        for i, v in enumerate(self.MVA_Vars['Nominal']):
            importanceList.append({'feature': v, 'importance': clf.feature_importances_[i]})
        importanceList.sort(key=lambda x:x['importance'], reverse=True)
        html.append('<table>')
        for d in importanceList:
            print((d['feature']+":").ljust(50), d['importance'])
            if len(d['feature']) > 60:
                d['feature'] = d['feature'][:60] + '...'
            html.append("<tr><td style='width:600px;overflow:hidden;'><b>{feature}</b></td><td style='width:100px;'>{importance}</td><td style='width:520px;'><div style='width:{barWidth}px;height:20px;background-color:#226;color:white'> {relImportance}</div></td></tr>".format(feature=d['feature'], importance=d['importance'], relImportance=round(100.0*d['importance']/maxImportance,1), barWidth=d['importance']/maxImportance*500))
        html.append('</table>')

        try:
            print(clf.oob_improvement_)
        except:
            pass

        html.append('</body></html>')
        with open(self.logpath + '/scikit_comp_bdt_' + timestamp + '.html', 'w') as outputfile:
            outputfile.write('\n'.join(html))

        #tree.export_graphviz(clf, out_file='tree.gpv')
        #self.config.get('Directories','vhbbpath')+'/python/weights/'

        classifierOutputPath = self.getCachedNumpyArrayPath()
        joblib.dump(clf, classifierOutputPath + '/clf.pkl') 

        return self

    def printInfo(self):
        print("not implemented")

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

