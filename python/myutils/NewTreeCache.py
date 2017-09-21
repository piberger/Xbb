from __future__ import print_function
import glob
from Hash import Hash
from sampleTree import SampleTree as SampleTree
import ROOT
import subprocess
import os

# ------------------------------------------------------------------------------
# TreeCache
#
# cache for ROOT trees (abstracted by sampleTree class!) with specific cuts or
# branch selections
#
# usage e.g.:
#
# tc = TreeCache.TreeCache(
#     sample='ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1',
#     cutList='V_pt>100',
#     inputFolder='/scratch/p/',
#     outputFolder='/scratch/p/tmp/',
#     debug=True
# )
#
# #obtain sampleTree of already cached tree:
#
# if tc.isCached():
#    sampleTree = tc.getTree()
#
# #cache one (or several at a time!) new tree
#
# else:
#    sampleTreeBkg = SampleTree('test/bkg.txt')
#    tc.setSampleTree(sampleTreeBkg)
#    tc.cache()
#    tc2.setSampleTree(sampleTreeBkg)
#    tc2.cache()
#    tc3.setSampleTree(sampleTreeBkg)
#    tc3.cache()
#    sampleTreeBkg.process()
#
# one can add many different cuts to process at the same time with multiple
# calls of:
#    tc.setSampleTree(sampleTreeBkg)
#    tc.cache()
# with different tc objects and the same sampleTreeBkg object. In the end, one
# has to run:
#    sampleTreeBkg.process()
# to write the files
# ------------------------------------------------------------------------------
class TreeCache:

    def __init__(self, sample, cutList = '1', branches = None, inputFolder = None, tmpFolder = 'tmp/', outputFolder = 'cache/', cachePart=-1, cacheParts=-1, splitFiles=-1, debug=False):
        self.sample = sample
        self.cutList = cutList
        self.minCut = SampleTree.findMinimumCut(self.cutList)
        self.inputFolder = inputFolder
        self.tmpFolder = tmpFolder
        self.outputFolder = outputFolder
        self.cachedFileNames = []
        self.branches = branches
        self.hash = Hash(sample=sample, minCut=self.minCut, branches=self.branches, splitFiles=splitFiles, debug=False).get()
        self.cachePart = cachePart
        self.cacheParts = cacheParts if cacheParts > 1 else 1
        self.splitFiles = splitFiles
        self.identification = '{sample}[{cut}]of{parts}'.format(sample=self.sample, cut=self.minCut, parts=self.cacheParts)
        self.debug = debug
        self.sampleTree = None
        self.isCachedChecked = False
        self.outputFileNameFormat = '{outputFolder}/tmp_{hash}_{part}of{parts}.root'
        self.tmpFiles = []

        self.createFolders()

    # file, where skimmed tree is written to
    def getTmpFileName(self):
        return self.outputFileNameFormat.format(
            outputFolder = self.tmpFolder,
            hash = self.hash,
            part = self.cachePart if self.cachePart > 0 else 1,
            parts = '%d'%self.cacheParts
        )

    # file, where skimmed tree is moved to after it has been written completely
    def getOutputFileName(self):
        return self.outputFileNameFormat.format(
            outputFolder = self.outputFolder,
            hash = self.hash,
            part = self.cachePart if self.cachePart > 0 else 1,
            parts = '%d'%self.cacheParts
        )

    # check existence of files with skimmed trees
    def findCachedFileNames(self):
        cachedFilesMaskRaw = self.outputFileNameFormat.format(
            outputFolder = self.outputFolder,
            hash = self.hash,
            part = '*',
            parts = '*'
        )
        cachedFilesMask = SampleTree.getLocalFileName(cachedFilesMaskRaw)
        self.cachedFileNames = glob.glob(cachedFilesMask)
        if self.debug:
            print ('DEBUG: search files:', cachedFilesMask)
            print ('\x1b[32mDEBUG: files:')
            for fileName in self.cachedFileNames:
                print (' > ', fileName)
            if len(self.cachedFileNames) < 1:
                print ('none!')
            print ('\x1b[0m(%d files found)'%len(self.cachedFileNames))

    def partIsCached(self):
        cachedFilesMaskRaw = self.outputFileNameFormat.format(
            outputFolder = self.outputFolder,
            hash = self.hash,
            part = self.cachePart,
            parts = '*'
        )
        cachedFilesMask = SampleTree.getLocalFileName(cachedFilesMaskRaw)
        return (len(glob.glob(cachedFilesMask))>0)

    # isCached == all files containing the skimmed tree found!
    def isCached(self):
        self.findCachedFileNames()
        if (len(self.cachedFileNames) != self.cacheParts and self.cacheParts > 1) or len(self.cachedFileNames) == 0:
            if self.debug:
                print ('\x1b[32mDEBUG: not cached:', self.identification, '\x1b[0m')
            return False
        self.isCachedChecked = True
        return True

    # check if an existing file can be opened without errors by ROOT
    def checkFileValidity(self, rawFileName):
        xrootdFileName = SampleTree.getXrootdFileName(rawFileName)
        f = ROOT.TFile.Open(xrootdFileName, 'read')
        if not f or f.GetNkeys() == 0 or f.TestBit(ROOT.TFile.kRecovered) or f.IsZombie():
            print ('\x1b[31mWARNING: broken file:', rawFileName, ' => redo caching!\x1b[0m')
            if f:
                f.Close()
            self.deleteFile(rawFileName)
            return False
        if f:
            f.Close()
        return True

    # check if all cached files are valid
    def isCachedAndValid(self):
        valid = True
        if self.isCached():
            # check file integrity
            for fileName in self.cachedFileNames:
                valid = valid and self.checkFileValidity(fileName)
        else:
            valid = False
        return valid

    # set input sampleTree object
    def setSampleTree(self, sampleTree):
        self.sampleTree = sampleTree
        return self

    # this prepares the caching by telling the sampleTree object what to write during processing of the file
    # note: does not run the caching by itself! needs an additional sampleTree.process()
    def cache(self):
        if self.sampleTree:
            outputFileName = self.getTmpFileName()
            callbacks = {'afterWrite': self.moveFilesToFinalLocation}
            self.sampleTree.addOutputTree(outputFileName=outputFileName, cut=self.cutList, hash=self.hash, branches=self.branches, callbacks=callbacks)
            self.tmpFiles.append(outputFileName)
            if self.debug:
                print ('\x1b[32mDEBUG: output file for ', self.identification, ' is ', outputFileName, '\x1b[0m')
        else:
            print ('\x1b[31mERROR: no sample tree connected!:', self.identification, ' set the sampleTree first with "setSampleTree(sampleTree)" \x1b[0m')
        return self

    # return sample tree class of cached samples if all files found
    def getTree(self):
        if not self.isCachedChecked:
            self.isCached()

        if self.isCachedChecked:
            self.sampleTree = SampleTree(self.cachedFileNames)
        return self.sampleTree

    # delete file
    def deleteFile(self, rawFileName):
        if self.debug:
            print ('DELETE:', rawFileName)
        xrootdFileName = SampleTree.getXrootdFileName(rawFileName)
        if '://' not in xrootdFileName:
            command = 'rm %s' % (xrootdFileName)
        else:
            command = 'gfal-rm %s' % (xrootdFileName)

        returnCode = subprocess.call([command], shell=True)
        if self.debug:
            print(command, ' => ', returnCode)

    # delete cached files
    def deleteCachedFiles(self):
        self.findCachedFileNames()
        for fileName in self.cachedFileNames:
            self.deleteFile(fileName)

    # create folders
    def createFolders(self):
        
        tmpfolderLocal = SampleTree.getLocalFileName(self.tmpFolder)
        if not os.path.isdir(tmpfolderLocal):
            try:
                xrootdFileName = SampleTree.getXrootdFileName(self.tmpFolder)
                if '://' not in xrootdFileName:
                    command = 'mkdir %s' % (xrootdFileName)
                else:
                    command = 'gfal-mkdir %s' % (xrootdFileName)
                returnCode = subprocess.call([command], shell=True)
                if self.debug:
                    print(command, ' => ', returnCode)
            except:
                pass
        outputFolderLocal = SampleTree.getLocalFileName(self.outputFolder)

        if not os.path.isdir(outputFolderLocal):
            try:
                xrootdFileName = SampleTree.getXrootdFileName(self.outputFolder)
                if '://' not in xrootdFileName:
                    command = 'mkdir %s' % (xrootdFileName)
                else:
                    command = 'gfal-mkdir %s' % (xrootdFileName)

                returnCode = subprocess.call([command], shell=True)
                if self.debug:
                    print(command, ' => ', returnCode)
            except Exception as e:
                print ('Exception during mkdir:',e)

    # move files from temporary to final location
    def moveFilesToFinalLocation(self):
        success = True

        for tmpFileName in self.tmpFiles:
            outputFileName = self.outputFolder + '/' + self.tmpFolder.join(tmpFileName.split(self.tmpFolder)[1:])
            print ('copy ', tmpFileName, ' to ', outputFileName)
            self.deleteFile(outputFileName)
            command = 'xrdcp -d 1 ' + SampleTree.getXrootdFileName(tmpFileName) + ' ' + SampleTree.getXrootdFileName(outputFileName)
            print('the command is', command)
            returnCode = subprocess.call([command], shell=True)
            if returnCode != 0:
                success = False
                print('\x1b[31mERROR: XRDCP failed for {tmpfile}->{outputfile} !\x1b[0m'.format(tmpfile=tmpFileName,
                                                                                                outputfile=outputFileName))
            else:
                # delete temporary file if copy was successful
                self.deleteFile(tmpFileName)
        return success
