#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include "TGraph.h"
#include "TFile.h"
#include "TF1.h"
#include "TH2F.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <cmath>
#include <string>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>
#include <map>


#ifndef VBFnewFakeWeightOTF
#define VBFnewFakeWeightOTF

using namespace std;

class VBFnewFakeWeightOTFall : public multidraw::TTreeFunction {
public:
  //VBFnewFakeWeightOTFall(string file, string ele_WP, string mu_WP, string fr_ele_path, string pr_ele_path, string fr_mu_path, string pr_mu_path);
  VBFnewFakeWeightOTFall(string ele_WP, string mu_WP, string fr_ele_path_1, string pr_ele_path_1, string fr_mu_path_1, string pr_mu_path_1, string fr_ele_path_2, string pr_ele_path_2, string fr_mu_path_2, string pr_mu_path_2, bool do_absEta, bool do_statUp, bool do_statDo);

  char const* getName() const override { 
      return "VBFnewFakeWeightOTFall"; 
  }
  TTreeFunction* clone() const override { 
      //return new VBFnewFakeWeightOTFall(inputfile_path, ele_WP, mu_WP, fr_ele_path, pr_ele_path, fr_mu_path, pr_mu_path); 
      return new VBFnewFakeWeightOTFall(ele_WP, mu_WP, fr_ele_path_1, pr_ele_path_1, fr_mu_path_1, pr_mu_path_1, fr_ele_path_2, pr_ele_path_2, fr_mu_path_2, pr_mu_path_2, do_absEta, do_statUp, do_statDo); 
  }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
  ~VBFnewFakeWeightOTFall();
  void bindTree_(multidraw::FunctionLibrary&) override;
  bool do_statUp;
  bool do_statDo;
  bool do_absEta;

  
  //string inputfile_path;
  string pr_ele_path_1;
  string fr_ele_path_1;

  string pr_mu_path_1;
  string fr_mu_path_1;

  string pr_ele_path_2;
  string fr_ele_path_2;

  string pr_mu_path_2;
  string fr_mu_path_2;
  //TFile* inputfile;

  TFile* pr_ele_file_1;
  TFile* fr_ele_file_1;

  TFile* pr_mu_file_1;
  TFile* fr_mu_file_1;

  TFile* pr_ele_file_2;
  TFile* fr_ele_file_2;

  TFile* pr_mu_file_2;
  TFile* fr_mu_file_2;

  TH2F* pr_ele_h2_1;
  TH2F* fr_ele_h2_1;

  TH2F* pr_mu_h2_1;
  TH2F* fr_mu_h2_1;

  TH2F* pr_ele_h2_2;
  TH2F* fr_ele_h2_2;

  TH2F* pr_mu_h2_2;
  TH2F* fr_mu_h2_2;

  TH2F* pr_ele_h2;
  TH2F* fr_ele_h2;

  TH2F* pr_mu_h2;
  TH2F* fr_mu_h2;

  string ele_WP;
  string mu_WP;

  //string fakew_name;
  //vector<TF1 *> eff_A_L;
  //vector<TF1 *> eff_A_T;
  //vector<TF1 *> eff_B_L;
  //vector<TF1 *> eff_B_T;

  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  FloatArrayReader* Lepton_phi{};

  FloatValueReader* PuppiMET_phi{};
  
  IntArrayReader*   Lepton_pdgId{};
  IntArrayReader*   Lepton_isTightEle{};
  IntArrayReader*   Lepton_isTightMu{};

};

