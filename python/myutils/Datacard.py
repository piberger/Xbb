#!/usr/bin/env python
from __future__ import print_function
import os, ROOT
ROOT.gROOT.SetBatch(True)
from math import sqrt
from copy import deepcopy
from sample_parser import ParseInfo
import json
import NewTreeCache as TreeCache
from sampleTree import SampleTree as SampleTree
from NewStackMaker import NewStackMaker as StackMaker
from NewHistoMaker import NewHistoMaker as HistoMaker
from BranchList import BranchList
from XbbTools import XbbTools
from FileLocator import FileLocator
import array
import re
import itertools
import math

class Datacard(object):
    def __init__(self, config, region, verbose=True, fileLocator=None, systematics=None):
        self.reshapeBins = True
        self.debug = 'XBBDEBUG' in os.environ 
        self.verbose = verbose
        self.config = config
        self.DCtype = 'TH'
        self.histograms = None
        self.histogramCounter = 0
        self.defaultMcRescaleMVA = 2.0
        if self.config.has_option('LimitGeneral','mcRescaleMVA'):
            self.defaultMcRescaleMVA = float(self.config.get('LimitGeneral','mcRescaleMVA'))
            print("INFO: rescaling MC for MVA regions by:", self.defaultMcRescaleMVA)
            print("INFO: to compensate for eval cut:", self.config.get('Cuts','EvalCut'))
        self.fileLocator = fileLocator if fileLocator is not None else FileLocator(config=self.config)
        self.DCprocessSeparatorDict = {'WS':':','TH':'/'}
        VHbbNameSpace = config.get('VHbbNameSpace', 'library')
        returnCode = ROOT.gSystem.Load(VHbbNameSpace)

        # 0=ok, 1=already loaded, others = error
        if returnCode == 0:
            print ("INFO: loaded VHbbNameSpace: %s"%VHbbNameSpace)
        elif returnCode != 1:
            print ("\x1b[31mERROR: loading VHbbNameSpace failed with code %d\x1b[0m"%returnCode)

        self.region = region
        self.anaTag = config.get("Analysis", "tag")
        if self.anaTag not in ['7TeV', '8TeV', '13TeV']:
            raise Exception("anaTag %s unknown. Specify 8TeV or 7TeV or 13TeV in the general config"%self.anaTag)
        # Directories:
        self.Wdir = config.get('Directories', 'Wdir')
        self.vhbbpath = config.get('Directories', 'vhbbpath')
        self.path = config.get('Directories', 'dcSamples')
        self.cachedPath = self.config.get('Directories', 'tmpSamples')
        self.tmpPath = self.config.get('Directories', 'scratch')
        self.outpath = config.get('Directories', 'limits')
        self.optimisation = "" #TODO: opts.optimisation
        self.optimisation_training = False
        try:
            self.UseTrainSample = eval(config.get('Analysis', 'UseTrainSample'))
        except:
            self.UseTrainSample = False
        if self.UseTrainSample:
            print ('Training events will be used')
        if not self.optimisation == '':
            print ('Preparing DC for BDT optimisaiton')
            self.optimisation_training = True
        if self.verbose:
            print ('optimisation is', self.optimisation)
        try:
            os.stat(self.outpath)
        except:
            os.mkdir(self.outpath)
        self.produceTextFiles = eval(self.config.get('Datacard', 'produceTextFiles')) if self.config.has_option('Datacard', 'produceTextFiles') else True

        # parse histogram config:
        self.treevar = config.get('dc:%s'%self.region, 'var')
        if self.verbose:
            print ('treevar is', self.treevar)
        self.name = config.get('dc:%s'%self.region, 'wsVarName') if config.has_option('dc:%s'%self.region, 'wsVarName') else self.region
        if self.optimisation_training:
            self.treevar = self.optimisation + '.Nominal'
            self.name += '_' + self.optimisation
            if self.UseTrainSample:
                self.name += '_Train'
        if self.verbose:
            print ('again, treevar is', self.treevar)

        # set binning
        self.binning = {
                'nBinsX': 15, 
                'minX': 0.0,
                'maxX': 1.0, 
                'rebin_method': (config.get('dc:%s'%self.region,'rebin_method') if config.has_option('dc:%s'%self.region, 'rebin_method') else 'no'),
                'rebin_list': (eval(config.get('dc:%s'%self.region,'rebin_list')) if config.has_option('dc:%s'%self.region, 'rebin_list') else []),
                }
        print("INFO: bin list:", self.binning['rebin_list'])
        if self.config.has_option('dc:%s'%self.region, 'range'):
            self.binning['nBinsX'] = int(self.config.get('dc:%s'%self.region, 'range').split(',')[0])
            self.binning['minX']   = float(self.config.get('dc:%s'%self.region, 'range').split(',')[1])
            self.binning['maxX']   = float(self.config.get('dc:%s'%self.region, 'range').split(',')[2])

        self.variableBins = None
        if self.verbose:
            print ("DEBUG: binning is ", self.binning)
        self.ROOToutname = config.get('dc:%s'%self.region, 'dcName') if config.has_option('dc:%s'%self.region, 'dcName') else self.region
        if self.optimisation_training:
           self.ROOToutname += self.optimisation
           if self.UseTrainSample:
               self.ROOToutname += '_Train'
        self.RCut = config.get('dc:%s'%self.region, 'cut') if config.has_option('dc:%s'%self.region, 'cut') else self.region
        self.signals = eval('['+config.get('dc:%s'%self.region, 'signal')+']') #TODO
        self.Datacardbin = config.get('dc:%s'%self.region, 'dcBin') if config.has_option('dc:%s'%self.region, 'dcBin') else self.region
        self.anType = config.get('dc:%s'%self.region, 'type')
        self.EvalCut = config.get('Cuts', 'EvalCut')

        # blinding
        self.configSection = 'dc:%s'%self.region
        self.blindCut = None
        if config.has_option(self.configSection, 'blindCuts'):
            self.blindCut = eval(config.get(self.configSection, 'blindCuts'))
        if self.verbose:
            print("\x1b[41m\x1b[97mblind cut:", self.blindCut,"\x1b[0m")

        self.keep_branches = eval(config.get('Branches', 'keep_branches'))

        #Systematics:
        if config.has_option('LimitGeneral', 'addSample_sys'):
            self.addSample_sys = eval(config.get('LimitGeneral','addSample_sys'))
            self.additionals = [self.addSample_sys[key] for key in self.addSample_sys]
        else:
            self.addSample_sys = None
            self.additionals = []

        #TODO: move to config!
        analysisSystematics = {
                'bdt': 'sys_BDT',
                'mjj': 'sys_Mjj',
                'cr': 'sys_cr',
                }
        if self.anType.lower() in analysisSystematics:
            self.systematics = eval(config.get('LimitGeneral', analysisSystematics[self.anType.lower()]))
        else:
            print ("\x1b[31mEXIT: please specify if your datacards are BDT, Mjj or cr.\x1b[0m")
            raise Exception("InvalidDatacardSystematicsType")

        if systematics is not None:
            if self.debug:
                print("DEBUG: overwrite systematics list to:", systematics)
            self.systematics = systematics

        self.sysOptions = {}
        # define the options read directly from the config
        sysOptionNames = ['sys_cut_suffix', 'sys_weight_corr', 'decorrelate_sys_weight', 'sys_cut_include', 'sys_factor', 'sys_affecting', 'sys_lhe_affecting', 'rescaleSqrtN', 'toy', 'blind', 
                'addBlindingCut', 'change_shapes', 'Group', 'Dict', 'binstat', 'binstat_cr', 'rebin_active', 'ignore_stats', 'signal_inject', 'add_signal_as_bkg', 'systematicsnaming', 'weightF_sys',
                'sample_sys_info', 'addSample_sys', 'removeWeightSystematics', 'ptRegionsDict', 'setup', 'setupSignals', 'reshapeBins', 'sys_cut_dict', 'sys_cut_dict_per_syst', 'useMinmaxCuts', 'sys_cut_replacement_final',
                'normalizeShapes'
                ]
        for sysOptionName in sysOptionNames:
            self.sysOptions[sysOptionName] = eval(config.get('LimitGeneral', sysOptionName)) if config.has_option('LimitGeneral', sysOptionName) else None
            if self.debug:
                print (" > \x1b[34m{name}\x1b[0m:{value}".format(name=sysOptionName.ljust(40), value=self.sysOptions[sysOptionName]))

        # read weights
        self.weightF = config.get('Weights', 'weightF')
        self.SBweight = None
        if self.verbose:
            print('before adding SBweight, weightF is', self.weightF)
        if self.anType.lower() == 'mjj':
            print ('Passed mJJ')
            if config.has_option('dc:%s'%self.region, 'SBweight'):
                print ('passed config')
                self.SBweight = config.get('dc:%s'%self.region, 'SBweight')
                self.weightF ='('+self.weightF+')*('+self.SBweight+')'
                print ('after adding SBweight, weightF is', self.weightF)
            else:
                print ('NOT Passed config')

        self.treecut = config.get('Cuts', self.RCut)

        # checks on read options
        #on control region cr never blind. Overwrite whatever is in the config
        if self.anType.lower() == 'cr':
            if self.sysOptions['blind'] and self.verbose:
                print ('@WARNING: Changing blind to false since you are running for control region.')
            self.sysOptions['blind'] = False
            
            # binstat_cr can be used to disable BBB in CR
            if self.sysOptions['binstat_cr'] is not None:
                self.sysOptions['binstat'] = self.sysOptions['binstat_cr']
        if self.verbose:
            print("INFO: bin-by-bin:", self.sysOptions['binstat'])

        if self.sysOptions['blind'] and self.verbose:
            print('\x1b[31mI AM BLINDED!\x1b[0m')
        
        # new behavior: rebin_method can be set to 'legacy' per region to restore HIG16044 style rebinning
        # old behavior: global option rebin_active was set to True/False in config, and for CR's changed to False here
        #if self.anType.lower() != 'bdt':
        #    if self.sysOptions['rebin_active']:
        #        print ('@WARNING: Changing rebin_active to false since you are running for control region.')
        #    self.sysOptions['rebin_active'] = False

        if self.sysOptions['add_signal_as_bkg']:
            self.sysOptions['setup'].append(self.sysOptions['add_signal_as_bkg'])

        #Assign Pt region for sys factors
        if self.verbose:
            print ('Assign Pt region for sys factors')
            print ('================================\n')

        if self.sysOptions['ptRegionsDict']:
            self.ptRegion = [ptRegion for ptRegion, outputNames in self.sysOptions['ptRegionsDict'].iteritems() if len([x for x in outputNames if x.upper() in self.ROOToutname.upper()])>0]
            if len(self.ptRegion) != 1:
                if self.verbose:
                    print("INFO: invalid pt region:", self.ptRegion, ", use default.")
                self.ptRegion = None
            else:
                self.ptRegion = self.ptRegion[0]
        else:
            self.ptRegion = None

        if self.verbose:
            print ("\x1b[33mptRegion:\x1b[0m", self.ptRegion)

        for outputName, removeSystematics in self.sysOptions['removeWeightSystematics'].iteritems():
            if outputName in self.ROOToutname:
                self.sysOptions['weightF_sys'] = [x for x in self.sysOptions['weightF_sys'] if x not in removeSystematics]

        #systematics up/down
        self.UD = ['Up', 'Down']

        if self.debug:
            print ('Parse the sample information')
            print ('============================\n')
        #Parse samples configuration
        self.samplesInfo = ParseInfo(samples_path=self.path, config=self.config)

        if self.debug:
            print ('Get the sample list')
            print ('===================\n')
        self.backgrounds = eval(config.get('dc:%s'%self.region, 'background'))
        self.signals = eval(config.get('dc:%s'%self.region, 'signal'))
        self.data_sample_names = eval(config.get('dc:%s'%self.region, 'data'))

        #sample systematics:
        if self.sysOptions['addSample_sys']: 
            self.additionals = [self.sysOptions['addSample_sys'][key] for key in self.sysOptions['addSample_sys']]
        else:
            self.additionals = []

        if self.sysOptions['sample_sys_info']:
            self.sample_sys_list = []#List of all the samples used for the sys. Those samples need to be skiped, except for corresponding sys
            #Extract list of sys samples
            for key, item in self.sysOptions['sample_sys_info'].iteritems():
                for item2 in item:
                    for sample_type in item2:
                        NOMsamplesys = sample_type[0]
                        noNom = False
                        for nomsample in NOMsamplesys: #This is for mergesyscachingdcsplit. Doesn't add the sys if nom is not present
                            if self.debug:
                                print ('nomsample is', nomsample)
                                print ('signals+backgrounds are', self.signals+self.backgrounds)
                            if nomsample not in self.signals+self.backgrounds: noNom = True
                        if noNom: continue
                        DOWNsamplesys = sample_type[1]
                        UPsamplesys = sample_type[2]
                        self.sample_sys_list += DOWNsamplesys
                        self.sample_sys_list += UPsamplesys
        else:
            self.sample_sys_list = None
        #Create dictonary to "turn of" all the sample systematic (for nominal)
        self.sample_sys_dic = {}
        if self.sample_sys_list:
            for sample_sys in self.sample_sys_list:
                self.sample_sys_dic[sample_sys] = False
        if self.debug:
            print("\x1b[34msample_sys_list\x1b[0m =", self.sample_sys_list)

        self.samples = {
                'SIG': self.samplesInfo.get_samples(self.signals),
                'BKG': self.samplesInfo.get_samples(self.backgrounds),
                'DATA': self.samplesInfo.get_samples(self.data_sample_names),
                'ADD': self.samplesInfo.get_samples(self.additionals),
                }

        if self.debug:
            print ('sample list')
            print ('===================\n')
            print (json.dumps(self.samples, sort_keys=True, indent=8, default=str))

        if self.debug:
            print ('systematics')
            print ('===================\n')
            print (json.dumps(self.sysOptions['sys_affecting'], sort_keys=True, indent=8, default=str))

        # define the nominal
        self.systematicsDictionaryNominal = {
                # 'cut': real cut for this systematic variation
                'cut': self.treecut,
                'cachecut': self.treecut,
                'var': self.treevar,
                'name': self.name,
                'systematicsName': 'nominal',
                'binning': self.binning,
                'weight': self.weightF,
                'countHisto': None,
                'countbin': 0,
                'blind': self.sysOptions['blind'],
                'sysType': 'nominal',
                'SBweight': self.SBweight,
                'sample_sys_dic': self.sample_sys_dic,
                }
        
        # contains all systematicDictionaries, first entry will be nominal
        self.systematicsList = [self.systematicsDictionaryNominal]

        # MC stats
        mcStatsDict = deepcopy(self.systematicsDictionaryNominal)
        mcStatsDict['sysType'] = 'unweighted'
        mcStatsDict['systematicsName'] = 'unweighted'
        self.systematicsList.append(mcStatsDict)
        
        # Sumw2
        mcStatsDict = deepcopy(self.systematicsDictionaryNominal)
        mcStatsDict['sysType'] = 'sumw2'
        mcStatsDict['systematicsName'] = 'sumw2'
        self.systematicsList.append(mcStatsDict)

        if self.verbose or self.debug:
            print ('Assign the systematics')
            print ('======================\n')

        # shape systematics
        for syst in self.systematics:
            for Q in self.UD:
                systematicsDictionary = deepcopy(self.systematicsDictionaryNominal)
                systematicsDictionary.update({
                        'cut': self.getSystematicsCut(syst, Q),
                        # 'cachecut': looser cut, which is the same for many of the systematics and therefore reduces number of unique cuts
                        #'cachecut': self.getSystematicsCut('minmax', Q) if self.sysOptions['useMinmaxCuts'] else self.getSystematicsCut(syst, Q),
                        'cachecut': self.getSystematicsCut(syst, Q),
                        'var': self.getSystematicsVar(syst, Q),
                        'weight': self.getSystematicsWeight(syst, Q),
                        'sysType': 'shape',
                        'systematicsName': '{sysName}_{Q}'.format(sysName=self.sysOptions['systematicsnaming'][syst] if syst in self.sysOptions['systematicsnaming'] else syst, Q=Q) 
                    })
                self.systematicsList.append(systematicsDictionary)
        
        # weight systematics
        for weightF_sys in self.sysOptions['weightF_sys']:
            for Q in self.UD:
                # to keep compatiblity with legacy analysis where naming was uppercase for weight systematics
                # look for *_Up first and then for *_UP if it does not exist
                weightNames = ['%s_%s'%(weightF_sys, x) for x in [Q, Q.upper()]]
                try:
                    weight = next(iter([self.config.get('Weights', x) for x in weightNames if self.config.has_option('Weights', x)]))
                except Exception as e:

                    match = False
                    if self.config.has_option('Weights', 'regex'):
                        regex = eval(self.config.get('Weights', 'regex'))
                        for findString,replaceString in regex:
                            for x in weightNames:
                                if re.match(findString, x):
                                    weight = re.sub(findString, replaceString, x)
                                    match = True
                    if match:
                        if self.debug:
                            print('DEBUG: matched ', weightF_sys, ' ---> ', weight)

                    else:
                        print('\x1b[31mERROR: could not find weight fot weight_sys:', weightF_sys, x, " check general.ini!\x1b[0m")
                        print('DEBUG: general.ini > [Weights] > (one of) ', weightNames)
                        raise e

                systematicsDictionary = deepcopy(self.systematicsDictionaryNominal)
                systematicsDictionary.update({
                        'sysType': 'weight',
                        'weight': weight if self.SBweight == None else '('+weight+')*('+self.SBweight+')', 
                        'name': weightF_sys,
                        'systematicsName': '{sysName}_{Q}'.format(sysName=self.sysOptions['systematicsnaming'][weightF_sys] if weightF_sys in self.sysOptions['systematicsnaming'] else weightF_sys, Q=Q) 
                    })
                self.systematicsList.append(systematicsDictionary)

        # sample systematics
        if self.sysOptions['sample_sys_info']:
            for sampleSystematicName, sampleSystematicSamples in self.sysOptions['sample_sys_info'].iteritems(): #loop over the systematics
                for Q in self.UD:
                    systematicsDictionary = deepcopy(self.systematicsDictionaryNominal)
                    systematicsDictionary.update({
                            'sysType': 'sample',
                            'samples': sampleSystematicSamples, 
                            'name': sampleSystematicName,
                            'systematicsName': '{sysName}_{Q}'.format(sysName=self.sysOptions['systematicsnaming'][sampleSystematicName], Q=Q) 
                        })
                    # loop over list of sample per systematic e.g.: ggZH, ZH. Note: sample sys assumed to be correlated among the samples
                    for sampleSystematicSample in sampleSystematicSamples:
                        for sample_type in sampleSystematicSample:
                            sampleSystematicVariationTypes = {
                                    0: False,          # nominal
                                    1: (Q == 'Down'),  # down variation
                                    2: (Q == 'Up'),    # up variation
                                }
                            # mark nominal/up/down variations in sample_sys_dic
                            for index, value in sampleSystematicVariationTypes.iteritems():
                                for sampleName in sample_type[index]:
                                    systematicsDictionary['sample_sys_dic'][sampleName] = value

                    self.systematicsList.append(systematicsDictionary)
        
        if self.debug:
            print ('systematics dict')
            print ('===================\n')

            # make list of differences compared to nominal
            systematicsListDelta = [self.systematicsList[0]]
            for i in range(1,len(self.systematicsList)):
                delta = {k:v for k,v in self.systematicsList[i].iteritems() if systematicsListDelta[0][k] != v}
                systematicsListDelta.append(delta)
            print (json.dumps(systematicsListDelta, sort_keys=True, indent=8, default=str))
        
        if self.debug or self.verbose:
            print('INFO: datacard initialization complete!')
            print('INFO: {nSys} systematics for {nSamples} samples'.format(nSys=len(self.systematicsList), nSamples=sum([len(x) for k,x in self.samples.iteritems()])))
        

    def calcBinning(self):

        if self.binning['rebin_method'] in ['fixed', 'list'] and len(self.binning['rebin_list']) > 0:
            self.variableBins = array.array('d',self.binning['rebin_list'])
        elif self.binning['rebin_method'] == 'legacy':
            # below is the old method, that was used for 2016 Heppy analysis
            temporaryBins = 1000
            targetBins = self.binning['nBinsX'] 
            tolerance = 0.35
            samples = self.samples['BKG'] 
            totalBG = None

            # make a histogramm with entries of ALL BKG samples
            for i, sample in enumerate(samples): 
                print("INFO: Add BKG sample ", i, " of ", len(samples))
                # get sample tree from cache
                tc = TreeCache.TreeCache(
                        sample=sample,
                        cutList=self.getCacheCut(sample),
                        inputFolder=self.path,
                        config=self.config,
                        debug=False,
                        fileLocator=self.fileLocator
                    )
                if not tc.isCached():
                    print("\x1b[31m:ERROR not cached! run cachedc step again\x1b[0m")
                    raise Exception("NotCached")
                sampleTree = tc.getTree()
                systematics = self.systematicsList[0] # nominal TODO
                histogramOptions = {
                                'rebin': 1,
                                'weight': systematics['weight'],
                                'treeVar': systematics['var'],
                                'uniqueid': True,
                                'nBinsX': temporaryBins,
                                'minX': self.binning['minX'],
                                'maxX': self.binning['maxX'],
                            }
                # get histogram for this sample and add it to histogram for BKG
                histoMaker = HistoMaker(self.config, sample=sample, sampleTree=sampleTree, histogramOptions=histogramOptions)
                if not totalBG:
                    totalBG = histoMaker.getHistogram(systematics['cut']).Clone()
                else:
                    totalBG.Add(histoMaker.getHistogram(systematics['cut']))
            # OLD REBINNER
            ErrorR=0
            ErrorL=0
            TotR=0
            TotL=0
            binR=temporaryBins
            binL=1
            rel=1.0
            if self.verbose:
                print ("START loop from right")
            #print "totalBG.Draw("","")",totalBG.Integral()
            #---- from right
            while rel > tolerance :
                TotR+=totalBG.GetBinContent(binR)
                ErrorR=sqrt(ErrorR**2+totalBG.GetBinError(binR)**2)
                binR-=1
                if binR < 0: break
                if TotR < 1.: continue
                if self.verbose:
                    print ('binR is', binR)
                    print ('TotR is', TotR)
                    print ('ErrorR is', ErrorR)
                if not TotR <= 0 and not ErrorR == 0:
                    rel=ErrorR/TotR
                    if self.verbose:
                        print ('rel is',  rel)
            if self.verbose:
                print ('upper bin is %s'%binR)
                print ("END loop from right")

            #---- from left

            rel=1.0
            if self.verbose:
                print ("START loop from left")
            while rel > tolerance:
                TotL+=totalBG.GetBinContent(binL)
                ErrorL=sqrt(ErrorL**2+totalBG.GetBinError(binL)**2)
                binL+=1
                if binL > temporaryBins: break
                if TotL < 1.: continue
                if not TotL <= 0 and not ErrorL == 0:
                    rel=ErrorL/TotL
                    print (rel)
            #it's the lower edge
            binL+=1
            if self.verbose:
                print ("STOP loop from left")
                print ('lower bin is %s'%binL)

            inbetween=binR-binL
            stepsize=int(inbetween)/(targetBins-2)
            modulo = int(inbetween)%(targetBins-2)

            if self.verbose:
                print ('stepsize %s'% stepsize)
                print ('modulo %s'%modulo)
            binlist=[binL]
            for i in range(0,targetBins-3):
                binlist.append(binlist[-1]+stepsize)
            binlist.append(binR)
            # add remainder to the last bin lower edge, to have equal sized bins (except first bin and the last one, which is larger anyway)
            binlist[-1]+=modulo
            binlist.append(temporaryBins+1)
            if self.verbose:
                print ('binning set to %s'%binlist)

            # TODO !!!! TODO !!!
            self.variableBins = array.array('d',sorted([self.binning['minX']]+[totalBG.GetBinLowEdge(i) for i in binlist]))

        if self.verbose:
            print("INFO: new bins boundaries:", self.variableBins)

    def getSystematicsList(self, isData=False):
        if isData:
            return [x for x in self.systematicsList if x['sysType'] == 'nominal']
        else:
            return self.systematicsList

    def getRegion(self):
        return self.region

    # return tree variable as string
    def getSystematicsVar(self, syst, Q):
        treevar = self.treevar
        #replace tree variable
        if self.anType.lower() in ['bdt', 'dnn']:
            if not 'UD' in syst:
                if self.debug:
                    print ('treevar was', treevar)
                    print ('.nominal by', '.%s_%s'%(syst, Q))
                treevar = treevar.replace('.Nominal','.%s_%s'%(syst, Q)).replace('.nominal','.%s_%s'%(syst, Q))
            else:
                treevar = treevar.replace('.Nominal','.%s'%(syst.replace('UD', Q))).replace('.nominal','.%s'%(syst.replace('UD', Q)))
                if self.debug:
                    print ('.nominal by', '.%s'%(syst.replace('UD', Q)))
        elif self.anType.lower() == 'mjj':
            if not 'UD' in syst:
                if self.debug:
                    print ('treevar was', treevar)
                    print ('_reg_mass', '_reg_mass_corr%s%s'%(syst, Q))
                treevar = treevar.replace('_reg_mass', '_reg_mass_corr%s%s'%(syst, Q))
            else:
                print ('\x1b[31m@ERROR: Why is there UD in sys ? Abort\x1b[0m')
                raise Exception("DcSystMjjContainsUD")
        return treevar 

    # return weight as string
    def getSystematicsWeight(self, syst, Q):
        weight = self.weightF
        if syst in self.sysOptions['sys_weight_corr']:
            weightName = '{sysWeightCorr}_{ud}'.format(sysWeightCorr=self.sysOptions['sys_weight_corr'][syst], ud=Q.upper())
            weight = self.config.get('Weights', weightName)
            print ('weightName is \x1b[34m{weightName}\x1b[0m'.format(weightName=weightName))
            print ('weight is \x1b[34m{weight}\x1b[0m'.format(weight=weight))
        return weight

    def getReplacementRulesList(self, syst):
        return self.sysOptions['sys_cut_suffix'][syst] if isinstance(self.sysOptions['sys_cut_suffix'][syst], list) else [self.sysOptions['sys_cut_suffix'][syst]]

    # return cut for systematics variation as string
    def getSystematicsCut(self, syst, Q):
        replacementRulesList = XbbTools.getReplacementRulesList(self.config, syst)
        cut = XbbTools.getSystematicsVariationTemplate(self.treecut, replacementRulesList)
        cut = cut.replace('{syst}', syst).replace('{UD}', Q)
        return cut

    # return full (flattened) list of sample objects
    def getAllSamples(self):
        return sum([y for x, y in self.samples.iteritems()], []) 

    # if checkExistenc=False, returns number of files which should be present, if checkExistenc=True counts how many of them actually exist
    def getNumberOfCachedFiles(self, useSampleIdentifiers=None, checkExistence=True):
        nFiles = -1
        allSamples = self.getAllSamples()
        if type(useSampleIdentifiers) == str:
            useSampleIdentifiers = [useSampleIdentifiers]
        if useSampleIdentifiers:
            allSamples = [sample for sample in allSamples if sample.identifier in useSampleIdentifiers]
        cacheStatus = {}
        for i, sample in enumerate(allSamples):
            # get cuts that were used in caching for this sample
            sampleCuts = self.getCacheCut(sample) 

            # get sample tree from cache
            tc = TreeCache.TreeCache(
                    sample=sample,
                    cutList=sampleCuts,
                    inputFolder=self.path,
                    config=self.config,
                    debug=self.debug,
                    fileLocator=self.fileLocator
                )

            if checkExistence:
                # check if fiels are complete
                if not tc.isCached():
                    return -1
                if nFiles == -1:
                    nFiles = len(tc.cachedFileNames)
                else:
                    # if one of the subsamples has a different number of files, this indicates an error
                    if nFiles != len(tc.cachedFileNames):
                        print("nF:", nFiles)
                        print("nC:", len(tc.cachedFileNames))
                        print("C:", tc.cachedFileNames)
                        print('ERROR: subsample incomplete, this should not happen!!')
                        return -1
            else:
                # return number of files whether they exist or not
                return tc.getTotalNumberOfOutputFiles()

        return nFiles 

    def getCacheStatus(self, useSampleIdentifiers=None):
        allSamples = self.getAllSamples()
        if useSampleIdentifiers:
            allSamples = [sample for sample in allSamples if sample.identifier in useSampleIdentifiers]
        cacheStatus = {}
        for i, sample in enumerate(allSamples):
            # get cuts that were used in caching for this sample
            sampleCuts = self.getCacheCut(sample) 

            # get sample tree from cache
            tc = TreeCache.TreeCache(
                    sample=sample,
                    cutList=sampleCuts,
                    inputFolder=self.path,
                    config=self.config,
                    debug=self.debug,
                    fileLocator=self.fileLocator
                )
            cacheStatus[sample.name] = tc.isCached()
        return cacheStatus

    # get a little looser cut, which is the same for all systematics
    def getCacheCut(self, sample):
        systematicsCuts = sorted(list(set([x['cachecut'] for x in self.getSystematicsList(isData=sample.isData())])))
        # nominal cut is still the original one, to ensure all nominal events are kept if approximations are used for systematics
        # therefore the list systematicsCuts also contains the nominal cut string
        sampleCuts = {'AND': [sample.subcut, {'OR': systematicsCuts}]}
        return sampleCuts

    def getUniqueHistogramName(self, sampleName, systName):
        histogramName = "{sampleName}_{systName}_c{counter}".format(sampleName=sampleName, systName=systName, counter=self.histogramCounter)
        self.histogramCounter += 1
        return histogramName

    def run(self, useSampleIdentifiers=None, chunkNumber=-1):
        
        # compute bin boundaries/read the mfrom config if given
        self.calcBinning()

        # select samples to use
        allSamples = self.getAllSamples()
        if useSampleIdentifiers:
            allSamples = [sample for sample in allSamples if sample.identifier in useSampleIdentifiers] 

        usedSamplesString = ''
        if useSampleIdentifiers:
            usedSamplesString = ('_'.join(sorted(list(set([sample.identifier for sample in allSamples])))))

        if len(allSamples) < 1:
            print("INFO: all:", [x.name for x in self.getAllSamples()])
            print("USE:", useSampleIdentifiers)
            print("INFO: no samples, nothing to do.")
            return None

        print ('\n\t...fetching histos...\n')

        self.histograms = {}

        # each sample group corresponds to a datacard process
        sampleGroups = list(set([self.getSampleGroup(sample) for sample in allSamples]))
        if self.debug:
            print("DEBUG: sample group ---> datacard process")
            for sampleGroup in sampleGroups:
                print("DEBUG: ", sampleGroup, "--->", self.getProcessName(sampleGroup))

        # loop over all processes (for each process there is 1:1 a 'sampleGroup' defined) 
        # read cached sample trees: for every sample there is one SampleTree, which contains the events needed for ALL the systematics
        # use this sample tree with appropriate cuts for each systematics to fill the histograms
        for i,sampleGroup in enumerate(sampleGroups):

            samplesInGroup = [sample for sample in allSamples if self.getSampleGroup(sample) == sampleGroup]

            if self.debug: 
                print("DEBUG: sample group", sampleGroup, " (",(i+1),"/",len(sampleGroups),")")
                print("DEBUG: consists of samples:")
                for x in samplesInGroup:
                    print("DEBUG: > %s (%s)"%(x.name, x.identifier))

            sampleHistogramName = sampleGroup
            self.histograms[sampleHistogramName] = {}

            for sample in samplesInGroup:
                # get cuts that were used in caching for this sample
                sampleCuts = self.getCacheCut(sample)

                # get sample tree from cache
                tc = TreeCache.TreeCache(
                        sample=sample,
                        cutList=sampleCuts,
                        inputFolder=self.path,
                        config=self.config,
                        debug=True,
                        fileLocator=self.fileLocator
                    )

                if not tc.isCached():
                    print("\x1b[31mERROR not cached! run cachedc step again\x1b[0m")
                    print (json.dumps(sampleCuts, sort_keys=True, indent=4, default=str))
                    raise Exception("NotCached")

                chunkSize = self.getChunkSize(sample.identifier) if chunkNumber > 0 else -1
                sampleTree = tc.getTree(chunkSize, chunkNumber)

                systematicsList = self.getSystematicsList(isData=sample.isData())

                # add all the cuts/weights for the different systematics 
                evalcutInfoShown = False
                for systematics in systematicsList:
                    
                    # 'decorrelate_sys_weight' in datacards.ini can be used to enable weight systematics for specific samples only
                    # and even don't compute the histograms in this case (because e.g. branches missing)
                    # (this is different from the 'affecting' option, which only modifies the textfile but always creates histograms)
                    systematics['enabled'] = True
                    if systematics['sysType'] == 'weight' and systematics['name'] in self.sysOptions['decorrelate_sys_weight']:
                        #if self.sysOptions['Group'][sample.name] not in self.sysOptions['decorrelate_sys_weight'][systematics['name']]:
                        groupName = self.getSampleGroup(sample)
                        if groupName not in self.sysOptions['decorrelate_sys_weight'][systematics['name']]:
                            if self.debug:
                                print('\x1b[31m group', groupName, 'is not in', self.sysOptions['decorrelate_sys_weight'][systematics['name']], '==> disable\x1b[0m')
                            systematics['enabled'] = False
                    
                    # additional BLINDING cut
                    if self.sysOptions['addBlindingCut']:
                        systematics['cutWithBlinding'] = '({cut})&&({blindingCut})'.format(cut=systematics['cut'], blindingCut=self.sysOptions['addBlindingCut'])
                    else:
                        systematics['cutWithBlinding'] = systematics['cut']

                    # prepare histograms (only for the first sample in the group)
                    if systematics['systematicsName'] not in self.histograms[sampleHistogramName]:
                        histogramName = self.getUniqueHistogramName(sampleHistogramName, systematics['systematicsName'])
                        self.histograms[sampleHistogramName][systematics['systematicsName']] = ROOT.TH1F(histogramName, histogramName, len(self.variableBins)-1, self.variableBins) if self.variableBins else ROOT.TH1F(histogramName, histogramName, self.binning['nBinsX'], self.binning['minX'], self.binning['maxX'])
                        self.histograms[sampleHistogramName][systematics['systematicsName']].Sumw2()

                    # if BDT variables are plotted (signal region!) exclude samples used for training and rescale by 2
                    if (self.anType.lower() in ['bdt','dnn'] or 'bdt' in systematics['var'].lower() or 'dnn' in systematics['var'].lower()) and not sample.isData():
                        systematics['addCut'] = self.EvalCut
                        systematics['mcRescale'] = self.defaultMcRescaleMVA
                        sampleTree.addFormula(systematics['addCut'], systematics['addCut'])
                        if self.debug and not evalcutInfoShown:
                            print('\x1b[31mDEBUG: using 50% of sample not used in training:', self.EvalCut, '\x1b[0m')
                            evalcutInfoShown = True
                    else:
                        if self.debug:
                            if sample.isData():
                                print('\x1b[31mDEBUG: using full sample since it is DATA!',systematics['var'].lower(), "\x1b[0m")
                            else:
                                print('\x1b[31mDEBUG: using full sample for sample of type', sample.type, 'for', systematics['var'].lower(), "\x1b[0m")

                    # add shape cut
                    if self.config.has_option('Cuts', 'additionalShapeCut'):
                        if 'addCut' in systematics and  systematics['addCut'] is not None:
                            systematics['addCut'] = "(" + systematics['addCut'] + ")&&(" + self.config.get('Cuts','additionalShapeCut')  + ")"
                        else:
                            systematics['addCut'] = "(" + self.config.get('Cuts','additionalShapeCut')  + ")"
                        sampleTree.addFormula(systematics['addCut'])
                        print("\x1b[31mINFO: additional cut active for making shapes:", self.config.get('Cuts','additionalShapeCut'), "\x1b[0m")

                    # add TTreeFormulas
                    systematics['cutWithBlinding'] = systematics['cutWithBlinding'].replace(' ', '')

                    if systematics['enabled']:
                        sampleTree.addFormula(systematics['cutWithBlinding'])
                        if not sample.isData():
                            sampleTree.addFormula(systematics['weight'], systematics['weight'])
                        sampleTree.addFormula(systematics['var'], systematics['var'])

                # sample scale factor, to match to cross section
                sampleScaleFactor = sampleTree.getScale(sample) if not sample.isData() else 1.0

                # get used branches, which are either used in cut, weight or the variable itself
                usedBranchList = BranchList()
                for systematics in systematicsList:
                    usedBranchList.addCut(systematics['cutWithBlinding'])
                    if not sample.isData():
                        usedBranchList.addCut(systematics['weight'])
                    usedBranchList.addCut(systematics['var'])
                    if 'addCut' in systematics:
                        usedBranchList.addCut(systematics['addCut'])

                # per sample special weight which is read from the config instead of the .root files 
                useSpecialweight = False
                if self.config.has_option('Weights', 'useSpecialWeight') and eval(self.config.get('Weights', 'useSpecialWeight')):
                    useSpecialweight = True
                    sampleTree.addFormula('specialweight', sample.specialweight)
                    usedBranchList.addCut(sample.specialweight)
                    print("INFO: use specialweight: {specialweight}".format(specialweight=sample.specialweight))
                else:
                    print("INFO: don't use specialweight, weight:", systematicsList[0]['weight'])

                # enable only used branches
                usedBranchList.addCut(['evt','run','isData','event'])
                listOfBranchesToKeep = usedBranchList.getListOfBranches()
                sampleTree.enableBranches(listOfBranchesToKeep)
                print("DEBUG: branches enabled!")

                # loop over all events in this sample
                weight = 1.0
                specialweight = 1.0
                sampleTree.Print()

                for event in sampleTree:

                    # evaluate all systematics for this event
                    for systematics in systematicsList:
                        cutPassed = sampleTree.evaluate(systematics['cutWithBlinding']) if systematics['enabled'] else False
                        if cutPassed:
                            if 'addCut' in systematics:
                                cutPassed = cutPassed and sampleTree.evaluate(systematics['addCut'])
                            if cutPassed:
                                weight = sampleTree.evaluate(systematics['weight']) if not sample.isData() else 1.0
                                treeVar = sampleTree.evaluate(systematics['var'])
                                specialweight = sampleTree.evaluate('specialweight') if useSpecialweight else 1.0
                                if systematics['sysType'] == 'unweighted':
                                    self.histograms[sampleHistogramName][systematics['systematicsName']].Fill(treeVar)
                                elif systematics['sysType'] == 'sumw2':
                                    self.histograms[sampleHistogramName][systematics['systematicsName']].Fill(treeVar, (weight * specialweight * sampleScaleFactor)**2)
                                else:
                                    self.histograms[sampleHistogramName][systematics['systematicsName']].Fill(treeVar, weight * specialweight * sampleScaleFactor)

                if not sampleTree.checkProcessingComplete():
                    raise Exception('FileReadIncomplete')
                else:
                    print('INFO: sampleTree TChain: all files have been processed.')


            # if histogram is empty, fill it with 0 to avoid having histograms with 0 entries
            for systematics in systematicsList:
                if self.histograms[sampleHistogramName][systematics['systematicsName']].GetEntries() < 1:
                    if self.debug:
                        print("INFO: ",systematics['systematicsName'], "histogram had 0 entries! => filled with 0")
                    self.histograms[sampleHistogramName][systematics['systematicsName']].SetEntries(1)
                    for i in range(self.histograms[sampleHistogramName][systematics['systematicsName']].GetXaxis().GetNbins()):
                        self.histograms[sampleHistogramName][systematics['systematicsName']].SetBinContent(1+i, 0)

            # rescale histograms to match cross section and to compensate for cut on MC to not use MVA training samples
            for systematics in systematicsList:
                mcRescale = systematics['mcRescale'] if 'mcRescale' in systematics else 1.0
                self.histograms[sampleHistogramName][systematics['systematicsName']].Scale(mcRescale)

            nominalHist = self.histograms[sampleHistogramName][systematicsList[0]['systematicsName']]
            print("nominal shape:",systematicsList[0]['systematicsName'],nominalHist,"N(MC)=",nominalHist.GetEntries(),"N(weighted)=",nominalHist.Integral())
            nBins = nominalHist.GetXaxis().GetNbins()
            binList = '|'.join([('%d'%(i+1)).ljust(8) for i in range(nBins)])
            binContentList = '|'.join([('%1.2f'%nominalHist.GetBinContent(i+1)).ljust(8) for i in range(nBins)])
            print(binList)
            print(binContentList)

            # normalize up/down variations
            for systematics in systematicsList:
                if systematics['systematicsName'] in self.sysOptions['normalizeShapes']:
                    print("INFO: normalize shape variation to nominal:", systematics['systematicsName'])
                    normNominal = nominalHist.Integral()
                    normVariation = self.histograms[sampleHistogramName][systematics['systematicsName']].Integral()
                    if normVariation > 0:
                        self.histograms[sampleHistogramName][systematics['systematicsName']].Scale(normNominal/normVariation)
                        print("INFO: scaled by", normNominal/normVariation, "=",normNominal,"/",normVariation)

            # force positive shapes
            for systematics in systematicsList:
                if self.histograms[sampleHistogramName][systematics['systematicsName']].Integral() < 0:
                    self.histograms[sampleHistogramName][systematics['systematicsName']].Scale(-0.00001)
                    print("INFO: shape", systematics['systematicsName'], "was negative, forced positive")

        self.writeDatacards(samples=allSamples, dcName=usedSamplesString, chunkSize=chunkSize, chunkNumber=chunkNumber)

        for systematics in systematicsList:
            if 'mcRescale' in systematics and systematics['mcRescale'] != 1.0:
                print("INFO: some samples have been rescaled by \x1b[33m", systematics['mcRescale'], "\x1b[0m!")
                if 'addCut' in systematics:
                    print("INFO: and the additional cuts was:", systematics['addCut'])
                break

    # return sample dependent number of chunks
    def getChunkSize(self, sampleIdentifier):
        if self.config.has_option('Configuration', 'disableShapeChunks') and eval(self.config.get('Configuration', 'disableShapeChunks')):
            return 99999 if self.config.has_option(sampleIdentifier, 'dcChunkSize') else -1
        else:
            return int(self.config.get(sampleIdentifier, 'dcChunkSize')) if self.config.has_option(sampleIdentifier, 'dcChunkSize') else -1

    # number of chunks, -1 if split into chunks is disabled
    def getNumberOfChunks(self, sampleIdentifier, checkExistence=True):
        chunkSize = self.getChunkSize(sampleIdentifier)
        if chunkSize < 1:
            nChunks = -1
        else:
            nFiles = self.getNumberOfCachedFiles(sampleIdentifier, checkExistence=checkExistence)
            nChunks = int(math.ceil(1.0*nFiles/chunkSize))
        return nChunks 

    # if split into chunks is enabled, file name will end in _#.root with # being the chunk number, # starts from 1
    def getShapeFileNames(self, sampleIdentifier):
        nChunks = self.getNumberOfChunks(sampleIdentifier, False)
        if nChunks > 0:
            rootFileNames = [self.getDatacardBaseName(subPartName=sampleIdentifier, chunkNumber=chunkNumber) + '.root' for chunkNumber in range(1, 1+nChunks)]
        else:
            rootFileNames = [self.getDatacardBaseName(subPartName=sampleIdentifier) + '.root']
        return rootFileNames

    def getSampleGroup(self, sample):
        # if Group dictionary is used, prioritize it over group from config
        if sample.name in self.sysOptions['Group']:
            sampleGroup = self.sysOptions['Group'][sample.name]
        else:
            sampleGroup = sample.group
        if len(sampleGroup.strip()) < 1:
            print("\x1b[41m\x1b[37mERROR: sample group not defined for identifier=", sample.identifier, " name=", sample.name, "\x1b[0m")
            raise Exception("ConfigError")
        return sampleGroup
    
    def getSampleGroupFromName(self, sampleName, samples):
        matchingSamples = [x for x in samples if x.name == sampleName]
        if len(matchingSamples) == 1:
            return self.getSampleGroup(matchingSamples[0])
        else:
            print("ERROR: no or multiple samples match '" + sampleName + "'")
            print("DEBUG:", [x.name for x in samples])
            raise Exception("SamplesError")

    # translate the sample group name (Xbb config) to name used for datacards 
    def getProcessName(self, groupName):
        if groupName == 'DATA':
            processName = 'data_obs'
        elif groupName in self.sysOptions['Dict']:
            processName = self.sysOptions['Dict'][groupName]
        else:
            processName = groupName
        if len(processName.strip()) < 1:
            print("\x1b[41m\x1b[37mERROR: process empty for groupName=", groupName, "\x1b[0m")
            raise Exception("ConfigError")
        return processName

    def getGroupNameFromProcessName(self, processName):
        dcProcessSampleGroup = {v: k for k,v in self.sysOptions['Dict'].iteritems()}
        if processName in dcProcessSampleGroup:
            return dcProcessSampleGroup[processName]
        else:
            return processName

    def load(self):
        self.histograms   = {}
        allSamples        = self.getAllSamples()
        sampleIdentifiers = sorted(list(set([sample.identifier for sample in allSamples])))

        for sampleIdentifier in sampleIdentifiers:

            subsamples = [sample for sample in allSamples if sample.identifier == sampleIdentifier]

            if all([x.isData() for x in subsamples]):
                isData = True
            elif all([not x.isData() for x in subsamples]):
                isData = False
            else:
                print("\x1b[31mERROR: subsamples can't be partially data!\x1b[0m")
                raise Exception("ConfigError")

            # all shape .root files of that sample identifier
            rootFileNames = self.getShapeFileNames(sampleIdentifier)
            for rootFileName in rootFileNames:
                print("\x1b[33m", rootFileName, "\x1b[0m")
                rootFile = ROOT.TFile.Open(rootFileName, 'read')
                if not rootFile or rootFile.IsZombie():
                    print ("\x1b[31mERROR: bad root file:", rootFileName, "\x1b[0m")
                    raise Exception("FileIOError")

                # in every ROOT file samples for several groups can be present if split into subsamples
                sampleGroups      = list(set([self.getSampleGroup(sample) for sample in allSamples if sample.identifier==sampleIdentifier]))

                # loop over datacard processes 
                for sampleGroup in sampleGroups:

                    datacardProcess = self.getProcessName(sampleGroup) 

                    systematicsToEvaluate = self.getSystematicsList(isData=isData)
                    for systematics in systematicsToEvaluate:
                        datacardProcessHistogramName = self.getHistogramName(process=datacardProcess, systematics=systematics)
                        histogramPath                = '{folder}/{histogram}'.format(folder=self.Datacardbin, histogram=datacardProcessHistogramName)
                        histogram                    = rootFile.Get(histogramPath)
                        if not histogram:
                            print ("IN:", rootFileName)
                            print ("FILE:", rootFile)
                            print ("LOOKING FOR:", histogramPath)
                            raise Exception("HistogramMissing")

                        if sampleGroup not in self.histograms:
                            self.histograms[sampleGroup] = {}
                        if systematics['systematicsName'] in self.histograms[sampleGroup]:
                            self.histograms[sampleGroup][systematics['systematicsName']].Add(histogram)
                        else:
                            self.histograms[sampleGroup][systematics['systematicsName']] = histogram.Clone()
                            self.histograms[sampleGroup][systematics['systematicsName']].SetDirectory(0)

    def splitFilesExist(self, useSampleIdentifier=None, chunkNumber=-1):
        filesExist = True
        allSamples = self.getAllSamples()
        if useSampleIdentifier:
            sampleIdentifiers = useSampleIdentifier
        else:
            sampleIdentifiers = sorted(list(set([sample.identifier for sample in allSamples])))
        print("DEBUG: check shape file existence:")
        for sampleIdentifier in sampleIdentifiers:
            print("DEBUG: -> sample=", sampleIdentifier)
            subsamples = [sample for sample in allSamples if sample.identifier == sampleIdentifier]
            rootFileName = self.getDatacardBaseName(subPartName=sampleIdentifier, chunkNumber=chunkNumber) + '.root'
            if not self.fileLocator.isValidRootFile(rootFileName):
                print("DEBUG:   -> ERROR:", rootFileName) 
                filesExist = False
                break
            else:
                print("DEBUG:   -> OK:", rootFileName) 
            rootFile = ROOT.TFile.Open(rootFileName, 'read')
            txtFileName = self.getDatacardBaseName(subPartName=sampleIdentifier, chunkNumber=chunkNumber) + '.txt'
            if self.produceTextFiles:
                filesExist = filesExist and os.path.isfile(txtFileName)
        return filesExist

    def getHistogramName(self, process, systematics):
        systematicsName = systematics['systematicsName'] if systematics['sysType'] != 'nominal' else ''

        #TODO: this is ugly, just for now to test!
        systematicsName = systematicsName.replace('_Up','Up')
        systematicsName = systematicsName.replace('_Down','Down')
        systematicsName = systematicsName.replace('_UP','Up')
        systematicsName = systematicsName.replace('_DOWN','Down')
        systematicsName = systematicsName.replace('UP','Up')
        systematicsName = systematicsName.replace('DOWN','Down')
        return '{process}{systematicsName}'.format(process=process, systematicsName=systematicsName)

    def writeDatacards(self, samples=None, dcName='', chunkSize=-1, chunkNumber=-1):

        if not self.histograms:
            print("\x1b[31mERROR: no histograms found, datacard histograms must be either created with run() or loaded with load()\x1b[0m")
            raise Exception("DcHistogramsMissing")

        if samples is None:
            samples = self.getAllSamples()

        # open and prepare histogram output files
        histogramFileName = self.getDatacardBaseName(dcName, ext='.root', chunkNumber=chunkNumber)
        print("INFO: HISTOGRAM: \x1b[34m", histogramFileName, "\x1b[0m")
        try:
            datacardFolder = '/'.join(histogramFileName.split('/')[:-1])
            os.makedirs(datacardFolder)
        except:
            pass

        outfile = ROOT.TFile(histogramFileName, 'RECREATE')
        if not outfile or outfile.IsZombie():
            print("\x1b[31mERROR: unable to open output file", histogramFileName,"\x1b[0m")
            raise Exception("FileIOError")
        rootFileSubdir = outfile.mkdir(self.Datacardbin, self.Datacardbin)

        # sample groups for datacard, all samples of each group will be added in a single column (datacard process)
        sampleGroups = list(set([self.getSampleGroup(sample) for sample in samples]))
        if self.debug:
            print("\x1b[31mDEBUG: groups=", sampleGroups,"\x1b[0m")

        for systematics in self.getSystematicsList(isData=sample.isData()):
            systematics['histograms'] = {}

        for sampleGroup in sampleGroups:
            for systematics in self.getSystematicsList(isData=(sampleGroup == 'DATA')):
                # sum histograms of all samples in the datacard group
                #print ("->",self.sysOptions['Dict'])
                datacardProcess = self.getProcessName(sampleGroup) 
                datacardProcessHistogramName = self.getHistogramName(process=datacardProcess, systematics=systematics)

                # add up all the sample histograms for this process and this systematic
                histogramsInGroup = [h[systematics['systematicsName']] for k, h in self.histograms.iteritems() if k == sampleGroup]

                if len(histogramsInGroup) > 0:
                    systematics['histograms'][sampleGroup] = StackMaker.sumHistograms(histogramsInGroup, datacardProcessHistogramName)
                    if self.sysOptions['reshapeBins']:
                        nB = systematics['histograms'][sampleGroup].GetXaxis().GetNbins()
                        x0 = systematics['histograms'][sampleGroup].GetXaxis().GetBinLowEdge(1)
                        x1 = systematics['histograms'][sampleGroup].GetXaxis().GetBinUpEdge(nB)
                        th = ROOT.TH1F(systematics['histograms'][sampleGroup].GetName(),systematics['histograms'][sampleGroup].GetTitle(),nB,x0,x1)
                        th.Sumw2()
                        for i in range(nB):
                            th.SetBinContent(1+i,systematics['histograms'][sampleGroup].GetBinContent(1+i))
                            th.SetBinError(1+i,systematics['histograms'][sampleGroup].GetBinError(1+i))
                        th.SetDirectory(rootFileSubdir)
                        systematics['histograms'][sampleGroup] = th
                    else:
                        systematics['histograms'][sampleGroup].SetDirectory(rootFileSubdir)

        # DEPRECATED! now done by combine harvester!!
        # write bin-by-bin systematic histograms for sample groups
        if self.sysOptions['binstat'] and not self.sysOptions['ignore_stats']:
            binsBelowThreshold = {}
            systematicsListBeforeBBB = self.getSystematicsList(isData=(sampleGroup == 'DATA'))
            sampleGroupsMC = [x for x in sampleGroups if x != 'DATA']
            for sampleGroup in sampleGroupsMC:
                threshold =  0.5 #stat error / sqrt(value). It was 0.5
                if self.debug:
                    print("Running Statistical uncertainty")
                    print("threshold", threshold)
                for systematics in systematicsListBeforeBBB:
                    if 'histograms' in systematics and sampleGroup in systematics['histograms'] and systematics['systematicsName'] == 'nominal':
                        #dcProcess = self.sysOptions['Dict'][sampleGroup]
                        dcProcess = self.getProcessName(sampleGroup) 
                        hist = systematics['histograms'][sampleGroup]
                        for bin in range(1, self.binning['nBinsX'] + 1):
                            if dcProcess not in binsBelowThreshold.keys():
                                binsBelowThreshold[dcProcess] = []
                            if self.debug:
                                print ("binsBelowThreshold", binsBelowThreshold)
                                print ("hist.GetBinContent(bin)", hist.GetBinContent(bin))
                                print ("hist.GetBinError(bin)", hist.GetBinError(bin))
                            belowThreshold = False
                            if hist.GetBinContent(bin) > 0.:
                                if hist.GetBinError(bin)/sqrt(hist.GetBinContent(bin)) > threshold and hist.GetBinContent(bin) >= 1.:
                                    belowThreshold = True
                                elif hist.GetBinError(bin)/(hist.GetBinContent(bin)) > threshold and hist.GetBinContent(bin) < 1.:
                                    belowThreshold = True
                            if belowThreshold:
                                binsBelowThreshold[dcProcess].append(bin)
                            for Q in self.UD:
                                # add histogram with bin n varied up/down
                                bbbHistogram = hist.Clone()
                                bbbHistogram.SetDirectory(rootFileSubdir)
                                if Q == 'Up':
                                    bbbHistogram.SetBinContent(bin,max(1.E-6,hist.GetBinContent(bin)+hist.GetBinError(bin)))
                                if Q == 'Down':
                                    bbbHistogram.SetBinContent(bin,max(1.E-6,hist.GetBinContent(bin)-hist.GetBinError(bin)))
                                # add entry for the txt file
                                systematicsDictionary = deepcopy(self.systematicsDictionaryNominal)
                                systematicsDictionary.update({
                                        'sysType': 'bbb',
                                        'systematicsName': '%s_bin%s_%s_%s'%(self.sysOptions['systematicsnaming']['stats'], bin, dcProcess, self.Datacardbin),
                                        'dcProcess': dcProcess,
                                        'histograms': {sampleGroup: bbbHistogram},
                                        'binBelowThreshold': belowThreshold,
                                    })
                                bbbHistogramName = self.getHistogramName(process=dcProcess, systematics=systematicsDictionary) + Q
                                bbbHistogram.SetName(bbbHistogramName)
                                self.systematicsList.append(systematicsDictionary)

        outfile.Write()

        # ----------------------------------------------
        # write TEXT file
        # ----------------------------------------------
        if self.produceTextFiles:
            txtFileName = self.getDatacardBaseName(dcName, ext='.txt', chunkNumber=chunkNumber)
            print("INFO: TEXTFILE:\x1b[34m", txtFileName, "\x1b[0m")

            numProcesses = len([x for x in sampleGroups if x != 'DATA'])
            numSignals = len(self.sysOptions['setupSignals']) if 'setupSignals' in self.sysOptions else 1
            numBackgrounds = numProcesses - numSignals

            with open(txtFileName, 'w') as f:
                f.write('imax\t1\tnumber of channels\n')
                f.write('jmax\t%s\tnumber of processes minus 1 (\'*\' = automatic)\n'%(numProcesses-1))
                f.write('kmax\t*\tnumber of nuisance parameters (sources of systematical uncertainties)\n\n')
                f.write('shapes * * vhbb_%s_%s.root $CHANNEL%s$PROCESS $CHANNEL%s$PROCESS$SYSTEMATIC\n\n'%(self.DCtype, self.ROOToutname, self.DCprocessSeparatorDict[self.DCtype], self.DCprocessSeparatorDict[self.DCtype]))
                f.write('bin\t%s\n\n'%self.Datacardbin)
                # TODO: implement
                #if toy or signal_inject:
                #    f.write('observation\t%s\n\n'%(hDummy.Integral()))
                #else:
                #    if not split or (split and split_data):
                #        f.write('observation\t%s\n\n'%(theData.Integral()))
                if len([s for s in samples if s.isData()]) > 0:
                    nominalDict = self.getSystematicsList(isData=True)
                    if len(nominalDict) == 1:
                        nominalValue = nominalDict[0]['histograms']['DATA'].Integral()
                        print("\x1b[42mOBSERVED:", nominalValue, "\x1b[0m")
                        f.write('observation\t%s\n\n'%(nominalValue))
                    else:
                        print("\x1b[31mERROR: more or less than 1 nominal values found!!\x1b[0m")
                        raise Exception("DcDictError")

                # MC datacard processes
                if len([s for s in samples if not s.isData()]) < 1:
                    dcProcesses = []
                else:
                    #dcProcesses = [(self.sysOptions['Dict'][sampleGroup]) for sampleGroup in sampleGroups if sampleGroup != 'DATA']
                    dcProcesses = [self.getProcessName(sampleGroup) for sampleGroup in sampleGroups if sampleGroup != 'DATA']

                # order datacard processes as given in config
                dcProcesses.sort(key=lambda x: self.sysOptions['setup'].index(self.getGroupNameFromProcessName(x)) if self.getGroupNameFromProcessName(x) in self.sysOptions['setup'] else 99999)

                # header
                dcRows = []
                dcRows.append(['bin', ''] + [self.Datacardbin for x in range(numProcesses)])
                dcRows.append(['process', ''] + dcProcesses)

                # negative or zero for signals, otherwise for backgrounds
                dcRows.append(['process', ''] + ['%d'%x for x in range(-numSignals+1,1)] + ['%d'%x for x in range(1, numBackgrounds+1)])

                nominalHistograms = [x for x in self.systematicsList if x['sysType'] == 'nominal'][0]['histograms']
                histogramTotals = [nominalHistograms[self.getGroupNameFromProcessName(dcProcess)].Integral() for dcProcess in dcProcesses]

                dcRows.append(['rate', ''] + ['%f'%x for x in histogramTotals])
                
                # write non-shape systematics
                nonShapeSystematics = eval(self.config.get('Datacard', 'InUse_%s_%s'%(self.anType, self.ptRegion) if self.ptRegion else 'InUse'))
                for systematic in nonShapeSystematics:
                    systematicDict = eval(self.config.get('Datacard', systematic))
                    dcRow = [systematic, systematicDict['type']]
                    for dcProcess in dcProcesses:
                        dcRow.append(str(systematicDict[self.getGroupNameFromProcessName(dcProcess)]) if self.getGroupNameFromProcessName(dcProcess) in systematicDict else '-')
                    dcRows.append(dcRow)

                # bin by bin
                if self.sysOptions['binstat'] and not self.sysOptions['ignore_stats']:
                    # sort rows for bbb systematics in the same order as the processes and only include the bins below threshold
                    bbbSystematics = sorted([x for x in self.systematicsList if x['sysType'] == 'bbb' and x['binBelowThreshold']], key=lambda y: dcProcesses.index(y['dcProcess']) if y['dcProcess'] in dcProcesses else -1)
                    for systematics in bbbSystematics:
                        systematicsNameForDC = systematics['systematicsName'].split('_'+self.UD[0])[0].split('_'+self.UD[1])[0]
                        if systematicsNameForDC not in [dcRow[0] for dcRow in dcRows]:
                            dcRow = [systematicsNameForDC, 'shape']
                            for dcProcess in dcProcesses:
                                value = '1.0' if dcProcess == systematics['dcProcess'] else '-'
                                dcRow.append(value)
                            dcRows.append(dcRow)

                # UEPS systematics
                for systematics in self.systematicsList:
                    if systematics['sysType'] == 'weight':
                        systematicsNameForDC = systematics['systematicsName'].split('_'+self.UD[0])[0].split('_'+self.UD[1])[0]
                        if systematicsNameForDC not in [dcRow[0] for dcRow in dcRows]:
                            dcRow = [systematicsNameForDC, 'shape']
                            for dcProcess in dcProcesses:
                                value = '-'
                                if systematics['name'] in self.sysOptions['decorrelate_sys_weight']:
                                    if self.getGroupNameFromProcessName(dcProcess) in self.sysOptions['decorrelate_sys_weight'][systematics['name']]:
                                        value = '1.0'
                                else:
                                    value = '1.0'
                                dcRow.append(value)
                            dcRows.append(dcRow)

                # shape systematics
                for systematics in self.systematicsList:
                    if systematics['sysType'] == 'shape':
                        systematicsNameForDC = systematics['systematicsName'].split('_'+self.UD[0])[0].split('_'+self.UD[1])[0]
                        if systematicsNameForDC not in [dcRow[0] for dcRow in dcRows]:
                            dcRows.append([systematicsNameForDC, 'shape']  + ['1.0' for x in range(numProcesses)])

                # sample systematics
                for systematics in self.systematicsList:
                    if systematics['sysType'] == 'sample':

                        systematicsNameForDC = systematics['systematicsName'].split('_'+self.UD[0])[0].split('_'+self.UD[1])[0]
                        if systematicsNameForDC not in [dcRow[0] for dcRow in dcRows]:
                            dcRow = [systematicsNameForDC, 'shape']
                            
                            # check if the samples belonging to the current DC process are affected by sample sys
                            #TODO: too many list levels here, [0] index is not useful
                            sampleSysSamples = [x[0] for x in systematics['samples']]
                            sampleSysSamplesFlat = sum(sampleSysSamples, [])
                            sampleSysSamplesFlat = sum(sampleSysSamplesFlat, [])
                            sampleSysGroups = [self.sysOptions['Group'][x] for x in sampleSysSamplesFlat] 

                            for dcProcess in dcProcesses:
                                if self.getGroupNameFromProcessName(dcProcess) in sampleSysGroups:
                                    value = '1.0'
                                else:
                                    value = '-'
                                dcRow.append(value)

                            dcRows.append(dcRow)

                # rate params
                rateParams = eval(self.config.get('Datacard', 'rateParams_%s_%s'%(self.anType, self.ptRegion) if self.ptRegion else 'rateParams'))
                try:
                    rateParamRange = eval(self.config.get('Datacard', 'rateParamRange'))
                except:
                    rateParamRange = [0, 10]
                assert len(rateParamRange) is 2, 'rateParamRange is not 2! rateParamRange:' + len(rateParamRange)
                for rateParam in rateParams:
                    dictProcs = eval(self.config.get('Datacard', rateParam))
                    for dcProcess in dictProcs.keys():
                        dcRows.append([rateParam, 'rateParam', self.Datacardbin, dcProcess, str(dictProcs[dcProcess]), '[{minR},{maxR}]'.format(minR=rateParamRange[0], maxR=rateParamRange[1])])

                # write DC txt file 
                nColumns = max([len(dcRow) for dcRow in dcRows])
                nRows = len(dcRows)
                columnWidths = [max([(len(dcRows[row][column]) if len(dcRows[row]) > column else 0) for row in range(nRows)]) for column in range(nColumns)]

                for dcRow in dcRows:
                    f.write(' '.join([value.ljust(columnWidths[columnIndex]) for columnIndex, value in enumerate(dcRow)]) + '\n')

        print("done")

    def getDatacardBaseName(self, subPartName='', ext='', chunkNumber=-1):
        dcType = self.DCtype
        if len(subPartName) > 0:
            # temporary
            if chunkNumber>0:
                subPartName += '_%d'%chunkNumber
            baseFileName = '{path}/vhbb_{dcType}_{rootName}/{rootName}_{part}{ext}'.format(dcType=dcType, path=self.outpath, rootName=self.ROOToutname, part=subPartName, ext=ext)
        else:
            # final
            # different naming of text files and histograms, for some reason
            if ext.endswith('txt'):
                dcType = 'DC_' + dcType
            baseFileName = '{path}/vhbb_{dcType}_{rootName}{ext}'.format(dcType=dcType, path=self.outpath, rootName=self.ROOToutname, ext=ext)
        if self.verbose:
             print("DEBUG: base name =", baseFileName)
        return baseFileName

    @staticmethod
    def getRegions(config):
        return [x.strip() for x in (config.get('LimitGeneral', 'List')).split(',')]

    @staticmethod
    def getSamples(config, regions=None):
        # default is all regions
        if regions is None:
            regions = Datacard.getRegions(config)

        # get list of all sample names used in DC step
        sampleNames = []
        if config.has_option('LimitGeneral', 'addSample_sys'):
            addSample_sys = eval(config.get('LimitGeneral', 'addSample_sys'))
            sampleNames += [addSample_sys[key] for key in addSample_sys]
        for region in regions:
            for sampleType in ['data', 'signal', 'background']:
                sampleNames += eval(config.get('dc:%s'%region, sampleType))

        # get samples info
        sampleFolder = config.get('Directories', 'dcSamples')
        samplesInfo = ParseInfo(samples_path=sampleFolder, config=config)
        samples = samplesInfo.get_samples(sampleNames)

        return samples

