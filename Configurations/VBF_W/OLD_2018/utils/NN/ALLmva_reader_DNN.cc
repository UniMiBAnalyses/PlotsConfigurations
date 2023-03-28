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

#ifndef MVAREADERDNN
#define MVAREADERDNN

typedef TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReaderDNN : public multidraw::TTreeFunction {
public:
  
  MVAReaderDNN(const char* model_path,  const char* transform_path, bool verbose, int category);

  char const* getName() const override { return "MVAReaderDNN"; }
  TTreeFunction* clone() const override { return new MVAReaderDNN(model_path_.c_str(), 
                                           transform_path_.c_str(), verbose, category_); }

  std::string model_path_;
  std::string transform_path_;
  int category_;
  TGraph * dnn_transformation; 
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  // ~MVAReaderDNN();
  
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

  FloatArrayReader* Jet_qgl{};

  // TTreeReaderArray<Double_t>* ptW{};

  // TTreeReaderArray<Double_t>* Zl1{};
  
  // TTreeReaderArray<Double_t>* R_AN{};
/*
- detajj
- jetpt1
- mjj
- ptW
- R
- pt1
- Zl1
- eta1
- QGL1
- QGL2
*/
};


MVAReaderDNN::MVAReaderDNN(const char* model_path, const char* transform_path, bool verbose, int category):
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
      dnn_transformation = (TGraph*) tf_file->Get("cumulative_signal");
      std::cout << "file NON zombie!!" << std::endl;
    }
    // std::cout << "PATH: " << transform_path_.c_str();
    tf_file->Close();
}



double
MVAReaderDNN::evaluate(unsigned)
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

  // ++++++++++++++ R from AN +++++++++++++++++
  double x_Wjj = (x_ptj1 + x_ptj2 + x_ptW);
  double y_Wjj = (y_ptj1 + y_ptj2 + y_ptW);
  double ptWjj = (std::sqrt((x_Wjj*x_Wjj) + (y_Wjj*y_Wjj)));
  float R_AN = (ptWjj / ((CleanJet_pt->At(0)) + (CleanJet_pt->At(1)) + ptW));

  // I do this in training, the NN is trained with QGL=-10 for these strange events, I need to do the same thing!
  float qgl1 = Jet_qgl->At(0);
  if(std::isnan(qgl1) == true){
    qgl1 = -10.;
  }

  float qgl2 = Jet_qgl->At(1);
  if(std::isnan(qgl2) == true){
    qgl2 = -10.;
  }

  std::vector<float> input{};

  input.push_back(qgl1);
  // std::cout << "qgl1 : " << qgl1 << std::endl;

  input.push_back(qgl2);
  // std::cout << "(float) Jet_qgl->At(1) "<< endl;
  // std::cout << "qgl2 : " << qgl2 << std::endl;

  input.push_back(R_AN);
  // std::cout << "(float) R_AN->At(0): "<< endl;
  // std::cout << "RAN : " << R_AN << std::endl;

  input.push_back(Zl1);
  // std::cout << "(float) Zl1->At(0) : " << endl;
  // std::cout << "Zl1 : " << Zl1 << std::endl;

  input.push_back((float) *(detajj->Get()) );
  // std::cout << "(float)* (detajj->Get()): "<< endl;

  input.push_back((float) Lepton_eta->At(0) );
  // std::cout << "(float) Lepton_eta->At(0): "<< endl;
  // std::cout << "eta1 : " << Lepton_eta->At(0) << std::endl;

  input.push_back((float) CleanJet_pt->At(0) );
  // std::cout << "(float) CleanJet_pt->At(0): "<< endl;
  // std::cout << "jetpt1 : " << CleanJet_pt->At(0) << std::endl;
  
  input.push_back((float) *(mjj->Get()) );
  // std::cout << "(float) *(mjj->Get()): "<< endl;

  input.push_back((float) Lepton_pt->At(0) );
  // std::cout << "(float) Lepton_pt->At(0): " << endl;

  input.push_back(ptW);
  // std::cout << "(float) ptW->At(0): "<< endl;
  
  // float x = 1.;
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);
  // input.push_back(x);

  
  vector<float> dnn_scores = dnn_tensorflow->analyze(input);
  return dnn_transformation->Eval(dnn_scores.at(0));
  // return dnn_scores.at(0);
}

void
MVAReaderDNN::bindTree_(multidraw::FunctionLibrary& _library)
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
  _library.bindBranch(Jet_qgl, "Jet_qgl");
}


// MVAReaderDNN::~MVAReaderDNN(){  
//   delete dnn_transformation;
//   // delete dnn_tensorflow;

//   detajj = nullptr;
//   CleanJet_pt = nullptr;
//   mjj = nullptr;
//   CleanJet_eta = nullptr;
//   CleanJet_phi = nullptr;
//   Lepton_pt = nullptr;
//   Lepton_eta = nullptr;
//   Lepton_phi = nullptr;
//   Jet_qgl = nullptr;
//   PuppiMET_phi = nullptr;
//   PuppiMET_pt = nullptr;

// }

#endif 
