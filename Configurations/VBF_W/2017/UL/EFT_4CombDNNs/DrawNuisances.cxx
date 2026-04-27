#include <vector>
#include <string>
#include <map>
#include <regex>

void DrawNuisances(std::string inputRootFile, std::string histoNominal, std::vector<std::string> histo_up_list, std::vector<std::string> histo_down_list, std::string outputDirPlots = "./", std::string drawYields = "0", std::string plotName = "default_plot") {
 
  gStyle->SetOptStat(0);
  gStyle->SetPadTopMargin(0.21);

  // Apri il file ROOT
  TFile* file = new TFile(inputRootFile.c_str(), "READ");

  // Ottieni l'istogramma nominale
  TH1F* hNominal = (TH1F*) file->Get(histoNominal.c_str());
  hNominal->SetTitle("");
  hNominal->SetLineColor(kBlue);
  hNominal->SetLineWidth(5);

  // Prepariamo una legenda
  TLegend* leg = new TLegend(0.1, 0.8, 0.9, 0.99);
  leg->SetFillColor(kWhite);
  leg->AddEntry(hNominal, histoNominal.c_str(), "l");

  // Color-blind friendly palette with ROOT color codes
  std::vector<int> colors = { kGreen+3, 800, 920, 616, kCyan, kYellow+2, kRed+1}; 
  int nColors = colors.size();

  // Massimo valore per il plot
  Float_t max = hNominal->GetMaximum();
  Float_t min = hNominal->GetMinimum();

  // Mappa di raggruppamenti
  std::map<std::string, std::vector<std::string>> nuisances_map = {
      {"JES", {"JESAbsolute", "JESBBEC1", "JESHF", "JESEC2", "JESFlavorQCD", "JESRelativeSample", "JESRelativeBal"}},
      {"btag", {"btag_jes", "btag_hf", "btag_lf", "btag_cferr", "btag_hfstats", "btag_lfstats"}},
      {"Theory", {"QCDscale", "pdf_weight", "PS_FSR", "PS_ISR"}},
      {"Reweight", {"rew", "singleTopToTTbar"}},
      {"Others", { // Nuisance non categorizzate
          "CMS_scale_e", 
          "CMS_eff_e",
          "CMS_scale_m", 
          "CMS_eff_m",
          "CMS_scale_met",
          "CMS_res_j",
          "CMS_eff_trigger",
          "CMS_jetpuid",
          "CMS_PU",
          "CMS_eff_prefiring"
      }}
  };

  // Mappe dinamiche per ogni gruppo
  std::map<std::string, TH1F*> combinedUp;
  std::map<std::string, TH1F*> combinedDown;

  std::set<size_t> nuisances_to_skip;

  // Itera sulle nuisance up e down
  for (size_t i = 0; i < histo_up_list.size(); ++i) {
    std::string nuisanceNameUp = histo_up_list[i];
    std::string nuisanceNameDown = histo_down_list[i];

    TH1F* hUp = (TH1F*) file->Get(nuisanceNameUp.c_str());
    TH1F* hDo = (TH1F*) file->Get(nuisanceNameDown.c_str());

    if (!hUp || !hDo) {
      std::cerr << "Error: Could not find histograms for nuisance " << nuisanceNameUp << " or " << nuisanceNameDown << std::endl;
      continue;
    }

    // Verifica a quale gruppo appartiene la nuisance
    bool nuisanceCombined = false;
    if (histo_up_list.size() > 1){
      for (const auto& entry : nuisances_map) {
        const std::string& group = entry.first;
        const std::vector<std::string>& groupKeywords = entry.second;

        bool isInGroup = false;
        for (const auto& keyword : groupKeywords) {
          if (nuisanceNameUp.find(keyword) != std::string::npos) {
            isInGroup = true;
            break;
          }
        }

        // Se la nuisance appartiene al gruppo, somma in quadratura
        if (isInGroup) {
          nuisanceCombined = true;
          cout << "Nuisance " << nuisanceNameUp << " is in group " << group << endl;
          nuisances_to_skip.insert(i); 

          // Inizializza l'istogramma combinato se non esiste
          if (combinedUp[group] == nullptr) {
            cout << "Creating combined histogram for group " << group << endl;
            combinedUp[group] = (TH1F*) hUp->Clone();
            combinedDown[group] = (TH1F*) hDo->Clone();
          } else {
            // Somma in quadratura per ogni bin
            for (int bin = 1; bin <= combinedUp[group]->GetNbinsX(); ++bin) {
              float previous_diff_up = combinedUp[group]->GetBinContent(bin) - hNominal->GetBinContent(bin);
              float previous_diff_do = hNominal->GetBinContent(bin) - combinedUp[group]->GetBinContent(bin);

              float diff_up = hUp->GetBinContent(bin) - hNominal->GetBinContent(bin);
              float diff_do = hNominal->GetBinContent(bin) - hDo->GetBinContent(bin);

              float valUp = sqrt(pow(previous_diff_up, 2) + pow(diff_up, 2));
              float valDown = sqrt(pow(previous_diff_do, 2) + pow(diff_do, 2));

              combinedUp[group]->SetBinContent(bin,  hNominal->GetBinContent(bin) + valUp);
              combinedDown[group]->SetBinContent(bin,  hNominal->GetBinContent(bin) - valDown);
              combinedUp[group]->SetBinError(bin, 0.0);
              combinedDown[group]->SetBinError(bin, 0.0);
            }
          }
        }
      }
    }

    // Se la nuisance è stata raggruppata, la escludiamo dal plot individuale
    if (!nuisanceCombined) {
      // Setta i colori e gli stili
      int colorIndex = i % nColors;
      hUp->SetLineColor(colors[colorIndex]);
      hUp->SetLineWidth(2);
      hUp->SetLineStyle(3);

      hDo->SetLineColor(colors[colorIndex]);
      hDo->SetLineWidth(2);
      hDo->SetLineStyle(2);

      // Aggiungi alla legenda
      leg->AddEntry(hUp, histo_up_list[i].c_str(), "l");
      leg->AddEntry(hDo, histo_down_list[i].c_str(), "l");
    }
  }

  // aggiusta il massimo e minimo se necessario sulle nuisance non raggruppate
  for (size_t i = 0; i < histo_up_list.size(); ++i) {
    // Salta quelle che sono state raggruppate
    if (nuisances_to_skip.find(i) != nuisances_to_skip.end()) continue;

    TH1F* hUp = (TH1F*) file->Get(histo_up_list[i].c_str());
    TH1F* hDo = (TH1F*) file->Get(histo_down_list[i].c_str());

    // Trova il massimo valore
    max = std::max(max, static_cast<Float_t>(hUp->GetMaximum()));
    min = std::min(min, static_cast<Float_t>(hDo->GetMinimum()));
  }

  for (const auto& entry : combinedUp) {
    const std::string& group = entry.first;
    TH1F* hGroupUp = entry.second;
    TH1F* hGroupDown = combinedDown[group];

    // Trova il massimo valore
    max = std::max(max, static_cast<Float_t>(hGroupUp->GetMaximum()));
    min = std::min(min, static_cast<Float_t>(hGroupDown->GetMinimum()));
  }


  // Crea il canvas completo con due pad
  TCanvas* ccFull = new TCanvas("ccFull", "", 800, 800);
  TPad* pad1 = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
  TPad* pad2 = new TPad("pad2", "pad2", 0, 0.0, 1, 0.3);

  pad1->SetTopMargin(0.08);
  pad1->SetBottomMargin(0.001);
  pad1->Draw();

  pad2->SetTopMargin(0.05);
  pad2->SetBottomMargin(0.35);
  pad2->Draw();

  // Disegna il plot principale nel primo pad
  pad1->cd();
  hNominal->GetYaxis()->SetRangeUser(min * 0.8, max * 1.2);
  hNominal->Draw("histo");

  // Disegna le nuisance non raggruppate
  for (size_t i = 0; i < histo_up_list.size(); ++i) {
    // Salta quelle che sono state raggruppate
    if (nuisances_to_skip.find(i) != nuisances_to_skip.end()) continue;

    TH1F* hUp = (TH1F*) file->Get(histo_up_list[i].c_str());
    TH1F* hDo = (TH1F*) file->Get(histo_down_list[i].c_str());
    hUp->Draw("histo same");
    hDo->Draw("histo same");
  }

  // Disegna le nuisance raggruppate
  int colorIndex = 0;
  for (const auto& entry : combinedUp) {
    const std::string& group = entry.first;
    TH1F* hGroupUp = entry.second;
    TH1F* hGroupDown = combinedDown[group];

    // Imposta i colori
    hGroupUp->SetLineColor(colors[colorIndex % nColors]);
    hGroupUp->SetLineStyle(2);
    hGroupUp->SetLineWidth(3);
    hGroupUp->Draw("histo same");

    hGroupDown->SetLineColor(colors[colorIndex % nColors]);
    hGroupDown->SetLineStyle(3);
    hGroupDown->SetLineWidth(3);
    hGroupDown->Draw("histo same");

    // Aggiungi alla legenda
    leg->AddEntry(hGroupUp, ("Total " + group + " Up").c_str(), "l");
    leg->AddEntry(hGroupDown, ("Total " + group + " Down").c_str(), "l");
    colorIndex++;
  }

  leg->Draw();
  gPad->SetGrid();

  // Disegna il ratio nel secondo pad
  pad2->cd();
  TH1F* hReferenceRatio = (TH1F*) hNominal->Clone("Reference");
  hReferenceRatio->SetMaximum(1.3);
  hReferenceRatio->SetMinimum(0.7);
  hReferenceRatio->SetLineColor(kBlue);
  hReferenceRatio->SetLineWidth(5);

  // Imposta il ratio a 1 e rimuovi l'errore dal nominale
  for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); ++iBin) {
    hReferenceRatio->SetBinContent(iBin+1, 1.0);
    hReferenceRatio->SetBinError(iBin+1, 0.0);
  }
  hReferenceRatio->Draw();

  // Disegna il ratio per le nuisance combinate
  colorIndex = 0;
  if (combinedUp.size() > 0) {
    for (const auto& entry : combinedUp) {
      const std::string& group = entry.first;
      TH1F* hRatioUp = (TH1F*) entry.second->Clone();
      TH1F* hRatioDown = (TH1F*) combinedDown[group]->Clone();

      // Calcola il ratio per ogni bin
      for (int iBin = 0; iBin < hNominal->GetNbinsX(); ++iBin) {
        float nominal = hNominal->GetBinContent(iBin+1);
        if (nominal != 0) {
          hRatioUp->SetBinContent(iBin+1, hRatioUp->GetBinContent(iBin+1) / nominal);
          hRatioUp->SetBinError(iBin+1, 0.0);
          hRatioDown->SetBinContent(iBin+1, hRatioDown->GetBinContent(iBin+1) / nominal);
          hRatioDown->SetBinError(iBin+1, 0.0);
        }
      }

      // Imposta i colori
      hRatioUp->SetLineColor(colors[colorIndex % nColors]);
      hRatioUp->SetLineStyle(2);
      hRatioUp->Draw("same");

      hRatioDown->SetLineColor(colors[colorIndex % nColors]);
      hRatioDown->SetLineStyle(3);
      hRatioDown->Draw("same");
      colorIndex++;
    }
  }

  // Disegna il ratio per le nuisance non combinate
  for (size_t i = 0; i < histo_up_list.size(); ++i) {
    if (nuisances_to_skip.find(i) != nuisances_to_skip.end()){
      continue;
    }

    TH1F* hRatioUp = (TH1F*) file->Get(histo_up_list[i].c_str())->Clone();
    TH1F* hRatioDown = (TH1F*) file->Get(histo_down_list[i].c_str())->Clone();

    // Calcola il ratio per ogni bin
    for (int iBin = 0; iBin < hNominal->GetNbinsX(); ++iBin) {
      float nominal = hNominal->GetBinContent(iBin+1);
      if (nominal != 0) {
        hRatioUp->SetBinContent(iBin+1, hRatioUp->GetBinContent(iBin+1) / nominal);
        hRatioUp->SetBinError(iBin+1, 0.0);
        hRatioDown->SetBinContent(iBin+1, hRatioDown->GetBinContent(iBin+1) / nominal);
        hRatioDown->SetBinError(iBin+1, 0.0);
      }
    }

    // Imposta i colori
    int colorIndex = i % nColors;
    hRatioUp->SetLineColor(colors[colorIndex]);
    hRatioUp->Draw("same");

    hRatioDown->SetLineColor(colors[colorIndex]);
    hRatioDown->SetLineStyle(2);
    hRatioDown->Draw("same");
  }

  gPad->SetGrid();

  // Salva i plot
  TString name;
  name = Form("%s/%s_Full.png", outputDirPlots.c_str(), plotName.c_str());
  ccFull->SaveAs(name.Data());
  name = Form("%s/%s_Full.pdf", outputDirPlots.c_str(), plotName.c_str());
  ccFull->SaveAs(name.Data());

  // Salva il plot in formato logaritmico
  hNominal->GetYaxis()->SetRangeUser(0.01, max * 10.);
  pad1->SetLogy();

  name = Form("%s/log_%s_Full.png", outputDirPlots.c_str(), plotName.c_str());
  ccFull->SaveAs(name.Data());
  name = Form("%s/log_%s_Full.pdf", outputDirPlots.c_str(), plotName.c_str());
  ccFull->SaveAs(name.Data());
}


