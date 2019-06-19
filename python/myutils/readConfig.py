from __future__ import print_function
from BetterConfigParser import BetterConfigParser
import os

class readConfig(object):

    @staticmethod
    def fromTag(tag):
        pathconfig = tag + 'config/paths.ini'
        if not os.path.isfile(pathconfig):
            print("\x1b[31mERROR: file missing:", pathconfig, "\x1b[0m")
            raise Exception("ConfigMissing")

        # read path config
        config = BetterConfigParser()
        config.read(pathconfig)

        # get list of config files
        configList = [x.strip() for x in config.get('Configuration', 'List').split(' ') if len(x.strip()) > 0]
        
        # read full config
        config2 = BetterConfigParser()
        for configFile in configList:
            config2.read(tag + 'config/' + configFile)

        return config2

