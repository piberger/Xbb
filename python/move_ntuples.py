#! /usr/bin/env python
import sys,os,shutil,ROOT

# TO BE CUSTOMIZED
indir = '/scratch/perrozzi/VHbb13TeVntuples/V12/V12all/merged/'
outdir = '/pnfs/psi.ch/cms/trivcat/store/t3groups/ethz-higgs/run2/V12/'

filelist = os.popen('ls '+indir).read()
filelist = filelist.split('\n')
filelist = [w.replace('\r','') for w in filelist]
filelist = filter(None, filelist) # fastest

for file in filelist:
    print'##############################################################'
    init_size = os.popen('ls -lrt '+indir+'/'+file).read()
    check_file = int(os.popen('ls /scratch/perrozzi/gfalFS/T3_CH_PSI/'+outdir+'/'+file+'|wc -l').read())
    if check_file==1:
      print(os.popen('ls -lrt '+indir+'/'+file).read())
      print os.popen('ls -lrt /scratch/perrozzi/gfalFS/T3_CH_PSI/'+outdir+'/'+file).read()
      nb = raw_input('Overwrite? ')
      if nb == 'y':
        os.system('rm /scratch/perrozzi/gfalFS/T3_CH_PSI/'+outdir+'/'+file)
        check_file = 0
    if check_file==0:
      os.popen('srmcp -2 -globus_tcp_port_range 20000,25000 file:///'+indir+'/'+file+' srm://t3se01.psi.ch:8443/srm/managerv2?SFN=/'+outdir+'/'+file)
      print os.popen('ls -lrt /scratch/perrozzi/gfalFS/T3_CH_PSI/'+outdir+'/'+file).read()

print 'finished'
