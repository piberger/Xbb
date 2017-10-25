#!/usr/bin/env python
from __future__ import print_function
import sys
import random
sys.path.append('../')
from myutils.sampleTree import SampleTree as SampleTree

scratchDirectory = '.'

def getTree():
    fileNames = [scratchDirectory + '/tree_%d.root'%i for i in range(10)]
    return SampleTree(fileNames)

def testNumberOfEntries(sampleTree):
    return sampleTree.tree.GetEntries() == 1000000


def testSimpleTreeIteration(sampleTree):
    nSelectedEvents = 0
    for event in sampleTree:
        if event.nJet == 9:
            s1 = sum([event.Jet[x] for x in range(event.nJet)])
            if s1 > 900:
                nSelectedEvents += 1
    nSelectedEventsDraw = sampleTree.tree.Draw("a", "nJet==9&&Sum$(Jet)>900", "goff")
    print ("method A:", nSelectedEvents)
    print ("method B:", nSelectedEventsDraw)
    return nSelectedEventsDraw == nSelectedEvents


def testMultiOutput():
    sampleTree = getTree()

    # define some random cuts
    cuts = [
        "nJet==5&&Sum$(Jet)>500",
        "nJet==6&&Sum$(Jet)>600",
        "nJet==7&&Sum$(Jet)>700",
        "nJet==8&&Sum$(Jet)>800",
        "nJet==9 && Sum$(Jet)>800 && a<0 && (b>30 || b > 50)",
        "nJet==9 && Sum$(Jet)>800 && (a<0 && (b>30 || b > 50)) || (a>0 && (b>10 || b > 90)) || (a>0.8 && (b>5 || b > 50))",
    ]

    # add some random cut
    randomCuts = ["(a<%f && (b>%f || c > %f))"%(random.gauss(0,0.5), random.uniform(0,50), random.uniform(0,2)) for i in range(50)]
    cuts.append('||'.join(randomCuts))

    # write skimmed subtrees to file
    for i, cut in enumerate(cuts):
        sampleTree.addOutputTree(scratchDirectory + '/tree_skimmed_%d.root'%i, cut, '')
    sampleTree.process()

    # load subtrees and count events
    resultsMethodA = [SampleTree([scratchDirectory + '/tree_skimmed_%d.root'%i]).tree.GetEntries() for i, cut in enumerate(cuts)]

    # count directly
    resultsMethodB = [sampleTree.tree.Draw("a", cut, "goff") for i, cut in enumerate(cuts)]

    print(resultsMethodA)
    print(resultsMethodB)

    return all([resultsMethodA[i] == resultsMethodB[i] for i in range(len(resultsMethodA))])


sampleTree = getTree()

results = [
    ["num entries", testNumberOfEntries(sampleTree)],
    ["simple tree iteration", testSimpleTreeIteration(sampleTree)],
    ["multi output", testMultiOutput()],
]

for result in results:
    if result[1]:
        print("\x1b[42m\x1b[97m[OK] "+result[0], "\x1b[0m")
    else:
        print("\x1b[41m\x1b[97m[ERROR] "+result[0], "\x1b[0m")