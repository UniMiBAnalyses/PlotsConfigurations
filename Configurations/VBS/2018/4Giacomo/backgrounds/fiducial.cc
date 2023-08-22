#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class FiducialRegion : public multidraw::TTreeFunction {
public:
  FiducialRegion();

  char const* getName() const override { return "FiducialRegion"; }
  TTreeFunction* clone() const override { return new FiducialRegion(); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nGenDressedLepton;
  IntArrayReader* GenDressedLepton_pdgId;
  FloatArrayReader* GenDressedLepton_pt;
  FloatArrayReader* GenDressedLepton_eta;
  FloatArrayReader* GenDressedLepton_phi;
  FloatArrayReader* GenDressedLepton_mass;

  UIntValueReader* nGenJet;
  FloatArrayReader* GenJet_pt;
  FloatArrayReader* GenJet_eta;
  FloatArrayReader* GenJet_phi;
  FloatArrayReader* GenJet_mass;

  FloatValueReader* GenMET_pt;
  FloatValueReader* GenMET_phi;
};

FiducialRegion::FiducialRegion() :
  TTreeFunction()
{
}

double
FiducialRegion::evaluate(unsigned)
{
  unsigned nJ{*nGenJet->Get()};
  if (nJ < 2)
    return 0.;

  unsigned nL{*nGenDressedLepton->Get()};
  if (nL < 2)
    return 0.;

  // more gen lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(GenDressedLepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13)
      continue;

    iPromptL.push_back(iL);
  }

  if (iPromptL.size() < 2)
    return 0.; // false

  if (iPromptL.size() >= 3 && GenDressedLepton_pt->At(iPromptL[2]) >= 10.)
    return 0.;

  if (GenDressedLepton_pdgId->At(iPromptL[0]) * GenDressedLepton_pdgId->At(iPromptL[1]) <= 0)
    return 0.;

  if (GenDressedLepton_pt->At(iPromptL[0]) <= 30. || std::abs(GenDressedLepton_eta->At(iPromptL[0])) >= 2.5 ||
      GenDressedLepton_pt->At(iPromptL[1]) <= 30. || std::abs(GenDressedLepton_eta->At(iPromptL[1])) >= 2.5)
    return 0.;

  ROOT::Math::PtEtaPhiMVector pl0(
    GenDressedLepton_pt->At(iPromptL[0]),
    GenDressedLepton_eta->At(iPromptL[0]),
    GenDressedLepton_phi->At(iPromptL[0]),
    GenDressedLepton_mass->At(iPromptL[0])
  );
  ROOT::Math::PtEtaPhiMVector pl1(
    GenDressedLepton_pt->At(iPromptL[1]),
    GenDressedLepton_eta->At(iPromptL[1]),
    GenDressedLepton_phi->At(iPromptL[1]),
    GenDressedLepton_mass->At(iPromptL[1])
  );

  ROOT::Math::PtEtaPhiMVector pll{pl0 + pl1};

  if (pll.M() <= 20.)
    return 0.;

  //if (!(abs(pll.M()-91.1876)>15 || abs(GenDressedLepton_pdgId->At(iPromptL[0])*GenDressedLepton_pdgId->At(iPromptL[1]))!=121)){
  //  return 0.;
  //}
  // more gen jet selections
  std::vector<unsigned> iCleanJ{};
  iCleanJ.reserve(nJ);

  std::vector<ROOT::Math::PtEtaPhiMVector> dressedLeptons{};
  for (unsigned iL : iPromptL) {
    dressedLeptons.emplace_back(
      GenDressedLepton_pt->At(iL),
      GenDressedLepton_eta->At(iL),
      GenDressedLepton_phi->At(iL),
      GenDressedLepton_mass->At(iL));
  }
  unsigned n{0};
  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    if (GenJet_pt->At(iJ) <= 30.)
      continue;

    bool overlap{false};
    for (auto& p4 : dressedLeptons) {
      if (p4.pt() < 10.)
        continue;

      double dEta{p4.eta() - GenJet_eta->At(iJ)};
      double dPhi{TVector2::Phi_mpi_pi(p4.phi() - GenJet_phi->At(iJ))};
      if (dEta * dEta + dPhi * dPhi < 0.016) {
        overlap = true;
        break;
      }
    }
    if (!overlap){
      ++n;
      iCleanJ.push_back(iJ);
    }
  }
  if (n<2)
    return 0.;

  if (GenJet_pt->At(iCleanJ[0]) <= 30. || std::abs(GenJet_eta->At(iCleanJ[0])) >= 4.7 ||
      GenJet_pt->At(iCleanJ[1]) <= 30. || std::abs(GenJet_eta->At(iCleanJ[1])) >= 4.7)
    return 0.;

  ROOT::Math::PtEtaPhiMVector pj0(
    GenJet_pt->At(iCleanJ[0]),
    GenJet_eta->At(iCleanJ[0]),
    GenJet_phi->At(iCleanJ[0]),
    GenJet_mass->At(iCleanJ[0])
  );
  ROOT::Math::PtEtaPhiMVector pj1(
    GenJet_pt->At(iCleanJ[1]),
    GenJet_eta->At(iCleanJ[1]),
    GenJet_phi->At(iCleanJ[1]),
    GenJet_mass->At(iCleanJ[1])
  );

  ROOT::Math::PtEtaPhiMVector pjj{pj0 + pj1};

  if (pjj.M() <= 500.)
    return 0.;
  if (abs(GenJet_eta->At(iCleanJ[0])-GenJet_eta->At(iCleanJ[1]))<=2.5)
    return 0.;

  //double genMet{*GenMET_pt->Get()};
  //if (genMet<=30)
  // return 0.;

  // gen zepp
  //double zepp1=abs((GenDressedLepton_eta->At(iPromptL[0])-(GenJet_eta->At(iCleanJ[0])+GenJet_eta->At(iCleanJ[1]))/2.)/(GenJet_eta->At(iCleanJ[0])-GenJet_eta->At(iCleanJ[1])));
  //double zepp2=abs((GenDressedLepton_eta->At(iPromptL[1])-(GenJet_eta->At(iCleanJ[0])+GenJet_eta->At(iCleanJ[1]))/2.)/(GenJet_eta->At(iCleanJ[0])-GenJet_eta->At(iCleanJ[1])));
  //if (zepp1>=0.75 || zepp2>=0.75){
  //  return 0.;
  //}
  return 1.;
}

void
FiducialRegion::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nGenDressedLepton, "nGenDressedLepton");
  _library.bindBranch(GenDressedLepton_pdgId, "GenDressedLepton_pdgId");
  _library.bindBranch(GenDressedLepton_pt, "GenDressedLepton_pt");
  _library.bindBranch(GenDressedLepton_eta, "GenDressedLepton_eta");
  _library.bindBranch(GenDressedLepton_phi, "GenDressedLepton_phi");
  _library.bindBranch(GenDressedLepton_mass, "GenDressedLepton_mass");

  _library.bindBranch(nGenJet, "nGenJet");
  _library.bindBranch(GenJet_pt, "GenJet_pt");
  _library.bindBranch(GenJet_eta, "GenJet_eta");
  _library.bindBranch(GenJet_phi, "GenJet_phi");
  _library.bindBranch(GenJet_mass, "GenJet_mass");

  _library.bindBranch(GenMET_pt, "GenMET_pt");
  _library.bindBranch(GenMET_phi, "GenMET_phi");
}
