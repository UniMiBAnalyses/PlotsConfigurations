#ifndef PDFsRead
#define PDFsRead

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

typedef TTreeReaderValue<Double_t> DoubleValueReader;
using namespace std;

class PDFsReader : public multidraw::TTreeFunction {
public:
  PDFsReader(string file_path, bool up, bool down);
  ~PDFsReader();

  char const* getName() const override { return "PDFsReader"; }
  TTreeFunction* clone() const override { return new PDFsReader(file_path, up, down); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
  void bindTree_(multidraw::FunctionLibrary&) override;

private:
  bool up;
  bool down;
  string file_path;

  TFile* file;
  TH2F* up_histo;
  TH2F* down_histo;

  DoubleValueReader * DNNJoined;
  FloatArrayReader* CleanJet_phi{};
};

// 📌 Costruttore: Carica il file ROOT e gli istogrammi
PDFsReader::PDFsReader(string in_file_path, bool up, bool down)
  : TTreeFunction(), file_path(in_file_path), up(up), down(down) {

  file = new TFile(file_path.c_str(), "READ");
  if (!file || file->IsZombie()) {
    cerr << " Error: ROOT file ZOMBIE " << file_path << endl;
    return;
  }

  up_histo = (TH2F*) file->Get("h2d_envelope_up");
  down_histo = (TH2F*) file->Get("h2d_envelope_down");

  if (up_histo) up_histo->SetDirectory(0);
  if (down_histo) down_histo->SetDirectory(0);

  file->Close();
  delete file;  // no memory leak
}

double PDFsReader::evaluate(unsigned) {

  float DNNval = (*DNNJoined->Get());
  float Dphij1j2 = fabs(CleanJet_phi->At(0) - CleanJet_phi->At(1)) * 
                      (fabs(CleanJet_phi->At(0) - CleanJet_phi->At(1)) < 3.1415) + 
                      (2 * 3.1415 - fabs(CleanJet_phi->At(0) - CleanJet_phi->At(1))) * 
                      (fabs(CleanJet_phi->At(0) - CleanJet_phi->At(1)) >= 3.1415);
  double weight = 1.0;

  if (up && up_histo) {
    weight = up_histo->GetBinContent(up_histo->FindBin(DNNval, Dphij1j2));
  } 
  else if (down && down_histo) {
    weight = down_histo->GetBinContent(down_histo->FindBin(DNNval, Dphij1j2));
  } 
  else {
    cerr << "Up/down request but histo not open correctly!!!" << endl;
  }

  // std::cout << "returning weight: " << weight << " given DNN and dphi: " << DNNval << " " << Dphij1j2 << std::endl;
  return weight;
}

// 📌 Funzione `bindTree_()`
void PDFsReader::bindTree_(multidraw::FunctionLibrary& _library) {   
  _library.bindBranch(DNNJoined, "DNNJoined");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
}

// 📌 Distruttore: Libera la memoria
PDFsReader::~PDFsReader() {
  DNNJoined = nullptr;

  if (up_histo) delete up_histo;
  if (down_histo) delete down_histo;
}

#endif