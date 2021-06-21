import sys
import os
import ROOT

fileForSync = open("DYToLL_HT100To200_Zlf_low_Zee_v2.txt", "w")

# selection Cut used for Nicks Zmm Zhf high comparison file
#selectionCut="(((hJidx[0]>-1&&hJidx[1]>-1) && !(boostedSR&&!resolvedSR)) && ((H_mass > 50) && (dPhiVH > 2.5) && V_mass > 85. && V_mass < 97. && MET_Pt < 60 && Jet_btagDeepB[hJidx[0]] > 0.6321 && Jet_btagDeepB[hJidx[1]] > 0.2217) && (H_mass < 90 || H_mass > 150)) && isZmm && (V_pt>=250.0)"

selectionCut = "(((hJidx[0]>-1&&hJidx[1]>-1) && !(boostedSR&&!resolvedSR)) && ((H_mass > 50) && (H_mass < 250) && V_mass > 75. && V_mass < 105. && Jet_btagDeepB[hJidx[0]] < 0.2217 && Jet_btagDeepB[hJidx[1]] < 0.2217 && (dPhiVH > 2.5) && (H_mass > 90 && H_mass < 150))) && isZee && (V_pt>=75.0&&V_pt<150.0)"

varsToCheck=["run","event","luminosityBlock","btagLeading","btagSubleading","H_mass","H_pt","MET_Pt","SA5","V_mass","V_pt","dPhiVH","ratiovpt","naddjet","maxFSR_var","minFSR_var", "weightF", "genWeight", "puWeight", "muonSF", "electronSF", "bTagWeightDeepCSV", "EWKw", "weightLOtoNLO_2016", "weightJetPUID", "PrefireWeight","StitchingWeight"]
#21 instances


varsToCheck_formula=["isZee","run","event","luminosityBlock","V_pt","hJidx","boostedSR","resolvedSR","dPhiVH", "V_mass","sWenu","isWmunu","H_mass","H_pt","nAddLep15_2p5","dPhiLepMet","Jet_btagDeepB","MET_sig30puid","isWmunu","MET_Pt","SA5","V_mt","V_pt","top_mass2_05","Jet_Pt","Jet_eta","Jet_puId","Jet_jetId","Jet_lepFilter","hJets_0_pt_FSRrecovered","hJets_1_pt_FSRrecovered","genWeight","puWeight","muonSF_Id", "muonSF_trigger", "muonSF_Iso", "electronSF", "boostedSR_VZ", "resolvedSR_VZ","EWKw","weightLOtoNLO_2016","weightJetPUID","bTagWeightDeepCSV","isZmm", "PrefireWeight","LHE_Nb","nGenStatus2bHad","LHE_Vpt","LHE_HT"]


treeName="Events"
for var in varsToCheck:
    fileForSync.write(str(var)+",")
fileForSync.write("\n")

print sys.argv
fileNames=sys.argv[1:]
print fileNames

