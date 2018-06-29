#!/usr/bin/env python
import ROOT
from BranchTools import Collection
from BranchTools import AddCollectionsModule
import array

# create branches for gen level particles with HEPPY naming (only for those used)
class HeppyStyleGen(AddCollectionsModule):

    def __init__(self, debug=False):
        self.debug = debug
        super(HeppyStyleGen, self).__init__()

    def customInit(self, initVars):
        self.sampleTree = initVars['sampleTree']
        self.isData = initVars['sample'].isData()
        if not self.isData:
            self.addCollection(Collection('GenVbosons', ['pt','pdgId','GenPartIdx'], maxSize=40))
            self.addCollection(Collection('GenTop', ['pt','GenPartIdx'], maxSize=4))
            self.addCollection(Collection('GenHiggsBoson', ['pt','GenPartIdx'], maxSize=4))
        
            self.branchBuffers['VtypeSim'] = array.array('i', [0])
            self.branches.append({'name': 'VtypeSim', 'formula': self.getBranch, 'arguments': 'VtypeSim', 'type': 'i'})
    
    def processEvent(self, tree):
        if not self.hasBeenProcessed(tree):
            self.markProcessed(tree)

            if not self.isData:
                higgsParticles = []
                vParticles = []
                tParticles = []

                genParticles = self.sampleTree.getCollection('GenPart')
                for idx in range(genParticles.size()):
                    if genParticles.pdgId[idx] == 25 and genParticles.genPartIdxMother[idx] == 0:
                        higgsParticles.append({'pt': genParticles.pt[idx], 'GenPartIdx': idx})
                    if genParticles.pdgId[idx] in [23, 24, -24]:
                        vParticles.append({'pt': genParticles.pt[idx], 'pdgId': genParticles.pdgId[idx], 'daughters': [], 'GenPartIdx': idx})
                    if genParticles.pdgId[idx] in [-6, 6] and genParticles.genPartIdxMother[idx] == 0:
                        tParticles.append({'pt': genParticles.pt[idx], 'GenPartIdx': idx})

                    for vParticle in vParticles:
                        if genParticles.genPartIdxMother[idx] == vParticle['GenPartIdx']:
                            vParticle['daughters'].append({'pdgId': genParticles.pdgId[idx], 'GenPartIdx': idx})


                # only keep last V which decays into leptons
                oldLen = len(vParticles)
                vParticles = [x for x in vParticles if len(x['daughters'])>0 and x['pdgId']!=x['daughters'][0]['pdgId']]
               
                # write collections
                self.collections['GenHiggsBoson'].fromList(higgsParticles)
                self.collections['GenVbosons'].fromList(vParticles)
                self.collections['GenTop'].fromList(tParticles)

                # get VtypeSim
                VtypeSim = -1
                if len(vParticles) == 1:
                    vParticle = vParticles[0]
                    if vParticle['pdgId'] == 23 and len(vParticle['daughters'])>1 and abs(vParticle['daughters'][0]['pdgId'])==abs(vParticle['daughters'][1]['pdgId']):
                        if abs(vParticle['daughters'][0]['pdgId']) == 11:
                            VtypeSim = 1
                        elif abs(vParticle['daughters'][0]['pdgId']) == 13:
                            VtypeSim = 0
                        elif abs(vParticle['daughters'][0]['pdgId']) == 15:
                            VtypeSim = 5
                        elif abs(vParticle['daughters'][0]['pdgId']) in [12,14,16]:
                            VtypeSim = 4
                    elif abs(vParticle['pdgId']) == 24 and len(vParticle['daughters'])==2:
                        if (abs(vParticle['daughters'][0]['pdgId']) == 11 and abs(vParticle['daughters'][1]['pdgId']) == 12) or (abs(vParticle['daughters'][0]['pdgId']) == 12 and abs(vParticle['daughters'][1]['pdgId']) == 11):
                            VtypeSim = 3
                        elif (abs(vParticle['daughters'][0]['pdgId']) == 13 and abs(vParticle['daughters'][1]['pdgId']) == 14) or (abs(vParticle['daughters'][0]['pdgId']) == 14 and abs(vParticle['daughters'][1]['pdgId']) == 13):
                            VtypeSim = 2
                elif len(vParticles) == 2:
                    VtypeSim = -2
                self.branchBuffers['VtypeSim'][0] = VtypeSim


        return True

