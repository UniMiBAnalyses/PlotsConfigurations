#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TFile.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TString.h"
#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/VectorUtil.h"

#include <iostream>
using namespace ROOT::Math;
typedef TTreeReaderValue<Double_t> DoubleValueReader;


class LepWPairing: public multidraw::TTreeFunction {
public:
  LepWPairing(vector<PtEtaPhiMVector> leptons);
  ~LepWPairing();

  char const* getName() const override { return "ReweightZpT";}
  TTreeFunction* clone() const override { return new ReweightZpT(_weights_file.Data(),_debug); }

  unsigned getNdata() override { return 1; } 
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;
  

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  std::array<double> outputValues;

  void setValues();
  TString _weights_file;
  TFile* _file;
  TH2D* weights;
  //TH1D* hard_weight;
  //TH1D* PU_weight;
  bool _debug;
  
  //DoubleValueReader * Category;
  FloatValueReader * ptll;
  //FloatValueReader * ptj2;
  FloatArrayReader * ptj;
  //FloatValueReader * ZpT;

};

ReweightZpT::ReweightZpT(const char * weights_file ,bool debug) :
  TTreeFunction(), _weights_file(weights_file),_debug(debug)
{
  _file = new TFile(weights_file,"READ");

  weights = (TH2D*)_file->Get("corr");
  //hard_weight = (TH1D*)_file->Get("corr_hard");
  //PU_weight = (TH1D*)_file->Get("corr_PU");

  weights->SetDirectory(0);
  //hard_weight->SetDirectory(0);
  //PU_weight->SetDirectory(0);

}

ReweightZpT::~ReweightZpT(){
  _file->Close();
  delete weights;
  //delete hard_weight;
  //delete PU_weight;
  delete _file;
}


double
ReweightZpT::evaluate(unsigned iJ){
//  int lepId = abs(Lepton_pdgId->At(0));
  //int cat = abs(Category->At(0));
  //int cat = int(*(Category->Get()));
  //float zpt = *(ZpT->Get());
  float ptl = *ptll->Get();
  float ptj2 = ptj->At(1);
  //TH1D * h = cat==0? hard_weight : PU_weight;
  //TH2D * h = weights ;
  
  double weight = weights->GetBinContent(weights->GetBin(weights->GetXaxis()->FindBin(ptl), weights->GetYaxis()->FindBin(ptj2)));
  if (weight >= 1e-4 && weight <2) return weight;
  return 1.;
//  if (cat==1){
//    return 1;
//  }
//  if (ptj<500 && ptj>50){
//      weight =  h->GetBinContent(h->FindBin(ptj));
//  } else{
//      weight = 1;
//  }

//  if (zpt<1000){
//      weight =  h->GetBinContent(h->FindBin(zpt));
//  } else{
//      weight = 0.75;
//  }

}

void
ReweightZpT::bindTree_(multidraw::FunctionLibrary& _library)
{
  //_library.bindBranch(Category, "category_DY");
  _library.bindBranch(ptll, "ptll");
  _library.bindBranch(ptj, "CleanJet_pt");
//  _library.bindBranch(Lepton_pdgId, "Leptons_pdgId");
  //_library.bindBranch(ZpT, "ptll");
}

