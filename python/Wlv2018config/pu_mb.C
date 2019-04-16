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
#include <TLatex.h>
#include "TColor.h"
#include "TAxis.h"
#include "TColor.h"
#include "TAxis.h"
#include "TLorentzVector.h"
#include <TMath.h>
#include <TLegend.h>
#include "cmath" 


using namespace RooFit;
using namespace RooStats;
using namespace std;

//TH1D* getMC_hist(TString inputfile, TH1D *h1);
TH1D* getdata_hist(TString mbxsec);
void plot_ratio(TH1D* data_pu,TH1D* mc_pu_1, TH1D* mc_pu_2, TH1D* mc_pu_3, TH1D* mc_pu_4, TH1D* data_pu_5, TH1D* data_pu_6, TString s1, TString s2, TString s3, TString s4, TString s5, TString s6);
void plot_660(TH1D* mc_pu,TH1D* mc_pu_rwt_660, TH1D* data_pu_660);


TString s1 = "/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/Wlv2018config/PU_hist/MyDataPileupHistogram_mbxsec_";
TString s2 = ".root";

void pu_mb()
{   
//    TFile* file1 = new TFile("/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2018/runplot-12mar-v3/Plots/ttu__Pileup_nPU_.root");
/*
    TFile* file1 = new TFile("/afs/cern.ch/user/c/capalmer/public/VHbb/pileup2018.root"); 
    file1->ls();

    TCanvas *c = (TCanvas *)file1->Get("pu_nom");	
    TCanvas *c_up = (TCanvas *)file1->Get("pu_up");
    TCanvas *c_down = (TCanvas *)file1->Get("pu_down");

    TGraph *g = (TGraph*)c->GetPrimitive("pu_nom");
    TGraph *g_up = (TGraph*)c_up->GetPrimitive("pu_up");
    TGraph *g_down = (TGraph*)c_down->GetPrimitive("pu_down");

    g->Clear();
    g_up->Clear();
    g_down->Clear();

    auto nPoints = g->GetN();
    double data_rho[100];
    cout<<nPoints<<endl;
   

    TProfile *data  = new TProfile("pileup","pileup",100,0,100,0,1);
    for(int i=0; i < nPoints; ++i) 
    {
        double x,y;
        g->GetPoint(i, x, y);
        data->Fill(x,y); 
        data_rho[i] = y;
    }

    TProfile *data_up  = new TProfile("pileup","pileup",100,0,100,0,1);
    for(int i=0; i < nPoints; ++i)
    {
        double x,y;
        g_up->GetPoint(i, x, y);
        data_up->Fill(x,y);        
    }
        
    TProfile *data_down  = new TProfile("pileup","pileup",100,0,100,0,1);
    for(int i=0; i < nPoints; ++i)
    {
        double x,y;
        g_down->GetPoint(i, x, y);
        data_down->Fill(x,y);     
    }
    
*/   

    TProfile *mc_pu_profile = new TProfile("pileup","pileup",100,0,100,0,1);
    TProfile *mc_pu_profile_rwt_660 = new TProfile("mc_pu_profile_rwt_660","mc_pu_profile_rwt_660",100,0,100,0,1);

    double x[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99};

    double y[] = {4.695341*pow(10,-10), 1.206213*pow(10,-6), 1.162593*pow(10,-6), 6.118058*pow(10,-6), 1.626767*pow(10,-5), 3.508135*pow(10,-5), 7.12608*pow(10,-5), 0.0001400641, 0.0002663403, 0.0004867473, 0.0008469, 0.001394142, 0.002169081, 0.003198514, 0.004491138, 0.006036423, 0.007806509, 0.00976048, 0.0118498, 0.01402411, 0.01623639, 0.01844593, 0.02061956, 0.02273221, 0.02476554, 0.02670494, 0.02853662, 0.03024538, 0.03181323, 0.03321895, 0.03443884, 0.035448, 0.03622242, 0.03674106, 0.0369877, 0.03695224, 0.03663157, 0.03602986, 0.03515857, 0.03403612, 0.0326868, 0.03113936, 0.02942582, 0.02757999, 0.02563551, 0.02362497, 0.02158003, 0.01953143, 0.01750863, 0.01553934, 0.01364905, 0.01186035, 0.01019246, 0.008660705, 0.007275915, 0.006043917, 0.004965276, 0.004035611, 0.003246373, 0.002585932, 0.002040746, 0.001596402, 0.001238498, 0.0009533139, 0.0007282885, 0.000552306, 0.0004158005, 0.0003107302, 0.0002304612, 0.0001696012, 0.0001238161, 8.96531*pow(10,-5), 6.438087*pow(10,-5), 4.585302*pow(10,-5), 3.23949*pow(10,-5), 2.271048*pow(10,-5), 1.580622*pow(10,-5), 1.09286*pow(10,-5), 7.512748*pow(10,-6), 5.140304*pow(10,-6), 3.505254*pow(10,-6), 2.386437*pow(10,-6), 1.625859*pow(10,-6), 1.111865*pow(10,-6), 7.663272*pow(10,-7), 5.350694*pow(10,-7), 3.808318*pow(10,-7), 2.781785*pow(10,-7), 2.098661*pow(10,-7), 1.642811*pow(10,-7), 1.312835*pow(10,-7), 1.081326*pow(10,-7), 9.141993*pow(10,-8), 7.890983*pow(10,-8), 6.91468*pow(10,-8), 6.119019*pow(10,-8), 5.443693*pow(10,-8), 4.85036*pow(10,-8), 4.31486*pow(10,-8), 3.822112*pow(10,-8)};

    double pu_66[] = {11211.394439494106, 16.292218459826124, 52.51571442439952, 21.68266432332575, 14.329960252403486, 10.310664659901956, 7.594378755030866, 5.6766099912501895, 4.24159936604362, 3.268939722057175, 2.6693797071949734, 2.301336336694521, 2.0704991838218714, 1.9233914718088363, 1.833362829237541, 1.7838479931338431, 1.7606928701631681, 1.7503329922187238, 1.7401375055879362, 1.7197138837787993, 1.6827855378201575, 1.6287253817588454, 1.562300197534378, 1.4911301760572442, 1.4224595839420935, 1.36122961807162, 1.3096871558098409, 1.2678902610837974, 1.2345628788225238, 1.2078158271118324, 1.1856940895402925, 1.166417453629219, 1.1483399018664004, 1.1297820406673487, 1.1089204967914246, 1.083809540460237, 1.0525818815102819, 1.0137121811313974, 0.9662800809819212, 0.9101367417761889, 0.8459660907967447, 0.7752312631706615, 0.6999958555206172, 0.622704405813786, 0.5459214317933418, 0.47205360308548655, 0.40311629490166007, 0.34056195157532065, 0.28523072897386353, 0.23738657909681085, 0.19681887982111984, 0.16297301765763791, 0.1350843939195093, 0.11229823310880921, 0.09375799530465541, 0.07866768528118954, 0.06633098851632448, 0.05616539837910282, 0.04770224735131212, 0.040576684461480675, 0.03451257662715626, 0.02930626457449734, 0.02481036367521389, 0.020919040633320573, 0.017555037255882245, 0.014658944556386423, 0.012181386571766047, 0.01007785352101093, 0.008305937959522051, 0.006824433036765718, 0.005593621741234151, 0.004576074431069572, 0.003737548867115925, 0.003047659820899512, 0.0024801863278975165, 0.002013053827537605, 0.001628047268913978, 0.0013103584976870248, 0.0010480625486745435, 0.0008315966365566472, 0.0006532716812076916, 0.0005068659193270776, 0.00038729841973123783, 0.00029038622334682124, 0.00021267064046364654, 0.0001512873200678384, 0.00010384659677809482, 6.829392834273135*pow(10,-5), 4.2744000946559064*pow(10,-5), 2.5336965830696364*pow(10,-5), 1.4453274453140426*pow(10,-5), 7.857298607023454*pow(10,-6), 4.086800626662558*pow(10,-6), 2.04437433796376*pow(10,-6), 9.8900821440477*pow(10,-7), 4.6508512001802176*pow(10,-7), 2.1353996309784114*pow(10,-7), 9.608021755375838*pow(10,-8), 4.2493273070323666*pow(10,-8), 1.8521345806913333*pow(10,-8)};

    for (Int_t i = 0; i < 100; i++)
    {
        mc_pu_profile->Fill(x[i],y[i]);
	mc_pu_profile_rwt_660->Fill(x[i],y[i]*pu_66[i]);
    }

    TH1D *mc_pu = mc_pu_profile->ProjectionX("pileup","e");
    TH1D *mc_pu_rwt_660 = mc_pu_profile_rwt_660->ProjectionX("check","e");

    TFile* file_mc_pu = new TFile("/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/Wlv2018config/pu_hist/mc_pu.root","RECREATE");
    mc_pu->Write();
    file_mc_pu->Close();
    file_mc_pu->Delete();


    TH1D *data_pu_300 = getdata_hist("30000");   
    TH1D *data_pu_400 = getdata_hist("40000");
    TH1D *data_pu_500 = getdata_hist("50000");
    TH1D *data_pu_600 = getdata_hist("60000");
    TH1D *data_pu_605 = getdata_hist("60500");
    TH1D *data_pu_610 = getdata_hist("61000");
    TH1D *data_pu_615 = getdata_hist("61500");
    TH1D *data_pu_620 = getdata_hist("62000");
    TH1D *data_pu_625 = getdata_hist("62500");
    TH1D *data_pu_630 = getdata_hist("63000");
    TH1D *data_pu_635 = getdata_hist("63500");
    TH1D *data_pu_640 = getdata_hist("64000");
    TH1D *data_pu_645 = getdata_hist("64500");
    TH1D *data_pu_650 = getdata_hist("65000");
    TH1D *data_pu_655 = getdata_hist("65500");
    TH1D *data_pu_660 = getdata_hist("66000");
    TH1D *data_pu_665 = getdata_hist("66500");
    TH1D *data_pu_670 = getdata_hist("67000");
    TH1D *data_pu_675 = getdata_hist("67500");
    TH1D *data_pu_680 = getdata_hist("68000");
    TH1D *data_pu_685 = getdata_hist("68500");
    TH1D *data_pu_690 = getdata_hist("69000");
    TH1D *data_pu_692 = getdata_hist("69200");
    TH1D *data_pu_695 = getdata_hist("69500");
    TH1D *data_pu_700 = getdata_hist("70000");
    TH1D *data_pu_705 = getdata_hist("70500"); 
    TH1D *data_pu_710 = getdata_hist("71000");
    TH1D *data_pu_715 = getdata_hist("71500");
    TH1D *data_pu_720 = getdata_hist("72000");
    TH1D *data_pu_725 = getdata_hist("72500");
    TH1D *data_pu_730 = getdata_hist("73000");
    TH1D *data_pu_735 = getdata_hist("73500");
    TH1D *data_pu_740 = getdata_hist("74000");
    TH1D *data_pu_745 = getdata_hist("74500");
    TH1D *data_pu_750 = getdata_hist("75000");
    TH1D *data_pu_755 = getdata_hist("75500");
    TH1D *data_pu_760 = getdata_hist("76000");
    TH1D *data_pu_765 = getdata_hist("76500");
    TH1D *data_pu_770 = getdata_hist("77000");
    TH1D *data_pu_775 = getdata_hist("77500");
    TH1D *data_pu_780 = getdata_hist("78000");
    TH1D *data_pu_785 = getdata_hist("78500");
    TH1D *data_pu_790 = getdata_hist("79000");
    TH1D *data_pu_795 = getdata_hist("79500");
    TH1D *data_pu_800 = getdata_hist("80000");
    TH1D *data_pu_900 = getdata_hist("90000");

/*
    TCanvas *closure_660 = new TCanvas("closure_660","closure_660",800,600);
    mc_pu_rwt_660->SetLineColor(kBlue);
    data_pu_660->SetLineColor(kRed);
    mc_pu->SetLineColor(kBlack);
    mc_pu_rwt_660->Draw("HIST");
    data_pu_660->Draw("E SAME");
    mc_pu->Draw("HIST SAME");
    closure_660->Draw();
*/

//    plot_ratio(mc_pu, data_pu_600, data_pu_620, data_pu_640, data_pu_660, data_pu_680, data_pu_670, "_60_0", "_68_0", "_69_0", "_70_0", "_71_0", "_72_0");


    TProfile *chisq_rho_ = new TProfile("chisq_rho","chisq_rho",40,50,90,0,100);
    TProfile *chisq_npv_ = new TProfile("chisq_npv","chisq_npv",40,50,90,0,100);

    double x_rho[] = {60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73};
    double x_npv[] = {71, 72, 73, 74, 75, 76, 77, 78, 79, 80};
    double x_mjj[] = {60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80};

    double rho_[] = {64.82, 48.88, 36.16, 26.49, 19.73, 15.76, 14.44, 15.64, 19.26, 25.18, 33.28, 43.45, 55.57, 69.51};
    double rho_whf_[] = {33.96, 25.06, 18.13, 13.06, 9.73, 8.08, 8.00, 9.43, 12.29, 16.50, 21.97, 28.64, 36.41, 45.19}; 

    //double npv_[] = {1136.16, 924.69, 750.62, 606.57, 487.00, 387.68, 305.33, 237.35, 181.66, 136.54, 100.58, 72.58, 51.51, 36.51, 26.84, 21.85, 20.99, 23.76, 29.74, 38.56, 49.88};
    double npv_[] = {72.58, 51.51, 36.51, 26.84, 21.85, 20.99, 23.76, 29.74, 38.56, 49.88};
    double npv_whf_[] = {46.73, 33.50, 24.15, 18.22, 15.26, 14.91, 16.84, 20.78, 26.49, 33.74};

    double mjj_[] = {2.51, 2.58, 2.65, 2.72, 2.78, 2.85, 2.91, 2.98, 3.05, 3.11, 3.18, 3.25, 3.32, 3.38, 3.45, 3.52, 3.59, 3.66, 3.73, 3.79, 3.86};
    double mjj_whf_[] = {4.20, 4.34, 4.48, 4.61, 4.74, 4.85, 4.97, 5.07, 5.15, 5.23, 5.29, 5.33, 5.36, 5.36, 5.34, 5.29, 5.22, 5.12, 4.98, 4.82, 4.62};


/*
    for (Int_t i = 0; i < (sizeof(rho_) / sizeof(rho_[0])); i++)
    {
        chisq_rho_->Fill(x_rho[i], rho_[i]);   
    }


    for (Int_t i = 0; i < (sizeof(npv_) / sizeof(npv_[0])); i++)
    {
        chisq_npv_->Fill(x_npv[i], npv_[i]);
    }



    TH1D *chisq_rho = chisq_rho_->ProjectionX("chisq_rho","e");
    TH1D *chisq_npv = chisq_npv_->ProjectionX("chisq_npv","e");
*/    
    TCanvas *chisq = new TCanvas("chisq/ndf","chisq/ndf",800,600);
/*    chisq_rho->SetLineColor(kBlue);
    chisq_npv->SetLineColor(kRed);
    chisq_rho->Draw("L");
    chisq_npv->Draw("L SAME");
*/

    TGraph *chisq_rho = new TGraph(14,x_rho,rho_whf_);
    TGraph *chisq_npv = new TGraph(10,x_npv,npv_whf_);
    TGraph *chisq_mjj = new TGraph(21,x_mjj,mjj_whf_);
/*
    TGraph *chisq_rho = new TGraph(14,x_rho,rho_);
    TGraph *chisq_npv = new TGraph(10,x_npv,npv_);
    TGraph *chisq_mjj = new TGraph(21,x_mjj,mjj_);
*/
    chisq_rho->SetLineColor(46);
    chisq_npv->SetLineColor(8);
    chisq_mjj->SetLineColor(9);
    chisq_rho->SetLineWidth(3);
    chisq_npv->SetLineWidth(3);
    chisq_mjj->SetLineWidth(3);
    chisq_rho->SetMarkerColor(1);
    chisq_npv->SetMarkerColor(1);
    chisq_mjj->SetMarkerColor(1);
    chisq_rho->SetMarkerStyle(21);
    chisq_npv->SetMarkerStyle(21);
    chisq_mjj->SetMarkerStyle(21);
    chisq_rho->SetTitle("#chi^{2}/ndf");
    chisq_rho->GetXaxis()->SetTitle("data_nPU");
    chisq_rho->GetYaxis()->SetTitle("#chi^{2}/ndf");
    TAxis *axis = chisq_rho->GetXaxis();
    axis->SetLimits(55.,85.);       
//    chisq_rho->GetHistogram()->SetMaximum(75.);            
    chisq_rho->GetHistogram()->SetMaximum(50.);
    chisq_rho->GetHistogram()->SetMinimum(0.);  
    chisq_rho->Draw("apl");
    chisq_npv->Draw("pl same");
    chisq_mjj->Draw("pl same");

    TLegend* l = new TLegend(0.6516547,0.7688758,0.807482,1.02674,NULL,"brNDC");
    TLegend* la;
    la = l;
    la->AddEntry(chisq_rho,"#rho","l");
    la->AddEntry(chisq_npv,"nPV","l");
    la->AddEntry(chisq_mjj,"mjj","l");
    la->SetTextFont(12);
    la->SetTextSize(0.06237499);
    la->SetBorderSize(0);
    la->SetFillColor(0);
    la->Draw("same");

    chisq->Update();

    TH1D* ndata_pu_660 = data_pu_660;
    TH1D* nmc_pu_rwt_660 = mc_pu_rwt_660;
    TH1D* nmc_pu = mc_pu;
  
    plot_660(nmc_pu,nmc_pu_rwt_660,ndata_pu_660);

    //plot_ratio(mc_pu, data_pu_600, data_pu_620, data_pu_640, data_pu_660, data_pu_680, data_pu_692, "_60_0", "_62_0", "_64_0", "_66_0", "_68_0", "_69_2");
    //plot_ratio(mc_pu, data_pu_700, data_pu_720, data_pu_740, data_pu_760, data_pu_780, data_pu_800, "_70_0", "_72_0", "_74_0", "_76_0", "_78_0", "_80_0");
}

