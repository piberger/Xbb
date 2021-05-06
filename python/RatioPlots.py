import matplotlib
matplotlib.use("Agg")
import ROOT
from root_numpy import root2array, tree2array
import numpy as np
import matplotlib.pyplot as plt
from rootpy.plotting import Hist, HistStack
import rootpy.plotting.root2matplotlib as rplt
from rootpy.io import root_open
from matplotlib.ticker import AutoMinorLocator
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import rootpy

varnames = { 
    "sl_jge6_tge4__jetsByPt_1_bjet_pt" : r"subleading b-jet $p_T$ [GeV]",
    "sl_jge6_tge4__jetsByPt_0_lightjet_pt" : r"leading light jet $p_T$ [GeV]",
    "dl_jge4_tge4__jetsByPt_1_bjet_pt" : r"subleading b-jet $p_T$ [GeV]",
    "dl_jge4_tge4__jetsByPt_0_lightjet_pt" : r"leading light jet $p_T$ [GeV]"
}

template = {
    "sl_jge6_tge4__jetsByPt_0_lightjet_pt" : rootpy.plotting.Hist(30,0,200),
    "sl_jge6_tge4__jetsByPt_1_bjet_pt" : rootpy.plotting.Hist(30,0,300),
    "dl_jge4_tge4__jetsByPt_0_lightjet_pt" : rootpy.plotting.Hist(30,0,200),
    "dl_jge4_tge4__jetsByPt_1_bjet_pt" : rootpy.plotting.Hist(30,0,300)
}

regions_Znn = [
    "SR_high1_Znn",
    "SR_high1_Znn_BOOST",
    "SR_high2_Znn",
    "SR_high2_Znn_BOOST",
    "SR_med_Znn_0j",
    "SR_med_Znn_ge1j",
    "Zhf_high_Znn",
    "Zhf_high_Znn_BOOST",
    "Zhf_med_Znn"
]

regions_Zee = [
    "SR_high1_Zee",
    "SR_high1_Zee_BOOST",
    "SR_high2_Zee",
    "SR_high2_Zee_BOOST",
    "SR_med_Zee_0j",
    "SR_med_Zee_ge1j",
    "SR_low_Zee",
    "Zhf_high_Zee",
    "Zhf_high_Zee_BOOST",
    "Zhf_med_Zee",
    "Zhf_low_Zee"
]

regions_Zmm = [
    "SR_high1_Zmm",
    "SR_high1_Zmm_BOOST",
    "SR_high2_Zmm",
    "SR_high2_Zmm_BOOST",
    "SR_med_Zmm_0j",
    "SR_med_Zmm_ge1j",
    "SR_low_Zmm",
    "Zhf_high_Zmm",
    "Zhf_high_Zmm_BOOST",
    "Zhf_med_Zmm",
    "Zhf_low_Zmm"
]

regions_Wen = [
    "SR_high1_Wen",
    "SR_high1_Wen_BOOST",
    "SR_high2_Wen",
    "SR_high2_Wen_BOOST",
    "SR_med_Wen",
    "Whf_high_Wen",
    "Whf_high_Wen_BOOST",
    "Whf_med_Wen",
]

regions_Wmn = [
    "SR_high1_Wmn",
    "SR_high1_Wmn_BOOST",
    "SR_high2_Wmn",
    "SR_high2_Wmn_BOOST",
    "SR_med_Wmn",
    "Whf_high_Wmn",
    "Whf_high_Wmn_BOOST",
    "Whf_med_Wmn",
]




# function to post the post-fit shapes
def draw_prefit_postfit_shape(shapefile1, shapefile2, region, process):

    f1 = root_open(shapefile1, 'read')
    f2 = root_open(shapefile2, 'read')
    
    b1_w = f1.Get(region + "/" + process + "1b")
    b1_wo = f2.Get(region + "/" + process + "1b")

    b2_w = f1.Get(region + "/" + process + "2b")
    b2_wo = f2.Get(region + "/" + process + "2b")

    temp1 = (b1_w + b2_w)
    temp2 = (b1_wo + b2_wo)

    #temp1 = template[cat].Clone(wStitching.GetName())
    #temp2 = template[cat].Clone(woStitching.GetName())
    #for ibin in range(pre.GetNbinsX()+2):
    #    temp1.SetBinContent(ibin, wStitching.GetBinContent(ibin))
    #    temp1.SetBinContent(ibin, wStitching.GetBinContent(ibin))
    #    temp2.SetBinContent(ibin, woStitching.GetBinContent(ibin))
    #    temp2.SetBinContent(ibin, woStitching.GetBinContent(ibin))

    fig = plt.figure(figsize=(6,6))
    a1 = plt.axes([0.0,0.22,1.0,0.8])

    # do top panel
    fig.suptitle(r"$\mathbf{CMS}$ private work", y=1.02, x=0.02, horizontalalignment="left", verticalalignment="bottom", fontsize=16)    

    # do main plot
    temp1.linecolor = "blue"
    temp2.linecolor = "red"

    p1, = rplt.step(temp1)
    p2, = rplt.step(temp2)

    plt.legend([p1,p2], ['Old Stitching', 'w/o Stitching'], loc='best', prop={'size':16})

    xmin = temp1.GetXaxis().GetXmin()
    xmax = temp2.GetXaxis().GetXmax()
    print xmin, xmax
    a1.set_xlim(xmin,xmax)
    a1.get_xaxis().set_visible(False)
    a1.set_ylim(bottom=0, top=1.2*a1.get_ylim()[1])

    #a1.grid(zorder=100000)
    plt.ylabel("events / bin", fontsize=24)

    # do ratio plot
    a2 = plt.axes([0.0,0.0, 1.0, 0.18], sharex=a1)
    minorLocator = AutoMinorLocator()
    a2.yaxis.set_minor_locator(minorLocator)

    plt.xlabel("Discriminant", fontsize=24)
    #a2.grid(which='minor', axis='y', linestyle='-')

    ratio = temp2.clone()
    ratio.linecolor = "green"
    ratio.Divide(temp1)

    rplt.step(ratio)
    plt.ylabel("ratio", fontsize=16)
    plt.axhline(1.0, color="black")

    a2.set_ylim(0.4, 1.6)
    ticks = a1.get_xticks()
    a2.set_xticks(ticks)
    a2.set_xlim(xmin, xmax)

    fig.savefig("shapes_"+region+"_"+process+".png", pad_inches=0.5, bbox_inches='tight')
    fig.savefig("shapes_"+region+"_"+process+".pdf", pad_inches=0.5, bbox_inches='tight')
    
if __name__=="__main__":

    shapefile1 = "/work/creissel/VHbb/CMSSW_10_1_0/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2016/rundc-2021-03-09/Limits/vhbb_Wmn-2016.root"
    shapefile2 = "/work/creissel/VHbb/CMSSW_10_2_13/src/CombineHarvester/VHLegacy/shapes/Xbb_2021-03-06/vhbb_Wmn-2016.root"

    for reg in regions_Wmn:
        for proc in ["Wj"]:
            draw_prefit_postfit_shape(shapefile1, shapefile2, reg, proc)
        
