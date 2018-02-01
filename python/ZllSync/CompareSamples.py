import ROOT
import sys
from copy import copy

ROOT.gROOT.SetBatch(True)

ROOT.gSystem.Load("../../interface/VHbbNameSpace_h.so")

path_prefix = '/mnt/t3nfs01/data01/shome/gaperrin/VHbb/CMSSW_7_4_3/src/Xbb/python/WlvSync'

#RegionList = ['TTel','ZLFel','ZHFel','TTul','ZLFul','ZHFul','TTeh','ZLFeh','ZHFeh','TTuh','ZLFuh','ZHFuh']
RegionList = ['TTel']
SampleList = ['TT','ZHbb','DY400']
#total
#VarList = ['PU','genSign','bTag','dEtabb', 'NLOVpt', 'NLOewk','Wpt','eSelSF','uSelSF','eTrigSF','uTrigSF']
#VarList = ['PU','genSign','bTag','FitCorr', 'Vweight','LepSelSF','eTrigSF','uTrigSF']
#VarList = ['PU', Vtype]
#Delete those guys afterwards
##Heiner
#VarList = ['Vtype','lepPt','HT', 'CMVAmin',' Vmass', 'CMVAmax', 'Vpt','HVdPhi','lepRelIso1','nAddLeptons','lepMetDPhi','sigma_met_pt','jetleadpt','jetsubleadpt','puWeight','MET','BDT','Hmass','lepRelIso2','nAddJets']
#SampleVar_AT = {'Vtype':'Vtype_new','lepPt':'vLeptons_new_pt','HT':'cutFlow','CMVAmin':'CMVAmin','Vmass':'Vmass','CMVAmax':'CMVAmax','Vpt':'Vpt','cutFlow':'cutFlow','HVdPhi':'HVdPhi','lepRelIso1':'lepRelIso1','nAddLeptons':'nAddLeptons','lepMetDPhi':'lepMetDPhi','sigma_met_pt':'sigma_met_pt','jetleadpt':'jetleadpt','jetsubleadpt':'jetsubleadpt','':'controlSample','PU':'puWeight','MET':'met_pt','MetTkMetDPhi':'MetTkMetDPhi','count':'count','BDT':'BDT','Hmass':'Hmass','lepRelIso2':'lepRelIso2','nAddJets':'nAddJets','minMetjDPhi':'minMetjDPhi')

#Not sure (implementation)
#
#
#
VarList = ['Vtype']
#VarList = ['Vtype',
#    'lepPt',
#    'HT',
#    'CMVAmin',
#    'Vmass',
#    'CMVAmax',
#    'Vpt',
#    'HVdPhi',
#    'lepRelIso1',
#    'jetleadpt',
#    'jetsubleadpt',
#    'PU',
#    'MET',
#    'count',
#    'Hmass',
#    'lepRelIso2'
#]

SampleVar_Xbb = {'Vtype':'Vtype_new','lepPt':'vLeptons_new_pt[0]','HT':'lheHT','CMVAmin':'Jet_btagCMVAV2[hJCMVAV2idx[1]]','Vmass':'V_mass','CMVAmax':'Jet_btagCMVAV2[hJCMVAV2idx[0]]','Vpt':'V_pt','HVdPhi':'VHbb::deltaPhi(HCMVA_phi,V_phi)','lepRelIso1':'vLeptons_new_relIso04[0]','jetleadpt':'Jet_pt[hJCMVAV2idx[0]]','jetsubleadpt':'Jet_pt[hJCMVAV2idx[1]]','PU':'puWeight','MET':'met_pt','count':'1','Hmass':'HCMVAV2_mass','lepRelIso2':'vLeptons_new_relIso04[0]','nAddJets':'Sum$(Jet_pt>30 && abs(Jet_eta)<5.2 && Jet_puId>=4)'}

