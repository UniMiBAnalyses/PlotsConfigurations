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


#ifndef HEMcorr
#define HEMcorr

using namespace std;

class HEMcorrector : public multidraw::TTreeFunction {
public:
  HEMcorrector(std::string histo_path, bool do_statUp, bool do_statDo);

  char const* getName() const override { 
      return "HEMcorrector"; 
  }
  TTreeFunction* clone() const override { 
      return new HEMcorrector(histo_path, do_statUp, do_statDo);
  }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
  ~HEMcorrector();
  void bindTree_(multidraw::FunctionLibrary&) override;
  bool do_statUp;
  bool do_statDo;

  string histo_path;
  TFile* histo_file;
  TH1F* h1;

  FloatArrayReader* Lepton_phi{};
  FloatArrayReader* Lepton_eta{};
  IntArrayReader*   Lepton_pdgId{};

};

//HEMcorrector::HEMcorrector(string in_file, string ele_WP, string mu_WP, string in_fr_ele_path, string in_pr_ele_path, string in_fr_mu_path, string in_pr_mu_path) :
HEMcorrector::HEMcorrector(string in_histo_path, bool do_statUp = false, bool do_statDo = false) :
  TTreeFunction(), 
                  //inputfile_path(in_file), 
                  histo_path(in_histo_path), do_statUp(do_statUp), do_statDo(do_statDo) 
{

  histo_file = new TFile(histo_path.c_str(), "read");

  h1 = (TH1F*) histo_file->Get("histo_variable_binning"); 
  h1->SetDirectory(0);
  histo_file->Close();

  if (do_statUp && do_statDo){
      throw std::runtime_error("Can't do both up and down at once");
  }
}


double
HEMcorrector::evaluate(unsigned)
{
  float eta = Lepton_eta->At(0);
  float phi = Lepton_phi->At(0);

  float weight = 0.;
  float weight_err = 0.;

  if(abs(Lepton_pdgId->At(0)) == 11 && eta < -1.3){
    weight = h1->GetBinContent(h1->FindBin(phi));
    weight_err = h1->GetBinError(h1->FindBin(phi));

    if (do_statUp){
        weight += weight_err;
    }
    if (do_statDo){
        weight -= weight_err;
    }
  } else {
    weight = 1.;
  }

  return weight;
}

void
HEMcorrector::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
}

HEMcorrector::~HEMcorrector(){
    Lepton_phi = nullptr;
    Lepton_eta = nullptr;
    Lepton_pdgId = nullptr;

    delete h1;
}


#endif