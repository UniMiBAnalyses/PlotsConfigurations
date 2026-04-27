#ifndef LHE_mjj__
#define LHE_mjj__

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <TLorentzVector.h>
#include <cmath>
#include <vector>

class LHE_selection : public multidraw::TTreeFunction {
public:
  LHE_selection();
  ~LHE_selection();

  char const* getName() const override { return "LHE_selection"; }
  TTreeFunction* clone() const override { return new LHE_selection(); }

  void beginEvent(long long) override;
  unsigned getNdata() override { return 1; }
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  FloatArrayReader* LHEPart_pt{};
  FloatArrayReader* LHEPart_eta{};
  FloatArrayReader* LHEPart_phi{};
  FloatArrayReader* LHEPart_mass{};
  IntArrayReader* LHEPart_pdgId{};
  IntArrayReader* LHEPart_status{};
};

LHE_selection::LHE_selection() : TTreeFunction() {}
LHE_selection::~LHE_selection() {}

void
LHE_selection::beginEvent(long long) {}

double LHE_selection::evaluate(unsigned) {

  unsigned n = LHEPart_pt->GetSize();

  std::vector<unsigned> final_quarks;
  std::vector<unsigned> charged_leptons;
  std::vector<unsigned> neutrinos;

  // 1) LOOP
  for (unsigned i = 0; i < n; ++i) {
    if (LHEPart_status->At(i) != 1) continue;

    int apdg = std::abs(LHEPart_pdgId->At(i));

    if (apdg >= 1 && apdg <= 6) final_quarks.push_back(i);
    if (apdg == 11 || apdg == 13 || apdg == 15) charged_leptons.push_back(i);
    if (apdg == 12 || apdg == 14 || apdg == 16) neutrinos.push_back(i);
  }

  // Richieste minime: >=2 quark, >=1 lepton
  if (final_quarks.size() < 2) return 0.0;
  if (charged_leptons.empty()) return 0.0;

  // Ordina quark per pT e prendi i due leading
  std::sort(final_quarks.begin(), final_quarks.end(),
            [&](unsigned a, unsigned b) { return LHEPart_pt->At(a) > LHEPart_pt->At(b); });

  unsigned j1 = final_quarks[0];
  unsigned j2 = final_quarks[1];

  float pt1  = LHEPart_pt->At(j1);
  float pt2  = LHEPart_pt->At(j2);
  float eta1 = LHEPart_eta->At(j1);
  float eta2 = LHEPart_eta->At(j2);
  float phi1 = LHEPart_phi->At(j1);
  float phi2 = LHEPart_phi->At(j2);

  // mjj (con dphi robusto)
  float deta = eta1 - eta2;
  float dphi = std::acos(std::cos(phi1 - phi2));
  float dphi_n = phi1 - phi2;
  float mjj  = std::sqrt(2.0f * pt1 * pt2 * (std::cosh(deta) - std::cos(dphi_n)));

  // --- CUT BASE: mjj > 120 ---
  if (mjj < 120.0) return 0.0;

  // Se vuoi anche m(l nu) > 50, mettilo QUI come optional
  // bool require_mlv = true; // oppure da config
  // if (require_mlv) { ... calcola mlv e se <50 return 0; }


  // --- CUT TIGHT: ptj > 25 sui due leading ---
  if (pt1 < 25.0f || pt2 < 25.0f) return 0.0;

  //  se esiste un b, richiedi ptb>25 ---
  for (unsigned idx : final_quarks) {
    int apdg = std::abs(LHEPart_pdgId->At(idx));
    if (apdg == 5 && LHEPart_pt->At(idx) <= 25.0f) {
      return 0.0;
    }
  }

  return 1.0;
}

void
LHE_selection::bindTree_(multidraw::FunctionLibrary& _library) {
  _library.bindBranch(LHEPart_pt, "LHEPart_pt");
  _library.bindBranch(LHEPart_eta, "LHEPart_eta");
  _library.bindBranch(LHEPart_phi, "LHEPart_phi");
  _library.bindBranch(LHEPart_mass, "LHEPart_mass");
  _library.bindBranch(LHEPart_pdgId, "LHEPart_pdgId");
  _library.bindBranch(LHEPart_status, "LHEPart_status");
}

#endif