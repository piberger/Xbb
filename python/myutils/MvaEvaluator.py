import ROOT
from array import array
from mvainfos import mvainfo

class MvaEvaluator:
    def __init__(self, config, MVAinfo):
        self.varset = MVAinfo.varset
        #Define reader
        self.reader = ROOT.TMVA.Reader("!Color:!Silent")
        MVAdir=config.get('Directories','vhbbpath')
        self.systematics=config.get('systematics','systematics').split(' ')
        self.MVA_Vars={}
        self.MVAname = MVAinfo.MVAname
        for systematic in self.systematics:
            self.MVA_Vars[systematic]=config.get(self.varset,systematic)
            self.MVA_Vars[systematic]=self.MVA_Vars[systematic].split(' ')
        #define variables and specatators
        self.MVA_var_buffer = []
        for i in range(len( self.MVA_Vars['Nominal'])):
            self.MVA_var_buffer.append(array( 'f', [ 0 ] ))
            self.reader.AddVariable( self.MVA_Vars['Nominal'][i],self.MVA_var_buffer[i])
        self.reader.BookMVA(MVAinfo.MVAname,MVAdir+'/python/weights/'+MVAinfo.getweightfile())
        self.sample = None
        #--> Now the MVA is booked

    def setVariables(self,tree,job):
        #Set formulas for all vars
        self.MVA_formulas={}
        for systematic in self.systematics: 
            if job.type == 'DATA' and not systematic == 'Nominal': 
                continue
            self.MVA_formulas[systematic]=[]
            for j in range(len( self.MVA_Vars['Nominal'])):
                self.MVA_formulas[systematic].append(ROOT.TTreeFormula("MVA_formula%s_%s"%(j,systematic),self.MVA_Vars[systematic][j],tree))
        self.sample = job

    def evaluate(self, tree=None, destinationArray=None):
        #tree is not used, but has to be given as argument to match convention
        #Evaluate all vars and fill the branches
        if destinationArray:
            for systematic in self.systematics:
                for j in range(len( self.MVA_Vars['Nominal'])):
                    systematicNameInFormula = systematic
                    if self.sample.type == 'DATA' and not systematic == 'Nominal':
                        systematicNameInFormula = 'Nominal'
                    self.MVA_formulas[systematicNameInFormula][j].GetNdata()
                    self.MVA_var_buffer[j][0] = self.MVA_formulas[systematicNameInFormula][j].EvalInstance()
                destinationArray[self.systematics.index(systematic)] = self.reader.EvaluateMVA(self.MVAname)
