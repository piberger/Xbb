#! /usr/bin/env python
import os, pickle, sys, ROOT
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser
from myutils import BetterConfigParser, copytree, copytreePSI, ParseInfo
#import utils

print 'start prepare_environment_with_config.py'

import os
if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

argv = sys.argv

#get files info from config
parser = OptionParser()
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="directory config")
parser.add_option("-S", "--samples", dest="names", default="",
                              help="samples you want to run on")
parser.add_option("-f", "--filelist", dest="filelist", default="",
                              help="list of files you want to run on")

(opts, args) = parser.parse_args(argv)

config = BetterConfigParser()
config.read(opts.config)

namelist=opts.names.split(',')
filelist=opts.filelist.split(';')
print "namelist:",namelist
print "len(filelist)",len(filelist),"filelist[0]:",filelist[0]

pathIN = config.get('Directories','PREPin')
pathOUT = config.get('Directories','PREPout')
samplesinfo=config.get('Directories','samplesinfo')
sampleconf = BetterConfigParser()
sampleconf.read(samplesinfo)

whereToLaunch = config.get('Configuration','whereToLaunch')
TreeCopierPSI = config.get('Configuration','TreeCopierPSI')
prefix=sampleconf.get('General','prefix')

info = ParseInfo(samplesinfo,pathIN)
print "samplesinfo:",samplesinfo
print "info:",info
for job in info:
    if not job.name in namelist and not job.identifier in namelist:
        continue
    if job.subsample:
        continue
    if('lxplus' in whereToLaunch):
        pass
        # TreeCopier class
        #utils.TreeCopier(pathIN, pathOUT, job.identifier, job.prefix, job.addtreecut)
    else:
        if TreeCopierPSI == 'True':
            # copytreePSI class, allowing for single file workflow
            samplefiles = config.get('Directories','samplefiles')
            copytreePSI(samplefiles,pathOUT,prefix,job.prefix,job.identifier,'',job.addtreecut, config, filelist)
        else:
          # copytree function
          copytree(pathIN,pathOUT,prefix,job.prefix,job.identifier,'',job.addtreecut, config)

print 'end prepare_environment_with_config.py'
