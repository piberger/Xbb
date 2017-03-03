import glob
import os
import sys

if len(sys.argv) < 2:
    print "missing sysout folder as argument"
    exit(2)

#basePath = "/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/sys_v5" 
basePath = sys.argv[1]
globPath = basePath + "/*.root"
rootFileNames = glob.glob(globPath)
for rootFileName in rootFileNames:
    size = os.stat(rootFileName).st_size
    sampleName = rootFileName.split('/')[-1].replace('ZmmH.BestCSV.heppy.','').replace('.root','')
    print sampleName
    
    globPathSplit = basePath + '/' + sampleName + '/*.root'
    rootFileNamesSplit = glob.glob(globPathSplit)
    nFiles = 0
    totalSize = 0
    for rootFileNameSplit in rootFileNamesSplit:
        nFiles += 1
        totalSize += os.stat(rootFileNameSplit).st_size

    difference = 1.0 * size / totalSize
    if difference < 0:
        difference = -difference

    if difference < 0.95 or difference > 1.50:
        print " => \x1b[31mWARNING: merged: {mergedSize} all files: {totalSize} fraction: {diff} percent\x1b[0m".format(mergedSize=size, totalSize=totalSize, diff=100.0*difference)
    else:
        print " => \x1b[32mmerged: {mergedSize} all files: {totalSize}\x1b[0m".format(mergedSize=size, totalSize=totalSize)



