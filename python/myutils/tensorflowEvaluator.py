#!/usr/bin/env python
import ROOT
import array
from Jet import Jet
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import sys
sys.path.append("..")
sys.path.append("../tfZllDNN/")
sys.path.append("../tfVHbbDNN/")

# tfZllDNN repository has to be cloned inside the python folder
from tfVHbbDNN.tfDNNclassifier import TensorflowDNNClassifier as TensorflowDNNClassifier_new
try:
    from tfZllDNN.TensorflowDNNClassifier import TensorflowDNNClassifier as TensorflowDNNClassifier_old
    TensorflowDNNClassifier = TensorflowDNNClassifier_old
except:
    print "WARNING: only NEW(version==2) DNN training code found, legacy files can't be read!"
    TensorflowDNNClassifier = TensorflowDNNClassifier_new

from MyStandardScaler import StandardScaler
import numpy as np
import pickle

# reads tensorflow checkpoints and applies DNN output to ntuples,
# including variations from systematic uncertainties
# needs: tensorflow >=1.4
class tensorflowEvaluator(AddCollectionsModule):

    def __init__(self, mvaName, nano=False, version=2):
        self.mvaName = mvaName
        self.nano = nano
        self.debug = False
        # version>1 uses new cleaned up code, version=1 uses legacy code
        self.version = version
        if self.version > 1:
            global TensorflowDNNClassifier,TensorflowDNNClassifier_new
            TensorflowDNNClassifier = TensorflowDNNClassifier_new
            print "INFO: new version:", self.version
        super(tensorflowEvaluator, self).__init__()

    def customInit(self, initVars):
        self.config = initVars['config']
        self.sampleTree = initVars['sampleTree']
        self.sample = initVars['sample']
        self.tensorflowConfig = self.config.get(self.mvaName, 'tensorflowConfig')
        self.scalerDump = self.config.get(self.mvaName, 'scalerDump')
        self.checkpoint = self.config.get(self.mvaName, 'checkpoint')
        self.branchName = self.config.get(self.mvaName, 'branchName')
        self.signalIndex = 0
        if self.config.has_option(self.mvaName, 'signalIndex'):
            self.signalIndex = int(self.config.get(self.mvaName, 'signalIndex'))
        try:
            self.nClasses = int(self.config.get(self.mvaName, 'nClasses'))
        except Exception as e:
            print "exception:",e
            self.nClasses = 1
        self.classes = eval(self.config.get(self.mvaName, 'classes')) if self.config.has_option(self.mvaName, 'classes') else None
        self.nFeatures = len(self.config.get(self.config.get(self.mvaName, "treeVarSet"), "Nominal").strip().split(" "))
        self.signalClassIds = [self.signalIndex]
        if self.classes:
            self.signalClassIds = [x for x,y in enumerate(self.classes) if y[0].startswith('SIG')]
            print "INFO: signals:", self.signalClassIds
        self.classMultiplier = eval(self.config.get(self.mvaName, 'classMultiplier')) if self.config.has_option(self.mvaName, 'classMultiplier') else None

        print "\x1b[31mnum categories:", self.nClasses, "\x1b[0m"

        # Jet systematics
        self.systematics = self.config.get('systematics', 'systematics').split(' ')
        
        self.dnnCollections = []
        # additional pre-computed values for multi-classifiers

        for i in range(self.nClasses):
            # create output branches
            collectionName = self.branchName if self.nClasses==1 else self.branchName + "_%d"%i
            self.dnnCollection = Collection(collectionName, self.systematics, leaves=True) 
            self.addCollection(self.dnnCollection)
            self.dnnCollections.append(self.dnnCollection)

        # create formulas for input variables
        self.inputVariables = {}
        for syst in self.systematics:
            self.inputVariables[syst] = self.config.get(self.config.get(self.mvaName, "treeVarSet"), syst if self.sample.isMC() else 'Nominal').split(' ')
            for var in self.inputVariables[syst]:
                self.sampleTree.addFormula(var)
        
        if self.nClasses > 1:
            self.dnnCollectionsMulti = {
                        'argmax' : Collection(self.branchName + "_argmax", self.systematics, leaves=True),
                        'max'    : Collection(self.branchName + "_max",    self.systematics, leaves=True),
                        'max2'   : Collection(self.branchName + "_max2",   self.systematics, leaves=True),  
                        'signal' : Collection(self.branchName + "_signal", self.systematics, leaves=True),
                        'default': Collection(self.branchName,   self.systematics, leaves=True),
                    }

            for k,v in self.dnnCollectionsMulti.items(): 
                self.addCollection(v)

        # create tensorflow graph
        self.reloadModel()

    # read network architecture/hyper parameters from *.cfg file
    def loadModelConfig(self):
        with open(self.tensorflowConfig, 'r') as inputFile:
            lines = inputFile.read()
        print("INFO: read config parameters from", self.tensorflowConfig)
        return eval(lines)

    # rebuild tensorflow graph
    def reloadModel(self):
        self.parameters = self.loadModelConfig()

        # initialize arrays for transfering data to graph
        self.data = {'test':{
                                'X': np.full((len(self.systematics), self.nFeatures), 0.0, dtype=np.float32),
                                'y': np.full((len(self.systematics),), 1.0, dtype=np.float32),
                                'sample_weight': np.full((len(self.systematics),), 1.0, dtype=np.float32),
                            }
                    }


        # for evaluation of weights always set limitResources=True which limits threads (and therefore memory)
        self.clf = TensorflowDNNClassifier(parameters=self.parameters, nFeatures=len(self.inputVariables[self.systematics[0]]), limitResources=True, nClasses=self.nClasses if self.nClasses>1 else 2)
        self.clf.evaluationOnly = True
        if self.version > 1:
            self.clf.setInputs(self.data)
        self.clf.buildModel()

        # restore rom checkpoint
        self.clf.restore(self.checkpoint)
        with open(self.scalerDump, "r") as inputFile:
            self.scaler = pickle.load(inputFile)
        
        if self.classes:
            self.data['category_labels'] = [x[0] for x in self.classes]
        
        # multiplicative factors for classes, applied directly after softmax
        if self.classMultiplier:
            try:
                self.clf.set_class_multiplier_from_dict(self.classMultiplier)
            except Exception as e:
                print("ERROR: could not set class multiplier:", e)

    # called from main loop for every event
    def processEvent(self, tree):

        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)
            
            # fill input variables
            for j, syst in enumerate(self.systematics):
                for i, var in enumerate(self.inputVariables[syst]):
                    self.data['test']['X'][j,i] = self.sampleTree.evaluate(var)
            
            # new style
            if hasattr(self.clf, "eval"):
                probabilities, labels, weights = self.clf.eval(feed_dict={self.clf.x: self.scaler.transform(self.data['test']['X'])})

            # "old style"
            else:
                self.data['test']['X_sc'] = self.scaler.transform(self.data['test']['X'])
                probabilities = self.clf.session.run(self.clf.predictions, feed_dict={
                            self.clf.x: self.data['test']['X_sc'], 
                            self.clf.y_: self.data['test']['y'].astype(int),
                            self.clf.w: self.data['test']['sample_weight'],
                            self.clf.keep_prob: np.array([1.0]*len(self.clf.pKeep), dtype=np.float32),
                            self.clf.learning_rate_adam: self.parameters['learning_rate_adam_start'],
                            self.clf.is_training: False,
                        })

            # fill output branches
            if len(self.dnnCollections) == 1:
                # for signal/background store just one of the two, selected by self.signalIndex
                for i,dnnCollection in enumerate(self.dnnCollections):
                    for j, syst in enumerate(self.systematics):
                        dnnCollection[dnnCollection.name][j] = probabilities[j, self.signalIndex]
            else:
                # for multi-class, store all
                for i,dnnCollection in enumerate(self.dnnCollections):
                    for j, syst in enumerate(self.systematics):
                        dnnCollection[dnnCollection.name][j] = probabilities[j, i]
                for j, syst in enumerate(self.systematics):
                    self.dnnCollectionsMulti['argmax']._b()[j] = np.argmax(probabilities[j])
                    sortedValues = np.sort(probabilities[j])
                    self.dnnCollectionsMulti['max']._b()[j] = min(sortedValues[-1], 0.9999)
                    self.dnnCollectionsMulti['max2']._b()[j] = min(sortedValues[-2], 0.9999)

                    # sum the total signal probability, useful in case of multiple signals
                    self.dnnCollectionsMulti['signal']._b()[j] = min(sum([probabilities[j, i] for i in self.signalClassIds]), 0.9999)

                    # default linearization method
                    #self.dnnCollectionsMulti['default']._b()[j] = self.dnnCollectionsMulti['argmax']._b()[j] + min(np.power(sortedValues[-1] - sortedValues[-2], 0.25), 0.9999)
                    self.dnnCollectionsMulti['default']._b()[j] = self.dnnCollectionsMulti['argmax']._b()[j] + min(sortedValues[-1], 0.9999) 

        return True

    def cleanUp(self):
        try:
            if self.clf:
                self.clf.cleanUp()
                print("INFO: tensorflow session cleaned up!")
        except Exception as e:
            print("ERROR: clean-up failed!", e)

