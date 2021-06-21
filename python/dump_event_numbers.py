import ROOT
import glob
from myutils.sampleTree import SampleTree
import sys
import os
from myutils.XbbConfig import XbbConfigReader, XbbConfigTools
from myutils import ParseInfo
from myutils.BranchList import BranchList
from myutils.FileLocator import FileLocator

ROOT.gROOT.SetBatch(True) 
ROOT.gSystem.Load("../interface/VHbbNameSpace_h.so")

#use this if its just one root file
#files = ["/pnfs/psi.ch/cms/trivcat/store/user/krgedia/VHbb/Zll/VHbbPostNano2018/prep_test/DoubleMuon/tree_Run2018A-Nano14Dec2018-v180_190426_091335_0000_1 _ece43a8e07c7252be5b485d4343748de876253455fdf9d5f1cfc2f11.root"]

#use this if you want to use wildcard root file address. It gives you list of all root files in the directory
files = glob.glob("/pnfs/psi.ch/cms/trivcat/store/user/creissel/VHbb/Wlv/VHbbPostNano2016_V11/2020_05_15/sys_withTop/SingleMuon/tree_*.root")

#Use one of the above two options

#Here you parse the config file
config = XbbConfigTools(config=XbbConfigReader.read("Wlv2016"))

#Once you parse the config file, you can access the quantities from the config. 
sel_formula  = str(config.get("Cuts","ttbar_high_Wmn"))

#Here you kind of TChain all the 'Event' TTrees from all the TTrees from the list 'files' you provided and use it latter as an iterator
sampleTree = SampleTree(files, treeName='Events', xrootdRedirector='root://t3dcachedb03.psi.ch:1094/')
nEvents = sampleTree.GetEntries()

#Here you add the formula you want
sampleTree.addFormula("f",sel_formula)

j=0
#Here you iterate over all the events from the TChained TTrees
for event in sampleTree:    
    #Here you evaluate the fomula for each event
    passed = sampleTree.evaluate("f")
    if passed:
        j=j+1
        #if (j<50): 
        if (j<nEvents): 
            #200 is just the number of events you want to iterate.
            #you can get other variables for event as well. Like event.Hmass and so on...
            print(event.event, event.run)

