#!/usr/bin/env python
from __future__ import print_function
import ROOT
import argparse
import os
import sys
import time

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

    def __init__(self, samples, treeName='tree', limitFiles=-1):
        self.verbose = True

        if type(samples) == list:
            sampleFileNames = samples
        else:
            sampleTextFileName = samples
            if os.path.isfile(sampleTextFileName):
                self.sampleTextFileName = sampleTextFileName
                if self.verbose:
                    print('open samples .txt file: %s' % self.sampleTextFileName)
            else:
                print("\x1b[31mERROR: file not found: %s \x1b[0m" % sampleTextFileName)
                status = 0
                return

            with open(self.sampleTextFileName, 'r') as sampleTextFile:
                sampleFileNames = sampleTextFile.readlines()

        self.status = 0
        self.treeName = treeName
        self.formulas = {}
        self.oldTreeNum = -1
        self.limitFiles = int(limitFiles) 
        self.timeStart = time.time()
        self.timeETA = 0
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
        self.tree = ROOT.TChain(self.treeName)

        # check all .root files listed in the sample .txt file
        for rootFileName in sampleFileNames:

            if self.verbose:
                print ('--> tree: %s'%(rootFileName.split('/')[-1].strip()))
            if rootFileName.strip().startswith('/store/'):
                rootFileName = '/pnfs/psi.ch/cms/trivcat' + rootFileName.strip()

            # check root file existence
            if os.path.isfile(rootFileName.replace('root://t3dcachedb03.psi.ch:1094/','').strip()):
                obj = None
                rootFileName = self.sanitizeRootFileName(rootFileName)
                input = ROOT.TFile.Open(rootFileName,'read')
                if input and not input.IsZombie():

                    # add count histograms, since they are not in the tchain
                    for key in input.GetListOfKeys():
                        obj = key.ReadObj()
                        if obj.GetName() == self.treeName:
                            continue
                        for region, regionInfo in self.regionDict.iteritems():
                            histogramName = obj.GetName()+region

                            if histogramName in self.histograms:
                                if self.histograms[histogramName]:
                                    self.histograms[histogramName].Add(obj.Clone(obj.GetName()))
                                else:
                                    print ("ERROR: histogram object was None!!!")
                            else:
                                self.histograms[histogramName] = obj.Clone(obj.GetName())
                                self.histograms[histogramName].SetDirectory(regionInfo['file'])
                    input.Close()

                    # add file to chain
                    chainTree = '%s/%s'%(rootFileName, self.treeName)
                    if self.verbose:
                        print ('chaining '+chainTree)
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
                    self.brokenFiles.append(rootFileName)
            else:
                print ('ERROR: file is missing: %s'%rootFileName)

        if self.verbose:
            print ('INFO: # files chained: %d'%len(self.chainedFiles))
            print ('INFO: # files broken : %d'%len(self.brokenFiles))

    def addFormula(self, formulaName, formula):
        self.formulas[formulaName] = ROOT.TTreeFormula(formulaName, formula, self.tree) 

    def next(self):
        self.treeIterator.next()
        treeNum = self.tree.GetTreeNumber()
        # TTreeFormulas have to be updated when the tree number changes in a TChain
        if treeNum != self.oldTreeNum:
            # update ETA estimates
            if treeNum == 0:
                self.timeStart = time.time()
            else:
                fraction = 1.0*treeNum/len(self.chainedFiles)
                passedTime = time.time() - self.timeStart
                self.timeETA = (1.0-fraction)/fraction * passedTime if fraction > 0 else 0
            # output status
            if self.verbose:
                percentage = 100.0*treeNum/len(self.chainedFiles)
                print ('INFO: switching trees --> %d (=%1.1f %%, ETA: %1.1f min)'%(treeNum, percentage, self.getETA()/60.0))
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
        return self.timeETA

    def GetListOfBranches(self):
        return self.tree.GetListOfBranches()

    def sanitizeRootFileName(self, rawFileName):
        isRemote = '/pnfs/' in rawFileName
        if isRemote:
            return 'root://t3dcachedb03.psi.ch:1094/' + rawFileName.replace('root://t3dcachedb03.psi.ch:1094/', '').strip()
        else:
            return rawFileName.strip()

    def addOutputTree(self, outputFileName, cut, hash):
        outputTree = {
            'tree': self.tree.CloneTree(0),
            'fileName': outputFileName,
            'file': ROOT.TFile.Open(outputFileName, 'recreate'),
            'cut': cut,
            'hash': hash,
            'passed': 0,
        }
        self.addFormula(hash, cut)
        outputTree['tree'].SetDirectory(outputTree['file'])

        # copy count histograms to output files
        outputTree['histograms'] = {}
        for histogramName, histogram in self.histograms.iteritems():
            outputTree['histograms'][histogramName] = histogram.Clone(histogram.GetName())
            outputTree['histograms'][histogramName].SetDirectory(outputTree['file'])

        self.outputTrees.append(outputTree)

    def process(self):
        if self.verbose:
            print ('OUTPUT TREES:')
            for outputTree in self.outputTrees:
                print (' > ', outputTree['fileName'], ' <== ', outputTree['hash'], ' cut: ', outputTree['cut'])
            print ('FORMULAS:')
            for formulaName, formula in self.formulas.iteritems():
                print (' > ', formulaName, ' ==> ', formula)

        # loop over all events and write to output branches
        for event in self:
            for outputTree in self.outputTrees:
                if self.evaluate(outputTree['hash']):
                    outputTree['tree'].Fill()
                    outputTree['passed'] += 1

        # write files
        for outputTree in self.outputTrees:
            outputTree['file'].Write()
            outputTree['file'].Close()

        if self.verbose:
            print ('OUTPUT TREES:')
            for outputTree in self.outputTrees:
                print (' > ', outputTree['fileName'], ' passed: ', outputTree['passed'], ' cut: ', outputTree['cut'])