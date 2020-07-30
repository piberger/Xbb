#!/bin/bash
echo "usage: $0 path/to/FitDiagnostics.root name"
echo "this will create DNN postfit plots!"

for FITTYPE in shapes_prefit shapes_fit_s; do
./submit.py -T Zvv2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS_NoQCD!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:='${FITTYPE}';Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitCRDNN_BKG.log:=True;plotDef:postfitCRDNN_BKG.log:=True;plotDef:postfitNormalization.log=False;plotDef:postfitNormalization.nBins=2;plotDef:postfitNormalization.max=2;plotDef:postfitNormalization.min=0;plotDef:postfitNormalization.xAxis=CR' --local -F postfit_$2 --region="Zhf_med_Znn,Zlf_med_Znn,ttbar_med_Znn,Zhf_high_Znn,Zlf_high_Znn,ttbar_high_Znn,Zhf_high_Znn_BOOST,Zlf_high_Znn_BOOST,ttbar_high_Znn_BOOST";
./submit.py -T Wlv2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;plotDef:postfitMultiDNNbackground.log:=True;Fit.FitDiagnosticsDump:='$1';Fit.FitType:='${FITTYPE}';Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitNormalization.log=False;plotDef:postfitNormalization.nBins=2;plotDef:postfitNormalization.max=2;plotDef:postfitNormalization.min=0;plotDef:postfitNormalization.xAxis=CR' --local -F postfit_$2 --region="ttbar_high_Wen,ttbar_high_Wmn,Wlf_high_Wen,Wlf_high_Wmn,Whf_high_Wen,Whf_high_Wmn,Wlf_high_Wmn_BOOST,Wlf_high_Wen_BOOST,Whf_high_Wmn_BOOST,Whf_high_Wen_BOOST,ttbar_high_Wen_BOOST,ttbar_high_Wmn_BOOST,ttbar_med_Wen,ttbar_med_Wmn,Wlf_med_Wen,Wlf_med_Wmn,Whf_med_Wen,Whf_med_Wmn";
./submit.py -T Zll2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;plotDef:postfitMultiDNNbackground.log:=True;Fit.FitDiagnosticsDump:='$1';Fit.FitType:='${FITTYPE}';Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitNormalization.log=False;plotDef:postfitNormalization.nBins=2;plotDef:postfitNormalization.max=2;plotDef:postfitNormalization.min=0;plotDef:postfitNormalization.xAxis=CR' --local -F postfit_$2 --region="Zhf_low_Zee,Zhf_low_Zmm,Zhf_med_Zee,Zhf_med_Zmm,Zhf_high_Zee,Zhf_high_Zmm,Zlf_low_Zee,ttbar_low_Zee,Zlf_low_Zmm,ttbar_low_Zmm,Zlf_med_Zee,ttbar_med_Zee,Zlf_med_Zmm,ttbar_med_Zmm,Zlf_high_Zee,ttbar_high_Zee,Zlf_high_Zmm,ttbar_high_Zmm,Zlf_high_Zee_BOOST,ttbar_high_Zee_BOOST,Zlf_high_Zmm_BOOST,ttbar_high_Zmm_BOOST,Zhf_high_Zee_BOOST,Zhf_high_Zmm_BOOST";
done

mkdir postfit_$2
cp logs_Zll2017/postfit_$2/Plots/* postfit_$2/
cp logs_Zvv2017/postfit_$2/Plots/* postfit_$2/
cp logs_Wlv2017/postfit_$2/Plots/* postfit_$2/