TH1D* getdata_hist(TString mbxsec)
{
    TFile* file2 = new TFile(s1+mbxsec+s2);
    file2->ls();

    //*(&h1) = (TH1D*)file2->Get("pileup");
    TH1D *h1 = (TH1D*)file2->Get("pileup");
    h1->Scale(1/h1->Integral());

    TFile* file_data_pu = new TFile("/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/Wlv2018config/pu_hist/data_pu_" + mbxsec + ".root","RECREATE");
    h1->Write();
    file_data_pu->Close();
    file_data_pu->Delete();

    return h1;
}
/*
    g->Clear();
    g_up->Clear();
    g_down->Clear();




    TCanvas *g1 = new TCanvas("g1","g1",800,600);
    TH1D *data_pu = data->ProjectionX("pileup","e");
    data_pu->Draw("E");
    g1->Draw();

    TH1D *data_pu_up = data_up->ProjectionX("pileup","e");
    TH1D *data_pu_down = data_down->ProjectionX("pileup","e");    


    TFile* file_data_pu = new TFile("data_pu.root","RECREATE");
    data_pu->Write();
    file_data_pu->Close();
    file_data_pu->Delete();

    TFile* file_data_pu_up = new TFile("data_pu_up.root","RECREATE");
    data_pu_up->Write();
    file_data_pu_up->Close();
    file_data_pu_up->Delete();

    TFile* file_data_pu_down = new TFile("data_pu_down.root","RECREATE");
    data_pu_down->Write();
    file_data_pu_down->Close();
    file_data_pu_down->Delete();




//    TCanvas *g2 = new TCanvas("g2","g2",800,600) ;
//    TH1D *mc_pu = mc->ProjectionX();
*/

