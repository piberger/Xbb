#! /usr/bin/env python
import sys,os,shutil,ROOT

# TO BE CUSTOMIZED
outdir = '/scratch/perrozzi/VHbb13TeVntuples/V12/V12all/'

filelist = '/scratch/perrozzi/VHbb13TeVntuples/V12/V12all/filelist.log'

if not os.path.exists(outdir+'/merged'):
    os.makedirs(outdir+'/merged')

all_files = os.popen('ls '+outdir).read()
all_files = all_files.split('\n')
single_files = all_files
single_files = [w.split('_tree')[0] for w in single_files]
single_files = [w.replace('\r','') for w in single_files]
single_files = filter(None, single_files) 
single_files = list(set(single_files))

for basename in single_files:
    if '.root' in basename: continue
    if 'merged' in basename: continue
    if '.log' in basename: continue
    string = 'hadd -f '+outdir+'/merged'+'/'+basename+'.root '
    check = float(os.popen('ls '+outdir+'/merged'+'/'+basename+'.root |wc -l').read())
    if check == 1: continue
    for file in all_files:
      # print file
      if basename in file:
        string = string+' '+outdir+'/'+file
    print string
    os.system(string)
    # sys.exit()

# datasets = os.popen('more '+filelist).read()

# datasets = datasets.split('\n')
# datasets = [w.replace('\r','') for w in datasets]
# datasets = filter(None, datasets) # fastest
# # print datasets

# count=1

# for dataset in datasets:
    # files = os.popen('python ./das_client.py --query=\"file dataset='+dataset+' instance=prod/phys03\"').read()
    # files = files.split('\n')
    # files = [w.replace('\r','') for w in files]
    # files = filter(None, files) # fastest
    # files =  [elem for elem in files if "/store" in elem]
    # # print dataset
    # # print files
    # for file in files:
      # outfile = file.split('/')[6]+'_'+file.split('/')[9]
      # all_files = float(os.popen('ls '+outdir+'/'+outfile+'|wc -l').read())
      # print outfile,all_files,all_files != 1
      # if all_files != 1:
        # print 'running',os.popen('ps aux | grep $USER | grep xrdcp |wc -l').read()
        # while float(os.popen('ps aux | grep $USER | grep xrdcp |wc -l').read())>5: 
          # print os.popen('ps aux | grep $USER | grep xrdcp |wc -l').read(),' running, waiting 30 seconds'; 
          # os.system('sleep 30')
        # # if(count%6==0): print 'waiting 60 sec'; os.system('sleep 60')
        # print 'copy',outfile
        # # os.system('xrdcp root://cms-xrd-global.cern.ch/'+file+' '+outdir+'/'+outfile+'&')
        # os.system('xrdcp root://xrootd.ba.infn.it/'+file+' '+outdir+'/'+outfile+'&')
        # count = count+1
      # else: print 'skipping' 
      # # sys.exit()
    # # infile = ROOT.TFile.Open(dataset)
    # # if infile.IsZombie(): 
        # # print dataset,'Is Zombie!'
        # # zombies = zombies+1

# print 'finished'
# # print 'checked',len(datasets),'datasets,',zombies,'zombies'
