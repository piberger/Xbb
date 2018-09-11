import json
import os
import array
from JsonTable import JsonTable
from vLeptons import vLeptonSelector

class ElectronSFfromJSON(object):
    
    def __init__(self, jsonFiles=None):
        self.jsonFiles = jsonFiles
        self.debug = 'XBBDEBUG' in os.environ

        # load JOSN files
        self.jsonTable = JsonTable(jsonFiles)
        self.idIsoSfName = 'doubleEleIDISO2017'
        self.triggerLegNames = ['doubleEleTriggerLeg1', 'doubleEleTriggerLeg2']
        self.systVariations = [None, 'Down', 'Up']
        self.idIsoSf = self.jsonTable.getEtaPtTable(self.idIsoSfName)
        self.triggerSf = [self.jsonTable.getEtaPtTable(x) for x in self.triggerLegNames]

    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'
        self.config = initVars['config']

        # prepare buffers for new branches to add
        self.branches = []
        self.branchBuffers = {}
        self.lastEntry = -1
        if not self.isData:
            for branchName in ['electronSF', 'electronSF_IdIso', 'electronSF_trigger']:
		self.branchBuffers[branchName] = array.array('f', [1.0, 1.0, 1.0])
                self.branches.append({'name': branchName, 'formula': self.getVectorBranch, 'arguments': {'branch': branchName, 'length':3}, 'length': 3})
            for branchName in ['electronSF_IdIso_B', 'electronSF_IdIso_E']:
                self.branchBuffers[branchName] = array.array('f', [1.0, 1.0])
                self.branches.append({'name': branchName, 'formula': self.getVectorBranch, 'arguments': {'branch': branchName, 'length':2}, 'length': 2})
#                for syst in self.systVariations:
#                    branchNameSyst = branchName+syst if syst else branchName
#                    self.branchBuffers[branchNameSyst] = array.array('f', [0])
#                    self.branches.append({'name': branchNameSyst, 'formula': self.getBranch, 'arguments': branchNameSyst}) 

    def getBranches(self):
        return self.branches

    # read from buffers which have been filled in processEvent()    
    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        # if current entry has not been processed yet
        if currentEntry != self.lastEntry and not self.isData:
            self.lastEntry = currentEntry

            zElectrons = vLeptonSelector(tree, config=self.config).getZelectrons()

       	    lep_eta = []
	    lep_pt = []
	    if len(zElectrons) == 2: 
       	     lep_eta = [zElectrons[0].eta,zElectrons[1].eta]
	     lep_pt = [zElectrons[0].pt,zElectrons[1].pt]

            self.computeSF(self.branchBuffers['electronSF_trigger'], self.branchBuffers['electronSF_IdIso'], self.branchBuffers['electronSF_IdIso_B'], self.branchBuffers['electronSF_IdIso_E'], self.branchBuffers['electronSF'], lep_eta, lep_pt, len(zElectrons), 1.566)


#            for syst in self.systVariations:
#                # require two electrons
#                if len(zElectrons) == 2: 
#                    sfIdIso = self.getIdIsoSf(eta=zElectrons[0].eta, pt=zElectrons[0].pt, syst=syst) * self.getIdIsoSf(eta=zElectrons[1].eta, pt=zElectrons[1].pt, syst=syst)
#                    sfTrigger = self.getTriggerSf(eta1=zElectrons[0].eta, pt1=zElectrons[0].pt, eta2=zElectrons[1].eta, pt2=zElectrons[1].pt, syst=syst)
#                else:
#                    sfIdIso = 1.0
#                    sfTrigger = 1.0
#                # Up/Down variations should be taken from individual components instead of total during the datacard creation
#                self.branchBuffers['electronSF' + (syst if syst else '')][0] = sfIdIso * sfTrigger
#                self.branchBuffers['electronSF_IdIso' + (syst if syst else '')][0] = sfIdIso
#                self.branchBuffers['electronSF_trigger' + (syst if syst else '')][0] = sfTrigger

        return True


#Separated weight_Iso in eta (Barrel/Endcap) :
#----------------------------------------------------------------------------------------------------
	 
    def computeSF(self, weight_trigg, weight_Iso, weight_Iso_LowEta, weight_Iso_HighEta, weight_SF, lep_eta, lep_pt, lep_n, etacut):

        '''Computes the trigger, IdIso (including separated variations in eta) and final event SF'''
        # require two electrons
