#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)
from myutils import BetterConfigParser
from myutils.pandasConverter import SampleTreesToDataFrameConverter
import resource
from myutils.NewRebinner import Rebinner
import os
import sys
import pickle
import glob
import shutil


# read arguments
argv = sys.argv
parser = OptionParser()
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration file")
parser.add_option("-T", "--tag", dest="tag", default='',
                      help="configuration tag")
parser.add_option("-t","--trainingRegions", dest="trainingRegions", default='',
                      help="cut region identifier")
(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = ["config"]

# Import after configure to get help message
if len(opts.tag.strip()) > 1:
    config = BetterConfigParser()
    config.read("{tag}config/paths.ini".format(tag=opts.tag))
    configFiles = config.get("Configuration", "List").split(' ')
    opts.config = ["{tag}config/{file}".format(tag=opts.tag, file=x.strip()) for x in configFiles]
    print("reading config files:", opts.config)

# load config
config = BetterConfigParser()
config.read(opts.config)


converter = SampleTreesToDataFrameConverter(config) 
converter.loadSamples()
dfs = converter.getDataFrames()
for region,df_dict in dfs.iteritems():
    print(region)
    bin_list = None
    dc = converter.dcMakers[region]
    mva_min = dc.binning["minX"]
    mva_max = dc.binning["maxX"]
    n_bins = dc.binning["nBinsX"]
    try:
        binner = Rebinner(mva_min,mva_max,df_dict['SIG'],df_dict['BKG'])
        bin_list = binner.getBinEdges(n_bins)
    except:
        print ("Could not fit ROC curve. Set rebin method to default")

    if bin_list is None:
        print ("Binning fit did not converge. Set rebin method to default")
        #TODO set rebin method to default
    else:
        rebin_list = "[" + ", ".join(str(bin_list)) + "]"
        print ("rebin_list set to " + rebin_list + ", rebin_method set to 'fixed'")
        #TODO do so!
