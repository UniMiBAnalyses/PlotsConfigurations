# -*- coding: utf-8 -*-

import ROOT
import argparse
import numpy as np
from array import array
import sys
import ast


class ParseBinsAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # Funzione per verificare se una variabile è una tupla (nbin, min, max)
        def is_tuple_of_three_elements(val):
            return (isinstance(val, tuple) and len(val) == 3 and 
                    isinstance(val[0], int) and 
                    isinstance(val[1], (int, float)) and 
                    isinstance(val[2], (int, float)))
        
        # Controlla se l'argomento contiene i due punti ":"
        if ':' in values:
            # Dividi l'argomento in base ai due punti
            parts = values.split(':')
            parsed_parts = []
            for part in parts:
                try:
                    # Prova a interpretare ogni parte come una lista o una tupla
                    parsed_part = ast.literal_eval(part)
                    if isinstance(parsed_part, list):
                        # Verifica che ogni elemento della lista sia un numero o una tupla
                        if all(isinstance(x, (int, float)) for x in parsed_part):
                            parsed_parts.append(parsed_part)
                        elif all(is_tuple_of_three_elements(x) for x in parsed_part):
                            parsed_parts.append(parsed_part)
                        else:
                            raise ValueError("Ogni elemento nella lista deve essere un numero o una tupla (nbin, min, max)")
                    elif is_tuple_of_three_elements(parsed_part):
                        # Se è una tupla (nbin, min, max), aggiungila alla lista
                        parsed_parts.append(parsed_part)
                    elif isinstance(parsed_part, (int, float)):
                        # Se è un numero, aggiungilo alla lista
                        parsed_parts.append(parsed_part)
                    else:
                        raise ValueError("L'argomento deve essere una lista, una tupla (nbin, min, max) o un numero")
                except (ValueError, SyntaxError):
                    raise ValueError("Ogni parte dell'argomento deve essere una lista, una tupla (nbin, min, max) o un numero")
            # Unisci le parti valide con ":"
            joined_values = ':'.join(map(str, parsed_parts))
            setattr(namespace, self.dest, joined_values)
        else:
            try:
                # Prova a interpretare l'argomento come una lista o una tupla
                parsed_value = ast.literal_eval(values)
                if isinstance(parsed_value, list):
                    # Se è una lista, convertila in una lista di numeri o tuple
                    if all(isinstance(x, (int, float)) for x in parsed_value):
                        setattr(namespace, self.dest, parsed_value)
                    elif all(is_tuple_of_three_elements(x) for x in parsed_value):
                        setattr(namespace, self.dest, parsed_value)
                    else:
                        raise ValueError("Ogni elemento nella lista deve essere un numero o una tupla (nbin, min, max)")
                elif is_tuple_of_three_elements(parsed_value):
                    # Se è una tupla (nbin, min, max), assegnala
                    setattr(namespace, self.dest, parsed_value)
                elif isinstance(parsed_value, (int, float)):
                    # Se è un numero, assegna il valore
                    setattr(namespace, self.dest, parsed_value)
                else:
                    raise ValueError("L'argomento deve essere una lista, una tupla (nbin, min, max) o un numero")
            except (ValueError, SyntaxError):
                raise ValueError("L'argomento deve essere una lista, una tupla (nbin, min, max) o un numero")


def get_matrix_from_histogram(hist):
    # Ottieni le dimensioni dell'istogramma
    nbinsx = hist.GetNbinsX()
    nbinsy = hist.GetNbinsY()
    
    # Crea una matrice NumPy
    matrix = np.zeros((nbinsx, nbinsy))
    
    # Riempie la matrice con i valori dell'istogramma
    for ix in range(1, nbinsx + 1):
        for iy in range(1, nbinsy + 1):
            matrix[ix - 1, iy - 1] = hist.GetBinContent(ix, iy)

    ## due to the binning, some columns/raw are empy --> remove them from the calculation of the condition number
    nonzero_rows = np.any(matrix != 0, axis=1)
    nonzero_cols = np.any(matrix != 0, axis=0)
    # Trova gli indici dei bordi non vuoti
    first_nonzero_row = np.argmax(nonzero_rows)
    last_nonzero_row = len(nonzero_rows) - 1 - np.argmax(nonzero_rows[::-1])
    first_nonzero_col = np.argmax(nonzero_cols)
    last_nonzero_col = len(nonzero_cols) - 1 - np.argmax(nonzero_cols[::-1])

    # Estrai la sottomatrice senza righe e colonne esterne vuote
    filtered_matrix = matrix[first_nonzero_row:last_nonzero_row+1, first_nonzero_col:last_nonzero_col+1]
        
    cond_number = np.linalg.cond(filtered_matrix)
    return cond_number