#	print "Number of leptons {nl}".format(nl=lep_n)
	if lep_n == 2:

 	 #Calculating IdIso weights, separately for each electron
	 weight = []
	 for lep in [0,1]:
	  #weights_temp=[Nominal,Down,Up] for the corespondong lepton	 
	  weights_temp=[]
          for syst in self.systVariations:
	   weights_temp.append(self.getIdIsoSf(eta=lep_eta[lep], pt=lep_pt[lep], syst=syst))
	  weight.append(weights_temp)

	 #Calculating the trigger and IdIso weights and Down/Up variations
         for i, syst in enumerate(self.systVariations):
	  weight_trigg[i] = self.getTriggerSf(eta1=lep_eta[0], pt1=lep_pt[0], eta2=lep_eta[1], pt2=lep_pt[1], syst=syst)
	  weight_Iso[i] = weight[0][i] * weight[1][i]
	  weight_SF[i] = weight_trigg[i] * weight_Iso[i]

	 #Assignes the IdIso for different eta regions (Barrel : LowEta and Endcap : Higheta)
         if abs(lep_eta[0]) < etacut and abs(lep_eta[1]) < etacut:
             #assign sys
             weight_Iso_LowEta[0] = weight[0][1] * weight[1][1]
             weight_Iso_LowEta[1] = weight[0][2] * weight[1][2]
             #sys are nom value
             weight_Iso_HighEta[0] = weight[0][0] * weight[1][0]
             weight_Iso_HighEta[1] = weight[0][0] * weight[1][0]

         elif abs(lep_eta[0]) > etacut and abs(lep_eta[1]) > etacut:
             #sys are nom value
             weight_Iso_LowEta[0] = weight[0][0] * weight[1][0]
             weight_Iso_LowEta[1] = weight[0][0] * weight[1][0]
             #assign sys
             weight_Iso_HighEta[0] =  weight[0][1] * weight[1][1]
             weight_Iso_HighEta[1] =  weight[0][2] * weight[1][2]

         elif abs(lep_eta[0]) < etacut and abs(lep_eta[1]) > etacut:
             weight_Iso_LowEta[0] =  weight[0][1] * weight[1][0]
             weight_Iso_LowEta[1] =  weight[0][2] * weight[1][0]
             weight_Iso_HighEta[0] = weight[0][0] * weight[1][1]
             weight_Iso_HighEta[1] = weight[0][0] * weight[1][2]

         elif abs(lep_eta[0]) > etacut and abs(lep_eta[1]) < etacut:
             weight_Iso_LowEta[0] = weight[0][0] * weight[1][1]
             weight_Iso_LowEta[1] = weight[0][0] * weight[1][2]
             weight_Iso_HighEta[0] = weight[0][1] * weight[1][0]
             weight_Iso_HighEta[1] = weight[0][2] * weight[1][0]
	#This is when an event has more than 2 lepton
	else:
         for i, syst in enumerate(self.systVariations):
	  weight_trigg[i] = 1.
	  weight_Iso[i] = 1.
	  weight_SF[i] = 1.
	  if i <= 1:
	   weight_Iso_LowEta[i] = 1.0
	   weight_Iso_HighEta[i] = 1.0

	 
#-------------------------------------------------------------------------------------------------------

    def getIdIsoSf(self, eta, pt, syst=None):
        sf = self.jsonTable.find(self.idIsoSf, eta, pt, syst=syst)
        #if self.debug:
        #    print "id/iso eta:", eta, "pt:", pt, "->", sf
        return sf
    
    def getTriggerSf(self, eta1, pt1, eta2, pt2, syst=None):
        leg1 = self.jsonTable.find(self.triggerSf[0], eta1, pt1, syst=syst)
    
        leg2 = self.jsonTable.find(self.triggerSf[1], eta2, pt2, syst=syst)
        #if self.debug:
        #    print "leg1: eta:", eta1, " pt:", pt1, "->", leg1
        #    print "leg2: eta:", eta2, " pt:", pt2, "->", leg2
        #    print "-->", leg1*leg2
        return leg1*leg2

if __name__ == "__main__":
    sfObject = ElectronSFfromJSON([
            'weights/Zll/Electrons/VHbb2ElectronIDISO2017.json',
            'weights/Zll/Electrons/VHbb2ElectronTriggerLeg12017.json',
            'weights/Zll/Electrons/VHbb2ElectronTriggerLeg22017.json',
        ])
    print sfObject.getIdIsoSf(0.5, 50)
    print sfObject.getIdIsoSf(-2.5, 50)
    print sfObject.getIdIsoSf(2.5, 250)
    print sfObject.getIdIsoSf(-0.5, 250)
    print sfObject.getTriggerSf(0.5, 50, 1.1, 40)
