#! /usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import sys
import os
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools
from myutils import ParseInfo

argv = sys.argv
parser = OptionParser()
parser.add_option("-T","--tag", dest="tag", default='', help="config tag")
parser.add_option("-V","--value", dest="val", default='', help="section.value")
(opts, args) = parser.parse_args(argv)

config = XbbConfigTools(config=XbbConfigReader.read(opts.tag))

print(config.get(opts.val.split('.')[0],opts.val.split('.')[1]))
