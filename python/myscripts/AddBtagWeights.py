#!/usr/bin/env python
###################################
#Inclde low/high/central/forward bTag weights using macro from Stephane
###################################

import os
import subprocess
import ROOT

inputFolder = '/scratch/berger_p2/EWKQCD/'
outputFolder = '/scratch/berger_p2/SignalCorrAndBtag/'
logFolder = '/mnt/t3nfs01/data01/shome/berger_p2/VHbb/CMSSW_7_4_3/src/Xbb/python/logs_v24/SP_V24_addbtagw_v2/'

try:
    os.makedirs(outputFolder)
except:
    pass

try:
    os.mkdir(logFolder)
except:
    pass

done_samples = os.listdir(outputFolder)

n_simul_jobs = 5
counter = 0

FILE = os.listdir(inputFolder)
for file in FILE:
    if not '.root' in file: continue
    print 'file is', file

    ifile_ = ('root://t3dcachedb03.psi.ch:1094/' if inputFolder.strip('/').split('/')[0] == 'pnfn' else '') + inputFolder + file
    ofile_ = ('root://t3dcachedb03.psi.ch:1094/' if outputFolder.strip('/').split('/')[0] == 'pnfn' else '') + outputFolder + file
    logfile = logFolder + file.replace('.root','.log')

    subprocess.call('python bTagSF.py %s %s 2>&1 > %s &' %(ifile_, ofile_, logfile), shell=True)

    counter = int(subprocess.check_output('ps aux | grep $USER | grep bTagSF.py | wc -l', shell=True)) -2
    while counter > n_simul_jobs:
        print 'Counter is', counter, '. Gonna sleeZzz...Zzz...'
        os.system('sleep '+str(30))
        counter = int(subprocess.check_output('ps aux | grep $USER | grep bTagSF.py | wc -l', shell=True)) -2

