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

from myutils import BetterConfigParser, ParseInfo, TreeCache, LeptonSF, bTagSF
#from btagSF import BtagSF
#import BtagSF
from bTagSF import *

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
AngLikeBkgs=eval(config.get('AngularLike','backgrounds'))
ang_yield=eval(config.get('AngularLike','yields'))

pathIN = config.get('Directories','SYSin')
pathOUT = config.get('Directories','SYSout')
tmpDir = os.environ["TMPDIR"]

print 'INput samples:\t%s'%pathIN
print 'OUTput samples:\t%s'%pathOUT

applyBTagweights=eval(config.get('Regression','applyBTagweights'))
print 'applyBTagweights is', applyBTagweights
csv_rwt_hf=config.get('BTagHFweights','file')
csv_rwt_lf=config.get('BTagLFweights','file')
applyRegression=eval(config.get('Regression','applyRegression'))
print 'applyRegression is', applyRegression
print "csv_rwt_hf",csv_rwt_hf,"csv_rwt_lf",csv_rwt_lf
bweightcalc = BTagWeightCalculator(
    csv_rwt_hf,
    csv_rwt_lf
)
bweightcalc.btag = "btag"

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

def deltaPhi(phi1, phi2): 
    result = phi1 - phi2
    while (result > math.pi): result -= 2*math.pi
    while (result <= -math.pi): result += 2*math.pi
    return result

def deltaR(phi1, eta1, phi2, eta2):
    deta = eta1-eta2
    dphi = deltaPhi(phi1, phi2)
    result = math.sqrt(deta*deta + dphi*dphi)
    return result

def addAdditionalJets(H, tree):
    for i in range(tree.nhjidxaddJetsdR08):
        idx = tree.hjidxaddJetsdR08[i]
        if (idx == tree.hJCidx[0]) or (idx == tree.hJCidx[1]): continue
        addjet = ROOT.TLorentzVector()
        if idx<tree.nJet:
            addjet.SetPtEtaPhiM(tree.Jet_pt[idx],tree.Jet_eta[idx],tree.Jet_phi[idx],tree.Jet_mass[idx])
        H = H + addjet
    return H

def resolutionBias(eta):
    if(eta< 0.5): return 0.052
    if(eta< 1.1): return 0.057
    if(eta< 1.7): return 0.096
    if(eta< 2.3): return 0.134
    if(eta< 5): return 0.28
    return 0

def corrPt(pt,eta,mcPt):
    return 1 ##FIXME
    # return (pt+resolutionBias(math.fabs(eta))*(pt-mcPt))/pt

def corrCSV(btag,  csv, flav):
    if(csv < 0.): return csv
    if(csv > 1.): return csv;
    if(flav == 0): return csv;
    if(math.fabs(flav) == 5): return  btag.ib.Eval(csv)
    if(math.fabs(flav) == 4): return  btag.ic.Eval(csv)
    if(math.fabs(flav) != 4  and math.fabs(flav) != 5): return  btag.il.Eval(csv)
    return -10000


def csvReshape(sh, pt, eta, csv, flav):
    return sh.reshape(float(eta), float(pt), float(csv), int(flav))

def computeSF(weight_SF):
    weight_SF[0] = (weight[0][0]*weight[1][0])
    weight_SF[1] = ( (weight[0][0]-weight[0][1])*(weight[1][0]-weight[1][1]) )
    weight_SF[2] = ( (weight[0][0]+weight[0][1])*(weight[1][0]+weight[1][1]) )

def computeEff(weight_Eff):
    eff1 = []
    eff2 = []
    eff1.append(weight[0][0])
    eff1.append(weight[0][0]-weight[0][1])
    eff1.append(weight[0][0]+weight[0][1])
    eff2.append(weight[1][0])
    eff2.append(weight[1][0]-weight[1][1])
    eff2.append(weight[1][0]+weight[1][1])
    weight_Eff[0] = (eff1[0]*(1-eff2[0])*eff1[0] + eff2[0]*(1-eff1[0])*eff2[0] + eff1[0]*eff1[0]*eff2[0]*eff2[0])
    weight_Eff[1] = (eff1[1]*(1-eff2[1])*eff1[1] + eff2[1]*(1-eff1[1])*eff2[1] + eff1[1]*eff1[1]*eff2[1]*eff2[1])
    weight_Eff[2] = (eff1[2]*(1-eff2[2])*eff1[2] + eff2[2]*(1-eff1[2])*eff2[2] + eff1[2]*eff1[2]*eff2[2]*eff2[2])
    return weight_Eff

def computeWeight(a, b):
    weight = []
    weight.append([])
    weight.append([])
    for i in range(2):
        weight[i].append(a*muTrigEffBfr[i][0] + b*muTrigEffAftr[i][0])
        weight[i].append(math.sqrt((a*muTrigEffBfr[i][1])**2 + (b*muTrigEffAftr[i][1])**2))
    return weight

#    muTrigEffBfr
#    muTrigEffAftr



if channel == "Znn":
    filt = ROOT.TFile("plot.root")
    NewUnder    = filt.Get("NewUnder")
    NewOver     = filt.Get("NewOver")
    NewUnderQCD = filt.Get("NewUnderQCD")
    NewOverQCD  = filt.Get("NewOverQCD")

