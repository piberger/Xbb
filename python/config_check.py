#! /usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import sys
import os
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools, XbbConfigChecker

argv = sys.argv
parser = OptionParser()
parser.add_option("-T","--tag", dest="tag", default='', help="config tag")
parser.add_option("--set", action="append", dest="setOptions", help="set config option. --set='Section.option:value'")
(opts, args) = parser.parse_args(argv)

config = XbbConfigTools(config=XbbConfigReader.read(opts.tag))
if opts.setOptions is not None and len(opts.setOptions) > 0:
    setOptions = ';'.join(opts.setOptions)
    config.setList(setOptions) 

xcc = XbbConfigChecker(config)
xcc.checkAll()
xcc.printErrors()
sys.exit(xcc.getStatus())
