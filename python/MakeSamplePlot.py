#####
#info:  Macro used to make quick plots for a few samples. Limited but faster than Xbb if only need to check a few variables
#only working on tier3 for now (use tier3 "protocols" to access files)
####

import os
import ROOT

class sample:
    '''Store all the info for a given sample'''

    def __init__(self, path, name, weight, maxfiles=500):
        self.path = path
        self.name = name
        self.weight = weight
        self.maxfiles = maxfiles

        self.getfilelist()

    def getfilelist(self):
        '''Get list of all the files corresponding to the sample'''
        self.filelist = os.listdir(self.path)[:self.maxfiles]
        print 'filelist is', self.filelist

    def gethisto(self, var):
        h = ROOT.TH1F('h','h', var[2], var[3], var[4])
        for f in self.filelist:
            file = ROOT.TFile.Open('root://t3dcachedb03.psi.ch:1094/'+self.path+f)
            tree = file.Get('tree')
            if f == self.filelist[0]:
                tree.Draw('%s>>h'%var[1])
            else:
                h2 = ROOT.TH1F('h2','h2', var[2], var[3], var[4])
                tree.Draw('%s>>h2'%var[1])
                h.Add(h2)
        return h

class ploter:
    '''Takes a list of samples and a list of variables. Makes correspoinding plots'''
    def __init__(self, sampleList, varList):
        for var in varList:
            c = ROOT.TCanvas('c','c')
            index = 0
            for s in sampleList:

                h = s.gethisto(var)

                if index == 0: self.SetPadParemeter(h, var[0])
                else: self.SetHistoStyle(h, index)
                index += 1

                c.cd()
                if s == sampleList[0]: h.Draw()
                else: h.Draw('SAME')

            c.SaveAs('test.pdf')

    def SetPadParemeter(self, h, title):

        h.SetLineWidth(2)
        h.GetYaxis().SetTitleFont(63)
        h.GetYaxis().SetLabelFont(43)
        h.GetYaxis().SetLabelSize(20)
        h.GetXaxis().SetTitle(title)

    def SetHistoStyle(self, h, index):
        '''Modify color and style of the plot'''
        color = [4, 2, 6, 9, 50, 40, 30, 95, 51]
        h.SetLineColor(color[index])
        h.SetLineWidth(2)

if __name__ == "__main__":

    path = '/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/Boost/sys_2/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/'

    sampleNameList = ['ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8']

    sampleList = []

    for sampleName in sampleNameList:
        sampleList.append(sample(path, sampleName, 1))

    varList = [
            ['test', 'FatjetAK08ungroomed_pt>250', 100, 0, 300]
            #['test', '(Sum$(FatjetAK08ungroomed_pt>250 && abs(FatjetAK08ungroomed_eta)<2.4))', 6, 0, 6]
            #['test', '1', 100, 0, 300]
            ]

    p = ploter(sampleList, varList)