for job in info:
    if not job.name in namelist and len([x for x in namelist if x==job.identifier])==0:
        #print 'job.name',job.name,'and job.identifier',job.identifier,'not in namelist',namelist
        continue
    ROOT.gROOT.ProcessLine(
        "struct H {\
        int         HiggsFlag;\
        float         mass;\
        float         pt;\
        float         eta;\
        float         phi;\
        float         dR;\
        float         dPhi;\
        float         dEta;\
        } ;"
    )
    #ROOT.gROOT.ProcessLine(
    #    "struct JET{\
    #    float         pt;\
    #    float         eta;\
    #    int         hadronFlavour;\
    #    float         btag;\
    #    } ;"
    #)
    class Jet :
        def __init__(self, pt, eta, fl, csv) :
            self.pt = pt
            self.eta = eta
            self.hadronFlavour = fl
            self.csv = csv

    
    lhe_weight_map = False if not config.has_option('LHEWeights', 'weights_per_bin') else eval(config.get('LHEWeights', 'weights_per_bin'))
    
    
    print '\t match - %s' %(job.name)
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
            #if not os.path.isfile(inputFile): continue
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

        H = ROOT.H()
        HNoReg = ROOT.H()
        HaddJetsdR08 = ROOT.H()
        HaddJetsdR08NoReg = ROOT.H()

        #Jet structure (to apply CSV weight)

        
       # tree.SetBranchStatus('H',0)
        output.cd()
        newtree = tree.CloneTree(0)

        hJ0 = ROOT.TLorentzVector()
        hJ1 = ROOT.TLorentzVector()
        vect = ROOT.TLorentzVector()
        # hFJ0 = ROOT.TLorentzVector()
        # hFJ1 = ROOT.TLorentzVector()

        if applyRegression == True:
            writeNewVariables = eval(config.get("Regression","writeNewVariables"))
            regWeight = config.get("Regression","regWeight")
            regDict = eval(config.get("Regression","regDict"))
            regVars = eval(config.get("Regression","regVars"))
            # regWeightFilterJets = config.get("Regression","regWeightFilterJets")
            # regDictFilterJets = eval(config.get("Regression","regDictFilterJets"))
            # regVarsFilterJets = eval(config.get("Regression","regVarsFilterJets"))

            # Regression branches
            # hJet_pt = array('f',[0]*2)
            # hJet_mass = array('f',[0]*2)
            newtree.Branch( 'H', H , 'HiggsFlag/I:mass/F:pt/F:eta/F:phi/F:dR/F:dPhi/F:dEta/F' )
            newtree.Branch( 'HNoReg', HNoReg , 'HiggsFlag/I:mass/F:pt/F:eta/F:phi/F:dR/F:dPhi/F:dEta/F' )
            newtree.Branch( 'HaddJetsdR08', HaddJetsdR08 , 'HiggsFlag/I:mass/F:pt/F:eta/F:phi/F:dR/F:dPhi/F:dEta/F' )
            newtree.Branch( 'HaddJetsdR08NoReg', HaddJetsdR08NoReg , 'HiggsFlag/I:mass/F:pt/F:eta/F:phi/F:dR/F:dPhi/F:dEta/F' )
            # FatHReg = array('f',[0]*2)
            # newtree.Branch('FatHReg',FatHReg,'filteredmass:filteredpt/F')
            Event = array('f',[0])
            METet = array('f',[0])
            rho = array('f',[0])
            METphi = array('f',[0])
            frho = ROOT.TTreeFormula("rho",'rho',tree)
            fEvent = ROOT.TTreeFormula("Event",'evt',tree)
            fFatHFlag = ROOT.TTreeFormula("FatHFlag",'nFatjetCA15trimmed>0',tree)
            fFatHnFilterJets = ROOT.TTreeFormula("FatHnFilterJets",'nFatjetCA15ungroomed',tree)
            fMETet = ROOT.TTreeFormula("METet",'met_pt',tree)
            fMETphi = ROOT.TTreeFormula("METphi",'met_phi',tree)
            # fHVMass = ROOT.TTreeFormula("HVMass",'VHbb::HV_mass(H_pt,H_eta,H_phi,H_mass,V_pt,V_eta,V_phi,V_mass)',tree)
            hJet_MtArray = [array('f',[0]),array('f',[0])]
            hJet_etarray = [array('f',[0]),array('f',[0])]
            hJet_MET_dPhi = array('f',[0]*2)
            hJet_regWeight = array('f',[0]*2)
            fathFilterJets_regWeight = array('f',[0]*2)
            hJet_MET_dPhiArray = [array('f',[0]),array('f',[0])]
            hJet_rawPtArray = [array('f',[0]),array('f',[0])]
            newtree.Branch('hJet_MET_dPhi',hJet_MET_dPhi,'hJet_MET_dPhi[2]/F')
            newtree.Branch('hJet_regWeight',hJet_regWeight,'hJet_regWeight[2]/F')
            readerJet0 = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet1 = ROOT.TMVA.Reader("!Color:!Silent" )

            readerJet0_JER_up = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet1_JER_up = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet0_JER_down = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet1_JER_down = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet0_JEC_up = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet1_JEC_up = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet0_JEC_down = ROOT.TMVA.Reader("!Color:!Silent" )
            readerJet1_JEC_down = ROOT.TMVA.Reader("!Color:!Silent" )

            theForms = {}
            theVars0 = {}
            theVars1 = {}
            theVars0_JER_up = {}
            theVars1_JER_up = {}
            theVars0_JER_down = {}
            theVars1_JER_down = {}
            theVars0_JEC_up = {}
            theVars1_JEC_up = {}
            theVars0_JEC_down = {}
            theVars1_JEC_down = {}

        def addVarsToReader(reader,regDict,regVars,theVars,theForms,i,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,syst=""):
            # print "regDict: ",regDict
            # print "regVars: ",regVars
            for key in regVars:
                var = regDict[key]
                theVars[key+syst] = array( 'f', [ 0 ] )
                reader.AddVariable(key,theVars[key+syst])
                formulaX = var
                brakets = ""
                if formulaX.find("[hJCidx[0]]"): brakets = "[hJCidx[0]]"
                elif formulaX.find("[hJCidx[1]]"): brakets = "[hJCidx[1]]"
                elif formulaX.find("[0]"): brakets = "[0]"
                elif formulaX.find("[1]"): brakets = "[1]"
                else: pass

                formulaX = formulaX.replace(brakets,"[X]")

                if syst == "":
                    pass
                    # formulaX = formulaX.replace("Jet_pt[X]","Jet_rawPt[X]*Jet_corr[X]*Jet_corr_JER[X]")
                elif syst == "JER_up":
                    formulaX = formulaX.replace("Jet_pt[X]","Jet_rawPt[X]*Jet_corr[X]*Jet_corr_JERUp[X]")
                elif syst == "JER_down":
                    formulaX = formulaX.replace("Jet_pt[X]","Jet_rawPt[X]*Jet_corr[X]*Jet_corr_JERDown[X]")
                elif syst == "JEC_up":
                    formulaX = formulaX.replace("Jet_pt[X]","Jet_rawPt[X]*Jet_corr_JECUp[X]*Jet_corr_JER[X]")
                elif syst == "JEC_down":
                    formulaX = formulaX.replace("Jet_pt[X]","Jet_rawPt[X]*Jet_corr_JECDown[X]*Jet_corr_JER[X]")
                else:
                    raise Exception(syst," is unknown!")

                formula = formulaX.replace("[X]",brakets)
                formula = formula.replace("[0]","[%.0f]" %i)
                theForms['form_reg_%s_%.0f'%(key+syst,i)] = ROOT.TTreeFormula("form_reg_%s_%.0f"%(key+syst,i),'%s' %(formula),tree)
            return

        if applyRegression == True:
            addVarsToReader(readerJet0,regDict,regVars,theVars0,theForms,0,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray)
            addVarsToReader(readerJet1,regDict,regVars,theVars1,theForms,1,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray)
            if job.type != 'DATA':
                addVarsToReader(readerJet0_JER_up,regDict,regVars,theVars0,theForms,0,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JER_up")
                addVarsToReader(readerJet1_JER_up,regDict,regVars,theVars1,theForms,1,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JER_up")
                addVarsToReader(readerJet0_JER_down,regDict,regVars,theVars0,theForms,0,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JER_down")
                addVarsToReader(readerJet1_JER_down,regDict,regVars,theVars1,theForms,1,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JER_down")
                addVarsToReader(readerJet0_JEC_up,regDict,regVars,theVars0,theForms,0,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JEC_up")
                addVarsToReader(readerJet1_JEC_up,regDict,regVars,theVars1,theForms,1,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JEC_up")
                addVarsToReader(readerJet0_JEC_down,regDict,regVars,theVars0,theForms,0,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JEC_down")
                addVarsToReader(readerJet1_JEC_down,regDict,regVars,theVars1,theForms,1,hJet_MET_dPhiArray,METet,rho,hJet_MtArray,hJet_etarray,hJet_rawPtArray,"JEC_down")

            readerJet0.BookMVA( "jet0Regression", regWeight )
            readerJet1.BookMVA( "jet1Regression", regWeight )

            if job.type != 'DATA':
                readerJet0_JER_up.BookMVA( "jet0Regression", regWeight )
                readerJet1_JER_up.BookMVA( "jet1Regression", regWeight )
                readerJet0_JER_down.BookMVA( "jet0Regression", regWeight )
                readerJet1_JER_down.BookMVA( "jet1Regression", regWeight )

                readerJet0_JEC_up.BookMVA( "jet0Regression", regWeight )
                readerJet1_JEC_up.BookMVA( "jet1Regression", regWeight )
                readerJet0_JEC_down.BookMVA( "jet0Regression", regWeight )
                readerJet1_JEC_down.BookMVA( "jet1Regression", regWeight )


        # Add training Flag
        EventForTraining = array('i',[0])
        newtree.Branch('EventForTraining',EventForTraining,'EventForTraining/I')
        EventForTraining[0]=0

        TFlag=ROOT.TTreeFormula("EventForTraining","evt%2",tree)

        # Add bTag weights
        if applyBTagweights:
            bTagWeight_RunEF = array('f',[0])
            bTagWeightJESUp_RunEF = array('f',[0])
            bTagWeightJESDown_RunEF = array('f',[0])
            bTagWeightLFUp_RunEF = array('f',[0])
            bTagWeightLFDown_RunEF = array('f',[0])
            bTagWeightHFUp_RunEF = array('f',[0])
            bTagWeightHFDown_RunEF = array('f',[0])
            bTagWeightLFStats1Up_RunEF = array('f',[0])
            bTagWeightLFStats1Down_RunEF = array('f',[0])
            bTagWeightLFStats2Up_RunEF = array('f',[0])
            bTagWeightLFStats2Down_RunEF = array('f',[0])
            bTagWeightHFStats1Up_RunEF = array('f',[0])
            bTagWeightHFStats1Down_RunEF = array('f',[0])
            bTagWeightHFStats2Up_RunEF = array('f',[0])
            bTagWeightHFStats2Down_RunEF = array('f',[0])
            bTagWeightcErr1Up_RunEF = array('f',[0])
            bTagWeightcErr1Down_RunEF = array('f',[0])
            bTagWeightcErr2Up_RunEF = array('f',[0])
            bTagWeightcErr2Down_RunEF = array('f',[0])


            bTagWeight_RunEF[0] = 1
            bTagWeightJESUp_RunEF[0] = 1
            bTagWeightJESDown_RunEF[0] = 1
            bTagWeightLFUp_RunEF[0] = 1
            bTagWeightLFDown_RunEF[0] = 1
            bTagWeightHFUp_RunEF[0] = 1
            bTagWeightHFDown_RunEF[0] = 1
            bTagWeightLFStats1Up_RunEF[0] = 1
            bTagWeightLFStats1Down_RunEF[0] = 1
            bTagWeightLFStats2Up_RunEF[0] = 1
            bTagWeightLFStats2Down_RunEF[0] = 1
            bTagWeightHFStats1Up_RunEF[0] = 1
            bTagWeightHFStats1Down_RunEF[0] = 1
            bTagWeightHFStats2Up_RunEF[0] = 1
            bTagWeightHFStats2Down_RunEF[0] = 1
            bTagWeightcErr1Up_RunEF[0] = 1
            bTagWeightcErr1Down_RunEF[0] = 1
            bTagWeightcErr2Up_RunEF[0] = 1
            bTagWeightcErr2Down_RunEF[0] = 1

            newtree.Branch('bTagWeight_RunEF',bTagWeight_RunEF,'bTagWeight_RunEF/F')
            newtree.Branch('bTagWeightJESUp_RunEF',bTagWeightJESUp_RunEF,'bTagWeightJESUp_RunEF/F')
            newtree.Branch('bTagWeightJESDown_RunEF',bTagWeightJESDown_RunEF,'bTagWeightJESDown_RunEF/F')
            newtree.Branch('bTagWeightLFUp_RunEF',bTagWeightLFUp_RunEF,'bTagWeightLFUp_RunEF/F')
            newtree.Branch('bTagWeightLFDown_RunEF',bTagWeightLFDown_RunEF,'bTagWeightLFDown_RunEF/F')
            newtree.Branch('bTagWeightHFUp_RunEF',bTagWeightHFUp_RunEF,'bTagWeightHFUp_RunEF/F')
            newtree.Branch('bTagWeightHFDown_RunEF',bTagWeightHFDown_RunEF,'bTagWeightHFDown_RunEF/F')
            newtree.Branch('bTagWeightLFStats1Up_RunEF',bTagWeightLFStats1Up_RunEF,'bTagWeightLFStats1Up_RunEF/F')
            newtree.Branch('bTagWeightLFStats1Down_RunEF',bTagWeightLFStats1Down_RunEF,'bTagWeightLFStats1Down_RunEF/F')
            newtree.Branch('bTagWeightLFStats2Up_RunEF',bTagWeightLFStats2Up_RunEF,'bTagWeightLFStats2Up_RunEF/F')
            newtree.Branch('bTagWeightLFStats2Down_RunEF',bTagWeightLFStats2Down_RunEF,'bTagWeightLFStats2Down_RunEF/F')
            newtree.Branch('bTagWeightHFStats1Up_RunEF',bTagWeightHFStats1Up_RunEF,'bTagWeightHFStats1Up_RunEF/F')
            newtree.Branch('bTagWeightHFStats1Down_RunEF',bTagWeightHFStats1Down_RunEF,'bTagWeightHFStats1Down_RunEF/F')
            newtree.Branch('bTagWeightHFStats2Up_RunEF',bTagWeightHFStats2Up_RunEF,'bTagWeightHFStats2Up_RunEF/F')
            newtree.Branch('bTagWeightHFStats2Down_RunEF',bTagWeightHFStats2Down_RunEF,'bTagWeightHFStats2Down_RunEF/F')
            newtree.Branch('bTagWeightcErr1Up_RunEF',bTagWeightcErr1Up_RunEF,'bTagWeightcErr1Up_RunEF/F')
            newtree.Branch('bTagWeightcErr1Down_RunEF',bTagWeightcErr1Down_RunEF,'bTagWeightcErr1Down_RunEF/F')
            newtree.Branch('bTagWeightcErr2Up_RunEF',bTagWeightcErr2Up_RunEF,'bTagWeightcErr2Up_RunEF/F')
            newtree.Branch('bTagWeightcErr2Down_RunEF',bTagWeightcErr2Down_RunEF,'bTagWeightcErr2Down_RunEF/F')

        #Other btag stuff
        if job.type != 'DATA':

            # ===== btag weight branches =====
            btag_weight_JECUp_high       = array('f',[0]*1)
            btag_weight_JECUp_low        = array('f',[0]*1)
            btag_weight_JECUp_central    = array('f',[0]*1)
            btag_weight_JECUp_forward    = array('f',[0]*1)

            btag_weight_JECDown_high     = array('f',[0]*1)
            btag_weight_JECDown_low      = array('f',[0]*1)
            btag_weight_JECDown_central  = array('f',[0]*1)
            btag_weight_JECDown_forward  = array('f',[0]*1)

            btag_weight_lfUp_high     = array('f',[0]*1)
            btag_weight_lfUp_low      = array('f',[0]*1)
            btag_weight_lfUp_central  = array('f',[0]*1)
            btag_weight_lfUp_forward  = array('f',[0]*1)

            btag_weight_lfDown_high     = array('f',[0]*1)
            btag_weight_lfDown_low      = array('f',[0]*1)
            btag_weight_lfDown_central  = array('f',[0]*1)
            btag_weight_lfDown_forward  = array('f',[0]*1)

            btag_weight_hfUp_high     = array('f',[0]*1)
            btag_weight_hfUp_low      = array('f',[0]*1)
            btag_weight_hfUp_central  = array('f',[0]*1)
            btag_weight_hfUp_forward  = array('f',[0]*1)

            btag_weight_hfDown_high     = array('f',[0]*1)
            btag_weight_hfDown_low      = array('f',[0]*1)
            btag_weight_hfDown_central  = array('f',[0]*1)
            btag_weight_hfDown_forward  = array('f',[0]*1)

            btag_weight_lfstats1Up_high     = array('f',[0]*1)
            btag_weight_lfstats1Up_low      = array('f',[0]*1)
            btag_weight_lfstats1Up_central  = array('f',[0]*1)
            btag_weight_lfstats1Up_forward  = array('f',[0]*1)

            btag_weight_lfstats1Down_high     = array('f',[0]*1)
            btag_weight_lfstats1Down_low      = array('f',[0]*1)
            btag_weight_lfstats1Down_central  = array('f',[0]*1)
            btag_weight_lfstats1Down_forward  = array('f',[0]*1)

            btag_weight_lfstats2Up_high   = array('f',[0]*1)
            btag_weight_lfstats2Up_low      = array('f',[0]*1)
            btag_weight_lfstats2Up_central  = array('f',[0]*1)
            btag_weight_lfstats2Up_forward  = array('f',[0]*1)

            btag_weight_lfstats2Down_high     = array('f',[0]*1)
            btag_weight_lfstats2Down_low      = array('f',[0]*1)
            btag_weight_lfstats2Down_central  = array('f',[0]*1)
            btag_weight_lfstats2Down_forward  = array('f',[0]*1)

            btag_weight_hfstats1Up_high   = array('f',[0]*1)
            btag_weight_hfstats1Up_low      = array('f',[0]*1)
            btag_weight_hfstats1Up_central  = array('f',[0]*1)
            btag_weight_hfstats1Up_forward  = array('f',[0]*1)

            btag_weight_hfstats1Down_high = array('f',[0]*1)
            btag_weight_hfstats1Down_low      = array('f',[0]*1)
            btag_weight_hfstats1Down_central  = array('f',[0]*1)
            btag_weight_hfstats1Down_forward  = array('f',[0]*1)

            btag_weight_hfstats2Up_high    = array('f',[0]*1)
            btag_weight_hfstats2Up_low      = array('f',[0]*1)
            btag_weight_hfstats2Up_central  = array('f',[0]*1)
            btag_weight_hfstats2Up_forward  = array('f',[0]*1)

            btag_weight_hfstats2Down_high  = array('f',[0]*1)
            btag_weight_hfstats2Down_low      = array('f',[0]*1)
            btag_weight_hfstats2Down_central  = array('f',[0]*1)
            btag_weight_hfstats2Down_forward  = array('f',[0]*1)

            btag_weight_cferr1Up_high      = array('f',[0]*1)
            btag_weight_cferr1Up_low      = array('f',[0]*1)
            btag_weight_cferr1Up_central  = array('f',[0]*1)
            btag_weight_cferr1Up_forward  = array('f',[0]*1)

            btag_weight_cferr1Down_high    = array('f',[0]*1)
            btag_weight_cferr1Down_low      = array('f',[0]*1)
            btag_weight_cferr1Down_central  = array('f',[0]*1)
            btag_weight_cferr1Down_forward  = array('f',[0]*1)

            btag_weight_cferr2Up_high      = array('f',[0]*1)
            btag_weight_cferr2Up_low      = array('f',[0]*1)
            btag_weight_cferr2Up_central  = array('f',[0]*1)
            btag_weight_cferr2Up_forward  = array('f',[0]*1)

            btag_weight_cferr2Down_high    = array('f',[0]*1)
            btag_weight_cferr2Down_low      = array('f',[0]*1)
            btag_weight_cferr2Down_central  = array('f',[0]*1)
            btag_weight_cferr2Down_forward  = array('f',[0]*1)

            newtree.Branch('btag_weight_JECUp_high', btag_weight_JECUp_high, 'btag_weight_JECUp_high[1]/F')
            newtree.Branch('btag_weight_JECUp_low', btag_weight_JECUp_low, 'btag_weight_JECUp_low[1]/F')
            newtree.Branch('btag_weight_JECUp_central', btag_weight_JECUp_central, 'btag_weight_JECUp_central[1]/F')
            newtree.Branch('btag_weight_JECUp_forward', btag_weight_JECUp_forward, 'btag_weight_JECUp_forward[1]/F')

            newtree.Branch('btag_weight_JECDown_high', btag_weight_JECDown_high, 'btag_weight_JECDown_high[1]/F')
            newtree.Branch('btag_weight_JECDown_low', btag_weight_JECDown_low, 'btag_weight_JECDown_low[1]/F')
            newtree.Branch('btag_weight_JECDown_central', btag_weight_JECDown_central, 'btag_weight_JECDown_central[1]/F')
            newtree.Branch('btag_weight_JECDown_forward', btag_weight_JECDown_forward, 'btag_weight_JECDown_forward[1]/F')

            newtree.Branch('btag_weight_lfUp_high', btag_weight_lfUp_high, 'btag_weight_lfUp_high[1]/F')
            newtree.Branch('btag_weight_lfUp_low', btag_weight_lfUp_low, 'btag_weight_lfUp_low[1]/F')
            newtree.Branch('btag_weight_lfUp_central', btag_weight_lfUp_central, 'btag_weight_lfUp_central[1]/F')
            newtree.Branch('btag_weight_lfUp_forward', btag_weight_lfUp_forward, 'btag_weight_lfUp_forward[1]/F')

            newtree.Branch('btag_weight_lfDown_high', btag_weight_lfDown_high, 'btag_weight_lfDown_high[1]/F')
            newtree.Branch('btag_weight_lfDown_low', btag_weight_lfDown_low, 'btag_weight_lfDown_low[1]/F')
            newtree.Branch('btag_weight_lfDown_central', btag_weight_lfDown_central, 'btag_weight_lfDown_central[1]/F')
            newtree.Branch('btag_weight_lfDown_forward', btag_weight_lfDown_forward, 'btag_weight_lfDown_forward[1]/F')

            newtree.Branch('btag_weight_hfUp_high', btag_weight_hfUp_high, 'btag_weight_hfUp_high[1]/F')
            newtree.Branch('btag_weight_hfUp_low', btag_weight_hfUp_low, 'btag_weight_hfUp_low[1]/F')
            newtree.Branch('btag_weight_hfUp_central', btag_weight_hfUp_central, 'btag_weight_hfUp_central[1]/F')
            newtree.Branch('btag_weight_hfUp_forward', btag_weight_hfUp_forward, 'btag_weight_hfUp_forward[1]/F')

            newtree.Branch('btag_weight_hfDown_high', btag_weight_hfDown_high, 'btag_weight_hfDown_high[1]/F')
            newtree.Branch('btag_weight_hfDown_low', btag_weight_hfDown_low, 'btag_weight_hfDown_low[1]/F')
            newtree.Branch('btag_weight_hfDown_central', btag_weight_hfDown_central, 'btag_weight_hfDown_central[1]/F')
            newtree.Branch('btag_weight_hfDown_forward', btag_weight_hfDown_forward, 'btag_weight_hfDown_forward[1]/F')

            newtree.Branch('btag_weight_lfstats1Up_high', btag_weight_lfstats1Up_high, 'btag_weight_lfstats1Up_high[1]/F')
            newtree.Branch('btag_weight_lfstats1Up_low', btag_weight_lfstats1Up_low, 'btag_weight_lfstats1Up_low[1]/F')
            newtree.Branch('btag_weight_lfstats1Up_central', btag_weight_lfstats1Up_central, 'btag_weight_lfstats1Up_central[1]/F')
            newtree.Branch('btag_weight_lfstats1Up_forward', btag_weight_lfstats1Up_forward, 'btag_weight_lfstats1Up_forward[1]/F')

            newtree.Branch('btag_weight_lfstats1Down_high', btag_weight_lfstats1Down_high, 'btag_weight_lfstats1Down_high[1]/F')
            newtree.Branch('btag_weight_lfstats1Down_low', btag_weight_lfstats1Down_low, 'btag_weight_lfstats1Down_low[1]/F')
            newtree.Branch('btag_weight_lfstats1Down_central', btag_weight_lfstats1Down_central, 'btag_weight_lfstats1Down_central[1]/F')
            newtree.Branch('btag_weight_lfstats1Down_forward', btag_weight_lfstats1Down_forward, 'btag_weight_lfstats1Down_forward[1]/F')

            newtree.Branch('btag_weight_lfstats2Up_high', btag_weight_lfstats2Up_high, 'btag_weight_lfstats2Up_high[1]/F')
            newtree.Branch('btag_weight_lfstats2Up_low', btag_weight_lfstats2Up_low, 'btag_weight_lfstats2Up_low[1]/F')
            newtree.Branch('btag_weight_lfstats2Up_central', btag_weight_lfstats2Up_central, 'btag_weight_lfstats2Up_central[1]/F')
            newtree.Branch('btag_weight_lfstats2Up_forward', btag_weight_lfstats2Up_forward, 'btag_weight_lfstats2Up_forward[1]/F')

            newtree.Branch('btag_weight_lfstats2Down_high', btag_weight_lfstats2Down_high, 'btag_weight_lfstats2Down_high[1]/F')
            newtree.Branch('btag_weight_lfstats2Down_low', btag_weight_lfstats2Down_low, 'btag_weight_lfstats2Down_low[1]/F')
            newtree.Branch('btag_weight_lfstats2Down_central', btag_weight_lfstats2Down_central, 'btag_weight_lfstats2Down_central[1]/F')
            newtree.Branch('btag_weight_lfstats2Down_forward', btag_weight_lfstats2Down_forward, 'btag_weight_lfstats2Down_forward[1]/F')

            newtree.Branch('btag_weight_hfstats1Up_high', btag_weight_hfstats1Up_high, 'btag_weight_hfstats1Up_high[1]/F')
            newtree.Branch('btag_weight_hfstats1Up_low', btag_weight_hfstats1Up_low, 'btag_weight_hfstats1Up_low[1]/F')
            newtree.Branch('btag_weight_hfstats1Up_central', btag_weight_hfstats1Up_central, 'btag_weight_hfstats1Up_central[1]/F')
            newtree.Branch('btag_weight_hfstats1Up_forward', btag_weight_hfstats1Up_forward, 'btag_weight_hfstats1Up_forward[1]/F')

            newtree.Branch('btag_weight_hfstats1Down_high', btag_weight_hfstats1Down_high, 'btag_weight_hfstats1Down_high[1]/F')
            newtree.Branch('btag_weight_hfstats1Down_low', btag_weight_hfstats1Down_low, 'btag_weight_hfstats1Down_low[1]/F')
            newtree.Branch('btag_weight_hfstats1Down_central', btag_weight_hfstats1Down_central, 'btag_weight_hfstats1Down_central[1]/F')
            newtree.Branch('btag_weight_hfstats1Down_forward', btag_weight_hfstats1Down_forward, 'btag_weight_hfstats1Down_forward[1]/F')

            newtree.Branch('btag_weight_hfstats2Up_high', btag_weight_hfstats2Up_high, 'btag_weight_hfstats2Up_high[1]/F')
            newtree.Branch('btag_weight_hfstats2Up_low', btag_weight_hfstats2Up_low, 'btag_weight_hfstats2Up_low[1]/F')
            newtree.Branch('btag_weight_hfstats2Up_central', btag_weight_hfstats2Up_central, 'btag_weight_hfstats2Up_central[1]/F')
            newtree.Branch('btag_weight_hfstats2Up_forward', btag_weight_hfstats2Up_forward, 'btag_weight_hfstats2Up_forward[1]/F')

            newtree.Branch('btag_weight_hfstats2Down_high', btag_weight_hfstats2Down_high, 'btag_weight_hfstats2Down_high[1]/F')
            newtree.Branch('btag_weight_hfstats2Down_low', btag_weight_hfstats2Down_low, 'btag_weight_hfstats2Down_low[1]/F')
            newtree.Branch('btag_weight_hfstats2Down_central', btag_weight_hfstats2Down_central, 'btag_weight_hfstats2Down_central[1]/F')
            newtree.Branch('btag_weight_hfstats2Down_forward', btag_weight_hfstats2Down_forward, 'btag_weight_hfstats2Down_forward[1]/F')

            newtree.Branch('btag_weight_cferr1Up_high', btag_weight_cferr1Up_high, 'btag_weight_cferr1Up_high[1]/F')
            newtree.Branch('btag_weight_cferr1Up_low', btag_weight_cferr1Up_low, 'btag_weight_cferr1Up_low[1]/F')
            newtree.Branch('btag_weight_cferr1Up_central', btag_weight_cferr1Up_central, 'btag_weight_cferr1Up_central[1]/F')
            newtree.Branch('btag_weight_cferr1Up_forward', btag_weight_cferr1Up_forward, 'btag_weight_cferr1Up_forward[1]/F')

            newtree.Branch('btag_weight_cferr1Down_high', btag_weight_cferr1Down_high, 'btag_weight_cferr1Down_high[1]/F')
            newtree.Branch('btag_weight_cferr1Down_low', btag_weight_cferr1Down_low, 'btag_weight_cferr1Down_low[1]/F')
            newtree.Branch('btag_weight_cferr1Down_central', btag_weight_cferr1Down_central, 'btag_weight_cferr1Down_central[1]/F')
            newtree.Branch('btag_weight_cferr1Down_forward', btag_weight_cferr1Down_forward, 'btag_weight_cferr1Down_forward[1]/F')

            newtree.Branch('btag_weight_cferr2Up_high', btag_weight_cferr2Up_high, 'btag_weight_cferr2Up_high[1]/F')
            newtree.Branch('btag_weight_cferr2Up_low', btag_weight_cferr2Up_low, 'btag_weight_cferr2Up_low[1]/F')
            newtree.Branch('btag_weight_cferr2Up_central', btag_weight_cferr2Up_central, 'btag_weight_cferr2Up_central[1]/F')
            newtree.Branch('btag_weight_cferr2Up_forward', btag_weight_cferr2Up_forward, 'btag_weight_cferr2Up_forward[1]/F')

            newtree.Branch('btag_weight_cferr2Down_high', btag_weight_cferr2Down_high, 'btag_weight_cferr2Down_high[1]/F')
            newtree.Branch('btag_weight_cferr2Down_low', btag_weight_cferr2Down_low, 'btag_weight_cferr2Down_low[1]/F')
            newtree.Branch('btag_weight_cferr2Down_central', btag_weight_cferr2Down_central, 'btag_weight_cferr2Down_central[1]/F')
            newtree.Branch('btag_weight_cferr2Down_forward', btag_weight_cferr2Down_forward, 'btag_weight_cferr2Down_forward[1]/F')

          # Add new JER/JEC SYS branches for high/low and central/forward regions

            #Do loop here to define all the variables
            VarList = ['HCSV_reg_corrSYSUD_mass_CAT','HCSV_reg_corrSYSUD_pt_CAT', 'HCSV_reg_corrSYSUD_phi_CAT', 'HCSV_reg_corrSYSUD_eta_CAT','Jet_pt_reg_corrSYSUD_CAT']
            SysList = ['JER','JEC']
            UDList = ['Up','Down']
            #CatList = ['low','high','central','forward']
            CatList = ['low_central','low_forward','high_central','high_forward']
            SysDicList = []

            #ConditionDic = {'low':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and (tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]]<100. or tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]]<100.)',\
            #                'high':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and (tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]]>100. or tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]]>100.)',\
            #                'central':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and (abs(tree.Jet_eta[tree.hJCidx[0]])<1.4 or abs(tree.Jet_eta[tree.hJCidx[1]])<1.4)',\
            #                'forward':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and (abs(tree.Jet_eta[tree.hJCidx[0]])>1.4 or abs(tree.Jet_eta[tree.hJCidx[1]])>1.4)'
            #        }
            ConditionDic = {'low_central':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and ((tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]]<100. and abs(tree.Jet_eta[tree.hJCidx[0]])<1.4) or (tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]]<100. and abs(tree.Jet_eta[tree.hJCidx[1]])<1.4))',\
                            'low_forward':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and ((tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]]<100. and abs(tree.Jet_eta[tree.hJCidx[0]])>1.4) or (tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]]<100. and abs(tree.Jet_eta[tree.hJCidx[1]])>1.4))',\
                            'high_central':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and ((tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]]>100. and abs(tree.Jet_eta[tree.hJCidx[0]])<1.4) or (tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]]>100. and abs(tree.Jet_eta[tree.hJCidx[1]])<1.4))',\
                            'high_forward':'len(tree.hJCidx)==2 and tree.Jet_corr_SYSUD[tree.hJCidx[0]]>0. and tree.Jet_corr_SYSUD[tree.hJCidx[1]]>0. and ((tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]]>100. and abs(tree.Jet_eta[tree.hJCidx[0]])>1.4) or (tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]]>100. and abs(tree.Jet_eta[tree.hJCidx[1]])>1.4))'
                    }
            #JetConditionDic = {'low':'tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[INDEX]]<100.',\
            #                   'high':'tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[INDEX]]>100.',\
            #                   'central':'abs(tree.Jet_eta[tree.hJCidx[INDEX]])<1.4',\
            #                   'forward':'abs(tree.Jet_eta[tree.hJCidx[INDEX]])>1.4'
            #        }
            JetConditionDic = {'low_central':'tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[INDEX]]<100. and abs(tree.Jet_eta[tree.hJCidx[INDEX]])<1.4',\
                               'low_forward':'tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[INDEX]]<100. and abs(tree.Jet_eta[tree.hJCidx[INDEX]])>1.4',\
                               'high_central':'tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[INDEX]]>100. and abs(tree.Jet_eta[tree.hJCidx[INDEX]])<1.4',\
                               'high_forward':'tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[INDEX]]>100. and abs(tree.Jet_eta[tree.hJCidx[INDEX]])>1.4'
                    }
            DefaultVar = {'HCSV_reg_corrSYSUD_mass_CAT':'tree.HCSV_reg_mass','HCSV_reg_corrSYSUD_pt_CAT':'tree.HCSV_reg_pt','HCSV_reg_corrSYSUD_phi_CAT':'tree.HCSV_reg_phi','HCSV_reg_corrSYSUD_eta_CAT':'tree.HCSV_reg_eta','Jet_pt_reg_corrSYSUD_CAT':'tree.Jet_pt_reg[INDEX]'}
            SYSVar = {'HCSV_reg_corrSYSUD_mass_CAT':'tree.HCSV_reg_mass*(HJet_sys.M()/HJet.M())','HCSV_reg_corrSYSUD_pt_CAT':'tree.HCSV_reg_pt*(HJet_sys.Pt()/HJet.Pt())','HCSV_reg_corrSYSUD_phi_CAT':'tree.HCSV_reg_phi*(HJet_sys.Phi()/HJet.Phi())','HCSV_reg_corrSYSUD_eta_CAT':'tree.HCSV_reg_eta*(HJet_sys.Eta()/HJet.Eta())','Jet_pt_reg_corrSYSUD_CAT':'tree.Jet_pt_reg_corrSYSUD[INDEX]'}

            #Make a dic corresponding to each sys and create the variables
            for var in VarList:
                for syst in SysList:
                    for cat in CatList:
                        for ud in UDList:
                            #fill Dic
                            SysDic = {}
                            SysDic['var'] = var
                            SysDic['sys'] = syst
                            SysDic['UD'] = ud
                            SysDic['cat'] = cat
                            SysDic['varname'] = var.replace('SYS',syst).replace('UD',ud).replace('CAT',cat)
                            #Define var
                            if var == 'Jet_pt_reg_corrSYSUD_CAT':
                                SysDic['varptr'] = array('f',21*[0])
                                newtree.Branch(SysDic['varname'],SysDic['varptr'],SysDic['varname']+'[21]/F')
                                SysDicList.append(SysDic)
                            else:
                                SysDic['varptr'] = array('f',[0])
                                newtree.Branch(SysDic['varname'],SysDic['varptr'],SysDic['varname']+'/F')
                                SysDicList.append(SysDic)


           # # Jet flag for low/high central/forward region
           # hJet_low     = array('f',[0]*2)
           # hJet_high    = array('f',[0]*2)
           # hJet_central = array('f',[0]*2)
           # hJet_forward = array('f',[0]*2)

           # newtree.Branch('hJet_low', hJet_low, 'hJet_low[2]/F')
           # newtree.Branch('hJet_high',hJet_high, 'hJet_high[2]/F')
           # newtree.Branch('hJet_central', hJet_central, 'hJet_central[2]/F')
           # newtree.Branch('hJet_forward', hJet_forward, 'hJet_forward[2]/F')

            #other variables:

        if channel == "Zmm":
        #Special weights

            DY_specialWeight= array('f',[0])
            DY_specialWeight[0] = 1
            newtree.Branch('DY_specialWeight',DY_specialWeight,'DY_specialWeight/F')


        #Add reg VHDphi
            HVdPhi_reg = array('f',[0])
            HVdPhi_reg[0] = 300
            newtree.Branch('HVdPhi_reg',HVdPhi_reg,'HVdPhi_reg/F')

        #Add CSV

            bTagWeight_ichep = array('f',[0])
            bTagWeight_ichep[0] = 1
            newtree.Branch('bTagWeight_ichep',bTagWeight_ichep,'bTagWeight_ichep/F')

        # Add  Lepton SF
            #Loose ISO+ID SF 
               #muon iso (wrong in the nutples)
            weight_SF_LooseISO = array('f',[0]*3)
            weight_SF_LooseISO[0], weight_SF_LooseISO[1], weight_SF_LooseISO[2] = 1,1,1
            newtree.Branch('weight_SF_LooseISO',weight_SF_LooseISO,'weight_SF_LooseISO[3]/F')
               #electron MVAID (wrong in the ntuples)
            weight_SF_LooseMVAID_BCD = array('f',[0]*3)
            weight_SF_LooseMVAID_BCD[0], weight_SF_LooseMVAID_BCD[1], weight_SF_LooseMVAID_BCD[2] = 1,1,1
            newtree.Branch('weight_SF_LooseMVAID_BCD',weight_SF_LooseMVAID_BCD,'weight_SF_LooseMVAID_BCD[3]/F')
               #
            weight_SF_LooseMVAID_BCDEF = array('f',[0]*3)
            weight_SF_LooseMVAID_BCDEF[0], weight_SF_LooseMVAID_BCDEF[1], weight_SF_LooseMVAID_BCDEF[2] = 1,1,1
            newtree.Branch('weight_SF_LooseMVAID_BCDEF',weight_SF_LooseMVAID_BCDEF,'weight_SF_LooseMVAID_BCDEF[3]/F')
            #Lepton trigger
               #electron
            weight_Eff_eletriglooseBCD = array('f',[0]*3)
            weight_Eff_eletriglooseBCD[0], weight_Eff_eletriglooseBCD[1], weight_Eff_eletriglooseBCD[2] = 1,1,1
            newtree.Branch('weight_Eff_eletriglooseBCD',weight_Eff_eletriglooseBCD,'weight_Eff_eletriglooseBCD[3]/F')
            weight_Eff_eletriglooseBCDEF = array('f',[0]*3)
            weight_Eff_eletriglooseBCDEF[0], weight_Eff_eletriglooseBCDEF[1], weight_Eff_eletriglooseBCDEF[2] = 1,1,1
            newtree.Branch('weight_Eff_eletriglooseBCDEF',weight_Eff_eletriglooseBCDEF,'weight_Eff_eletriglooseBCDEF[3]/F')
               #pt23
            weight_Eff_eletrigloosept23 = array('f',[0]*3)
            weight_Eff_eletrigloosept23[0], weight_Eff_eletrigloosept23[1], weight_Eff_eletrigloosept23[2] = 1,1,1
            newtree.Branch('weight_Eff_eletrigloosept23',weight_Eff_eletrigloosept23,'weight_Eff_eletrigloosept23[3]/F')
               #muon
               #for ICHEP dataset
            weight_Eff_mutriglooseICHEP = array('f',[0]*3)
            weight_Eff_mutriglooseICHEP[0], weight_Eff_mutriglooseICHEP[1], weight_Eff_mutriglooseICHEP[2]= 1,1,1
            newtree.Branch('weight_Eff_mutriglooseICHEP',weight_Eff_mutriglooseICHEP,'weight_Eff_mutriglooseICHEP[3]/F')
               #for full 22/fb dataset
            weight_Eff_mutrigloose = array('f',[0]*3)
            weight_Eff_mutrigloose[0], weight_Eff_mutrigloose[1], weight_Eff_mutrigloose[2] = 1,1,1
            newtree.Branch('weight_Eff_mutrigloose',weight_Eff_mutrigloose,'weight_Eff_mutrigloose[3]/F')
               #Trk:
                  #electron
            weight_trk_electron = array('f',[0]*3)
            weight_trk_electron[0], weight_trk_electron[1], weight_trk_electron[2] = 1,1,1
            newtree.Branch('weight_trk_electron',weight_trk_electron,'weight_trk_electron[3]/F')
               #final weight (without triggers):
            muweight = array('f',[0]*3)
            muweight[0], muweight[1], muweight[2] = 1,1,1
            newtree.Branch('muweight',muweight,'muweight[3]/F')
            eleweight= array('f',[0]*3)
            eleweight[0], eleweight[1], eleweight[2] = 1,1,1
            newtree.Branch('eleweight',eleweight,'eleweight[3]/F')

        # Angular Likelihood
        if channel == "Znn" or channel == "Zmm":
            angleHB = array('f',[0])
            newtree.Branch('angleHB',angleHB,'angleHB/F')
            angleLZ = array('f',[0])
            newtree.Branch('angleLZ',angleLZ,'angleLZ/F')
            angleZZS = array('f',[0])
            newtree.Branch('angleZZS',angleZZS,'angleZZS/F')
            kinLikeRatio = array('f',[0]*len(AngLikeBkgs))
            newtree.Branch('kinLikeRatio',kinLikeRatio,'%s/F' %(':'.join(AngLikeBkgs)))
            fAngleHB = ROOT.TTreeFormula("fAngleHB",'abs(VHbb::ANGLEHB(Jet_pt[hJCidx[0]],Jet_eta[hJCidx[0]],Jet_phi[hJCidx[0]],Jet_mass[hJCidx[0]],Jet_pt[hJCidx[1]],Jet_eta[hJCidx[1]],Jet_phi[hJCidx[1]],Jet_mass[hJCidx[1]]))',newtree)
            fAngleLZ = ROOT.TTreeFormula("fAngleLZ",'abs(VHbb::ANGLELZ(vLeptons_pt[hJCidx[0]],vLeptons_eta[hJCidx[0]],vLeptons_phi[hJCidx[0]],vLeptons_mass[hJCidx[0]],vLeptons_pt[hJCidx[1]],vLeptons_eta[hJCidx[1]],vLeptons_phi[hJCidx[1]],vLeptons_mass[hJCidx[1]]))',newtree)
            fAngleZZS = ROOT.TTreeFormula("fAngleZZS",'abs(VHbb::ANGLELZ(H_pt,H_eta,H_phi,H_pt,V_pt,V_eta,V_phi,V_mass))',newtree)
            fVpt = ROOT.TTreeFormula("fVpt",'V_pt',tree)
            fVeta = ROOT.TTreeFormula("fVeta",'V_eta',tree)
            fVphi = ROOT.TTreeFormula("fVphi",'V_phi',tree)
            fVmass = ROOT.TTreeFormula("fVmass",'V_mass',tree)
            likeSBH = array('f',[0]*len(AngLikeBkgs))
            likeBBH = array('f',[0]*len(AngLikeBkgs))
            likeSLZ = array('f',[0]*len(AngLikeBkgs))
            likeBLZ = array('f',[0]*len(AngLikeBkgs))
            likeSZZS = array('f',[0]*len(AngLikeBkgs))
            likeBZZS = array('f',[0]*len(AngLikeBkgs))
            likeSMassZS = array('f',[0]*len(AngLikeBkgs))
            likeBMassZS = array('f',[0]*len(AngLikeBkgs))
            HVMass_Reg = array('f',[0])
            newtree.Branch('HVMass_Reg',HVMass_Reg,'HVMass_Reg/F')

            SigBH = []; BkgBH = []; SigLZ = []; BkgLZ = []; SigZZS = []; BkgZZS = []; SigMassZS = []; BkgMassZS = [];

        # if job.type != 'DATA': ##FIXME###
        if channel == "Znn" or channel == "Zmm":
            #CSV branches
            hJet_hadronFlavour = array('f',[0]*2)
            hJet_btagCSV = array('f',[0]*2)
            hJet_btagCSVOld = array('f',[0]*2)
            hJet_btagCSVUp = array('f',[0]*2)
            hJet_btagCSVDown = array('f',[0]*2)
            hJet_btagCSVFUp = array('f',[0]*2)
            hJet_btagCSVFDown = array('f',[0]*2)
            newtree.Branch('hJet_btagCSV',hJet_btagCSV,'hJet_btagCSV[2]/F')
            newtree.Branch('hJet_btagCSVOld',hJet_btagCSVOld,'hJet_btagCSVOld[2]/F')
            newtree.Branch('hJet_btagCSVUp',hJet_btagCSVUp,'hJet_btagCSVUp[2]/F')
            newtree.Branch('hJet_btagCSVDown',hJet_btagCSVDown,'hJet_btagCSVDown[2]/F')
            newtree.Branch('hJet_btagCSVFUp',hJet_btagCSVFUp,'hJet_btagCSVFUp[2]/F')
            newtree.Branch('hJet_btagCSVFDown',hJet_btagCSVFDown,'hJet_btagCSVFDown[2]/F')

            # Jet in bad (eta,phi) [for fake-MET]
            Jet_under = array('f',[0]*50)
            newtree.Branch('Jet_under',Jet_under,'Jet_under[nJet]/F')
            Jet_over = array('f',[0]*50)
            newtree.Branch('Jet_over',Jet_over,'Jet_over[nJet]/F')
            Jet_underMC = array('f',[0]*50)
            newtree.Branch('Jet_underMC',Jet_underMC,'Jet_underMC[nJet]/F')
            Jet_overMC = array('f',[0]*50)
            newtree.Branch('Jet_overMC',Jet_overMC,'Jet_overMC[nJet]/F')
            Jet_bad = array('f',[0]*50)
            newtree.Branch('Jet_bad',Jet_bad,'Jet_bad[nJet]/F')

            if channel == "Znn" or channel == "Zmm":
                DiscardedJet_under = array('f',[0]*50)
                newtree.Branch('DiscardedJet_under',DiscardedJet_under,'DiscardedJet_under[nDiscardedJet]/F')
                DiscardedJet_over = array('f',[0]*50)
                newtree.Branch('DiscardedJet_over',DiscardedJet_over,'DiscardedJet_over[nDiscardedJet]/F')
                DiscardedJet_underMC = array('f',[0]*50)
                newtree.Branch('DiscardedJet_underMC',DiscardedJet_underMC,'DiscardedJet_underMC[nDiscardedJet]/F')
                DiscardedJet_overMC = array('f',[0]*50)
                newtree.Branch('DiscardedJet_overMC',DiscardedJet_overMC,'DiscardedJet_overMC[nDiscardedJet]/F')
                DiscardedJet_bad = array('f',[0]*50)
                newtree.Branch('DiscardedJet_bad',DiscardedJet_bad,'DiscardedJet_bad[nDiscardedJet]/F')

                aLeptons_under = array('f',[0]*50)
                newtree.Branch('aLeptons_under',aLeptons_under,'aLeptons_under[naLeptons]/F')
                aLeptons_over = array('f',[0]*50)
                newtree.Branch('aLeptons_over',aLeptons_over,'aLeptons_over[naLeptons]/F')
                aLeptons_underMC = array('f',[0]*50)
                newtree.Branch('aLeptons_underMC',aLeptons_underMC,'aLeptons_underMC[naLeptons]/F')
                aLeptons_overMC = array('f',[0]*50)
                newtree.Branch('aLeptons_overMC',aLeptons_overMC,'aLeptons_overMC[naLeptons]/F')
                aLeptons_bad = array('f',[0]*50)
                newtree.Branch('aLeptons_bad',aLeptons_bad,'aLeptons_bad[naLeptons]/F')

                vLeptons_under = array('f',[0]*50)
                newtree.Branch('vLeptons_under',vLeptons_under,'vLeptons_under[nvLeptons]/F')
                vLeptons_over = array('f',[0]*50)
                newtree.Branch('vLeptons_over',vLeptons_over,'vLeptons_over[nvLeptons]/F')
                vLeptons_underMC = array('f',[0]*50)
                newtree.Branch('vLeptons_underMC',vLeptons_underMC,'vLeptons_underMC[nvLeptons]/F')
                vLeptons_overMC = array('f',[0]*50)
                newtree.Branch('vLeptons_overMC',vLeptons_overMC,'vLeptons_overMC[nvLeptons]/F')
                vLeptons_bad = array('f',[0]*50)
                newtree.Branch('vLeptons_bad',vLeptons_bad,'vLeptons_bad[nvLeptons]/F')

            # JER branches
            if applyRegression == True:
                hJet_pt_JER_up = array('f',[0]*2)
                newtree.Branch('hJet_pt_JER_up',hJet_pt_JER_up,'hJet_pt_JER_up[2]/F')
                hJet_pt_JER_down = array('f',[0]*2)
                newtree.Branch('hJet_pt_JER_down',hJet_pt_JER_down,'hJet_pt_JER_down[2]/F')
                hJet_mass_JER_up = array('f',[0]*2)
                newtree.Branch('hJet_mass_JER_up',hJet_mass_JER_up,'hJet_mass_JER_up[2]/F')
                hJet_mass_JER_down = array('f',[0]*2)
                newtree.Branch('hJet_mass_JER_down',hJet_mass_JER_down,'hJet_mass_JER_down[2]/F')
                H_JER = array('f',[0]*4)
                newtree.Branch('H_JER',H_JER,'mass_up:mass_down:pt_up:pt_down/F')
                HVMass_JER_up = array('f',[0])
                HVMass_JER_down = array('f',[0])
                newtree.Branch('HVMass_JER_up',HVMass_JER_up,'HVMass_JER_up/F')
                newtree.Branch('HVMass_JER_down',HVMass_JER_down,'HVMass_JER_down/F')
                angleHB_JER_up = array('f',[0])
                angleHB_JER_down = array('f',[0])
                angleZZS_JER_up = array('f',[0])
                angleZZS_JER_down = array('f',[0])
                newtree.Branch('angleHB_JER_up',angleHB_JER_up,'angleHB_JER_up/F')
                newtree.Branch('angleHB_JER_down',angleHB_JER_down,'angleHB_JER_down/F')
                newtree.Branch('angleZZS_JER_up',angleZZS_JER_up,'angleZZS_JER_up/F')
                newtree.Branch('angleZZS_JER_down',angleZZS_JER_down,'angleZZS_JER_down/F')

                hJet_ptOld = array('f',[0]*2)
                newtree.Branch('hJet_ptOld',hJet_ptOld,'hJet_ptOld[2]/F')

                hJet_pt = array('f',[0]*2)
                newtree.Branch('hJet_pt',hJet_pt,'hJet_pt[2]/F')

                hJet_ptMc = array('f',[0]*2)
                newtree.Branch('hJet_ptMc',hJet_ptMc,'hJet_ptMc[2]/F')

                hJet_mass = array('f',[0]*2)
                newtree.Branch('hJet_mass',hJet_mass,'hJet_mass[2]/F')

                hJet_eta = array('f',[0]*2)
                newtree.Branch('hJet_eta',hJet_eta,'hJet_eta[2]/F')

                hJet_phi = array('f',[0]*2)
                newtree.Branch('hJet_phi',hJet_phi,'hJet_phi[2]/F')


                # JES branches
                hJet_pt_JES_up = array('f',[0]*2)
                newtree.Branch('hJet_pt_JES_up',hJet_pt_JES_up,'hJet_pt_JES_up[2]/F')
                hJet_pt_JES_down = array('f',[0]*2)
                newtree.Branch('hJet_pt_JES_down',hJet_pt_JES_down,'hJet_pt_JES_down[2]/F')
                hJet_mass_JES_up = array('f',[0]*2)
                newtree.Branch('hJet_mass_JES_up',hJet_mass_JES_up,'hJet_mass_JES_up[2]/F')
                hJet_mass_JES_down = array('f',[0]*2)
                newtree.Branch('hJet_mass_JES_down',hJet_mass_JES_down,'hJet_mass_JES_down[2]/F')
                H_JES = array('f',[0]*4)
                newtree.Branch('H_JES',H_JES,'mass_up:mass_down:pt_up:pt_down/F')
                HVMass_JES_up = array('f',[0])
                HVMass_JES_down = array('f',[0])
                newtree.Branch('HVMass_JES_up',HVMass_JES_up,'HVMass_JES_up/F')
                newtree.Branch('HVMass_JES_down',HVMass_JES_down,'HVMass_JES_down/F')
                angleHB_JES_up = array('f',[0])
                angleHB_JES_down = array('f',[0])
                angleZZS_JES_up = array('f',[0])
                angleZZS_JES_down = array('f',[0])
                newtree.Branch('angleHB_JES_up',angleHB_JES_up,'angleHB_JES_up/F')
                newtree.Branch('angleHB_JES_down',angleHB_JES_down,'angleHB_JES_down/F')
                newtree.Branch('angleZZS_JES_up',angleZZS_JES_up,'angleZZS_JES_up/F')
                newtree.Branch('angleZZS_JES_down',angleZZS_JES_down,'angleZZS_JES_down/F')
        
                #Formulas for syst in angular
                fAngleHB_JER_up = ROOT.TTreeFormula("fAngleHB_JER_up",'abs(VHbb::ANGLEHBWithM(hJet_pt_JER_up[0],Jet_eta[hJCidx[0]],Jet_phi[hJCidx[0]],hJet_mass_JER_up[0],hJet_pt_JER_up[1],Jet_eta[hJCidx[1]],Jet_phi[hJCidx[1]],hJet_mass_JER_up[1]))',newtree)
                fAngleHB_JER_down = ROOT.TTreeFormula("fAngleHB_JER_down",'abs(VHbb::ANGLEHBWithM(hJet_pt_JER_down[0],Jet_eta[hJCidx[0]],Jet_phi[hJCidx[0]],hJet_mass_JER_down[0],hJet_pt_JER_down[1],Jet_eta[hJCidx[1]],Jet_phi[hJCidx[1]],hJet_mass_JER_down[1]))',newtree)
                fAngleHB_JES_up = ROOT.TTreeFormula("fAngleHB_JES_up",'abs(VHbb::ANGLEHBWithM(hJet_pt_JES_up[0],Jet_eta[hJCidx[0]],Jet_phi[hJCidx[0]],hJet_mass_JES_up[0],hJet_pt_JES_up[1],Jet_eta[hJCidx[1]],Jet_phi[hJCidx[1]],hJet_mass_JES_up[1]))',newtree)
                fAngleHB_JES_down = ROOT.TTreeFormula("fAngleHB_JES_down",'abs(VHbb::ANGLEHBWithM(hJet_pt_JES_down[0],Jet_eta[hJCidx[0]],Jet_phi[hJCidx[0]],hJet_mass_JES_down[0],hJet_pt_JES_down[1],Jet_eta[hJCidx[1]],Jet_phi[hJCidx[1]],hJet_mass_JES_down[1]))',newtree)
                fAngleZZS_JER_up = ROOT.TTreeFormula("fAngleZZS_JER_Up",'abs(VHbb::ANGLELZ(H_JER.pt_up,H_eta,H_phi,H_JER.pt_up,V_pt,V_eta,V_phi,V_mass))',newtree)
                fAngleZZS_JER_down = ROOT.TTreeFormula("fAngleZZS_JER_Down",'abs(VHbb::ANGLELZ(H_JER.pt_down,H_eta,H_phi,H_JER.pt_down,V_pt,V_eta,V_phi,V_mass))',newtree)
                fAngleZZS_JES_up = ROOT.TTreeFormula("fAngleZZS_JES_Up",'abs(VHbb::ANGLELZ(H_JER.pt_up,H_eta,H_phi,H_JER.pt_up,V_pt,V_eta,V_phi,V_mass))',newtree)
                fAngleZZS_JES_down = ROOT.TTreeFormula("fAngleZZS_JES_Down",'abs(VHbb::ANGLELZ(H_JER.pt_down,H_eta,H_phi,H_JER.pt_down,V_pt,V_eta,V_phi,V_mass))',newtree)
                lheWeight = array('f',[0])
                newtree.Branch('lheWeight',lheWeight,'lheWeight/F')
                theBinForms = {}
                if lhe_weight_map and 'DY' in job.name:
                    for bin in lhe_weight_map:
                        theBinForms[bin] = ROOT.TTreeFormula("Bin_formula_%s"%(bin),bin,tree)
                else:
                    lheWeight[0] = 1.
            
        ### Adding new variable from configuration ###
        newVariableNames = []
        try:
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
                newVariables[variableName] = array('f',[0])
                newtree.Branch(variableName,newVariables[variableName],variableName+'/F')
                newVariableFormulas[variableName] =ROOT.TTreeFormula(variableName,formula,tree)
                print "adding variable ",variableName,", using formula",writeNewVariables[variableName]," ."
        except:
            pass

        print 'starting event loop, processing',str(nEntries),'events'
        j_out=1;

        #########################
        #Start event loop
        #########################

        for entry in range(0,nEntries):
                #if entry>10000: break
                #if entry>1000: break
                if entry>10000: break
                if ((entry%j_out)==0):
                    if ((entry/j_out)==9 and j_out < 1e4): j_out*=10;
                    print strftime("%Y-%m-%d %H:%M:%S", gmtime()),' - processing event',str(entry)+'/'+str(nEntries), '(cout every',j_out,'events)'
                    #sys.stdout.flush()

                tree.GetEntry(entry)

                ### Fill new variable from configuration ###
                for variableName in newVariableNames:
                    newVariableFormulas[variableName].GetNdata()
                    newVariables[variableName][0] = newVariableFormulas[variableName].EvalInstance()

                if tree.nhJCidx<2: continue
                # if len(tree.hJCidx) == 0: continue
                if tree.nJet<=tree.hJCidx[0] or tree.nJet<=tree.hJCidx[1]:
                    print('tree.nJet<=tree.hJCidx[0] or tree.nJet<=tree.hJCidx[1]',tree.nJet,tree.hJCidx[0],tree.hJCidx[1])
                    print('skip event')
                    newtree.Fill()
                    continue
                if job.type != 'DATA':
                    EventForTraining[0]=int(not TFlag.EvalInstance())
                if lhe_weight_map and 'DY' in job.name:
                    match_bin = None
                    for bin in lhe_weight_map:
                        if applyRegression:
                            if theBinForms[bin].EvalInstance() > 0.:
                                match_bin = bin
                    if applyRegression:
                        if match_bin:
                            lheWeight[0] = lhe_weight_map[match_bin]
                        else:
                            lheWeight[0] = 1.

                # Has fat higgs
                # fatHiggsFlag=fFatHFlag.EvalInstance()*fFatHnFilterJets.EvalInstance()

                # get
                if channel == "Znn":
                    vect.SetPtEtaPhiM(fVpt.EvalInstance(),fVeta.EvalInstance(),fVphi.EvalInstance(),fVmass.EvalInstance())
                    # print tree.Jet_pt
                    # print tree.hJCidx
                    # hJet_pt = tree.Jet_pt[tree.hJCidx]
                    # hJet_mass = tree.Jet_mass[tree.hJCidx]

                    ##FIXME##
                    try:
                        hJet_pt0 = tree.Jet_pt[tree.hJCidx[0]]
                        hJet_pt1 = tree.Jet_pt[tree.hJCidx[1]]
                    except:
                        print "tree.nhJCidx",tree.nhJCidx
                        print "tree.nJet",tree.nJet
                        print "tree.hJCidx[0]",tree.hJCidx[0]
                        print "tree.hJCidx[1]",tree.hJCidx[1]
                        if tree.hJCidx[1] >=tree.nJet : tree.hJCidx[1] =1
                        if tree.hJCidx[0] >=tree.nJet : tree.hJCidx[0] =0


                    hJet_pt[0] = hJet_pt0
                    hJet_pt[1] = hJet_pt1
                    hJet_mass0 = tree.Jet_mass[tree.hJCidx[0]]
                    hJet_mass1 = tree.Jet_mass[tree.hJCidx[1]]
                    if job.type != 'DATA': hJet_mcPt0 = tree.Jet_mcPt[tree.hJCidx[0]]
                    if job.type != 'DATA': hJet_mcPt1 = tree.Jet_mcPt[tree.hJCidx[1]]
                    hJet_rawPt0 = tree.Jet_rawPt[tree.hJCidx[0]]
                    hJet_rawPt1 = tree.Jet_rawPt[tree.hJCidx[1]]
                    hJet_phi0 = tree.Jet_phi[tree.hJCidx[0]]
                    hJet_phi1 = tree.Jet_phi[tree.hJCidx[1]]
                    hJet_eta0 = tree.Jet_eta[tree.hJCidx[0]]
                    hJet_eta1 = tree.Jet_eta[tree.hJCidx[1]]

                    # NB. Jet_corr_JECUp - Jet_corr = Jet_corr - Jet_corr_JECDown
                    # hJet_JECUnc0 = tree.Jet_corr_JECUp[tree.hJCidx[0]] - tree.Jet_corr[tree.hJCidx[0]]
                    # hJet_JECUnc1 = tree.Jet_corr_JECUp[tree.hJCidx[1]] - tree.Jet_corr[tree.hJCidx[1]]

                    hJet_ptOld[0] = tree.Jet_pt[tree.hJCidx[0]]
                    hJet_ptOld[1] = tree.Jet_pt[tree.hJCidx[1]]
                    if job.type != 'DATA': hJet_ptMc[0] = tree.Jet_mcPt[tree.hJCidx[0]]
                    if job.type != 'DATA': hJet_ptMc[1] = tree.Jet_mcPt[tree.hJCidx[1]]
                    hJet_phi[0] = tree.Jet_phi[tree.hJCidx[0]]
                    hJet_phi[1] = tree.Jet_phi[tree.hJCidx[1]]
                    hJet_eta[0] = tree.Jet_eta[tree.hJCidx[0]]
                    hJet_eta[1] = tree.Jet_eta[tree.hJCidx[1]]
                    hJet_mass[0] = tree.Jet_mass[tree.hJCidx[0]]
                    hJet_mass[1] = tree.Jet_mass[tree.hJCidx[1]]


                    # Filterjets
                    # if fatHiggsFlag:
                       # fathFilterJets_pt0 = tree.fathFilterJets_pt[tree.hJCidx[0]]
                       # fathFilterJets_pt1 = tree.fathFilterJets_pt[tree.hJCidx[1]]
                       # fathFilterJets_eta0 = tree.fathFilterJets_eta[tree.hJCidx[0]]
                       # fathFilterJets_eta1 = tree.fathFilterJets_eta[tree.hJCidx[1]]
                       # fathFilterJets_phi0 = tree.fathFilterJets_phi[tree.hJCidx[0]]
                       # fathFilterJets_phi1 = tree.fathFilterJets_phi[tree.hJCidx[1]]
                       # fathFilterJets_e0 = tree.fathFilterJets_e[tree.hJCidx[0]]
                       # fathFilterJets_e1 = tree.fathFilterJets_e[tree.hJCidx[1]]
                    Event[0]=fEvent.EvalInstance()
                    METet[0]=fMETet.EvalInstance()
                    rho[0]=frho.EvalInstance()
                    METphi[0]=fMETphi.EvalInstance()
                    for key, value in regDict.items():
                        # if not (value == 'hJet_MET_dPhi' or value == 'METet' or value == "rho" or value == "hJet_et" or value == 'hJet_mt' or value == 'hJet_rawPt'):
                        for syst in ["","JER_up","JER_down","JEC_up","JEC_down"]:
                            if job.type == 'DATA' and not syst is "": continue
                            theForms["form_reg_%s_0" %(key+syst)].GetNdata();
                            theForms["form_reg_%s_1" %(key+syst)].GetNdata();
                            theVars0[key+syst][0] = theForms["form_reg_%s_0" %(key+syst)].EvalInstance()
                            theVars1[key+syst][0] = theForms["form_reg_%s_1" %(key+syst)].EvalInstance()
                    # for key, value in regDictFilterJets.items():
                       # if not (value == 'hJet_MET_dPhi' or value == 'METet' or value == "rho" or value == "hJet_et" or value == 'hJet_mt' or value == 'hJet_rawPt'):
                           # theVars0FJ[key][0] = theFormsFJ["form_reg_%s_0" %(key)].EvalInstance()
                           # theVars1FJ[key][0] = theFormsFJ["form_reg_%s_1" %(key)].EvalInstance()
                    hJet_MET_dPhi[0] = deltaPhi(METphi[0],hJet_phi0)
                    hJet_MET_dPhi[1] = deltaPhi(METphi[0],hJet_phi1)
                    hJet_MET_dPhiArray[0][0] = deltaPhi(METphi[0],hJet_phi0)
                    hJet_MET_dPhiArray[1][0] = deltaPhi(METphi[0],hJet_phi1)
                    if not job.type == 'DATA':
                        corrRes0 = corrPt(hJet_pt0,hJet_eta0,hJet_mcPt0)
                        corrRes1 = corrPt(hJet_pt1,hJet_eta1,hJet_mcPt1)
                        hJet_rawPt0 *= corrRes0
                        hJet_rawPt1 *= corrRes1
                    hJet_rawPtArray[0][0] = hJet_rawPt0
                    hJet_rawPtArray[1][0] = hJet_rawPt1
                    hJ0.SetPtEtaPhiM(hJet_pt0,hJet_eta0,hJet_phi0,hJet_mass0)
                    hJ1.SetPtEtaPhiM(hJet_pt1,hJet_eta1,hJet_phi1,hJet_mass1)
                    jetEt0 = hJ0.Et()
                    jetEt1 = hJ1.Et()
                    hJet_mt0 = hJ0.Mt()
                    hJet_mt1 = hJ1.Mt()

                if channel == "Znn":
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

                ##########################
                # Loop to fill bTag weights variables
                ##########################

                if applyBTagweights:
                    if not job.type == 'DATA':

                         sysMap = {}
                         sysMap["JESUp"] = "up_jes"
                         sysMap["JESDown"] = "down_jes"
                         sysMap["LFUp"] = "up_lf"
                         sysMap["LFDown"] = "down_lf"
                         sysMap["HFUp"] = "up_hf"
                         sysMap["HFDown"] = "down_hf"
                         sysMap["HFStats1Up"] = "up_hfstats1"
                         sysMap["HFStats1Down"] = "down_hfstats1"
                         sysMap["HFStats2Up"] = "up_hfstats2"
                         sysMap["HFStats2Down"] = "down_hfstats2"
                         sysMap["LFStats1Up"] = "up_lfstats1"
                         sysMap["LFStats1Down"] = "down_lfstats1"
                         sysMap["LFStats2Up"] = "up_lfstats2"
                         sysMap["LFStats2Down"] = "down_lfstats2"
                         sysMap["cErr1Up"] = "up_cferr1"
                         sysMap["cErr1Down"] = "down_cferr1"
                         sysMap["cErr2Up"] = "up_cferr2"
                         sysMap["cErr2Down"] = "down_cferr2"

                         jets = []
                         for i in range(tree.nJet):
                             if (tree.Jet_pt[i] > 25 and abs(tree.Jet_eta[i]) < 2.4):
                                 jet = Jet(tree.Jet_pt[i], tree.Jet_eta[i], tree.Jet_hadronFlavour[i], tree.Jet_btagCSV[i])
                                 jets.append(jet)

                         weights = {}
                         for syst in ["JES", "LF", "HF", "LFStats1", "LFStats2", "HFStats1", "HFStats2", "cErr1", "cErr2"]:
                            for sdir in ["Up", "Down"]:
                                weights[syst+sdir] = get_event_SF( jets, sysMap[syst+sdir], "CSV")

                         weights["central"] = get_event_SF( jets, "central", "CSV")
                         bTagWeight_RunEF[0] = weights["central"]
                         bTagWeightJESUp_RunEF[0] = weights["JESUp"]
                         bTagWeightJESDown_RunEF[0] = weights["JESDown"]
                         bTagWeightLFUp_RunEF[0] = weights["LFUp"]
                         bTagWeightLFDown_RunEF[0] = weights["LFDown"]
                         bTagWeightHFUp_RunEF[0] = weights["HFUp"]
                         bTagWeightHFDown_RunEF[0] = weights["HFDown"]
                         bTagWeightLFStats1Up_RunEF[0] = weights["LFStats1Up"]
                         bTagWeightLFStats1Down_RunEF[0] = weights["LFStats1Down"]
                         bTagWeightLFStats2Up_RunEF[0] = weights["LFStats2Up"]
                         bTagWeightLFStats2Down_RunEF[0] = weights["LFStats2Down"]
                         bTagWeightHFStats1Up_RunEF[0] = weights["HFStats1Up"]
                         bTagWeightHFStats1Down_RunEF[0] = weights["HFStats1Down"]
                         bTagWeightHFStats2Up_RunEF[0] = weights["HFStats2Up"]
                         bTagWeightHFStats2Down_RunEF[0] = weights["HFStats2Down"]
                         bTagWeightcErr1Up_RunEF[0] = weights["cErr1Up"]
                         bTagWeightcErr1Down_RunEF[0] = weights["cErr1Down"]
                         bTagWeightcErr2Up_RunEF[0] = weights["cErr2Up"]
                         bTagWeightcErr2Down_RunEF[0] = weights["cErr2Down"]


            # ================ Lepton Scale Factors =================
                # For custom made form own JSON files

                    #Reinitialize all the variables

                DY_specialWeight[0] = 1.
                weight_SF_LooseISO[0], weight_SF_LooseISO[1],  weight_SF_LooseISO[2] = 1.,1.,1.
                weight_SF_LooseMVAID_BCD[0], weight_SF_LooseMVAID_BCD[1], weight_SF_LooseMVAID_BCD[2]  = 1.,1.,1.
                weight_SF_LooseMVAID_BCDEF[0], weight_SF_LooseMVAID_BCDEF[1], weight_SF_LooseMVAID_BCDEF[2] = 1.,1.,1.
                weight_Eff_eletriglooseBCD[0], weight_Eff_eletriglooseBCD[1], weight_Eff_eletriglooseBCD[2] = 1.,1.,1.
                weight_Eff_eletriglooseBCDEF[0], weight_Eff_eletriglooseBCDEF[1], weight_Eff_eletriglooseBCDEF[2] = 1.,1.,1.
                weight_Eff_eletrigloosept23[0], weight_Eff_eletrigloosept23[1], weight_Eff_eletrigloosept23[2]= 1.,1.,1.
                weight_Eff_mutriglooseICHEP[0], weight_Eff_mutriglooseICHEP[1], weight_Eff_mutriglooseICHEP[2] = 1.,1.,1.
                weight_Eff_mutrigloose[0], weight_Eff_mutrigloose[1], weight_Eff_mutrigloose[2] = 1.,1.,1.
                weight_trk_electron[0], weight_trk_electron[1], weight_trk_electron[2] = 1.,1.,1.
                eleweight[0], eleweight[1], eleweight[2] = 1.,1.,1.
                muweight[0], muweight[1], muweight[2] = 1.,1.,1.

                if not job.type == 'DATA':

                    muTrigEffBfr = []
                    muTrigEffAftr = []
                    wdir = config.get('Directories','vhbbpath')
                    jsons = {
                        wdir+'/python/json/EfficienciesAndSF_ISO.json' : ['MC_NUM_LooseRelIso_DEN_LooseID_PAR_pt_spliteta_bin1', 'abseta_pt_ratio'],
                        wdir+'/python/json/HLT_Ele23_WPLoose.json' : ['ScaleFactor_egammaEff_WP80', 'eta_pt_ratio'],
                        wdir+'/python/json/ScaleFactor_egammaEff_WP80.json' : ['ScaleFactor_egammaEff_WP80', 'pt_eta_ratio'],
                        wdir+'/python/json/ScaleFactor_egammaEff_WP90.json' : ['ScaleFactor_egammaEff_WP90', 'eta_pt_ratio'],
                        wdir+'/python/json/eff_Ele27_WPLoose_Eta2p1_RunBtoF.json' : ['Trigger_Eff', 'eta_pt_ratio'],
                        wdir+'/python/json/egammaEffi_tracker.json' : ['egammaEffi_tracker', 'eta_pt_ratio'],
                        wdir+'/python/json/SingleMuonTrigger_LooseMuons_beforeL2fix_Z_RunBCD_prompt80X_7p65.json' : ['MuonTrigger_data_all_IsoMu22_OR_IsoTkMu22_pteta_Run2016B_beforeL2Fix', 'abseta_pt_MC'],
                        wdir+'/python/json/SingleMuonTrigger_LooseMuons_afterL2fix_Z_RunBCD_prompt80X_7p65.json' : ['MuonTrigger_data_all_IsoMu22_OR_IsoTkMu22_pteta_Run2016B_afterL2Fix', 'abseta_pt_MC'],
                        #ID+ISO
                        wdir+'/python/json/WP90PlusIso_BCD.json' : ['WP90PlusIso_BCD', 'eta_pt_ratio'],
                        wdir+'/python/json/WP90PlusIso_BCDEF.json' : ['WP90PlusIso_BCDEF', 'eta_pt_ratio'],
                        #trigg
                        wdir+'/python/json/WP90_BCD_withRelIso.json' : ['electronTriggerEfficiencyHLT_Ele27_WPLoose_eta2p1_WP90_BCD', 'eta_pt_ratio'],
                        wdir+'/python/json/WP90_BCDEF_withRelIso.json' : ['electronTriggerEfficiencyHLT_Ele27_WPLoose_eta2p1_WP90_BCDEF', 'eta_pt_ratio']
                        }
                    for j, name in jsons.iteritems():

                        weight = []
                        lepCorr = LeptonSF(j , name[0], name[1])

                        if not j.find('ScaleFactor_egammaEff_WP80') != -1:
                            weight.append(lepCorr.get_2D( tree.vLeptons_pt[0], tree.vLeptons_eta[0]))
                            weight.append(lepCorr.get_2D( tree.vLeptons_pt[1], tree.vLeptons_eta[1]))
                        else: 
                            weight.append(lepCorr.get_2D( tree.vLeptons_eta[0], tree.vLeptons_pt[0]))
                            weight.append(lepCorr.get_2D( tree.vLeptons_eta[1], tree.vLeptons_pt[1]))

                        if tree.Vtype == 0:
                            if j.find('EfficienciesAndSF_ISO') != -1:
                                computeSF(weight_SF_LooseISO)
                            elif j.find('SingleMuonTrigger_LooseMuons_beforeL2fix_Z_RunBCD_prompt80X_7p65') != -1:
                                muTrigEffBfr = weight
                            elif j.find('SingleMuonTrigger_LooseMuons_afterL2fix_Z_RunBCD_prompt80X_7p65') != -1:
                                muTrigEffAftr = weight
                        elif tree.Vtype == 1:
                            if j.find('WP90PlusIso_BCD.json') != -1:
                                computeSF(weight_SF_LooseMVAID_BCD)
                            elif j.find('WP90PlusIso_BCDEF.json') != -1:
                                computeSF(weight_SF_LooseMVAID_BCDEF)
                            elif j.find('egammaEffi_tracker') != -1:
                                computeSF(weight_trk_electron)
                            elif j.find('WP90_BCD_withRelIso') != -1:
                                computeEff(weight_Eff_eletriglooseBCD)
                            elif j.find('WP90_BCDEF_withRelIso') != -1:
                                computeEff(weight_Eff_eletriglooseBCDEF)
                            elif j.find('HLT_Ele23_WPLoose') != -1:
                                computeEff(weight_Eff_eletrigloosept23)
                        else:
                            sys.exit('@ERROR: SF list doesn\'t match json files. Abort')

                    # End JSON loop ====================================

                    #Fill muon triggers

                    if tree.Vtype == 0:
                           #for ICHEP dataset
                        weight = computeWeight(0.04854, 0.95145)
                        computeEff(weight_Eff_mutriglooseICHEP)

                           #for full 22/fb dataset
                        weight = computeWeight(0.02772, 0.97227)
                        computeEff(weight_Eff_mutrigloose)
                    #comput total weight
                    if tree.Vtype == 0:
                        muweight[0] = tree.vLeptons_SF_IdCutLoose[0]*tree.vLeptons_SF_IdCutLoose[1]*weight_SF_LooseISO[0]*tree.vLeptons_SF_trk_eta[0]*tree.vLeptons_SF_trk_eta[1]
                        muweight[1] = (tree.vLeptons_SF_IdCutLoose[0]-tree.vLeptons_SFerr_IdCutLoose[0])*(tree.vLeptons_SF_IdCutLoose[1]-tree.vLeptons_SFerr_IdCutLoose[1])*weight_SF_LooseISO[1]*(tree.vLeptons_SF_trk_eta[0]-tree.vLeptons_SFerr_trk_eta[0])*(tree.vLeptons_SF_trk_eta[1]-tree.vLeptons_SFerr_trk_eta[1])
                        muweight[2] = (tree.vLeptons_SF_IdCutLoose[0]+tree.vLeptons_SFerr_IdCutLoose[0])*(tree.vLeptons_SF_IdCutLoose[1]+tree.vLeptons_SFerr_IdCutLoose[1])*weight_SF_LooseISO[2]*(tree.vLeptons_SF_trk_eta[0]+tree.vLeptons_SFerr_trk_eta[0])*(tree.vLeptons_SF_trk_eta[1]+tree.vLeptons_SFerr_trk_eta[1])
                        #muweight[2] = tree.vLeptons_SF_IdCutLoose[0]*tree.vLeptons_SF_IdCutLoose[1]*weight_SF_LooseISO[0]*tree.vLeptons_SF_trk_eta[0]*tree.vLeptons_SF_trk_eta[1]
                    elif tree.Vtype == 1:
                        eleweight[0] = weight_SF_LooseMVAID_BCD[0]*weight_trk_electron[0]
                        eleweight[1] = weight_SF_LooseMVAID_BCD[1]*weight_trk_electron[1]
                        eleweight[2] = weight_SF_LooseMVAID_BCD[2]*weight_trk_electron[2]

                    if not job.specialweight:
                        DY_specialWeight[0] = 1
                    else :
                        specialWeight = ROOT.TTreeFormula('specialWeight',job.specialweight, tree)
                        specialWeight_ = specialWeight.EvalInstance()
                        DY_specialWeight[0] = specialWeight_

                ###########################
                ## Adding mu SFs
                ###########################


                #eTrigSFWeight = 1
                #eIDLooseSFWeight = 1
                #eTrigSFWeight= 1

                #HVdPhi_reg[0] = 300

                #dphi = tree.HCSV_reg_phi - tree.V_phi
                #if dphi > math.pi:
                #    dphi = dphi - 2*math.pi
                #elif dphi <= -math.pi:
                #    dphi = dphi + 2*math.pi
                #HVdPhi_reg[0] = dphi

                #if job.type != 'DATA':

                #    if tree.Vtype == 1:
                #        lepton_EvtWeight[0] = eIDLooseSFWeight*eTrigSFWeight