def parse_bins(binning, df, var):
    try:
        # Tenta di interpretare l'argomento come una struttura Python (lista, tupla, numero)
        parsed_part = ast.literal_eval(binning)
    except (ValueError, SyntaxError):
        # Se fallisce, utilizza l'argomento come una stringa
        parsed_part = binning
    
    if isinstance(parsed_part, list):
        # Se è una lista, convertila in array di bin
        parsed_part = np.around(parsed_part, decimals=2).tolist()
        bins = array('d', parsed_part)
        return bins
    
    elif isinstance(parsed_part, int):
        # Se è un intero, crea bin lineari
        min_val = min(df.AsNumpy(columns=[var])[var])
        max_val = max(df.AsNumpy(columns=[var])[var])
        parsed_part = list(np.linspace(min_val, max_val, parsed_part + 1))
        parsed_part = np.around(parsed_part, decimals=2).tolist()
        bins = array('d', parsed_part)
        return bins
    
    elif isinstance(parsed_part, str):
        # Se è una stringa, convertila in intero e crea bin lineari
        parsed_part = int(parsed_part)
        min_val = min(df.AsNumpy(columns=[var])[var])
        max_val = max(df.AsNumpy(columns=[var])[var])
        parsed_part = list(np.linspace(min_val, max_val, parsed_part + 1))
        parsed_part = np.around(parsed_part, decimals=2).tolist()
        bins = array('d', parsed_part)
        return bins
    
    elif isinstance(parsed_part, tuple) and len(parsed_part) == 3:
        nbin, min_val, max_val = parsed_part
        if not isinstance(nbin, int) or not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
            raise ValueError("Tuple should be in the format (nbin, min, max), where nbin is an int and min/max are numbers.")
        # Se è una tupla (nbin, min, max), crea bin lineari
        parsed_part = list(np.linspace(min_val, max_val, nbin + 1))
        parsed_part = np.around(parsed_part, decimals=2).tolist()
        bins = array('d', parsed_part)
        return bins

    else:
        print("Error in parsing bins, bins need to be int, list, tuple (nbin, min, max) or str representing these")
        sys.exit(1)
    

def rearrange_args(argstring):
    # Dividi la stringa sulle virgolette di due punti
    argstring_list = str(argstring).split(':')
    
    if len(argstring_list) > 2:
        # Mantieni la prima variabile in ordine e inverti il resto
        first_var = argstring_list[0]
        rest_vars_reversed = argstring_list[1:][::-1]
        # Combina il risultato
        rearranged_args = [first_var] + rest_vars_reversed
        return ':'.join(rearranged_args)
    else:
        print("No action needed")
        print("argstring: ", argstring)
        print(type(argstring))
        # Se ci sono 2 o meno variabili, restituisci la stringa originale
        return argstring


def plot_response_matrix(data, cut, RecoVar, GenVar, RecoBins, GenBins):
    df = data.Filter(cut)
    # print("doing oneee")

    # Creazione dell'istogramma
    histo = df.Histo2D(("hist", "{}".format(cut), len(RecoBins) - 1, RecoBins, len(GenBins) - 1, GenBins), RecoVar, GenVar)

    if histo.Integral() != 0:
        scale = 1.0 / histo.Integral()
        histo.Scale(scale)

    ##set axis labels
    histo.GetXaxis().SetTitle(RecoVar)
    histo.GetYaxis().SetTitle(GenVar)

    # Calcola il condition number
    condNumber = get_matrix_from_histogram(histo)
    print('Condition number della matrice: {}'.format(condNumber))

    return histo, condNumber

def rearrange_tuple(tup):
    # Verifica che la tupla sia di lunghezza pari
    if len(tup) % 2 != 0:
        raise ValueError("La tupla deve avere una lunghezza pari.")
    mid = len(tup) // 2
    first_half = tup[:mid]
    second_half = tup[mid:]
    result = []
    # Alterna gli elementi delle due tuple
    for item1, item2 in zip(first_half, second_half):
        result.append(item1)
        result.append(item2)
    # Converti la lista di ritorno in una tupla
    return tuple(result)


