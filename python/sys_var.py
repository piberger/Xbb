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

# test replacement rules
replacementRulesList = XbbTools.getReplacementRulesList(config, opts.syst)
for x in nominalVariables:
    sysVar = XbbTools.getSystematicsVariationTemplate(x, replacementRulesList) 
    sysVar = sysVar.replace('{syst}', opts.syst).replace('{UD}', opts.ud)
    print(sysVar)

##replacementRulesList = XbbTools.getReplacementRulesList(config, opts.syst)
##sysVars = []
#for i,x in enumerate(nominalVariables):
#    sysVar = XbbTools.getSystematicsVariationTemplate(x, replacementRulesList)
#    sysVar = sysVar.replace('{syst}', opts.syst).replace('{UD}', opts.ud)
#    print(sysVar)
#    sysVars.append(sysVar)
#    if varsFromConfig[i]!=sysVars[i]:
#        print("\x1b[31mMISMATCH:")
#        print(" config:   ", varsFromConfig[i])
#        print(" generated:", sysVars[i], "\x1b[0m")

# test XbbMvaInputsList class
from myutils.XbbTools import XbbMvaInputsList
inputsList = XbbMvaInputsList(nominalVariables, config=config)
for i,x in enumerate(nominalVariables):
    print("NOMINAL:", inputsList.get(i))
    print("     UP:", inputsList.get(i, syst=opts.syst, UD='Up'))
    print("   DOWN:", inputsList.get(i, syst=opts.syst, UD='Down'))