//VBFnewFakeWeightOTFall::VBFnewFakeWeightOTFall(string in_file, string ele_WP, string mu_WP, string in_fr_ele_path, string in_pr_ele_path, string in_fr_mu_path, string in_pr_mu_path) :
VBFnewFakeWeightOTFall::VBFnewFakeWeightOTFall(string ele_WP, string mu_WP, string in_fr_ele_path_1, string in_pr_ele_path_1, string in_fr_mu_path_1, string in_pr_mu_path_1, string in_fr_ele_path_2, string in_pr_ele_path_2, string in_fr_mu_path_2, string in_pr_mu_path_2, bool do_absEta, bool do_statUp = false, bool do_statDo = false) :
  TTreeFunction(), 
                  //inputfile_path(in_file), 
                  fr_ele_path_1(in_fr_ele_path_1), pr_ele_path_1(in_pr_ele_path_1),
                  fr_mu_path_1(in_fr_mu_path_1), pr_mu_path_1(in_pr_mu_path_1),
                  fr_ele_path_2(in_fr_ele_path_2), pr_ele_path_2(in_pr_ele_path_2),
                  fr_mu_path_2(in_fr_mu_path_2), pr_mu_path_2(in_pr_mu_path_2),
                  ele_WP(ele_WP), mu_WP(mu_WP), do_absEta(do_absEta),
                  do_statUp(do_statUp), do_statDo(do_statDo) 
{
  //inputfile = new TFile(inputfile_path.c_str(), "read");
  //for (int i = 1; i<=10; i++){
  //  eff_A_L.push_back((TF1*)inputfile->Get(("f_A_L_etabin"+ to_string(i)).c_str() ));
  //  eff_A_T.push_back((TF1*)inputfile->Get(("f_A_T_etabin"+ to_string(i)).c_str() ));
  //  eff_B_L.push_back((TF1*)inputfile->Get(("f_B_L_etabin"+ to_string(i)).c_str() ));
  //  eff_B_T.push_back((TF1*)inputfile->Get(("f_B_T_etabin"+ to_string(i)).c_str() ));
  //} 
  //inputfile->Close();


  fr_ele_file_1 = new TFile(fr_ele_path_1.c_str(), "read");
  pr_ele_file_1 = new TFile(pr_ele_path_1.c_str(), "read");
  fr_ele_h2_1 = (TH2F*) fr_ele_file_1->Get("FR_pT_eta_EWKcorr"); 
  pr_ele_h2_1 = (TH2F*) pr_ele_file_1->Get("h_Ele_signal_pt_eta_bin");  
  fr_ele_h2_1->SetDirectory(0);
  pr_ele_h2_1->SetDirectory(0);
  fr_ele_file_1->Close();
  pr_ele_file_1->Close();

  fr_mu_file_1 = new TFile(fr_mu_path_1.c_str(), "read");
  pr_mu_file_1 = new TFile(pr_mu_path_1.c_str(), "read");
  fr_mu_h2_1 = (TH2F*) fr_mu_file_1->Get("FR_pT_eta_EWKcorr");   
  pr_mu_h2_1 = (TH2F*) pr_mu_file_1->Get("h_Muon_signal_pt_eta_bin");  
  fr_mu_h2_1->SetDirectory(0);
  pr_mu_h2_1->SetDirectory(0);
  fr_mu_file_1->Close();
  pr_mu_file_1->Close();

  fr_ele_file_2 = new TFile(fr_ele_path_2.c_str(), "read");
  pr_ele_file_2 = new TFile(pr_ele_path_2.c_str(), "read");
  fr_ele_h2_2 = (TH2F*) fr_ele_file_2->Get("FR_pT_eta_EWKcorr"); 
  pr_ele_h2_2 = (TH2F*) pr_ele_file_2->Get("h_Ele_signal_pt_eta_bin");  
  fr_ele_h2_2->SetDirectory(0);
  pr_ele_h2_2->SetDirectory(0);
  fr_ele_file_2->Close();
  pr_ele_file_2->Close();

  fr_mu_file_2 = new TFile(fr_mu_path_2.c_str(), "read");
  pr_mu_file_2 = new TFile(pr_mu_path_2.c_str(), "read");
  fr_mu_h2_2 = (TH2F*) fr_mu_file_2->Get("FR_pT_eta_EWKcorr");   
  pr_mu_h2_2 = (TH2F*) pr_mu_file_2->Get("h_Muon_signal_pt_eta_bin");  
  fr_mu_h2_2->SetDirectory(0);
  pr_mu_h2_2->SetDirectory(0);
  fr_mu_file_2->Close();
  pr_mu_file_2->Close();
  
  if (do_statUp && do_statDo){
      throw std::runtime_error("Can't do both up and down at once");
  }

  std::cout << "DEBUGGGG: finished the getting-histos operations" << std::endl;
}