/*    g2->Divide(1,2);
    g2->cd(1);
    gPad->SetPad(0,0.33,1,0.9378806);
    data_pu->Draw();
    mc_pu->Draw("same");
    g2->cd(2);
    gPad->SetPad(0.0,0.0,1.0,0.33);
    ratio->Draw("hist");
    g2->Draw();   
*/

/*
    double r[100];
    TH1D *ratio = new TH1D("ratio","ratio",100,0,100);
    ratio->GetYaxis()->SetRangeUser(0,2);    
    for(int i=0; i<100; i++)
    {
	r[i] = data_rho[i]/y[i];
        ratio->Fill(i+0.5,r[i]);
        cout<<i<<" for value "<<r[i]<<endl;
    }
*/	
/*    
    TH1D *mc_pu = mc->ProjectionX("pileup","e");

    TFile* file_mc_pu = new TFile("mc_pu.root","RECREATE");
    mc_pu->Write();
    file_mc_pu->Close();
    file_mc_pu->Delete();



    TCanvas *g3 = new TCanvas("g3","g3",800,600) ;
    TH1D *ratio = new TH1D("ratio","ratio",100,0,100);
    ratio->Sumw2();
    ratio->Divide(data_pu,mc_pu);
    ratio->Draw("E");
    cout<<ratio->GetBinError(20);
     
   //data_pu->Divide(mc_pu); 
    //data_pu->Draw();
    //g3->Draw();

*/

