#!/usr/bin/env python
from __future__ import print_function
import ROOT
import numpy as np

ROOT.Math.MinimizerOptions.SetDefaultMaxFunctionCalls(100000)

#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_HT_psDYB --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100;Stitching.MethodDY=OFF;Stitching.MethodZJ=OFF;Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_BE_psDYB --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100;Stitching.MethodDY=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_HT_psDYB_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100&&(((hJidx[0]>-1&&hJidx[1]>-1))&&((H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250));Stitching.MethodDY=OFF;Stitching.MethodZJ=OFF;Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_BE_psDYB_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100&&(((hJidx[0]>-1&&hJidx[1]>-1))&&((H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250));Stitching.MethodDY=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_HT_psDYF --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100;Stitching.MethodDY=OFF;Stitching.MethodZJ=OFF;Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_BE_psDYF --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100;Stitching.MethodDY=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_HT_psDYF_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100&&(((hJidx[0]>-1&&hJidx[1]>-1))&&((H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250));Stitching.MethodDY=OFF;Stitching.MethodZJ=OFF;Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zll2017 -J runplot -F plots_stitching_checks_BE_psDYF_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100&&(((hJidx[0]>-1&&hJidx[1]>-1))&&((H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250));Stitching.MethodDY=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'DY*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_HT_psZJB --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100;Stitching.MethodZJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_BE_psZJB --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100;Stitching.MethodZJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_HT_psZJB_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100&&(((isZnn&&MET_Pt>170.0&&min(MHT_pt,MET_pt)>100&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250&&H_pt>120.0&&abs(TVector2::Phi_mpi_pi(H_phi-MET_Phi))>2.0&&Sum$(abs(TVector2::Phi_mpi_pi(Jet_phi-MET_Phi))<0.5&&Jet_Pt>30&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter)==0&&H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&abs(TVector2::Phi_mpi_pi(MET_Phi-TkMET_phi))<0.5&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.4&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2));Stitching.MethodZJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_BE_psZJB_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100&&(((isZnn&&MET_Pt>170.0&&min(MHT_pt,MET_pt)>100&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250&&H_pt>120.0&&abs(TVector2::Phi_mpi_pi(H_phi-MET_Phi))>2.0&&Sum$(abs(TVector2::Phi_mpi_pi(Jet_phi-MET_Phi))<0.5&&Jet_Pt>30&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter)==0&&H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&abs(TVector2::Phi_mpi_pi(MET_Phi-TkMET_phi))<0.5&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.4&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2));Stitching.MethodZJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_HT_psZJF --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100;Stitching.MethodZJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_BE_psZJF --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100;Stitching.MethodZJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_HT_psZJF_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100&&(((isZnn&&MET_Pt>170.0&&min(MHT_pt,MET_pt)>100&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250&&H_pt>120.0&&abs(TVector2::Phi_mpi_pi(H_phi-MET_Phi))>2.0&&Sum$(abs(TVector2::Phi_mpi_pi(Jet_phi-MET_Phi))<0.5&&Jet_Pt>30&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter)==0&&H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&abs(TVector2::Phi_mpi_pi(MET_Phi-TkMET_phi))<0.5&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.4&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2));Stitching.MethodZJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Zvv2017 -J runplot -F plots_stitching_checks_BE_psZJF_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100&&(((isZnn&&MET_Pt>170.0&&min(MHT_pt,MET_pt)>100&&Jet_btagDeepB[hJidx[1]]>0.1522&&H_mass<250&&H_pt>120.0&&abs(TVector2::Phi_mpi_pi(H_phi-MET_Phi))>2.0&&Sum$(abs(TVector2::Phi_mpi_pi(Jet_phi-MET_Phi))<0.5&&Jet_Pt>30&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter)==0&&H_mass>50)&&Jet_btagDeepB[hJidx[0]]>0.4941&&abs(TVector2::Phi_mpi_pi(MET_Phi-TkMET_phi))<0.5&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.4&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2));Stitching.MethodZJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'ZJ*,ZBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_HT_psWJB --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100;Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_BE_psWJB --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100;Stitching.MethodWJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_HT_psWJB_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100&&((((isWenu||isWmunu)&&H_pt>100&&dPhiLepMet<2.0&&H_mass>50)&&H_mass>50&&H_mass<250&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.5&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2&&abs(TVector2::Phi_mpi_pi(H_phi-V_phi))>2.5&&dPhiLepMet<2.0));Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_BE_psWJB_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb>0&&LHE_Vpt>=100&&((((isWenu||isWmunu)&&H_pt>100&&dPhiLepMet<2.0&&H_mass>50)&&H_mass>50&&H_mass<250&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.5&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2&&abs(TVector2::Phi_mpi_pi(H_phi-V_phi))>2.5&&dPhiLepMet<2.0));Stitching.MethodWJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_HT_psWJF --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100;Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_BE_psWJF --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100;Stitching.MethodWJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_HT_psWJF_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100&&((((isWenu||isWmunu)&&H_pt>100&&dPhiLepMet<2.0&&H_mass>50)&&H_mass>50&&H_mass<250&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.5&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2&&abs(TVector2::Phi_mpi_pi(H_phi-V_phi))>2.5&&dPhiLepMet<2.0));Stitching.MethodWJ=OFF;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'
#./submit.py -T Wlv2017 -J runplot -F plots_stitching_checks_BE_psWJF_RWR --parallel=8 --queue veryshort.q --regions Inclusive  --set='Cuts.additionalPlottingCut=LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt>=100&&((((isWenu||isWmunu)&&H_pt>100&&dPhiLepMet<2.0&&H_mass>50)&&H_mass>50&&H_mass<250&&Jet_btagDeepB[hJidx[0]]>0.4941&&Jet_btagDeepB[hJidx[1]]>0.1522&&Sum$(Jet_Pt>30&&abs(Jet_eta)<2.5&&(Jet_puId>6||Jet_Pt>50)&&Jet_jetId>4&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])<2&&abs(TVector2::Phi_mpi_pi(H_phi-V_phi))>2.5&&dPhiLepMet<2.0));Stitching.MethodWJ=BE;Stitching.ReweightLHEVpt=OFF' --vars LHE_Vpt -S 'WJ*,WBJ*'

