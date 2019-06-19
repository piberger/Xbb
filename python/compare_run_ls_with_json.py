#!/usr/bin/env python
import json

jsonFile = 'Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
runLsLists = [
        ['existing_lumis_pp_V11_DoubleMuon.txt', 43, '0'],
        ['existing_lumis_pp_V11_DoubleEG.txt', 44, '1'],
        ['existing_lumis_pp_V11_SingleMuon.txt', 45, '2'],
        ['existing_lumis_pp_V11_SingleElectron.txt', 46, '3'],
        ['existing_lumis_pp_V11_MET.txt', 47, '4'],
        ]
ntupleVersion = "2017 Nano post-proc V11"

print "-"*80
print "run/ls checker for data"
print "JSON is:", jsonFile
print "NTuples:", ntupleVersion
print "-"*80

def runLsListToDict(existingData):
    existingDataDict = {}
    for i in existingData:
        if i[0] not in existingDataDict:
            existingDataDict[i[0]] = {}
        existingDataDict[i[0]][i[1]] = True
    return existingDataDict

with open(jsonFile,'rb') as f:
    jsonData = json.load(f)

existingData = []
for runLsList in runLsLists:
    with open(runLsList[0],'r') as f:
        existingData.append(runLsListToDict(json.load(f)))

runs = sorted(jsonData.keys())
counts = {
        'ok': 0,
        'empty': 0,
        'mixed': 0,
        }
for runLsList in runLsLists:
    counts[runLsList[0]] = 0
print "-"*80
print " legend:"
print "  \x1b[42m \x1b[0m OK: all datasets have events in this lumisection"
print "  - EMPTY: no dataset has events in this lumisection"
print "  \x1b[41m?\x1b[0m SOME: some datasets have events in this lumisection, more than 1 has not"
for runLsList in runLsLists:
    print "  " + '\x1b[%dm%s\x1b[0m'%(runLsList[1], runLsList[2]) + " missing only in " + runLsList[0] 
print "-"*80

for run in runs:
    lsList = jsonData[run]
    for lsRange in lsList:
        printout = ("%d %r:"%(int(run), lsRange)).ljust(24)
        lsCount = 0
        for ls in range(lsRange[0],lsRange[1]+1):
            iRun = int(run)
            lsExisting = [iRun in x and ls in x[iRun] for x in existingData] 
            datasets_empty = [i for i,x in enumerate(lsExisting) if not x]

            if len(datasets_empty) == 0:
                counts['ok'] += 1
                box = '\x1b[42m \x1b[0m'
            elif len(datasets_empty) == len(existingData):
                counts['empty'] += 1
                box = '-'
            elif len(datasets_empty) == 1:
                counts[runLsLists[datasets_empty[0]][0]] += 1
                box = '\x1b[%dm%s\x1b[0m'%(runLsLists[datasets_empty[0]][1], runLsLists[datasets_empty[0]][2])
            else:
                counts['mixed'] += 1
                box = '\x1b[41m?\x1b[0m'
            printout += box

            lsCount += 1
            if lsCount > 300:
                printout += "\n" + "".ljust(24)
                lsCount = 0
        print printout
print "%r"%counts