void plot_ratio(TH1D* mc_pu,TH1D* data_pu_1, TH1D* data_pu_2, TH1D* data_pu_3, TH1D* data_pu_4, TH1D* data_pu_5, TH1D* data_pu_6, TString s1, TString s2, TString s3, TString s4, TString s5, TString s6)
{
    TCanvas *g2 = new TCanvas(s1,s1,800,600) ;
    g2->Range(0,0,1,1);
    g2->SetFillColor(0);
    g2->SetBorderMode(0);
    g2->SetBorderSize(2);
    g2->SetFrameBorderMode(0);
    gStyle->SetPadBorderMode(0);
    g2->Divide(1,2);
    g2->cd(1);
    gPad->Range(-69.03766,-0.0002509835,628.8703,0.06681207);
    gPad->SetGridx();
    gPad->SetTopMargin(0.006574267);
    gPad->SetBottomMargin(0.001912046);
    mc_pu->SetLineColor(kBlack);
    data_pu_1->SetLineColor(kRed);
    data_pu_2->SetLineColor(kMagenta+2);
    data_pu_3->SetLineColor(kGreen+2);
    data_pu_4->SetLineColor(kYellow+3);
    data_pu_5->SetLineColor(kBlue+1);
    data_pu_6->SetLineColor(kPink+10);
    gPad->SetPad(0,0.33,1,0.9378806);
       
    mc_pu->Sumw2();
    data_pu_1->Sumw2();
    THStack* hs = new THStack();
    hs->Add(mc_pu,"HIST");
    hs->Add(data_pu_1,"HIST");
    hs->Add(data_pu_2,"HIST");
    hs->Add(data_pu_3,"HIST");
    hs->Add(data_pu_4,"HIST");       
    hs->Add(data_pu_5,"HIST");
    hs->Add(data_pu_6,"HIST");
    hs->Draw("nostack");
    hs->GetHistogram()->GetXaxis()->SetLabelOffset(999);
    hs->GetHistogram()->GetXaxis()->SetTitle("");
    hs->GetHistogram()->GetYaxis()->SetTitle("");
    hs->GetHistogram()->GetYaxis()->SetTitleOffset(1.4);
    hs->GetHistogram()->GetYaxis()->SetTitleSize(0.03);
    hs->GetHistogram()->GetYaxis()->SetLabelSize(0.03);
    hs->GetHistogram()->GetYaxis()->CenterTitle();
    TLegend* la = new TLegend(0.6516547,0.7688758,0.857482,1.292674,NULL,"brNDC");
    TLegend* l1a;
    l1a = la;
    l1a->AddEntry(mc_pu,"MC","l");
    l1a->AddEntry(data_pu_1,"data"+s1,"l");
    l1a->AddEntry(data_pu_2,"data"+s2,"l");
    l1a->AddEntry(data_pu_3,"data"+s3,"l");
    l1a->AddEntry(data_pu_4,"data"+s4,"l");
    l1a->AddEntry(data_pu_5,"data"+s5,"l");
    l1a->AddEntry(data_pu_6,"data"+s6,"l");
    l1a->SetTextFont(12);
    l1a->SetTextSize(0.06237499);
    l1a->SetBorderSize(0);
    l1a->SetFillColor(0);
    l1a->Draw("same");



    g2->cd(2);
    gPad->SetPad(0.0,0.0,1.0,0.33);
    gPad->SetTickx();
    gPad->SetGridx();
    gPad->SetGridy();
    gPad->SetTopMargin(0);
    gPad->SetBottomMargin(0.3536693);
    TH1D *ratio_1 = new TH1D("ratio","ratio",100,0,100);
    TH1D *ratio_2 = new TH1D("ratio","ratio",100,0,100);    
    TH1D *ratio_3 = new TH1D("ratio","ratio",100,0,100);
    TH1D *ratio_4 = new TH1D("ratio","ratio",100,0,100);
    TH1D *ratio_5 = new TH1D("ratio","ratio",100,0,100);
    TH1D *ratio_6 = new TH1D("ratio","ratio",100,0,100);
    ratio_1->Divide(data_pu_1,mc_pu);
    ratio_2->Divide(data_pu_2,mc_pu);
    ratio_3->Divide(data_pu_3,mc_pu);
    ratio_4->Divide(data_pu_4,mc_pu);
    ratio_5->Divide(data_pu_5,mc_pu); 
    ratio_6->Divide(data_pu_6,mc_pu);
    ratio_1->SetStats(0);
    ratio_1->SetLineColor(kRed);
    ratio_2->SetLineColor(kMagenta+2);
    ratio_3->SetLineColor(kGreen+2);
    ratio_4->SetLineColor(kYellow+3);
    ratio_5->SetLineColor(kBlue+1);
    ratio_6->SetLineColor(kPink+10);
    ratio_1->SetTitle("");
    ratio_1->GetXaxis()->SetLabelSize(0.12);
    ratio_1->GetXaxis()->SetTitle("nPU");
    ratio_1->GetXaxis()->SetTitleSize(0.15);
    ratio_1->GetXaxis()->SetTitleOffset(0.99);
    ratio_1->GetXaxis()->SetTickLength(0.03);
    ratio_1->GetYaxis()->SetTitle("data/MC");
    ratio_1->GetYaxis()->CenterTitle();
    ratio_1->GetYaxis()->SetTitleSize(0.115);
    ratio_1->GetYaxis()->SetLabelSize(0.105);
    ratio_1->GetYaxis()->SetTitleOffset(0.35);
    ratio_1->GetYaxis()->SetNdivisions(406);
    ratio_1->GetYaxis()->SetRangeUser(0.5,1.5);
    //ratio->Sumw2();
    ratio_1->Draw("HIST");
    ratio_2->Draw("HIST SAME");
    ratio_3->Draw("HIST SAME");
    ratio_4->Draw("HIST SAME");
    ratio_5->Draw("HIST SAME");
    ratio_6->Draw("HIST SAME");
   // ratio->Sumw2();

    Double_t low = ratio_1->GetXaxis()->GetXmin();
    Double_t high = ratio_1->GetXaxis()->GetXmax();
    TLine *line = new TLine(low, 1, high, 1);
    line->SetLineColor(1);
    line->SetLineStyle(7);
    line->Draw();
    gPad->Modified();
    g2->Update();
    g2->Draw();

}


