#! /usr/bin/env python
import sys,os,shutil,ROOT

# TO BE CUSTOMIZED
dir = '/pnfs/psi.ch/cms/trivcat/store/user/perrozzi/test_merge/syst/'

files = os.popen('ls '+dir+' |grep root').read()

files = files.split('\n')
files = filter(None, files) # fastest

zombies = 0
for file in files:
    file = 'dcap://t3se01.psi.ch:22125/'+dir+file
    infile = ROOT.TFile.Open(file)
    if infile.IsZombie(): 
        print file,'Is Zombie!'
        zombies = zombies+1

print 'checked',len(files),'files,',zombies,'zombies'