double
VBFnewFakeWeightOTFall::evaluate(unsigned)
{
  std::cout << "DEBUGGGG: start evaluating!!!" << std::endl;
  float eta = Lepton_eta->At(0);
  float abseta = abs(eta);
  float eta_touse = eta; 
  if(do_absEta) eta_touse = abseta;

  float pt = Lepton_pt->At(0);
  float new_fakew = 0.;

  float dphilep1met = (abs(Lepton_phi->At(0) - *PuppiMET_phi->Get())) * (abs(Lepton_phi->At(0) - *PuppiMET_phi->Get()) < 3.1415) + (2*3.1415 - abs(Lepton_phi->At(0) - *PuppiMET_phi->Get())) * (abs(Lepton_phi->At(0) - *PuppiMET_phi->Get()) >= 3.1415);
  
  std::cout << "dphilep1met: "<< dphilep1met << std::endl;

  if(dphilep1met<1.5) {
    pr_mu_h2 = pr_mu_h2_1;
    fr_mu_h2 = fr_mu_h2_1;
    pr_ele_h2 = pr_ele_h2_1;
    fr_ele_h2 = fr_ele_h2_1;
  } else { 
    pr_mu_h2 = pr_mu_h2_2;
    fr_mu_h2 = fr_mu_h2_2;
    pr_ele_h2 = pr_ele_h2_2;
    fr_ele_h2 = fr_ele_h2_2;
  }

  std::cout << "done with selecting the correct histo" << std::endl;


  if (abs(Lepton_pdgId->At(0)) != 11){
      float maxpt = pr_mu_h2->GetXaxis()->GetBinCenter(pr_mu_h2->GetNbinsX());
      float prompt_rate;
      if (pt > maxpt){
        prompt_rate   = pr_mu_h2->GetBinContent(pr_mu_h2->FindBin(maxpt,eta_touse));
      }else{
        prompt_rate   = pr_mu_h2->GetBinContent(pr_mu_h2->FindBin(pt,eta_touse));
      }
      std::cout << "prompt_rate ele: " << prompt_rate << std::endl;
      float fake_rate, fake_rate_e; 
      //maxpt = 35.; 
      maxpt = fr_mu_h2->GetXaxis()->GetBinCenter(fr_mu_h2->GetNbinsX());
      if (pt > maxpt){
        fake_rate   = fr_mu_h2->GetBinContent(fr_mu_h2->FindBin(maxpt, eta_touse));
        fake_rate_e = fr_mu_h2->GetBinError(fr_mu_h2->FindBin(maxpt, eta_touse));
      }else{
        fake_rate   = fr_mu_h2->GetBinContent(fr_mu_h2->FindBin(pt, eta_touse));
        fake_rate_e = fr_mu_h2->GetBinError(fr_mu_h2->FindBin(pt, eta_touse));
      }
      std::cout << "Fake_rate ele: " << fake_rate << std::endl;
      if (do_statUp){
        if (pt >=40 ) fake_rate += fake_rate_e / 2; // Only for muons
        else fake_rate += fake_rate_e;
        if (fake_rate >=1.) fake_rate = 0.99; 
      }
      if (do_statDo){
        if (pt >=40 ) fake_rate -= fake_rate_e / 2;
        else fake_rate -= fake_rate_e;
        if (fake_rate < 0) fake_rate=0.;
      }
      // We have to fix this case if not the formula will fail
       if (fake_rate >= (prompt_rate-0.025)){
            fake_rate = prompt_rate - 0.025; // Educated guess, keep fake rate 2.5% less of the prompt rate
       }
      std::cout << "fw ele: "<< fake_rate << ",  prompt rate "<< prompt_rate << "  " << 1/(prompt_rate - fake_rate) <<" eta,pt "<< eta_touse << " " << pt << std::endl;
      if (Lepton_isTightMu->At(0)){
          // new_fakew = (-1) * fake_rate * (1 - prompt_rate)/(prompt_rate - fake_rate);
          new_fakew = (-1) * (1 - prompt_rate)/(prompt_rate - fake_rate);
      }else{
          // new_fakew = (fake_rate * prompt_rate)/(prompt_rate - fake_rate);
          new_fakew = (prompt_rate)/(prompt_rate - fake_rate);
      }
  }else{
      float maxpt = pr_ele_h2->GetXaxis()->GetBinCenter(pr_ele_h2->GetNbinsX());
      float prompt_rate;
      if (pt > maxpt){
        prompt_rate   = pr_ele_h2->GetBinContent(pr_ele_h2->FindBin(maxpt,eta_touse));
      }else{
        prompt_rate   = pr_ele_h2->GetBinContent(pr_ele_h2->FindBin(pt,eta_touse));
      }
      std::cout << "prompt_rate mu: " << prompt_rate << std::endl;
      float fake_rate, fake_rate_e; 
      //maxpt = 35.; 
      maxpt = fr_ele_h2->GetXaxis()->GetBinCenter(fr_ele_h2->GetNbinsX());
      if (pt > maxpt){
        fake_rate   = fr_ele_h2->GetBinContent(fr_ele_h2->FindBin(maxpt, eta_touse));
        fake_rate_e = fr_ele_h2->GetBinError(fr_ele_h2->FindBin(maxpt, eta_touse));
      }else{
        fake_rate   = fr_ele_h2->GetBinContent(fr_ele_h2->FindBin(pt, eta_touse));
        fake_rate_e = fr_ele_h2->GetBinError(fr_ele_h2->FindBin(pt, eta_touse));
      }
      std::cout << "Fake_rate mu: " << fake_rate << std::endl;

      if (do_statUp){
          fake_rate += fake_rate_e;
          if (fake_rate >=1.) fake_rate = 0.99; 
      }
      if (do_statDo){
          fake_rate -= fake_rate_e; 
          if (fake_rate < 0) fake_rate=0.;
      }
      // We have to fix this case if not the formula will fail
       if (fake_rate >= (prompt_rate-0.02)){
            fake_rate = prompt_rate - 0.02; // Educated guess, keep fake rate 2% less of the prompt rate
       }
      if (Lepton_isTightEle->At(0)){
          // new_fakew = (-1) * fake_rate * (1 - prompt_rate)/(prompt_rate - fake_rate);
          new_fakew = (-1) * (1 - prompt_rate)/(prompt_rate - fake_rate);
      }else{
          // new_fakew = (fake_rate * prompt_rate)/(prompt_rate - fake_rate);
          new_fakew = (prompt_rate)/(prompt_rate - fake_rate);
      }
      std::cout << "fw mu: "<< fake_rate << ",  prompt rate "<< prompt_rate << "  " << 1/(prompt_rate - fake_rate) <<" eta,pt "<< eta_touse << " " << pt << std::endl;
  }

  return new_fakew;
}

