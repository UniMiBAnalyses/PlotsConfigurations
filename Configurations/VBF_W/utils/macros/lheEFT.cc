#ifndef LHE_EFT__
#define LHE_EFT__

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <TLorentzVector.h>
#include <cmath>
#include <vector>

class LHE_EFT : public multidraw::TTreeFunction {
public:
  LHE_EFT();
  ~LHE_EFT();

  char const* getName() const override { return "LHE_EFT"; }
  TTreeFunction* clone() const override { return new LHE_EFT(); }

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

LHE_EFT::LHE_EFT() : TTreeFunction() {}
LHE_EFT::~LHE_EFT() {}

void
LHE_EFT::beginEvent(long long) {}

double
LHE_EFT::evaluate(unsigned) {
  unsigned n = LHEPart_pt->GetSize();

  std::vector<unsigned> final_quarks;
  std::vector<unsigned> charged_leptons;
  std::vector<unsigned> neutrinos;

  bool has_b_finalstate = false;

  // ==============================
  // 1) LOOP SULLE PARTICELLE
  // ==============================
  for (unsigned i = 0; i < n; ++i) {
    int status = LHEPart_status->At(i);
    int pdg    = LHEPart_pdgId->At(i);
    int apdg   = std::abs(pdg);

    // --- VETO: b-quark in stato finale ---
    if (status == 1 && apdg == 5) {
      has_b_finalstate = true;
    }

    // Consideriamo solo status == 1 per la selezione
    if (status != 1)
      continue;

    // Quarks finali (d..t)
    if (apdg >= 1 && apdg <= 6) {
      final_quarks.push_back(i);
    }

    // Leptoni carichi (e, mu, tau)
    if (apdg == 11 || apdg == 13 || apdg == 15) {
      charged_leptons.push_back(i);
    }

    // Neutrini
    if (apdg == 12 || apdg == 14 || apdg == 16) {
      neutrinos.push_back(i);
    }
  }

  // 1-bis) Applica il veto sui b
  if (has_b_finalstate)
    return 0.0;

  // ==============================
  // 2) JETS: SERVONO ALMENO 2 QUARK
  // ==============================
  if (final_quarks.size() < 2)
    return 0.0;

  // (a) tag su eta MAX di QUALSIASI jet: |eta| < 5
  double max_abs_eta_jet = 0.0;
  for (auto idx : final_quarks) {
    double eta = LHEPart_eta->At(idx);
    double absEta = std::abs(eta);
    if (absEta > max_abs_eta_jet)
      max_abs_eta_jet = absEta;
  }
  if (max_abs_eta_jet > 5.0)
    return 0.0;

  // (b) ordina i quark per pT (leading jets)
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

  // (c) tagli sui due leading jets
  if (std::abs(eta1) > 5.0 || std::abs(eta2) > 5.0)
    return 0.0;

  // (d) m_jj > 300 (usiamo solo pt,eta,phi come prima)
  float deta = eta1 - eta2;
  float dphi = std::acos(std::cos(phi1 - phi2));
  float mjj  = std::sqrt(2.0 * pt1 * pt2 * (std::cosh(deta) - std::cos(dphi)));

  if (mjj < 300.0)
    return 0.0;

  // ==============================
  // 3) LEPTONE E NEUTRINO
  // ==============================
  if (charged_leptons.empty() || neutrinos.empty())
    return 0.0;

  // leading leptone
  std::sort(charged_leptons.begin(), charged_leptons.end(),
            [&](unsigned a, unsigned b) {
              return LHEPart_pt->At(a) > LHEPart_pt->At(b);
            });
  unsigned il   = charged_leptons[0];
  int pdgL      = LHEPart_pdgId->At(il);
  float ptL     = LHEPart_pt->At(il);
  float etaL    = LHEPart_eta->At(il);
  float phiL    = LHEPart_phi->At(il);
  float massL   = LHEPart_mass->At(il);

  // leading neutrino (per semplicità)
  std::sort(neutrinos.begin(), neutrinos.end(),
            [&](unsigned a, unsigned b) {
              return LHEPart_pt->At(a) > LHEPart_pt->At(b);
            });
  unsigned inu   = neutrinos[0];
  float ptNu     = LHEPart_pt->At(inu);
  float etaNu    = LHEPart_eta->At(inu);
  float phiNu    = LHEPart_phi->At(inu);
  float massNu   = LHEPart_mass->At(inu);

  // accettanza leptonica
  if (std::abs(etaL) > 2.5)
    return 0.0;

  // (e) m(l + nu) > 50
  TLorentzVector pL, pNu;
  pL.SetPtEtaPhiM(ptL,  etaL,  phiL,  massL);
  pNu.SetPtEtaPhiM(ptNu, etaNu, phiNu, massNu);
  float mlnu = (pL + pNu).M();

  if (mlnu < 50.0)
    return 0.0;

  // ==============================
  // 4) Distinzione carica:
  //    1 = l+
  //    2 = l-
  // ==============================
  if (pdgL == -11 || pdgL == -13 || pdgL == -15)
    return 1.0;   // l+
  else if (pdgL == 11 || pdgL == 13 || pdgL == 15)
    return 1.0;   // l-
  else
    return 0.0;   // qualcosa di strano
}

void
LHE_EFT::bindTree_(multidraw::FunctionLibrary& _library) {
  _library.bindBranch(LHEPart_pt, "LHEPart_pt");
  _library.bindBranch(LHEPart_eta, "LHEPart_eta");
  _library.bindBranch(LHEPart_phi, "LHEPart_phi");
  _library.bindBranch(LHEPart_mass, "LHEPart_mass");
  _library.bindBranch(LHEPart_pdgId, "LHEPart_pdgId");
  _library.bindBranch(LHEPart_status, "LHEPart_status");
}

#endif