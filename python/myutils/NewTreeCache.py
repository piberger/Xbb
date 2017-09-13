from __future__ import print_function
import glob
from Hash import Hash
from sampleTree import SampleTree as SampleTree
import subprocess

#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------
class TreeCache:

    def __init__(self, sample, cutList = '1', branches = None, inputFolder = None, outputFolder = 'tmp/', cachePart=-1, cacheParts=-1, debug=False):
        self.sample = sample
        self.minCut = self.findMinimumCut(cutList)
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.cachedFileNames = []
        self.hash = Hash(sample=sample, minCut=self.minCut, debug=False).get()
        self.cachePart = cachePart
        self.cacheParts = cacheParts if cacheParts > 1 else 1
        self.identification = '{sample}[{cut}]of{parts}'.format(sample=self.sample, cut=self.minCut, parts=self.cacheParts)
        self.debug = debug
        self.sampleTree = None
        self.isCachedChecked = False
        self.outputFileNameFormat = '{outputFolder}/tmp_{hash}_{part}of{parts}.root'

    # minimum common cut, sorted and cleaned. warning: may not contain spaces in e.g. string comparisons
    def findMinimumCut(self, cutList):
        if type(cutList) == list:
            cuts = cutList
        else:
            cuts = [cutList]
        return '||'.join(['(%s)'%x.replace(' ', '') for x in sorted(cuts)])

    # file, where skimmed tree is written to
    def getOutputFileName(self):
        return self.outputFileNameFormat.format(
            outputFolder = self.outputFolder,
            hash = self.hash,
            part = self.cachePart if self.cachePart > 0 else 1,
            parts = '%d'%self.cacheParts
        )

    # check existence of files with skimmed trees
    def findCachedFileNames(self):
        cachedFilesMask = self.outputFileNameFormat.format(
            outputFolder = self.outputFolder,
            hash = self.hash,
            part = '*',
            parts = '%d'%self.cacheParts
        )
        self.cachedFileNames = glob.glob(cachedFilesMask)
        if self.debug:
            print ('\x1b[32mDEBUG: found files:')
            for fileName in self.cachedFileNames:
                print (' > ', fileName)
            if len(self.cachedFileNames) < 1:
                print ('none!')
            print ('\x1b[0m')

    # isCached == all files containing the skimmed tree found!
    # todo: check file integrity
    def isCached(self):
        self.findCachedFileNames()
        if len(self.cachedFileNames) != self.cacheParts:
            if self.debug:
                print ('\x1b[32mDEBUG: not cached:', self.identification, '\x1b[0m')
            return False
        self.isCachedChecked = True
        return True

    def isCachedAndValid(self):
        if self.isCached():
            # check file integrity
            for fileName in self.cachedFileNames:
                pass
        else:
            return False


    # set input sampleTree object
    def setSampleTree(self, sampleTree):
        self.sampleTree = sampleTree

    # this prepares the caching by telling the sampleTree object what to write during processing of the file
    # note: does not run the caching by itself! needs an additional sampleTree.process()
    def cache(self):
        if self.sampleTree:
            outputFileName = self.getOutputFileName()
            self.sampleTree.addOutputTree(outputFileName, self.minCut, self.hash)
            if self.debug:
                print ('\x1b[32mDEBUG: output file for ', self.identification, ' is ', outputFileName, '\x1b[0m')
        else:
            print ('\x1b[31mERROR: no sample tree!:', self.identification, '\x1b[0m')

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
