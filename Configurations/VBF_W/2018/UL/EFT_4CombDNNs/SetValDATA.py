# -*- coding: utf-8 -*-
import ROOT

def modify_bins_in_rootfile(input_file, targets):
    # Apri il file in modalità UPDATE
    f = ROOT.TFile.Open(input_file, "UPDATE")
    
    if not f or f.IsZombie():
        # print(f"Cannot open file {input_file}")
        return

    for folder_name, (hist_name, bin_to_modify, new_content) in targets.items():
        print("Processing folder {}...".format(folder_name))

        folder = f.Get(folder_name)
        if not folder:
            # print(f"Warning: folder {folder_name} not found!")
            continue
        
        hist = folder.Get(hist_name)
        if not hist:
            # print(f"Warning: histogram {hist_name} not found in {folder_name}")
            continue

        # Modifica bin
        old_content = hist.GetBinContent(bin_to_modify)
        print("Old content of bin {}: {}".format(bin_to_modify,old_content))

        hist.SetBinContent(bin_to_modify, new_content)

        # Ricalcola errore come sqrt(contenuto)
        if new_content >= 0:
            new_error = new_content**0.5
            hist.SetBinError(bin_to_modify, new_error)
            print("Set new content {} and error {} in bin {}".format(new_content,new_error,bin_to_modify))
        else:
            print("Warning: new content is negative, error not set.")

        # Salva la modifica
        folder.Write("", ROOT.TObject.kOverwrite)

    # Scrive e chiude il file
    f.Close()


input_file = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/rootFile/EFT_4Comb_final_v1/test3.root"

targets = {
    "mu_SR/DNNJoined_Dphijj_jet1pt": ("histo_DATA", 19, 70.0),
    "ele_SR/DNNJoined_Dphijj_jet1pt": ("histo_DATA", 18, 350.0),
    # etc.
}

modify_bins_in_rootfile(input_file, targets)