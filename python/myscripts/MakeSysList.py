import ROOT
import sys

#print list of all variations used in the training step

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()

#VarList = ['HCMVAV2_reg_mass','HCMVAV2_reg_pt','HCMVAV2_reg_eta','HCMVAV2_reg_phi','hJetCMVAV2_pt_reg_0','hJetCMVAV2_pt_reg_1','hJetCMVAV2_pt_reg']

#List of BDT variables
#VarList_in = 'SYS_UD: HCMVAV2_reg_mass HCMVAV2_reg_pt VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi) Jet_btagCMVAV2[hJCMVAV2idx[0]] Jet_btagCMVAV2[hJCMVAV2idx[1]] hJetCMVAV2_pt_reg_0 hJetCMVAV2_pt_reg_1 V_new_mass Sum$(hJetCMVAV2_pt_reg>30&&abs(Jet_eta)<2.4&&Jet_puId==7&&Jet_id>0&&aJCidx!=(hJCMVAV2idx[0])&&(aJCidx!=(hJCMVAV2idx[1]))) V_new_pt (HCMVAV2_reg_pt/V_new_pt) abs(Jet_eta[hJCMVAV2idx[0]]-Jet_eta[hJCMVAV2idx[1]]) softActivityVH_njets5 VHbb::deltaR(HCMVAV2_reg_eta,HCMVAV2_reg_phi,V_new_eta,V_new_phi) met_pt'

#nominal
#VarList_in = 'SYS_UD: H_mass,H_pt,H_pt/V_pt,V_pt,Jet_btagCMVA[hJidxCMVA[1]],Jet_btagCMVA[hJidxCMVA[1]],top_mass,abs(TVector2::Phi_mpi_pi(H_phi-V_phi)),Sum$(Jet_PtReg>30&&abs(Jet_eta)<2.4&&Jet_puId>=4&&Jet_lepFilter&&Iteration$!=hJidxCMVA[0]&&Iteration$!=hJidxCMVA[1]),SA5,abs(TVector2::Phi_mpi_pi(-V_phi)),V_mt,MET,Jet_PtReg[hJidxCMVA[0]],Jet_pt[hJidxCMVA[1]],abs(Jet_eta[hJidxCMVA[0]]-Jet_eta[hJidxCMVA[1]]),((Jet_eta[hJidxCMVA[0]]-Jet_eta[hJidxCMVA[1]])**2+(TVector2::Phi_mpi_pi(Jet_phi[hJidxCMVA[0]]-Jet_phi[hJidxCMVA[1]]))**2)**0.5'

VarList_in = 'SYS_UD: H_mass_SYS_UD,H_pt_SYS_UD,H_pt_SYS_UD/V_pt,V_pt,Jet_btagCMVA[hJidxCMVA[1]],Jet_btagCMVA[hJidxCMVA[1]],top_mass,abs(TVector2::Phi_mpi_pi(H_phi-V_phi)),Sum$(Jet_pt_SYSUD>30&&abs(Jet_eta)<2.4&&Jet_puId>=4&&Jet_lepFilter&&Iteration$!=hJidxCMVA[0]&&Iteration$!=hJidxCMVA[1]),SA5,abs(TVector2::Phi_mpi_pi(-V_phi)),V_mt,MET,Jet_pt_SYSUD[hJidxCMVA[0]],Jet_pt_SYSUD[hJidxCMVA[1]],abs(Jet_eta[hJidxCMVA[0]]-Jet_eta[hJidxCMVA[1]]),((Jet_eta[hJidxCMVA[0]]-Jet_eta[hJidxCMVA[1]])**2+(TVector2::Phi_mpi_pi(Jet_phi[hJidxCMVA[0]]-Jet_phi[hJidxCMVA[1]]))**2)**0.5'

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
VarSysDic= ['H_pt_SYS_UD/V_pt','H_mass_SYS_UD','H_pt_SYS_UD','Sum$(Jet_pt_SYSUD>30&&abs(Jet_eta)<2.4&&Jet_puId>=4&&Jet_lepFilter&&Iteration$!=hJidxCMVA[0]&&Iteration$!=hJidxCMVA[1])','Jet_pt_SYSUD[hJidxCMVA[0]]','Jet_pt_SYSUD[hJidxCMVA[1]]']


VarList_new =  []
#SysList = ['JER','JEC']
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
