from __future__ import print_function
import ROOT
import os
import sys
import array
import numpy as np
from XbbConfig import XbbConfigReader, XbbConfigTools

class PostFitWeight(object):

    def __init__(self, config, region):
        self.config = config
        self.region = region
        self.postFitShapesFile = ROOT.TFile.Open(self.config.get('Fit', 'PostFitShapes'), "READ")
        # apply postfit/prefit reweighting only if pre-fit contribution is larger than the threshold
        # combine puts small epsilon values instead of zero sometimes
        self.preFitThreshold = 1.0e-4
        self.limits = [0.0, 5.0]
    
    def getDatacardProcessName(self, groupName):
        dcNameDict = eval(self.config.get('LimitGeneral', 'Dict'))
        if groupName == 'DATA':
            processName = 'data_obs'
        elif groupName in dcNameDict: 
            processName = dcNameDict[groupName]
        else:
            processName = groupName
        if len(processName.strip()) < 1:
            print("\x1b[41m\x1b[37mERROR: process empty for groupName=", groupName, "\x1b[0m")
            raise Exception("ConfigError")
        return processName

    def getDatacardRegionName(self, region):
        dcRegionNameDict = eval(self.config.get('Fit', 'regions'))
        return dcRegionNameDict[region]

    def getWeight(self, sampleGroup):
        dcProcess = self.getDatacardProcessName(sampleGroup)
        dcRegion  = self.getDatacardRegionName(self.region)

        postFitShapes = self.postFitShapesFile.Get(dcRegion + '_postfit/' + dcProcess)
        preFitShapes  = self.postFitShapesFile.Get(dcRegion + '_prefit/' + dcProcess)

        var = self.config.get('dc:' + self.region, 'var')

        binningMethod = self.config.get('dc:' + self.region, 'rebin_method') if self.config.has_option('dc:' + self.region, 'rebin_method') else None
        if binningMethod in ['fixed', 'list']:
            bins = np.array(eval(self.config.get('dc:' + self.region, 'rebin_list')))
        else:
            if self.config.has_option('dc:' + self.region, 'range'):
                varRange = self.config.get('dc:' + self.region, 'range')
                bins = np.linspace(float(varRange.split(',')[1]),float(varRange.split(',')[2]),int(varRange.split(',')[0])+1)
            elif self.config.has_option('dc:' + self.region, 'min'):
                bins = np.linspace(float(self.config.get('dc:' + self.region, 'min')), float(self.config.get('dc:' + self.region, 'max')), int(self.config.get('dc:' + self.region, 'nBins'))+1)
            else:
                raise Exception("VariableRange")
        try:
            weightStrings = []
            for i in range(postFitShapes.GetXaxis().GetNbins()):
                # avoid huge ratio due to very small contribution << 1 in pre-fit shapes
                r = postFitShapes.GetBinContent(1+i) / preFitShapes.GetBinContent(1+i) if preFitShapes.GetBinContent(1+i) > self.preFitThreshold else 1.0
                r = max(min(r,self.limits[1]),self.limits[0])
                weightStrings.append("({var}>={lowEdge}&&{var}<{highEdge})*{weight}".format(var=var,lowEdge=bins[i],highEdge=bins[i+1],weight=r))
            weightString = "+".join(weightStrings)
        except Exception as e:
            print("\x1b[31mERROR: can't apply post-fit weights:",e,", using pre-fit instead for this process.\x1b[0m")
            weightString = "1.0"
        return weightString

if __name__ == '__main__':

    config = XbbConfigTools(XbbConfigReader.read('Zll2017'))

    pfw = PostFitWeight(config, "SR_low_Zmm")
    print(pfw.getWeight("TT"))
    print("-")
    
    pfw = PostFitWeight(config, "Zlf_low_Zmm")
    print(pfw.getWeight("TT"))

