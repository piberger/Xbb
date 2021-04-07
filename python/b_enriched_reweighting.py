#!/usr/bin/env python
from __future__ import print_function
import ROOT

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


for nLep in [0,1,2]:
    for enrichmentType in ['B','F']:

        if enrichmentType == 'F':
            if nLep == 2:
                f1 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
            elif nLep == 0:
                f1 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_HT_psZJF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_BE_psZJF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_HT_psZJF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zvv2017/plots_stitching_checks_BE_psZJF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
            elif nLep == 1:
                f1 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_HT_psWJF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_BE_psWJF/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_HT_psWJF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Wlv2017/plots_stitching_checks_BE_psWJF_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
        else:
            if nLep == 2:
                f1 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYB/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f2 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYB/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f3 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_HT_psDYB_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
                f4 = ROOT.TFile.Open("./logs_Zll2017/plots_stitching_checks_BE_psDYB_RWR/Plots/Inclusive__LHE_Vpt_.shapes.root","READ")
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

        altText = "SR/HF-CR (no mjj)"

        h1 = f1.Get("summedMcHistograms")
        h2 = f2.Get("summedMcHistograms")
        h3 = f3.Get("summedMcHistograms")
        h4 = f4.Get("summedMcHistograms")

        # make b-enriched shape similar to inclusive+HT binned
        # -> shape_BE * RW(HT/BE)
        h1.Divide(h2)
        h1.SetTitle("ratio: (incl.+HT) / b-enriched {nLep} type {enrichmentType}".format(nLep=nLep,enrichmentType=enrichmentType))
        h1.SetStats(0)
        h1.Draw()
        h1.GetYaxis().SetRangeUser(0,3.0)
        h1.GetXaxis().SetRangeUser(90.0,510.0)
        h1.GetXaxis().SetTitle("LHE_Vpt")
        h3.SetStats(0)


        fitModel    = "[0]+[1]*TMath::Min(x,300.0)+[2]*TMath::Min(x,300.0)**2"
        fitRangeMin = 100
        fitRangeMax = 600
            
        polFit = ROOT.TF1("f1",fitModel, fitRangeMin, fitRangeMax)
        h1.Fit(polFit, "R")
        fitResult = h1.Fit(polFit, "RS")

        fitParListWithErrors = sum([ [polFit.GetParameter(i), polFit.GetParError(i)] for i in range(polFit.GetNpar())], [])
        print("\x1b[32mFIT RESULT:", ["%1.4e"%x for x in fitParListWithErrors], "\x1b[0m") 

        grint = ROOT.TGraphErrors(h1.GetXaxis().GetNbins())
        for i in range(h1.GetXaxis().GetNbins()):
            grint.SetPoint(i,h1.GetBinCenter(1+i), 0)
        ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint, 0.95)
        grint.SetLineColor(ROOT.kRed)
        grint.Draw("p same")



        h3.Divide(h4)
        h3.SetMarkerColor(ROOT.kBlue+2)
        h3.SetLineColor(ROOT.kBlue+2)
        h3.SetMarkerStyle(22)
        h3.Draw("same")

        polFit2 = ROOT.TF1("f2",fitModel, fitRangeMin, fitRangeMax)
        polFit2.SetLineColor(ROOT.kBlue)
        h3.Fit(polFit2, "R")
        fitResult2 = h3.Fit(polFit2, "RS")

        fitParListWithErrors2 = sum([ [polFit2.GetParameter(i), polFit2.GetParError(i)] for i in range(polFit2.GetNpar())], [])
        print("\x1b[32mFIT RESULT 2:", ["%1.4e"%x for x in fitParListWithErrors2], "\x1b[0m") 

        grint2 = ROOT.TGraphErrors(h3.GetXaxis().GetNbins())
        for i in range(h3.GetXaxis().GetNbins()):
            grint2.SetPoint(i,h3.GetBinCenter(1+i), 0)
        ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(grint2, 0.95)
        grint2.SetLineColor(ROOT.kBlue)
        grint2.Draw("p same")

        h1.SetFillStyle(0)
        h3.SetFillStyle(0)
        h1.SetFillColor(0)
        h3.SetFillColor(0)

        leg = ROOT.TLegend(0.15,0.7,0.5,0.88)
        leg.AddEntry(h1, "loose sel.")
        leg.AddEntry(polFit, "fit")
        leg.AddEntry(h3, altText) 
        leg.AddEntry(polFit2, "fit")
        leg.Draw()

        fitFormulaString = fitModel
        for i in range(polFit2.GetNpar()):
            fitFormulaString = fitFormulaString.replace("[%i]"%i, "(%1.4e+/-%1.4e)"%(polFit2.GetParameter(i),  polFit2.GetParError(i)))
        fitFormulaString = fitFormulaString.replace("TMath::Min","min")

        text = ROOT.TText(105,0.15,fitFormulaString)
        text.SetTextSize(0.025)
        text.SetTextColor(ROOT.kBlue+2)
        text.SetTextAlign(12)
        text.Draw()

        for ext in ['png','pdf','root']:
            c1.SaveAs("reweighting_b_enriched_{nLep}{enrichmentType}.{ext}".format(nLep=nLep,enrichmentType=enrichmentType,ext=ext))

        ROOT.gPad.Update()