##
#RegionList = ['TTel','ZLFel','ZHFel','TTul','ZLFul','ZHFul','TTeh','ZLFeh','ZHFeh','TTuh','ZLFuh','ZHFuh']
#AT
SamplePath_Xbb = {'TT':'Xbb/Sample/TT.root','ZHbb':'Xbb/Sample/ZHbb.root','DY400':'Xbb/Sample/DYH400.root'}
#SampleVar_Xbb = {'PU':['puWeight', 50, 0, 2], 'genSign':['sign(genWeight)', 50, 0, 2],'bTag':['bTagWeightCMVAV2_Moriond', 50, 0, 2],'FitCorr':['FitCorr[0]', 50, 0, 2],'Vweight':['DYw[0]', 50, 0, 2],'LepSelSF':['weight_SF_Lepton[0]', 50, 0, 2],'eTrigSF':['eTrigSFWeight_singleEle80[0]', 50, 0, 2],'uTrigSF':['muTrigSFWeight_singlemu[0]', 50, 0, 2]}
RegionCut_Xbb = {
    'TTel':'(V_new_mass > 10 & (V_new_mass < 75 || V_new_mass > 120) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) & (Vtype_new == 1 && (abs(vLeptons_new_eta[0]) >= 1.57 || abs(vLeptons_new_eta[0]) <= 1.44) & (abs(vLeptons_new_eta[1])>=1.57 || abs(vLeptons_new_eta[1])<=1.44) && vLeptons_new_relIso03[0] < 0.15 && vLeptons_new_relIso03[1] < 0.15) & (V_new_pt > 50 & V_new_pt < 150)',
    'ZLFel':'((V_new_mass > 75. && V_new_mass < 105. && Jet_btagCMVAV2[hJCMVAV2idx[0]] < -0.5884 && Jet_btagCMVAV2[hJCMVAV2idx[1]] < -0.5884 && abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) && V_new_pt > 50) && (HCMVAV2_reg_mass > 90 && HCMVAV2_reg_mass < 150) & (Vtype_new == 1 && (abs(vLeptons_new_eta[0]) >= 1.57 || abs(vLeptons_new_eta[0]) <= 1.44) & (abs(vLeptons_new_eta[1])>=1.57 || abs(vLeptons_new_eta[1])<=1.44) && vLeptons_new_relIso03[0] < 0.15 && vLeptons_new_relIso03[1] < 0.15) & (V_new_pt > 50 & V_new_pt < 150)',
    'ZHFel':'(abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & V_new_mass > 85. & V_new_mass < 97. & met_pt < 60 & (HCMVAV2_reg_mass < 90 || HCMVAV2_reg_mass > 150) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884 &  (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20)) & V_new_pt > 50) & (Vtype_new == 1 && (abs(vLeptons_new_eta[0]) >= 1.57 || abs(vLeptons_new_eta[0]) <= 1.44) & (abs(vLeptons_new_eta[1])>=1.57 || abs(vLeptons_new_eta[1])<=1.44) && vLeptons_new_relIso03[0] < 0.15 && vLeptons_new_relIso03[1] < 0.15) & (V_new_pt > 50 & V_new_pt < 150)',
    'TTul':'(V_new_mass > 10 & (V_new_mass < 75 || V_new_mass > 120) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) & (Vtype_new == 0) & (V_new_pt > 50 & V_new_pt < 150)',
    'ZLFul':'((V_new_mass > 75. && V_new_mass < 105. && Jet_btagCMVAV2[hJCMVAV2idx[0]] < -0.5884 && Jet_btagCMVAV2[hJCMVAV2idx[1]] < -0.5884 && abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) && V_new_pt > 50) && (HCMVAV2_reg_mass > 90 && HCMVAV2_reg_mass < 150) & (Vtype_new == 0) & (V_new_pt > 50 & V_new_pt < 150)',
    'ZHFul':'(abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & V_new_mass > 85. & V_new_mass < 97. & met_pt < 60 & (HCMVAV2_reg_mass < 90 || HCMVAV2_reg_mass > 150) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884 &  (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20)) & V_new_pt > 50) & (Vtype_new == 0) & (V_new_pt > 50 & V_new_pt < 150)',
    'TTeh':'(V_new_mass > 10 & (V_new_mass < 75 || V_new_mass > 120) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) & (Vtype_new == 1 && (abs(vLeptons_new_eta[0]) >= 1.57 || abs(vLeptons_new_eta[0]) <= 1.44) & (abs(vLeptons_new_eta[1])>=1.57 || abs(vLeptons_new_eta[1])<=1.44) && vLeptons_new_relIso03[0] < 0.15 && vLeptons_new_relIso03[1] < 0.15) & (V_new_pt > 150)',
    'ZLFeh':'(abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & V_new_mass > 85. & V_new_mass < 97. & met_pt < 60 & (HCMVAV2_reg_mass < 90 || HCMVAV2_reg_mass > 150) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884 &  (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20)) & V_new_pt > 50) & (Vtype_new == 1 && (abs(vLeptons_new_eta[0]) >= 1.57 || abs(vLeptons_new_eta[0]) <= 1.44) & (abs(vLeptons_new_eta[1])>=1.57 || abs(vLeptons_new_eta[1])<=1.44) && vLeptons_new_relIso03[0] < 0.15 && vLeptons_new_relIso03[1] < 0.15) & (V_new_pt > 150)',
    'TTuh':' (V_new_mass > 10 & (V_new_mass < 75 || V_new_mass > 120) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) & (Vtype_new == 0) & (V_new_pt > 150)',
    'ZLFuh':'((V_new_mass > 75. && V_new_mass < 105. && Jet_btagCMVAV2[hJCMVAV2idx[0]] < -0.5884 && Jet_btagCMVAV2[hJCMVAV2idx[1]] < -0.5884 && abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20))) && V_new_pt > 50) && (HCMVAV2_reg_mass > 90 && HCMVAV2_reg_mass < 150) & (Vtype_new == 0) & (V_new_pt > 150)',
    'ZHFuh':'(abs(VHbb::deltaPhi(HCMVAV2_reg_phi,V_new_phi)) > 2.5  & V_new_mass > 85. & V_new_mass < 97. & met_pt < 60 & (HCMVAV2_reg_mass < 90 || HCMVAV2_reg_mass > 150) & Jet_btagCMVAV2[hJCMVAV2idx[0]] > 0.9432 & Jet_btagCMVAV2[hJCMVAV2idx[1]] > -0.5884 &  (BasicCutsCMVA && ( hJetCMVAV2_pt_reg_0 > 20 &&  hJetCMVAV2_pt_reg_1 > 20) && (vLeptons_new_pt[0]>20 && vLeptons_new_pt[1]>20)) & V_new_pt > 50) & (Vtype_new == 0) & (V_new_pt > 150)'
    }


