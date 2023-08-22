#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TFile.h"
#include "TH2D.h"
#include "TString.h"
#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/VectorUtil.h"

#include <iostream>
using namespace ROOT::Math;

// // Search for the GenParticle index that correspond to the desired lepton/neutrino (based on pt correspondence):
// int findGenPartIdx(float pTlep, FloatArrayReader* GP_pt{};) {
//   double prov = 9999.9;
//   int idx = 0;
//   for (long unsigned int i=0; i< GP_pt.size()-1; ++i){
//     if (abs(ptLep-GP_pt.at(i)) < prov){
//       prov = abs(ptLep-GP_pt.at(i));
//       idx = i;
//     }
//    }
//   return idx;
// }

// // Search for the W mother index of any GenParticle (based on the GenParticle index):
// // THERE IS NO CHECK NOT SMART !!
// int findWMother(int idx, FloatArrayReader* GP_pt{}, FloatArrayReader* GP_pdgid{}, FloatArrayReader* GP_momidx{}){
//   idxW = GP_momidx.at(GP_momidx.at(GP_mom_idx.at(idx)));
//     // WANT TO ADD CHECKS
//     return idxW;
// }

class GenLevelObjects : public multidraw::TTreeFunction {
public:
  GenLevelObjects();
  ~GenLevelObjects(){};

  char const* getName() const override { return "GenLevelObjects"; }
  TTreeFunction* clone() const override { return new GenLevelObjects(); }

  void setValues();
  void beginEvent(long long) override;
  unsigned getNdata() override { return outputValues.size(); } 
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;
  

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  std::array<int,2> outputValues;
  
  UIntValueReader* nGenPart{};
  IntArrayReader* GenPart_status{};
  IntArrayReader* GenPart_pdgId{};
  IntArrayReader* GenPart_genPartIdxMother{};
  FloatArrayReader* GenPart_pt{};
  FloatArrayReader* GenPart_eta{};
  FloatArrayReader* GenPart_phi{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* NeutrinoGen_pt{};
};

GenLevelObjects::GenLevelObjects() :
  TTreeFunction(){}

void
GenLevelObjects::beginEvent(long long _iEntry)
{
  setValues();
}


double
GenLevelObjects::evaluate(unsigned iJ)
{
  // 0) index of NeutrinoGen particle corresponding to W0 (Lep0)
  // 1) index of NeutrinoGen particle corresponding to W1 (Lep1)
  return outputValues[iJ];
}

void
GenLevelObjects::setValues()
{
  // indexes (among the Gen Partcles) of the leptons I care about:
  int idxl0;
  int idxl1;
  int idxn0;
  int idxn1;

  float provl0 = 9999.9;
  float provl1 = 9999.9;
  float provn0 = 9999.9;
  float provn1 = 9999.9;

  for (long unsigned int i=0; i< *(nGenPart->Get()); ++i){
    if (abs(Lepton_pt->At(0) - GenPart_pt->At(i)) < provl0){
      provl0 = abs(Lepton_pt->At(0) - GenPart_pt->At(i));
      idxl0 = i;
    }
    if (abs(Lepton_pt->At(1) - GenPart_pt->At(i)) < provl1){
      provl1 = abs(Lepton_pt->At(1) - GenPart_pt->At(i));
      idxl1 = i;
    }
    if (abs(NeutrinoGen_pt->At(0) - GenPart_pt->At(i)) < provn0){
      provn0 = abs(NeutrinoGen_pt->At(0) - GenPart_pt->At(i));
      idxn0 = i;
    }
    if (abs(NeutrinoGen_pt->At(1) - GenPart_pt->At(i)) < provn1){
      provn1 = abs(NeutrinoGen_pt->At(1) - GenPart_pt->At(i));
      idxn1 = i;
    }
  }

  int idxW_l0 = (GenPart_genPartIdxMother->At(GenPart_genPartIdxMother->At(idxl0)));
  int idxW_l1 = (GenPart_genPartIdxMother->At(GenPart_genPartIdxMother->At(idxl1)));
  int idxW_n0 = (GenPart_genPartIdxMother->At(GenPart_genPartIdxMother->At(idxn0)));
  int idxW_n1 = (GenPart_genPartIdxMother->At(GenPart_genPartIdxMother->At(idxn1)));

  std::cout << "leptons: " << idxW_l0 << " " << idxW_l1 << "   neutrinos: " << idxW_n0 << " " << idxW_n1 << std::endl;

  if ((idxW_l0 == idxW_n0) && (idxW_l1 == idxW_n1)){
    outputValues[0] = 0;
    outputValues[1] = 1;
    //    std::cout << " case 0 1" << std::endl;
  } else if ((idxW_l0 == idxW_n1) && (idxW_l1 == idxW_n0)){
    outputValues[0] = 1;
    outputValues[1] = 0;
    //    std::cout << " case 1 0" << std::endl;
  } else {
    outputValues[0] = 999;
    outputValues[1] = 999;
    std::cout << "caso schifo" << std::endl;
  }




  return;
}

void
GenLevelObjects::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nGenPart, "nGenPart");
  _library.bindBranch(GenPart_status, "GenPart_status"),
  _library.bindBranch(GenPart_pdgId, "GenPart_pdgId");
  _library.bindBranch(GenPart_genPartIdxMother, "GenPart_genPartIdxMother");
  _library.bindBranch(GenPart_pt, "GenPart_pt");
  _library.bindBranch(GenPart_eta, "GenPart_eta");
  _library.bindBranch(GenPart_phi, "GenPart_phi");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(NeutrinoGen_pt, "NeutrinoGen_pt");
}

