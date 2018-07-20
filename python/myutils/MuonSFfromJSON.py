import json
import os
import array
from JsonTable import JsonTable
from vLeptons import vLeptonSelector

class MuonSFfromJSON(object):

    def __init__(self, jsonFiles=None):
        self.jsonFiles = jsonFiles
        self.debug = 'XBBDEBUG' in os.environ

        # load JOSN files
        self.jsonTable = JsonTable(jsonFiles)
        self.idSf = self.jsonTable.getEtaPtTable('NUM_LooseID_DEN_genTracks', 'abseta_pt')
        self.isoSf = self.jsonTable.getEtaPtTable('NUM_LooseRelIso_DEN_LooseID', 'abseta_pt')

    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'
        self.config = initVars['config']

        # prepare buffers for new branches to add
        self.branches = []
        self.branchBuffers = {}
        self.lastEntry = -1
        if not self.isData:
            for branchName in ['muonSF', 'muonSF_Id', 'muonSF_Iso', 'muonSF_trigger']:
                self.branchBuffers[branchName] = array.array('f', [1.0, 1.0, 1.0])
                self.branches.append({'name': branchName, 'formula': self.getBranch, 'arguments': branchName}) 

    def getBranches(self):
        return self.branches

    # read from buffers which have been filled in processEvent()    
    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def processEvent(self, tree):
        currentEntry = tree.GetReadEntry()
        # if current entry has not been processed yet
        if currentEntry != self.lastEntry and not self.isData:
            self.lastEntry = currentEntry

            vLeptons = vLeptonSelector(tree, config=self.config)
            zMuons = vLeptons.getZmuons()

            # require two muons
            if len(zMuons) == 2:
                sfId =       self.getIdSf(eta=zMuons[0].eta, pt=zMuons[0].pt) * self.getIdSf(eta=zMuons[1].eta, pt=zMuons[1].pt) 
                sfId_Down =  self.getIdSf(eta=zMuons[0].eta, pt=zMuons[0].pt) * self.getIdSf(eta=zMuons[1].eta, pt=zMuons[1].pt, syst='Down') 
                sfId_Up =    self.getIdSf(eta=zMuons[0].eta, pt=zMuons[0].pt) * self.getIdSf(eta=zMuons[1].eta, pt=zMuons[1].pt, syst='Up') 
                
                sfIso =      self.getIsoSf(eta=zMuons[0].eta, pt=zMuons[0].pt) * self.getIsoSf(eta=zMuons[1].eta, pt=zMuons[1].pt) 
                sfIso_Down = self.getIsoSf(eta=zMuons[0].eta, pt=zMuons[0].pt) * self.getIsoSf(eta=zMuons[1].eta, pt=zMuons[1].pt, syst='Down') 
                sfIso_Up =   self.getIsoSf(eta=zMuons[0].eta, pt=zMuons[0].pt) * self.getIsoSf(eta=zMuons[1].eta, pt=zMuons[1].pt, syst='Up') 

                sfTrigger =      self.getTriggerSf(eta1=zMuons[0].eta, pt1=zMuons[0].pt, eta2=zMuons[1].eta, pt2=zMuons[1].pt)
                sfTrigger_Down = self.getTriggerSf(eta1=zMuons[0].eta, pt1=zMuons[0].pt, eta2=zMuons[1].eta, pt2=zMuons[1].pt, syst='Down')
                sfTrigger_Up =   self.getTriggerSf(eta1=zMuons[0].eta, pt1=zMuons[0].pt, eta2=zMuons[1].eta, pt2=zMuons[1].pt, syst='Up')

                self.branchBuffers['muonSF'][0] = sfId * sfIso * sfTrigger
                self.branchBuffers['muonSF'][1] = sfId_Down * sfIso_Down * sfTrigger_Down
                self.branchBuffers['muonSF'][2] = sfId_Up * sfIso_Up * sfTrigger_Up
                self.branchBuffers['muonSF_Id'][0] = sfId
                self.branchBuffers['muonSF_Id'][1] = sfId_Down
                self.branchBuffers['muonSF_Id'][2] = sfId_Up
                self.branchBuffers['muonSF_Iso'][0] = sfIso
                self.branchBuffers['muonSF_Iso'][1] = sfIso_Down
                self.branchBuffers['muonSF_Iso'][2] = sfIso_Up
                self.branchBuffers['muonSF_trigger'][0] = sfTrigger
                self.branchBuffers['muonSF_trigger'][1] = sfTrigger_Down
                self.branchBuffers['muonSF_trigger'][2] = sfTrigger_Up
            else:
                for i in range(3):
                    self.branchBuffers['muonSF'][i] = 1.0
                    self.branchBuffers['muonSF_Id'][i] = 1.0
                    self.branchBuffers['muonSF_Iso'][i] = 1.0
                    self.branchBuffers['muonSF_trigger'][i] = 1.0
        return True

    def getIdSf(self, eta, pt, syst=None):
        return self.jsonTable.find(self.idSf, eta=eta, pt=pt, syst=syst)

    def getIsoSf(self, eta, pt, syst=None):
        return self.jsonTable.find(self.isoSf, eta=eta, pt=pt, syst=syst)
    
    def getTriggerSf(self, eta1, pt1, eta2, pt2, syst=None):
        leg1 = 1.0 #not implemented yet
        leg2 = 1.0 
        #define efficiency for MC and 
        effData_leg8 = []
        effData_leg17= []
        effMC_leg8= []
        effMC_leg17 = []
        #if self.debug:
        #    print "leg1: eta:", eta1, " pt:", pt1, "->", leg1
        #    print "leg2: eta:", eta2, " pt:", pt2, "->", leg2
        #    print "-->", leg1*leg2
        return leg1*leg2

if __name__ == "__main__":
    sfObject = MuonSFfromJSON([
            'weights/Zll/Muons/RunBCDEF_SF_ID.json',
            'weights/Zll/Muons/RunBCDEF_SF_ISO.json',
        ])
    print sfObject.getIdSf(0.5, 42)
    print sfObject.getIdSf(-0.5, 42)
    print sfObject.getIsoSf(1.5, 21)
    print sfObject.getIsoSf(-1.5, 21)