#Analysis Tools
#Histograms location in files from Heiner
DirName = {'TTel':'CR_2Lepton_lowVpt_TTbar_El',
    'ZLFel':'CR_2Lepton_lowVpt_VpLF_El',
    'ZHFel':'CR_2Lepton_lowVpt_VpHF_El',
    'TTul':'CR_2Lepton_lowVpt_TTbar_Mu',
    'ZLFul':'CR_2Lepton_lowVpt_VpLF_Mu',
    'ZHFul':'CR_2Lepton_lowVpt_VpHF_Mu',
    'TTeh':'CR_2Lepton_highVpt_TTbar_El',
    'ZLFeh':'CR_2Lepton_highVpt_VpLF_El',
    'ZHFeh':'CR_2Lepton_highVpt_VpHF_El',
    'TTuh':'CR_2Lepton_highVpt_TTbar_Mu',
    'ZLFuh':'CR_2Lepton_highVpt_VpLF_Mu',
    'ZHFuh':'CR_2Lepton_highVpt_VpHF_Mu'
    }

#SamplePath_AT= {'AT/Heiner_mail_18_01_2018/CR_2Lept','AT/Heiner_mail_18_01_2018/CR_2Lept'}



SamplePath_AT= {'TT':'AT/Heiner_mail_18_01_2018/CR_2LeptREGION/TT_powheg.root','ZHbb':'AT/Heiner_mail_18_01_2018/CR_2LeptREGION/ZH125_powheg.root','DY400':'AT/Heiner_mail_18_01_2018/CR_2LeptREGION/DYToLL_HT400to600.root'}
#SampleVar_AT = {'PU':['puWeight', 50, 0, 2]}
#RegionCut_AT = {'TT':'selLeptons_relIso_0<0.06&&met_pt<170&&isWmunu&&Vtype==2&&controlSample==1'}



