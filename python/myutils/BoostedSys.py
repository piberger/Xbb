#!/usr/bin/env python
import ROOT
import sys
import numpy as np
import array
import math as m

class BoostedSys(object):

    def __init__(self, JMS_SF, JMS_sys, JMR_SF, JMR_sys, tau21sys):
        #JMS_SF:    jet mass scale SF
        #JMS_sys:   jet mass scale systematic
        #JMR_SF:    jet mass resolution smearing SF
        #JMR_SF:    jet mass resolution smearing systematic
        self.JMS_SF  = JMS_SF 
        self.JMS_sys = JMS_sys
        self.JMR_SF  = JMR_SF
        self.JMR_sys = JMR_sys
        self.tau21sys= tau21sys


        self.branchBuffers = {}
        self.branches = []
        
        #JER smearing
        self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFat'] = array.array('f', [0])
        self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatUp'] = array.array('f', [0])
        self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatDown'] = array.array('f', [0])
        self.branches.append({'name': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJERFat', 'formula': self.getBranch, 'arguments': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJERFat'})
        self.branches.append({'name': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatUp', 'formula': self.getBranch, 'arguments': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatUp'})
        self.branches.append({'name': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatDown', 'formula': self.getBranch, 'arguments': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatDown'})

        #JEC scale
        self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFat'] = array.array('f', [0])
        self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatUp'] = array.array('f', [0])
        self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatDown'] = array.array('f', [0])
        self.branches.append({'name': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJESFat', 'formula': self.getBranch, 'arguments': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJESFat'})
        self.branches.append({'name': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatUp', 'formula': self.getBranch, 'arguments': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatUp'})
        self.branches.append({'name': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatDown', 'formula': self.getBranch, 'arguments': 'FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatDown'})

        #Tau21 systematics. Weight propagated at high pT. Taken from  https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#Systematic_uncertainties
        self.branchBuffers['tau21_weight_up']   = array.array('f', [0])
        self.branchBuffers['tau21_weight_down'] = array.array('f', [0])
        self.branches.append({'name': 'tau21_weight_up', 'formula': self.getBranch, 'arguments': 'tau21_weight_up'})
        self.branches.append({'name': 'tau21_weight_down', 'formula': self.getBranch, 'arguments': 'tau21_weight_down'})

    def getBranch(self, event, arguments=None):
        self.processEvent(event)
        if arguments:
            return self.branchBuffers[arguments][0]

    def getVectorBranch(self, event, arguments=None, destinationArray=None):
        self.processEvent(event)
        for i in range(arguments['length']):
            destinationArray[i] =  self.branchBuffers[arguments['branch']][i]

    def getBranches(self):
        return self.branches

    def processEvent(self, tree):
        #Not filled for the moment
        #JER smearing. Need to implement smearing procedure, but resolution variable needed

        if tree.nFatjetAK08ungroomed == 0:
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFat'][0] = 1
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatUp'][0] = 1
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatDown'][0] = 1

            #JER 
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFat'][0] = 1
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatUp'][0] = 1
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatDown'][0] = 1

            #tau21 systematic
            self.branchBuffers['tau21_weight_up'][0] = 1
            self.branchBuffers['tau21_weight_down'][0] = 1

        else:
            #print 'tree.Maxbbtagidx is', tree.Maxbbtagidx
            index = int(tree.Maxbbtagidx)
            mass = tree.FatjetAK08ungroomed_puppi_msoftdrop[index]
            pt = tree.FatjetAK08ungroomed_pt[index]
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFat'][0] = mass
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatUp'][0] = mass
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJERFatDown'][0] = mass

            #JER 
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFat'][0] = mass*self.JMS_SF
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatUp'][0] = mass*(self.JMS_SF + self.JMS_sys)
            self.branchBuffers['FatjetAK08ungroomed_puppi_msoftdrop_corrJESFatDown'][0] = mass*(self.JMS_SF - self.JMS_sys)

            #tau21 systematic
            self.branchBuffers['tau21_weight_up'][0] = (1.- self.tau21sys*m.log(pt/200.))
            self.branchBuffers['tau21_weight_down'][0] = (1. + self.tau21sys*m.log(pt/200.))

        return True

