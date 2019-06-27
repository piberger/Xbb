#! /usr/bin/env python
import os, pickle, sys, ROOT
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser
from myutils import BetterConfigParser, copytree, ParseInfo

print "Launch me with:"
print "./print_cross_sections.py --config ZvvHbb13TeVconfig/paths.ini"

argv = sys.argv

#get files info from config
parser = OptionParser()
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="directory config")
#parser.add_option("-S", "--samples", dest="names", default="",
#                              help="samples you want to run on")

(opts, args) = parser.parse_args(argv)

config = BetterConfigParser()
config.read(opts.config)

#namelist=opts.names.split(',')
#print "namelist:",namelist

pathIN = config.get('Directories','PREPin')
pathOUT = config.get('Directories','PREPout')
samplesinfo=config.get('Directories','samplesinfo')
sampleconf = BetterConfigParser()
sampleconf.read(samplesinfo)

prefix=sampleconf.get('General','prefix')

info = ParseInfo(samples_path=pathIN, config=config)
print "samplesinfo:",samplesinfo
cross_sections={}
samples = []
for job in info:
    if not job.identifier in samples:
        if type(job.xsec) is list: job.xsec = job.xsec[0]
        cross_sections[job.identifier]=job.xsec
        samples.append(job.identifier)

for sample in samples:
    print sample,"\t",cross_sections[sample]
#    print dir(job)
#    print "job.name:",job.name," job.cross_section:",job.xsec
#    print "job.prefix:",job.prefix
#    if not job.name in namelist: 
#        continue
#    if job.subsample:
#        continue
#    copytree(pathIN,pathOUT,prefix,job.prefix,job.identifier,'',job.addtreecut)
