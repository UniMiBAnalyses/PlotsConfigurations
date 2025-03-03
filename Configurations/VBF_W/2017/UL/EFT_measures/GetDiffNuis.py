# -*- coding: utf-8 -*-

import sys
# bypass ROOT argv parsing
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse
import pandas as pd
import json

def save_to_json(df, output_file):
    """
    Salva le informazioni del DataFrame in un file JSON nel formato richiesto.

    :param df: DataFrame contenente le colonne ['sample', 'variation', 'num', 'ratio'].
    :param output_file: Nome del file JSON da creare.
    """
    # Creazione del dizionario strutturato
    result = {}

    # Itera su ogni gruppo di sample e variation
    grouped = df.groupby(['sample', 'variation'])
    for (sample, variation), group in grouped:
        # Ordina i valori per 'num'
        sorted_ratios = group.sort_values(by='num')['ratio'].tolist()

        # Aggiungi al dizionario
        if sample not in result:
            result[sample] = {}
        result[sample][variation] = sorted_ratios

    # Salvataggio del dizionario come JSON
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)
        print(f"Dati salvati in {output_file}")

def iterate_histograms(file, directory=None, base_path="", histograms_info=[], samples=["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"]):
    """
    Itera su tutti gli istogrammi in un file ROOT, comprese le directory e sottodirectory.
    Salva i nomi degli istogrammi e le directory in un elenco per la conversione in un DataFrame.
    
    :param file: Oggetto TFile di ROOT.
    :param directory: Oggetto TDirectory corrente, None per partire dalla radice.
    :param base_path: Percorso corrente nella gerarchia delle directory.
    :param histograms_info: Lista per salvare le informazioni sugli istogrammi.
    :return: Lista con informazioni sugli istogrammi.
    """
    if directory is None:
        directory = file

    map = {
        # "pdf_weight": {'source': 'pdf_weight', 'dest': "PDFSF"},
        # "QCDscale": {'source': 'QCDscale', 'dest': "QCDFSF"},
        # "PS_FSR": {'source': 'PS_FSR', 'dest': "PSFSR"},
        # "PS_ISR": {'source': 'PS_ISR', 'dest': "PSISR"},
        "JESRelativeSample_2017":{'source': 'JESRelativeSample_2017', 'dest': "JESRelativeSample_2017"},
        "met":{'source': 'scale_met_2017_UL', 'dest': "scale_met_2017_UL"},
        "JESRelativeBal":{'source': 'JESRelativeBal', 'dest': "JESRelativeBal"},
    }
    

    # Itera su tutti gli oggetti nella directory corrente
    for key in directory.GetListOfKeys():
        obj = key.ReadObj()
        # Se l'oggetto è un istogramma, aggiungi le informazioni alla lista
        if isinstance(obj, ROOT.TH1):
            region = base_path.split("/")[0]
            var = base_path.split("/")[-1]
            sampleName = [sample for sample in samples if sample in obj.GetName()]
            variation = [
                v["dest"]
                for v in map.values()
                if v["source"] in obj.GetName()
            ]
            print(obj.GetName())
            print(variation)
            if len(variation) != 0:
                try:
                    num = int(obj.GetName().split("Var")[0].split("V")[-1])
                except ValueError:
                    if "PDFSF" in variation: continue
                    else:
                        if "Down" in obj.GetName():
                            num = -1
                        elif "Up" in obj.GetName():
                            num = 1
            else:
                num = 0
                

            if not variation:
                if any(obj.GetName().endswith(v) for v in samples):
                    variation = ["Nominal"]
                else:
                    continue

            if len(sampleName) > 1:
                print(f"WARNING: Multiple samples found in object name {obj.GetName()}")
            if len(variation) > 1:
                print(f"WARNING: Multiple variations found in object name {obj.GetName()}")

            histograms_info.append({"region": region, "variable": var, "sample": sampleName[0], "variation": variation[0], "histogram": obj.GetBinContent(1), "num": num})

        # Se l'oggetto è una directory, esplorala ricorsivamente
        elif isinstance(obj, ROOT.TDirectory):
            new_base_path = f"{base_path}/{obj.GetName()}" if base_path else obj.GetName()
            iterate_histograms(file, obj, new_base_path, histograms_info)

    return histograms_info

if __name__ == '__main__':
    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--file',  dest='FileName'     , help='Path to file with source histos')

    (opt, args) = parser.parse_args()

    # Validazione dell'opzione --file
    if opt.FileName is None:
        parser.error("Option --file is required")

    sourceFile = ROOT.TFile(opt.FileName,"r")

    histograms_info = iterate_histograms(sourceFile)
    df_histograms = pd.DataFrame(histograms_info)
    print(df_histograms)

    # Step 1: Raggruppa per `sample`, `variation`, e `num`, sommando i valori di `histogram`
    grouped = df_histograms.groupby(['sample', 'variation', 'num'], as_index=False)['histogram'].sum()

    # Step 2: Ottieni i valori nominali per ciascun `sample`
    nominal = grouped[grouped['variation'] == 'Nominal'].copy()
    nominal = nominal.rename(columns={'histogram': 'nominal_histogram'})[['sample', 'nominal_histogram']]

    # Step 3: Unisci i valori nominali al gruppo principale
    merged = pd.merge(grouped, nominal, on='sample', how='outer')

    # Step 4: Calcola il rapporto tra `histogram` e `nominal_histogram`
    merged['ratio'] = merged['histogram'] / merged['nominal_histogram']
    print(merged[merged["variation"]== "PSFSR"])

    # Assumiamo che `df_histograms` sia il tuo DataFrame
    merged_filtered = merged[merged['variation'] != 'Nominal']

    # Chiamata alla funzione per salvare i dati
    save_to_json(merged_filtered, 'sample_variations_TEST.json')


