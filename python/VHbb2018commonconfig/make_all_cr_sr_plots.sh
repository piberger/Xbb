#!/bin/sh
echo "(this makes all CR+SR plots for all channels with SF from fit applied)"
echo "enter folder name:"
read PLOTDIR
echo "saving plots to: ${PLOTDIR}, press any key to continue"

read -n 1 -s -r -p "Press any key to continue"

./submit.py -J runplot --parallel=8 --regions 'SR_high_Zee' --set='General.SF_TT=0.837441384792;General.SF_ZJets=[0.944891571999,1.01359498501,0.725618302822];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'SR_high_Zmm' --set='General.SF_TT=0.87372303009;General.SF_ZJets=[0.953935265541,1.0585026741,0.752622008324];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'SR_med_Zee' --set='General.SF_TT=0.837441384792;General.SF_ZJets=[0.944891571999,1.01359498501,0.725618302822];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'SR_med_Zmm' --set='General.SF_TT=0.87372303009;General.SF_ZJets=[0.953935265541,1.0585026741,0.752622008324];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'SR_low_Zee' --set='General.SF_TT=0.862698316574;General.SF_ZJets=[0.99000197649,0.887936115265,0.689128398895];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'SR_low_Zmm' --set='General.SF_TT=0.903396010399;General.SF_ZJets=[1.03968167305,0.922896504402,0.701815366745];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017

./submit.py -J runplot --parallel=8 --regions 'ttbar_high_Zee' --set='General.SF_TT=0.837676882744;General.SF_ZJets=[0.990469396114,1.01253032684,0.731635928154];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_high_Zmm' --set='General.SF_TT=0.872848749161;General.SF_ZJets=[0.995450675488,1.05015695095,0.749461293221];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_med_Zee' --set='General.SF_TT=0.837676882744;General.SF_ZJets=[0.990469396114,1.01253032684,0.731635928154];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_med_Zmm' --set='General.SF_TT=0.872848749161;General.SF_ZJets=[0.995450675488,1.05015695095,0.749461293221];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_low_Zee' --set='General.SF_TT=0.861741542816;General.SF_ZJets=[0.985073924065,0.90275233984,0.682124555111];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_low_Zmm' --set='General.SF_TT=0.899236381054;General.SF_ZJets=[1.09632658958,0.971735417843,0.727545142174];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017

./submit.py -J runplot --parallel=8 --regions 'Whf_high_Zee' --set='General.SF_TT=0.829375624657;General.SF_ZJets=[0.952968537807,1.01248598099,0.720306456089];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zhf_high_Zmm' --set='General.SF_TT=0.876134216785;General.SF_ZJets=[0.96587318182,1.04794371128,0.752240598202];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Whf_med_Zee' --set='General.SF_TT=0.829375624657;General.SF_ZJets=[0.952968537807,1.01248598099,0.720306456089];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zhf_med_Zmm' --set='General.SF_TT=0.876134216785;General.SF_ZJets=[0.96587318182,1.04794371128,0.752240598202];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zhf_low_Zee' --set='General.SF_TT=0.864887177944;General.SF_ZJets=[0.979775428772,0.958690643311,0.707998991013];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zhf_low_Zmm' --set='General.SF_TT=0.898682177067;General.SF_ZJets=[0.986830770969,0.929006159306,0.71709227562];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017

./submit.py -J runplot --parallel=8 --regions 'Zlf_high_Zee' --set='General.SF_TT=0.787740170956;General.SF_ZJets=[0.771099627018,0.966122746468,0.681974232197];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zlf_high_Zmm' --set='General.SF_TT=0.804518580437;General.SF_ZJets=[0.806298851967,0.996399700642,0.7394323349];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zlf_med_Zee' --set='General.SF_TT=0.787740170956;General.SF_ZJets=[0.771099627018,0.966122746468,0.681974232197];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zlf_med_Zmm' --set='General.SF_TT=0.804518580437;General.SF_ZJets=[0.806298851967,0.996399700642,0.7394323349];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zlf_low_Zee' --set='General.SF_TT=0.856904327869;General.SF_ZJets=[0.850623607635,0.890011847019,0.69317227602];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017
./submit.py -J runplot --parallel=8 --regions 'Zlf_low_Zmm' --set='General.SF_TT=0.886552155018;General.SF_ZJets=[0.877430140972,0.912353277206,0.701307952404];General.SF_WJets=[1.0,1.0,1.0]' -F ${PLOTDIR} -T Zll2017


