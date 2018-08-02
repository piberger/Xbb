import ROOT
import sys

# print list of all variations used in the training step
# configured for Wlv (2016)

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()

#nominal
VarList_in = 'SYS_UD: H_mass_SYS_UD,H_pt_SYS_UD,V_pt,abs(TVector2::Phi_mpi_pi(H_phi-V_phi)),Jet_btagCMVA[hJidxCMVA[1]],MET,abs(TVector2::Phi_mpi_pi(Alt$(Muon_phi[tree.VMuonIdx[0]],0)+Alt$(Electron_phi[tree.VElectronIdx[0]],0)-V_phi)),top_mass,V_mt,Sum$(Jet_pt_SYSUD>25&&abs(Jet_eta)<2.5&&Jet_puId>0&&Jet_lepFilter&&Iteration$!=<!General|btagidx0!>&&Iteration$!=<!General|btagidx1!>),SA5'

#List of the systematics
JECsys = [
        'jer',
        'jesAbsoluteStat',
        'jesAbsoluteScale',
        'jesAbsoluteFlavMap',
        'jesAbsoluteMPFBias',
        'jesFragmentation',
        'jesSinglePionECAL',
        'jesSinglePionHCAL',
        'jesFlavorQCD',
        'jesRelativeJEREC1',
        'jesRelativeJEREC2',
        'jesRelativeJERHF',
        'jesRelativePtBB',
        'jesRelativePtEC1',
        'jesRelativePtEC2',
        'jesRelativePtHF',
        'jesRelativeBal',
        'jesRelativeFSR',
        'jesRelativeStatFSR',
        'jesRelativeStatEC',
        'jesRelativeStatHF',
        'jesPileUpDataMC',
        'jesPileUpPtRef',
        'jesPileUpPtBB',
        'jesPileUpPtEC1',
        'jesPileUpPtEC2',
        'jesPileUpPtHF',
        'jesPileUpMuZero',
        'jesPileUpEnvelope'
    ]

#List of the variables affected by the sys
VarSysDic= ['H_mass_SYS_UD','H_pt_SYS_UD','Sum$(Jet_pt_SYSUD>25&&abs(Jet_eta)<2.5&&Jet_puId>0&&Jet_lepFilter&&Iteration$!=<!General|btagidx0!>&&Iteration$!=<!General|btagidx1!>)']

VarList_new =  []
SysList = JECsys
UDList = ['Up','Down']
for syst in SysList:
    for ud in UDList:
        VarList = VarList_in
        for var in VarSysDic:
            if not var in VarList:
                print 'var:', var, 'not found'
                print 'Aborting'
                sys.exit()
            VarList = VarList.replace(var,var+"_corr"+syst+ud)
        VarList = VarList.replace('SYS',syst)
        VarList = VarList.replace('_UD','_'+ud)
        VarList_new.append(VarList)

print '==========================='
print 'PRINTING varlists'
print '==========================='
for var_new in VarList_new: 
    print var_new +'\n'

print '==========================='
print 'PRINTING systematicslist'
print '==========================='

systematics = 'systematics ='

for var_new in VarList_new: 
    systematics = systematics + ' ' +var_new.split(':')[0]
print systematics