void plot_660(TH1D* nmc_pu,TH1D* nmc_pu_rwt_660, TH1D* ndata_pu_660) 
{
    TCanvas *g1 = new TCanvas("g1","g1",800,600) ;
    g1->Range(0,0,1,1);
    g1->SetFillColor(0);
    g1->SetBorderMode(0);
    g1->SetBorderSize(2);
    g1->SetFrameBorderMode(0);
    gStyle->SetPadBorderMode(0);
    g1->Divide(1,2);
    g1->cd(1);
    gPad->Range(-69.03766,-0.0002509835,628.8703,0.06681207);
    gPad->SetGridx();
    gPad->SetTopMargin(0.006574267);
    gPad->SetBottomMargin(0.001912046);
    ndata_pu_660->SetLineColor(kBlack);
    ndata_pu_660->SetLineStyle(7);
    ndata_pu_660->SetLineWidth(3);    
    nmc_pu_rwt_660->SetLineColor(kRed);
    nmc_pu->SetLineColor(kGreen+2);
    gPad->SetPad(0,0.33,1,0.9378806);
       
    //mc_pu->Sumw2();
    //data_pu_1->Sumw2();
    THStack* hs = new THStack("hs","Closure test for 66.0 mb min bias xsec of data");
    ndata_pu_660->SetLineWidth(3);
    //data_pu_660->Sumw2();
    hs->Add(nmc_pu,"HIST");
    hs->Add(ndata_pu_660,"HIST");
    hs->Add(nmc_pu_rwt_660,"HIST");
    hs->Draw("nostack");
    TText T; T.SetTextFont(42); T.SetTextAlign(21);
    //T.DrawTextNDC(.5,.95,"Default drawing option");
    //hs->GetHistogram()->SetTitle("Closure test for data_nPU = 66.0 mb");
    hs->GetHistogram()->GetXaxis()->SetLabelOffset(999);
    hs->GetHistogram()->GetXaxis()->SetTitle("");
    hs->GetHistogram()->GetYaxis()->SetTitle("");
    hs->GetHistogram()->GetYaxis()->SetTitleOffset(1.4);
    hs->GetHistogram()->GetYaxis()->SetTitleSize(0.03);
    hs->GetHistogram()->GetYaxis()->SetLabelSize(0.03);
    hs->GetHistogram()->GetYaxis()->CenterTitle();
    TLegend* la = new TLegend(0.6516547,0.7688758,0.857482,1.12674,NULL,"brNDC");
    TLegend* l1a;
    l1a = la;
    l1a->AddEntry(nmc_pu,"MC_nPU_66.0","l");
    l1a->AddEntry(nmc_pu_rwt_660,"MC_nPU_rwt_66.0","l");
    l1a->AddEntry(ndata_pu_660,"data_nPU_66.0","l");
    l1a->SetTextFont(12);
    l1a->SetTextSize(0.06237499);
    l1a->SetBorderSize(0);
    l1a->SetFillColor(0);
    l1a->Draw("same");



    g1->cd(2);
    gPad->SetPad(0.0,0.0,1.0,0.33);
    gPad->SetTickx();
    gPad->SetGridx();
    gPad->SetGridy();
    gPad->SetTopMargin(0);
    gPad->SetBottomMargin(0.3536693);
    TH1D *ratio_1 = new TH1D("ratio","ratio",100,0,100);
    TH1D *ratio_2 = new TH1D("ratio","ratio",100,0,100);    
    ratio_1->Divide(ndata_pu_660,nmc_pu);
    ratio_2->Divide(ndata_pu_660,nmc_pu_rwt_660);
    ratio_1->SetStats(0);
    ratio_1->SetLineColor(kGreen+2);
    ratio_2->SetLineColor(kRed);
    ratio_1->SetTitle("");
    ratio_1->GetXaxis()->SetLabelSize(0.12);
    ratio_1->GetXaxis()->SetTitle("nPU");
    ratio_1->GetXaxis()->SetTitleSize(0.15);
    ratio_1->GetXaxis()->SetTitleOffset(0.99);
    ratio_1->GetXaxis()->SetTickLength(0.03);
    ratio_1->GetYaxis()->SetTitle("data/MC");
    ratio_1->GetYaxis()->CenterTitle();
    ratio_1->GetYaxis()->SetTitleSize(0.115);
    ratio_1->GetYaxis()->SetLabelSize(0.105);
    ratio_1->GetYaxis()->SetTitleOffset(0.35);
    ratio_1->GetYaxis()->SetNdivisions(406);
    ratio_1->GetYaxis()->SetRangeUser(0.5,1.5);
    //ratio->Sumw2();
    ratio_1->Draw("HIST");
    ratio_2->Draw("HIST SAME");
   // ratio->Sumw2();

    Double_t low = ratio_1->GetXaxis()->GetXmin();
    Double_t high = ratio_1->GetXaxis()->GetXmax();
    TLine *line = new TLine(low, 1, high, 1);
    line->SetLineColor(1);
    line->SetLineStyle(7);
    line->SetLineWidth(3);
    line->Draw();
    gPad->Modified();
    g1->Update();
    g1->Draw();

}
