# -*- coding: utf-8 -*-
from __future__ import print_function  # Compatibilità con Python 3 per 'print'
import ROOT
import numpy as np
import os
import re
import argparse

# Mappa: prefisso variabile → shape originale (nx, ny, nz)
shape_map = {
    "DNNJoined_Dphijj_DphilepMET1": (2, 3, 3),
    "DNNJoined_Dphijj_DphilepMET2": (3, 3, 3),
    "DNNJoined_Dphijj_DphilepMET3": (4, 3, 3),
    "DNNJoined_Dphijj_jet1pt": (3, 3, 3),
}

def match_shape_from_name(name):
    for prefix, shape in shape_map.items():
        if name.startswith(prefix):
            return shape
    return None

def remap_hist_1d_from_3d(h1D, nx, ny, nz):
    # Leggi l'array 1D da ROOT
    cont = np.array([h1D.GetBinContent(i) for i in range(1, h1D.GetNbinsX() + 1)])

    # Verifica che l'array 1D abbia la dimensione corretta
    if len(cont) != nx * ny * nz:
        raise ValueError("Il numero di bin 1D ({}) non corrisponde alla dimensione attesa ({}).".format(len(cont), nx * ny * nz))

    # Riforma l'array 1D in un array 3D (con le dimensioni nx, ny, nz)
    array3d = cont.reshape((nz, ny, nx))  # (nz, ny, nx)

    # Se vuoi invertire la trasposizione che hai fatto prima, esegui una trasposizione di nuovo
    array3d = array3d.transpose(2, 1, 0)  # (nx, ny, nz)

    # Ora array3d è il tuo array 3D, ma devi convertirlo di nuovo in un istogramma 1D
    new_cont = array3d.flatten()

    # Sovrascrivi nell'istogramma 1D
    for i, value in enumerate(new_cont, 1):
        h1D.SetBinContent(i, value)

    return h1D

def process_file(input_file, output_file):
    ROOT.TH1.AddDirectory(False)
    fin = ROOT.TFile.Open(input_file, "READ")
    fout = ROOT.TFile.Open(output_file, "RECREATE")

    def recurse_directory(src_dir, dest_dir, parent_region=""):
        for key in src_dir.GetListOfKeys():
            obj = key.ReadObj()

            if obj.InheritsFrom(ROOT.TDirectory.Class()):
                # Nome della cartella da concatenare con il nome della cartella padre
                new_region = parent_region + "/" + obj.GetName() if parent_region else obj.GetName()
                dest_dir.mkdir(obj.GetName())
                recurse_directory(obj, dest_dir.GetDirectory(obj.GetName()), new_region)  # Passa la cartella corrente

            elif obj.InheritsFrom(ROOT.TH1.Class()):
                h = obj.Clone()
                var_name = parent_region.split("/")[-1]
                cut_name = parent_region.split("/")[-2]
                shape = match_shape_from_name(var_name)
                if shape is not None:
                    nx, ny, nz = shape
                    expected_bins = nx * ny * nz
                    if h.GetNbinsX() == expected_bins:
                        remap_hist_1d_from_3d(h, nx, ny, nz)
                dest_dir.cd()
                h.Write()

    recurse_directory(fin, fout)

    fout.Close()
    fin.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", help="Input ROOT file")
    parser.add_argument("--output", dest="output", help="Output ROOT file")
    args = parser.parse_args()

    process_file(args.input, args.output)