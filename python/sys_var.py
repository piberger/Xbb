#! /usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import sys
import os
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools
from myutils.XbbTools import XbbTools
from myutils import ParseInfo

# example: ./sys_var.py -T Zvv2017 -S jerReg -R SR_medhigh_Znn

argv = sys.argv
parser = OptionParser()
parser.add_option("-T","--tag", dest="tag", default='', help="config tag")
parser.add_option("-R","--region", dest="region", default='', help="region")
parser.add_option("-S","--syst", dest="syst", default='', help="syst")
parser.add_option("-D","--ud", dest="ud", default='Up', help="Up/Down")
(opts, args) = parser.parse_args(argv)

print("TAG:", opts.tag)
print("REGION:", opts.region)
print("SYST:", opts.syst)
print("DIRECTION:", opts.ud)

config = XbbConfigTools(config=XbbConfigReader.read(opts.tag))
treeVarSet = config.get(opts.region, 'treeVarSet') 
nominalVariables = config.get(treeVarSet, 'Nominal').split(' ')

replacementRulesList = XbbTools.getReplacementRulesList(config, opts.syst)
for x in nominalVariables:
    sysVar = XbbTools.getSystematicsVariationTemplate(x, replacementRulesList) 
    sysVar = sysVar.replace('{syst}', opts.syst).replace('{UD}', opts.ud)
    print(sysVar)