#               # elif channel == "Zmm":
                #    # Add trigger SF
                #    pTcut = 22;

                #    DR = [999, 999]
                #    debug = False

                #    # dR matching
                #    for k in range(0,2):
                #        for l in range(0,len(tree.trgObjects_hltIsoMu18_eta)):
                #            dr_ = deltaR(tree.vLeptons_eta[k], tree.vLeptons_phi[k], tree.trgObjects_hltIsoMu18_eta[l], tree.trgObjects_hltIsoMu18_phi[l])
                #            if dr_ < DR[k] and tree.vLeptons_pt[k] > 22:
                #                DR[k] = dr_

                #    Mu1pass = DR[0] < 0.5
                #    Mu2pass = DR[1] < 0.5

                #    SF1 = tree.vLeptons_SF_HLT_RunD4p2[0]*0.1801911165 + tree.vLeptons_SF_HLT_RunD4p3[0]*0.8198088835
                #    SF2 = tree.vLeptons_SF_HLT_RunD4p2[1]*0.1801911165 + tree.vLeptons_SF_HLT_RunD4p3[1]*0.8198088835
                #    eff1 = tree.vLeptons_Eff_HLT_RunD4p2[0]*0.1801911165 + tree.vLeptons_Eff_HLT_RunD4p3[0]*0.8198088835
                #    eff2 = tree.vLeptons_Eff_HLT_RunD4p2[1]*0.1801911165 + tree.vLeptons_Eff_HLT_RunD4p3[1]*0.8198088835

                #    #print 'vLeptSFw is', vLeptons_SFweight_HLT[0]
                #    #print 'Vtype is', tree.Vtype

                #    if tree.Vtype == 1:
                #        vLeptons_SFweight_HLT[0] = 1
                #    elif tree.Vtype == 0:
                #        if not Mu1pass and not Mu2pass:
                #            vLeptons_SFweight_HLT[0] = 0
                #        elif Mu1pass and not Mu2pass:
                #            vLeptons_SFweight_HLT[0] = SF1
                #        elif not Mu1pass and Mu2pass:
                #            vLeptons_SFweight_HLT[0] = SF2
                #        elif Mu1pass and Mu2pass:
                #            effdata = 1 - (1-SF1*eff1)*(1-SF2*eff2);
                #            effmc = 1 - (1-eff1)*(1-eff2);
                #            vLeptons_SFweight_HLT[0] = effdata/effmc
                #    #print 'vLeptSFw afer fill is', vLeptons_SFweight_HLT[0]

            # ================ BTag weights from CSV =================
                #

                ##setcalibCSV('ttH_BTV_CSVv2_13TeV_2016BC_7p6_2016_08_13.csv')


                if applyRegression:
                    HNoReg.HiggsFlag = 1
                    HNoReg.mass = (hJ0+hJ1).M()
                    HNoReg.pt = (hJ0+hJ1).Pt()
                    HNoReg.eta = (hJ0+hJ1).Eta()
                    HNoReg.phi = (hJ0+hJ1).Phi()
                    HNoReg.dR = hJ0.DeltaR(hJ1)
                    HNoReg.dPhi = hJ0.DeltaPhi(hJ1)
                    HNoReg.dEta = abs(hJ0.Eta()-hJ1.Eta())

                    HNoRegwithFSR = ROOT.TLorentzVector()
                    HNoRegwithFSR.SetPtEtaPhiM(HNoReg.pt,HNoReg.eta,HNoReg.phi,HNoReg.mass)
                    
                    HNoRegwithFSR = addAdditionalJets(HNoRegwithFSR,tree)

                    HaddJetsdR08NoReg.HiggsFlag = 1
                    HaddJetsdR08NoReg.mass = HNoRegwithFSR.M()
                    HaddJetsdR08NoReg.pt = HNoRegwithFSR.Pt()
                    HaddJetsdR08NoReg.eta = HNoRegwithFSR.Eta()
                    HaddJetsdR08NoReg.phi = HNoRegwithFSR.Phi()
                    HaddJetsdR08NoReg.dR = 0
                    HaddJetsdR08NoReg.dPhi = 0
                    HaddJetsdR08NoReg.dEta = 0

                    hJet_MtArray[0][0] = hJ0.Mt()
                    hJet_MtArray[1][0] = hJ1.Mt()
                    hJet_etarray[0][0] = hJ0.Et()
                    hJet_etarray[1][0] = hJ1.Et()

                    rPt0 = max(0.0001,readerJet0.EvaluateRegression( "jet0Regression" )[0])
                    rPt1 = max(0.0001,readerJet1.EvaluateRegression( "jet1Regression" )[0])

                    hJet_pt[0] = rPt0
                    hJet_pt[1] = rPt1

                    hJet_regWeight[0] = rPt0/hJet_pt0
                    hJet_regWeight[1] = rPt1/hJet_pt1

                    hJ0.SetPtEtaPhiM(rPt0,hJ0.Eta(),hJ0.Phi(),hJ0.M())
                    hJ1.SetPtEtaPhiM(rPt1,hJ1.Eta(),hJ1.Phi(),hJ1.M())
                    rMass0 = hJ0.M()
                    rMass1 = hJ1.M()

                    H.HiggsFlag = 1
                    H.mass = (hJ0+hJ1).M()
                    H.pt = (hJ0+hJ1).Pt()
                    H.eta = (hJ0+hJ1).Eta()
                    H.phi = (hJ0+hJ1).Phi()
                    H.dR = hJ0.DeltaR(hJ1)
                    H.dPhi = hJ0.DeltaPhi(hJ1)
                    H.dEta = abs(hJ0.Eta()-hJ1.Eta())
                    HVMass_Reg[0] = (hJ0+hJ1+vect).M()

                    HwithFSR = ROOT.TLorentzVector()
                    HwithFSR.SetPtEtaPhiM(H.pt,H.eta,H.phi,H.mass)

                    HwithFSR = addAdditionalJets(HwithFSR,tree)

                    HaddJetsdR08.HiggsFlag = 1
                    HaddJetsdR08.mass = HwithFSR.M()
                    HaddJetsdR08.pt = HwithFSR.Pt()
                    HaddJetsdR08.eta = HwithFSR.Eta()
                    HaddJetsdR08.phi = HwithFSR.Phi()
                    HaddJetsdR08.dR = 0
                    HaddJetsdR08.dPhi = 0
                    HaddJetsdR08.dEta = 0

                    debug_flag = False
                    if debug_flag and (hJet_regWeight[0] > 3. or hJet_regWeight[1] > 3. or hJet_regWeight[0] < 0.3 or hJet_regWeight[1] < 0.3):
                        print '### Debug event with ptReg/ptNoReg>0.3 or ptReg/ptNoReg<3 ###'
                        print 'Event %.0f' %(Event[0])
                        print 'MET %.2f' %(METet[0])
                        print 'rho %.2f' %(rho[0])
                        for key, value in regDict.items():
                            if not (value == 'hJet_MET_dPhi' or value == 'METet' or value == "rho"):
                                print '%s 0: %.2f'%(key, theVars0[key][0])
                                print '%s 1: %.2f'%(key, theVars1[key][0])
                        for i in range(2):
                            print 'dPhi %.0f %.2f' %(i,hJet_MET_dPhiArray[i][0])
                        for i in range(2):
                            print 'ptRaw %.0f %.2f' %(i,hJet_rawPtArray[i][0])
                        for i in range(2):
                            print 'Mt %.0f %.2f' %(i,hJet_MtArray[i][0])
                        for i in range(2):
                            print 'Et %.0f %.2f' %(i,hJet_etarray[i][0])
                        print 'corr 0 %.2f' %(hJet_regWeight[0])
                        print 'corr 1 %.2f' %(hJet_regWeight[1])
                        print 'rPt0 %.2f' %(rPt0)
                        print 'rPt1 %.2f' %(rPt1)
                        print 'rMass0 %.2f' %(rMass0)
                        print 'rMass1 %.2f' %(rMass1)
                        print 'Mass %.2f' %(H.mass)

                        print 'hJet_pt0: ',hJet_pt0
                        print 'hJet_pt1: ',hJet_pt1
                    # if fatHiggsFlag:
                        # hFJ0.SetPtEtaPhiE(fathFilterJets_pt0,fathFilterJets_eta0,fathFilterJets_phi0,fathFilterJets_e0)
                        # hFJ1.SetPtEtaPhiE(fathFilterJets_pt1,fathFilterJets_eta1,fathFilterJets_phi1,fathFilterJets_e1)
                        # rFJPt0 = max(0.0001,readerFJ0.EvaluateRegression( "jet0RegressionFJ" )[0])
                        # rFJPt1 = max(0.0001,readerFJ1.EvaluateRegression( "jet1RegressionFJ" )[0])
                        # fathFilterJets_regWeight[0] = rPt0/fathFilterJets_pt0
                        # fathFilterJets_regWeight[1] = rPt1/fathFilterJets_pt1
                        # rFJE0 = fathFilterJets_e0*fathFilterJets_regWeight[0]
                        # rFJE1 = fathFilterJets_e1*fathFilterJets_regWeight[1]
                        # hFJ0.SetPtEtaPhiE(rFJPt0,fathFilterJets_eta0,fathFilterJets_phi0,rFJE0)
                        # hFJ1.SetPtEtaPhiE(rFJPt1,fathFilterJets_eta1,fathFilterJets_phi1,rFJE1)
                        # FatHReg[0] = (hFJ0+hFJ1).M()
                        # FatHReg[1] = (hFJ0+hFJ1).Pt()
                    # else:
                        # FatHReg[0] = 0.
                        # FatHReg[1] = 0.

                        # print rFJPt0
                        # print rFJPt1

                if channel == "Znn":
                    angleHB[0]=fAngleHB.EvalInstance()
                    angleLZ[0]=fAngleLZ.EvalInstance()
                    angleZZS[0]=fAngleZZS.EvalInstance()

               # for i, angLikeBkg in enumerate(AngLikeBkgs):
                   # likeSBH[i] = math.fabs(SigBH[i].Eval(angleHB[0]))
                   # likeBBH[i] = math.fabs(BkgBH[i].Eval(angleHB[0]))

                   # likeSZZS[i] = math.fabs(SigZZS[i].Eval(angleZZS[0]))
                   # likeBZZS[i] = math.fabs(BkgZZS[i].Eval(angleZZS[0]))

                   # likeSLZ[i] = math.fabs(SigLZ[i].Eval(angleLZ[0]))
                   # likeBLZ[i] = math.fabs(BkgLZ[i].Eval(angleLZ[0]))

                   # likeSMassZS[i] = math.fabs(SigMassZS[i].Eval(fHVMass.EvalInstance()))
                   # likeBMassZS[i] = math.fabs(BkgMassZS[i].Eval(fHVMass.EvalInstance()))

                   # scaleSig  = float( ang_yield['Sig'] / (ang_yield['Sig'] + ang_yield[angLikeBkg]))
                   # scaleBkg  = float( ang_yield[angLikeBkg] / (ang_yield['Sig'] + ang_yield[angLikeBkg]) )

                   # numerator = (likeSBH[i]*likeSZZS[i]*likeSLZ[i]*likeSMassZS[i]);
                   # denominator = ((scaleBkg*likeBLZ[i]*likeBZZS[i]*likeBBH[i]*likeBMassZS[i])+(scaleSig*likeSBH[i]*likeSZZS[i]*likeSLZ[i]*likeSMassZS[i]))

                   # if denominator > 0:
                       # kinLikeRatio[i] = numerator/denominator;
                   # else:
                       # kinLikeRatio[i] = 0;


                if channel == "Znn":
                    if job.type == 'DATA':
                        for i in range(2):
                            csv = float(tree.Jet_btagCSV[tree.hJCidx[i]])
                            hJet_btagCSVOld[i] = csv
                            hJet_btagCSV[i] = csv
                        newtree.Fill()
                        continue

                    for i in range(2):
                        flavour = int(tree.Jet_hadronFlavour[tree.hJCidx[i]])
                        pt = float(tree.Jet_pt[tree.hJCidx[i]])
                        eta = float(tree.Jet_eta[tree.hJCidx[i]])
                        csv = float(tree.Jet_btagCSV[tree.hJCidx[i]])
                        ##FIXME## we have to add the CSV reshaping
                        hJet_btagCSVOld[i] = tree.Jet_btagCSV[tree.hJCidx[i]]
                        hJet_btagCSV[i] = tree.Jet_btagCSV[tree.hJCidx[i]]
                        hJet_btagCSVDown[i] = tree.Jet_btagCSV[tree.hJCidx[i]]
                        hJet_btagCSVUp[i] = tree.Jet_btagCSV[tree.hJCidx[i]]
                        hJet_btagCSVFDown[i] = tree.Jet_btagCSV[tree.hJCidx[i]]
                        hJet_btagCSVFUp[i] = tree.Jet_btagCSV[tree.hJCidx[i]]

                #Add here all the new JER/JEC variables

                if job.type != 'DATA':

                  # # hJet flags

                  #  hJet_high[0], hJet_high[1] = 0,0
                  #  hJet_low[0],hJet_low[0]  = 0,0
                  #  hJet_central[0],hJet_central[0]  = 0,0
                  #  hJet_forward[0],hJet_forward[0]  = 0,0

                  # # hJet flags
                  #  if tree.Jet_pt_reg[tree.hJCidx[0]] > 100.: hJet_high[0] == 1
                  #  if tree.Jet_pt_reg[tree.hJCidx[1]] > 100.: hJet_high[1] == 1

                  #  if tree.Jet_pt_reg[tree.hJCidx[0]] < 100.: hJet_low[0] == 1
                  #  if tree.Jet_pt_reg[tree.hJCidx[1]] < 100.: hJet_low[1] == 1

                  #  if tree.Jet_eta[tree.hJCidx[0]] > 1.4: hJet_forward[0] == 1
                  #  if tree.Jet_eta[tree.hJCidx[1]] > 1.4: hJet_forward[1] == 1

                  #  if tree.Jet_eta[tree.hJCidx[0]] < 1.4: hJet_central[0] == 1
                  #  if tree.Jet_eta[tree.hJCidx[1]] < 1.4: hJet_central[1] == 1

                    ####################
                    #Dijet mass
                    ####################

                    #Initialize two higgs jet


                    def fillvar():
                        #DefaultVar = {'HCSV_reg_corrSYSUD_mass_CAT':tree.HCSV_reg_mass,'HCSV_reg_corrSYSUD_pt_CAT':tree.HCSV_reg_pt,'HCSV_reg_corrSYSUD_phi_CAT':tree.HCSV_reg_phi,'HCSV_reg_corrSYSUD_eta_CAT':tree.HCSV_reg_eta}
                        for SysDic in SysDicList:
                            if not eval(ConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('CAT',SysDic['cat'])):
                                if SysDic['var'] == 'Jet_pt_reg_corrSYSUD_CAT':
                                    SysDic['varptr'][0] =  eval(DefaultVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','0'))
                                    SysDic['varptr'][1] =  eval(DefaultVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','1'))
                                else:
                                    SysDic['varptr'][0] =  eval(DefaultVar[SysDic['var']])
                            else:
                                if SysDic['var'] == 'Jet_pt_reg_corrSYSUD_CAT':
                                    for jetindex in range(len(tree.Jet_eta)):
                                        booljet = eval(JetConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('tree.hJCidx[INDEX]',str(jetindex)))
                                        if booljet:
                                            #print 'jetindex is', jetindex
                                            #print 'sysdic is', SysDic['varptr']
                                            SysDic['varptr'][jetindex] =  eval(SYSVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX',str(jetindex)))

                                #    booljet1 = eval(JetConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','0'))
                                #    booljet2 = eval(JetConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','1'))
                                #    if booljet1 and not booljet2:
                                #        SysDic['varptr'][0] =  eval(SYSVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','0'))
                                #        SysDic['varptr'][1] =  eval(DefaultVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','1'))
                                #    elif not booljet1 and booljet2:
                                #        SysDic['varptr'][0] =  eval(DefaultVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','0'))
                                #        SysDic['varptr'][1] =  eval(SYSVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','1'))
                                #    elif booljet1 and booljet1:
                                #        SysDic['varptr'][0] =  eval(SYSVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','0'))
                                #        SysDic['varptr'][1] =  eval(SYSVar[SysDic['var']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','1'))
                                #    else:
                                #        print '@ERROR: jet category could not be indentified. Aborting'
                                else:
                                    Jet1 = ROOT.TLorentzVector()
                                    Jet2 = ROOT.TLorentzVector()
                                    Jet1_sys = ROOT.TLorentzVector()
                                    Jet2_sys = ROOT.TLorentzVector()
                                    Jet1.SetPtEtaPhiM(tree.Jet_pt_reg[tree.hJCidx[0]],tree.Jet_eta[tree.hJCidx[0]],tree.Jet_phi[tree.hJCidx[0]],tree.Jet_mass[tree.hJCidx[0]])
                                    Jet2.SetPtEtaPhiM(tree.Jet_pt_reg[tree.hJCidx[1]],tree.Jet_eta[tree.hJCidx[1]],tree.Jet_phi[tree.hJCidx[1]],tree.Jet_mass[tree.hJCidx[1]])

                                    booljet1 = eval(JetConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','0'))
                                    booljet2 = eval(JetConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('INDEX','1'))

                                    if booljet1 and not booljet2:
                                        eval('Jet1_sys.SetPtEtaPhiM(tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]],tree.Jet_eta[tree.hJCidx[0]],tree.Jet_phi[tree.hJCidx[0]],tree.Jet_mass[tree.hJCidx[0]])'.replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']))
                                        Jet2_sys = Jet2
                                    elif not booljet1 and booljet2:
                                        eval('Jet2_sys.SetPtEtaPhiM(tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]],tree.Jet_eta[tree.hJCidx[1]],tree.Jet_phi[tree.hJCidx[1]],tree.Jet_mass[tree.hJCidx[1]])'.replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']))
                                        Jet1_sys = Jet1
                                    elif booljet1 and booljet1:
                                        eval('Jet1_sys.SetPtEtaPhiM(tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[0]],tree.Jet_eta[tree.hJCidx[0]],tree.Jet_phi[tree.hJCidx[0]],tree.Jet_mass[tree.hJCidx[0]])'.replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']))
                                        eval('Jet2_sys.SetPtEtaPhiM(tree.Jet_pt_reg_corrSYSUD[tree.hJCidx[1]],tree.Jet_eta[tree.hJCidx[1]],tree.Jet_phi[tree.hJCidx[1]],tree.Jet_mass[tree.hJCidx[1]])'.replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']))
                                    else:
                                        print '@ERROR: jet category could not be indentified. Aborting'
                                        print 'cat is', SysDic['cat']
                                        print 'condition is', ConditionDic[SysDic['cat']].replace('SYS',SysDic['sys']).replace('UD',SysDic['UD']).replace('CAT',SysDic['cat'])
                                        print 'jet cond is', JetConditionDic[SysDic['cat']].replace('INDEX','1')
                                        sys.exit()

                                    HJet = Jet1+Jet2
                                    HJet_sys = Jet1_sys+Jet2_sys
                                    SysDic['varptr'][0] = eval(SYSVar[SysDic['var']])

                    fillvar()



                    ####  Btag Weights for high/low and eta regions ####
                    if tree.Jet_pt_reg[tree.hJCidx[0]]>100. or tree.Jet_pt_reg[tree.hJCidx[1]]>100.:
                        btag_weight_JECUp_high[0] = tree.btagWeightCSV_up_jes
                        btag_weight_JECDown_high[0] = tree.btagWeightCSV_down_jes
                        btag_weight_lfUp_high[0] = tree. btagWeightCSV_up_lf
                        btag_weight_lfDown_high[0] = tree. btagWeightCSV_down_lf
                        btag_weight_hfUp_high[0] = tree.btagWeightCSV_up_hf
                        btag_weight_hfDown_high[0] = tree.btagWeightCSV_down_hf
                        btag_weight_lfstats1Up_high[0] = tree. btagWeightCSV_up_lfstats1
                        btag_weight_lfstats1Down_high[0] = tree.btagWeightCSV_down_lfstats1
                        btag_weight_lfstats2Up_high[0] = tree.btagWeightCSV_up_lfstats2
                        btag_weight_lfstats2Down_high[0] = tree.btagWeightCSV_down_lfstats2
                        btag_weight_hfstats1Up_high[0] = tree.btagWeightCSV_up_hfstats1
                        btag_weight_hfstats2Up_high[0] = tree.btagWeightCSV_up_hfstats2
                        btag_weight_hfstats1Down_high[0] = tree.btagWeightCSV_down_hfstats1
                        btag_weight_hfstats2Down_high[0] = tree. btagWeightCSV_down_hfstats2
                        btag_weight_cferr1Up_high[0] = tree.btagWeightCSV_up_cferr1
                        btag_weight_cferr2Up_high[0] = tree.btagWeightCSV_up_cferr2
                        btag_weight_cferr1Down_high[0] = tree.btagWeightCSV_down_cferr1
                        btag_weight_cferr2Down_high[0] = tree.btagWeightCSV_down_cferr2

                    else:
                        btag_weight_JECUp_high[0] = tree.btagWeightCSV
                        btag_weight_JECDown_high[0] = tree.btagWeightCSV
                        btag_weight_JECDown_high[0] = tree.btagWeightCSV
                        btag_weight_lfUp_high[0] = tree.btagWeightCSV
                        btag_weight_lfDown_high[0] = tree.btagWeightCSV
                        btag_weight_hfUp_high[0] = tree.btagWeightCSV
                        btag_weight_hfDown_high[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Up_high[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Down_high[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Up_high[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Down_high[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Up_high[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Up_high[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Down_high[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Down_high[0] = tree.btagWeightCSV
                        btag_weight_cferr1Up_high[0] = tree.btagWeightCSV
                        btag_weight_cferr2Up_high[0] = tree.btagWeightCSV
                        btag_weight_cferr1Down_high[0] = tree.btagWeightCSV
                        btag_weight_cferr2Down_high[0] = tree.btagWeightCSV


                    if tree.Jet_pt_reg[tree.hJCidx[0]]<100. or tree.Jet_pt_reg[tree.hJCidx[1]]<100.:
                        btag_weight_JECUp_low[0] = tree.btagWeightCSV_up_jes
                        btag_weight_JECDown_low[0] = tree.btagWeightCSV_down_jes
                        btag_weight_lfUp_low[0] = tree. btagWeightCSV_up_lf
                        btag_weight_lfDown_low[0] = tree. btagWeightCSV_down_lf
                        btag_weight_hfUp_low[0] = tree.btagWeightCSV_up_hf
                        btag_weight_hfDown_low[0] = tree.btagWeightCSV_down_hf
                        btag_weight_lfstats1Up_low[0] = tree. btagWeightCSV_up_lfstats1
                        btag_weight_lfstats1Down_low[0] = tree.btagWeightCSV_down_lfstats1
                        btag_weight_lfstats2Up_low[0] = tree.btagWeightCSV_up_lfstats2
                        btag_weight_lfstats2Down_low[0] = tree.btagWeightCSV_down_lfstats2
                        btag_weight_hfstats1Up_low[0] = tree.btagWeightCSV_up_hfstats1
                        btag_weight_hfstats2Up_low[0] = tree.btagWeightCSV_up_hfstats2
                        btag_weight_hfstats1Down_low[0] = tree.btagWeightCSV_down_hfstats1
                        btag_weight_hfstats2Down_low[0] = tree. btagWeightCSV_down_hfstats2
                        btag_weight_cferr1Up_low[0] = tree.btagWeightCSV_up_cferr1
                        btag_weight_cferr2Up_low[0] = tree.btagWeightCSV_up_cferr2
                        btag_weight_cferr1Down_low[0] = tree.btagWeightCSV_down_cferr1
                        btag_weight_cferr2Down_low[0] = tree.btagWeightCSV_down_cferr2

                    else:
                        btag_weight_JECUp_low[0] = tree.btagWeightCSV
                        btag_weight_JECDown_low[0] = tree.btagWeightCSV
                        btag_weight_JECDown_low[0] = tree.btagWeightCSV
                        btag_weight_lfUp_low[0] = tree.btagWeightCSV
                        btag_weight_lfDown_low[0] = tree.btagWeightCSV
                        btag_weight_hfUp_low[0] = tree.btagWeightCSV
                        btag_weight_hfDown_low[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Up_low[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Down_low[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Up_low[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Down_low[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Up_low[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Up_low[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Down_low[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Down_low[0] = tree.btagWeightCSV
                        btag_weight_cferr1Up_low[0] = tree.btagWeightCSV
                        btag_weight_cferr2Up_low[0] = tree.btagWeightCSV
                        btag_weight_cferr1Down_low[0] = tree.btagWeightCSV
                        btag_weight_cferr2Down_low[0] = tree.btagWeightCSV

                    if tree.Jet_eta[tree.hJCidx[0]]>1.4 or tree.Jet_eta[tree.hJCidx[1]]>1.4:
                        btag_weight_JECUp_central[0] = tree.btagWeightCSV_up_jes
                        btag_weight_JECDown_central[0] = tree.btagWeightCSV_down_jes
                        btag_weight_lfUp_central[0] = tree. btagWeightCSV_up_lf
                        btag_weight_lfDown_central[0] = tree. btagWeightCSV_down_lf
                        btag_weight_hfUp_central[0] = tree.btagWeightCSV_up_hf
                        btag_weight_hfDown_central[0] = tree.btagWeightCSV_down_hf
                        btag_weight_lfstats1Up_central[0] = tree. btagWeightCSV_up_lfstats1
                        btag_weight_lfstats1Down_central[0] = tree.btagWeightCSV_down_lfstats1
                        btag_weight_lfstats2Up_central[0] = tree.btagWeightCSV_up_lfstats2
                        btag_weight_lfstats2Down_central[0] = tree.btagWeightCSV_down_lfstats2
                        btag_weight_hfstats1Up_central[0] = tree.btagWeightCSV_up_hfstats1
                        btag_weight_hfstats2Up_central[0] = tree.btagWeightCSV_up_hfstats2
                        btag_weight_hfstats1Down_central[0] = tree.btagWeightCSV_down_hfstats1
                        btag_weight_hfstats2Down_central[0] = tree. btagWeightCSV_down_hfstats2
                        btag_weight_cferr1Up_central[0] = tree.btagWeightCSV_up_cferr1
                        btag_weight_cferr2Up_central[0] = tree.btagWeightCSV_up_cferr2
                        btag_weight_cferr1Down_central[0] = tree.btagWeightCSV_down_cferr1
                        btag_weight_cferr2Down_central[0] = tree.btagWeightCSV_down_cferr2

                    else:
                        btag_weight_JECUp_central[0] = tree.btagWeightCSV
                        btag_weight_JECDown_central[0] = tree.btagWeightCSV
                        btag_weight_JECDown_central[0] = tree.btagWeightCSV
                        btag_weight_lfUp_central[0] = tree.btagWeightCSV
                        btag_weight_lfDown_central[0] = tree.btagWeightCSV
                        btag_weight_hfUp_central[0] = tree.btagWeightCSV
                        btag_weight_hfDown_central[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Up_central[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Down_central[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Up_central[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Down_central[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Up_central[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Up_central[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Down_central[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Down_central[0] = tree.btagWeightCSV
                        btag_weight_cferr1Up_central[0] = tree.btagWeightCSV
                        btag_weight_cferr2Up_central[0] = tree.btagWeightCSV
                        btag_weight_cferr1Down_central[0] = tree.btagWeightCSV
                        btag_weight_cferr2Down_central[0] = tree.btagWeightCSV


                    if tree.Jet_eta[tree.hJCidx[0]]<1.4 or tree.Jet_eta[tree.hJCidx[1]]<1.4:
                        btag_weight_JECUp_forward[0] = tree.btagWeightCSV_up_jes
                        btag_weight_JECDown_forward[0] = tree.btagWeightCSV_down_jes
                        btag_weight_lfUp_forward[0] = tree. btagWeightCSV_up_lf
                        btag_weight_lfDown_forward[0] = tree. btagWeightCSV_down_lf
                        btag_weight_hfUp_forward[0] = tree.btagWeightCSV_up_hf
                        btag_weight_hfDown_forward[0] = tree.btagWeightCSV_down_hf
                        btag_weight_lfstats1Up_forward[0] = tree. btagWeightCSV_up_lfstats1
                        btag_weight_lfstats1Down_forward[0] = tree.btagWeightCSV_down_lfstats1
                        btag_weight_lfstats2Up_forward[0] = tree.btagWeightCSV_up_lfstats2
                        btag_weight_lfstats2Down_forward[0] = tree.btagWeightCSV_down_lfstats2
                        btag_weight_hfstats1Up_forward[0] = tree.btagWeightCSV_up_hfstats1
                        btag_weight_hfstats2Up_forward[0] = tree.btagWeightCSV_up_hfstats2
                        btag_weight_hfstats1Down_forward[0] = tree.btagWeightCSV_down_hfstats1
                        btag_weight_hfstats2Down_forward[0] = tree. btagWeightCSV_down_hfstats2
                        btag_weight_cferr1Up_forward[0] = tree.btagWeightCSV_up_cferr1
                        btag_weight_cferr2Up_forward[0] = tree.btagWeightCSV_up_cferr2
                        btag_weight_cferr1Down_forward[0] = tree.btagWeightCSV_down_cferr1
                        btag_weight_cferr2Down_forward[0] = tree.btagWeightCSV_down_cferr2

                    else:
                        btag_weight_JECUp_forward[0] = tree.btagWeightCSV
                        btag_weight_JECDown_forward[0] = tree.btagWeightCSV
                        btag_weight_JECDown_forward[0] = tree.btagWeightCSV
                        btag_weight_lfUp_forward[0] = tree.btagWeightCSV
                        btag_weight_lfDown_forward[0] = tree.btagWeightCSV
                        btag_weight_hfUp_forward[0] = tree.btagWeightCSV
                        btag_weight_hfDown_forward[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Up_forward[0] = tree.btagWeightCSV
                        btag_weight_lfstats1Down_forward[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Up_forward[0] = tree.btagWeightCSV
                        btag_weight_lfstats2Down_forward[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Up_forward[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Up_forward[0] = tree.btagWeightCSV
                        btag_weight_hfstats1Down_forward[0] = tree.btagWeightCSV
                        btag_weight_hfstats2Down_forward[0] = tree.btagWeightCSV
                        btag_weight_cferr1Up_forward[0] = tree.btagWeightCSV
                        btag_weight_cferr2Up_forward[0] = tree.btagWeightCSV
                        btag_weight_cferr1Down_forward[0] = tree.btagWeightCSV
                        btag_weight_cferr2Down_forward[0] = tree.btagWeightCSV


                if applyRegression:
                    if job.type != 'DATA':
                        ## JER_up
                        rPt0 = max(0.0001,readerJet0_JER_up.EvaluateRegression( "jet0Regression" )[0])
                        rPt1 = max(0.0001,readerJet1_JER_up.EvaluateRegression( "jet1Regression" )[0])
                        hJ0.SetPtEtaPhiM(rPt0,hJet_eta0,hJet_phi0,hJet_mass0)
                        hJ1.SetPtEtaPhiM(rPt1,hJet_eta1,hJet_phi1,hJet_mass1)
                        rMass0=hJ0.M()
                        rMass1=hJ1.M()
                        hJet_pt_JER_up[0]=rPt0
                        hJet_pt_JER_up[1]=rPt1
                        hJet_mass_JER_up[0]=rMass0
                        hJet_mass_JER_up[1]=rMass1
                        H_JER[0]=(hJ0+hJ1).M()
                        H_JER[2]=(hJ0+hJ1).Pt()
                        HVMass_JER_up[0] = (hJ0+hJ1+vect).M()

                        ## JER_down
                        rPt0 = max(0.0001,readerJet0_JER_down.EvaluateRegression( "jet0Regression" )[0])
                        rPt1 = max(0.0001,readerJet1_JER_down.EvaluateRegression( "jet1Regression" )[0])
                        hJ0.SetPtEtaPhiM(rPt0,hJet_eta0,hJet_phi0,hJet_mass0)
                        hJ1.SetPtEtaPhiM(rPt1,hJet_eta1,hJet_phi1,hJet_mass1)
                        rMass0=hJ0.M()
                        rMass1=hJ1.M()
                        hJet_pt_JER_down[0]=rPt0
                        hJet_pt_JER_down[1]=rPt1
                        hJet_mass_JER_down[0]=rMass0
                        hJet_mass_JER_down[1]=rMass1
                        H_JER[1]=(hJ0+hJ1).M()
                        H_JER[3]=(hJ0+hJ1).Pt()
                        HVMass_JER_down[0] = (hJ0+hJ1+vect).M()

                        ## JEC_up
                        rPt0 = max(0.0001,readerJet0_JEC_up.EvaluateRegression( "jet0Regression" )[0])
                        rPt1 = max(0.0001,readerJet1_JEC_up.EvaluateRegression( "jet1Regression" )[0])
                        hJ0.SetPtEtaPhiM(rPt0,hJet_eta0,hJet_phi0,hJet_mass0)
                        hJ1.SetPtEtaPhiM(rPt1,hJet_eta1,hJet_phi1,hJet_mass1)
                        rMass0=hJ0.M()
                        rMass1=hJ1.M()
                        hJet_pt_JES_up[0]=rPt0
                        hJet_pt_JES_up[1]=rPt1
                        hJet_mass_JES_up[0]=rMass0
                        hJet_mass_JES_up[1]=rMass1
                        H_JES[0]=(hJ0+hJ1).M()
                        H_JES[2]=(hJ0+hJ1).Pt()
                        HVMass_JES_up[0] = (hJ0+hJ1+vect).M()

                        ## JEC_down
                        rPt0 = max(0.0001,readerJet0_JEC_down.EvaluateRegression( "jet0Regression" )[0])
                        rPt1 = max(0.0001,readerJet1_JEC_down.EvaluateRegression( "jet1Regression" )[0])
                        hJ0.SetPtEtaPhiM(rPt0,hJet_eta0,hJet_phi0,hJet_mass0)
                        hJ1.SetPtEtaPhiM(rPt1,hJet_eta1,hJet_phi1,hJet_mass1)
                        rMass0=hJ0.M()
                        rMass1=hJ1.M()
                        hJet_pt_JES_down[0]=rPt0
                        hJet_pt_JES_down[1]=rPt1
                        hJet_mass_JES_down[0]=rMass0
                        hJet_mass_JES_down[1]=rMass1
                        H_JES[1]=(hJ0+hJ1).M()
                        H_JES[3]=(hJ0+hJ1).Pt()
                        HVMass_JES_down[0] = (hJ0+hJ1+vect).M()

                    angleHB_JER_up[0]=fAngleHB_JER_up.EvalInstance()
                    angleHB_JER_down[0]=fAngleHB_JER_down.EvalInstance()
                    angleHB_JES_up[0]=fAngleHB_JES_up.EvalInstance()
                    angleHB_JES_down[0]=fAngleHB_JES_down.EvalInstance()
                    angleZZS[0]=fAngleZZS.EvalInstance()
                    angleZZS_JER_up[0]=fAngleZZS_JER_up.EvalInstance()
                    angleZZS_JER_down[0]=fAngleZZS_JER_down.EvalInstance()
                    angleZZS_JES_up[0]=fAngleZZS_JES_up.EvalInstance()
                    angleZZS_JES_down[0]=fAngleZZS_JES_down.EvalInstance()

                # print "hJet_eta[0]",hJet_eta[0]
                # print "hJet_eta[1]",hJet_eta[1]
                # print "hJet_phi[0]",hJet_phi[0]
                # print "hJet_phi[1]",hJet_phi[1]
                # print "hJet_mass[0]",hJet_mass[0]
                # print "hJet_mass[1]",hJet_mass[1]

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
            command = "uberftp t3se01 'mkdir %s ' " %(pathOUT.replace('gsidcap://t3se01.psi.ch:22128/','')+'/'+job.identifier).replace('root://t3dcachedb03.psi.ch:1094/','')
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
                # srmpathOUT = pathOUT.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('dcap://t3se01.psi.ch:22125/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                # command = 'srmcp -2 -globus_tcp_port_range 20000,25000 file:///'+tmpfile+' '+outputFile.replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                command = 'xrdcp -d 1 '+tmpfile+' '+outputFile
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
