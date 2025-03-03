import uproot
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import os

def check_histogram(file_path, directory, hist_name):
    """
    Controlla un istogramma per valori negativi bin-by-bin.

    :param file_path: Percorso al file ROOT.
    :param directory: Cartella contenente l'istogramma.
    :param hist_name: Nome dell'istogramma.
    """
    try:
        # Apri il file e l'istogramma
        with uproot.open(file_path) as f:
            hist = f[f"{directory}/{hist_name}"]
            values = hist.values()
            edges = hist.axes[0].edges()

            # Cerca valori negativi nei bin
            for i, value in enumerate(values):
                if value < 0:
                    bin_center = (edges[i] + edges[i + 1]) / 2
                    print(f"Negative value found: Directory={directory}, Histogram={hist_name}, Bin={i}, Center={bin_center}, Value={value}")
    except Exception as e:
        print(f"Error processing {hist_name} in {directory}: {e}")

def process_directory(file_path, directory):
    """
    Elabora tutti gli istogrammi in una directory.

    :param file_path: Percorso al file ROOT.
    :param directory: Cartella contenente gli istogrammi.
    """
    try:
        with uproot.open(file_path) as f:
            # l = [f.keys()]
            # hist_names = [i for i in l if directory in i]

            # Ottieni tutti gli oggetti nella directory
            hist_names = [key for key in f[directory].keys() if f[f"{directory}/{key}"]]
            hist_names = [key for key in hist_names if not key.endswith("Var")]
            # print(hist_names)

            
            # Esegui il controllo su ogni istogramma
            with ThreadPoolExecutor() as executor:
                executor.map(lambda hist: check_histogram(file_path, directory, hist), hist_names)
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")

if __name__ == "__main__":
    import argparse

    # Parser degli argomenti
    parser = argparse.ArgumentParser(description="Check histograms for negative bin values in a ROOT file.")
    parser.add_argument("--file", help="Path to the ROOT file.")
    parser.add_argument("--directory", help="Directory inside the ROOT file to check.")
    args = parser.parse_args()

    # Controlla la directory
    if os.path.exists(args.file):
        process_directory(args.file, args.directory)
    else:
        print(f"File not found: {args.file}")
