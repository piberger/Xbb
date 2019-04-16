##################
#Description:   Takes a plot in root format from the plot step. Calculates signal and background efficiency by scanning a cut along the x-axis
#  #################

import ROOT
import math


#####note: 
##For S/S+B cut optimisation, use without opt
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/Inclusive_BOOST__tau21_.root'
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/Inclusive_BOOST__DoubleB_.root'
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/Signal_BOOST_highBB__OutBJet_.root'
path    = '/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2018/runplot-12mar-v3/Plots/ttu__Pileup_nPU_.root'

#For ROCs/Efficiency, used comp_
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/comp_Inclusive_BOOST__tau21_.root'
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/comp_Inclusive_BOOST__DoubleB_.root'
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/comp_Signal_BOOST_highBB__OutBJet_.root'
#path    = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb2018/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016_v2/runplot_boost_v101/Plots/comp_Signal_BOOST_highBB__FatMass_.root'


bkg     = 'bkg'
signal  = 'sig'

#example: tau21
#purity =  'left'

#example: double b
purity = 'right'

varname = path.split('__')[1].replace('_.root','')

####
#Retrieve the histograms
####




file_in = ROOT.TFile.Open(path)
canvas = None
for key in file_in.GetListOfKeys():
    if key.GetClassName() == 'TCanvas':
        canvas = file_in.Get(key.GetName())

stack = None
if 'comp' in path:
    for p in canvas.GetListOfPrimitives():
        if p.ClassName() == 'THStack':
            stack = canvas.GetPrimitive(p.GetName())
else:
    for p in canvas.GetListOfPrimitives():
        if p.ClassName() == 'TPad' and p.GetName() == 'oben':
            pad = canvas.GetPrimitive(p.GetName())
    for p in pad.GetListOfPrimitives():
        print p.GetName()
        print p.ClassName()
        if p.ClassName() == 'THStack':
            stack = pad.GetPrimitive(p.GetName())
            print stack
            break

hbkg = None
hsig = None
for h in stack.GetHists():
    print h
    if 'sig' in h.GetName().lower():
        hsig = h
    elif 'bkg' in h.GetName().lower():
        hbkg = h


#########
#Loop over histograms
#########

axis_bkg   = hbkg.GetXaxis()
axis_sig   = hsig.GetXaxis()

nbins = axis_bkg.GetNbins()

sig_eff     = [0]*(nbins)
bkg_eff     = [0]*(nbins)
S_overSpB   = [0]*(nbins)
axis        = [0]*(nbins)

hbkg_tot = hbkg.Integral(1,nbins)
hsig_tot = hsig.Integral(1,nbins)


#only for plot purpose
x_range_down = 0
x_range_up = 0

for b in range(1,nbins+1):
    #print axis_bkg.GetBinLowEdge(b)

    axis[b-1] = axis_bkg.GetBinUpEdge(b-1)

    sig_eff[b-1]    = hsig.GetBinContent(b-1)
    bkg_eff[b-1]    = hbkg.GetBinContent(b-1)

    if not b == 1:
        sig_eff[b-1] += sig_eff[b-2]
        bkg_eff[b-1] += bkg_eff[b-2]
 
    if math.sqrt(bkg_eff[b-1]+sig_eff[b-1]) != 0:
        S_overSpB[b-1]  = sig_eff[b-1]/math.sqrt(bkg_eff[b-1]+sig_eff[b-1])
    else: S_overSpB[b-1] = 0

    if b == 1:
        x_range_down = axis_bkg.GetBinUpEdge(b-1)
    if b == nbins:
        x_range_up = axis_bkg.GetBinLowEdge(b)

if purity == 'right':
    sig_eff_copy = sig_eff
    bkg_eff_copy = bkg_eff
    axis.append(x_range_up)
    del axis[0]
    for i in range(0,nbins):
        sig_eff[i] = hsig_tot - sig_eff[i]
        bkg_eff[i] = hbkg_tot - bkg_eff[i]
        if math.sqrt(bkg_eff[i]+sig_eff[i]) != 0:
            S_overSpB[i]  = sig_eff[i]/math.sqrt(bkg_eff[i]+sig_eff[i])
        else: S_overSpB[i] = 0


