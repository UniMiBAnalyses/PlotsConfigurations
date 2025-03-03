## dopo aver fatto le datacard, devo andare a predermi i path degli histos (per le regioni di controllo)
## in modo parallelo, devo fare il combine datacard e poi il relativo workspace. (eventualmente, potrei dover fittare)
##### fin qui possiamo stare in combine

## mi serve poi il mkPostFitCombinedPlot.py (qui bisogna andare in latinos)
## mkplot in una config fatta per i plot combinati

import argparse
import os
import subprocess
import concurrent.futures

def process_combined_card_for_region_and_variable(tag, region, variable, years):
    """ Funzione per gestire la combinazione della datacard e la creazione del workspace per una variabile e una regione. """
    do_combined_card(tag, region, variable, years)

def process_shapesWS_for_region_and_variable(tag, region, variable, years, fit):
    """ Funzione per gestire la combinazione della datacard e la creazione del workspace per una variabile e una regione. """
    do_shapes_from_WS(tag, region, variable, years, fit)

def MultiCoreCombineCards(args):
    """ Funzione per eseguire il processo in parallelo per variabili e regioni. """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for region in args.region:
            for variable in args.variabile:
                futures.append(executor.submit(process_shapesWS_for_region_and_variable, args.DatacardTag, region, variable, args.years, args.fit))
        
        # Wait for all futures to complete
        concurrent.futures.wait(futures)


def MultiCoreFromWSToShapes(args):
    """ Funzione per eseguire il processo in parallelo per variabili e regioni. """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for region in args.region:
            for variable in args.variabile:
                futures.append(executor.submit(process_combined_card_for_region_and_variable, args.DatacardTag, region, variable, args.years))
        
        # Wait for all futures to complete
        concurrent.futures.wait(futures)


def do_shapes_from_WS(tag, region, var, years, fit):

    ### redo something to get names!
    if isinstance(tag, list) and len(tag) > 1:
        # Se ci sono più di un tag, utilizziamo il primo tag nella lista
        tagName = tag[0]
    else:
        # Se c'è solo un tag, crea una lista di tag[0] lunga quanto gli anni
        tag = [tag[0]] * len(years)
        tagName = tag[0]

    yearName = "FullRunII" if all(year in years for year in ["2016HIPM", "2016noHIPM", "2017", "2018"]) else "_".join([i for i in years])
    combined_txt = f"combined{tagName}{region}{var}_{yearName}.txt"
    combined_root = f"combined{tagName}{region}{var}_{yearName}.root"
    combined_out = f"Shape{tagName}{region}{var}_{yearName}.root"

    command = "PostFitShapesFromWorkspace \\\n"
    command += f"-w {combined_root}\\\n"
    command += f"-d {combined_txt}\\\n"
    command += f"-o {combined_out}\\\n"

    if fit:
        command += "--postfit --sampling -f fitDiagnosticsCombined/fitDiagnostics.root:fit_s \\\n"
    command += "--total-shapes"

    print("Eseguendo il comando:")
    print(command)  # Debug

    try:
        # Esegui il comando
        result = subprocess.run(command, shell=True, check=True)
        print(f"WS --> Shapes Riuscita")

    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione di un comando: {e}")
        print("Terminazione del processo.")


def do_combined_card(tag, region, var, years):
    """ Combina le datacard e crea il workspace, gestendo gli errori. """

    if isinstance(tag, list) and len(tag) > 1:
        # Se ci sono più di un tag, utilizziamo il primo tag nella lista
        tagName = tag[0]
    else:
        # Se c'è solo un tag, crea una lista di tag[0] lunga quanto gli anni
        tag = [tag[0]] * len(years)
        tagName = tag[0]
        
    
    yearName = "FullRunII" if all(year in years for year in ["2016HIPM", "2016noHIPM", "2017", "2018"]) else "_".join([i for i in years])
    combined_txt = f"combined{tagName}{region}{var}_{yearName}.txt"
    combined_root = f"combined{tagName}{region}{var}_{yearName}.root"

    # Costruzione del comando di combinazione delle datacard
    command = "combineCards.py \\\n"
    
    for i, (t, y) in enumerate(zip(tag, years)):
        if "HIPM" in y:
            if "no" in y:
                t = "noHIPM"+t
                y = "2016"
            else:
                t = "HIPM"+t
                y = "2016"
        
        command += f"    bin{i}=../../{y}/datacards/{t}/{region}/{var}/datacard.txt \\\n"
    
    command += f"    > {combined_txt}"

    print("Eseguendo il comando:")
    print(command)  # Debug

    try:
        # Esegui il comando
        result = subprocess.run(command, shell=True, check=True)
        print(f"Combinazione riuscita: {combined_txt}")

        # Se la combinazione ha successo, passa alla creazione del workspace
        command = f"text2workspace.py {combined_txt} -o {combined_root}"
        print("Eseguendo la conversione in workspace:")
        print(command)

        result = subprocess.run(command, shell=True, check=True)
        print(f"Workspace creato con successo: {combined_root}")

    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione di un comando: {e}")
        print("Terminazione del processo.")

    return True


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Script per gestire analisi fisica con vari parametri.")

    parser.add_argument("--DatacardTag", "-DT", type=str, nargs='+', required=True,
                        help="Tag per identificare la datacard. Se più di una, nello stesso ordine dei rispettivi anni")
    parser.add_argument("--variabile", "-var", type=str, nargs='+', required=True,
                        help="Nome della/e variabile/e da analizzare")
    parser.add_argument("--flavor", "-f", type=str, nargs='+', default=["ele", "mu"],
                        help="Flavor da considerare (default: ['ele', 'mu'])")
    parser.add_argument("--region", "-r", type=str, nargs='+', choices=["HWJ", "PUWJ", "topcr", "SR", "FakeCR"], 
                        default=["HWJ", "PUWJ", "topcr", "SR", "FakeCR"], 
                        help="Regione da analizzare (HWJ, PUWJ, topcr, SR, FakeCR). Può essere una o più regioni.")
    parser.add_argument("--notregion", "-nr", type=str, nargs='+', choices=["HWJ", "PUWJ", "topcr", "SR", "FakeCR"], 
                        default=["SR"],
                        help="Regione da escludere tra (HWJ, PUWJ, topcr, SR, FakeCR). Può essere una o più regioni.")
    parser.add_argument("--years", "-y", type=str, nargs='+', default=["2018", "2017", "2016HIPM", "2016noHIPM"],
                        help="Anni da considerare (default: ['2018', '2017', '2016HIPM', '2016noHIPM'])")
    parser.add_argument("--fit", "-fit", action="store_true", default = False, help="Se specificato, esegue il fit dopo aver combinato le datacard")

    args = parser.parse_args()

    print(f"DatacardTag: {args.DatacardTag}")
    print(f"Variabile: {args.variabile}")
    print(f"Flavor: {args.flavor}")
    print(f"Years: {args.years}")

    regions_of_interest = list(set(args.region) - set(args.notregion))
    regions = [f"{f}_{r}" for f in args.flavor for r in regions_of_interest if "topcr" not in r]
    regions = regions + [f"{r}" for r in regions_of_interest if "topcr" in r]

    args.region = regions

    print(f"Region: {args.region}")

    success = MultiCoreCombineCards(args)

    if success:
        if args.fit:
            print("not implemented yet!!") 

        MultiCoreFromWSToShapes(args, outTxt, outWs)


