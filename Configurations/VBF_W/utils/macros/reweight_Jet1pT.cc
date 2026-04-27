#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>
#include <string>

#include "TFile.h"
#include "TF1.h"
#include "TString.h"
#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/VectorUtil.h"

#include <iostream>
using namespace ROOT::Math;
typedef TTreeReaderValue<Double_t> DoubleValueReader;


class ReweightJet1pT: public multidraw::TTreeFunction {
public:
  ReweightJet1pT(const char * weights_file, string ele_function, string mu_function);
  ~ReweightJet1pT();

  char const* getName() const override { return "ReweightJet1pT"; }
  TTreeFunction* clone() const override { return new ReweightJet1pT(_weights_file.Data(), ele_function, mu_function); }

  unsigned getNdata() override { return 1; } 
  double evaluate(unsigned) override;
  

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  void setValues();
  TString _weights_file;
  TFile* _file;
  string ele_function;
  string mu_function;

  TF1* ele_hard_weight;
  TF1* mu_hard_weight;
  
  // DoubleValueReader* Category; this does not work... same strategy, redefine the alias here
  IntArrayReader* CleanJet_jetIdx;
  IntArrayReader* Jet_genJetIdx;

  FloatArrayReader* GenJet_pt{};

  IntArrayReader * Lepton_pdgId;
  FloatArrayReader* CleanJet_pt;

};

ReweightJet1pT::ReweightJet1pT(const char * weights_file, string ele_function, string mu_function) :
  TTreeFunction(), _weights_file(weights_file), ele_function(ele_function), mu_function(mu_function)
{
  _file = new TFile(weights_file,"READ");

  ele_hard_weight = (TF1*)_file->Get(ele_function.c_str());
  mu_hard_weight = (TF1*)_file->Get(mu_function.c_str());

}

ReweightJet1pT::~ReweightJet1pT(){
  if (_file) {
    _file->Close();
    delete _file;
    _file = nullptr;
  }
}


double ReweightJet1pT::evaluate(unsigned iJ) {
  if (Lepton_pdgId->GetSize() == 0) {
    return 1.0;  
  }

  int lepId = abs(Lepton_pdgId->At(0));

  if (CleanJet_jetIdx->GetSize() < 2 || CleanJet_pt->GetSize() < 1) {
    return 1.0;  
  }

  int Cjetidx0 = CleanJet_jetIdx->At(0);
  int Cjetidx1 = CleanJet_jetIdx->At(1);

  if (Cjetidx0 < 0 || Cjetidx1 < 0 || static_cast<std::size_t>(Cjetidx0) >= Jet_genJetIdx->GetSize() || 
    static_cast<std::size_t>(Cjetidx1) >= Jet_genJetIdx->GetSize()) {
    return 1.0;  
  }

  int Jjetidx0 = Jet_genJetIdx->At(Cjetidx0);
  int Jjetidx1 = Jet_genJetIdx->At(Cjetidx1);

  bool is_hard = (Jjetidx0 >= 0 && Jjetidx1 >= 0 &&
                  static_cast<std::size_t>(Jjetidx0) < GenJet_pt->GetSize() && 
                  static_cast<std::size_t>(Jjetidx1) < GenJet_pt->GetSize() &&
                  GenJet_pt->At(Jjetidx0) > 10 && GenJet_pt->At(Jjetidx1) > 10);


  int cat = is_hard ? 0 : 1;

  if (CleanJet_pt->GetSize() == 0) {
    return 1.0;
  }

  float jet1pt = CleanJet_pt->At(0);
  if (jet1pt > 350) {
    jet1pt = 350;
  }

  double weight = 1.0;

  if (cat == 0) {
    if (lepId == 11 && ele_hard_weight) {
      weight = ele_hard_weight->Eval(jet1pt);
    } else if (lepId == 13 && mu_hard_weight) {
      weight = mu_hard_weight->Eval(jet1pt);
    }
  }

  return weight;
}

void
ReweightJet1pT::bindTree_(multidraw::FunctionLibrary& _library)
{
  //_library.bindBranch(Category, "category_WJets");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
  _library.bindBranch(Jet_genJetIdx, "Jet_genJetIdx");
  _library.bindBranch(GenJet_pt, "GenJet_pt");
}