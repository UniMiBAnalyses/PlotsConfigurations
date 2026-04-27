#ifndef LHE_GEN__
#define LHE_GEN__

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <TLorentzVector.h>
#include <cmath>
#include <vector>

class LHE_GEN : public multidraw::TTreeFunction {
public:
  LHE_GEN();
  ~LHE_GEN();

  char const* getName() const override { return "LHE_GEN"; }
  TTreeFunction* clone() const override { return new LHE_GEN(); }

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

LHE_GEN::LHE_GEN() : TTreeFunction() {}
LHE_GEN::~LHE_GEN() {}

void
LHE_GEN::beginEvent(long long) {}

double
LHE_GEN::evaluate(unsigned) {
  unsigned n = LHEPart_pt->GetSize();

  std::vector<unsigned> final_quarks;
  std::vector<unsigned> charged_leptons;
  std::vector<unsigned> neutrinos;

  bool has_final_b   = false;
  bool has_final_tau = false;

  for (unsigned i = 0; i < n; ++i) {
    if (LHEPart_status->At(i) != 1) continue;

    int pdg  = LHEPart_pdgId->At(i);
    int apdg = std::abs(pdg);

    // Quarks (d,u,s,c,b,t)
    if (apdg >= 1 && apdg <= 6) {
      final_quarks.push_back(i);
      if (apdg == 5) has_final_b = true; // <-- b veto flag
    }

    // Charged leptons (e, mu, tau)
    if (apdg == 11 || apdg == 13 || apdg == 15) {
      charged_leptons.push_back(i);
      if (apdg == 15) has_final_tau = true;  // <-- tau veto flag
    }

    // Neutrinos
    if (apdg == 12 || apdg == 14 || apdg == 16) {
      neutrinos.push_back(i);
    }
  }

  // ==============================
  // 1b) TAU VETO: se c'è un tau status=1, butta via l'evento
  // ==============================
  if (has_final_b)   return 0.0;
  if (has_final_tau) return 0.0;

  // ==============================
  // 2) JETS: SERVONO ALMENO 2 QUARK
  // ==============================
  if (final_quarks.size() < 2) return 0.0;

  std::sort(final_quarks.begin(), final_quarks.end(),
            [&](unsigned a, unsigned b) {
              return LHEPart_pt->At(a) > LHEPart_pt->At(b);
            });

  unsigned j1 = final_quarks[0];
  unsigned j2 = final_quarks[1];

  float pt1  = LHEPart_pt->At(j1);
  float pt2  = LHEPart_pt->At(j2);
  float eta1 = LHEPart_eta->At(j1);
  float eta2 = LHEPart_eta->At(j2);
  float phi1 = LHEPart_phi->At(j1);
  float phi2 = LHEPart_phi->At(j2);

  // ==============================
  // 3) LEPTONE + NEUTRINO: SERVONO >=1 E >=1
  // ==============================
  if (charged_leptons.empty() || neutrinos.empty()) return 0.0;

  std::sort(charged_leptons.begin(), charged_leptons.end(),
            [&](unsigned a, unsigned b) {
              return LHEPart_pt->At(a) > LHEPart_pt->At(b);
            });
  std::sort(neutrinos.begin(), neutrinos.end(),
            [&](unsigned a, unsigned b) {
              return LHEPart_pt->At(a) > LHEPart_pt->At(b);
            });

  unsigned il = charged_leptons[0];
  unsigned in = neutrinos[0];

  float ptL  = LHEPart_pt->At(il);
  float etaL = LHEPart_eta->At(il);
  float phiL = LHEPart_phi->At(il);

  float ptN  = LHEPart_pt->At(in);
  float etaN = LHEPart_eta->At(in);
  float phiN = LHEPart_phi->At(in);

  // ==============================
  // 4) TAGLI "BASE" + m(l nu) > 50
  // ==============================
  // Jet acceptance (Born-like)
  // if (pt1 < 25.0 || pt2 < 25.0) return 0.0;
  // if (std::abs(eta1) > 5.0 || std::abs(eta2) > 5.0) return 0.0;

  // Lepton acceptance (leading lepton)
  // if (std::abs(etaL) > 2.5) return 0.0;

  // m_jj (massless jets approx)
  float deta = eta1 - eta2;
  float dphi = std::acos(std::cos(phi1 - phi2));
  float mjj  = std::sqrt(2.0f * pt1 * pt2 * (std::cosh(deta) - std::cos(dphi)));
  if (mjj < 120.0) return 0.0;

  // // m(l nu) (massless approx)
  float dphiLN = std::acos(std::cos(phiL - phiN));
  float detaLN = etaL - etaN;
  float mlv    = std::sqrt(2.0f * ptL * ptN * (std::cosh(detaLN) - std::cos(dphiLN)));
  if (mlv < 50.0) return 0.0;

  // ==============================
  // 5) SE PASSA TUTTO (e non aveva tau), return 1
  // ==============================
  return 1.0;
}

void
LHE_GEN::bindTree_(multidraw::FunctionLibrary& _library) {
  _library.bindBranch(LHEPart_pt, "LHEPart_pt");
  _library.bindBranch(LHEPart_eta, "LHEPart_eta");
  _library.bindBranch(LHEPart_phi, "LHEPart_phi");
  _library.bindBranch(LHEPart_mass, "LHEPart_mass");
  _library.bindBranch(LHEPart_pdgId, "LHEPart_pdgId");
  _library.bindBranch(LHEPart_status, "LHEPart_status");
}

#endif