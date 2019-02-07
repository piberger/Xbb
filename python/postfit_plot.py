#!/usr/bin/env python
from __future__ import print_function
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)

from myutils.NewStackMaker import NewStackMaker as StackMaker
from myutils.samplesclass import Sample
import os,sys
import array
import math

class PostfitPlotter(object):

    def __init__(self, config, region, vars=None, directory="shapes_fit_s", title=None):
        self.config = config
        self.region = region
        self.fitRegions = eval(self.config.get('Fit', 'regions'))
        self.dcRegion = self.fitRegions[self.region]
        self.var = "postfitDNN"
        self.directory = directory
        self.shapesFile = None
        self.plotPath = config.get('Directories', 'plotpath')
        self.title = None # "CMS #scale[0.8]{work in progress}"
        self.blindBins = []
        self.plotText = [""]
        if self.config.has_option('Fit', 'plotText'):
            self.plotText = eval(self.config.get('Fit', 'plotText'))

        if self.config.has_section('Fit:'+self.region):
            if self.config.has_option('Fit:'+self.region, 'var'):
                self.var = self.config.get('Fit:'+self.region, 'var')
            if self.config.has_option('Fit:'+self.region, 'blindBins'):
                self.blindBins = eval(self.config.get('Fit:'+self.region, 'blindBins'))
            if self.config.has_option('Fit:'+self.region, 'plotText'):
                self.plotText += eval(self.config.get('Fit:'+self.region,'plotText'))

    def prepare(self):
        shapesFileName = self.config.get('Fit', 'FitDiagnosticsDump')
        self.shapesFile = ROOT.TFile.Open(shapesFileName, "READ")

        # dump S/B
        shapeS = self.getShape("total_signal")
        shapeB = self.getShape("total_background")
        print("file:", self.shapesFile)
        print("shape:", shapeS, shapeB)
        print(self.region,"-"*40)
        print( ("bin").ljust(5), ("S").ljust(8), ("B").ljust(8))
        sum_s_over_sqrtb = 0.0
        sum_s = 0.0
        sum_b = 0.0
        sum_med_z_a = 0.0
        for i in range(shapeS.GetXaxis().GetNbins()):
            s = shapeS.GetBinContent(1+i)
            b = shapeB.GetBinContent(1+i)
            print( ("%d"%i).ljust(5), ("%1.2f"%s).ljust(8), ("%1.2f"%b).ljust(8))

            sum_s_over_sqrtb += s*s/b if b>0 else 0
            sum_s += s
            sum_b += b
            sum_med_z_a += 2.0* ( (s+b) * math.log(1.0 + s/b) - s) if s > 0 else 0.0
        sum_s_over_sqrtb = math.sqrt(sum_s_over_sqrtb)
        sum_med_z_a = math.sqrt(sum_med_z_a)
        print("TOTAL: s/sqrt(b):", "%1.3f"%sum_s_over_sqrtb, " s:",sum_s, " b:",sum_b, " med[Z]=sqrt(q_A)=", sum_med_z_a)


    def getShape(self, process):
        histogramName = self.directory + '/' + self.dcRegion + '/' + process
        print("DEBUG: get shape ", histogramName)
        histogram = self.shapesFile.Get(histogramName)
        print("DEBUG: -->", histogram)
        return histogram

    def run(self):
        self.dcDict = eval(self.config.get('LimitGeneral','Dict'))
        self.reverseDcDict = {v:k for k,v in self.dcDict.iteritems()}
        self.setup = eval(self.config.get('LimitGeneral','setup'))
        
        self.stack = StackMaker(self.config, self.var, self.region, True, self.setup, '_', title=self.title)
        self.stack.setPlotText(self.plotText)

        # add MC
        print("INFO: setup = \x1b[31m", self.setup, "\x1b[0m")
        for process in self.setup:
            histogram = self.getShape(self.dcDict[process])
            if histogram:
                self.stack.histograms.append({
                        'name': process, 
                        'histogram': histogram, 
                        'group': process
                    })
            else:
                print("\x1b[31mINFO: empty: ",process,"\x1b[0m")
        
        # add DATA
        dataHistogram = self.getShape("data") 
        pointX = array.array('d', [0.0, 0.0])
        pointY = array.array('d', [0.0, 0.0])

        # blind last few bins
        for i in range(dataHistogram.GetN()):
            dataHistogram.GetPoint(i, pointX, pointY)
            if int(pointX[0]+1) in self.blindBins:
                dataHistogram.SetPoint(i, -100, -100)

        # style data
        dataHistogram.SetMarkerColor(ROOT.kBlack)
        dataHistogram.SetMarkerStyle(20)

        self.stack.histograms.append({
                'name': 'DATA', 
                'histogram': dataHistogram,
                'group': 'DATA'
            })

        # draw
        self.stack.Draw(outputFolder=self.plotPath, prefix='{region}__{var}_'.format(region=self.region, var=self.directory))


if __name__ == "__main__":
    # read arguments
    argv = sys.argv
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                              help="Verbose mode.")
    parser.add_option("-C", "--config", dest="config", default=[], action="append",
                          help="configuration file")
    parser.add_option("-r","--regions", dest="regions", default='',
                          help="cut region identifiers, separated by comma")
    parser.add_option("-t","--type", dest="fitType", default='',
                          help="shapes_prefit, shapes_fit_b, shapes_fit_s")

    (opts, args) = parser.parse_args(argv)
    if opts.config == "":
            opts.config = ["config"]

    # Import after configure to get help message
    from myutils import BetterConfigParser, mvainfo, ParseInfo
    config = BetterConfigParser()
    config.read(opts.config)

    if len(opts.fitType) < 1:
        if config.has_option('Fit','FitType'):
            opts.fitType = config.get('Fit','FitType')
        else:
            opts.fitType = "shapes_prefit"

    # run plotter
    if len(opts.regions) < 1:
        regions = eval(config.get('Fit', 'regions')).keys()
    else:
        regions = opts.regions.split(',')
    for region in regions:
        print("INFO: region:", region)
        plotter = PostfitPlotter(config=config, region=region, directory=opts.fitType)
        plotter.prepare()
        plotter.run()

