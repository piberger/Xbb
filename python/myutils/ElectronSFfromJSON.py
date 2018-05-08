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
        self.systVariations = [None, 'Up', 'Down']
        self.idIsoSf = self.jsonTable.getEtaPtTable(self.idIsoSfName)
        self.triggerSf = [self.jsonTable.getEtaPtTable(x) for x in self.triggerLegNames]

    def customInit(self, initVars):
        sample = initVars['sample']
        self.isData = sample.type == 'DATA'

        # prepare buffers for new branches to add
        self.branches = []
        self.branchBuffers = {}
        self.lastEntry = -1
        if not self.isData:
            for branchName in ['electronSF', 'electronSF_IdIso', 'electronSF_trigger']:
                for syst in self.systVariations:
                    branchNameSyst = branchName+syst if syst else branchName
                    self.branchBuffers[branchNameSyst] = array.array('f', [0])
                    self.branches.append({'name': branchNameSyst, 'formula': self.getBranch, 'arguments': branchNameSyst}) 

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

            zElectrons = vLeptonSelector(tree).getZelectrons()
            
            for syst in self.systVariations:
                # require two electrons
                if len(zElectrons) == 2: 
                    sfIdIso = self.getIdIsoSf(eta=zElectrons[0].eta, pt=zElectrons[0].pt, syst=syst) * self.getIdIsoSf(eta=zElectrons[1].eta, pt=zElectrons[1].pt, syst=syst)
                    sfTrigger = self.getTriggerSf(eta1=zElectrons[0].eta, pt1=zElectrons[0].pt, eta2=zElectrons[1].eta, pt2=zElectrons[1].pt, syst=syst)
                else:
                    sfIdIso = 1.0
                    sfTrigger = 1.0
                # Up/Down variations should be taken from individual components instead of total during the datacard creation
                self.branchBuffers['electronSF' + (syst if syst else '')][0] = sfIdIso * sfTrigger
                self.branchBuffers['electronSF_IdIso' + (syst if syst else '')][0] = sfIdIso
                self.branchBuffers['electronSF_trigger' + (syst if syst else '')][0] = sfTrigger
        return True

    def getIdIsoSf(self, eta, pt, syst=None):
        sf = self.jsonTable.find(self.idIsoSf, eta, pt, syst=syst)
        if self.debug:
            print "id/iso eta:", eta, "pt:", pt, "->", sf
        return sf
    
    def getTriggerSf(self, eta1, pt1, eta2, pt2, syst=None):
        leg1 = self.jsonTable.find(self.triggerSf[0], eta1, pt1, syst=syst)
        leg2 = self.jsonTable.find(self.triggerSf[1], eta2, pt2, syst=syst)
        if self.debug:
            print "leg1: eta:", eta1, " pt:", pt1, "->", leg1
            print "leg2: eta:", eta2, " pt:", pt2, "->", leg2
            print "-->", leg1*leg2
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