def compute_map(numeration, RecoBins, GenBins):
### (X1;X2;Y1;Y2) -> (X;Y)
### function works for (X1;Y1;X2;Y2) so i'm swapping the values
# # # GenBins:  [array('d', [501.01, 4335.95, 8170.89]), array('d', [501.01, 3057.64, 5614.26, 8170.89]), array('d', [501.01, 2418.48, 4335.95, 6253.42, 8170.89])]
# # # RecoBins:  [array('d', [552.38, 4282.05, 8011.72]), array('d', [552.38, 3038.83, 5525.27, 8011.72]), array('d', [552.38, 2417.22, 4282.05, 6146.88, 8011.72])]

    numeration = rearrange_tuple(numeration)

    print(numeration)
    if len(numeration) == 2:
        print("no action needed")
        return numeration
    elif len(numeration) >= 4:
        print("action needed")
        x = numeration[-2]
        y = numeration[-1]

    for i in range(len(numeration)):
        if i % 2 == 0 and i < len(numeration) - 2:
            x += numeration[i] * len(RecoBins[i+1])
        elif i % 2 == i and i < len(numeration) - 2:
            y += numeration[i] * len(GenBins[i])

    print("X: ", x)
    print("Y: ", y)
    return (x,y)

def generate_numerations(RecoBins, GenBins):
    """
    Genera tutte le numerazioni possibili in base alle dimensioni dei bin.
    
    Args:
    - RecoBins (list): Lista di array di bin per le variabili di reco, ignorando il primo elemento.
    - GenBins (list): Lista di array di bin per le variabili di gen, ignorando il primo elemento.
    
    Returns:
    - generator: Un generatore di tuple che rappresentano le numerazioni possibili.
    """
    # Ignora il primo elemento di RecoBins e GenBins
    RecoBins = RecoBins[1:]  # Ignora il primo elemento
    GenBins = GenBins[1:]  # Ignora il primo elemento

    # Crea una lista delle lunghezze degli array di bin, escludendo il primo elemento
    bin_lengths_reco = [len(bins) - 1 for bins in RecoBins]
    bin_lengths_gen = [len(bins) - 1 for bins in GenBins]
    
    # Crea una lista di range per ogni dimensione
    ranges = [range(length) for length in bin_lengths_reco + bin_lengths_gen]
    
    # Genera tutte le combinazioni possibili delle numerazioni
    return product(*ranges)

def merge_TH2(hist_dic, RecoBins, GenBins, output_name):

    xBins = 1
    yBins = 1
    for bin in RecoBins:
        xBins *= (len(bin) - 1)

    for bin in GenBins:
        yBins *= (len(bin) - 1)

    new_hist = ROOT.TH2F("combined_hist", "Respose Matrix", xBins, 0, xBins, yBins, 0, yBins)

    # Analizza gli istogrammi
    for numeration, data in histos.items():
        hist = data["hist"]
        offx, offy = compute_map(numeration,RecoBins, GenBins)
        # print("Numeration: ", numeration)
        print("Offset X: ", offx*hist.GetNbinsX())
        print("Offset Y: ", offy*hist.GetNbinsY())
        offx *= hist.GetNbinsX()
        offy *= hist.GetNbinsY()

        x_bins = hist.GetNbinsX()
        y_bins = hist.GetNbinsY()

        ## now just need to fill the histogram
        for x_bin in range(1, x_bins + 1):
            for y_bin in range(1, y_bins + 1):
                content = hist.GetBinContent(x_bin, y_bin)
                new_hist.SetBinContent(x_bin + offx, y_bin + offy, content)
                print("setted content: ", content)
                print("x_bin: ", x_bin + offx)
                print("y_bin: ", y_bin + offy)
    
    return new_hist

def normalize_histogram_yaxis(histogram):
    """
    Funzione per normalizzare un istogramma 2D lungo l'asse Y.
    La somma dei bin lungo l'asse X diventa 1 per ogni bin dell'asse Y.

    Parametri:
    -----------
    histogram : ROOT.TH2
        L'istogramma 2D da normalizzare.
    
    Restituisce:
    -----------
    ROOT.TH2
        L'istogramma normalizzato.
    """
    
    # Itera su tutti i bin lungo l'asse Y
    for ybin in range(1, histogram.GetNbinsY() + 1):
        # Calcola la somma per i bin lungo l'asse X per il bin corrente dell'asse Y
        sum_x = 0
        for xbin in range(1, histogram.GetNbinsX() + 1):
            sum_x += histogram.GetBinContent(xbin, ybin)
        
        # Se la somma è diversa da zero, normalizza i bin lungo l'asse X
        if sum_x > 0:
            for xbin in range(1, histogram.GetNbinsX() + 1):
                current_content = histogram.GetBinContent(xbin, ybin)
                histogram.SetBinContent(xbin, ybin, current_content / sum_x)

        histogram.GetYaxis().SetBinLabel(ybin, f"bin{ybin}")
    
    return histogram