def getFitFormula(fitModel, fit, unc=False):

    fitFormulaString = fitModel
    for i in range(fit.GetNpar()):
        if unc:
            fitFormulaString = fitFormulaString.replace("[%i]"%i, "(%1.4e+/-%1.4e)"%(fit.GetParameter(i),  fit.GetParError(i)))
        else:
            fitFormulaString = fitFormulaString.replace("[%i]"%i, "%1.4e"%(fit.GetParameter(i)))
    fitFormulaString = fitFormulaString.replace("TMath::Min","min")
    fitFormulaString = fitFormulaString.replace("TMath::Max","max")
    fitFormulaString = fitFormulaString.replace("+-","-")
    return fitFormulaString


for nLep in [1]:
    for enrichmentType in ['B']:

        if enrichmentType == 'F':
            if nLep == 2:
                f1 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYF_RWR_CR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYF_RWR_CR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYF_RWR_SR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYF_RWR_SR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
            elif nLep == 0:
                f1 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_HT_psZJF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_BE_psZJF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_HT_psZJF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_BE_psZJF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
            elif nLep == 1:
                f1 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_HT_psWJF_RWR_CR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_BE_psWJF_RWR_CR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_HT_psWJF_RWR_SR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_BE_psWJF_RWR_SR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
        else:
            if nLep == 2:
                f1 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYB_RWR_CR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYB_RWR_CR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYB_RWR_SR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYB_RWR_SR_nobtag/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
            elif nLep == 0:
                f1 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_HT_psZJB/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_BE_psZJB/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_HT_psZJB_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_BE_psZJB_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
            elif nLep == 1:
                f1 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_HT_psWJB/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_BE_psWJB/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_HT_psWJB_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_BE_psWJB_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")

        c1 = ROOT.TCanvas("c1","",800,500)

        defaultText = "CR"
        altText     = "SR"
        #altText2    = "Njets==3"
        #altText3    = "Njets==4"

        h1 = f1.Get("summedMcHistograms")
        h2 = f2.Get("summedMcHistograms")
        h3 = f3.Get("summedMcHistograms")
        h4 = f4.Get("summedMcHistograms")
        #h5 = f5.Get("summedMcHistograms")
        #h6 = f6.Get("summedMcHistograms")
        #h7 = f7.Get("summedMcHistograms")
        #h8 = f8.Get("summedMcHistograms")
        
        fitModel    = "[0]+[1]*TMath::Min(x,[3])+[2]*TMath::Min(x,[3])**2"
        fitRangeMin = 100
        fitRangeMax = 800
        startValues = []

        if nLep==2 and enrichmentType == 'F':
            fitModel    = "[0]+[1]*TMath::Min(x,[2])"
            fitRangeMin = 100
            fitRangeMax = 800
            startValues = [[2,300.0]]
            #newBins = np.array([100.0,110.0,130,160,260,500,800])
            #h1 = h1.Rebin(len(newBins)-1,"rebin1",newBins)
            #h2 = h2.Rebin(len(newBins)-1,"rebin2",newBins)
            #h3 = h3.Rebin(len(newBins)-1,"rebin3",newBins)
            #h4 = h4.Rebin(len(newBins)-1,"rebin4",newBins)

        # make b-enriched shape similar to inclusive+HT binned
        # -> shape_BE * RW(HT/BE)
        h1.Divide(h2)
        h1.SetTitle("ratio: (incl.+HT) / b-enriched {nLep} type {enrichmentType}".format(nLep=nLep,enrichmentType=enrichmentType))
        h1.SetStats(0)
        h1.Draw()
        h1.GetYaxis().SetRangeUser(0,3.0)
        h1.GetXaxis().SetRangeUser(90.0,810.0)
        h1.GetXaxis().SetTitle("LHE_Vpt")
        h3.SetStats(0)


        #fitModel    = "[0]+[1]*(TMath::Min(x,[2])-[2])**2+[3]*TMath::Min(x,[4])"
        #startValues = [[2,300.0],[3,-0.00001],[4,500]]
            
        polFit = ROOT.TF1("f1",fitModel, fitRangeMin, fitRangeMax)
        for n,v in startValues:
            polFit.SetParameter(n,v)
            polFit.SetParLimits(n,0.5*v,2*v)
        h1.Fit(polFit, "R")
        fitResult = h1.Fit(polFit, "RS")

        fitParListWithErrors = sum([ [polFit.GetParameter(i), polFit.GetParError(i)] for i in range(polFit.GetNpar())], [])
        print("\x1b[32mFIT RESULT:", ["%1.4e"%x for x in fitParListWithErrors], "\x1b[0m") 
        print(getFitFormula(fitModel, polFit))
        

        grint = ROOT.TGraphErrors(h1.GetXaxis().GetNbins())
        for i in range(h1.GetXaxis().GetNbins()):
            grint.SetPoint(i,h1.GetBinCenter(1+i), 0)
        ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint, 0.68)
        grint.SetLineColor(ROOT.kRed)
        grint.SetFillStyle(3001)
        grint.SetFillColor(ROOT.kMagenta-3)
        #grint.Draw("p same e3")



        h3.Divide(h4)
        h3.SetMarkerColor(ROOT.kBlue+2)
        h3.SetLineColor(ROOT.kBlue+2)
        h3.SetMarkerStyle(22)
        h3.Draw("same")

        polFit2 = ROOT.TF1("f2",fitModel, fitRangeMin, fitRangeMax)
        for n,v in startValues:
            polFit2.SetParameter(n,v)
        polFit2.SetLineColor(ROOT.kBlue)
        h3.Fit(polFit2, "R")
        fitResult2 = h3.Fit(polFit2, "RS")

        fitParListWithErrors2 = sum([ [polFit2.GetParameter(i), polFit2.GetParError(i)] for i in range(polFit2.GetNpar())], [])
        print("\x1b[32mFIT RESULT 2:", ["%1.4e"%x for x in fitParListWithErrors2], "\x1b[0m") 
        print(getFitFormula(fitModel, polFit2))

        grint2 = ROOT.TGraphErrors(h3.GetXaxis().GetNbins())
        for i in range(h3.GetXaxis().GetNbins()):
            grint2.SetPoint(i,h3.GetBinCenter(1+i), 0)
        ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint2, 0.68)
        grint2.SetLineColor(ROOT.kBlue)
        grint2.SetFillStyle(3001)
        grint2.SetFillColor(ROOT.kCyan-3)
        #grint2.Draw("p same e3")


        if True: 
            polFit3 = ROOT.TF1("f3",fitModel, fitRangeMin, fitRangeMax)
            for n,v in startValues:
                polFit3.SetParameter(n,v)
            polFit3.SetLineColor(ROOT.kOrange)
            grint3 = ROOT.TGraphErrors(h1.GetXaxis().GetNbins() + h3.GetXaxis().GetNbins())
            grint4 = ROOT.TGraphErrors(h1.GetXaxis().GetNbins())
            for i in range(h1.GetXaxis().GetNbins()):
                grint3.SetPoint(i,h1.GetBinCenter(1+i), h1.GetBinContent(1+i))
                grint3.SetPointError(i,0, h1.GetBinError(1+i))
                grint4.SetPoint(i,h1.GetBinCenter(1+i), 0)
            for i in range(h3.GetXaxis().GetNbins()):
                grint3.SetPoint(h1.GetXaxis().GetNbins() + i,h3.GetBinCenter(1+i), h3.GetBinContent(1+i))
                grint3.SetPointError(h1.GetXaxis().GetNbins() + i, 0, h3.GetBinError(1+i))



            grint3.Draw("P same")

            #grint3.Fit(polFit3, "R")
            fitResult3 = grint3.Fit(polFit3, "RS")
            print("BOTH REGIONS:", getFitFormula(fitModel, polFit3))
            
            ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint4, 0.68)
            grint4.SetLineColor(ROOT.kGreen+1)
            grint4.SetFillStyle(3001)
            grint4.SetFillColor(ROOT.kSpring-3)
            grint4.Draw("p same e3")

        h1.SetFillStyle(0)
        h3.SetFillStyle(0)
        #h5.SetFillStyle(0)
        #h7.SetFillStyle(0)
        h1.SetFillColor(0)
        h3.SetFillColor(0)
        #h5.SetFillColor(0)
        #h7.SetFillColor(0)

        leg = ROOT.TLegend(0.15,0.7,0.5,0.88)
        leg.AddEntry(h1, defaultText)
        leg.AddEntry(polFit, "fit")
        leg.AddEntry(h3, altText) 
        leg.AddEntry(polFit2, "fit")
        #leg.AddEntry(h5, altText2) 
        #leg.AddEntry(polFit3, "fit")
        #leg.AddEntry(h7, altText3) 
        #leg.AddEntry(polFit4, "fit")
        leg.Draw()

        #fitFormulaString = fitModel
        #for i in range(polFit2.GetNpar()):
        #    fitFormulaString = fitFormulaString.replace("[%i]"%i, "(%1.4e+/-%1.4e)"%(polFit2.GetParameter(i),  polFit2.GetParError(i)))
        #fitFormulaString = fitFormulaString.replace("TMath::Min","min")
        #fitFormulaString = fitFormulaString.replace("TMath::Max","max")

        #text = ROOT.TText(105,0.15,fitFormulaString)
        #text.SetTextSize(0.025)
        #text.SetTextColor(ROOT.kBlue+2)
        #text.SetTextAlign(12)
        #text.Draw()

        for ext in ['png','pdf','root']:
            c1.SaveAs("reweighting_b_enriched_{nLep}{enrichmentType}.{ext}".format(nLep=nLep,enrichmentType=enrichmentType,ext=ext))

        ROOT.gPad.Update()
        raw_input()


