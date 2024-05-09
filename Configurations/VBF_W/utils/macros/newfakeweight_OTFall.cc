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


#ifndef newFakeWeightOTF
#define newFakeWeightOTF

using namespace std;

class newFakeWeightOTFall : public multidraw::TTreeFunction {
public:
  //newFakeWeightOTFall(string file, string ele_WP, string mu_WP, string fr_ele_path, string pr_ele_path, string fr_mu_path, string pr_mu_path);
  newFakeWeightOTFall(string ele_WP, string mu_WP, string fr_ele_path, string pr_ele_path, string fr_mu_path, string pr_mu_path, bool do_absEta, bool do_statUp, bool do_statDo, bool do_shiftPR);

  char const* getName() const override { 
      return "newFakeWeightOTFall"; 
  }
  TTreeFunction* clone() const override { 
      //return new newFakeWeightOTFall(inputfile_path, ele_WP, mu_WP, fr_ele_path, pr_ele_path, fr_mu_path, pr_mu_path); 
      return new newFakeWeightOTFall(ele_WP, mu_WP, fr_ele_path, pr_ele_path, fr_mu_path, pr_mu_path,do_absEta, do_statUp, do_statDo, do_shiftPR); 
  }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
  ~newFakeWeightOTFall();
  void bindTree_(multidraw::FunctionLibrary&) override;
  bool do_statUp;
  bool do_statDo;
  bool do_absEta;
  bool do_shiftPR;

  
  //string inputfile_path;
  string pr_ele_path;
  string fr_ele_path;
  string pr_mu_path;
  string fr_mu_path;
  //TFile* inputfile;
  TFile* pr_ele_file;
  TFile* fr_ele_file;
  TFile* pr_mu_file;
  TFile* fr_mu_file;
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
  IntArrayReader*   Lepton_pdgId{};
  IntArrayReader*   Lepton_isTightEle{};
  IntArrayReader*   Lepton_isTightMu{};

};

//newFakeWeightOTFall::newFakeWeightOTFall(string in_file, string ele_WP, string mu_WP, string in_fr_ele_path, string in_pr_ele_path, string in_fr_mu_path, string in_pr_mu_path) :
newFakeWeightOTFall::newFakeWeightOTFall(string ele_WP, string mu_WP, string in_fr_ele_path, string in_pr_ele_path, string in_fr_mu_path, string in_pr_mu_path,bool do_absEta, bool do_statUp, bool do_statDo, bool do_shiftPR) :
  TTreeFunction(), 
                  //inputfile_path(in_file), 
                  fr_ele_path(in_fr_ele_path), pr_ele_path(in_pr_ele_path),
                  fr_mu_path(in_fr_mu_path), pr_mu_path(in_pr_mu_path),
                  ele_WP(ele_WP), mu_WP(mu_WP), do_absEta(do_absEta),
                  do_statUp(do_statUp), do_statDo(do_statDo), do_shiftPR(do_shiftPR) 
{
  //inputfile = new TFile(inputfile_path.c_str(), "read");
  //for (int i = 1; i<=10; i++){
  //  eff_A_L.push_back((TF1*)inputfile->Get(("f_A_L_etabin"+ to_string(i)).c_str() ));
  //  eff_A_T.push_back((TF1*)inputfile->Get(("f_A_T_etabin"+ to_string(i)).c_str() ));
  //  eff_B_L.push_back((TF1*)inputfile->Get(("f_B_L_etabin"+ to_string(i)).c_str() ));
  //  eff_B_T.push_back((TF1*)inputfile->Get(("f_B_T_etabin"+ to_string(i)).c_str() ));
  //} 
  //inputfile->Close();
  fr_ele_file = new TFile(fr_ele_path.c_str(), "read");
  pr_ele_file = new TFile(pr_ele_path.c_str(), "read");
  fr_ele_h2 = (TH2F*) fr_ele_file->Get("FR_pT_eta_EWKcorr"); 
  // pr_ele_h2 = (TH2F*) pr_ele_file->Get("h_Ele_signal_pt_eta_bin");  
  pr_ele_h2 = (TH2F*) pr_ele_file->Get("FR_pT_eta_EWKcorr");  
  fr_ele_h2->SetDirectory(0);
  pr_ele_h2->SetDirectory(0);
  fr_ele_file->Close();
  fr_ele_file->Close();

  fr_mu_file = new TFile(fr_mu_path.c_str(), "read");
  pr_mu_file = new TFile(pr_mu_path.c_str(), "read");
  fr_mu_h2 = (TH2F*) fr_mu_file->Get("FR_pT_eta_EWKcorr");   
  pr_mu_h2 = (TH2F*) pr_mu_file->Get("FR_pT_eta_EWKcorr");  
  // pr_mu_h2 = (TH2F*) pr_mu_file->Get("h_Muon_signal_pt_eta_bin");  
  fr_mu_h2->SetDirectory(0);
  pr_mu_h2->SetDirectory(0);
  fr_mu_file->Close();
  fr_mu_file->Close();
  
  if (do_statUp && do_statDo){
      throw std::runtime_error("Can't do both up and down at once");
  }
}


