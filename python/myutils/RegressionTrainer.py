import sys,re,ROOT
ROOT.gROOT.SetBatch(True)
from BranchList import BranchList
from sample_parser import ParseInfo
#from TreeCache import TreeCache
from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree
class RegressionTrainer():
    def __init__(self, config,forceCaching = False):
        vhbb_name_space = config.get('VHbbNameSpace','library')
        ROOT.gSystem.Load(vhbb_name_space)
        
        self.__weight = config.get("TrainRegression","weight")
        self.__varsList = eval(config.get("TrainRegression","regVars"))
        self.__varsDict = eval(config.get("TrainRegression","regDict"))
        self.__vars = self.__varsDict.values()
        self.__target = config.get("TrainRegression","target")
        self.__cut = config.get("TrainRegression","cut")
        self.__title = config.get("TrainRegression","name")
        self.__signals = config.get("TrainRegression","signals")
        self.__regOptions = config.get("TrainRegression","options")
        self.__path = config.get('Directories','REGin')
        samplesinfo=config.get('Directories','samplesinfo')
        self.__info = ParseInfo(samplesinfo,self.__path)
        self.__samples = self.__info.get_samples(self.__signals)
        #self.__tc = TreeCache([self.__cut],self.__samples,path,config)
        self.__trainCut = config.get("TrainRegression","trainCut")
        self.__testCut = config.get("TrainRegression","testCut")
        self.__config = config

        fnameOutput='weights/training_Reg_%s.root' %(self.__title)
        self.output = ROOT.TFile.Open(fnameOutput, "RECREATE")
        self.factory = ROOT.TMVA.Factory('MVA', self.output, '!V:!Silent:!Color:!DrawProgressBar:Transformations=I:AnalysisType=Regression')
        self.force = forceCaching

        #self.force = True
    def train(self):
        print "AAAAAAAA"
        print "__title=",self.__title
        print "__signals=",self.__signals
        print "__info=",self.__info
        print "__samples=",self.__samples
        
        sWeight = 1.
        signals = []
        signalsTest = []
        try:
            addRegressionTreeMethod = self.factory.AddRegressionTree
            self.dataLoader = None
        except:
            print("oh no..")
            # the DataLoader wants to be called '.'
            self.dataLoader = ROOT.TMVA.DataLoader(".")
            addRegressionTreeMethod = self.dataLoader.AddRegressionTree

        branchListOfMVAVars = BranchList()
        for var in self.__vars:
            branchListOfMVAVars.addCut(var)
        for var in [self.__trainCut, self.__testCut]:
            branchListOfMVAVars.addCut(var)
        for var in [self.__cut,self.__target]:
            branchListOfMVAVars.addCut(var)
        branches = branchListOfMVAVars.getListOfBranches()
        print branches 
        self.sampleTree = None
        for sample in self.__samples:
            treeCaches = {}
            for additionalCut in [self.__trainCut, self.__testCut]:
            # cuts
                sampleCuts = [sample.subcut]
                if additionalCut:
                    sampleCuts.append(additionalCut)
                # cut from the mva region
                if self.__cut:
                    sampleCuts.append(self.__cut)

                tc = TreeCache.TreeCache(
                    name='{sample}_{tr}'.format(sample=sample.name, tr='TRAIN' if additionalCut==self.__trainCut else 'EVAL'),
                    sample=sample.name,
                    cutList=sampleCuts,
                    inputFolder=self.__path,
                    branches=branches,
                    config=self.__config,
                    debug=True
                )

                # check if this part of the sample is already cached
                isCached = tc.isCached()
                if not isCached or self.force:
                    if isCached:
                        tc.deleteCachedFiles()
                    # for the first sample which comes from this files, load the tree
                    if not self.sampleTree:
                        self.sampleTree = SampleTree({'name': sample.identifier, 'folder': self.__path}, config=self.__config)
                    treeCaches[additionalCut]=(tc.setSampleTree(self.sampleTree).cache())
                else: 
                    sampleTree = tc.getTree()
                    if additionalCut == self.__trainCut:
                        signals.append(sampleTree)
                    else:
                        signalsTest.append(sampleTree)
                    if sampleTree.tree.GetEntries() == 0:
                        print "empty tree"


            if len(treeCaches) > 0:
                # run on the tree
                print "number of files to cache: "+ str(len(treeCaches))
                self.sampleTree.process()
                for cut, tc in treeCaches.iteritems():
                    sampleTree = tc.getTree()
                    if cut == self.__trainCut:
                        signals.append(sampleTree)
                    else:
                        signalsTest.append(sampleTree)
                    if sampleTree.tree.GetEntries() == 0:
                        print "empty tree"
                    
            else:
                print ("nothing to do!")

                
        for sampleTree in signals:
            tree = sampleTree.tree
            addRegressionTreeMethod( tree,  sWeight, ROOT.TMVA.Types.kTraining )
        for sampleTree in signalsTest:
            tree = sampleTree.tree
            addRegressionTreeMethod( tree, sWeight, ROOT.TMVA.Types.kTesting )
           #     sampleTree.addOutputTree('training_Reg_%s.root' %(hash(additionalCut)),sampleCuts,branches=branches)
           # sampleTree.process()
            
           # for additionalCut in [self.__trainCut, self.__testCut]:
           #     f = ROOT.TFile.Open('training_Reg_%s.root' %(hash(additionalCut)),'read')
           #     t = f.Get('tree') 


        #factory.SetSignalWeightExpression( self.__weight )
        #set input trees
        self.__apply = []
        p = re.compile(r'hJCidx\w+')
        self.factory.Verbose()
        if self.dataLoader:
            for var in self.__varsList:
                self.dataLoader.AddVariable(var+":="+self.__varsDict[var],'D')
            self.dataLoader.AddTarget( self.__target )
            self.factory.BookMethod(self.dataLoader,ROOT.TMVA.Types.kBDT,'BDT_REG_%s'%(self.__title),self.__regOptions) # book an MVA method
        else:
            for var in self.__varsList:
                self.factory.AddVariable(var+":="+self.__varsDict[var], 'D')
            self.factory.AddTarget( self.__target )
            self.factory.BookMethod(ROOT.TMVA.Types.kBDT,'BDT_REG_%s'%(self.__title),self.__regOptions) # book an MVA method
        for var in self.__varsList:
            self.__apply.append(p.sub(r'\g<0>\[0\]', self.__varsDict[var]))
        print (self.__apply)
            
        print "DEBUG1"
        #mycut = ROOT.TCut( self.__cut )
        self.factory.TrainAllMethods()
        self.factory.TestAllMethods()
        self.factory.EvaluateAllMethods()
        self.output.Write()
        regDict = dict(zip(self.__varsList, self.__apply)) 
        self.__config.set('Regression', 'regWeight', '../weights/MVA_BDT_REG_%s.weights.xml' %self.__title)
        self.__config.set('Regression', 'regDict', '%s' %regDict)
        self.__config.set('Regression', 'regVars', '%s' %self.__vars)
        for section in self.__config.sections():
            if not section == 'Regression':
                self.__config.remove_section(section)
        with open('weights/Config_BDT_REG_%s.ini'%self.__title, 'w') as configfile:
            self.__config.write(configfile)
#        with open('weights/Config_BDT_REG_%s.ini'%self.__title, 'r') as configfile:
#            for line in configfile:
#                print line.strip()

