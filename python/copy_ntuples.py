#! /usr/bin/env python
import sys,os,shutil,ROOT

# TO BE CUSTOMIZED
outdir = '/scratch/perrozzi/VHbb13TeVntuples/V12/V12all'

filelist = '/scratch/perrozzi/VHbb13TeVntuples/V12/V12all/ntuple_filelist_V12.log'

datasets = os.popen('more '+filelist).read()

datasets = datasets.split('\n')
datasets = [w.replace('\r','') for w in datasets]
datasets = filter(None, datasets) # fastest
# print datasets

count=1

for dataset in datasets:
    files = os.popen('python ./das_client.py --limit=0 --query=\"file dataset='+dataset+' instance=prod/phys03\"').read()
    files = files.split('\n')
    files = [w.replace('\r','') for w in files]
    files = filter(None, files) # fastest
    files =  [elem for elem in files if "/store" in elem]
    # print dataset
    # print files
    for file in files:
      outfile = file.split('/')[6]+'_'+file.split('/')[9]
      check = float(os.popen('ls '+outdir+'/'+outfile+'|wc -l').read())
      print outfile,check,check != 1
      if check != 1:
        print 'running',os.popen('ps aux | grep $USER | grep xrdcp |wc -l').read()
        while float(os.popen('ps aux | grep $USER | grep xrdcp |wc -l').read())>5: 
          print os.popen('ps aux | grep $USER | grep xrdcp |wc -l').read(),' running, waiting 30 seconds'; 
          os.system('sleep 10')
        # if(count%6==0): print 'waiting 60 sec'; os.system('sleep 60')
        print 'copy',outfile
        # os.system('xrdcp root://cms-xrd-global.cern.ch/'+file+' '+outdir+'/'+outfile+'&')
        os.system('xrdcp root://xrootd.ba.infn.it/'+file+' '+outdir+'/'+outfile+'&')
        count = count+1
      else: print 'skipping' 
      # sys.exit()
    # infile = ROOT.TFile.Open(dataset)
    # if infile.IsZombie(): 
        # print dataset,'Is Zombie!'
        # zombies = zombies+1

print 'finished'
# print 'checked',len(datasets),'datasets,',zombies,'zombies'
