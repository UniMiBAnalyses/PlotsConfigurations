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


#ifndef Fakes_corr
#define Fakes_corr

using namespace std;

class Fakes_corrector : public multidraw::TTreeFunction {
public:
  Fakes_corrector(std::string histo_path_ele,std::string histo_path_mu, bool do_statUp, bool do_statDo);

  char const* getName() const override { 
      return "Fakes_corrector"; 
  }
  TTreeFunction* clone() const override { 
      return new Fakes_corrector(histo_path_ele,histo_path_mu, do_statUp, do_statDo);
  }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
  ~Fakes_corrector();
  void bindTree_(multidraw::FunctionLibrary&) override;
  bool do_statUp;
  bool do_statDo;

  string histo_path_ele;
  string histo_path_mu;
  TFile* histo_file_ele;
  TFile* histo_file_mu;
  TH1F* h_ele;
  TH1F* h_mu;

  FloatArrayReader* Lepton_phi{};
  FloatArrayReader* Lepton_eta{};
  IntArrayReader*   Lepton_pdgId{};

};

//Fakes_corrector::Fakes_corrector(string in_file, string ele_WP, string mu_WP, string in_fr_ele_path, string in_pr_ele_path, string in_fr_mu_path, string in_pr_mu_path) :
Fakes_corrector::Fakes_corrector(string in_histo_path_ele, string in_histo_path_mu, bool do_statUp = false, bool do_statDo = false) :
  TTreeFunction(), 
                  //inputfile_path(in_file), 
                  histo_path_ele(in_histo_path_ele),histo_path_mu(in_histo_path_mu), do_statUp(do_statUp), do_statDo(do_statDo) 
{

  histo_file_ele = new TFile(histo_path_ele.c_str(), "read");
  histo_file_mu = new TFile(histo_path_mu.c_str(), "read");

  h_ele = (TH1F*) histo_file_ele->Get("histo_variable_binning"); 
  h_ele->SetDirectory(0);
  histo_file_ele->Close();

  h_mu = (TH1F*) histo_file_mu->Get("histo_variable_binning"); 
  h_mu->SetDirectory(0);
  histo_file_mu->Close();

  if (do_statUp && do_statDo){
      throw std::runtime_error("Can't do both up and down at once");
  }
}


double
Fakes_corrector::evaluate(unsigned)
{
  float eta = Lepton_eta->At(0);
  float phi = Lepton_phi->At(0);

  float weight = 1.;
  float weight_err = 0.;

  if(abs(Lepton_pdgId->At(0)) == 11 && eta < -1.3){
    weight = h_ele->GetBinContent(h_ele->FindBin(phi));
    weight_err = h_ele->GetBinError(h_ele->FindBin(phi));

    if (do_statUp){
        weight += weight_err;
    }
    if (do_statDo){
        weight -= weight_err;
    }
  } else if (abs(Lepton_pdgId->At(0)) == 13) {
    weight = h_mu->GetBinContent(h_mu->FindBin(phi));
    weight_err = h_mu->GetBinError(h_mu->FindBin(phi));

    if (do_statUp){
        weight += weight_err;
    }
    if (do_statDo){
        weight -= weight_err;
    }
  }

  return weight;
}

void
Fakes_corrector::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
}

Fakes_corrector::~Fakes_corrector(){
    Lepton_phi = nullptr;
    Lepton_eta = nullptr;
    Lepton_pdgId = nullptr;

    delete h_ele;
    delete h_mu;
}


#endif