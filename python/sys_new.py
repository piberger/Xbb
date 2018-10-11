#!/usr/bin/env python
import sys
import os
import ROOT
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser
from myutils.FileList import FileList
from myutils import BetterConfigParser, ParseInfo, LeptonSF
from myutils.FileLocator import FileLocator
import importlib
from myutils.sampleTree import SampleTree
import resource

# ntuple processing class (former "sys-step")

class XbbRun:

    def __init__(self, opts):
        self.filelist = FileList.decompress(opts.fileList) if len(opts.fileList) > 0 else None
        print "len(filelist)",len(self.filelist),
        if len(self.filelist) > 0:
            print "filelist[0]:", self.filelist[0]
        else:
            print ''
        self.debug = 'XBBDEBUG' in os.environ
        self.opts = opts

        self.config = BetterConfigParser()
        self.config.read(opts.config)

        samplesinfo = self.config.get('Directories', 'samplesinfo')
        self.channel = self.config.get('Configuration', 'channel')

        VHbbNameSpace = self.config.get('VHbbNameSpace', 'library')
        ROOT.gSystem.Load(VHbbNameSpace)

        self.pathIN = self.config.get('Directories','SYSin')
        self.pathOUT = self.config.get('Directories','SYSout')
        self.tmpDir = self.config.get('Directories','scratch')
        print 'INput samples:\t%s'%self.pathIN
        print 'OUTput samples:\t%s'%self.pathOUT

        self.fileLocator = FileLocator(config=self.config)

        # samples
        info = ParseInfo(samplesinfo, self.pathIN)
        matchingSamples = [x for x in info if x.identifier==opts.sampleIdentifier and not x.subsample]
        if len(matchingSamples) != 1:
            print "need exactly 1 sample identifier as input with -S !!"
            print matchingSamples
            exit(1)
        self.sample = matchingSamples[0]

        # collections
        self.collections = [x.strip() for x in opts.addCollections.split(',') if len(x.strip()) > 0] if len(opts.addCollections.strip())>0  else []
        if len(self.collections) < 1:
            print "\x1b[31mWARNING: no collections added! Specify the collections to add with the --addCollections option!\x1b[0m"
        print 'collections to add:', self.collections
        self.collections = self.parseCollectionList(self.collections)
        print 'after parsing:', self.collections

        # input files
        self.subJobs = []
        if opts.join:
            print("INFO: join input files!")
            
            # translate naming convention of .txt file to imported files after the prep step
            inputFileNamesAfterPrep = [self.fileLocator.getFilenameAfterPrep(x) for x in self.filelist]

            self.subJobs.append({
                'inputFileNames': self.filelist,
                'localInputFileNames': ["{path}/{subfolder}/{filename}".format(path=self.pathIN, subfolder=self.sample.identifier, filename=localFileName) for localFileName in inputFileNamesAfterPrep],
                'outputFileName': "{path}/{subfolder}/{filename}".format(path=self.pathOUT, subfolder=self.sample.identifier, filename=inputFileNamesAfterPrep[0]),
                'tmpFileName': "{path}/{subfolder}/{filename}".format(path=self.tmpDir, subfolder=self.sample.identifier, filename=inputFileNamesAfterPrep[0]),
                })

        else:
            
            # create separate subjob for all files (default!)
            for inputFileName in self.filelist:
                inputFileNamesAfterPrep = [self.fileLocator.getFilenameAfterPrep(inputFileName)]

                self.subJobs.append({
                    'inputFileNames': [inputFileName],
                    'localInputFileNames': ["{path}/{subfolder}/{filename}".format(path=self.pathIN, subfolder=self.sample.identifier, filename=localFileName) for localFileName in inputFileNamesAfterPrep],
                    'outputFileName': "{path}/{subfolder}/{filename}".format(path=self.pathOUT, subfolder=self.sample.identifier, filename=inputFileNamesAfterPrep[0]),
                    'tmpFileName': "{path}/{subfolder}/{filename}".format(path=self.tmpDir, subfolder=self.sample.identifier, filename=inputFileNamesAfterPrep[0]),
                    })

    # lists of single modules can be given instead of a module, "--addCollections Sys.all"
    # [Sys]
    # all = ['Sys.Vtype', 'Sys.Leptons', ...]
    # TODO: make it fully recursive
    def parseCollectionList(self, collections): 
        collectionsListsReplaced = []
        for collection in collections:
            if '.' in collection:
                section = collection.split('.')[0]
                key = collection.split('.')[1]
                listExpression = self.config.get(section, key).strip()
                if listExpression.startswith('[') and listExpression.endswith(']'):
                    listParsed = eval(listExpression)
                    for i in listParsed:
                        collectionsListsReplaced.append(i)
                else:
                    collectionsListsReplaced.append(collection)
            else:
                collectionsListsReplaced.append(collection)
        return collectionsListsReplaced
    
    # run all subjobs
    def run(self):

        for subJob in self.subJobs:

            if self.opts.force or not self.fileLocator.isValidRootFile(subJob['outputFileName']):
                
                outputFolder = '/'.join(subJob['outputFileName'].split('/')[:-1])
                tmpFolder = '/'.join(subJob['tmpFileName'].split('/')[:-1])
                self.fileLocator.makedirs(outputFolder)
                self.fileLocator.makedirs(tmpFolder)

                # load sample tree and initialize vtype corrector
                sampleTree = SampleTree(subJob['localInputFileNames'], config=self.config)
                if not sampleTree.tree:

                    if len(subJob['inputFileNames']) == 1:
                        # try original naming scheme if reading directly from Heppy/Nano ntuples (without prep)
                        fileNameOriginal = self.pathIN + '/' + subJob['inputFileNames']
                        print "FO:", fileNameOriginal
                        xrootdRedirector = self.fileLocator.getRedirector(fileNameOriginal)
                        sampleTree = SampleTree([fileNameOriginal], config=self.config, xrootdRedirector=xrootdRedirector)
                        if not sampleTree.tree:
                            print "\x1b[31mERROR: file does not exist or is broken, will be SKIPPED!\x1b[0m"
                            continue
                    else:
                        print "\x1b[31mERROR: file does not exist or is broken, will be SKIPPED! (old naming scheme not supported for joining multipel files)\x1b[0m"
                        continue

                # to use this syntax, use "--addCollections Sys.Vtype" for a config file entry like this:
                # [Sys]
                # Vtype = VtypeCorrector.VtypeCorrector(channel='Zll')
                # (instead of passing the tree in the constructor, the setTree method can be used)
                pyModules = []
                for collection in self.collections:
                    if '.' in collection:
                        section = collection.split('.')[0]
                        key = collection.split('.')[1]
                        pyCode = self.config.get(section, key)

                        # import module from myutils
                        moduleName = pyCode.split('(')[0].split('.')[0].strip()
                        if self.debug:
                            print "DEBUG: import module:", moduleName
                            print("\x1b[33mDEBUG: " + collection + ": run PYTHON code:\n"+pyCode+"\x1b[0m")
                        globals()[moduleName] = importlib.import_module(".{module}".format(module=moduleName), package="myutils")

                        # get object
                        wObject = eval(pyCode)

                        # pass the tree and other variables if needed to finalize initialization
                        if hasattr(wObject, "customInit") and callable(getattr(wObject, "customInit")):
                            wObject.customInit({'config': self.config,
                                                'sampleTree': sampleTree,
                                                'tree': sampleTree.tree,
                                                'sample': self.sample,
                                                'channel': self.channel,
                                                })

                        # add callbacks if the objects provides any
                        if hasattr(wObject, "processEvent") and callable(getattr(wObject, "processEvent")):
                            sampleTree.addCallback('event', wObject.processEvent)

                        # add branches
                        if hasattr(wObject, "getBranches") and callable(getattr(wObject, "getBranches")):
                            sampleTree.addOutputBranches(wObject.getBranches())

                        pyModules.append(wObject)

                # DEPRECATED, do not use anymore ---> use BranchTools.TreeFormulas()
                if 'addbranches' in self.collections:
                    writeNewVariables = eval(self.config.get("Regression", "writeNewVariablesDict"))
                    sampleTree.addOutputBranches(writeNewVariables)
                
                # DEPRECATED, do not use anymore ---> use BranchTools.Drop()
                if 'removebranches' in self.collections:
                    bl_branch = eval(config.get('Branches', 'useless_branch'))
                    for br in bl_branch:
                        sampleTree.addBranchToBlacklist(br)
                    bl_branch = eval(config.get('Branches', 'useless_after_sys'))
                    for br in bl_branch:
                        sampleTree.addBranchToBlacklist(br)

                # define output file 
                sampleTree.addOutputTree(subJob['tmpFileName'], cut='1', branches='*', friend=self.opts.friend)
                
                # run processing
                for pyModule in pyModules:
                    if hasattr(pyModule, "beforeProcessing"):
                        getattr(pyModule, "beforeProcessing")()

                sampleTree.process()

                for pyModule in pyModules:
                    if hasattr(pyModule, "afterProcessing"):
                        getattr(pyModule, "afterProcessing")()

                # if output trees have been produced: copy temporary file to output folder
                if sampleTree.getNumberOfOutputTrees() > 0: 
                    try:
                        self.fileLocator.cp(subJob['tmpFileName'], subJob['outputFileName'], force=True)
                        print 'copy ', subJob['tmpFileName'], subJob['outputFileName']
                    except Exception as e:
                        print e
                        print "\x1b[31mERROR: copy from scratch to final destination failed!!\x1b[0m"
                    
                    # delete temporary file
                    try:
                        self.fileLocator.rm(subJob['tmpFileName'])
                    except Exception as e:
                        print e
                        print "WARNING: could not delete file on scratch!"


                # add callback for clean up
                if hasattr(wObject, "cleanUp") and callable(getattr(wObject, "cleanUp")):
                    getattr(wObject, "cleanUp")()

            else:
                print 'SKIP:', subJob['inputFileNames']

argv = sys.argv
parser = OptionParser()
parser.add_option("-S", "--sampleIdentifier", dest="sampleIdentifier", default="", 
                      help="samples you want to run on")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration defining the plots to make")
parser.add_option("-f", "--fileList", dest="fileList", default="",
                              help="list of files you want to run on")
parser.add_option("-b", "--addCollections", dest="addCollections", default="",
                              help="collections to add: vtype")
parser.add_option("-F", "--force", dest="force", action="store_true", help="overwrite existing files", default=False)
parser.add_option("-J", "--join", dest="join", action="store_true", help="chain all files of the sample", default=False)
parser.add_option("-d", "--friend", dest="friend", action="store_true", help="create a friend tree", default=False)

(opts, args) = parser.parse_args(argv)
if opts.config == "":
    opts.config = "config"

xr = XbbRun(opts)
xr.run()

