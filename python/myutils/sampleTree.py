#!/usr/bin/env python
from __future__ import print_function
import ROOT
import os
import math
import time
import glob

#------------------------------------------------------------------------------
# sample tree class
# 
# reads many .root files and chain them as a TChain and adds all the TH1D count
# histograms together. Provides an iterator which handles the updating of
# TTreeFormulas automatically when the tree number changes.
#
# create: (A)  sampleTree = SampleTree('path/to/indexfile.txt')
# create: (B)  sampleTree = SampleTree(['path/to/file1.root', 'path/to/file2.root'])
#
# add formula: sampleTree.addFormula('ptCut','pt>100')
#
# loop over events:
#
# for event in sampleTree: 
#     print 'pt cut:', sampleTree.evaluate('ptCut')
#     print 'pt:', event.pt
#------------------------------------------------------------------------------
class SampleTree(object):

    xrootdRedirector = 'root://t3dcachedb03.psi.ch:1094'
    moreXrootdRedirectors = ['root://t3dcachedb.psi.ch:1094']
    pnfsStoragePath = '/pnfs/psi.ch/cms/trivcat'

    def __init__(self, samples, treeName='tree', limitFiles=-1, splitFilesChunkSize=-1, chunkNumber=1, countOnly=False):
        self.verbose = True
        self.monitorPerformance = True
        self.samples = samples

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
            print("\x1b[31mERROR: wrong chunk number ", self.chunkNumber, " for: %s \x1b[0m" % sampleTextFileName)
            raise Exception("InvalidChunkNumber")
        if self.verbose:
            print ("INFO: reading part ", self.chunkNumber, " of ", self.numParts)

        self.status = 0
        self.treeName = treeName
        self.formulas = {}
        self.oldTreeNum = -1
        self.limitFiles = int(limitFiles) 
        self.timeStart = time.time()
        self.timeETA = 0
        self.eventsRead = 0
        self.outputTrees = []

        self.regionDict = {
            'default': {'file': 0}
        }

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

                # check root file existence
                if os.path.isfile(SampleTree.getLocalFileName(rootFileName)) or '/store/' in rootFileName:
                    rootFileName = SampleTree.getXrootdFileName(rootFileName)
                    input = ROOT.TFile.Open(rootFileName,'read')

                    # check file validity
                    if input and not input.IsZombie() and input.GetNkeys() > 0 and not input.TestBit(ROOT.TFile.kRecovered):

                        # add count histograms, since they are not in the tchain
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
                        if self.verbose:
                            print ('DEBUG: chaining '+chainTree)
                        statusCode = self.tree.Add(chainTree)

                        # check for errors in chaining the file
                        if statusCode != 1:
                            print ('ERROR: failed to chain ' + chainTree + ', returned: ' + str(statusCode),'tree:',tree)
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
                        print ('ERROR: file is damaged: %s'%rootFileName)
                        if input:
                            print ('DEBUG: Zombie:', input.IsZombie(), '#keys:', input.GetNkeys(), 'recovered:',input.TestBit(ROOT.TFile.kRecovered))
                        self.brokenFiles.append(rootFileName)
                else:
                    print ('ERROR: file is missing: %s'%rootFileName)

            if self.verbose:
                print ('INFO: # files chained: %d'%len(self.chainedFiles))
                if len(self.brokenFiles) > 0:
                    print ('INFO: # files broken : %d'%len(self.brokenFiles))
            
            if len(self.chainedFiles) < 1:
                self.tree = None

            if self.tree:
                self.tree.SetCacheSize(50*1024*1024)

    #------------------------------------------------------------------------------
    # return full list of sample root files 
    #------------------------------------------------------------------------------
    def getAllSampleFileNames(self): 
        # given argument is list -> this is already the list of root files
        if type(self.samples) == list:
            sampleFileNames = self.samples
        # given argument is name and folder -> glob
        elif type(self.samples) == dict:
            sampleName = self.samples['name']
            sampleFolder = self.samples['folder']
            if self.verbose:
                print ("INFO: use ",SampleTree.getLocalFileName(sampleFolder) + '/' + sampleName + '/*.root')
            sampleFileNames = glob.glob(SampleTree.getLocalFileName(sampleFolder) + '/' + sampleName + '/*.root') 
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

    #------------------------------------------------------------------------------
    # return lists of sample root files, split into chunks with certain size  
    #------------------------------------------------------------------------------
    def getSampleFileNameChunks(self):
        sampleFileNames = self.getAllSampleFileNames()
        if self.splitFilesChunkSize > 0 and len(sampleFileNames) > self.splitFilesChunkSize:
            self.numParts = int(math.ceil(float(len(sampleFileNames))/self.splitFilesChunkSize))
            sampleFileNamesParts = [sampleFileNames[i:i + self.splitFilesChunkSize] for i in xrange(0, len(sampleFileNames), self.splitFilesChunkSize)]
        else:
            self.numParts = 1
            sampleFileNamesParts = [sampleFileNames]
        return sampleFileNamesParts

    #------------------------------------------------------------------------------
    # return lists of sample root files for a single chunk  
    #------------------------------------------------------------------------------
    def getSampleFileNameChunk(self, chunkNumber):
        chunks = self.getSampleFileNameChunks()
        if chunkNumber > 0 and chunkNumber <= len(chunks):
            return chunks[chunkNumber-1]
        else:
            print("\x1b[31mERROR: invalid chunk number {n} \x1b[0m".format(n=chunkNumber))

    def getNumberOfParts(self):
        return self.numParts

    #------------------------------------------------------------------------------
    # add a TTreeFormula connected to the TChain
    #------------------------------------------------------------------------------
    def addFormula(self, formulaName, formula):
        self.formulas[formulaName] = ROOT.TTreeFormula(formulaName, formula, self.tree) 

    #------------------------------------------------------------------------------
    # implement iterator for TChain, with updating TTreeFormula objects on tree
    # switching and show performance statistics during loop
    #------------------------------------------------------------------------------
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
            if self.verbose:
                percentage = 100.0*treeNum/len(self.chainedFiles)
                if treeNum == 0:
                    print ('INFO: time ', time.ctime())
                print ('INFO: switching trees --> %d (=%1.1f %%, ETA: %s min, %s)'%(treeNum, percentage, self.getETA(), perfStats))
            self.oldTreeNum = treeNum
            # update TTreeFormula's
            for formulaName, treeFormula in self.formulas.iteritems():
                treeFormula.UpdateFormulaLeaves()
        return self.tree

    def __iter__(self):
        self.treeIterator = self.tree.__iter__()
        return self

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
    
    def getETA(self):
        # return ETA in seconds
        return '%1.1f'%(self.timeETA/60.0) if self.timeETA > 0 else '?'

    def GetListOfBranches(self):
        return self.tree.GetListOfBranches()

    #------------------------------------------------------------------------------
    # get file name WITH redirector
    #------------------------------------------------------------------------------
    @staticmethod
    def getXrootdFileName(rawFileName):
        xrootdFileName = rawFileName.strip()
        if xrootdFileName.startswith('/store/'):
            xrootdFileName = SampleTree.pnfsStoragePath + xrootdFileName.strip()
        isRemote = '/pnfs/' in xrootdFileName
        if isRemote:
            xrootdFileName = xrootdFileName.replace(SampleTree.xrootdRedirector, '')
            for red in SampleTree.moreXrootdRedirectors:
                xrootdFileName = xrootdFileName.replace(red, '')
            return SampleTree.xrootdRedirector + xrootdFileName.replace(SampleTree.xrootdRedirector, '').strip()
        else:
            return xrootdFileName.strip()

    #------------------------------------------------------------------------------
    # get file name WITHOUT redirector
    #------------------------------------------------------------------------------
    @staticmethod
    def getLocalFileName(rawFileName):
        localFileName = rawFileName.strip()
        localFileName = localFileName.replace(SampleTree.xrootdRedirector, '')
        for red in SampleTree.moreXrootdRedirectors:
            localFileName = localFileName.replace(red, '')
        if localFileName.startswith('/store/'):
            localFileName = SampleTree.pnfsStoragePath + localFileName.strip()
        return localFileName

    #------------------------------------------------------------------------------
    # add output tree to be written during the process() function 
    #------------------------------------------------------------------------------
    def addOutputTree(self, outputFileName, cut, hash, branches=None, callbacks=None):
        outputTree = {
            'tree': self.tree.CloneTree(0),
            'fileName': outputFileName,
            'file': ROOT.TFile.Open(outputFileName, 'recreate'),
            'cut': cut,
            'cutSequence': [],
            'hash': hash,
            'branches': branches,
            'callbacks': callbacks,
            'passed': 0,
        }

        if not outputTree['tree']:
            print ("\x1b[31mWARNING: output tree broken. try to recover!\x1b[0m")
            # if input tree has 0 entries, don't copy 0 entries to the output tree, but ALL of them instead! (sic!)
            outputTree['tree'] = self.tree.CloneTree()
            if not outputTree['tree']:
                print ("\x1b[31mERROR: output tree broken, input tree: ", self.tree, " \x1b[0m")
            else:
                print ("\x1b[32mINFO: recovered\x1b[0m")
        
        # add CUT formulas
        cutList = cut if type(cut) == list else [cut]
        for i, cutString in enumerate(cutList):
            formulaName = cutString.replace(' ','')
            if formulaName not in self.formulas:
                self.addFormula(formulaName, cutString)
            outputTree['cutSequence'].append(formulaName)
        
        # set output file
        outputTree['tree'].SetDirectory(outputTree['file'])

        # only copy specific branches
        if branches:
            outputTree['tree'].SetBranchStatus("*", 0)
            listOfBranches = self.GetListOfBranches()
            for branch in branches:
                if listOfBranches.findObject(branch):
                    outputTree['tree'].SetBranchStatus(branch, 1)
            if self.verbose:
                print ("enabled ", len(branches), " branches:", branches)

        # copy count histograms to output files
        outputTree['histograms'] = {}
        for histogramName, histogram in self.histograms.iteritems():
            outputTree['histograms'][histogramName] = histogram.Clone(histogram.GetName())
            outputTree['histograms'][histogramName].SetDirectory(outputTree['file'])

        self.outputTrees.append(outputTree)

    def SetBranchStatus(self, branchName, branchStatus):
        self.tree.SetBranchStatus(branchName, branchStatus)

    #------------------------------------------------------------------------------
    # loop over all entries in the TChain and copy events to output trees, if the
    # cuts are fulfilled.
    #------------------------------------------------------------------------------
    def process(self):
        if self.verbose:
            print ('OUTPUT TREES:')
            for outputTree in self.outputTrees:
                print (' > ', outputTree['fileName'], ' <== ', outputTree['hash'], ' cut: ', outputTree['cut'])
            print ('FORMULAS:')
            for formulaName, formula in self.formulas.iteritems():
                print (' > \x1b[35m', formulaName, '\x1b[0m ==> ', formula)

        self.tree.SetCacheSize(50*1024*1024)
        self.tree.AddBranchToCache('*', ROOT.kTRUE)
        self.tree.StopCacheLearningPhase()

        # enable/disable branches
        listOfExistingBranches = self.GetListOfBranches()
        listOfBranchesToKeep = []
        for outputTree in self.outputTrees:
            if 'branches' in outputTree and outputTree['branches']:
                listOfBranchesToKeep += outputTree['branches']
        listOfBranchesToKeep = list(set(listOfBranchesToKeep))

        # only disable the branches if there is no output tree which wants in have all
        if '*' not in listOfBranchesToKeep:

            # get the branches which are used implicitly in the cut formulas
            listOfBranchesNeededForCuts = []
            for formulaName, formula in self.formulas.iteritems():
                for formulaLeaf in range(formula.GetNcodes()):
                    try:
                        listOfBranchesNeededForCuts.append(formula.GetLeaf(formulaLeaf).GetName())
                    except:
                        print ("\x1b[31mWARNING: invalid leaf?!?! (not used for now)\x1b[0m")
            listOfBranchesNeededForCuts = list(set(listOfBranchesNeededForCuts))
            print ("INFO: list of branches need to be kept for cut formulas:")
            for branchName in listOfBranchesNeededForCuts:
                print ("INFO: > {branchName}".format(branchName=branchName))

            print ("INFO: list of branches need to be kept in output trees:")
            for branchName in listOfBranchesToKeep:
                print ("INFO: > {branchName}".format(branchName=branchName))

            print ("\x1b[31mINFO: NOT IMPLEMENTED ----> will keep all branches\x1b[0m")
            # set the branch status
            #self.tree.SetBranchStatus("*", 0)
            #for branchName in listOfBranchesNeededForCuts+listOfBranchesToKeep:
            #    if listOfExistingBranches.FindObject(branchName):
            #        self.tree.SetBranchStatus(branchName, 1)

        # callbacks before loop
        for outputTree in self.outputTrees:
            if outputTree['callbacks'] and 'beforeLoop' in outputTree['callbacks']:
                outputTree['callbacks']['beforeLoop']()

        # loop over all events and write to output branches
        for event in self:

            # evaluate all formulas
            formulaResults = {}
            for formulaName, formula in self.formulas.iteritems():
                formulaResults[formulaName] = self.evaluate(formulaName)
            
            # evaluate cuts for all output trees
            for outputTree in self.outputTrees:

                # evaluate all cuts of the sequence and abort early if one is not satisfied
                passedCut = True
                for cutFormulaName in outputTree['cutSequence']:
                    passedCut = passedCut and formulaResults[cutFormulaName]
                    if not passedCut:
                        break
                if passedCut:
                    outputTree['tree'].Fill()
                    outputTree['passed'] += 1
        print('INFO: end of processing. time ', time.ctime())

        # write files
        for outputTree in self.outputTrees:
            outputTree['file'].Write()
            outputTree['file'].Close()
        print('INFO: files written')

        # callbacks after having written file
        for outputTree in self.outputTrees:
            if outputTree['callbacks'] and 'afterWrite' in outputTree['callbacks']:
                outputTree['callbacks']['afterWrite']()

        print('INFO: done. time ', time.ctime())
        if self.verbose:
            print ('OUTPUT TREES:')
            for outputTree in self.outputTrees:
                print (' > ', outputTree['fileName'], ' passed: ', outputTree['passed'], ' cut: ', outputTree['cut'])

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

    def getScale(self, sample):
        try:
            sample.xsec = sample.xsec[0]
        except:
            pass

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
        lumi = float(sample.lumi)
        theScale = lumi * sample.xsec * sample.sf / float(count)

        if self.verbose:
            print("sampleTree.getScale(): sample: ",sample,"lumi: ",lumi,"xsec: ",sample.xsec,"sample.sf: ",sample.sf,"count: ",count," ---> using scale: ", theScale)
        return theScale

    # make AND of all cuts and return a single cut string. warning: cuts may not contain spaces in e.g. string comparisons
    @staticmethod
    def findMinimumCut(cutList):
        if type(cutList) == list:
            cuts = cutList
        else:
            cuts = [cutList]
        return '&&'.join(['(%s)'%x.replace(' ', '') for x in sorted(cuts)])