double
newFakeWeightOTFall::evaluate(unsigned)
{
  float eta = Lepton_eta->At(0);
  float abseta = abs(eta);
  float eta_touse = eta; 
  if(do_absEta) eta_touse = abseta;

  float pt = Lepton_pt->At(0);
  float new_fakew = 0.;

  // maximum effect of the statistical variation is 30%
  float limit_eff = 0.3;
  float limit = limit_eff*10;

  if (abs(Lepton_pdgId->At(0)) != 11){
      float maxpt = pr_mu_h2->GetXaxis()->GetBinCenter(pr_mu_h2->GetNbinsX());
      float prompt_rate;
      if (pt > maxpt){
        prompt_rate   = (pr_mu_h2->GetBinContent(pr_mu_h2->FindBin(maxpt,eta_touse)));
      }else{
        prompt_rate   = (pr_mu_h2->GetBinContent(pr_mu_h2->FindBin(pt,eta_touse)));
      }
      float fake_rate, fake_rate_e; 
      //maxpt = 35.; 
      maxpt = fr_mu_h2->GetXaxis()->GetBinCenter(fr_mu_h2->GetNbinsX());
      if (pt > maxpt){
        fake_rate   = (fr_mu_h2->GetBinContent(fr_mu_h2->FindBin(maxpt, eta_touse)));
        fake_rate_e = fr_mu_h2->GetBinError(fr_mu_h2->FindBin(maxpt, eta_touse));
      }else{
        fake_rate   = (fr_mu_h2->GetBinContent(fr_mu_h2->FindBin(pt, eta_touse)));
        fake_rate_e = fr_mu_h2->GetBinError(fr_mu_h2->FindBin(pt, eta_touse));
      }
      /// educated guess, never fake > prompt
      if (fake_rate >= prompt_rate) fake_rate = prompt_rate-0.025;

      // this is the limit value for the error on the FR for which the statistical effect does not 
      // reach more than 30% of effect. not very honest, to be honest.. but... you know..
      float val_lim = (limit*fake_rate*(prompt_rate-fake_rate))/(10*prompt_rate + limit*fake_rate);

      if (do_statUp){
        if (fake_rate_e > val_lim) {
          fake_rate_e = val_lim;
        }
        fake_rate += fake_rate_e; // Only for muons to prevent explosion at the denominator in the formula
        if (fake_rate >=1.) fake_rate = 0.99; 
      }

      if (do_statDo){
        if (fake_rate_e > val_lim) {
          fake_rate_e = val_lim;
        }
        fake_rate -= fake_rate_e;
        if (fake_rate < 0) fake_rate=0.;
      }
      // // We have to fix this case if not the formula will fail
      // // If do_shiftPR is False, means that i'm using the nominal (from DATA) PR, and I simply correct the FR  
      // // to keep it under 2% of the prompt. Now if do_shiftPR is true, i'm varying the PR (using the one from MC).
      // // This PR is *lower* then the one from data, so i'm **not** correcting the FR, lowering it to keep it under 2%
      // // but i'm raising the PR. Then i still have to correct in case of non physical numbers 
      if (do_shiftPR == true) {
        if (prompt_rate <= (fake_rate+0.025)){
          prompt_rate = fake_rate + 0.025;
          if( prompt_rate > 1. ){
            prompt_rate = 1.;
            fake_rate = prompt_rate - 0.025;
          } 
        }
      }
      if (Lepton_isTightMu->At(0)){
          new_fakew = (-1) * fake_rate * (1 - prompt_rate)/(prompt_rate - fake_rate);
          // new_fakew = (-1) * (1 - prompt_rate)/(prompt_rate - fake_rate);
      }else{
          new_fakew = (fake_rate * prompt_rate)/(prompt_rate - fake_rate);
          // new_fakew = (prompt_rate)/(prompt_rate - fake_rate);
      }
  }else{
      float maxpt = pr_ele_h2->GetXaxis()->GetBinCenter(pr_ele_h2->GetNbinsX());
      float prompt_rate;
      if (pt > maxpt){
        prompt_rate   = (pr_ele_h2->GetBinContent(pr_ele_h2->FindBin(maxpt,eta_touse)));
      }else{
        prompt_rate   = (pr_ele_h2->GetBinContent(pr_ele_h2->FindBin(pt,eta_touse)));
      }
      float fake_rate, fake_rate_e; 
      //maxpt = 35.; 
      maxpt = fr_ele_h2->GetXaxis()->GetBinCenter(fr_ele_h2->GetNbinsX());
      if (pt > maxpt){
        fake_rate   =  (fr_ele_h2->GetBinContent(fr_ele_h2->FindBin(maxpt, eta_touse)));
        fake_rate_e = fr_ele_h2->GetBinError(fr_ele_h2->FindBin(maxpt, eta_touse));
      }else{
        fake_rate   = (fr_ele_h2->GetBinContent(fr_ele_h2->FindBin(pt, eta_touse)));
        fake_rate_e = fr_ele_h2->GetBinError(fr_ele_h2->FindBin(pt, eta_touse));
      }

      float val_lim = (limit*fake_rate*(prompt_rate-fake_rate))/(10*prompt_rate + limit*fake_rate);
      
      if (do_statUp){
        if (fake_rate_e > val_lim) {
          fake_rate_e = val_lim;
        }
        fake_rate += fake_rate_e;
        if (fake_rate >=1.) fake_rate = 0.99; 
      }
      if (do_statDo){
        if (fake_rate_e > val_lim) {
          fake_rate_e = val_lim;
        }
        fake_rate -= fake_rate_e; 
          if (fake_rate < 0) fake_rate=0.;
      }
      // We have to fix this case if not the formula will fail and gives non physical results
      // If do_shiftPR is False, means that i'm using the nominal (from DATA) PR, and I simply correct the FR  
      // to keep it under 2% of the prompt. Now if do_shiftPR is true, i'm varying the PR (using the one from MC).
      // This PR is *lower* then the one from data, so i'm not correcting the FR, lowering it to keep it under 2%
      // but i'm raising the PR. Then i still have to correct in case of non physical numbers 
      if (do_shiftPR == true) {
        if (prompt_rate <= (fake_rate+0.02)){
          prompt_rate = fake_rate + 0.02;
          if( prompt_rate > 1. ){
            prompt_rate = 1.;
            fake_rate = prompt_rate - 0.02;
          } 
        }
      }

      if (Lepton_isTightEle->At(0)){
          new_fakew = (-1) * fake_rate * (1 - prompt_rate)/(prompt_rate - fake_rate);
          // new_fakew = (-1) * (1 - prompt_rate)/(prompt_rate - fake_rate);
      }else{
          new_fakew = (fake_rate * prompt_rate)/(prompt_rate - fake_rate);
          // new_fakew = (prompt_rate)/(prompt_rate - fake_rate);
      }
  }

  return new_fakew;
}

void
newFakeWeightOTFall::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_isTightEle, ("Lepton_isTightElectron_"+ele_WP).c_str());
    _library.bindBranch(Lepton_isTightMu, ("Lepton_isTightMuon_"+mu_WP).c_str());

}

newFakeWeightOTFall::~newFakeWeightOTFall(){
    Lepton_pt = nullptr;
    Lepton_eta = nullptr;
    Lepton_pdgId = nullptr;
    Lepton_isTightEle = nullptr;

    delete pr_ele_h2;
    delete fr_ele_h2;
    delete pr_mu_h2;
    delete fr_mu_h2;
}


#endif