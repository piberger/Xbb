#! /usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import sys
import os
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools
from myutils import ParseInfo
from myutils.FileLocator import FileLocator
from myutils.XbbTools import XbbTools

argv = sys.argv
parser = OptionParser()
parser.add_option("-T","--tag", dest="tag", default='', help="config tag")
parser.add_option("-D","--directory", dest="directory", default='MVAout', help="directory name, e.g. MVAout")
parser.add_option("-S","--sample", dest="sample", default='TT*', help="sample")
(opts, args) = parser.parse_args(argv)

config = XbbConfigTools(config=XbbConfigReader.read(opts.tag))
path = config.get("Directories", opts.directory)
sampleInfoDirectory = config.get('Directories', 'samplefiles')
info = ParseInfo(samples_path=path, config=config)

# only take first sample which matches
sampleIdentifier = XbbTools.filterSampleList(info.getSampleIdentifiers(), XbbTools.parseSamplesList(opts.sample))[0]

# get list of ORIGINAL file names for this sample: /store/...
sampleTreeFileNames = XbbTools.getSampleTreeFileNames(sampleInfoDirectory, sampleIdentifier)

fileLocator = FileLocator(config=config)

# get local name of ffirst file
localFilename     = fileLocator.getFilePath(path, sampleIdentifier, sampleTreeFileNames[0])
print(localFilename)
