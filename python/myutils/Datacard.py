#!/usr/bin/env python
from __future__ import print_function
import os, ROOT, warnings
ROOT.gROOT.SetBatch(True)
from copy import copy, deepcopy
from sample_parser import ParseInfo
import json
import hashlib
import NewTreeCache as TreeCache
from sampleTree import SampleTree as SampleTree
from NewHistoMaker import NewHistoMaker as HistoMaker
from NewStackMaker import NewStackMaker as StackMaker
from BranchList import BranchList

class Datacard(object):
    def __init__(self, config, region):
        self.verbose = True
        self.config = config
        self.DCtype = 'TH'
        self.histograms = None
        self.DCprocessSeparatorDict = {'WS':':','TH':'/'}
        VHbbNameSpace = config.get('VHbbNameSpace', 'library')
        returnCode = ROOT.gSystem.Load(VHbbNameSpace)
        if returnCode != 0:
            print ("\x1b[31mERROR: loading VHbbNameSpace failed with code %d\x1b[0m"%returnCode)
        else:
            print ("INFO: loaded VHbbNameSpace: %s"%VHbbNameSpace)
        
        self.region = region
        self.anaTag = config.get("Analysis", "tag")
        if self.anaTag not in ['7TeV', '8TeV', '13TeV']:
            raise Exception("anaTag %s unknown. Specify 8TeV or 7TeV or 13TeV in the general config"%self.anaTag)
        # Directories:
        self.Wdir = config.get('Directories', 'Wdir')
        self.vhbbpath = config.get('Directories', 'vhbbpath')
        self.samplesInfoDirectory = config.get('Directories', 'samplesinfo')
        self.path = config.get('Directories', 'dcSamples')
        self.cachedPath = self.config.get('Directories', 'tmpSamples')
        self.tmpPath = self.config.get('Directories', 'scratch')
        self.outpath = config.get('Directories', 'limits')
        self.optimisation = "" #TODO: opts.optimisation
        self.optimisation_training = False
        self.UseTrainSample = eval(config.get('Analysis', 'UseTrainSample'))
        if self.UseTrainSample:
            print ('Training events will be used')
        if not self.optimisation == '':
            print ('Preparing DC for BDT optimisaiton')
            self.optimisation_training = True
        print ('optimisation is', self.optimisation)
        try:
            os.stat(self.outpath)
        except:
            os.mkdir(self.outpath)
        
        # parse histogram config:
        self.treevar = config.get('dc:%s'%self.region, 'var')
        print ('treevar is', self.treevar)
        self.name = config.get('dc:%s'%self.region, 'wsVarName')
        if self.optimisation_training:
            self.treevar = self.optimisation + '.Nominal'
            self.name += '_' + self.optimisation
            if self.UseTrainSample:
                self.name += '_Train'
        print ('again, treevar is', self.treevar)
        
        # set binning
        self.binning = {
                'nBins': int(config.get('dc:%s'%self.region, 'range').split(',')[0]),
                'xMin': float(config.get('dc:%s'%self.region, 'range').split(',')[1]),
                'xMax': float(config.get('dc:%s'%self.region, 'range').split(',')[2]),
                }
        if self.verbose:
            print ("DEBUG: binning is ", self.binning)
        self.ROOToutname = config.get('dc:%s'%self.region, 'dcName')
        if self.optimisation_training:
           self.ROOToutname += self.optimisation
           if self.UseTrainSample:
               self.ROOToutname += '_Train'
        self.RCut = config.get('dc:%s'%self.region, 'cut')
        self.signals = eval('['+config.get('dc:%s'%self.region, 'signal')+']') #TODO
        self.Datacardbin=config.get('dc:%s'%self.region, 'dcBin')
        self.anType = config.get('dc:%s'%self.region, 'type').lower()

        #new
        try:
            self.BDTmin = eval(config.get('LimitGeneral', 'BDTmin'))
        except:
            self.BDTmin = None

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
        if self.anType in analysisSystematics:
            self.systematics = eval(config.get('LimitGeneral', analysisSystematics[self.anType]))
        else:
            print ("\x1b[31mEXIT: please specify if your datacards are BDT, Mjj or cr.\x1b[0m")
            raise Exception("InvalidDatacardSystematicsType")

        self.sysOptions = {}
        # define the options read directly from the config
        sysOptionNames = ['sys_cut_suffix', 'sys_weight_corr', 'decorrelate_sys_weight', 'sys_cut_include', 'sys_factor', 'sys_affecting', 'sys_lhe_affecting', 'rescaleSqrtN', 'toy', 'blind', 
                'addBlindingCut', 'change_shapes', 'Group', 'Dict', 'binstat', 'rebin_active', 'ignore_stats', 'signal_inject', 'add_signal_as_bkg', 'systematicsnaming', 'weightF_sys',
                'sample_sys_info', 'addSample_sys', 'removeWeightSystematics', 'ptRegionsDict', 'setup', 'setupSignals' 
                ]
        for sysOptionName in sysOptionNames:
            self.sysOptions[sysOptionName] = eval(config.get('LimitGeneral', sysOptionName)) if config.has_option('LimitGeneral', sysOptionName) else None
            print (" > \x1b[34m{name}\x1b[0m:{value}".format(name=sysOptionName.ljust(40), value=self.sysOptions[sysOptionName]))

        # read weights
        self.weightF = config.get('Weights', 'weightF')
        self.SBweight = None
        print ('before adding SBweight, weightF is', self.weightF)
        if self.anType == 'mjj':
            print ('Passed mJJ')
            if config.has_option('dc:%s'%self.region, 'SBweight'):
                print ('passed config')
                self.SBweight = config.get('dc:%s'%self.region, 'SBweight')
                self.weightF ='('+self.weightF+')*('+self.SBweight+')'
                print ('after adding SBweight, weightF is', self.weightF)
            else:
                print ('NOT Passed config')

        self.TrainFlag = eval(config.get('Analysis', 'TrainFlag'))
        self.treecut = config.get('Cuts', self.RCut)
        
        # checks on read options
        #on control region cr never blind. Overwrite whatever is in the config
        if self.anType == 'cr':
            if self.sysOptions['blind']:
                print ('@WARNING: Changing blind to false since you are running for control region.')
            self.sysOptions['blind'] = False
            self.sysOptions['binstat'] = False

        if self.sysOptions['blind']:
            print('\x1b[31mI AM BLINDED!\x1b[0m')
            
        if self.anType != 'bdt':
            if self.sysOptions['rebin_active']:
                print ('@WARNING: Changing rebin_active to false since you are running for control region.')
            self.sysOptions['rebin_active'] = False
        if self.sysOptions['add_signal_as_bkg']:
            self.sysOptions['setup'].append(self.sysOptions['add_signal_as_bkg'])

        #Assign Pt region for sys factors
        print ('Assign Pt region for sys factors')
        print ('================================\n')
        self.ptRegion = [ptRegion for ptRegion, outputNames in self.sysOptions['ptRegionsDict'].iteritems() if len([x for x in outputNames if x.upper() in self.ROOToutname.upper()])>0]
        if len(self.ptRegion) != 1:
            print("\x1b[31mERROR: invalid pt region:", self.ptRegion,"\1b[0m")
        else:
            self.ptRegion = self.ptRegion[0]
        print ("\x1b[33mptRegion:\x1b[0m", self.ptRegion)
       
        for outputName, removeSystematics in self.sysOptions['removeWeightSystematics'].iteritems():
            if outputName in self.ROOToutname:
                self.sysOptions['weightF_sys'] = [x for x in self.sysOptions['weightF_sys'] if x not in removeSystematics]

        #systematics up/down
        self.UD = ['Up', 'Down']

        print ('Parse the sample information')
        print ('============================\n')
        #Parse samples configuration
        self.samplesInfo = ParseInfo(self.samplesInfoDirectory, self.path)

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
        for sample_sys in self.sample_sys_list:
            self.sample_sys_dic[sample_sys] = False
        print ("\x1b[34msample_sys_list\x1b[0m =", self.sample_sys_list)
        
        self.MC_samples = self.signals + self.backgrounds + self.additionals
        
        self.samples = {
                'SIG': self.samplesInfo.get_samples(self.signals),
                'BKG': self.samplesInfo.get_samples(self.backgrounds),
                'DATA': self.samplesInfo.get_samples(self.data_sample_names),
                'ADD': self.samplesInfo.get_samples(self.additionals),
                }

        if self.verbose:
            print ('sample list')
            print ('===================\n')
            print (json.dumps(self.samples, sort_keys=True, indent=8, default=str))

        if self.verbose:
            print ('systematics')
            print ('===================\n')
            print (json.dumps(self.sysOptions['sys_affecting'], sort_keys=True, indent=8, default=str))

        self.systematicsDictionaryNominal = {
                'cut': self.treecut,
                'var': self.treevar,
                'name': self.name,
                'systematicsName': 'nominal',
                'binning': self.binning,
                'weight': self.weightF,
                'countHisto': 'CountWeighted',
                'countbin': 0,
                'blind': self.sysOptions['blind'],
                'sysType': 'nominal',
                'SBweight': self.SBweight,
                'sample_sys_dic': self.sample_sys_dic,
                }
        
        # contains all systematicDictionaries
        self.systematicsList = [self.systematicsDictionaryNominal]

        print ('Assign the systematics')
        print ('======================\n')

        # shape systematics
        for syst in self.systematics:
            for Q in self.UD:
                systematicsDictionary = deepcopy(self.systematicsDictionaryNominal)
                systematicsDictionary.update({
                        'cut': self.getSystematicsCut(syst, Q),
                        'var': self.getSystematicsVar(syst, Q),
                        'weight': self.getSystematicsWeight(syst, Q),
                        'sysType': 'shape',
                        'systematicsName': '{sysName}_{Q}'.format(sysName=self.sysOptions['systematicsnaming'][syst], Q=Q) 
                    })
                self.systematicsList.append(systematicsDictionary)
        
        if self.verbose:
            print ('systematics dict')
            print ('===================\n')
            print (json.dumps(self.systematicsList, sort_keys=True, indent=8, default=str))
        
        # weight systematics
        # TODO: why uppercase is used for weight systematics?
        for weightF_sys in self.sysOptions['weightF_sys']:
            for Q in self.UD:
                weight = self.config.get('Weights', '%s_%s' %(weightF_sys, Q.upper())) # <- here TODO
                systematicsDictionary = deepcopy(self.systematicsDictionaryNominal)
                systematicsDictionary.update({
                        'sysType': 'weight',
                        'weight': weight if self.SBweight == None else '('+weight+')*('+self.SBweight+')', 
                        'name': weightF_sys,
                        'systematicsName': '{sysName}_{Q}'.format(sysName=self.sysOptions['systematicsnaming'][weightF_sys], Q=Q) 
                    })
                self.systematicsList.append(systematicsDictionary)

        # sample systematics
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
        if self.anType == 'bdt':
            if not 'UD' in syst:
                print ('treevar was', treevar)
                treevar = treevar.replace('.Nominal','.%s_%s'%(syst, Q))
                print ('.nominal by', '.%s_%s'%(syst, Q))
            else:
                treevar = treevar.replace('.nominal','.%s'%(syst.replace('UD', Q)))
                print ('.nominal by', '.%s'%(syst.replace('UD', Q)))
        elif self.anType == 'mjj':
            if not 'UD' in syst:
                print ('treevar was', treevar)
                treevar = treevar.replace('_reg_mass', '_reg_mass_corr%s%s'%(syst, Q))
                print ('_reg_mass', '_reg_mass_corr%s%s'%(syst, Q))
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

    # return cut for systematics variation as string
    def getSystematicsCut(self, syst, Q):
        cut = self.treecut
        new_cut_list = self.sysOptions['sys_cut_suffix'][syst] if isinstance(self.sysOptions['sys_cut_suffix'][syst], list) else [self.sysOptions['sys_cut_suffix'][syst]] 
        for new_cut in new_cut_list:
            if not new_cut == 'nominal':
                old_str, new_str = new_cut.split('>')
                cut = cut.replace(old_str, new_str.replace('SYS', syst).replace('UD', Q).replace('?', Q))
        return cut

    # return full (flattened) list of sample objects
    def getAllSamples(self):
        return sum([y for x, y in self.samples.iteritems()], []) 

    def run(self, useSampleIdentifiers=None):
   
        #Calculate lumi
        lumi = sum([sample.lumi for sample in self.samples['DATA']])/len(self.samples['DATA']) if len(self.samples['DATA']) > 0 else 0  
        
        # select samples to use
        allSamples = self.getAllSamples() # sum([samples for sampleType, samples in self.samples.iteritems()], [])
        #if useDatacardProcess:
        #    allSamples = [sample for sample in allSamples if self.sysOptions['Group'][sample.name] != 'DATA' and self.sysOptions['Dict'][self.sysOptions['Group'][sample.name]] == useDatacardProcess] 
        if useSampleIdentifiers:
            allSamples = [sample for sample in allSamples if sample.identifier in useSampleIdentifiers] 
        #if useSampleNames:
        #    allSamples = [sample for sample in allSamples if sample.name in useSampleNames] 
        
        usedSamplesString = ''
        if useSampleIdentifiers:
            usedSamplesString = '_' + ('_'.join(sorted(list(set([sample.identifier for sample in allSamples])))))
        
        if len(allSamples) < 1:
            print ("INFO: no samples, nothing to do.")
            return None

        print ('\n\t...fetching histos...\n')

        self.histograms = {}
        histogramCounter = 0
        # read cached sample trees, for every sample there is one SampleTree, which contains the events needed for ALL the systematics
        # use this sample tree with appropriate cuts for each systematics to fill the histograms
        for i, sample in enumerate(allSamples): 
            
            print("SAMPLE NUMBER ", i, " OF ", len(allSamples))
            # get cuts that were used in caching for this sample
            systematicsCuts = [x['cut'] for x in self.getSystematicsList(isData=(sample.type == 'DATA'))]
            sampleCuts = {'AND': [sample.subcut, {'OR': systematicsCuts}]}

            # get sample tree from cache
            tc = TreeCache.TreeCache(
                    sample=sample,
                    cutList=sampleCuts,
                    inputFolder=self.path,
                    outputFolder=self.cachedPath,
                    debug=True
                )
            sampleTree = tc.getTree()

            self.histograms[sample.name] = {}
            # add all the cuts/weights for the different systematics 
            for systematics in self.getSystematicsList(isData=(sample.type == 'DATA')):

                # additional BLINDING cut
                if self.sysOptions['addBlindingCut']:
                    systematics['cutWithBlinding'] = '({cut})&&({blindingCut})'.format(cut=systematics['cut'], blindingCut=self.sysOptions['addBlindingCut'])
                else:
                    systematics['cutWithBlinding'] = systematics['cut']
                
                # prepare histograms
                histogramName = sample.name + '_' + systematics['systematicsName'] + '_c%d'%histogramCounter
                histogramCounter += 1
                self.histograms[sample.name][systematics['systematicsName']] = ROOT.TH1F(histogramName, histogramName, self.binning['nBins'], self.binning['xMin'], self.binning['xMax'])

                # add
                sampleTree.addFormula(systematics['cutWithBlinding'], systematics['cutWithBlinding'])
                if sample.type != 'DATA':
                    sampleTree.addFormula(systematics['weight'], systematics['weight'])
                sampleTree.addFormula(systematics['var'], systematics['var'])

            # sample scale factor, to match to cross section
            sampleScaleFactor = sampleTree.getScale(sample) if sample.type != 'DATA' else 1.0

            # get used branches, which are either used in cut, weight or the variable itself
            usedBranchList = BranchList()
            for systematics in self.getSystematicsList(isData=(sample.type == 'DATA')):
                usedBranchList.addCut(systematics['cutWithBlinding'])
                usedBranchList.addCut(systematics['weight'])
                usedBranchList.addCut(systematics['var'])

            # remove unused branches
            listOfBranchesToKeep = usedBranchList.getListOfBranches()
            sampleTree.enableBranches(listOfBranchesToKeep)
            
            systematicsToEvaluate = self.getSystematicsList(isData=(sample.type == 'DATA'))

            # loop over all events in this sample
            for event in sampleTree:

                # evaluate all systematics for this event
                for systematics in systematicsToEvaluate:

                    cutPassed = sampleTree.evaluate(systematics['cutWithBlinding'])
                    if cutPassed:
                        weight = sampleTree.evaluate(systematics['weight']) if sample.type != 'DATA' else 1.0
                        treeVar = sampleTree.evaluate(systematics['var'])
                        self.histograms[sample.name][systematics['systematicsName']].Fill(treeVar, weight * sampleScaleFactor)
        
        self.writeDatacards(samples=allSamples, dcName=usedSamplesString)

    def load(self, histogramFileNames):

        self.histograms = {}
        allSamples = self.getAllSamples()
        sampleIdentifiers = sorted(list(set([sample.identifier for sample in allSamples])))
        for sampleIdentifier in sampleIdentifiers:

            subsamples = [sample for sample in allSamples if sample.identifier == sampleIdentifier]
            print ("SUBS:", [sample.name for sample in subsamples])
                
            rootFileName = self.getDatacardBaseName(subPartName=sampleIdentifier) + '.root'
            rootFile = ROOT.TFile.Open(rootFileName, 'read')
            if not rootFile or rootFile.IsZombie():
                print ("\x1b[31mERROR: bad root file:", rootFileName, "\x1b[0m")
                raise Exception("FileIOError")

            for subsample in subsamples:
                sampleGroup = self.sysOptions['Group'][subsample.name]
                datacardProcess = self.sysOptions['Dict'][sampleGroup] if sampleGroup != 'DATA' else 'data_obs'

                systematicsToEvaluate = self.getSystematicsList(isData=(subsample.type == 'DATA'))
                for systematics in systematicsToEvaluate:
                    datacardProcessHistogramName = self.getHistogramName(process=datacardProcess, systematics=systematics)
                    histogramPath = '{folder}/{histogram}'.format(folder=self.Datacardbin, histogram=datacardProcessHistogramName)
                    histogram = rootFile.Get(histogramPath)
                    if not histogram:
                        print ("IN:", rootFileName)
                        print ("LOOKING FOR:", histogramPath)
                        print ("?:", rootFile.Get(histogramPath))
                        raise Exception("HistogramMissing")
                    if subsample.name not in self.histograms:
                        self.histograms[subsample.name] = {}

                    self.histograms[subsample.name][systematics['systematicsName']] = histogram.Clone()
                    self.histograms[subsample.name][systematics['systematicsName']].SetDirectory(0)


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

    def writeDatacards(self, samples=None, dcName=''):
        
        if not self.histograms:
            print("\x1b[31mERROR: no histograms found, datacard histograms must be either created with run() or loaded with load()\x1b[0m")
            raise Exception("DcHistogramsMissing")

        if samples is None:
            samples = self.getAllSamples()

        # open and prepare histogram output files
        histogramFileName = self.getDatacardBaseName(dcName) + '.root'
        print("HISTOGRAM:", histogramFileName)
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
        
        # sample groups for datacard, all samples of each group will be added in a single column
        sampleGroups = list(set([self.sysOptions['Group'][sample.name] for sample in samples]))
            
        for systematics in self.getSystematicsList(isData=(sample.type == 'DATA')): 
            systematics['histograms'] = {}
        
        for sampleGroup in sampleGroups:
            # adjust name for DC convention
            for systematics in self.getSystematicsList(isData=(sampleGroup == 'DATA')): 
                # sum histograms of all samples in the datacard group
                datacardProcess = self.sysOptions['Dict'][sampleGroup] if sampleGroup != 'DATA' else 'data_obs'
                datacardProcessHistogramName = self.getHistogramName(process=datacardProcess, systematics=systematics) 
                
                # add up all the sample histograms for this process and this systematic
                histogramsInGroup = [h[systematics['systematicsName']] for k, h in self.histograms.iteritems() if self.sysOptions['Group'][k] == sampleGroup] 

                print (sampleGroup," -> GROUPH:", histogramsInGroup)
                if len(histogramsInGroup) > 0:
                    systematics['histograms'][sampleGroup] = StackMaker.sumHistograms(histogramsInGroup, datacardProcessHistogramName)
                    systematics['histograms'][sampleGroup].SetDirectory(rootFileSubdir)
        
        outfile.Write()
        
        #----------------------------------------------
        # write TEXT file
        #----------------------------------------------
        txtFileName = self.getDatacardBaseName(dcName) + '.txt'
        print("TEXTFILE:", txtFileName)

        numProcesses = len([x for x in sampleGroups if x != 'DATA'])
        if 'setupSignals' in self.sysOptions:
            numSignals = len([x for x in sampleGroups if x in self.sysOptions['setupSignals']])
        else:
            numSignals = 1   # which is the first one by old convention!!!
        numBackgrounds = numProcesses - numSignals

        with open(txtFileName, 'w') as f:
            f.write('imax\t1\tnumber of channels\n')
            f.write('jmax\t%s\tnumber of backgrounds (\'*\' = automatic)\n'%(numBackgrounds))
            f.write('kmax\t*\tnumber of nuisance parameters (sources of systematical uncertainties)\n\n')
            f.write('shapes * * vhbb_%s_%s.root $CHANNEL%s$PROCESS $CHANNEL%s$PROCESS$SYSTEMATIC\n\n'%(self.DCtype, self.ROOToutname, self.DCprocessSeparatorDict[self.DCtype], self.DCprocessSeparatorDict[self.DCtype]))
            f.write('bin\t%s\n\n'%self.Datacardbin)
            # TODO: implement
            #if toy or signal_inject:
            #    f.write('observation\t%s\n\n'%(hDummy.Integral()))
            #else:
            #    if not split or (split and split_data):
            #        f.write('observation\t%s\n\n'%(theData.Integral()))
            if len([s for s in samples if s.type == 'DATA']) > 0:
                nominalDict = self.getSystematicsList(isData=True)
                if len(nominalDict) == 1:
                    nominalValue = nominalDict[0]['histograms']['DATA'].Integral()
                    print("\x1b[42mOBSERVED:", nominalValue, "\x1b[0m")
                    f.write('observation\t%s\n\n'%(nominalValue))
                else:
                    print("\x1b[31mERROR: more or less than 1 nominal values found!!\x1b[0m")
                    raise Exception("DcDictError")

            numProcesses = len(sampleGroups)
            
            # MC datacard processes
            if len([s for s in samples if s.type != 'DATA']) < 1:
                dcProcesses = []
            else:
                dcProcesses = [(self.sysOptions['Dict'][sampleGroup]) for sampleGroup in sampleGroups if sampleGroup != 'DATA']
            
            dcProcessSampleGroup = {v: k for k,v in self.sysOptions['Dict'].iteritems()}
            
            # order datacard processes as given in config
            dcProcesses.sort(key=lambda x: self.sysOptions['setup'].index(dcProcessSampleGroup[x]) if x in dcProcessSampleGroup and dcProcessSampleGroup[x] in self.sysOptions['setup'] else 99999)
            
            # header
            dcRows = []
            dcRows.append(['bin',''] + [self.Datacardbin for x in range(numProcesses)])
            dcRows.append(['process',''] + dcProcesses)

            # negative or zero for signals, otherwise for backgrounds
            dcRows.append(['process',''] + ['%d'%x for x in range(-numSignals+1,1)] + ['%d'%x for x in range(1, numBackgrounds+1)])

            histogramTotals = [systematics['histograms'][dcProcessSampleGroup[dcProcess]].Integral() for dcProcess in dcProcesses]
            dcRows.append(['rate',''] + ['%f'%x for x in histogramTotals])
            
            # write non-shape systematics
            nonShapeSystematics = eval(self.config.get('Datacard', 'InUse_%s_%s'%(self.anType, self.ptRegion)))
            for systematic in nonShapeSystematics:
                systematicDict = eval(self.config.get('Datacard', systematic))
                dcRow = [systematic, systematicDict['type']]
                for dcProcess in dcProcesses:
                    dcRow.append(str(systematicDict[dcProcessSampleGroup[dcProcess]]) if dcProcessSampleGroup[dcProcess] in systematicDict else '-')

                    #TODO: IMPLEMENT??
                    #if '_eff_e' in item and 'Zuu' in ROOToutname : f.write('\t-')
                    #elif '_eff_m' in item and 'Zee' in ROOToutname : f.write('\t-')
                    #elif '_trigger_e' in item and 'Zuu' in ROOToutname : f.write('\t-')
                    #elif '_trigger_m' in item and 'Zee' in ROOToutname : f.write('\t-')
                    #else:
                    #    f.write('\t%s'%what[c])
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
                                if dcProcessSampleGroup[dcProcess] in self.sysOptions['decorrelate_sys_weight'][systematics['name']]:
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
                            if dcProcessSampleGroup[dcProcess] in sampleSysGroups:
                                value = '1.0'
                            else:
                                value = '-'
                            dcRow.append(value)

                        dcRows.append(dcRow)

            # rate params
            rateParams = eval(self.config.get('Datacard', 'rateParams_%s_%s'%(self.anType, self.ptRegion)))
            try:
                rateParamRange = eval(self.config.get('Datacard', 'rateParamRange'))
            except:
                rateParamRange = [0, 10]
            assert len(rateParamRange) is 2, 'rateParamRange is not 2! rateParamRange:'+ len(rateParamRange)
            for rateParam in rateParams:
                dictProcs = eval(self.config.get('Datacard', rateParam))
                for dcProcess in dictProcs.keys():
                    dcRows.append([rateParam, 'rateParam', self.Datacardbin, dcProcess, str(dictProcs[dcProcess]), '[{minR},{maxR}]'.format(minR=rateParamRange[0], maxR=rateParamRange[1])]) 
            
            # write DC txt file 
            nColumns = max([len(dcRow) for dcRow in dcRows])
            nRows = len(dcRows)
            columnWidths = [max([ (len(dcRows[row][column]) if len(dcRows[row]) > column else 0) for row in range(nRows)])  for column in range(nColumns)]

            for dcRow in dcRows:
                f.write(' '.join([value.ljust(columnWidths[columnIndex]) for columnIndex, value in enumerate(dcRow)]) + '\n')

        print("done")

    def getDatacardBaseName(self, subPartName=''):
        if len(subPartName) > 0:
            # temporary
            baseFileName = '{path}/vhbb_{dcType}_{rootName}/{rootName}_{part}'.format(dcType=self.DCtype, path=self.outpath, rootName=self.ROOToutname, part=subPartName)
        else:
            # final
            baseFileName = '{path}/vhbb_{dcType}_{rootName}'.format(dcType=self.DCtype, path=self.outpath, rootName=self.ROOToutname)
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
        samplesInfoDirectory = config.get('Directories', 'samplesinfo')
        samplesInfo = ParseInfo(samplesInfoDirectory, sampleFolder)
        samples = samplesInfo.get_samples(sampleNames)

        return samples

