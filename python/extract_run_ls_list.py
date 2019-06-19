#!/usr/bin/env python
import ROOT
import sys
import os
from myutils.sampleTree import SampleTree

# input: file with one tree filename per line, e.g.
# /path/to/tree_1.root
# /path/to/tree_2.root

# output: txt file with json compatible list of [run, ls]
# [[304292, 29], [304663, 510], [302163, 561], ... ]

print "usage: %s outputfile.txt inputfile.txt [redirector]"

if os.path.isfile(sys.argv[2]):
    outputFileName = sys.argv[1]
    sampleTree = SampleTree(sys.argv[2], 'Events', xrootdRedirector=sys.argv[3] if len(sys.argv) > 3 else '') 
else:
    raise Exception("Input file not found!", sys.argv[2])

sampleTree.tree.SetBranchStatus("*", 0)
sampleTree.tree.SetBranchStatus("run", 1)
sampleTree.tree.SetBranchStatus("luminosityBlock", 1)

runLumi = {}
for i in sampleTree:
    if (i.run, i.luminosityBlock) not in runLumi:
        runLumi[(i.run, i.luminosityBlock)] = True

with open(outputFileName, 'w') as f:
    f.write("%r"%[list(x) for x in runLumi.keys()])

