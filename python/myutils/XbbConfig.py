#!/usr/bin/env python
from __future__ import print_function
import BetterConfigParser
import os

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
