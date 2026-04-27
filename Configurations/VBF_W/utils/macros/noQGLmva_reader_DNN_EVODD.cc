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

#ifndef MVAREADERDNNNOQGLEVODD
#define MVAREADERDNNNOQGLEVODD

typedef TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReaderDNNnoQGLEvOdd : public multidraw::TTreeFunction {
public:
  
  MVAReaderDNNnoQGLEvOdd(const char* model_path_ev,  const char* transform_path_ev, const char* model_path_odd,  const char* transform_path_odd, bool verbose);

  char const* getName() const override { return "MVAReaderDNNnoQGLEvOdd"; }
  TTreeFunction* clone() const override { return new MVAReaderDNNnoQGLEvOdd(model_path_ev_.c_str(), transform_path_ev_.c_str(), model_path_odd_.c_str(), transform_path_odd_.c_str(), verbose); }

  std::string model_path_ev_;
  std::string transform_path_ev_;
  std::string model_path_odd_;
  std::string transform_path_odd_;

  TGraph * dnn_transformation_ev; 
  TGraph * dnn_transformation_odd; 
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  ~MVAReaderDNNnoQGLEvOdd();
  
  DNNEvaluatorSavedModel* dnn_tensorflow_odd;
  DNNEvaluatorSavedModel* dnn_tensorflow_ev;

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


MVAReaderDNNnoQGLEvOdd::MVAReaderDNNnoQGLEvOdd(const char* model_path_ev, const char* transform_path_ev, const char* model_path_odd, const char* transform_path_odd, bool verbose):
    model_path_ev_(model_path_ev), 
    transform_path_ev_(transform_path_ev),
    model_path_odd_(model_path_odd), 
    transform_path_odd_(transform_path_odd),
    verbose(verbose)
{
    if (verbose) {
      std::cout << "Loading model: " << model_path_ev << std::endl;
      std::cout << "Loading model: " << model_path_odd << std::endl;
    }
    dnn_tensorflow_ev = new DNNEvaluatorSavedModel(model_path_ev, verbose);
    dnn_tensorflow_odd = new DNNEvaluatorSavedModel(model_path_odd, verbose);

    // Load the TGRaph used to transform the DNN score
    // The TGraph is the cumulative distribution of the DNN on the signal
    if (verbose) {
      std::cout << "Loading transformation: " << transform_path_ev << std::endl;
      std::cout << "Loading transformation: " << transform_path_odd << std::endl;
    }
    TFile * tf_file_ev = new TFile(transform_path_ev_.c_str(), "READ");
    TFile * tf_file_odd = new TFile(transform_path_odd_.c_str(), "READ");

    if(tf_file_ev->IsZombie() == false){
      dnn_transformation_ev = (TGraph*) tf_file_ev->Get("cumulative_signal");
      if (verbose) {
        std::cout << "Transformation ev loaded" << std::endl;
      }
    }
    if(tf_file_odd->IsZombie() == false){
      dnn_transformation_odd = (TGraph*) tf_file_odd->Get("cumulative_signal");
      if (verbose) {
        std::cout << "Transformation odd loaded" << std::endl;
      }
    }
    // std::cout << "ERROR READING TRASFORMER FILE :" << transform_path_.c_str();
    tf_file_ev->Close();
    tf_file_odd->Close();

}



double
MVAReaderDNNnoQGLEvOdd::evaluate(unsigned)
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

  ULong64_t event_ = *event->Get();

  std::vector<float> input{};

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

  vector<float> dnn_scores;
  if (std::fmod(event_, 2) == 0){
    dnn_scores = dnn_tensorflow_odd->analyze(input);
    return dnn_transformation_odd->Eval(dnn_scores.at(0));
  }
  else{
    dnn_scores = dnn_tensorflow_ev->analyze(input);
    return dnn_transformation_ev->Eval(dnn_scores.at(0));
  }

}

void
MVAReaderDNNnoQGLEvOdd::bindTree_(multidraw::FunctionLibrary& _library)
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


MVAReaderDNNnoQGLEvOdd::~MVAReaderDNNnoQGLEvOdd() {
    delete dnn_transformation_ev;
    delete dnn_transformation_odd;
    delete dnn_tensorflow_ev;
    delete dnn_tensorflow_odd;
}

#endif 
