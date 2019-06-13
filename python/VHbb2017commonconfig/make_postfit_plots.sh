#!/bin/bash
./submit.py -T Zvv2017 -J postfitplot --set='Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_fit_s;Fit.regions:=<!Fit|regions_multi!>;Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitCRDNN_BKG.log:=True' --local -F postfit_$2
./submit.py -T Zvv2017 -J postfitplot --set='Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_prefit;Fit.regions:=<!Fit|regions_multi!>;Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitCRDNN_BKG.log:=True' --local -F postfit_$2

./submit.py -T Wlv2017 -J postfitplot --set='plotDef:postfitMultiDNNbackground.log:=True;Fit.regions:=<!Fit|regions_multi!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_fit_s;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2
./submit.py -T Wlv2017 -J postfitplot --set='plotDef:postfitMultiDNNbackground.log:=True;Fit.regions:=<!Fit|regions_multi!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_prefit;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2

./submit.py -T Zll2017 -J postfitplot --set='plotDef:postfitMultiDNNbackground.log:=True;Fit.regions:=<!Fit|regions_multi!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_fit_s;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2
./submit.py -T Zll2017 -J postfitplot --set='plotDef:postfitMultiDNNbackground.log:=True;Fit.regions:=<!Fit|regions_multi!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_prefit;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2

mkdir postfit_$2
cp logs_Zll2017/postfit_$2/Plots/* postfit_$2/
cp logs_Zvv2017/postfit_$2/Plots/* postfit_$2/
cp logs_Wlv2017/postfit_$2/Plots/* postfit_$2/
