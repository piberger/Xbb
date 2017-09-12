#!/usr/bin/env python
from __future__ import print_function

from myutils.sampleTree import SampleTree as SampleTree

def test_branches(tree):
    print ('#### TEST branches ####')

    # print list of branches
    branches = tree.GetListOfBranches()
    print ('BRANCHES:')
    for branch in branches:
        print ('->', branch.GetName())

    print ('#### TEST branches END ####')


def test_loop(tree):
    print ('#### TEST loop ####')
    # loop over first few events
    i = 0
    imax = 10
    for event in tree:
        print (event.V_pt)
        i += 1
        if i>imax:
            print ('stop after ', imax, ' events')
            break
    print ('#### TEST loop END ####')

def test_loop2(tree):
    print ('#### TEST loop2 ####')
    # loop over all events
    i = 0
    for event in tree:
        i += 1
    print ('found ', i, ' events')
    print ('#### TEST loop2 END ####')

def test_cut(tree):
    print ('#### TEST cut ####')
    print ('add V_pt > 100 cut')
    tree.addFormula('ptCut','V_pt>100')

    # loop over first few events
    i = 0
    imax = 10
    for event in tree:
        print (event.V_pt, '===>', tree.evaluate('ptCut'))
        i += 1
        if i>imax:
            print ('stop after ', imax, ' events')
            break
    print ('#### TEST cut END ####')



sampleTreeBkg = SampleTree('test/bkg.txt')

test_branches(sampleTreeBkg)
test_loop(sampleTreeBkg)
test_loop2(sampleTreeBkg)
test_cut(sampleTreeBkg)