parser = argparse.ArgumentParser(description='Genera una matrice di risposta e la visualizza.')

# Aggiungi gli argomenti
parser.add_argument('--inputFile', required=True, help='Percorso e nome del file di input')
parser.add_argument('--treeName', default='tree_WLNuJJ', help='Nome dell\'albero nel file ROOT')
parser.add_argument('--dirName', default='all_SR/dnn_inputs_all', help='Nome della directory nel file ROOT')
parser.add_argument('--GenVar', required=True, type=str, help='Nome della variabile di livello generatore da utilizzare. Se 2D, usa var1:var2')
parser.add_argument('--RecoVar', required=True, type=str, help='Nome della variabile di livello ricostruzione da utilizzare. Se 2D, usa var1:var2')
parser.add_argument('--GenBins', action=ParseBinsAction,  type = str, default="20",  help='Numero di bin per la variabile di livello generatore. Anche accettata "[0,10,20..]:[0,10,20..]" (var1bins:var2bins). Anche tupla (nBin,min,max). Default è 20(:20)' )
parser.add_argument('--RecoBins', action=ParseBinsAction, type = str, default="50", help='Numero di bin per la variabile di livello ricostruzione. Anche accettata "[0,10,20..]:[0,10,20..]" (var1bins:var2bins). Anche tupla (nBin,min,max). Default è 50(:50)')
parser.add_argument('--output', default='/eos/user/a/abulla/www/public/VBF_W/differential/2018/ResponseMatrix/ResponseMatrix', help='Nome dell\'output del plot')

# Parsing degli argomenti
args = parser.parse_args()

f = ROOT.TFile(args.inputFile)
tree = f.Get(args.dirName + "/" + args.treeName)
df = ROOT.RDataFrame(tree)

## eveything is set up as V1:V2:V3:....:Vn
## where V1 is the one "plotted" in the very inside, all the others are used to filter the data
## if we consider only V2:V3:...:Vn, thehisto inside the histos are filled starting from Vn and going to V2 
## which is not intuitive. So, we rearrange the arguments such that we handle V1:Vn:Vn-1:...:V2 and same for the bin
## so that the user just has to provide the variables in the order he wants to see them in the plot
args.GenVar = rearrange_args(args.GenVar)
args.RecoVar = rearrange_args(args.RecoVar)
args.GenBins = rearrange_args(str(args.GenBins))
args.RecoBins = rearrange_args(str(args.RecoBins))


## lets understand if the variables are 1D or nD. if dimensions are different, exit
## auto assign number of bins if not specified
dGenVar = len(args.GenVar.split(':'))
dRecoVar = len(args.RecoVar.split(':'))

dRecoBins = len(str(args.RecoBins).split(':'))
dGenBins = len(str(args.GenBins).split(':'))


if dGenVar != dRecoVar:
    print("GenVar and RecoVar need to have the same number of dimensions")
    sys.exit(1)


if dGenBins != dGenVar:
    if dGenBins == 1:
        genBins = str(":".join(["{}".format(args.GenBins)] * dGenVar))
    else:
        print("Please provide a choerent var1:var2 bin1:bin2 choice")
        sys.exit(1)
else:
    genBins = args.GenBins

if dRecoBins != dRecoVar:
    if dRecoBins == 1:
        recoBins = str(":".join(["{}".format(args.RecoBins)] * dRecoVar))
    else:
        print("Please provide a choerent var1:var2 bin1:bin2 choice")
        sys.exit(1)
else:
    recoBins = args.RecoBins

##parse the bins for the variables
GenBins = []
RecoBins = []
for genvar,genbins in zip(args.GenVar.split(':'), genBins.split(':')):
    GenBins.append(parse_bins(genbins, df, genvar))
for recovar,recobins in zip(args.RecoVar.split(':'), recoBins.split(':')):
    RecoBins.append(parse_bins(recobins, df, recovar))

print("GenBins type: ", type(GenBins))
print("RecoBins type: ", type(RecoBins))
print("GenBins: ", GenBins)
print("RecoBins: ", RecoBins)

