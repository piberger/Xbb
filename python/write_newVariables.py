#!/usr/bin/env python
import sys,hashlib
import os,subprocess
import ROOT
import math
import shutil
from array import array
import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser
from btag_reweight import *
from time import gmtime, strftime
from muonSF import *

argv = sys.argv
parser = OptionParser()
parser.add_option("-S", "--samples", dest="names", default="",
                      help="samples you want to run on")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration defining the plots to make")
parser.add_option("-f", "--filelist", dest="filelist", default="",
                              help="list of files you want to run on")

(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = "config"

print 'opts.filelist="'+opts.filelist+'"'
filelist=filter(None,opts.filelist.replace(' ', '').split(';'))
print filelist
print "len(filelist)",len(filelist),
if len(filelist)>0:
    print "filelist[0]:",filelist[0];
else:
    print ''

from myutils import BetterConfigParser, ParseInfo, TreeCache

print opts.config
config = BetterConfigParser()
config.read(opts.config)
anaTag = config.get("Analysis","tag")
TrainFlag = eval(config.get('Analysis','TrainFlag'))
btagLibrary = config.get('BTagReshaping','library')
samplesinfo=config.get('Directories','samplesinfo')
channel=config.get('Configuration','channel')
print 'channel is', channel

VHbbNameSpace=config.get('VHbbNameSpace','library')
ROOT.gSystem.Load(VHbbNameSpace)
ROOT.gROOT.LoadMacro("../interface/VHbbNameSpace.h")


AngLikeBkgs=eval(config.get('AngularLike','backgrounds'))
ang_yield=eval(config.get('AngularLike','yields'))

pathIN = config.get('Directories','SYSin')
pathOUT = config.get('Directories','SYSout')
tmpDir = os.environ["TMPDIR"]

print 'INput samples:\t%s'%pathIN
print 'OUTput samples:\t%s'%pathOUT

namelist=opts.names.split(',')

#load info
info = ParseInfo(samplesinfo,pathIN)

def isInside(map_,eta,phi):
    bin_ = map_.FindBin(phi,eta)
    bit = map_.GetBinContent(bin_)
    if bit>0:
        return True
    else:
        return False

if channel == "Znn":
    filt = ROOT.TFile("plot.root")
    NewUnder    = filt.Get("NewUnder")
    NewOver     = filt.Get("NewOver")
    NewUnderQCD = filt.Get("NewUnderQCD")
    NewOverQCD  = filt.Get("NewOverQCD")

for job in info:
    if not job.name in namelist and len([x for x in namelist if x==job.identifier])==0:
        print 'job.name',job.name,'and job.identifier',job.identifier,'not in namelist',namelist
        continue

    inputfiles = []
    outputfiles = []
    tmpfiles = []
    if len(filelist) == 0:
        inputfiles.append(pathIN+'/'+job.prefix+job.identifier+'.root')
        print('opening '+pathIN+'/'+job.prefix+job.identifier+'.root')
        tmpfiles.append(tmpDir+'/'+job.prefix+job.identifier+'.root')
        outputfiles.append("%s/%s/%s" %(pathOUT,job.prefix,job.identifier+'.root'))
    else:
        for inputFile in filelist:
            subfolder = inputFile.split('/')[-4]
            filename = inputFile.split('/')[-1]
            filename = filename.split('_')[0]+'_'+subfolder+'_'+filename.split('_')[1]
            hash = hashlib.sha224(filename).hexdigest()
            inputFile = "%s/%s/%s" %(pathIN,job.identifier,filename.replace('.root','')+'_'+str(hash)+'.root')
            outputFile = "%s/%s/%s" %(pathOUT,job.identifier,filename.replace('.root','')+'_'+str(hash)+'.root')
            tmpfile = "%s/%s" %(tmpDir,filename.replace('.root','')+'_'+str(hash)+'.root')
            if inputFile in inputfiles: continue
            del_protocol = outputFile
            del_protocol = del_protocol.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
            del_protocol = del_protocol.replace('dcap://t3se01.psi.ch:22125/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
            del_protocol = del_protocol.replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
            if os.path.isfile(del_protocol.replace('srm://t3se01.psi.ch:8443/srm/managerv2?SFN=','')):
                f = ROOT.TFile.Open(outputFile,'read')
                if not f:
                  print 'file is null, adding to input'
                  inputfiles.append(inputFile)
                  outputfiles.append(outputFile)
                  tmpfiles.append(tmpfile)
                  continue
                # f.Print()
                if f.GetNkeys() == 0 or f.TestBit(ROOT.TFile.kRecovered) or f.IsZombie():
                    print 'f.GetNkeys()',f.GetNkeys(),'f.TestBit(ROOT.TFile.kRecovered)',f.TestBit(ROOT.TFile.kRecovered),'f.IsZombie()',f.IsZombie()
                    print 'File', del_protocol.replace('srm://t3se01.psi.ch:8443/srm/managerv2?SFN=',''), 'already exists but is buggy, gonna delete and rewrite it.'
                    #command = 'rm %s' %(outputFile)
                    command = 'srmrm %s' %(del_protocol)
                    subprocess.call([command], shell=True)
                    print(command)
                else: continue
            inputfiles.append(inputFile)
            outputfiles.append(outputFile)
            tmpfiles.append(tmpfile)
        print 'inputfiles',inputfiles,'tmpfiles',tmpfiles

    for inputfile,tmpfile,outputFile in zip(inputfiles,tmpfiles,outputfiles):
        input = ROOT.TFile.Open(inputfile,'read')
        output = ROOT.TFile.Open(tmpfile,'recreate')
        print ''
        print 'inputfile',inputfile
        print "Writing: ",tmpfile
        print 'outputFile',outputFile
        print ''

        input.cd()
        obj = ROOT.TObject
        for key in ROOT.gDirectory.GetListOfKeys():
            input.cd()
            obj = key.ReadObj()
            if obj.GetName() == job.tree:
                continue
            output.cd()
            obj.Write(key.GetName())

        input.cd()
        tree = input.Get(job.tree)
        nEntries = tree.GetEntries()

        output.cd()
        newtree = tree.CloneTree(0)

        if True:
            writeNewVariables = eval(config.get("Regression","writeNewVariables"))

            ## remove MC variables in data ##
            if job.type == 'DATA':
                for idx in dict(writeNewVariables):
                    formula = writeNewVariables[idx]
                    if 'gen' in formula or 'Gen' in formula or 'True' in formula or 'true' in formula or 'mc' in formula or 'Mc' in formula:
                        print "Removing: ",idx," with ",formula
                        del writeNewVariables[idx]

            newVariableNames = writeNewVariables.keys()
            newVariables = {}
            newVariableFormulas = {}
            for variableName in newVariableNames:
                formula = writeNewVariables[variableName]
                formula.replace(" ","")
                newVariables[variableName] = array('f',[0])
                newtree.Branch(variableName,newVariables[variableName],variableName+'/F')
                newVariableFormulas[variableName] =ROOT.TTreeFormula(variableName,formula,tree)
                print "adding variable ",variableName,", using formula",writeNewVariables[variableName]," ."
#        except:
#            pass

        print 'starting event loop, processing',str(nEntries),'events'
        j_out=1;

        #########################
        #Start event loop
        #########################

        for entry in range(0,nEntries):
                # if entry>1000: break
                if ((entry%j_out)==0):
                    if ((entry/j_out)==9 and j_out < 1e4): j_out*=10;
                    print strftime("%Y-%m-%d %H:%M:%S", gmtime()),' - processing event',str(entry)+'/'+str(nEntries), '(cout every',j_out,'events)'
                    sys.stdout.flush()

                tree.GetEntry(entry)

                ### Fill new variable from configuration ###
                for variableName in newVariableNames:
                    newVariableFormulas[variableName].GetNdata()
                    newVariables[variableName][0] = newVariableFormulas[variableName].EvalInstance()

                if channel == "ZnnFIXME":
                    for i in range(tree.nJet):
                        Jet_under[i]    = isInside(NewUnder   ,tree.Jet_eta[i],tree.Jet_phi[i])
                        Jet_over[i]     = isInside(NewOver    ,tree.Jet_eta[i],tree.Jet_phi[i])
                        Jet_underMC[i]  = isInside(NewUnderQCD,tree.Jet_eta[i],tree.Jet_phi[i])
                        Jet_overMC[i]   = isInside(NewOverQCD ,tree.Jet_eta[i],tree.Jet_phi[i])
                        Jet_bad[i]      = Jet_under[i] or Jet_over[i] or Jet_underMC[i] or Jet_overMC[i]
                    # for i in range(tree.nDiscardedJet):
                        # DiscardedJet_under[i]    = isInside(NewUnder   ,tree.DiscardedJet_eta[i],tree.DiscardedJet_phi[i])
                        # DiscardedJet_over[i]     = isInside(NewOver    ,tree.DiscardedJet_eta[i],tree.DiscardedJet_phi[i])
                        # DiscardedJet_underMC[i]  = isInside(NewUnderQCD,tree.DiscardedJet_eta[i],tree.DiscardedJet_phi[i])
                        # DiscardedJet_overMC[i]   = isInside(NewOverQCD ,tree.DiscardedJet_eta[i],tree.DiscardedJet_phi[i])
                        # DiscardedJet_bad[i]      = DiscardedJet_under[i] or DiscardedJet_over[i] or DiscardedJet_underMC[i] or DiscardedJet_overMC[i]
                    for i in range(tree.naLeptons):
                        aLeptons_under[i]    = isInside(NewUnder   ,tree.aLeptons_eta[i],tree.aLeptons_phi[i])
                        aLeptons_over[i]     = isInside(NewOver    ,tree.aLeptons_eta[i],tree.aLeptons_phi[i])
                        aLeptons_underMC[i]  = isInside(NewUnderQCD,tree.aLeptons_eta[i],tree.aLeptons_phi[i])
                        aLeptons_overMC[i]   = isInside(NewOverQCD ,tree.aLeptons_eta[i],tree.aLeptons_phi[i])
                        aLeptons_bad[i]      = aLeptons_under[i] or aLeptons_over[i] or aLeptons_underMC[i] or aLeptons_overMC[i]
                    for i in range(tree.nvLeptons):
                        vLeptons_under[i]    = isInside(NewUnder   ,tree.vLeptons_eta[i],tree.vLeptons_phi[i])
                        vLeptons_over[i]     = isInside(NewOver    ,tree.vLeptons_eta[i],tree.vLeptons_phi[i])
                        vLeptons_underMC[i]  = isInside(NewUnderQCD,tree.vLeptons_eta[i],tree.vLeptons_phi[i])
                        vLeptons_overMC[i]   = isInside(NewOverQCD ,tree.vLeptons_eta[i],tree.vLeptons_phi[i])
                        vLeptons_bad[i]      = vLeptons_under[i] or vLeptons_over[i] or vLeptons_underMC[i] or vLeptons_overMC[i]

                newtree.Fill()

        print 'Exit loop'
        newtree.AutoSave()
        print 'Save'
        output.Close()
        print 'Close'
        targetStorage = pathOUT.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')+'/'+job.prefix+job.identifier+'.root'
        if('pisa' in config.get('Configuration','whereToLaunch')):
            command = 'cp %s %s' %(tmpDir+'/'+job.prefix+job.identifier+'.root',targetStorage)
            print(command)
            subprocess.call([command], shell=True)
        else:
            command = 'srmmkdir %s' %(pathOUT.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')+'/'+job.identifier).replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch/')
            print(command)
            subprocess.call([command], shell=True)
            if len(filelist) == 0:
                command = 'srmrm %s' %(targetStorage.replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=/'))
                print(command)
                os.system(command)
                command = 'env -i X509_USER_PROXY=/shome/$USER/.x509up_u`id -u` gfal-copy file:////%s %s' %(tmpDir.replace('/mnt/t3nfs01/data01','')+'/'+job.prefix+job.identifier+'.root',targetStorage.replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch/'))
                print(command)
                os.system(command)
            else:
                srmpathOUT = pathOUT.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('dcap://t3se01.psi.ch:22125/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                command = 'srmcp -2 -globus_tcp_port_range 20000,25000 file:///'+tmpfile+' '+outputFile.replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                print command
                subprocess.call([command], shell=True)

                print 'checking output file',outputFile
                f = ROOT.TFile.Open(outputFile,'read')
                if not f or f.GetNkeys() == 0 or f.TestBit(ROOT.TFile.kRecovered) or f.IsZombie():
                    print 'TERREMOTO AND TRAGEDIA: THE MERGED FILE IS CORRUPTED!!! ERROR: exiting'
                    sys.exit(1)

                command = 'rm '+tmpfile
                print command
                subprocess.call([command], shell=True)