#MY
#VarList = ['PU','genSign','bTag','dEtabb', 'NLOVpt', 'NLOewk','Wpt','eSelSF','uSelSF','eTrigSF','uTrigSF']
#Heiner
#VarList = ['Vtype','lepPt','HT', 'CMVAmin',' Vmass', 'CMVAmax', 'Vpt','cutFlow','HVdPhi','lepRelIso1','nAddLeptons','lepMetDPhi','sigma_met_pt','jetleadpt','jetsubleadpt','controlSample','puWeight','MET','MetTkMetDPhi','count','BDT','Hmass','lepRelIso2','nAddJets','minMetjDPhi']
#To be used
#What is the cutFlow var ? count
#VarList = ['Vtype','lepPt','HT', 'CMVAmin',' Vmass', 'CMVAmax', 'Vpt','HVdPhi','lepRelIso1','nAddLeptons','jetleadpt','jetsubleadpt','puWeight','MET','BDT','Hmass','lepRelIso2','nAddJets', 'count']
SampleVar_AT = {'Vtype':'Vtype','lepPt':'lepPt','HT':'Hpt','CMVAmin':'CMVAmin','Vmass':'Vmass','CMVAmax':'CMVAmax','Vpt':'Vpt','cutFlow':'cutFlow','HVdPhi':'HVdPhi','lepRelIso1':'lepRelIso1','nAddLeptons':'nAddLeptons','lepMetDPhi':'lepMetDPhi','sigma_met_pt':'sigma_met_pt','jetleadpt':'jetleadpt','jetsubleadpt':'jetsubleadpt','':'controlSample','PU':'puWeight','MET':'met_pt','MetTkMetDPhi':'MetTkMetDPhi','count':'count','BDT':'BDT','Hmass':'Hmass','lepRelIso2':'lepRelIso2','nAddJets':'nAddJets','minMetjDPhi':'minMetjDPhi'}
##For test
#SampleVar_AT = {'PU':'puWeight'}

############
#Read all the AT histograms
############


def GetHisto(inputfile, region):
    '''Get all the histograms from a given region and inputfile'''
    histoList = {}
    file = ROOT.TFile.Open(inputfile,'read')
    nextkey = ROOT.TIter(ROOT.gDirectory.GetListOfKeys())
    key = nextkey.Next()
    #Loop over the region
    while (key):
        kname = key.GetName()
        if kname == DirName[region]:
            ROOT.gDirectory.cd(kname)
            #Loop over all the histograms
            nexth = ROOT.TIter(ROOT.gDirectory.GetListOfKeys())
            h = nexth.Next()
            #Loop over the variables
            while (h):
                hname = h.GetName()
                hobj = copy(ROOT.gDirectory.Get(hname))
                histoList[hname] = hobj
                h = nexth.Next()
            break
        key = nextkey.Next()
    return histoList

def MakeSampleDic(region, sampleList):
    '''For a given region, returns a dic like {'sample1':[variable1, variable2,...], 'sample2', [variable1, variable2,...]}'''
    SampleDic = {}

    #Check first if this is a low or high region
    LO = (region[-1] == 'l')
    Vpt = ''
    if LO: Vpt = 'LO'
    else: Vpt = 'HI'
    for s in sampleList:
        inputfile = SamplePath_AT[s].replace('REGION',Vpt)
        SampleDic[s] = GetHisto(inputfile, region)
    return SampleDic

