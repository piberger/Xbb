
import ROOT
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()

###
##Check the regression sys
###

#pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V24/TEST2/ZmmH.BestCSV.heppy.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1.root'
#
#f = ROOT.TFile.Open(pathin_)
#t = f.Get("tree")
#
#
#VarList = ['HCSV_reg_corrSYSUD_mass_CAT','HCSV_reg_corrSYSUD_pt_CAT', 'HCSV_reg_corrSYSUD_eta_CAT', 'HCSV_reg_corrSYSUD_phi_CAT','Jet_pt_reg_corrSYSUD_CAT_INDEX0','Jet_pt_reg_corrSYSUD_CAT_INDEX1', 'Sum$(Jet_pt_reg_corrSYSUD_CAT>30&&abs(Jet_eta)<2.4&&Jet_puId==7&&Jet_id>0&&aJCidx!=(hJCidx[0])&&(aJCidx!=(hJCidx[1])))']

###
##Check the BDT sys
###

#pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/mva_v8_TEST/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1/tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_4_a4085e20b6f3529b24861250b2d0c6748eed84fb3c9aaa402e946fba.root'

#ggZH
#pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/mva_v8_TEST/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1/'
#samples = [
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_4_a4085e20b6f3529b24861250b2d0c6748eed84fb3c9aaa402e946fba.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_9_7f43c75a51e986047797368d61b0e129bd516cb6bbc352c27f45b9d5.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_8_d69e2347f2937091e04e1166b308e7a41e16093409f1a0307f579312.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_10_0b3bbe9fe3cea647800b090931bd71801a809fec58316d4a7c11486b.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_15_939abb159fc830426dc23d69faa8879ffe7368ca6335454ca837ca5b.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_7_5f20f77bb644898056c698188a541ded17c21977297436090aac8b0a.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_14_4ae2e179a4ee6dec44672623dc4cf09b9f114e64c7f86bd0faaa9ebd.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_13_97e54c6de510f4c14f3d57a3b55d0965b9bf62672a2e35affceeb9be.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_5_0bda7591462d83c3be00525505f4ec7d8e8a28ce0d5f92737eb1b6bf.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_2_fbed43b47595a1cc25dc19e73aad98be133b83c2b51562c8f376e529.root',
#    'tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_3_129622619d1951fd2b9b51f45d5a2c70e9fd03cebb908d1ff886c2b6.root'
#]

