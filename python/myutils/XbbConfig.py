#!/usr/bin/env python
from __future__ import print_function
import BetterConfigParser
import os
from copytreePSI import filelist
from FileLocator import FileLocator

# helper class to read full config object
# use:
#      config = XbbConfigReader.read('Zll2017')

class XbbConfigReader(object):

    def __init__(self):
        self.config = None

    @staticmethod
    def read(configTag):

        configDirectory = configTag + 'config/'
        debug = 'XBBDEBUG' in os.environ
        if debug:
            print("DEBUG: read configuration \x1b[35m", configTag, "\x1b[0m")

        # paths.ini contains list of config files to use, relative to configDirectory
        pathconfig = BetterConfigParser.BetterConfigParser()
        pathconfig.read(configDirectory + '/paths.ini')
        configFiles = pathconfig.get('Configuration', 'List').split(' ')

        # read actual config
        config = BetterConfigParser.BetterConfigParser()
        for configFile in configFiles:
            if debug:
                print("DEBUG: --> read configFile:", configFile)
            config.read(configDirectory + configFile)
        if debug:
            print('DEBUG: \x1b[35m read', len(config.sections()), 'sections\x1b[0m')

        return config

class XbbConfigTools(object):

    def __init__(self, config):
        self.config = config
        self.fileLocator = None

    def initFS(self, force=False): 
        if self.fileLocator is None or force:
            self.fileLocator = FileLocator(config=self.config)

    # list of DATA sample names
    def getData(self):
        return eval(self.config.get('Plot_general', 'Data'))

    # list of MC sample names
    def getMC(self):
        return eval(self.config.get('Plot_general', 'samples'))
    
    # list of all sample names (data + mc)
    def getUsedSamples(self):
        return self.getMC() + self.getData()

    # get list of original file names: /store/...
    def getOriginalFileNames(self, sampleIdentifier):
        return filelist(self.config.get('Directories', 'samplefiles'), sampleIdentifier)

    # get list of file names (e.g. in SYSout folder)
    def getFileNames(self, sampleIdentifier, folder='SYSout'):
        self.initFS()
        originalFileNames = self.getOriginalFileNames(sampleIdentifier)
        samplePath = self.config.get('Directories', folder)
        fileNames = ["{path}/{subfolder}/{filename}".format(path=samplePath, subfolder=sampleIdentifier, filename=self.fileLocator.getFilenameAfterPrep(x)) for x in originalFileNames]
        return fileNames

    def has_section(self, section):
        return self.config.has_section(section)

    def has_option(self, section, option):
        return self.config.has_section(section) and self.config.has_option(section, option)

    def get(self, section, option, default=None):
        if default is not None:
            if self.has_option(section, option):
                return self.config.get(section, option)
            else:
                return default
        else:
            return self.config.get(section, option)

    def getPlotVariableSections(self):
        return [x for x in self.config.sections() if x.startswith('plotDef:')]