void
VBFnewFakeWeightOTFall::bindTree_(multidraw::FunctionLibrary& _library)
{   
    std::cout << "DEBUGGGG: start binding!!!" << std::endl;
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(PuppiMET_phi, "PuppiMET_phi");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_isTightEle, ("Lepton_isTightElectron_"+ele_WP).c_str());
    _library.bindBranch(Lepton_isTightMu, ("Lepton_isTightMuon_"+mu_WP).c_str());
    std::cout << "DEBUGGGG: done binding!!!" << std::endl;
}

VBFnewFakeWeightOTFall::~VBFnewFakeWeightOTFall(){
    std::cout << "DEBUGGGG: start destructing!!!" << std::endl;
    Lepton_pt = nullptr;
    
    Lepton_eta = nullptr;
    
    Lepton_phi = nullptr;
    
    PuppiMET_phi = nullptr;
    Lepton_pdgId = nullptr;
    Lepton_isTightEle = nullptr;
    Lepton_isTightMu = nullptr;

    // delete pr_ele_h2;
    // std::cout << "DEBUGGGG: 1" << std::endl;
    // delete fr_ele_h2;
    // std::cout << "DEBUGGGG: 2" << std::endl;
    // delete pr_mu_h2;
    // std::cout << "DEBUGGGG: 3" << std::endl;
    // delete fr_mu_h2;
    std::cout << "DEBUGGGG: 4" << std::endl;
    delete pr_ele_h2_1;
    std::cout << "DEBUGGGG: 5" << std::endl;
    delete fr_ele_h2_1;
    std::cout << "DEBUGGGG: 6" << std::endl;
    delete pr_mu_h2_1;
    std::cout << "DEBUGGGG: 7" << std::endl;
    delete fr_mu_h2_1;
    std::cout << "DEBUGGGG: 8" << std::endl;
    delete pr_ele_h2_2;
    std::cout << "DEBUGGGG: 9" << std::endl;
    delete fr_ele_h2_2;
    std::cout << "DEBUGGGG: 10" << std::endl;    
    delete pr_mu_h2_2;
    std::cout << "DEBUGGGG: 11" << std::endl;
    delete fr_mu_h2_2;
    std::cout << "DEBUGGGG: done destructing!!!" << std::endl;
}


#endif