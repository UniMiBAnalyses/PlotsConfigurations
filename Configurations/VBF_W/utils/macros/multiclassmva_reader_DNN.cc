#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluatorSavedModel.hh"

#include "TFile.h"
// #include "TMath.h"
#include "TGraph.h"

#include <cmath>
#include <string>
#include <iostream>
// #include <math.h>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAREADERDNNMULTI
#define MVAREADERDNNMULTI

typedef TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReaderDNNMulti : public multidraw::TTreeFunction {
public:
  
  MVAReaderDNNMulti(const char* model_path,  const char* transform_path, bool verbose, int category);

  char const* getName() const override { return "MVAReaderDNNMulti"; }
  TTreeFunction* clone() const override { return new MVAReaderDNNMulti(model_path_.c_str(), 
                                           transform_path_.c_str(), verbose, category_ ); }

  std::string model_path_;
  std::string transform_path_;
  int category_;
  TGraph * dnn_transformation; 
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  // ~MVAReaderDNNMulti();
  
  DNNEvaluatorSavedModel* dnn_tensorflow;

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



  // FloatArrayReader* Jet_qgl{};

  // TTreeReaderArray<Double_t>* ptW{};

  // TTreeReaderArray<Double_t>* Zl1{};
  
  // TTreeReaderArray<Double_t>* R_AN{};
/*
- Dphijet1jet2
- R
- Zl1
- detajj
- eta1
- jeteta1
- jeteta2
- jetpt1
- jetpt2
- mjj
- mtw1
- phi1
- pt1
- ptW

*/
};


MVAReaderDNNMulti::MVAReaderDNNMulti(const char* model_path, const char* transform_path, bool verbose, int category):
    model_path_(model_path), 
    transform_path_(transform_path),
    verbose(verbose),
    category_(category)
{
    // std::cout << "PATH_model: " << model_path_.c_str();
    dnn_tensorflow = new DNNEvaluatorSavedModel(model_path_, verbose);

    // Load the TGRaph used to transform the DNN score
    // The TGraph is the cumulative distribution of the DNN on the signal
    TFile * tf_file = new TFile(transform_path_.c_str(), "READ");
    if(tf_file->IsZombie() == false){
      // read the appropriate tgrph depending on category value
      dnn_transformation = (TGraph*) tf_file->Get(Form("Cumulative_Class_%d", category_ == 0 ? 1 : category_));
      // std::cout << "file NON zombie!!" << std::endl;
    }
    // std::cout << "ERROR READING TRASFORMER FILE :" << transform_path_.c_str();
    tf_file->Close();
}



double
MVAReaderDNNMulti::evaluate(unsigned)
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

  // ++++++++++++++ DNN +++++++++++++++++
  std::vector<float> input{};

  input.push_back(Dphijet1jet2);

  input.push_back(R_AN);

  input.push_back(Zl1);

  input.push_back((float) *(detajj->Get()) );

  input.push_back((float) Lepton_eta->At(0));

  input.push_back((float) CleanJet_eta->At(0));

  input.push_back((float) CleanJet_eta->At(1));

  input.push_back((float) CleanJet_pt->At(0));

  input.push_back((float) CleanJet_pt->At(1));

  input.push_back((float) *(mjj->Get()) );

  input.push_back(mtw1);

  input.push_back((float) Lepton_phi->At(0));

  input.push_back((float) Lepton_pt->At(0));

  input.push_back(ptW); 

  
  vector<float> dnn_scores = dnn_tensorflow->analyze(input);

  // Trova la probabilità massima
  float max_prob = *std::max_element(dnn_scores.begin() + 1, dnn_scores.end()); // ignora p0

  // Conta quante classi hanno max_prob
  int n_max = std::count(dnn_scores.begin(), dnn_scores.end(), max_prob);

  // Trova l'indice della prima occorrenza
  int max_index = std::distance(dnn_scores.begin(), std::find(dnn_scores.begin(), dnn_scores.end(), max_prob));

  // Se c'è un solo massimo ed è la mia categoria, applico la trasformazione
  // in caso di pareggio tra due classi -> evento ambiguo, lo butto in -1
  if (n_max == 1 && max_index == category_) {
      return dnn_transformation->Eval(max_prob);
  } else {
      return -1.0;
  }

}

void
MVAReaderDNNMulti::bindTree_(multidraw::FunctionLibrary& _library)
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
}

#endif 