##TT
pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/mva_v8_TEST/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/'
samples = [
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_107_007bca9e66cf6f1c3dad019168f9c948710b17bbb6e0e661354dc62f.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_105_01791181a29c348d598953248563ac7ee759cc28a1b8f16d25527daa.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_104_6696428a7a465ec3ecc3fe6fc31a178c4d9d008adf8df6e599164af9.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_109_358beee1c028e979339b62cc246d2ad1ed78bf9affe71204bda03514.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_111_7900a4f8938ceddb9bb4cbe9862442a3ff388d57d69cad08cbf9ab09.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_121_8ac4c195017b31a26e9c1f464c8e744e48a59c380cc1da4b26196373.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_106_df8a615ba5a8cea6647457a7d9df9bff95d576012af2b4c6d02640d4.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_123_03adf478c8b4ed5e6ba1db4e8dc4e8469f1b10c2806d2ccdd66e7e8f.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_113_ecabbc203a609b5ebb64857858217508f7da7a9dc1c2c4fd616e20bb.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_122_d429190290a4b0ab4f1a76f5857055a485b4adcc60d5890dc06aa9e8.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_124_26a08f4735c4bf018d49653e3e34e448b52bc46e6a7f54e3f0e82d45.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_108_138861f5ae1d3d53d994362b4b84e61eff3632af424345319dc173c7.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_11_fd0b1fb3ceee4420ceccf430236f804b99a599e8cbbede9dab5a7a12.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_112_3868fa6ed8f42493366d94f162cc2b967dfafbc228271221afdc810c.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_10_8395ca95ed627552b4d8f527773685b8c5029d8f1f70657aca0bf31c.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_117_07232e75a3f495820a897e2cbed0a7c75ba1d616fee601f4038d13cb.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_115_373e6bfeb242bfbb45f65719774e87c6eb3de15de1cd585a1e44fc4d.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_100_df9fc7c09d4acf15ca44512a591708161adc52ea326bd99a896e1403.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_126_28595e5d0116df6c1ea71b71ec2f0433611da0beb19ecb2dd76f7279.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_114_6f6107580dd57acf7ca8bb54cca05b2fc98d9f208170ca09c71fb568.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_102_25914c40297b81d16f864c1d89d3fdbe09a9f0644aa8bf1e38f1d4c7.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_1_f7c3226f659cfff828e62ba5f18ed3a81ed69fbd444e24c650b07faa.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_103_fa041d00270d0d33597ad2c4ea857c1885c0c9b6774aaf9a7c71633e.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_101_063dc50096a9f009483706e6784696a12b7fda28d41d258caf408d06.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_120_244a2b387a45d6f036ab452adf31c53f553004d13b0006db10e67c03.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_110_0ca0f195771fa1aa0511faf4dcc9e4b0f87ef9027650d436db53437a.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_119_49c230fc4df8f21be5e274627e66328c560314888e60828e904cc7c2.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_116_04cbdf819d0a47e683b61ecdb54ba9cc09f7775d3ad728cc3d008637.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_12_e0f491c6310ad1f498dc6be57dfa64db97318ae400ddff852753ca89.root',
    'tree_VHBB_HEPPY_V25_TT_TuneCUETP8M2T4_13TeV-powheg-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1_118_d4d3315145cff71278378a92ce6d9fcc1be19a1bc8a6192f14347c79.root'
]

##TChain
t = ROOT.TChain('tree')
for sample in samples:
    t.Add(pathin_+sample+'/tree')


##TFile
#f = ROOT.TFile.Open(pathin_)
#t = f.Get("tree")


VarList = ['ZllBDT_highptCMVA.SYS_UD']

JECsys = [
    "JER",
    "PileUpDataMC",
    "PileUpPtRef",
    "PileUpPtBB",
    "PileUpPtEC1",
    "RelativeJEREC1",
    "RelativeFSR",
    "RelativeStatFSR",
    "RelativeStatEC",
    "RelativePtBB",
    "RelativePtEC1",
    "AbsoluteScale",
    "AbsoluteMPFBias",
    "AbsoluteStat",
    "SinglePionECAL",
    "SinglePionHCAL",
    "Fragmentation"
    ]

