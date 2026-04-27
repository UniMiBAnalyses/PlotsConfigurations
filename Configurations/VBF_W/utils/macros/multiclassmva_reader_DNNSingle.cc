#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluatorSavedModel.hh"

#include "TFile.h"
#include "TMath.h"
#include "TGraph.h"

#include <cmath>
#include <string>
#include <iostream>
// #include <math.h>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAREADERDNNMULTISINGLE
#define MVAREADERDNNMULTISINGLE

typedef TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReaderDNNMultiSingle : public multidraw::TTreeFunction {
public:
  
  MVAReaderDNNMultiSingle(const char* model_path_ev, const char* model_path_odd,  bool verbose);

  char const* getName() const override { return "MVAReaderDNNMultiSingle"; }
  TTreeFunction* clone() const override { return new MVAReaderDNNMultiSingle(model_path_ev_.c_str(), model_path_odd_.c_str(), verbose); }

  std::string model_path_ev_;
  std::string model_path_odd_;

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  ~MVAReaderDNNMultiSingle();
  
  DNNEvaluatorSavedModel* dnn_tensorflow_ev;
  DNNEvaluatorSavedModel* dnn_tensorflow_odd;

  FloatValueReader* detajj{};
  FloatArrayReader* CleanJet_pt{};
  FloatValueReader* mjj{};
  FloatArrayReader* CleanJet_eta{};
  FloatArrayReader* CleanJet_phi{};

  FloatArrayReader* Lepton_eta{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_phi{};

  FloatValueReader* PuppiMET_phi{};
  FloatValueReader* PuppiMET_pt{};
  ULong64ValueReader* event{};

};


MVAReaderDNNMultiSingle::MVAReaderDNNMultiSingle(const char* model_path_ev, const char* model_path_odd, bool verbose):
    model_path_ev_(model_path_ev), 
    model_path_odd_(model_path_odd), 
    verbose(verbose)
{

    if (verbose) {
      std::cout << "Loading model: " << model_path_ev << std::endl;
      std::cout << "Loading model: " << model_path_odd << std::endl;
    }
    dnn_tensorflow_ev = new DNNEvaluatorSavedModel(model_path_ev, verbose);
    dnn_tensorflow_odd = new DNNEvaluatorSavedModel(model_path_odd, verbose);

}



double
MVAReaderDNNMultiSingle::evaluate(unsigned)
{

  // I have to bypass the aliases.py problem.
  // from other PlotConfig, to import aliases I woiuld need to declare TTreeReaderArray<Double_t>* 
  // but this, in CMSSW11 does not work (apparently). I shoud have to exagerate the usage of Alt$ to make every alias
  // of multiplicity 0 (you can see the multiplicity from the .out of jobs).. But still, does not work!
  // So since I need this macro, I redefine the aliases I need..
  // So I need those making up ptW, R_AN and Zl1 and hopefully it will work, as the reweight macro.
  // Is this the smarter way? Probably not. Do I care? Neither. So lets do this

  // ++++++++++++++ Zl1 +++++++++++++++++
  float Zl1 = (Lepton_eta->At(0) - 0.5*(CleanJet_eta->At(0) + CleanJet_eta->At(1)));

  // ++++++++++++++ L1 +++++++++++++++++
  double x_ptl1 = ((Lepton_pt->At(0)) * (std::cos(Lepton_phi->At(0))));
  double y_ptl1 = ((Lepton_pt->At(0)) * (std::sin(Lepton_phi->At(0))));

  // ++++++++++++++ J1, J2 +++++++++++++++++
  double x_ptj1 = ((CleanJet_pt->At(0)) * (std::cos(CleanJet_phi->At(0))));
  double y_ptj1 = ((CleanJet_pt->At(0)) * (std::sin(CleanJet_phi->At(0))));

  double x_ptj2 = ((CleanJet_pt->At(1)) * (std::cos(CleanJet_phi->At(1))));
  double y_ptj2 = ((CleanJet_pt->At(1)) * (std::sin(CleanJet_phi->At(1))));

  // ++++++++++++++ MET +++++++++++++++++
  double x_ptMET = ((*PuppiMET_pt->Get()) * (std::cos(*PuppiMET_phi->Get())));
  double y_ptMET = ((*PuppiMET_pt->Get()) * (std::sin(*PuppiMET_phi->Get())));

  // ++++++++++++++ W (L1 + MET) +++++++++++++++++
  double x_ptW = (x_ptl1 + x_ptMET);
  double y_ptW = (y_ptl1 + y_ptMET);
  float ptW = (std::sqrt((x_ptW*x_ptW) + (y_ptW*y_ptW)));

  // ++++++++++++++ MTW (L1 + MET) +++++++++++++++++
  float mtw1 = (std::sqrt(2 * (Lepton_pt->At(0)) * (*PuppiMET_pt->Get()) * (1 - (std::cos(Lepton_phi->At(0) - *PuppiMET_phi->Get())))));

  // ++++++++++++++ R from AN +++++++++++++++++
  double x_Wjj = (x_ptj1 + x_ptj2 + x_ptW);
  double y_Wjj = (y_ptj1 + y_ptj2 + y_ptW);
  double ptWjj = (std::sqrt((x_Wjj*x_Wjj) + (y_Wjj*y_Wjj)));
  float R_AN = (ptWjj / ((CleanJet_pt->At(0)) + (CleanJet_pt->At(1)) + ptW));

  // ++++++++++++++ dphijet1jet2 +++++++++++++++++
  float Dphijet1jet2 = (CleanJet_phi->At(0) - CleanJet_phi->At(1)) - 2*3.1415*((CleanJet_phi->At(0) - CleanJet_phi->At(1)) > 3.1415) + 2*3.1415*((CleanJet_phi->At(0) - CleanJet_phi->At(1)) < -3.1415);

  float Dphijet1met = abs(CleanJet_phi->At(0) - *PuppiMET_phi->Get()) * (abs(CleanJet_phi->At(0) - *PuppiMET_phi->Get()) < 3.1415) + (2 * 3.1415 - abs(CleanJet_phi->At(0) - *PuppiMET_phi->Get())) * (abs(CleanJet_phi->At(0) - *PuppiMET_phi->Get()) >= 3.1415);

  float Dphijet2met = abs(CleanJet_phi->At(1) - *PuppiMET_phi->Get()) * (abs(CleanJet_phi->At(1) - *PuppiMET_phi->Get()) < 3.1415) + (2 * 3.1415 - abs(CleanJet_phi->At(1) - *PuppiMET_phi->Get())) * (abs(CleanJet_phi->At(1) - *PuppiMET_phi->Get()) >= 3.1415);

  float Dphilep1jet1 = abs(Lepton_phi->At(0) - CleanJet_phi->At(0)) * (abs(Lepton_phi->At(0) - CleanJet_phi->At(0)) < 3.1415) + (2 * 3.1415 - abs(Lepton_phi->At(0) - CleanJet_phi->At(0))) * (abs(Lepton_phi->At(0) - CleanJet_phi->At(0)) >= 3.1415);

  float Dphilep1jet2 = abs(Lepton_phi->At(0) - CleanJet_phi->At(1)) * (abs(Lepton_phi->At(0) - CleanJet_phi->At(1)) < 3.1415) + (2 * 3.1415 - abs(Lepton_phi->At(0) - CleanJet_phi->At(1))) * (abs(Lepton_phi->At(0) - CleanJet_phi->At(1)) >= 3.1415);

  float Dphilep1met = abs(Lepton_phi->At(0) - *PuppiMET_phi->Get()) * (abs(Lepton_phi->At(0) - *PuppiMET_phi->Get()) < 3.1415) + (2 * 3.1415 - abs(Lepton_phi->At(0) - *PuppiMET_phi->Get())) * (abs(Lepton_phi->At(0) - *PuppiMET_phi->Get()) >= 3.1415);
  
  // ++++++++++++++ deta +++++++++++++++++
  
  float detalep1jet1 = (Lepton_eta->At(0) - CleanJet_eta->At(0));

  float detalep1jet2 = (Lepton_eta->At(0) - CleanJet_eta->At(1));

  // ++++++++++++++ mtWs +++++++++++++++++

  float mlep1jet1 = TMath::Sqrt(2 * Lepton_pt->At(0) * CleanJet_pt->At(0) * (TMath::CosH(Lepton_eta->At(0) - CleanJet_eta->At(0)) - TMath::Cos(Lepton_phi->At(0) - CleanJet_phi->At(0))));

  float mlep1jet2 = TMath::Sqrt(2 * Lepton_pt->At(0) * CleanJet_pt->At(1) * (TMath::CosH(Lepton_eta->At(0) - CleanJet_eta->At(1)) - TMath::Cos(Lepton_phi->At(0) - CleanJet_phi->At(1))));
  
  // ++++++++++++++ mtWs +++++++++++++++++

  float ptjj = TMath::Sqrt((x_ptj1 + x_ptj2) * (x_ptj1 + x_ptj2) + (y_ptj1 + y_ptj2) * (y_ptj1 + y_ptj2));

  ULong64_t event_ = *event->Get();

  // ++++++++++++++ DNN +++++++++++++++++
  std::vector<float> input{};

  input.push_back(Dphijet1jet2);

  input.push_back(Dphijet1met);

  input.push_back(Dphijet2met);

  input.push_back(Dphilep1jet1);

  input.push_back(Dphilep1jet2);

  input.push_back(Dphilep1met);

  input.push_back(R_AN);

  input.push_back(Zl1);

  input.push_back((float) *(detajj->Get()) );

  input.push_back(detalep1jet1);

  input.push_back(detalep1jet2);

  input.push_back((float) Lepton_eta->At(0));

  input.push_back((float) CleanJet_eta->At(0));

  input.push_back((float) CleanJet_eta->At(1));

  input.push_back((float) CleanJet_phi->At(0));

  input.push_back((float) CleanJet_phi->At(1));

  input.push_back((float) CleanJet_pt->At(0));

  input.push_back((float) CleanJet_pt->At(1));

  input.push_back((float) *(mjj->Get()) );

  input.push_back(mlep1jet1);

  input.push_back(mlep1jet2);

  input.push_back(mtw1);

  ///for the model with the new (reduced) binning
  input.push_back((float) CleanJet_pt->GetSize());

  input.push_back((float) Lepton_phi->At(0));

  input.push_back((float) Lepton_pt->At(0));

  input.push_back(ptW); 

  input.push_back(ptjj);

  input.push_back((float) *PuppiMET_phi->Get());

  input.push_back((float) *PuppiMET_pt->Get());

  std::vector<float> dnn_scores;
  if (std::fmod(event_, 2) == 0){
    dnn_scores = dnn_tensorflow_odd->analyze(input);
  } else {
    dnn_scores = dnn_tensorflow_ev->analyze(input);
  }

  // Probabilità massima tra le classi
  // auto max_it = std::max_element(dnn_scores.begin() + 1, dnn_scores.end());
  auto max_it = std::max_element(dnn_scores.begin(), dnn_scores.end());
  float max_prob = *max_it;

  // Controlla se ci sono più valori uguali al massimo
  // int max_count = std::count(dnn_scores.begin() + 1, dnn_scores.end(), max_prob);
  int max_count = std::count(dnn_scores.begin(), dnn_scores.end(), max_prob);
  if (max_count > 1) {
    return -1.0; // Ambiguità, esci subito
  }

  int max_index = std::distance(dnn_scores.begin(), std::find(dnn_scores.begin(), dnn_scores.end(), max_prob));

  return max_index+0.5;
}

void
MVAReaderDNNMultiSingle::bindTree_(multidraw::FunctionLibrary& _library)
{  
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(mjj, "mjj");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(PuppiMET_phi, "PuppiMET_phi");
  _library.bindBranch(PuppiMET_pt, "PuppiMET_pt");
  _library.bindBranch(event, "event");
}


MVAReaderDNNMultiSingle::~MVAReaderDNNMultiSingle() {
    delete dnn_tensorflow_ev;
    delete dnn_tensorflow_odd;
}

#endif 
