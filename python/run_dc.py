#!/usr/bin/env python
from __future__ import print_function
import os, sys, ROOT, warnings, pickle
ROOT.gROOT.SetBatch(True)
from array import array
from math import sqrt
from copy import copy, deepcopy
#suppres the EvalInstace conversion warning bug
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )
from optparse import OptionParser
from myutils import BetterConfigParser, Sample, progbar, printc, ParseInfo, Rebinner, HistoMaker
import re
import json
from myutils import NewTreeCache as TreeCache
from myutils.sampleTree import SampleTree as SampleTree
from myutils.Datacard import Datacard
from myutils.BranchList import BranchList
from myutils.FileList import FileList

class RunDatacards(object):

    def __init__(self, config, region, verbose=False, forceRedo=True):
        self.verbose = verbose
        self.forceRedo = forceRedo
        self.config = config
        self.region = region
        self.dcMaker = Datacard(config=self.config, region=region)

    def run(self):
        if self.dcMaker:
            self.dcMaker.run()
        else:
            print ("\x1b[31mERROR: could not produce datacards\x1b[0m")


if __name__ == "__main__":
    # read arguments
    argv = sys.argv
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                              help="Verbose mode.")
    parser.add_option("-C", "--config", dest="config", default=[], action="append",
                          help="configuration file")
    parser.add_option("-t", "--regions", dest="regions", default='',
                          help="cut regions identifier")
    parser.add_option("-f", "--force", action="store_true", dest="force", default=False,
                          help="force overwriting of already existing datacards")
    (opts, args) = parser.parse_args(argv)
    if opts.config == "":
            opts.config = "config"

    # Import after configure to get help message
    from myutils import BetterConfigParser, mvainfo, ParseInfo

    # load config
    config = BetterConfigParser()
    config.read(opts.config)

    # if no region is given in argument, run it for all of them
    regionsListString = opts.regions if len(opts.regions.strip())>0 else config.get('LimitGeneral', 'List')
    regions = [x.strip() for x in regionsListString.split(',') if len(x.strip()) > 0]
    
    for region in regions:
        runDC = RunDatacards(config, region)
        runDC.run()
