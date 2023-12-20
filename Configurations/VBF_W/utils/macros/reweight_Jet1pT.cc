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
  _file->Close();
  delete ele_hard_weight;
  delete mu_hard_weight;
  delete _file;
}


double
ReweightJet1pT::evaluate(unsigned iJ){
  int lepId = abs(Lepton_pdgId->At(0));

  int Cjetidx0 = CleanJet_jetIdx->At(0);
  int Cjetidx1 = CleanJet_jetIdx->At(1);

  int Jjetidx0 = Jet_genJetIdx->At(Cjetidx0);
  int Jjetidx1 = Jet_genJetIdx->At(Cjetidx1);

  int cat = 0.*(Jjetidx0 >= 0 && Jjetidx1 >= 0 && GenJet_pt->At(Jjetidx0) > 10 && GenJet_pt->At(Jjetidx1) > 10) + 1.*(!(Jjetidx0 >= 0 && Jjetidx1 >= 0 && GenJet_pt->At(Jjetidx0) > 10 && GenJet_pt->At(Jjetidx1) > 10));


  //cat==0 hard, cat==1 PU 

  float jet1pt = CleanJet_pt->At(0);
  double weight = 1.;
  if (jet1pt > 350){jet1pt = 350;}

  if(cat==0 and lepId == 11){
    weight = ele_hard_weight->Eval(jet1pt);
  }

  if(cat==0 and lepId == 13){
    weight = mu_hard_weight->Eval(jet1pt);
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