import ROOT

#prefix = "root://t3dcachedb03.psi.ch:1094/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V21/prep_v1/ZmmH.BestCSV.heppy."
#prefix = "root://t3dcachedb03.psi.ch:1094/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V21bis/singlesys_eandmu/ZmmH.BestCSV.heppy."
#prefix = "root://t3dcachedb03.psi.ch:1094/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V21bis/prep_eandmu/ZmmH.BestCSV.heppy."
#prefix = "root://t3dcachedb03.psi.ch:1094/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V21bis/singlesys_eandmu_v3/ZmmH.BestCSV.heppy."
prefix = "root://t3dcachedb03.psi.ch:1094/pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V22/prep_eandmu/ZmmH.BestCSV.heppy."


def getWeight(fileInc, fileB, region):

    countInc=0
    # print 'region',region,'\n'
    for file in fileInc:
        f = ROOT.TFile.Open(prefix+file+".root")
        # print 'adding',file
        tree = f.Get("tree")
        countInc    = countInc + 1.* tree.Draw("",region)
        # print 'countInc',countInc,'\n'
        #countInc    = 1.* tree.GetEntries(region)
        f.Close()

    countB=0
    for file in fileB:
        f = ROOT.TFile.Open(prefix+file+".root")
        # print 'adding',file
        tree = f.Get("tree")
        countB      = countB + 1.* tree.Draw("",region)
        # print 'countB',countB,'\n'
        #countB      = 1.* tree.GetEntries(region)
        f.Close()
#    print 'countInc is', countInc
#    print 'countB is', countB
    weight = countInc/(countB+countInc)
    return weight

def getExtWeight(files):

    Weights = []

    countWeights = 0
    for file in files:
        f = ROOT.TFile.Open(prefix+file+".root")
        tree = f.Get("tree")
        nevents = 1.* tree.Draw("","1")
        countWeights = countWeights + nevents
        Weights.append(nevents)
        f.Close()

#    print 'countWeights is'
    for weight, file in zip(Weights, files):
        print 'Weight for sample', file, 'is', weight/countWeights


ZLLjetsHT0       = ["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1"]
ZLLjetsHT100     = ["DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8","DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1"]
ZLLjetsHT200     = ["DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"]
ZLLjetsHT400     = ["DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1"]
ZLLjetsHT600     = ["DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8","DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1"]

ZLLBjets         = ["DYBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"]
ZLLjetsBGenFilter= ["DYJetsToLL_BGenFilter_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"]

#ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8
#ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1
#ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext2
#ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8
#ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1
#ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext2
#DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
#ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1
#ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_ext1

DYBJets          = "(lheNb>0)"
DYJetsBGenFilter = "(lheNb==0 && nGenStatus2bHad>0)"

HT0              = "(lheHT<100)"
HT100            = "(lheHT>100 && lheHT<200)"
HT200            = "(lheHT>200 && lheHT<400)"
HT400            = "(lheHT>400 && lheHT<600)"
HT600            = "(lheHT>600)"

########
#ZLL
########

#DYB

print "weightZBjetsHT0=\t%.2f\n"   %getWeight(ZLLjetsHT0,     ZLLBjets, HT0+"&&"+DYBJets)
print "weightZBjetsHT100=\t%.2f\n" %getWeight(ZLLjetsHT100,   ZLLBjets, HT100+"&&"+DYBJets)
print "weightZBjetsHT200=\t%.2f\n" %getWeight(ZLLjetsHT200,   ZLLBjets, HT200+"&&"+DYBJets)
print "weightZBjetsHT400=\t%.2f\n" %getWeight(ZLLjetsHT400,   ZLLBjets, HT400+"&&"+DYBJets)
print "weightZBjetsHT600=\t%.2f\n" %getWeight(ZLLjetsHT600,   ZLLBjets, HT600+"&&"+DYBJets)

print "weightZBjetsHT0=\t%.2f\n"   %getWeight(ZLLjetsHT0,     ZLLjetsBGenFilter, HT0+"&&"+DYJetsBGenFilter)
print "weightZBjetsHT100=\t%.2f\n" %getWeight(ZLLjetsHT100,   ZLLjetsBGenFilter, HT100+"&&"+DYJetsBGenFilter)
print "weightZBjetsHT200=\t%.2f\n" %getWeight(ZLLjetsHT200,   ZLLjetsBGenFilter, HT200+"&&"+DYJetsBGenFilter)
print "weightZBjetsHT400=\t%.2f\n" %getWeight(ZLLjetsHT400,   ZLLjetsBGenFilter, HT400+"&&"+DYJetsBGenFilter)
print "weightZBjetsHT600=\t%.2f\n" %getWeight(ZLLjetsHT600,   ZLLjetsBGenFilter, HT600+"&&"+DYJetsBGenFilter)

##If you use extension only
#getExtWeight(['ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8','ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1'])
#getExtWeight(['ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8','ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1','ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext2'])
#getExtWeight(['DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
#getExtWeight(['ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1','ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_ext1'])
getExtWeight(['DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
getExtWeight(['DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1'])
