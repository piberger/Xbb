from __future__ import print_function
import ROOT 
ROOT.gROOT.SetBatch(True)
import sys,os
from BetterConfigParser import BetterConfigParser

from Ratio import getRatio
from NewHistoMaker import NewHistoMaker as HistoMaker
from sampleTree import SampleTree as SampleTree

class NewStackMaker:
    def __init__(self, config, var, region, SignalRegion, setup=None, subcut = ''):
        self.config = config
        self.var = var
        self.region = region
        self.configSection = 'Plot:%s'%region
        self.subcut = subcut
        self.forceLog = None
        self.normalize = eval(self.config.get(self.configSection, 'Normalize'))
        self.log = eval(self.config.get(self.configSection, 'log'))
        if self.config.has_option('plotDef:%s'%var, 'log') and not self.log:
            self.log = eval(self.config.get('plotDef:%s'%var,'log'))
        self.blind = eval(self.config.get(self.configSection,'blind'))
        self.xAxis = self.config.get('plotDef:%s'%self.var,'xAxis')
        self.typLegendDict=eval(config.get('Plot_general','typLegendDict'))
        if setup is None:
            self.setup = [x.strip() for x in self.config.get('Plot_general', 'setupLog' if self.log else 'setup').split(',') if len(x.strip()) > 0]
        else:
            self.setup = setup
        
        # TODO
        if not SignalRegion: 
            if 'ZH' in self.setup:
                self.setup.remove('ZH')
            if 'WH' in self.setup:
                self.setup.remove('WH')
                self.setup.remove('ggZH')
        self.rebin = 1
        self.histogramOptions = {
                'rebin': 1,
                'var': self.var,
                }
        if self.config.has_option(self.configSection,'rebin'):
            self.histogramOptions['rebin'] = eval(self.config.get(self.configSection,'rebin'))
        if self.config.has_option(self.configSection,'nBins'):
            self.histogramOptions['nBins'] = int(eval(self.config.get(self.configSection,'nBins'))/self.histogramOptions['rebin'])
        else:
            self.histogramOptions['nBins'] = int(eval(self.config.get('plotDef:%s'%var,'nBins'))/self.histogramOptions['rebin'])
        if self.config.has_option(self.configSection,'min'):
            self.histogramOptions['xMin'] = eval(self.config.get(self.configSection,'min'))
        else:
            self.histogramOptions['xMin'] = eval(self.config.get('plotDef:%s'%var,'min'))
        if self.config.has_option(self.configSection,'max'):
            self.histogramOptions['xMax'] = eval(self.config.get(self.configSection,'max'))
        else:
            self.histogramOptions['xMax'] = eval(self.config.get('plotDef:%s'%var,'max'))
        self.histogramOptions['treeVar'] = self.config.get('plotDef:%s'%var,'relPath')

        if self.config.has_option('Weights','weightF'):
            self.histogramOptions['weight'] = self.config.get('Weights','weightF')
        else:
            self.histogramOptions['weight'] = None

        self.groups = {}
        self.histograms = []
        self.dataTitle = 'Data'

        print ("INFO: StackMaker initialized!", self.histogramOptions['treeVar'], " min=", self.histogramOptions['xMin'], " max=", self.histogramOptions['xMax'], "nBins=", self.histogramOptions['nBins'])

    def addSampleTree(self, sample, sampleTree, groupName):
        print ("INFO: var=", self.var, "-> treeVar=\x1b[34m", self.histogramOptions['treeVar'] , "\x1b[0m add sample \x1b[34m", sample,"\x1b[0m from sampleTree \x1b[34m", sampleTree, "\x1b[0m to group \x1b[34m", groupName, "\x1b[0m")

        histogramOptions = self.histogramOptions.copy()
        histogramOptions['group'] = groupName
        histoMaker = HistoMaker(self.config, sample=sample, sampleTree=sampleTree, histogramOptions=histogramOptions) 
        sampleHistogram = histoMaker.getHistogram()
        self.histograms.append({
            'histogram': sampleHistogram,
            'group': groupName
            })

    def Draw(self, outputFolder='./'):
        
        TdrStyles.tdrStyle()
        dataGroupName = 'DATA'

        # group MC+DATA histograms 
        groupedHistograms = {}
        for histogram in self.histograms:
            if histogram['group'] in groupedHistograms:
                groupedHistograms[histogram['group']].Add(histogram['histogram'])
            else:
                groupedHistograms[histogram['group']] = histogram['histogram'].Clone("group_" + histogram['group'])
        
        # canvas
        c = ROOT.TCanvas(self.var,'', 600, 600)
        c.SetFillStyle(4000)
        c.SetFrameFillStyle(1000)
        c.SetFrameFillColor(0)
        c.SetTopMargin(0.035)
        c.SetBottomMargin(0.12)
        
        # add MC histograms to stack
        allStack = ROOT.THStack(self.var, '')
        colorDict = eval(self.config.get('Plot_general', 'colorDict'))
        first = True
        for groupName in self.setup[::-1]:
            if groupName in groupedHistograms and groupName != dataGroupName:
                if groupName in colorDict:
                    groupedHistograms[groupName].SetFillColor(colorDict[groupName])
                if groupedHistograms[groupName]:
                    allStack.Add(groupedHistograms[groupName])
        
        # draw stack
        allStack.Draw("hist")
        if dataGroupName in groupedHistograms and not groupedHistograms[dataGroupName].GetSumOfWeights() % 1 == 0.0:
            yTitle = 'S/(S+B) weighted entries'
        else:
            yTitle = 'Entries'
        if not '/' in yTitle:
            if allStack and allStack.GetXaxis():
                if 'GeV' in self.xAxis:
                    yAppend = '%.0f' %(allStack.GetXaxis().GetBinWidth(1)) 
                else:
                    yAppend = '%.2f' %(allStack.GetXaxis().GetBinWidth(1)) 
                yTitle = '%s / %s' %(yTitle, yAppend)
                if 'GeV' in self.xAxis:
                    yTitle += ' GeV'
        if allStack and allStack.GetXaxis():
            allStack.GetYaxis().SetTitle(yTitle)
            allStack.GetXaxis().SetRangeUser(self.histogramOptions['xMin'], self.histogramOptions['xMax'])
            allStack.GetYaxis().SetRangeUser(0,20000)
        Ymax = max(allStack.GetMaximum(), groupedHistograms[dataGroupName].GetMaximum() if dataGroupName in groupedHistograms else 0) * 1.7
        if self.log:
            allStack.SetMinimum(0.1)
            Ymax = Ymax*ROOT.TMath.Power(10,1.2*(ROOT.TMath.Log(1.2*(Ymax/0.2))/ROOT.TMath.Log(10)))*(0.2*0.1)
            ROOT.gPad.SetLogy()
        allStack.SetMaximum(Ymax)

        # draw DATA
        if dataGroupName in groupedHistograms:
            drawOption = 'PE'
            if allStack and allStack.GetXaxis():
                drawOption += ',SAME'
            groupedHistograms[dataGroupName].Draw(drawOption)
        
        # draw legend
        l2 = ROOT.TLegend(0.5, 0.82,0.92,0.95)
        l2.SetLineWidth(2)
        l2.SetBorderSize(0)
        l2.SetFillColor(0)
        l2.SetFillStyle(4000)
        l2.SetTextFont(62)
        #l2.SetTextSize(0.035)
        l2.SetNColumns(2)
        
          
        l = ROOT.TLegend(0.45, 0.6,0.75,0.92)
        l.SetLineWidth(2)
        l.SetBorderSize(0)
        l.SetFillColor(0)
        l.SetFillStyle(4000)
        l.SetTextFont(62)
        l.SetTextSize(0.035)
        l_2 = ROOT.TLegend(0.68, 0.6,0.92,0.92)
        l_2.SetLineWidth(2)
        l_2.SetBorderSize(0)
        l_2.SetFillColor(0)
        l_2.SetFillStyle(4000)
        l_2.SetTextFont(62)
        l_2.SetTextSize(0.035)
 
        if dataGroupName in groupedHistograms:
            l.AddEntry(groupedHistograms[dataGroupName], self.dataTitle, 'P')
        groupNames = list(set([groupName for groupName, groupHistogram in groupedHistograms.iteritems()]))
        numLegendEntries = len(groupNames) + 2
        for j, (groupName, groupHistogram) in enumerate(groupedHistograms.iteritems()):
            if groupName != dataGroupName:
                legendEntryName = self.typLegendDict[groupName] if groupName in self.typLegendDict else groupName
                if j < numLegendEntries/2.-2:
                    l.AddEntry(groupHistogram, legendEntryName, 'F')
                else:
                    l_2.AddEntry(groupHistogram, legendEntryName, 'F')
        
        if not False: #self.AddErrors:
            l_2.AddEntry(groupedHistograms[dataGroupName], "MC uncert. (stat.)", "fl")
        else:
            l_2.AddEntry(groupedHistograms[dataGroupName], "MC uncert. (stat.+ syst.)", "fl")
        c.Update()
        ROOT.gPad.SetTicks(1,1)
        l.SetFillColor(0)
        l.SetBorderSize(0)
        l_2.SetFillColor(0)
        l_2.SetBorderSize(0)
        l.Draw()
        l_2.Draw()

        # save to file
        outputFileName = outputFolder + 'plot_test_' + self.var + '.png'
        c.SaveAs(outputFileName)
        print ("INFO: saved as \x1b[34m", outputFileName, "\x1b[0m")

