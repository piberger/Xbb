#!/usr/bin/env python
import sys
import os
import re
from ROOT import TFile, TIter, TKey, TH2F, Double
import json
import pickle

args = sys.argv[1:]
if len(args) > 0: inputTree = args[0]
print "input tree=", inputTree

if len(args) > 1: outputJson = args[1]
print "output json=", outputJson

#from array import *
#import math
#import pickle


def getValueError(value, error):
    binEntry={}
    binEntry["value"]=value
    binEntry["error"]=error
    print 'binEntry is', binEntry
    return binEntry

def getHistoContentInJson(histo):
    xBins={}
    histoName=histo.GetName()
    xaxisName = re.split("_",histoName)[0]
    yaxisName = re.split("_",histoName)[1]
    #if (histo.GetYaxis().GetNbins()==1):
    if (histo.GetYaxis().GetNbins()==1):
        print "this is a 1D histo"
        #for i in range(0,histo.GetXaxis().GetNbins()+1):
        for i in range(0,histo.GetN()):
            print 'i is', i
            x = Double(999)
            x_hi = 999
            x_low = 999
            y = Double(999)
            y_hi = 999
            y_low = 999
            histo.GetPoint(i,x,y)
            x_hi = x+ histo.GetErrorXhigh(i)
            x_low = x - histo.GetErrorXlow(i)
            y_hi = histo.GetErrorYhigh(i)
            y_low = histo.GetErrorYlow(i)
            xBinValue=xaxisName+":["+str(x_low)+","+str(x_hi)+"]"
            print 'xBinValue is', xBinValue
            xBins[xBinValue]=getValueError(y, max(y_low,y_hi))
    return xBins

data={}

rootoutput = TFile.Open(inputTree)

nextkey = TIter(rootoutput.GetListOfKeys())
key = nextkey.Next()
while (key): #loop
    efficienciesForThisID = {}
    print 'key name is', key.GetName()
    theHistoPlot = rootoutput.Get(key.GetName())
    efficienciesForThisID[key.GetName()] = getHistoContentInJson(theHistoPlot)
    data[key.GetName()]=efficienciesForThisID
    key = nextkey.Next()
    print 'data is', data


with open(outputJson,"w") as f:
    json.dump(data, f, sort_keys = False, indent = 4)
