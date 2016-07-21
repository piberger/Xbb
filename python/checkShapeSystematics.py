from ROOT import *
from copy import *


def getPlot(file_, sample, syst=None, UD=None):
    dir_ = file_.Get("Znn_13TeV")
    if syst==None:
        histoName = sample
    else:
        histoName = sample+syst+UD
    histo = dir_.Get(histoName)
    if histo == None:
        print dir_.ls()
        print histoName, " not found!"
    return copy(histo)

UD = ["Up","Down"]
#systs = ["CMS_vhbb_bTagWeightLFStats1"]
#systs = ["CMS_vhbb_puWeight"]
#systs = ["CMS_res_j"]
systs = ["CMS_vhbb_scale_j_13TeV"]
systs = [
#	"CMS_vhbb_ZnnHighPt_stats_bin1_WH_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin12_WH_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin14_WH_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin15_WH_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin2_ggZH_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin9_ggZH_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin5_VVHF_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin3_VVLF_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin7_VVLF_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin18_VVLF_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin20_Zj1b_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin3_Zj2b_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin20_Wj0b_Znn_13TeV",
#	"CMS_vhbb_ZnnHighPt_stats_bin1_Wj2b_Znn_13TeV",
	"CMS_vhbb_bTagWeightHF",
	"CMS_vhbb_bTagWeightLF",
	"CMS_vhbb_bTagWeightLFStats1",
	"CMS_vhbb_bTagWeightLFStats2",
	"CMS_vhbb_bTagWeightHFStats1",
	"CMS_vhbb_bTagWeightHFStats2",
	"CMS_vhbb_bTagWeightcErr1",
	"CMS_vhbb_bTagWeightcErr2",
	"CMS_vhbb_puWeight",
	"CMS_vhbb_triggerMET",
	"LHE_weights_scale_muF_ZH",
	"LHE_weights_scale_muF_ggZH",
	"LHE_weights_scale_muF_TT",
	"LHE_weights_scale_muF_WH",
	"LHE_weights_scale_muF_Wjets",
	"LHE_weights_scale_muF_Zjets",
	"LHE_weights_scale_muR_ZH",
	"LHE_weights_scale_muR_ggZH",
	"LHE_weights_scale_muR_TT",
	"LHE_weights_scale_muR_WH",
	"LHE_weights_scale_muR_Wjets",
	"LHE_weights_scale_muR_Zjets",
	"CMS_vhbb_res_j_13TeV",
	"CMS_vhbb_scale_j_13TeV"
]
regions = [
    'Znn_13TeVTightHighPt_QCD',
    'Znn_13TeVTightHighPt_Signal',
    'Znn_13TeVTightHighPt_TTbarTight',
    'Znn_13TeVTightHighPt_WLight',
    'Znn_13TeVTightHighPt_Wbb',
    'Znn_13TeVTightHighPt_ZLight',
    'Znn_13TeVTightHighPt_Zbb',
    'Znn_13TeVTightLowPt_QCD',
    'Znn_13TeVTightLowPt_Signal',
    'Znn_13TeVTightLowPt_TTbarTight',
    'Znn_13TeVTightLowPt_WLight',
    'Znn_13TeVTightLowPt_Wbb',
    'Znn_13TeVTightLowPt_ZLight',
    'Znn_13TeVTightLowPt_Zbb',
]

gROOT.SetBatch()
canvas = TCanvas("canvas","")
for region in regions:
    fileName = "/scratch/sdonato/VHbbRun2/V21_tesi/CMSSW_7_4_7/src/Xbb/Limit_expertAllnominal/FitTwoBinsTight/vhbb_TH_"+region+".root"
    file_ = TFile(fileName)
    data = getPlot(file_,"data_obs")
    data.SetLineWidth(3)
    data.SetLineColor(kBlue)
    data.Draw()

    plots = {}
    for sample in ["TT","Wj2b","Wj1b","Wj0b","Zj2b","Zj1b","Zj0b","s_Top","VVHF","VVLF","QCD"]:
        for syst in systs:
            for ud in ["Up","Down"]:
                name = syst+ud
                try:
                    histo = getPlot(file_,sample,syst,ud).Clone(name)
                except:
                    histo = getPlot(file_,sample).Clone(name)
                if ud=="Up":
                    histo.SetLineColor(kRed)
                else:
                    histo.SetLineColor(kGreen)
                if name in plots: plots[name].Add(histo)
                else: plots[name] = histo
    #            plots[name].Draw("HIST,same")
        histo = getPlot(file_,sample)
        histo.SetLineColor(kBlack)
        histo.SetLineWidth(2)
        if "nominal" in plots: plots["nominal"].Add(histo)
        else: plots["nominal"] = histo
    #    plots["nominal"].Draw("HIST,same")

    for plot in plots:
        plots[plot].Draw("HIST,same")

    canvas.SaveAs("check_"+region+".png")