import numpy as np
np_axis = np.array(axis)

np_sig = np.array(sig_eff) 
np_bkg = np.array(bkg_eff) 
np_S_overSpB = np.array(S_overSpB) 

if 'comp' in path:

   ############
   #ROC curve
   ############
   
   g = ROOT.TGraph(nbins, np_sig, np_bkg)
   
   g.SetTitle('ROC Curve')
   g.SetLineColor(2)
   g.SetLineWidth(2)
   g.SetMarkerColor(2)
   g.SetMarkerSize(1)
   g.SetMarkerStyle(21)
   g.GetXaxis().SetTitle("Signal Efficiency")
   g.GetYaxis().SetTitle("Background Efficiency")
   g.GetXaxis().SetRangeUser(0,1)
   
   c = ROOT.TCanvas()
   g.Draw()
   c.SaveAs('roc_%s.pdf'%varname)
   
   ############
   #Efficiencies
   ############
   
   gsig = ROOT.TGraph(nbins, np_axis, np_sig)
   
   gsig.SetLineColor(2)
   gsig.SetLineWidth(2)
   gsig.SetMarkerColor(2)
   gsig.SetMarkerSize(1)
   gsig.SetMarkerStyle(22)
   gsig.SetMarkerStyle(22)
   gsig.SetTitle("Efficiency")
   gsig.GetYaxis().SetTitle("Efficiency")
   gsig.GetYaxis().SetRangeUser(0,1)
   gsig.GetYaxis().SetNdivisions(10)
   gsig.GetXaxis().SetRangeUser(x_range_down,x_range_up)
   gsig.GetXaxis().SetTitle(varname)
   gsig.GetXaxis().SetNdivisions(20)
   #print x_range_down
   #print x_range_up
   
   gbkg = ROOT.TGraph(nbins, np_axis, np_bkg)
   gbkg.SetLineColor(4)
   gbkg.SetLineWidth(2)
   gbkg.SetMarkerColor(4)
   gbkg.SetMarkerSize(1)
   gbkg.SetMarkerStyle(22)
   
   legend = None
   if purity == 'right':
       legend = ROOT.TLegend(0.52,0.8,0.9,0.9)
   elif purity == 'left':
       legend = ROOT.TLegend(0.1,0.8,0.48,0.9)
   
   legend.AddEntry(gsig,"Signal")
   legend.AddEntry(gbkg,"Background")
   
   c2 = ROOT.TCanvas()
   c2.SetGrid()
   
   gsig.Draw()
   gbkg.Draw('same')
   legend.Draw('same')
   c2.SaveAs('Efficiency_%s2.pdf'%varname)

############
#S/S+B optimisation 
############

else:

   gopt = ROOT.TGraph(nbins, np_axis, np_S_overSpB)
   
   gopt.SetLineColor(2)
   gopt.SetLineWidth(2)
   gopt.SetMarkerColor(2)
   gopt.SetMarkerSize(1)
   gopt.SetMarkerStyle(22)
   gopt.SetMarkerStyle(22)
   gopt.SetTitle("S/#sqrt{S+B}")
   gopt.GetYaxis().SetTitle("S/#sqrt{S+B}")
   gopt.GetYaxis().SetNdivisions(10)
   gopt.GetXaxis().SetRangeUser(x_range_down,x_range_up)
   gopt.GetXaxis().SetTitle(varname)
   gopt.GetXaxis().SetNdivisions(20)
   #print x_range_down
   #print x_range_up
   
   c3 = ROOT.TCanvas()
   c3.SetGrid()
   gopt.Draw()
   
   c3.SaveAs('SOverSpB_%s.pdf'%varname)

