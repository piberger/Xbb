#!/bin/bash
#TEMP=`mktemp -d`
#OLDPWD=$PWD
#cp BTagCalibrationStandalone.cpp $TEMP
#cp BTagCalibrationStandalone.h $TEMP
#cp init_btag.cc $TEMP
#echo $TEMP
#ls $TEMP
#cd $TEMP
root -b -l -q ./init_btag.cc
#cp $TEMP/BTagCalibrationStandalone* $OLDPWD
#rm $TEMP/BTagCalibrationStandalone*
#rm $TEMP/init_btag.cc