for fileName in fileNames:
    tFile=ROOT.TFile.Open(fileName)
    tree=tFile.Get(treeName)


    tree.SetBranchStatus("*", 0)
    for branchName in varsToCheck_formula:
        tree.SetBranchStatus(branchName, 1)

    

    nEntries=tree.GetEntries()
   
    for iEntry in range(nEntries):
    #for iEntry in range(10000):
        tree.GetEntry(iEntry)
        if tree.Query("", selectionCut, "", 1, iEntry).GetRowCount() > 0:
            for var in varsToCheck:
                
                if "ratiovpt" in var:  
                    f_VptHpt = ROOT.TTreeFormula('f_VptHpt', 'V_pt/H_pt', tree )                  
                    f_VptHpt.GetNdata()                  
                    fileForSync.write(str((float)(f_VptHpt.EvalInstance()))+",") 
                
                elif "phi" in var:
                    f_phivar = ROOT.TTreeFormula('f_phivar', 'abs(TVector2::Phi_mpi_pi(V_phi-H_phi))', tree )                  
                    f_phivar.GetNdata()                   
                    fileForSync.write(str((int)(f_phivar.EvalInstance()))+",") 
                  
                elif "btagLeading" in var:
                    f_btagvarL=ROOT.TTreeFormula('f_btagvarL','Jet_btagDeepB[hJidx[0]]',tree)
                    f_btagvarL.GetNdata()
                    fileForSync.write(str((float)(f_btagvarL.EvalInstance()))+",")

                elif "btagSubleading" in var:
                    f_btagvarS=ROOT.TTreeFormula('f_btagvarS','Jet_btagDeepB[hJidx[1]]',tree)
                    f_btagvarS.GetNdata()   
                    fileForSync.write(str((float)(f_btagvarS.EvalInstance()))+",") 
                    
                elif "maxFSR" in var:
                    f_maxFSR=ROOT.TTreeFormula('f_maxFSR','max(hJets_0_pt_FSRrecovered,hJets_1_pt_FSRrecovered)',tree)   
                    f_maxFSR.GetNdata()   
                    fileForSync.write(str((float)(f_maxFSR.EvalInstance()))+",") 
                  
                elif "minFSR" in var:
                    f_minFSR=ROOT.TTreeFormula('f_minFSR','min(hJets_0_pt_FSRrecovered,hJets_1_pt_FSRrecovered)',tree)   
                    f_minFSR.GetNdata()   
                    fileForSync.write(str((float)(f_minFSR.EvalInstance()))+",") 
                  
                elif "naddjet" in var:
                    f_naddjet=ROOT.TTreeFormula('f_naddjet','Sum$(Jet_Pt>30&&abs(Jet_eta)<2.5&&(Jet_puId>6||Jet_Pt>50.0)&&Jet_jetId>2&&Jet_lepFilter&&Iteration$!=hJidx[0]&&Iteration$!=hJidx[1])',tree)   
                    f_naddjet.GetNdata()   
                    fileForSync.write(str((int)(f_naddjet.EvalInstance()))+",") 
                  
                elif "VH_Whf_medhigh_Wln_WP_resonly_22april" in var:
                    f_dnn = ROOT.TTreeFormula('f_dnn', 'VH_Whf_medhigh_Wln_WP_resonly_22april', tree )     
                    f_dnn.GetNdata()       
                    fileForSync.write(str((int)(f_dnn.EvalInstance()))+",")

                elif "muonSF" in var:
                    f_muonSF = ROOT.TTreeFormula('f_muonSF', 'muonSF[0]', tree )     
                    f_muonSF.GetNdata()      
                    fileForSync.write(str((float)(f_muonSF.EvalInstance()))+",")

                elif "electronSF" in var:
                    f_electronSF = ROOT.TTreeFormula('f_electronSF', 'electronSF[0]', tree )
                    f_electronSF.GetNdata()
                    fileForSync.write(str((float)(f_electronSF.EvalInstance()))+",")

                elif "EWKw" in var:
                    f_EWK = ROOT.TTreeFormula('f_EWK', 'EWKw[0]', tree )                                                     
                    f_EWK.GetNdata()                                                     
                    fileForSync.write(str((float)(f_EWK.EvalInstance()))+",")

                elif "weightF" in var:
                    f_weightF = ROOT.TTreeFormula('f_weightF', 'genWeight*puWeight*1.0*muonSF_Iso[0]*muonSF_Id[0]*muonSF_trigger[0]*electronSF[0]*(1.0+(((hJidx[0]>-1&&hJidx[1]>-1) && !(boostedSR&&!resolvedSR)) || ((hJidx[0]>-1&&hJidx[1]>-1) && !(boostedSR_VZ&&!resolvedSR_VZ)))*(-1.0+bTagWeightDeepCSV))*EWKw[0]*weightLOtoNLO_2016*1.0 * 1.0 * weightJetPUID * PrefireWeight', tree)
                    f_weightF.GetNdata()
                    fileForSync.write(str((float)(f_weightF.EvalInstance()))+",")

                elif "StitchingWeight" in var:
                    f_StitchingWeight = ROOT.TTreeFormula('f_StitchingWeight', '(1.0)*((LHE_Nb==0&&nGenStatus2bHad==0&&LHE_Vpt<100&&LHE_HT>=100&&LHE_HT<200)*0.68054 + (LHE_Nb==0&&nGenStatus2bHad>0&&LHE_Vpt<100&&LHE_HT>=100&&LHE_HT<200)*0.67236 + (LHE_Nb==0&&nGenStatus2bHad==0&&LHE_Vpt>=100&&LHE_Vpt<200&&LHE_HT>=100&&LHE_HT<200)*0.67944 + (LHE_Nb>0&&LHE_Vpt<100&&LHE_HT>=100&&LHE_HT<200)*0.68138)', tree)
                    f_StitchingWeight.GetNdata()
                    fileForSync.write(str((float)(f_StitchingWeight.EvalInstance()))+",")

                else:                  
                    fileForSync.write(str(getattr(tree,var))+",")
        

                
            fileForSync.write("\n")
           

    tFile.Close()

fileForSync.close()



