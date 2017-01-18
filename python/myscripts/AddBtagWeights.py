###################################
#Inclde low/high/central/forward bTag weights using macro from Stephane
###################################

import os
import subprocess
import ROOT

#_path = '/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V24/singlesys_23_final/'
_path = '/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V24/mva_v23_final/'
done_samples = os.listdir('/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V24/mva_v23_wBtagW')

n_simul_jobs = 5
counter = 0

FILE = os.listdir(_path)
for file in FILE:
    if not '.root' in file: continue
    print 'file is', file
    #if not 'ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_ext1' in file: continue
    if not 'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1' in file: continue
    #if 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX' in file: continue
    #if 'DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext1' in file: continue
    #if 'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1' in file: continue
    #if 'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_ext1' in file: continue
    #if 'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_ext1' in file: continue
    #if 'TT_pow' in file: continue
    #if 'ZZ_amc' in file: continue

    #if any(file in s for s in done_samples):
    #    print 'this sample is already done'
    #    continue

    ifile_ = 'root://t3dcachedb03.psi.ch:1094/' + _path + file
    #ofile_ = 'BtagWFiles/'+file
    ofile_ = '/scratch/gaperrin/BtagWFiles/'+file

    subprocess.call('python bTagSF.py %s %s 2>&1 > /dev/null &' %(ifile_, ofile_), shell=True)

    counter = int(subprocess.check_output('ps aux | grep $USER | grep bTagSF.py | wc -l', shell=True)) -2
    while counter > n_simul_jobs:
        print 'Counter is', counter, '. Gonna sleeZzz...Zzz...'
        os.system('sleep '+str(30))
        counter = int(subprocess.check_output('ps aux | grep $USER | grep bTagSF.py | wc -l', shell=True)) -2

