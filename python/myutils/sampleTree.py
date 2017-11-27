#!/usr/bin/env python
from __future__ import print_function
import ROOT
import os
import sys
import time
import glob
import BetterConfigParser
from BranchList import BranchList
from FileLocator import FileLocator
import array
import resource

# ------------------------------------------------------------------------------
# sample tree class
# 
# reads many .root files and chain them as a TChain and adds all the TH1D count
# histograms together. Provides an iterator which handles the updating of
# TTreeFormulas automatically when the tree number changes.
#
# create: (A)  sampleTree = SampleTree('path/to/indexfile.txt')
# create: (B)  sampleTree = SampleTree(['path/to/file1.root', 'path/to/file2.root'])
# create: (C)  sampleTree = SampleTree({'name': 'DY50to100', 'folder': ...})
#
# add formula: sampleTree.addFormula('ptCut','pt>100')
#
# loop over events:
#
# for event in sampleTree: 
#     print 'pt cut:', sampleTree.evaluate('ptCut')
#     print 'pt:', event.pt
# ------------------------------------------------------------------------------
class SampleTree(object):

    def __init__(self, samples, treeName='tree', limitFiles=-1, splitFilesChunkSize=-1, chunkNumber=1, countOnly=False, verbose=True, config=None):
        self.verbose = verbose
        self.debug = 'XBBDEBUG' in os.environ
        self.config = config
        self.monitorPerformance = True
        self.disableBranchesInOutput = True
        self.samples = samples
        self.fileLocator = FileLocator(config=self.config)

        # process only partial sample root file list
        self.splitFilesChunkSize = splitFilesChunkSize
        self.chunkNumber = chunkNumber
       
        # get list of sample root files to process
        sampleFileNamesParts = self.getSampleFileNameChunks()
        if self.chunkNumber > 0 and self.chunkNumber <= self.numParts:
            if len(sampleFileNamesParts) == self.numParts:
                chunkIndex = self.chunkNumber - 1
                self.sampleFileNames = sampleFileNamesParts[chunkIndex]
            else:
                raise Exception("InvalidNumberOfSplitParts")
        else:
            print("\x1b[31mERROR: wrong chunk number ", self.chunkNumber, "\x1b[0m")
            raise Exception("InvalidChunkNumber")
        if self.verbose:
            print ("INFO: reading part ", self.chunkNumber, " of ", self.numParts)

        self.status = 0
        self.treeName = treeName
        self.formulas = {}
        self.formulaDefinitions = []
        self.oldTreeNum = -1
        self.limitFiles = int(limitFiles) 
        self.timeStart = time.time()
        self.timeETA = 0
        self.eventsRead = 0
        self.outputTrees = []
        self.callbacks = {}
        self.removeBranches = []

        # e.g. for additional branches to be added
        self.newBranches = []

        # check existence of sample .txt file which contains list of .root files
        self.sampleTextFileName = ''

        # add all .root files to chain and add count histograms
        self.chainedFiles = []
        self.brokenFiles = []
        self.histograms = {}

        if not countOnly:
            self.tree = ROOT.TChain(self.treeName)

            # loop over all given .root files 
            for rootFileName in self.sampleFileNames:

                # check root file existence, TODO: simplify
                if os.path.isfile(self.fileLocator.getLocalFileName(rootFileName)) or self.fileLocator.isStoragePath(rootFileName) or self.fileLocator.exists(rootFileName):
                    if '://' not in rootFileName and (self.fileLocator.isStoragePath(rootFileName) or self.fileLocator.isPnfs(rootFileName)): 
                        rootFileName = self.fileLocator.getXrootdFileName(rootFileName)
                    input = ROOT.TFile.Open(rootFileName, 'read')

                    # check file validity
                    if input and not input.IsZombie() and input.GetNkeys() > 0 and not input.TestBit(ROOT.TFile.kRecovered):

                        # add count histograms, since they are not in the TChain
                        for key in input.GetListOfKeys():
                            obj = key.ReadObj()
                            if obj.GetName() == self.treeName:
                                continue
                            histogramName = obj.GetName()

                            if histogramName in self.histograms:
                                if self.histograms[histogramName]:
                                    self.histograms[histogramName].Add(obj.Clone(obj.GetName()))
                                else:
                                    print ("ERROR: histogram object was None!!!")
                                    raise Exception("CountHistogramMissing")
                            else:
                                self.histograms[histogramName] = obj.Clone(obj.GetName())
                                self.histograms[histogramName].SetDirectory(0)
                        input.Close()

                        # add file to chain
                        chainTree = '%s/%s'%(rootFileName, self.treeName)
                        if self.debug:
                            print ('DEBUG: chaining '+chainTree)
                        statusCode = self.tree.Add(chainTree)

                        # check for errors in chaining the file
                        if statusCode != 1:
                            print ('ERROR: failed to chain ' + chainTree + ', returned: ' + str(statusCode), 'tree:', self.tree)
                            raise Exception("TChain method Add failure")
                        elif not self.tree:
                            print ('\x1b[31mERROR: tree died after adding %s.\x1b[0m'%rootFileName)
                        else:
                            self.treeEmpty = False
                            self.chainedFiles.append(rootFileName)
                            if self.limitFiles > 0 and len(self.chainedFiles) >= self.limitFiles:
                                print ('\x1b[35mDEBUG: limit reached! no more files will be chained!!!\x1b[0m')
                                break
                    else:
                        print ('\x1b[31mERROR: file is damaged: %s\x1b[0m'%rootFileName)
                        if input:
                            print ('DEBUG: Zombie:', input.IsZombie(), '#keys:', input.GetNkeys(), 'recovered:', input.TestBit(ROOT.TFile.kRecovered))
                        self.brokenFiles.append(rootFileName)
                else:
                    print ('\x1b[31mERROR: file is missing: %s\x1b[0m'%rootFileName)

            if self.verbose:
                print ('INFO: # files chained: %d'%len(self.chainedFiles))
                if len(self.brokenFiles) > 0:
                    print ('INFO: # files broken : %d'%len(self.brokenFiles))
            
            if len(self.chainedFiles) < 1:
                self.tree = None

            if self.tree:
                self.tree.SetCacheSize(50*1024*1024)

    def __del__(self):
        self.delete()

    def delete(self):
        # close possible left open files referencing the TChain and delete output trees 
        self.callbacks = None
        self.tree.Reset()
        self.fileLocator = None
        self.config = None
        for outputTree in self.outputTrees:
            del outputTree['file']
        try:
            for formulaName, formula in self.formulas.iteritems():
                if formula:
                    del formula
                    formula = None
        except e:
            print("EXCEPTION:", e)
        try:
            for outputTree in self.outputTrees:
                if outputTree['tree']:
                    del outputTree['tree']
                    outputTree['tree'] = None
        except e:
            print("EXCEPTION:", e)
        try:
            if self.tree:
                del self.tree
                self.tree = None
        except e:
            print("EXCEPTION:", e)

    # ------------------------------------------------------------------------------
    # return full list of sample root files 
    # ------------------------------------------------------------------------------
    def getAllSampleFileNames(self): 
        # given argument is list -> this is already the list of root files
        if type(self.samples) == list:
            sampleFileNames = self.samples
        # given argument is name and folder -> glob
        elif type(self.samples) == dict:
            if 'sample' in self.samples:
                sampleName = self.samples['sample'].identifier
            else:
                sampleName = self.samples['name']
            sampleFolder = self.samples['folder']
            samplesMask = self.fileLocator.getLocalFileName(sampleFolder) + '/' + sampleName + '/*.root'
            if self.verbose:
                print ("INFO: use ", samplesMask)
            sampleFileNames = glob.glob(samplesMask)
            if self.verbose:
                print ("INFO: found ", len(sampleFileNames), " files.")
        # given argument is a single file name -> read this .txt file 
        else:
            sampleTextFileName = self.samples
            if os.path.isfile(sampleTextFileName):
                self.sampleTextFileName = sampleTextFileName
                if self.verbose:
                    print('open samples .txt file: %s' % self.sampleTextFileName)
            else:
                print("\x1b[31mERROR: file not found: %s \x1b[0m" % sampleTextFileName)
                return

            with open(self.sampleTextFileName, 'r') as sampleTextFile:
                sampleFileNames = sampleTextFile.readlines()
        return sampleFileNames

    # ------------------------------------------------------------------------------
    # return lists of sample root files, split into chunks with certain size  
    # ------------------------------------------------------------------------------
    def getSampleFileNameChunks(self):
        sampleFileNames = self.getAllSampleFileNames()
        if self.splitFilesChunkSize > 0 and len(sampleFileNames) > self.splitFilesChunkSize:
            sampleFileNamesParts = [sampleFileNames[i:i + self.splitFilesChunkSize] for i in xrange(0, len(sampleFileNames), self.splitFilesChunkSize)]
        else:
            sampleFileNamesParts = [sampleFileNames]
        self.numParts = len(sampleFileNamesParts)
        return sampleFileNamesParts

    # ------------------------------------------------------------------------------
    # return lists of sample root files for a single chunk  
    # ------------------------------------------------------------------------------
    def getSampleFileNameChunk(self, chunkNumber):
        chunks = self.getSampleFileNameChunks()
        if chunkNumber > 0 and chunkNumber <= len(chunks):
            return chunks[chunkNumber-1]
        else:
            print("\x1b[31mERROR: invalid chunk number {n} \x1b[0m".format(n=chunkNumber))

    def getNumberOfParts(self):
        return self.numParts

    # ------------------------------------------------------------------------------
    # add a TTreeFormula connected to the TChain
    # ------------------------------------------------------------------------------
    def addFormula(self, formulaName, formula):
        self.formulaDefinitions.append({'name': formulaName, 'formula': formula})
        self.formulas[formulaName] = ROOT.TTreeFormula(formulaName, formula, self.tree) 
        if self.formulas[formulaName].GetNdim() == 0:
            print("DEBUG: formula is:", formula)
            print("\x1b[31mERROR: adding the tree formula failed! Check branches of input tree and loaded namespaces.\x1b[0m")
            raise Exception("SampleTreeAddTTreeFormulaFailed")

    # ------------------------------------------------------------------------------
    # add a new branch
    # ------------------------------------------------------------------------------
    def addOutputBranch(self, branchName, formula, branchType='f', length=1, arguments=None, leaflist=None):
        # this is needed to overwrite the branch if it already exists!
        self.addBranchToBlacklist(branchName)

        # function
        if callable(formula):
            newBranch = {'name': branchName, 'function': formula, 'type': branchType, 'length': length}
            if arguments:
                newBranch['arguments'] = arguments
        # string which contains a TTreeFormula expression
        else:
            formulaName = 'alias:' + branchName
            self.addFormula(formulaName, formula)
            newBranch = {'name': branchName, 'formula': formulaName, 'type': branchType, 'length': length}
        if leaflist:
            newBranch['leaflist'] = leaflist
        self.newBranches.append(newBranch)

    # ------------------------------------------------------------------------------
    # pass a list of dictionaries of branches to add
    # TODO: avoid detour via addOutputBranch and set dictionary directly
    # ------------------------------------------------------------------------------
    def addOutputBranches(self, branchDictList):
        for branchDict in branchDictList:
            self.addOutputBranch(
                branchName=branchDict['name'],
                formula=branchDict['formula'],
                branchType=branchDict['type'] if 'type' in branchDict else 'f',
                length=branchDict['length'] if 'length' in branchDict else 1,
                arguments=branchDict['arguments'] if 'arguments' in branchDict else None,
                leaflist=branchDict['leaflist'] if 'leaflist' in branchDict else None,
            )

    # ------------------------------------------------------------------------------
    # implement iterator for TChain, with updating TTreeFormula objects on tree
    # switching and show performance statistics during loop
    # ------------------------------------------------------------------------------
    def next(self):
        self.treeIterator.next()
        self.eventsRead += 1
        treeNum = self.tree.GetTreeNumber()
        # TTreeFormulas have to be updated when the tree number changes in a TChain
        if treeNum != self.oldTreeNum:

            # update ETA estimates
            if treeNum == 0:
                self.timeStart = time.time()
                perfStats = '?'
            else:
                fraction = 1.0*treeNum/len(self.chainedFiles)
                passedTime = time.time() - self.timeStart
                self.timeETA = (1.0-fraction)/fraction * passedTime if fraction > 0 else 0
                perfStats = 'INPUT: {erps}/s, OUTPUT: {ewps}/s '.format(erps=self.eventsRead / passedTime if passedTime>0 else 0, ewps=sum([x['passed'] for x in self.outputTrees]) / passedTime if passedTime>0 else 0)

            # output status
            if self.verbose or self.debug:
                percentage = 100.0*treeNum/len(self.chainedFiles)
                if treeNum == 0:
                    print ('INFO: time ', time.ctime())
                print ('INFO: switching trees --> %d (=%1.1f %%, ETA: %s min, %s)'%(treeNum, percentage, self.getETA(), perfStats))
                if self.debug:
                    self.tree.PrintCacheStats()
                sys.stdout.flush()
            self.oldTreeNum = treeNum
            # update TTreeFormula's
            for formulaName, treeFormula in self.formulas.iteritems():
                treeFormula.UpdateFormulaLeaves()
        return self.tree

    def __iter__(self):
        self.treeIterator = self.tree.__iter__()
        return self

    # wrapper to evaluate a formula, which has been added to the formula dictionary
    # vector valued formulas are not supported
    def evaluate(self, formulaName):
        if formulaName in self.formulas:
            if self.formulas[formulaName].GetNdata() > 0:
                return self.formulas[formulaName].EvalInstance()
            else:
                return 0
        else:
            existingFormulas = [x for x,y in self.formulas.iteritems()]
            print ("existing formulas are: ", existingFormulas)
            raise Exception("SampleTree::evaluate: formula '%s' not found!"%formulaName)

    # evaluates a vector formula and fills an array, returns the number of dimensions of the formula
    def evaluateArray(self, formulaName, destinationArray):
        if formulaName in self.formulas:
            nData = self.formulas[formulaName].GetNdata()
            for i in range(nData):
                destinationArray[i] = self.formulas[formulaName].EvalInstance(i)
            return nData
        else:
            existingFormulas = [x for x, y in self.formulas.iteritems()]
            print("existing formulas are: ", existingFormulas)
            raise Exception("SampleTree::evaluate: formula '%s' not found!" % formulaName)

    # return string of ETA in minutes
    def getETA(self):
        return '%1.1f'%(self.timeETA/60.0) if self.timeETA > 0 else '?'

    def GetListOfBranches(self):
        return self.tree.GetListOfBranches()


    # ------------------------------------------------------------------------------
    # handle 'tree-typed' cuts, passed as dictionary:
    # e.g. cut = {'OR': [{'AND': ["pt>20","eta<3"]}, "data==1"]}
    # short-circuit evaluation is handled by builtins any() and all()
    # ------------------------------------------------------------------------------
    def addCutDictRecursive(self, cutDict):
        if type(cutDict) == str:
            if cutDict not in self.formulas:
                self.addFormula(cutDict, cutDict)
        elif 'OR' in cutDict and 'AND' in cutDict:
            raise Exception("BadTreeTypeCutDict")
        elif 'OR' in cutDict:
            for subDict in cutDict['OR']:
                self.addCutDictRecursive(subDict)
        elif 'AND' in cutDict:
            for subDict in cutDict['AND']:
                self.addCutDictRecursive(subDict)
        else:
            raise Exception("BadTreeTypeCutDict")

    def evaluateCutDictRecursive(self, cutDict):
        if type(cutDict) == str:
            if self.formulaResults[cutDict] is None:
                print ("FORMULA:", cutDict)
                raise Exception("UnevaluatedFormula!!")
            return self.formulaResults[cutDict]
        elif 'OR' in cutDict and 'AND' in cutDict:
            raise Exception("BadTreeTypeCutDict")
        elif 'OR' in cutDict:
            return any([self.evaluateCutDictRecursive(subDict) for subDict in cutDict['OR']])
        elif 'AND' in cutDict:
            return all([self.evaluateCutDictRecursive(subDict) for subDict in cutDict['AND']])
        else:
            raise Exception("BadTreeTypeCutDict")
    
    # set callback function, which MUST return a boolean. To continue processing this event, the function must return True. False means skip this event!
    def setCallback(self, category, fcn):
        if category not in ['event']:
            raise Exception("CallbackEventDoesNotExist")
        if category in self.callbacks:
            print("WARNING: callback function for ", category, " is overwritten!")
        self.callbacks[category] = [fcn]

    # add callback function, which MUST return a boolean. To continue processing this event, the function must return True. False means skip this event!
    def addCallback(self, category, fcn):
        if category not in ['event']:
            raise Exception("CallbackEventDoesNotExist")
        if category not in self.callbacks:
             self.callbacks[category] = []
        self.callbacks[category].append(fcn)

    # ------------------------------------------------------------------------------
    # add output tree to be written during the process() function
    # ------------------------------------------------------------------------------
    def addOutputTree(self, outputFileName, cut, hash='', branches=None, callbacks=None, cutSequenceMode='AND', name=''):

        # write events which satisfy either ONE of the conditions given in the list or ALL
        if cutSequenceMode not in ['AND', 'OR', 'TREE']:
            raise Exception("InvalidCutSequenceMode")

        outputTree = {
            'tree': None, # will create this tree later, after it is known which branches will be enabled 
            'name': name,
            'fileName': outputFileName,
            'file': ROOT.TFile.Open(outputFileName, 'recreate'),
            'cut': cut,
            'cutSequence': [],
            'cutSequenceMode': cutSequenceMode,
            'hash': hash,
            'branches': branches,
            'callbacks': callbacks,
            'passed': 0,
        }

        if not outputTree['file'] or outputTree['file'].IsZombie():
            print ("\x1b[31mERROR: output file broken\x1b[0m")
            raise Exception("OutputFileBroken")

        # copy count histograms to output files
        outputTree['histograms'] = {}
        for histogramName, histogram in self.histograms.iteritems():
            outputTree['histograms'][histogramName] = histogram.Clone(histogram.GetName())
            outputTree['histograms'][histogramName].SetDirectory(outputTree['file'])

        self.outputTrees.append(outputTree)
    
    # these branches are ALWAYS removed (e.g. because they will be recomputed), even when they are in the 'keep_branches' list
    def addBranchToBlacklist(self, branchName):
        self.removeBranches.append(branchName)

    # wrapper to enable/disable branches in the TChain
    def SetBranchStatus(self, branchName, branchStatus):
        listOfExistingBranches = self.GetListOfBranches()
        if listOfExistingBranches.FindObject(branchName) or '*' in branchName:
            self.tree.SetBranchStatus(branchName, branchStatus)

    # enables ONLY the given branches (* wildcards supported) and checks existence before enabling them to avoid warning messages during tree iteration
    def enableBranches(self, listOfBranchesToKeep):
        listOfExistingBranches = self.GetListOfBranches()
        self.tree.SetBranchStatus("*", 0)
        enabledBranches = []
        for branchName in listOfBranchesToKeep:
            if listOfExistingBranches.FindObject(branchName) or '*' in branchName:
                self.tree.SetBranchStatus(branchName, 1)
                enabledBranches.append(branchName)
        print("INFO: reduced number of enabled branches from", len(listOfExistingBranches), " to", len(enabledBranches))
        if self.verbose:
            print ("INFO: branches:", BranchList(enabledBranches).getShortRepresentation())

    # ------------------------------------------------------------------------------
    # loop over all entries in the TChain and copy events to output trees, if the
    # cuts are fulfilled.
    # ------------------------------------------------------------------------------
    def process(self):
        if self.debug:
            print('DEBUG: mem used:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if self.verbose:
            print ('OUTPUT TREES:')
            for outputTree in self.outputTrees:
                cutString = "%r"%outputTree['cut']
                if len(cutString) > 50:
                    cutString = cutString[0:50] + '...(%s more chars)'%(len(cutString)-50)
                print (' > ', outputTree['fileName'], ' <== ', outputTree['name'] if 'name' in outputTree else outputTree['hash'], ' cut: ', cutString)
            print ('FORMULAS:')
            for formulaName, formula in self.formulas.iteritems():
                print (' > \x1b[35m', formulaName, '\x1b[0m ==> ', formula)

        # find common set of branches which needs to be enabled for cuts and desired variables in all of the output trees
        listOfBranchesToKeep = []
        for outputTree in self.outputTrees:
            if 'branches' in outputTree and outputTree['branches']:
                listOfBranchesToKeep += outputTree['branches']
            if 'cut' in outputTree and outputTree['cut']:
                listOfBranchesToKeep += BranchList(outputTree['cut']).getListOfBranches()
            for formula in self.formulaDefinitions:
                listOfBranchesToKeep += BranchList(formula['formula']).getListOfBranches()

        # ALWAYS keep the branches stated in config
        if self.config:
            listOfBranchesToKeep += eval(self.config.get('Branches', 'keep_branches'))

        listOfBranchesToKeep = list(set(listOfBranchesToKeep))

        # disable the branches in the input if there is no output tree which wants to have all branches
        if '*' not in listOfBranchesToKeep and len(listOfBranchesToKeep) > 0:
            self.enableBranches(listOfBranchesToKeep)
        else:
            print("INFO: keep all branches")

        # now disable all branches, which will be e.g. recomputed
        for branchName in self.removeBranches:
            print ("INFO: but remove", branchName)
            self.SetBranchStatus(branchName, 0)

        # initialize the output trees, this has to be called after the calls to SetBranchStatus
        for outputTree in self.outputTrees:
            # clone tree structure, but don't copy any entries
            outputTree['tree'] = self.tree.CloneTree(0)
            if not outputTree['tree']:
                print ("\x1b[31mWARNING: output tree broken. try to recover!\x1b[0m")
                # if input tree has 0 entries, don't copy 0 entries to the output tree, but ALL of them instead! (sic!)
                # (this is done by omitting the argument to CloneTree)
                outputTree['tree'] = self.tree.CloneTree()
                if not outputTree['tree']:
                    print ("\x1b[31mERROR: output tree broken, input tree: ", self.tree, " \x1b[0m")
                else:
                    print ("\x1b[32mINFO: recovered\x1b[0m")
            outputTree['tree'].SetDirectory(outputTree['file'])

        # add CUT formulas, this has to be called after the calls to SetBranchStatus
        for outputTree in self.outputTrees:
            if outputTree['cutSequenceMode'] == 'TREE' and type(outputTree['cut']) == dict:
                outputTree['cutSequence'] = outputTree['cut']
                # now recursively parse the cut-tree and add all contained cut formulas
                self.addCutDictRecursive(outputTree['cut'])
            elif type(outputTree['cut']) == dict:
                print ("HINT: use cutSequenceMode='TREE' to pass dictionaries!")
                raise Exception("InvalidCutSequenceMode")
            else:
                # cut passed as string or list of strings
                cutList = outputTree['cut'] if type(outputTree['cut']) == list else [outputTree['cut']]
                for i, cutString in enumerate(cutList):
                    formulaName = cutString.replace(' ', '')
                    if formulaName not in self.formulas:
                        self.addFormula(formulaName, cutString)
                    outputTree['cutSequence'].append(formulaName)

        # prepare memory for new branches to be written
        for outputTree in self.outputTrees:
            outputTree['newBranchArrays'] = {}
            outputTree['newBranches'] = {}
            for branch in self.newBranches:
                outputTree['newBranchArrays'][branch['name']] = array.array(branch['type'], [0] * branch['length'])
                if 'leaflist' in branch:
                    leafList = branch['leaflist'] 
                else:
                    leafList = '{name}{length}/{type}'.format(name=branch['name'], length='[%d]'%branch['length'] if branch['length'] > 1 else '', type=branch['type'].upper())
                outputTree['newBranches'][branch['name']] = outputTree['tree'].Branch(branch['name'], outputTree['newBranchArrays'][branch['name']], leafList)
        if len(self.newBranches) > 0:
            print("ADD NEW BRANCHES:")
            for branch in self.newBranches:
                print(" > \x1b[32m{name}\x1b[0m {formula}".format(
                    name=(branch['name']+('[%d]'%branch['length'] if branch['length'] > 1 else '')).ljust(30),
                    formula=branch['formula'] if 'formula' in branch else 'function:\x1b[33m{fct}\x1b[0m'.format(fct=branch['function'].__name__)
                ))

        # callbacks before loop
        for outputTree in self.outputTrees:
            if outputTree['callbacks'] and 'beforeLoop' in outputTree['callbacks']:
                outputTree['callbacks']['beforeLoop']()

        print ("------------------")
        print (" start processing ")
        print ("------------------")
        # loop over all events and write to output branches
        for event in self:

            # new event callback
            if self.callbacks and 'event' in self.callbacks:
                # if callbacks return false, skip event!
                callbackResults = [fcn(event) for fcn in self.callbacks['event']]
                if not all(callbackResults):
                    continue

            # fill branches
            for branch in self.newBranches:
                # evaluate result either as function applied on the tree entry or as TTreeFormula
                if branch['length'] == 1:
                    if 'function' in branch:
                        if 'arguments' in branch:
                            branchResult = branch['function'](event, arguments=branch['arguments'])
                        else:
                            branchResult = branch['function'](event)
                    else:
                        branchResult = self.evaluate(branch['formula'])
                    if 'type' in branch and branch['type'] == 'i':
                        branchResult = int(branchResult)
                    # fill it for all the output trees
                    for outputTree in self.outputTrees:
                        outputTree['newBranchArrays'][branch['name']][0] = branchResult
                # for arrays pass the pointer to the array to the evaluation function to save the list->array conversion
                else:
                    if 'function' in branch:
                        # todo: make it more efficient by using a shared memory block for all of the output trees'
                        # todo: branches, this would help in case one adds new branches and writes to several trees at once
                        for outputTree in self.outputTrees:
                            if 'arguments' in branch:
                                branch['function'](event, destinationArray=outputTree['newBranchArrays'][branch['name']], arguments=branch['arguments'])
                            else:
                                branch['function'](event, destinationArray=outputTree['newBranchArrays'][branch['name']])
                    else:
                        for outputTree in self.outputTrees:
                            self.evaluateArray(branch['formula'], destinationArray=outputTree['newBranchArrays'][branch['name']])

            # evaluate all formulas
            self.formulaResults = {}
            for formulaName, formula in self.formulas.iteritems():
                self.formulaResults[formulaName] = self.evaluate(formulaName)

            # evaluate cuts for all output trees
            for outputTree in self.outputTrees:

                # evaluate all cuts of the sequence and abort early if one is not satisfied
                if outputTree['cutSequenceMode'] == 'AND':
                    passedCut = True
                    for cutFormulaName in outputTree['cutSequence']:
                        passedCut = passedCut and self.formulaResults[cutFormulaName]
                        if not passedCut:
                            break
                elif outputTree['cutSequenceMode'] == 'OR':
                    passedCut = False
                    for cutFormulaName in outputTree['cutSequence']:
                        passedCut = passedCut or self.formulaResults[cutFormulaName]
                        if passedCut:
                            break
                elif outputTree['cutSequenceMode'] == 'TREE':
                    passedCut = self.evaluateCutDictRecursive(outputTree['cutSequence'])
                else:
                    raise Exception("InvalidCutSequenceMode")

                # fill event if it passed the selection
                if passedCut:
                    outputTree['tree'].Fill()
                    outputTree['passed'] += 1
        print('INFO: end of processing. time ', time.ctime())
        sys.stdout.flush()

        # write files
        for outputTree in self.outputTrees:
            outputTree['file'].Write()
            outputTree['file'].Close()
        print('INFO: files written')
        sys.stdout.flush()

        # callbacks after having written file
        for outputTree in self.outputTrees:
            if outputTree['callbacks'] and 'afterWrite' in outputTree['callbacks']:
                try:
                    outputTree['callbacks']['afterWrite']()
                except Exception as e:
                    print("\x1b[31mWARNING: exception during callback:", e, "\x1b[0m")

        print('INFO: done. time ', time.ctime(), ' events read:', self.eventsRead)
        sys.stdout.flush()

        for outputTree in self.outputTrees:
            passedSelectionFraction = 100.0*outputTree['passed']/self.eventsRead if self.eventsRead>0 else '?'
            print (' > \x1b[34m{name}\x1b[0m {passed} ({fraction}%) => {outputFile}'.format(name=outputTree['name'], passed=outputTree['passed'], fraction=passedSelectionFraction, outputFile=outputTree['fileName']))
        sys.stdout.flush()


    @staticmethod
    def countSampleFiles(samples):
        # get list of sample root files
        if type(samples) == list:
            return len(samples)
        else:
            sampleTextFileName = samples
            if os.path.isfile(sampleTextFileName):
                with open(sampleTextFileName, 'r') as sampleTextFile:
                    sampleFileNames = sampleTextFile.readlines()
                return len(sampleFileNames)
            else:
                print ('ERROR: sample list text file does not exist:', sampleTextFileName)
        return -1

    def getNumSampleFiles(self):
        return len(self.sampleFileNames)

    # return the total scale for the sample, calculated from all count histograms from the TChain
    def getScale(self, sample, countHistogram="CountWeighted"):
        try:
            sample.xsec = sample.xsec[0]
        except:
            pass

        if not countHistogram:
            try:
                posWeight = self.histograms['CountPosWeight'].GetBinContent(1)
                negWeight = self.histograms['CountNegWeight'].GetBinContent(1)
                count = posWeight - negWeight
            except:
                if self.verbose:
                    print("sampleTree: no CountPosWeight/CountNegWeight: using Count instead!!!!!!!!!!!")
                try:
                    count = self.histograms['Count'].GetBinContent(1)
                except Exception as e:
                    print ("EXCEPTION:", e)
                    print ("ERROR: no weight histograms found in sampleTree => terminate")
                    print ("HISTOGRAMS:", self.histograms)
                    exit(0)
        else:
            count = self.histograms[countHistogram].GetBinContent(1)
        lumi = float(sample.lumi)
        theScale = lumi * sample.xsec * sample.sf / float(count)

        if self.verbose:
            print("sampleTree.getScale(): sample: ", sample, "lumi: ", lumi, "xsec: ", sample.xsec, "sample.sf: ", sample.sf, "count (", countHistogram, "):", count, " ---> using scale: ", theScale)
        return theScale

    # create a unique string representation of the total cut, e.g. used to calculate the hash for cached samples 
    # this is not required to be a 'real' cut string, used by TTreeFormula etc.
    @staticmethod
    def findMinimumCut(cutList, cutSequenceMode='AND'):
        if type(cutList) == list or type(cutList) == dict:
            cuts = cutList
        else:
            cuts = [cutList]
        if cutSequenceMode == 'TREE' or type(cutList) == dict:
            minCut = "%r"%cuts
        elif cutSequenceMode == 'AND':
            minCut = '&&'.join(['(%s)'%x.replace(' ', '') for x in sorted(cuts)])
        elif cutSequenceMode == 'OR':
            minCut = '||'.join(['(%s)'%x.replace(' ', '') for x in sorted(list(set(cuts)))])
        else:
            minCut = "%r"%cuts
        return minCut