# Esecuzione
from itertools import product
## filtro sulle variabili successive alla prima, e poi farò un loop in cui faccio th2 per ogni combinazione ma con gli assi x e y sempre le prime due variabili
FilterRecoVars = args.RecoVar.split(':')[1:]
FilterGenVars = args.GenVar.split(':')[1:]

FilterRecoBins_do = []
bins = RecoBins[1:]
for i in range(len(bins)):
    FilterRecoBins_do.append(bins[i][:-1])

FilterGenBins_do = []
bins = GenBins[1:]
for i in range(len(bins)):
    FilterGenBins_do.append(bins[i][:-1])

FilterRecoBins_up = []
bins = RecoBins[1:]
for i in range(len(bins)):
    FilterRecoBins_up.append(bins[i][1:])

FilterGenBins_up = []
bins = GenBins[1:]
for i in range(len(bins)):
    FilterGenBins_up.append(bins[i][1:])


# Genera tutte le combinazioni possibili dei binning
combinations_do = list(product(*FilterRecoBins_do, *FilterGenBins_do))
combinations_up = list(product(*FilterRecoBins_up, *FilterGenBins_up))
vars = FilterRecoVars + FilterGenVars


# breakpoint()
# Crea una numerazione per ogni combinazione possibile
# numerations = product(*[range(len(bins)) for bins in FilterRecoBins_do + FilterGenBins_do])
numerations_list = list(generate_numerations(RecoBins, GenBins))

Nnumeration = len(numerations_list)
Ncombup = len(combinations_up)
Ncombdo = len(combinations_do)

## in base al numero di variabili, avro istogrammi dentro a istogrammi.. 
if Nnumeration != Ncombup or Nnumeration != Ncombdo:
    print("Numerations and combinations are different")
    print("Dunno what to do")
    sys.exit(1)

histos = {}
# # Mostra le combinazioni
for num,(up,do) in zip(numerations_list,zip(combinations_up,combinations_do)):
    print("Doing one")
    cut_do = " && ".join([f"{vars[i]} >= {do[i]}" for i in range(len(do))])
    cut_up = " && ".join([f"{vars[i]} <= {up[i]}" for i in range(len(up))])
    cut = cut_do + " && " + cut_up
    print(cut)
    print(num)

    hist, condNum = plot_response_matrix(df, cut, args.RecoVar.split(':')[0], args.GenVar.split(':')[0], RecoBins[0], GenBins[0])
    histos[num] = {"hist": hist, "condNum": condNum}

## se sto usando una stessa variabile (i.e. mjj_gen:DNN vs mjj:DNN) fuori dalla diagonale per definizione
## gli isto sono vuoti --> li produco perche per la mappa devo farlo, ma non salvo il canvas
## lo faccio con getIntegral() == 0
for numeration, data in histos.items():
    hist = data["hist"]
    condNum = round(data["condNum"], 2)

    if hist.Integral() != 0:
        c = ROOT.TCanvas("c", "c", 800, 600)
        hist.SetStats(0)
        hist.Draw("colz")

        # # Aggiungi il condition number come testo sopra l'istogramma
        text = ROOT.TLatex()
        text.SetNDC(True)  # Usa coordinate normalizzate del canvas
        text.SetTextSize(0.04)
        text.SetTextAlign(11)  # Allineamento a sinistra
        text.DrawLatex(0.2, 0.9, "Condition Number: {}".format(condNum))

        c.SaveAs('{}_{}vs{}_{}.pdf'.format(args.output, args.GenVar.split(":")[0], args.RecoVar.split(":")[0], numeration))
        c.SaveAs('{}_{}vs{}_{}.png'.format(args.output, args.GenVar.split(":")[0], args.RecoVar.split(":")[0], numeration))

# breakpoint()

giant = merge_TH2(histos, RecoBins, GenBins, args.output)
giant = normalize_histogram_yaxis(giant)
c = ROOT.TCanvas("c", "c", 800, 600)
# c.SetLogz()
giant.SetStats(0)
## set axis labels
giant.GetXaxis().SetTitle(args.RecoVar.split(':')[1])
giant.GetYaxis().SetTitle(args.GenVar.split(':')[0])

giant.Draw("colz")
c.SaveAs('{}_{}vs{}_giant.pdf'.format(args.output, args.GenVar.split(":")[0], args.RecoVar.split(":")[0]))
c.SaveAs('{}_{}vs{}_giant.png'.format(args.output, args.GenVar.split(":")[0], args.RecoVar.split(":")[0]))
