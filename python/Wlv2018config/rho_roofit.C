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
#include "cmath" 


using namespace RooFit;
using namespace RooStats;
using namespace std;

void rho_roofit()
{   
//    TFile* file1 = new TFile("/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2018/runplot-12mar-v3/Plots/ttu__Pileup_nPU_.root");
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
    //c->Draw();
    //h->Draw();

    auto nPoints = g->GetN();
    double data_rho[100];
    cout<<nPoints<<endl;
    //double bin_width = h->GetXaxis()->GetNbins();
    //cout<<h->GetMinimum()<<endl;
    //cout<<bin_width<<endl;

    //TH1 *h1 = new TH1F("h","h",100,0,100);	
    //TH1 h; // the histogram (you should set the number of bins, the title etc)
   

    TProfile *data  = new TProfile("pileup","pileup",100,0,100,0,1);
    for(int i=0; i < nPoints; ++i) 
    {
        double x,y;
        g->GetPoint(i, x, y);
        data->Fill(x,y); //
        data_rho[i] = y;
        //cout<<x<<"  "<<y<<endl; 
    }

    TProfile *data_up  = new TProfile("pileup","pileup",100,0,100,0,1);
    for(int i=0; i < nPoints; ++i)
    {
        double x,y;
        g_up->GetPoint(i, x, y);
        data_up->Fill(x,y); //
       
     }
        
    TProfile *data_down  = new TProfile("pileup","pileup",100,0,100,0,1);
    for(int i=0; i < nPoints; ++i)
    {
        double x,y;
        g_down->GetPoint(i, x, y);
        data_down->Fill(x,y); 
         
     }
       

/*    float width = h1->GetXaxis()->GetBinWidth(0);
    cout<<width<<endl;
*/    
           
/*
    TCanvas *g1 = new TCanvas("g1","g1",800,600);
    TH1D *data_pu = data->ProjectionX();
    data_pu->Draw();
    g1->Draw();
*/


    //h2->Draw("hist");
    //cout<<h1->GetIntegral();


    //TFile* file2 = new TFile("/mnt/t3nfs01/data01/shome/krgedia/CMSSW_10_1_0/src/Xbb/python/logs_Wlv2018/runplot-12mar-v3/Plots/ttu__Pileup_nPU_.shapes.root");
    //file2->ls();

    TProfile *mc = new TProfile("pileup","pileup",100,0,100,0,1);

    double x[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99};

    double y[] = {4.695341*pow(10,-10), 1.206213*pow(10,-6), 1.162593*pow(10,-6), 6.118058*pow(10,-6), 1.626767*pow(10,-5), 3.508135*pow(10,-5), 7.12608*pow(10,-5), 0.0001400641, 0.0002663403, 0.0004867473, 0.0008469, 0.001394142, 0.002169081, 0.003198514, 0.004491138, 0.006036423, 0.007806509, 0.00976048, 0.0118498, 0.01402411, 0.01623639, 0.01844593, 0.02061956, 0.02273221, 0.02476554, 0.02670494, 0.02853662, 0.03024538, 0.03181323, 0.03321895, 0.03443884, 0.035448, 0.03622242, 0.03674106, 0.0369877, 0.03695224, 0.03663157, 0.03602986, 0.03515857, 0.03403612, 0.0326868, 0.03113936, 0.02942582, 0.02757999, 0.02563551, 0.02362497, 0.02158003, 0.01953143, 0.01750863, 0.01553934, 0.01364905, 0.01186035, 0.01019246, 0.008660705, 0.007275915, 0.006043917, 0.004965276, 0.004035611, 0.003246373, 0.002585932, 0.002040746, 0.001596402, 0.001238498, 0.0009533139, 0.0007282885, 0.000552306, 0.0004158005, 0.0003107302, 0.0002304612, 0.0001696012, 0.0001238161, 8.96531*pow(10,-5), 6.438087*pow(10,-5), 4.585302*pow(10,-5), 3.23949*pow(10,-5), 2.271048*pow(10,-5), 1.580622*pow(10,-5), 1.09286*pow(10,-5), 7.512748*pow(10,-6), 5.140304*pow(10,-6), 3.505254*pow(10,-6), 2.386437*pow(10,-6), 1.625859*pow(10,-6), 1.111865*pow(10,-6), 7.663272*pow(10,-7), 5.350694*pow(10,-7), 3.808318*pow(10,-7), 2.781785*pow(10,-7), 2.098661*pow(10,-7), 1.642811*pow(10,-7), 1.312835*pow(10,-7), 1.081326*pow(10,-7), 9.141993*pow(10,-8), 7.890983*pow(10,-8), 6.91468*pow(10,-8), 6.119019*pow(10,-8), 5.443693*pow(10,-8), 4.85036*pow(10,-8), 4.31486*pow(10,-8), 3.822112*pow(10,-8)};

    for (Int_t i = 0; i < 100; i++)
    {        
        mc->Fill(x[i],y[i]);
    }

//    TH1D *mc_pu = mc->ProjectionX();
    
    //TH1F *c2 = (TH1F *)file2->Get("summedMcHistograms");    
    //TH1F *h3 = (TH1F *)c2->GetPrimitive("Pileup_nPU");
    //h3->GetXaxis()->GetBinWidth(0);
    //c2->GetListOfPrimitives()->Print();
    //file2->GetListOfKeys()->Print();
    //c2->Draw("hist");

/*
    TCanvas *g2 = new TCanvas("g2","g2",800,600) ;
    mc_pu->Draw();
    g2->Draw();   
*/
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


    TCanvas *g2 = new TCanvas("g2","g2",800,600) ;
//    TH1D *mc_pu = mc->ProjectionX();
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
    data_pu->SetLineColor(kBlack);
    mc_pu->SetLineColor(kRed);
    gPad->SetPad(0,0.33,1,0.9378806);
    data_pu->SetStats(0);
    data_pu->SetTitle("");
    data_pu->GetYaxis()->SetLabelSize(0.05);
    data_pu->Sumw2();
    mc_pu->Sumw2();
    data_pu->Draw("E");
    mc_pu->Draw("HIST SAME");

    TLegend* la = new TLegend(0.6816547,0.7688758,0.897482,0.9892674,NULL,"brNDC");
    TLegend* l1a;
    l1a = la;
    l1a->AddEntry(data_pu,"data","l");
    l1a->AddEntry(mc_pu,"MC","l");
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
    ratio->SetStats(0);
    ratio->SetLineColor(kBlack);
    ratio->SetTitle("");
    ratio->GetXaxis()->SetLabelSize(0.12);
    ratio->GetXaxis()->SetTitle("rho");
    ratio->GetXaxis()->SetTitleSize(0.15);
    ratio->GetXaxis()->SetTitleOffset(0.99);
    ratio->GetXaxis()->SetTickLength(0.03);
    ratio->GetYaxis()->SetTitle("data/MC");
    ratio->GetYaxis()->CenterTitle();
    ratio->GetYaxis()->SetTitleSize(0.115);
    ratio->GetYaxis()->SetLabelSize(0.105);
    ratio->GetYaxis()->SetTitleOffset(0.35);
    ratio->GetYaxis()->SetNdivisions(406);
    ratio->GetYaxis()->SetRangeUser(0.5,1.5);
    //ratio->Sumw2();
    ratio->Draw("E");
   // ratio->Sumw2();

    Double_t low = ratio->GetXaxis()->GetXmin();
    Double_t high = ratio->GetXaxis()->GetXmax();
    TLine *line = new TLine(low, 1, high, 1);
    line->SetLineColor(2);
    line->SetLineStyle(7);
    line->Draw();
    gPad->Modified();
    g2->Update();

    g2->Draw();



}
/*
void rho_roofit()
{
    TFile* file1 = new TFile("TMVA_output_splots.root");
    TTree* datatree = (TTree*)(file1->Get("tree"));

    TFile* r_file1 = new TFile("r_TMVA_output_splots.root");
    TTree* r_datatree = (TTree*)(r_file1->Get("tree"));

    RooRealVar rho("rho","rho",-200,100);

    RooDataSet data_set("data_set","data_set",RooArgSet(rho),Import(*datatree));
    RooDataSet r_data_set("r_data_set","r_data_set",RooArgSet(rho),Import(*r_datatree));

    TH1* r_data_p_rho = (TH1*) r_data_set.createHistogram("r_data_p_rho",rho,Binning(100,0,100));
    TH1* data_p_rho = (TH1*) data_set.createHistogram("data_p_rho",rho,Binning(100,0,100));

    r_data_p_rho->Scale(1/r_data_p_rho->Integral());

    TCanvas* hist2 = new TCanvas("hist2","hist2");
    r_data_p_rho->Draw();
    hist2->Draw();

    data_p_rho->Scale(1/data_p_rho->Integral());

    TCanvas* hist1 = new TCanvas("hist1","hist1");
    data_p_rho->Draw();
    hist1->Draw();

    TH1* rho_ratio = new TH1F("rho_ratio" ,"rho_ratio" ,100 , 0, 100);
    rho_ratio->Divide(r_data_p_rho,data_p_rho);
    
    TCanvas* ratio = new TCanvas("ratio","ratio");
    rho_ratio->Draw();
    ratio->Draw();

    TF1 *func = new TF1("func","pol9",-100,100);

//    hist->Fit(func);

}

*/





