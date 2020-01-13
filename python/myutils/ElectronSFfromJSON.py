import json
import os
import array
from JsonTable import JsonTable
from vLeptons import vLeptonSelector
from BranchTools import Collection
from BranchTools import AddCollectionsModule

class ElectronSFfromJSON(AddCollectionsModule):
    
    def __init__(self, jsonFiles=None, branchName="electronSF",channel='None',year=2017):
        super(ElectronSFfromJSON, self).__init__()
        self.jsonFiles = jsonFiles
        self.debug = 'XBBDEBUG' in os.environ
        self.branchName = branchName

        # load JOSN files
        self.jsonTable = JsonTable(jsonFiles)
        self.channel = channel 
        self.trackerSfName = None
        if self.channel== 'Zll':
            #self.idIsoSfName = 'doubleEleIDISO2017'
            self.idIsoSfName = 'IDs2017passingMVA94Xwp90iso'
            #self.triggerLegNames = ['doubleEleTriggerLeg1', 'doubleEleTriggerLeg2']
            self.triggerLegNames = ['Trig{year}passingDoubleEleLeg1'.format(year=year), 'Trig{year}passingDoubleEleLeg2'.format(year=year)]
            self.trackerSfName = 'ScaleFactor_tracker_80x'
        elif self.channel == 'Wlv':
            #self.idIsoSfName = 'singleEleIDISO2017'
            self.idIsoSfName = 'IDs2017passingMVA94Xwp80iso'
            #self.triggerLegNames = ['singleEleTrigger']
            self.triggerLegNames = ['Trig{year}passingSingleEle'.format(year=year)]
            self.trackerSfName = 'ScaleFactor_tracker_80x'
        else: 
            print "Channel not defined!"
            raise Exception("ChannelNotDefined")

        self.systVariations = [None, 'Down', 'Up']
        self.idIsoSf = self.jsonTable.getEtaPtTable(self.idIsoSfName)
        self.triggerSf = [self.jsonTable.getEtaPtTable(x) for x in self.triggerLegNames]
        self.trackerSf = self.jsonTable.getEtaPtTable(self.trackerSfName)

    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'
        self.config = initVars['config']

        # prepare buffers for new branches to add
        if not self.isData:
            for x in ['', '_IdIso', '_trigger', '_tracker', '_IdIso_B', '_IdIso_E']:
                self.addVectorBranch(self.branchName + x, default=1.0, length=3)
    
    def processEvent(self, tree):
        # if current entry has not been processed yet
        if not self.hasBeenProcessed(tree) and not self.isData:
            self.markProcessed(tree)

            #TODO check the assigned weights for events with more than 2 letpns
            Vtype = tree.Vtype
            vLidx = []
            lep_eta = []
            lep_pt = []
         
            if self.channel == "Wlv" and Vtype == 3:
                vLidx = [tree.vLidx[0]]
                lep_pt = [tree.Electron_pt[vLidx[0]]]
                lep_eta = [tree.Electron_eta[vLidx[0]]]
            elif self.channel == "Zll" and Vtype ==1:
                vLidx = [tree.vLidx[0],tree.vLidx[1]]
                lep_pt = [tree.Electron_pt[vLidx[0]],tree.Electron_pt[vLidx[1]]]
                lep_eta = [tree.Electron_eta[vLidx[0]],tree.Electron_eta[vLidx[1]]]

            self.computeSF(
                        weight_trigg=self._b(self.branchName + '_trigger'),
                        weight_tracker=self._b(self.branchName + '_tracker'),
                        weight_Iso=self._b(self.branchName + '_IdIso'),
                        weight_Iso_LowEta=self._b(self.branchName + '_IdIso_B'),
                        weight_Iso_HighEta=self._b(self.branchName + '_IdIso_E'),
                        weight_SF=self._b(self.branchName),
                        lep_eta=lep_eta,
                        lep_pt=lep_pt,
                        lep_n=len(vLidx),
                        etacut=1.566
                    )

        return True