def MakeRegionDic(regionList, sampleList):
    '''For a given region, returns a dic like {'region':'{'sample1':[variable1, variable2,...], 'sample2', [variable1, variable2,...]}'}'''
    RegionDic = {}
    for r in regionList:
        RegionDic[r] = MakeSampleDic(r, sampleList)
    return RegionDic



##For test
hlist = GetHisto('AT/Heiner_mail_18_01_2018/CR_2LeptLO/DYToLL_HT400to600.root', 'ZLFel')
print 'hlist is', hlist
#sys.exit()
#slist = MakeSampleDic('ZLFel', SampleList)
#print 'slist is', slist
#rlist = MakeRegionDic(RegionList, SampleList)
#print 'rlist is', rlist

#Create dic organising all the histograms from AT
AT_AllHist = MakeRegionDic(RegionList, SampleList)
#print 'AT_AllHist', AT_AllHist

#sys.exit()


#To check variables in common subregion

for region in RegionList:
    print '========='
    print region
    print '========='
    for sample in SampleList:
        #Xbb
        file_Xbb = ROOT.TFile.Open(SamplePath_Xbb[sample],'read')
        tree_Xbb = file_Xbb.Get('tree')
        print tree_Xbb.GetName()
        ##AT
        #file_AT = ROOT.TFile.Open(SamplePath_AT[sample],'read')
        #tree_AT = file_AT.Get('tree')
        #print tree_AT.GetName()

        #Count the number of entries
        n_Xbb =  tree_Xbb.GetEntries(RegionCut_Xbb[region])
        #n_AT = tree_AT.GetEntries(RegionCut_AT[region])

        #print '\n'
        #print sample
        #print 'Xbb yield:', n_Xbb
        #print 'AT  yield:', n_AT
        #print '\n'


        #Make plots for all the relevant variables
        for var in VarList:



            #print '-------------------'
            #print AT_AllHist[region][sample]
            #sys.exit()
            h_AT = AT_AllHist[region][sample][SampleVar_AT[var]]
            nbins= h_AT.GetNbinsX()
            xmin = h_AT.GetXaxis().GetBinLowEdge(1)
            xmax = h_AT.GetXaxis().GetBinLowEdge(nbins+1)

            #h_AT = ROOT.TH1F('h_AT','h_AT',SampleVar_AT[var][1], SampleVar_AT[var][2], SampleVar_AT[var][3])
            #tree_AT.Draw('%s>>%s' %(SampleVar_AT[var][0], 'h_AT'), RegionCut_AT[region])

            h_Xbb = ROOT.TH1F('h_Xbb','h_Xbb', nbins, xmin, xmax)
            tree_Xbb.Draw('%s>>%s' %(SampleVar_Xbb[var], 'h_Xbb'), RegionCut_Xbb[region])

            c = ROOT.TCanvas('c','c')
            c.cd()

            h_Xbb.Draw()
            h_Xbb.SetLineColor(2)
            h_Xbb.SetLineWidth(4)
            if not h_Xbb.Integral() == 0:
                h_Xbb.Scale(1./h_Xbb.Integral())
            h_AT.Draw('SAME')
            h_AT.SetLineColor(4)
            h_AT.SetLineStyle(2)
            h_AT.SetLineWidth(4)
            if not h_AT.Integral() == 0:
                h_AT.Scale(1./h_AT.Integral())

            leg = ROOT.TLegend(0.1,0.7,0.48,0.9)
            leg.AddEntry(h_Xbb, 'Xbb')
            leg.AddEntry(h_AT, 'AT')
            leg.Draw()

            c.SaveAs('%s_%s_%s.pdf'%(region, sample,var))
            c.SaveAs('%s_%s_%s.png'%(region, sample,var))
            c.SaveAs('%s_%s_%s.root'%(region,sample,var))





