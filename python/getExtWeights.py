#!/usr/bin/env python
import ROOT
import sys
ROOT.gROOT.SetBatch(True)
from myutils import BetterConfigParser, ParseInfo
import glob

# 1) ./getExtWeights.py configname
# 2) ./getExtWeight.py configname verify

def countEvents(rootFileName):

    f = ROOT.TFile.Open(rootFileName)
    if not f or f.IsZombie():
        print "\x1b[31mnot found:",rootFileName,"\x1b[0m"
    tree = f.Get("tree")

    nevents = 1.* tree.Draw("","1")
    f.Close()
    return nevents

def getExtWeights(config, extParts):

    sysOut = config.get('Directories','SYSout').strip()
    t3proto = 'root://t3dcachedb.psi.ch:1094'
    sysOutMountedPath = sysOut.replace(t3proto,'').replace('root://t3dcachedb03.psi.ch:1094','')
    extPartCounts = {}
    for extPart in extParts:
        fileMask = "{path}/{sample}/{tree}.root".format(path=sysOutMountedPath, sample=extPart, tree='*')
        print fileMask
        extPartFiles = glob.glob(fileMask)
        print extPart,"=>",len(extPartFiles),"files"
        extPartCounts[extPart] = 0
        for extPartFile in extPartFiles:
            extPartCounts[extPart] += countEvents(t3proto + '/' + extPartFile)
            #root://t3dcachedb03.psi.ch:1094
    # get total count
    totalCount = sum([n for sampleName,n in extPartCounts.iteritems()])

    # relative weights
    for sampleName,n in extPartCounts.iteritems():
        print sampleName,":",(1.0*n/totalCount if totalCount > 0 else '-')

config = BetterConfigParser()
configPath = sys.argv[1] + '/samples_nosplit.ini'
config.read(configPath)
configPath = sys.argv[1] + '/paths.ini'
config.read(configPath)

sampleDict = {}
sampleWeights = {}
verify = len(sys.argv) > 2 and sys.argv[2]=='verify'
for section in config.sections():
    #try:
    #    sampleName = config.get(section, 'sampleName')
    #except:
    sampleName = section
    sampleNameShort = sampleName
    if '_ext' in sampleName:
        sampleNameShort = sampleName.split('_ext')[0]
    elif '_backup' in sampleName:
        sampleNameShort = sampleName.split('_backup')[0]
    if sampleNameShort in sampleDict:
        sampleDict[sampleNameShort].append(sampleName)
    else:
        sampleDict[sampleNameShort] = [sampleName]
    if verify:
        extweight = 0
        try:
            extweight = float(config.get(section, 'extweight'))
        except:
            pass
        sampleWeights[sampleNameShort] = float(sampleWeights[sampleNameShort]) + extweight if sampleNameShort in sampleWeights else extweight

if verify:
    for sampleNameShort,totalWeight in sampleWeights.iteritems():
        if sampleNameShort in sampleDict and len(sampleDict[sampleNameShort])>1:
            print sampleNameShort,":",totalWeight
else:
    for sample,extParts in sampleDict.iteritems():
        if len(extParts) > 1:
            print '-'*80
            print sample,":"
            getExtWeights(config,extParts)