SysList = JECsys
UDList = ['Up','Down']
#CatList = ['HighCentral','LowCentral','HighForward','LowForward']
AxisList = {'mass':[20,0,400],'HCSV_reg_pt':[20,0,400],'phi':[20,-3.2, 3.2],'eta':[20,0,5],'Jet_pt':[20,0,300],'CMVA':[20,-1,1]}
for var in VarList:
    for syst in SysList:
        #for cat in CatList:
        c = ROOT.TCanvas('c','c',800,800) 
        pad1 = ROOT.TPad('pad1','pad1', 0, 0.3, 1, 1.0)
        pad1.SetBottomMargin(0)
        pad1.SetGridx()
        pad1.Draw()
        pad1.cd()

        nbin = 0
        xmin = 0
        xmax = 0
        var_nom = var.replace('SYSUD','').replace('_CAT','').replace('_corr','').replace('.SYS_UD','.Nominal')
        for axis in AxisList:
            if axis in var_nom:
                nbin = AxisList[axis][0]
                xmin = AxisList[axis][1]
                xmax = AxisList[axis][2]

        h_nom = ROOT.TH1D('h_nom','h_nom',nbin, xmin, xmax)
        print 'var nom is', var_nom
        if 'Jet_pt' in var_nom:
            if '_INDEX0'in var_nom: t.Draw(var_nom.replace('_INDEX0','[hJCidx[0]]')+'>>h_nom')
            elif '_INDEX1'in var_nom: t.Draw(var_nom.replace('_INDEX1','[hJCidx[1]]')+'>>h_nom')
        else:
            t.Draw(var_nom+'>>h_nom')
        h_nom.SetLineColor(1)
        h_nom.SetMarkerStyle(20)
        h_nom.SetMarkerColor(1)
        h_nom.SetLineWidth(2)
        h_nom.Sumw2()

        h_ud = {} 
        for ud in UDList:
            #fill Dic
            SysDic = {}
            SysDic['var'] = var 
            SysDic['sys'] = syst
            SysDic['UD'] = ud 
            #SysDic['cat'] = cat 
            #SysDic['varname'] = var.replace('SYS',syst).replace('UD',ud).replace('CAT',cat)
            SysDic['varname'] = var.replace('SYS',syst).replace('UD',ud)
            h_ud[ud] = ROOT.TH1D('h_%s'%ud,'h_%s'%ud,nbin, xmin, xmax)
            if 'Jet_pt' in SysDic['varname']:
                if '_INDEX0'in SysDic['varname']: 
                    t.Draw(SysDic['varname'].replace('_INDEX0','[hJCidx[0]]')+'>>h_%s'%ud)
                elif '_INDEX1'in SysDic['varname']: 
                    t.Draw(SysDic['varname'].replace('_INDEX1','[hJCidx[1]]')+'>>h_%s'%ud)
            else:
                t.Draw(SysDic['varname']+'>>h_%s'%ud)
            #h_ud[ud].Draw('same')
            #t.Draw(SysDic['varname'])

        h_nom.Draw()
        h_nom.GetXaxis().SetTitle(var_nom)
        h_ud['Up'].Draw('same')
        h_ud['Up'].SetLineColor(4)
        h_ud['Up'].SetLineStyle(4)
        h_ud['Up'].SetLineWidth(2)
        h_ud['Up'].GetYaxis().SetNdivisions(505)
        h_ud['Up'].GetYaxis().SetTitleSize(20)
        h_ud['Up'].GetYaxis().SetTitleFont(43)
        h_ud['Up'].GetYaxis().SetTitleOffset(1.55)
        h_ud['Up'].GetYaxis().SetLabelFont(43)
        h_ud['Up'].GetYaxis().SetLabelSize(15)
        h_ud['Up'].GetXaxis().SetTitleSize(20)
        h_ud['Up'].GetXaxis().SetTitleFont(43)
        h_ud['Up'].GetXaxis().SetTitleOffset(4.)
        h_ud['Up'].GetXaxis().SetLabelFont(43)
        h_ud['Up'].GetXaxis().SetLabelSize(15)
        h_ud['Up'].GetXaxis().SetTitle(var_nom)

        h_ud['Down'].Draw('same')
        h_ud['Down'].SetLineColor(2)
        h_ud['Down'].SetLineStyle(2)
        h_ud['Down'].SetLineWidth(2)


        leg = ROOT.TLegend(0.7, 0.8, 1 , 1)
        leg.AddEntry(h_nom,'nominal')
        leg.AddEntry(h_ud['Up'],'up')
        leg.AddEntry(h_ud['Down'],'down')
        leg.Draw('same')

        c.cd()
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        pad2.SetTopMargin(0)
        pad2.SetBottomMargin(0.2)
        pad2.SetGridx()
        pad2.SetGridy()
        pad2.Draw()
        pad2.cd()

        ratio_up =  h_ud['Up'].Clone()
        ratio_up.Divide(h_nom) 
        ratio_up.Draw()
        ratio_up.GetYaxis().SetRangeUser(0.9,1.1)
        ratio_down =  h_ud['Down'].Clone()
        ratio_down.Divide(h_nom) 
        ratio_down.Draw('same')

        c.SaveAs('TT_MVANumUpDown/'+SysDic['varname']+'.pdf')
        c.SaveAs('TT_MVANumUpDown/'+SysDic['varname']+'.png')
        c.SaveAs('TT_MVANumUpDown/'+SysDic['varname']+'.root')
        c.SaveAs('TT_MVANumUpDown/'+SysDic['varname']+'.C')

