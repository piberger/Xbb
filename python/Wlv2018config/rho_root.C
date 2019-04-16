#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooRealVar.h"
#include "RooStats/SPlot.h"
#include "RooDataSet.h"
#include "RooRealVar.h"
#include "RooGaussian.h"
#include "RooExponential.h"
#include "RooChebychev.h"
#include "RooAddPdf.h"
#include "RooProdPdf.h"
#include "RooAddition.h"
#include "RooProduct.h"
#include "TCanvas.h"
#include "RooAbsPdf.h"
#include "RooFit.h"
#include "RooFitResult.h"
#include "RooWorkspace.h"
#include "RooConstVar.h"
#include <vector>
#include "RooPolynomial.h"
#include "RooRealProxy.h"
#include "RooListProxy.h"
#include "RooFormulaVar.h"
#include "RooDecay.h"
#include "RooGaussModel.h"
#include "RooDataHist.h"
#include "RooProdPdf.h"
#include "RooHistPdf.h"

#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <string>
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"
#include <cstring>
#include <sstream>
#include <stdlib.h>
#include <TH1.h>
#include <TF1.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TString.h>
#include "TColor.h"
#include "TAxis.h"
#include "TColor.h"
#include "TAxis.h"
#include "TLorentzVector.h"
#include <TMath.h>
#include <TLegend.h>

// use this order for safety on library loading
using namespace RooFit;
using namespace RooStats;
using namespace std;

void rho_root()
{
    TFile* file1 = new TFile("TMVA_output_splots.root");
    TTree* datatree = (TTree*)(file1->Get("tree"));

    double rho;
    datatree->SetBranchAddress("rho", &rho);

    TFile* r_file1 = new TFile("r_TMVA_output_splots.root");
    TTree* r_datatree = (TTree*)(r_file1->Get("tree"));

    double r_rho;
    r_datatree->SetBranchAddress("rho", &r_rho);

    TH1* data_p_rho = new TH1F("data_p_rho" ,"data_p_rho" ,100 , 0, 100);

    Long64_t nentries = datatree->GetEntries();

    for (Long64_t ientry=0; ientry < nentries; ientry++)
    {
        datatree->GetEntry(ientry);         
        data_p_rho->Fill(rho);
    }

    TH1* r_data_p_rho = new TH1F("r_data_p_rho" ,"r_data_p_rho" ,100 , 0, 100);

    Long64_t r_nentries = r_datatree->GetEntries();

    for (Long64_t r_ientry=0; r_ientry < r_nentries; r_ientry++)
    {
        r_datatree->GetEntry(r_ientry);
        r_data_p_rho->Fill(r_rho);
    }
        
    data_p_rho->Scale(1/data_p_rho->Integral());

    TCanvas* hist1 = new TCanvas("hist1","hist1");
    data_p_rho->Draw();
    hist1->Draw();

    r_data_p_rho->Scale(1/r_data_p_rho->Integral());

    TCanvas* hist2 = new TCanvas("hist2","hist2");
    r_data_p_rho->Draw();
    hist2->Draw();

    TH1* rho_ratio = new TH1F("rho_ratio" ,"rho_ratio" ,100 , 0, 100);
    rho_ratio->Divide(r_data_p_rho,data_p_rho);

    TCanvas* ratio = new TCanvas("ratio","ratio");
    rho_ratio->Draw();
    ratio->Draw();

    TF1 *func = new TF1("func","pol9",0,100);

//    r_data_p_rho->Fit(func);

}
    
 





