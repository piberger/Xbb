#####
#info:  Macro used to make quick plots for a few samples. Limited but faster than Xbb if only need to check a few variables
#only working on tier3 for now (use tier3 "protocols" to access files)
####

import os
import ROOT

class sample:
    '''Store all the info for a given sample'''

    def __init__(self, path, sname,  name, weight, maxfiles=500):
        self.path = path
        #short sample name e.g. ggZH
        self.sname = sname
        self.name = name
        self.weight = weight
        self.maxfiles = maxfiles

        self.getfilelist()

    def getfilelist(self):
        '''Get list of all the files corresponding to the sample'''
        self.filelist = os.listdir('%s/%s'%(self.path,self.name))[:self.maxfiles]
        print 'filelist is', self.filelist

    def gethisto(self, var):
        hname = 'h%s%s'%(self.sname,var[0])
        h = ROOT.TH1F(hname, hname, var[2], var[3], var[4])
        for f in self.filelist:
            file = ROOT.TFile.Open('root://t3dcachedb03.psi.ch:1094/'+self.path+'/'+self.name+'/'+'/'+f)
            tree = file.Get('tree')
            if f == self.filelist[0]:
                tree.Draw('%s>>%s'%(var[1],hname))
            else:
                h2 = ROOT.TH1F('h2','h2', var[2], var[3], var[4])
                tree.Draw('%s>>h2'%var[1])
                h.Add(h2)
        del h2
        file.Close()
        print h.Integral()
        #normalise
        h.Scale(1./h.Integral())
        return h

class ploter:
    '''Takes a list of samples and a list of variables. Makes correspoinding plots'''
    def __init__(self, sampleList, varList):
        for var in varList:

            hList = []

            for s in sampleList:
                hList.append([s.gethisto(var),s.sname])

            c = ROOT.TCanvas('c','c')
            leg = ROOT.TLegend(0.1, 0.75, 0.3 , 0.89)
            leg.SetBorderSize(0)
            leg.SetTextFont(42)
            leg.SetTextSize(0.04)

            #Get maximum y
            self.ymax = 0
            for hl in hList:
                if self.ymax < hl[0].GetMaximum():
                    self.ymax = hl[0].GetMaximum()

            index = 0
            for hl in hList:
                #print 'sample is', s.name
                #Get the histogram
                h = hl[0]
                sname = hl[1]

                h.SetStats(False)
                if index == 0: self.SetPadParemeter(h, var[5])
                else: self.SetHistoStyle(h, index)

                if index == 0:
                    h.Draw()
                else:
                    h.Draw('SAME')
                    #h.SetLineStyle(3)

                leg.AddEntry(h, sname,'LP')

                index += 1

            leg.Draw('SAME')
            #print 'goind to save'
            c.SaveAs('%s.pdf'%var[0])
            del c
            print 'saved'

    def SetPadParemeter(self, h, title):

        h.SetLineWidth(2)
        h.GetYaxis().SetTitleFont(63)
        h.GetYaxis().SetLabelFont(43)
        h.GetYaxis().SetLabelSize(20)
        h.GetYaxis().SetRangeUser(0,self.ymax*1.2)
        h.GetXaxis().SetTitle(title)

    def SetHistoStyle(self, h, index):
        '''Modify color and style of the plot'''
        color = [4, 2, 6, 9, 50, 40, 30, 95, 51]
        h.SetLineColor(color[index])
        h.SetLineWidth(2)
        #h.SetLineSyle(index+1)

if __name__ == "__main__":

    path = '/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/Boost/sys_2/'

    sampleNameDic = {'ZH':'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8', 'ggZH':'ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1'}
    #sampleNameDic = {'ZH':'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8'}

    sampleList = []

    for key in sampleNameDic:
        sampleList.append(sample(path, key, sampleNameDic[key], 1))

    varList = [
            #['Jet pt', 'FatjetAK08ungroomed_pt>250', 100, 0, 300]
            #['test', '(Sum$(FatjetAK08ungroomed_pt>250 && abs(FatjetAK08ungroomed_eta)<2.4))', 6, 0, 6]
            #['test', '1', 100, 0, 300]
            ['sdcorr','FatjetAK08ungroomed_puppi_TheaCorr[Maxbbtagidx]', 35, 0.9, 1.25, 'm_{sd} corrected'],
            ['msdcorr','FatjetAK08ungroomed_puppi_TheaCorr[Maxbbtagidx]*FatjetAK08ungroomed_puppi_msoftdrop[Maxbbtagidx]', 30, 90, 150, 'm_{sd} corrected'],
            ['msd','FatjetAK08ungroomed_puppi_msoftdrop[Maxbbtagidx]', 30, 90, 150, 'm_{sd} uncorrected']
            ]

    p = ploter(sampleList, varList)


