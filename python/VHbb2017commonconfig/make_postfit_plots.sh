#!/bin/bash
echo "usage: $0 path/to/FitDiagnostics.root name"
echo "this will create DNN postfit plots!"

./submit.py -T Zvv2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS_NoQCD!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_fit_s;Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitCRDNN_BKG.log:=True' --local -F postfit_$2
./submit.py -T Zvv2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS_NoQCD!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_prefit;Plot_general.mcUncertaintyLegend:="MC uncert.";plotDef:postfitCRDNN_BKG.log:=True' --local -F postfit_$2

./submit.py -T Wlv2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;plotDef:postfitMultiDNNbackground.log:=True;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_fit_s;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2
./submit.py -T Wlv2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;plotDef:postfitMultiDNNbackground.log:=True;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_prefit;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2

./submit.py -T Zll2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;plotDef:postfitMultiDNNbackground.log:=True;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_fit_s;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2
./submit.py -T Zll2017 -J postfitplot --set='LimitGeneral.setup=<!LimitGeneral|setup_NoSTXS!>;LimitGeneral.Group=<!VHbbCommon|GroupNoSTXS!>;plotDef:postfitMultiDNNbackground.log:=True;Fit.FitDiagnosticsDump:='$1';Fit.FitType:=shapes_prefit;Plot_general.mcUncertaintyLegend:="MC uncert."' --local -F postfit_$2

mkdir postfit_$2
cp logs_Zll2017/postfit_$2/Plots/* postfit_$2/
cp logs_Zvv2017/postfit_$2/Plots/* postfit_$2/
cp logs_Wlv2017/postfit_$2/Plots/* postfit_$2/
