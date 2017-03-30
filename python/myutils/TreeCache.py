from __future__ import print_function
import os,sys,subprocess,hashlib
import ROOT
from samplesclass import Sample
import time

class TreeCache:
    def __init__(self, cutList, sampleList, path, config,filelist=None,mergeplot=False,sample_to_merge=None):
        ROOT.gROOT.SetBatch(True)
        self.path = path
        self.config = config
        print("Init path",path)#," sampleList",sampleList)
        self._cutList = []
        #! Make the cut lists from inputs
        for cut in cutList:
            self._cutList.append('(%s)'%cut.replace(' ',''))
        try:
            self.__tmpPath = os.environ["TMPDIR"]
            print('The TMPDIR is ', os.environ["TMPDIR"])
            
        except KeyError:
            print("\x1b[32;5m %s \x1b[0m" %open('%s/data/vhbb.txt' %config.get('Directories','vhbbpath')).read())
            print("\x1b[31;5;1m\n\t>>> %s: Please set your TMPDIR and try again... <<<\n\x1b[0m" %os.getlogin())
            sys.exit(-1)

        if filelist:
            print('len(filelist)',len(filelist))

        self.__doCache = True
        if config.has_option('Directories','tmpSamples'):
            self.__cachedPath = config.get('Directories','tmpSamples')
        self.__hashDict = {}
        self.minCut = None
        self.__find_min_cut()# store the cut list as one string in minCut, using ROOT syntax (i.e. || to separate between each cut) 
        self.__sampleList = sampleList
        self.sample_to_merge = sample_to_merge
        print('\n\t>>> Caching FILES <<<\n')
        self.__cache_samples(filelist,mergeplot)
        
    def putOptions(self):
        return (self.__sampleList,self.__doCache,self.__tmpPath,self._cutList,self.__hashDict,self.minCut,self.path)
    
    def _mkdir_recursive(self, path):
        sub_path = os.path.dirname(path)
        if not os.path.exists(sub_path):
            self._mkdir_recursive(sub_path)
        if not os.path.exists(path):
            os.mkdir(path)

    def __find_min_cut(self):
        effective_cuts = []
        for cut in self._cutList:
            if not cut in effective_cuts:
                effective_cuts.append(cut)
        self._cutList = effective_cuts
        self.minCut = '||'.join(self._cutList)

    def _subtrim_tree(self, input_hash, output_hash, theCut):
        '''Performs a finer caching from an already cached files, using as additional cuts the one used in the get_tree function'''

        print("==================")
        print("Perform subcaching")
        print("==================\n")

        print('Reading input', '%s/tmp_%s.root'%(self.__cachedPath,input_hash))
        input = ROOT.TFile.Open('%s/tmp_%s.root'%(self.__cachedPath,input_hash),'read')

        #if exist in tmpdir, just copy
        tmpfile = "%s/%s" %(self.__tmpPath,'tmp_'+str(output_hash)+'.root')
        outputFile = '%s/tmp_%s.root'%(self.__cachedPath,output_hash)
        print('outputFile is', outputFile)

        if self.__doCache and self.file_exists(tmpfile):
            print ('File exists in TMPDIR, proceeding to the copy')
            command = 'xrdcp -d 1 '+tmpfile+' '+ outputFile
            print('the command is', command)
            subprocess.call([command], shell=True)
            return output_hash

        output = ROOT.TFile.Open(tmpfile,'recreate')

        #Skim input file
        print('The input file is', '%s/tmp_%s.root'%(self.__cachedPath,input_hash))
        input = ROOT.TFile.Open('%s/tmp_%s.root'%(self.__cachedPath,input_hash),'read')

        input.Print()
        print ("I read the tree")
        tree = input.Get("tree")
        assert type(tree) is ROOT.TTree

        input.cd()
        obj = ROOT.TObject
        for key in ROOT.gDirectory.GetListOfKeys():
            input.cd()
            obj = key.ReadObj()
            if obj.GetName() == 'tree':
                continue
            output.cd()
            obj.Write(key.GetName())
        output.cd()
        print ("the cut is", theCut)
        #Problem here: not working when empty tree
        cuttedTree=tree.CopyTree(theCut)
        cuttedTree.Write()
        output.Write()
        input.Close()
        del input
        output.Close()
        del output
        print ("Copying file to the tmp folder.")
        print('outputFile',outputFile)
        command = 'xrdcp -d 1 '+tmpfile+' '+ outputFile
        subprocess.call([command], shell=True)
        if '/scratch/' in  tmpfile: command = 'rm %s' %(tmpfile)
        else: command = 'gfal-rm %s' %(tmpfile)

    def _trim_tree(self, sample, filelist, mergeplot = False, forceReDo = False):

        start_time = time.time()
        print("Caching the sample")
        print("==================\n")

        ''' Create temporary file for each sample '''
        theName = sample.name
        print('Reading sample <<<< %s' %sample)
        # print('path',self.path,'get_path',sample.get_path)
        # print('filelist',filelist)
        inputfiles = []
        outputfiles = []
        tmpfiles = []
        # prefix
        tmpCache = ''
        tmpSource = ''
        theHash = ''

        if not filelist or len(filelist) == 0 or mergeplot:
            source = '%s/%s' %(self.path,sample.get_path)
            inputfiles.append(source)
            checksum = self.get_checksum(source)
            theHash = hashlib.sha224('%s_s%s_%s' %(sample,checksum,self.minCut)).hexdigest()
            self.__hashDict[theName] = theHash
            tmpSource = '%s/tmp_%s.root'%(self.__tmpPath,theHash)
            print('opening '+source)
            tmpfiles.append(tmpSource)
            tmpCache = '%s/tmp_%s.root'%(self.__cachedPath,theHash)
            outputfiles.append(tmpCache)
            print('tmpSource is', tmpSource)
            print('tmpCache is', tmpCache)
            print('MERGEPLOT IS',mergeplot)
            if eval(str(mergeplot)):
                 # mergetreePSI(pathIN, pathOUT,           prefix,  newprefix, folderName,        Aprefix, Acut, config):
                from mergetreePSI import mergetreePSI_def
                mergetreePSI_def(self.path, self.__cachedPath, theHash, "tmp_",    sample.identifier, hashlib.sha224(self.minCut).hexdigest(),      "",   "")
                return 0

        else:
            outputFolder = "%s/%s" %(self.__cachedPath.replace('root://t3dcachedb03.psi.ch:1094/',''),sample.identifier)
            print('outputFolder is', outputFolder)
            if not os.path.isfile(outputFolder):
                createFolder = 'gfal-mkdir -p gsiftp://t3se01.psi.ch/' + outputFolder
                print('Will create the missing fodler using the command', createFolder)
                subprocess.call([createFolder], shell=True)# delete the files a
            for inputFile in filelist:
                # print('inputFile',inputFile)
                subfolder = inputFile.split('/')[-4]
                # print('subfolder',subfolder)
                filename = inputFile.split('/')[-1]
                # print('filename1',filename)
                filename = filename.split('_')[0]+'_'+subfolder+'_'+filename.split('_')[1]
                # print('filename2',filename)
                hash = hashlib.sha224(filename).hexdigest()
                inputFile = "%s/%s/%s" %(self.path,sample.identifier,filename.replace('.root','')+'_'+str(hash)+'.root')
                print('inputFile2',inputFile,'isfile',os.path.isfile(inputFile.replace('root://t3dcachedb03.psi.ch:1094/','')))
                if not os.path.isfile(inputFile.replace('root://t3dcachedb03.psi.ch:1094/','')): continue
                hash = hashlib.sha224(self.minCut).hexdigest()
                outputFile = "%s/%s/%s" %(self.__cachedPath,sample.identifier,filename.replace('.root','')+'_'+str(hash)+'.root')
                print('outputFile',outputFile)
                tmpfile = "%s/%s" %(self.__tmpPath,filename.replace('.root','')+'_'+str(hash)+'.root')
                print('tmpfile',tmpfile)
                if inputFile in inputfiles: continue
                del_protocol = outputFile
                del_protocol = del_protocol.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                del_protocol = del_protocol.replace('dcap://t3se01.psi.ch:22125/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                del_protocol = del_protocol.replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                if os.path.isfile(del_protocol.replace('srm://t3se01.psi.ch:8443/srm/managerv2?SFN=','')):
                    f = ROOT.TFile.Open(outputFile,'read')
                    if not f:
                      print('file is null, adding to input')
                      inputfiles.append(inputFile)
                      outputfiles.append(outputFile)
                      tmpfiles.append(tmpfile)
                      continue
                    # f.Print()
                    if f.GetNkeys() == 0 or f.TestBit(ROOT.TFile.kRecovered) or f.IsZombie():
                        print('f.GetNkeys()',f.GetNkeys(),'f.TestBit(ROOT.TFile.kRecovered)',f.TestBit(ROOT.TFile.kRecovered),'f.IsZombie()',f.IsZombie())
                        print('File', del_protocol.replace('srm://t3se01.psi.ch:8443/srm/managerv2?SFN=',''), 'already exists but is buggy, gonna delete and rewrite it.')
                        #command = 'srmrm %s' %(del_protocol)
                        subprocess.call([command], shell=True)
                        print(command)
                    else: continue
                inputfiles.append(inputFile)
                outputfiles.append(outputFile)
                tmpfiles.append(tmpfile)
        print('inputfiles',inputfiles,'tmpfiles',tmpfiles)

        ######################################################################
        for inputfile,tmpfile,outputFile in zip(inputfiles,tmpfiles,outputfiles):

            #print('the tmp source is ', tmpSource)
            #print ('self.__doCache',self.__doCache,'self.file_exists(tmpSource)',self.file_exists(tmpSource))
            print("==================================================================")
            print ('The cut is ', self.minCut)
            print("==================================================================\n")
            if self.__doCache and self.file_exists(outputFile) and not forceReDo and (not filelist or len(filelist) == 0):
                print('sample',theName,'skipped, filename=',outputFile)
                return (theName,theHash)
            else:
                if self.__doCache and self.file_exists(tmpfile) and not forceReDo:
                    print ('File exists in TMPDIR, proceeding to the copy')
                    print('sample',theName,'skipped, filename=',tmpfile)
                    command = 'xrdcp -d 1 '+tmpfile+' '+ outputFile
                    print('the command is', command)
                    subprocess.call([command], shell=True)
                    if len(filelist) == 0: return (theName,theHash)

            print ('trying to create',tmpfile)
            print ('self.__tmpPath',self.__tmpPath)
            if self.__tmpPath.find('root://t3dcachedb03.psi.ch:1094/') != -1:
                mkdir_command = self.__tmpPath.replace('root://t3dcachedb03.psi.ch:1094/','')
                print('mkdir_command',mkdir_command)
                # RECURSIVELY CREATE REMOTE FOLDER ON PSI SE, but only up to 3 new levels
                mkdir_command1 = mkdir_command.rsplit('/',1)[0]
                mkdir_command2 = mkdir_command1.rsplit('/',1)[0]
                mkdir_command3 = mkdir_command2.rsplit('/',1)[0]
                my_user = os.popen("whoami").read().strip('\n').strip('\r')+'/'
                if my_user in mkdir_command3:
                  print ('mkdir_command3',mkdir_command3)
                  subprocess.call(["uberftp t3se01 'mkdir "+mkdir_command3+" ' "], shell=True)# delete the files already created ?
                  " "
                if my_user in mkdir_command2:
                  print ('mkdir_command2',mkdir_command2)
                  subprocess.call(["uberftp t3se01 'mkdir "+mkdir_command2+" ' "], shell=True)# delete the files already created ?
                if my_user in mkdir_command1:
                  print ('mkdir_command1',mkdir_command1)
                  subprocess.call(["uberftp t3se01 'mkdir "+mkdir_command1+" ' "], shell=True)# delete the files already created ?
                if my_user in mkdir_command:
                  print ('mkdir_command',mkdir_command)
                  subprocess.call(["uberftp t3se01 'mkdir "+mkdir_command+" ' "], shell=True)# delete the files already created ?
            else:
                mkdir_command = self.__tmpPath
                print('mkdir_command',mkdir_command)
                # RECURSIVELY CREATE REMOTE FOLDER ON PSI SE, but only up to 3 new levels
                mkdir_command1 = mkdir_command.rsplit('/',1)[0]
                mkdir_command2 = mkdir_command1.rsplit('/',1)[0]
                mkdir_command3 = mkdir_command2.rsplit('/',1)[0]
                my_user = os.popen("whoami").read().strip('\n').strip('\r')+'/'
                if my_user in mkdir_command and not os.path.exists(mkdir_command):
                  print ('mkdir_command',mkdir_command)
                  subprocess.call(['mkdir '+mkdir_command], shell=True)# delete the files already created ?

            try:
                print("Writing: ",tmpfile)
                #! read the tree from the input
                if forceReDo:
                    output = ROOT.TFile.Open(tmpfile,'recreate')
                else:
                    output = ROOT.TFile.Open(tmpfile,'create')
                output.cd()
            except:
                ## in case there are problems go to the next dataset [probably another process is working on this dataset]
                if len(filelist) == 0: return (theName,theHash)
                else: print('PROBLEM WITH FILE!!',tmpfile); continue
            print ('reading inputfile',inputfile)
            print ("I am reading")
            input = ROOT.TFile.Open(inputfile,'read')
            input.Print()
            print ("I read the tree")
            tree = input.Get(sample.tree)
            assert type(tree) is ROOT.TTree

            input.cd()
            obj = ROOT.TObject
            for key in ROOT.gDirectory.GetListOfKeys():
                input.cd()
                obj = key.ReadObj()
                if obj.GetName() == 'tree':
                    continue
                output.cd()
                obj.Write(key.GetName())
            output.cd()
            theCut = self.minCut
            if sample.subsample:
                theCut = '((%s)&(%s))' %(theCut,sample.subcut)
            print ("the cut is", theCut)
            #Problem here: not working when empty tree
            ROOT.TFormula.SetMaxima(100000,1000,1000000)
            #theCutForm = ROOT.TFormula('theCut',theCut)
            #theCutForm.SetMaxima(100000,1000,1000000)
            cuttedTree=tree.CopyTree(theCut)
            #cuttedTree=tree.CopyTree(theCutForm)
            cuttedTree.Write()
            output.Write()
            input.Close()
            del input
            output.Close()
    #        tmpSourceFile = ROOT.TFile.Open(tmpSource,'read')
    #        if tmpSourceFile.IsZombie():
    #            print("@ERROR: Zombie file")
            del output
            print ("debug4")
            print ("I've done " + theName + " in " + str(time.time() - start_time) + " s.")
            print ("Copying file to the tmp folder.")
            print('outputFile',outputFile)
            command = 'xrdcp -d 1 '+tmpfile+' '+ outputFile
            print('the command is', command)
            subprocess.call([command], shell=True)
            if '/scratch/' in  tmpfile: command = 'rm %s' %(tmpfile)
            else: command = 'gfal-rm %s' %(tmpfile)
            if not filelist or len(filelist) == 0: return (theName,theHash)


    def __cache_samples(self,filelist=None,mergeplot=False):
        inputs=[]
        skip = True 
        for job in self.__sampleList:
            # test1 = [method for method in dir(job) if callable(getattr(job, method))]
            # print(test1)
            # print(dir(job))
            # print('__doc__',job.__doc__,'\n__eq__',job.__eq__,'\n__init__',job.__init__,'\n__module__',job.__module__,'\n__str__',job.__str__,'\nactive',job.active,'\naddtreecut',job.addtreecut,'\ncount',job.count,'\nget_path',job.get_path,'\ngroup',job.group,'\nidentifier',job.identifier,'\nlumi',job.lumi,'\nname',job.name,'\nprefix',job.prefix,'\nsf',job.sf,'\nspecialweight',job.specialweight,'\nsubcut',job.subcut,'\nsubsample',job.subsample,'\ntree',job.tree,'\ntreecut',job.treecut,'\ntype',job.type,'\nweightexpression',job.weightexpression,'\nxsec',job.xsec)
            # sys.exit()

            # print("__cache_samples(",filelist,",",mergeplot,")")
            if self.sample_to_merge and (str(job) != self.sample_to_merge):
                continue
            skip = False 
            samplematch = False
            if filelist and not mergeplot:
                if not 'Run' in job.identifier:
                    # print('no RUN','job.identifier',job.identifier,'filelist[0]',filelist[0])
                    #no ext case
                    if len(job.identifier.split('_ext')) == 1 and len(filelist[0].split('_ext')) == 1:
                        samplematch = '/'+job.identifier+'/' in filelist[0]
                    #ext case
                    else:
                        samplematch_noext = '/'+job.identifier.split('_ext')[0]+'/' in filelist[0]
                        samplematch = samplematch_noext and ('_ext'+job.identifier.split('_ext')[1] in filelist[0])
                else:
                    samplematch = '/'+job.identifier.split('__')[0]+'/' in filelist[0]

            elif filelist and mergeplot:
                if not 'Run' in job.identifier:
                    # print('no RUN','job.identifier',job.identifier,'filelist[0]',filelist[0])
                    #no ext case
                    if len(job.identifier.split('_ext')) == 1 and len(filelist[0].split('_ext')) == 1:
                        samplematch = job.identifier in filelist[0]
                    #ext case
                    elif len(job.identifier.split('_ext')) == 1 and len(filelist[0].split('_ext')) != 1:
                        pass
                    else:
                        samplematch_noext = job.identifier.split('_ext')[0] in filelist[0]
                        samplematch = samplematch_noext and ('_ext'+job.identifier.split('_ext')[1] in filelist[0])
                else:
                    samplematch = '/'+job.identifier.split('__')[0]+'/' in filelist[0]
            else:
                samplematch = True

            if samplematch: print('job.name',job.name,'samplematch',samplematch)#,'filelist',filelist)
            if samplematch:
                inputs.append((self,"_trim_tree",(job),(filelist),(mergeplot)))

        if skip:
            print('@INFO: no samples has been found')
            return 1
        multiprocess=0
        # if('pisa' in self.config.get('Configuration','whereToLaunch')):
        multiprocess=int(self.config.get('Configuration','nprocesses'))
        outputs = []
        print('launching __cache_samples with ',multiprocess,' processes')
        if multiprocess>1:
            from multiprocessing import Pool
            from myutils import GlobalFunction
            p = Pool(multiprocess)
            outputs = p.map(GlobalFunction, inputs)
        else:
            for input_ in inputs:
                #CACHING OF THE FILES HAPPENS HERE!!!!! THIS IS EQUIVALENT TO
                # self._trim_tree(job,filenames,mergeplot)
                outputs.append((getattr(input_[0],input_[1])(input_[2],input_[3],input_[4])))
        if not filelist or  len(filelist)==0:
        # for output in outputs:
            (theName,theHash) = outputs[0]
            self.__hashDict[theName]=theHash

    def get_tree(self, sample, cut):
        print('input file %s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name]))
        input = ROOT.TFile.Open('%s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name]),'read')
        print ('Opening %s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name]))
        try:
            tree = input.Get(sample.tree)
            assert type(tree) is ROOT.TTree
        except:
            print ("%s/tmp_%s.root is corrupted. I'm relaunching _trim_tree"%(self.__cachedPath,self.__hashDict[sample.name]))
            self._trim_tree(sample, None, False,forceReDo=True)
            input = ROOT.TFile.Open('%s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name]),'read')
            tree = input.Get(sample.tree)
            print("Type of sample.tree ROOT.TTree? (again) ", type(tree) is ROOT.TTree)


        #fill all Count* histos as lists, like self.CountWeighted = [123.23]
        for obj in input.GetListOfKeys():
            name = obj.GetName()
            if "Count" in name:
                obj = obj.ReadObj()
                assert(type(obj) is ROOT.TH1F)
                counts = []
                for i in range(obj.GetNbinsX()):
                    value = obj.GetBinContent(i+1)
                    if value<=0:
                        print("WARNING: bin ",i+1," of ",name," is ",value,". I'm forcing it to be 1.")
                        value=1
                    counts.append(value)

                setattr(self,name,counts)

        print('cut is', cut)
        ROOT.gROOT.cd()
        print('getting the tree after applying cuts')
        input.Close()
        del input
        del tree
        if cut == '' or cut == '1':
            return '%s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name])
        else:
            #Hash of the subtree
            subcut_hash = hashlib.sha224('%s_%s' %(self.__hashDict[sample.name],cut)).hexdigest()
            print('subcut input file %s/tmp_%s.root'%(self.__cachedPath, subcut_hash))
            input_ = '%s/tmp_%s.root'%(self.__cachedPath, subcut_hash)
            input = ROOT.TFile.Open(input_,'read')
            print('Opening ', input_)
            try:
                tree = input.Get(sample.tree)
                assert type(tree) is ROOT.TTree
            except:
                print (input_,"is corrupted. I'm relaunching _subtrim_tree")
                self._subtrim_tree(self.__hashDict[sample.name], subcut_hash, cut)
                input_ = '%s/tmp_%s.root'%(self.__cachedPath, subcut_hash)
                input = ROOT.TFile.Open(input_,'read')
                tree = input.Get(sample.tree)
        return '%s/tmp_%s.root'%(self.__cachedPath, subcut_hash)



    #def get_copy_tree(self, sample, cut):
    #    input = ROOT.TFile.Open(self.get_tree(sample, cut),'read')
    #    tree = input.Get(sample.tree)
    #    cuttedTree=tree.CopyTree(cut)
    #    cuttedTree.SetDirectory(0)
    #    return cuttedTree


    @staticmethod
    def get_slc_version():
        command = 'uname -a'
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
        lines = p.stdout.readlines()
        line = lines[0].split()[2]
        if 'el5' in line:
            return 'SLC5'
        elif 'el6' in line:
            return 'SLC6'
        else:
            sys.exit(-1)

    @staticmethod
    #def get_scale(sample, config, lumi = None, count=1):
#   #     print float(sample.lumi)
    #    try: sample.xsec = sample.xsec[0]
    #    except: pass
    #    anaTag=config.get('Analysis','tag')
    #    theScale = 1.
    #    lumi = float(sample.lumi)
    #    print ('SCALE')
    #    print ('count is', count)
    #    theScale = lumi*sample.xsec*sample.sf/(count)
    #    print("sample: ",sample,"lumi: ",lumi,"xsec: ",sample.xsec,"sample.sf: ",sample.sf,"count: ",count," ---> using scale: ", theScale)
    #    return theScale

    def get_scale_training(self, sample, config, lumi = None, count=1):
#        print float(sample.lumi)
        try: sample.xsec = sample.xsec[0]
        except: pass
        self.__cachedPath
        tmpCache = '%s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name])
        input = ROOT.TFile.Open(tmpCache,'read')
        #input.GetListOfKeys().Print()
        posWeight = input.Get('CountPosWeight')
        negWeight = input.Get('CountNegWeight')
        anaTag=config.get('Analysis','tag')
        theScale = 1.
        count = (posWeight.GetBinContent(1) - negWeight.GetBinContent(1))
        lumi = float(sample.lumi)
        theScale = lumi*sample.xsec*sample.sf/(count)
        print("sample: ",sample,"lumi: ",lumi,"xsec: ",sample.xsec,"sample.sf: ",sample.sf,"count: ",count," ---> using scale: ", theScale)
        return theScale

    def get_scale(self, sample, config, lumi = None, count=1):

        #print('name of the class is', self.__class__.__name__)
        return self.get_scale_training(self, sample, config, lumi, count)

    def get_scale_LHE(self, sample, config, lhe_scale, lumi = None, count=1):
        self.__cachedPath
        tmpCache = '%s/tmp_%s.root'%(self.__cachedPath,self.__hashDict[sample.name])
        input = ROOT.TFile.Open(tmpCache,'read')
        #input.GetListOfKeys().Print()
        posWeight = input.Get('CountPosWeight')
        negWeight = input.Get('CountNegWeight')
        Weight = input.Get('CountWeighted')
        countWeightedLHEWeightScale = input.Get('CountWeightedLHEWeightScale')

        scaled_count = 0
        if lhe_scale == 0:
            scaled_count = countWeightedLHEWeightScale.GetBinContent(0+1)
        elif lhe_scale == 1:
            scaled_count = countWeightedLHEWeightScale.GetBinContent(1+1)
        elif lhe_scale == 2:
            scaled_count = countWeightedLHEWeightScale.GetBinContent(2+1)
        elif lhe_scale == 3:
            scaled_count = countWeightedLHEWeightScale.GetBinContent(3+1)

        count = (posWeight.GetBinContent(1) - negWeight.GetBinContent(1))
        countWeightNoPU = (posWeight.GetBinContent(1) + negWeight.GetBinContent(1))
        countWeightPU = Weight.GetBinContent(1)


        if scaled_count == 0:
            return 0.
        else:
            return (countWeightNoPU/count)*self.get_scale_training(self, sample, config, lumi, count)*count/(scaled_count*(countWeightNoPU/countWeightPU))


    #Jdef get_cache(self, sample, config):
    ##retrives the cahe __cachedPath and __hashDict
    #self.__cachedPath = config.get('Directories','tmpSamples')
    #source = '%s/%s' %(self.path,sample.get_path)
    #checksum = self.get_checksum(source)
    #theHash = hashlib.sha224('%s_s%s_%s' %(sample,checksum,self.minCut)).hexdigest()
    #self.__hashDict[sample.name] = theHash



    @staticmethod
    def get_checksum(file):
        if 'gsidcap://t3se01.psi.ch:22128' in file:
            srmPath = 'srm://t3se01.psi.ch:8443/srm/managerv2?SFN='
            if TreeCache.get_slc_version() == 'SLC5':
                command = 'lcg-ls -b -D srmv2 -l %s' %file.replace('gsidcap://t3se01.psi.ch:22128/','%s/'%srmPath)
                p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
                lines = p.stdout.readlines()
                if any('No such' in line for line in lines):
                    print('File not found')
                    print(command)
                line = lines[1].replace('\t* Checksum: ','')
                checksum = line.replace(' (adler32)\n','')
            elif TreeCache.get_slc_version() == 'SLC6':
                command = 'srmls -l %s' %file.replace('gsidcap://t3se01.psi.ch:22128/','%s/'%srmPath)
                p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
                lines = p.stdout.readlines()
                if any('does not exist' in line for line in lines):
                    print('File not found')
                    print(command)
                checksum = lines[6].replace('- Checksum value:','')
                checksum = checksum.strip()
                #srmPath = 'srm://t3se01.psi.ch'
                #command = 'gfal-sum %s ADLER32' %file.replace('gsidcap://t3se01.psi.ch:22128/','%s/'%srmPath)
                #print(command)
                #p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
                #lines = p.stdout.readlines()
                #if any('No such' in line for line in lines):
                #    print('File not found')
                #    print(command)
                #checksum = lines[0].split()[1]

        else:
            command = 'md5sum %s' %file
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
            lines = p.stdout.readlines()
            checksum = lines[0]
        return checksum
    
    @staticmethod
    def file_exists(file):
        print ('Will now check if the file exists')
        print ('=================================\n')

        file_exists = False

        file_dummy = file
        #srmPath = 'srm://t3se01.psi.ch:8443/srm/managerv2?SFN='
        file_dummy = file_dummy.replace('root://t3dcachedb03.psi.ch:1094/','')
        file_dummy = file_dummy.replace('srm://t3se01.psi.ch:8443/srm/managerv2?SFN=','')

        print ('The command is', 'os.path.isfile(',file_dummy,')', os.path.isfile(file_dummy))
        if os.path.isfile(file_dummy):
            print(file_dummy, 'exists.')
            f = ROOT.TFile.Open(file,'read')
            if not f:
                print ('File is null. Gonna redo it.')
                del_protocol = file.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('dcap://t3se01.psi.ch:22125/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                if '/scratch/' in  del_protocol: command = 'rm %s' %(del_protocol)
                else: command = 'gfal-rm %s' %(del_protocol)
                subprocess.call([command], shell=True)
                print(command)
            elif f.GetNkeys() == 0 or f.TestBit(ROOT.TFile.kRecovered) or f.IsZombie():
                print ('f.GetNkeys()',f.GetNkeys(),'f.TestBit(ROOT.TFile.kRecovered)',f.TestBit(ROOT.TFile.kRecovered),'f.IsZombie()',f.IsZombie())
                print ('File', file_dummy, 'already exists but is buggy, gonna delete and rewrite it.')
                del_protocol = file.replace('gsidcap://t3se01.psi.ch:22128/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('dcap://t3se01.psi.ch:22125/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=').replace('root://t3dcachedb03.psi.ch:1094/','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')
                # print('del_protocol',del_protocol)
                if '/scratch/' in  del_protocol: command = 'rm %s' %(del_protocol)
                else: command = 'gfal-rm %s' %(del_protocol)
                subprocess.call([command], shell=True)
                print(command)
            else:
                file_exists = True

        #exist = os.path.exists(file_dummy)
        #print('os.path.exists(',file_dummy,')',exist)
        #return os.path.exists(file_dummy)
        return file_exists