#Separated weight_Iso in eta (Barrel/Endcap) :
#----------------------------------------------------------------------------------------------------
    def computeSF(self, weight_trigg, weight_tracker, weight_Iso, weight_Iso_LowEta, weight_Iso_HighEta, weight_SF, lep_eta, lep_pt, lep_n, etacut):
        '''Computes the trigger, IdIso (including separated variations in eta) and final event SF'''
        # require two electrons

        if lep_n == 1 or lep_n == 2:
            #Calculating IdIso weights, separately for each electron
            weight = []
            for lep in range(lep_n):
                weights_temp = []
                for syst in self.systVariations:
                    weights_temp.append(self.getIdIsoSf(eta=lep_eta[lep], pt=lep_pt[lep], syst=syst))
                weight.append(weights_temp)

            #Calculating the trigger and IdIso weights and Down/Up variations
            for i, syst in enumerate(self.systVariations):
                weight_trigg[i] = self.getTriggerSf(lep_eta, lep_pt, lep_n, syst=syst)
                weight_tracker[i] = self.getTrackerSf(lep_eta, lep_pt, lep_n, syst=syst)
                weight_Iso[i] = weight[0][i] if lep_n == 1 else weight[0][i] * weight[1][i] 
                weight_SF[i] = weight_trigg[i] * weight_Iso[i] * weight_tracker[i]

            #Barrel and Endcap separated
            self.electronSf_BE(weight, weight_Iso_LowEta, weight_Iso_HighEta, lep_eta, lep_pt, lep_n, etacut)

        #This is when an event has 0 or more than 2 lepton
        else:
            for i, syst in enumerate(self.systVariations):
                weight_trigg[i] = 1.
                weight_Iso[i] = 1.
                weight_SF[i] = 1.
                weight_Iso_LowEta[i] = 1.0
                weight_Iso_HighEta[i] = 1.0

#-------------------------------------------------------------------------------------------------------

    def electronSf_BE(self, weight, weight_Iso_LowEta, weight_Iso_HighEta, lep_eta, lep_pt, lep_n, etacut):
        '''Assignes the IdIso for different eta regions (Barrel : LowEta and Endcap : Higheta)'''

        #Used for the Wlv channel
        weight_Iso_LowEta[2] = 1.0
        weight_Iso_HighEta[2] = 1.0
        if lep_n == 1:
          if abs(lep_eta[0]) < etacut:
              #assign sys
              weight_Iso_LowEta[0] = weight[0][1] 
              weight_Iso_LowEta[1] = weight[0][2]
              #sys are nom value
              weight_Iso_HighEta[0] = weight[0][0]
              weight_Iso_HighEta[1] = weight[0][0]
          elif abs(lep_eta[0]) > etacut:
              #sys are nom value
              weight_Iso_LowEta[0] = weight[0][0]
              weight_Iso_LowEta[1] = weight[0][0]
              #assign sys
              weight_Iso_HighEta[0] =  weight[0][1]
              weight_Iso_HighEta[1] =  weight[0][2]
 
        #Used for the Zll channel
        if lep_n == 2:
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


    def getIdIsoSf(self, eta, pt, syst=None):
        sf = self.jsonTable.find(self.idIsoSf, eta, pt, syst=syst)
        return sf
    
    def getTriggerSf(self, eta, pt, len_n, syst=None):
        triggSF = 1.
        for i in range(len_n):
            triggSF = triggSF * self.jsonTable.find(self.triggerSf[i], eta[i], pt[i], syst=syst)

        return triggSF
    
    def getTrackerSf(self, eta, pt, len_n, syst=None):
        SF = 1.
        for i in range(len_n):
            SF = SF * self.jsonTable.find(self.trackerSf, eta[i], pt[i], syst=syst)
        return SF

if __name__ == "__main__":
    sfObject = ElectronSFfromJSON([
            'data/Run2ElectronSF/Trig2017passingDoubleEleLeg1.json',
            'data/Run2ElectronSF/Trig2017passingDoubleEleLeg2.json',
            'data/Run2ElectronSF/IDs2017passingMVA94Xwp90iso.json',
        ], channel='Zll', year=2017)
    print sfObject.getIdIsoSf(0.5, 50)
    print sfObject.getIdIsoSf(-2.5, 50)
    print sfObject.getIdIsoSf(2.5, 250)
    print sfObject.getIdIsoSf(-0.5, 250)
    print sfObject.getTriggerSf([0.5, 1.1], [50, 30], 2)