./submit.py -J runplot --parallel=8 --regions 'Whf_med_Wen' --set='General.SF_TT=0.935850918293;General.SF_ZJets=[1.00691878796,0.976849555969,1.01604497433];General.SF_WJets=[1.06233108044,1.76807832718,1.167121768]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'SR_med_Wmn' --set='General.SF_TT=0.985979616642;General.SF_ZJets=[1.02522134781,1.10341393948,1.07637345791];General.SF_WJets=[1.23262929916,1.87706780434,1.19276082516]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'Wlf_med_Wmn' --set='General.SF_TT=0.942602872849;General.SF_ZJets=[1.05306506157,1.0027462244,1.03078532219];General.SF_WJets=[1.10312736034,1.80388760567,1.16774392128]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'Wlf_med_Wen' --set='General.SF_TT=0.916436314583;General.SF_ZJets=[1.01249575615,0.966426193714,1.00642311573];General.SF_WJets=[1.08975803852,1.74609386921,1.1345897913]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'SR_med_Wen' --set='General.SF_TT=0.947482049465;General.SF_ZJets=[1.02102196217,1.00171768665,1.03684830666];General.SF_WJets=[1.07794475555,1.87079274654,1.15540778637]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_med_Wmn' --set='General.SF_TT=0.947671711445;General.SF_ZJets=[1.15607047081,1.02284502983,1.07334494591];General.SF_WJets=[1.13791167736,1.82596707344,1.19283390045]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'Whf_med_Wmn' --set='General.SF_TT=0.97264277935;General.SF_ZJets=[1.15896070004,1.01207351685,1.05474245548];General.SF_WJets=[1.1853376627,1.8385642767,1.20151615143]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_med_Wen' --set='General.SF_TT=0.920777976513;General.SF_ZJets=[1.11521649361,0.991069972515,1.05435204506];General.SF_WJets=[1.13147747517,1.76934015751,1.15857231617]' -F ${PLOTDIR} -T Wlv2017

./submit.py -J runplot --parallel=8 --regions 'Whf_high_Wen' --set='General.SF_TT=0.935850918293;General.SF_ZJets=[1.00691878796,0.976849555969,1.01604497433];General.SF_WJets=[1.06233108044,1.76807832718,1.167121768]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'SR_high_Wmn' --set='General.SF_TT=0.985979616642;General.SF_ZJets=[1.02522134781,1.10341393948,1.07637345791];General.SF_WJets=[1.23262929916,1.87706780434,1.19276082516]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'Wlf_high_Wmn' --set='General.SF_TT=0.942602872849;General.SF_ZJets=[1.05306506157,1.0027462244,1.03078532219];General.SF_WJets=[1.10312736034,1.80388760567,1.16774392128]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'Wlf_high_Wen' --set='General.SF_TT=0.916436314583;General.SF_ZJets=[1.01249575615,0.966426193714,1.00642311573];General.SF_WJets=[1.08975803852,1.74609386921,1.1345897913]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'SR_high_Wen' --set='General.SF_TT=0.947482049465;General.SF_ZJets=[1.02102196217,1.00171768665,1.03684830666];General.SF_WJets=[1.07794475555,1.87079274654,1.15540778637]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_high_Wmn' --set='General.SF_TT=0.947671711445;General.SF_ZJets=[1.15607047081,1.02284502983,1.07334494591];General.SF_WJets=[1.13791167736,1.82596707344,1.19283390045]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'Whf_high_Wmn' --set='General.SF_TT=0.97264277935;General.SF_ZJets=[1.15896070004,1.01207351685,1.05474245548];General.SF_WJets=[1.1853376627,1.8385642767,1.20151615143]' -F ${PLOTDIR} -T Wlv2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_high_Wen' --set='General.SF_TT=0.920777976513;General.SF_ZJets=[1.11521649361,0.991069972515,1.05435204506];General.SF_WJets=[1.13147747517,1.76934015751,1.15857231617]' -F ${PLOTDIR} -T Wlv2017

./submit.py -J runplot --parallel=8 --regions 'Zlf_med_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.964708387852;General.SF_ZJets=[1.02653110027,0.916591346264,1.00535476208];General.SF_WJets=[1.10950660706,1.6721777916,1.31362521648]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_med_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.993492424488;General.SF_ZJets=[1.01904940605,1.0,1.01971065998];General.SF_WJets=[1.1913381815,1.7492171526,1.37831902504]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'SR_med_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.991339862347;General.SF_ZJets=[1.0758535862,0.944496154785,1.0404740572];General.SF_WJets=[1.14279294014,1.72214496136,1.36236417294]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'Zhf_med_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.950146436691;General.SF_ZJets=[1.05793190002,0.916414678097,1.01453232765];General.SF_WJets=[1.16985535622,1.69667816162,1.32072985172]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'Zlf_high_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.964708387852;General.SF_ZJets=[1.02653110027,0.916591346264,1.00535476208];General.SF_WJets=[1.10950660706,1.6721777916,1.31362521648]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'ttbar_high_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.993492424488;General.SF_ZJets=[1.01904940605,1.0,1.01971065998];General.SF_WJets=[1.1913381815,1.7492171526,1.37831902504]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'SR_high_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.991339862347;General.SF_ZJets=[1.0758535862,0.944496154785,1.0404740572];General.SF_WJets=[1.14279294014,1.72214496136,1.36236417294]' -F ${PLOTDIR} -T Zvv2017
./submit.py -J runplot --parallel=8 --regions 'Zhf_high_Znn' --set='Stitching.MethodZJ=V11;General.SF_TT=0.950146436691;General.SF_ZJets=[1.05793190002,0.916414678097,1.01453232765];General.SF_WJets=[1.16985535622,1.69667816162,1.32072985172]' -F ${PLOTDIR} -T Zvv2017

