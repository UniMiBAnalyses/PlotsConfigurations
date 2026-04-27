from pprint import pprint
import re
import json
from collections import defaultdict, OrderedDict
# # # name of samples here must match keys in samples.py 

mc_bkg =["Wjets_HT_hardJets","Wjets_HT_PUJets", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
signals = [c for c in samples if "WLNuJJ" in c or "sm" in c]
signals_correlated = list(set(re.sub(r'\d{1,2}$', '', c) for c in signals))

mc = signals + mc_bkg

regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","ele_topcr","mu_topcr","ele_FakeCR","mu_FakeCR"]

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]
phase_spaces_tot_sr_top = [ c for c in regions if 'SR' in c or "topcr" in c]
wj_region = [ c for c in regions if 'HWJ' in c]

bkg_to_norm = ['top', 'Wjets_HT_hardJets', 'Wjets_HT_PUJets']
# # # # # # # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

def merge_nuisances(nuisances):
    # Step 1: Raggruppa le keys per "name"
    name_to_keys = defaultdict(list)

    for key, nuis in nuisances.items():
        name = nuis.get('name')
        if name:
            name_to_keys[name].append(key)

    # Step 2: Per ogni gruppo di keys con lo stesso "name", fai il merge
    merged_nuisances = OrderedDict()

    # Mantieni l'ordine di apparizione di 'name' in nuisances
    seen_names = []
    for key, nuis in nuisances.items():
        name = nuis.get('name')
        if name and name not in seen_names:
            seen_names.append(name)

    for name in seen_names:
        keys = name_to_keys[name]

        # Usa la prima entry come base
        base_key = keys[0]
        base_nuis = dict(nuisances[base_key])  # copia

        # Mergia 'samples' e 'cuts' da tutte le altre entries
        merged_samples = dict(base_nuis.get('samples', {}))
        merged_cuts = list(base_nuis.get('cuts', []))  # se non esiste 'cuts', prende lista vuota

        for other_key in keys[1:]:
            other_nuis = nuisances[other_key]

            # Unisci samples
            for sample, val in other_nuis.get('samples', {}).items():
                merged_samples[sample] = val

            # Unisci cuts solo se esiste in questa nuisance
            if 'cuts' in other_nuis:
                merged_cuts.extend(other_nuis.get('cuts', []))

        # Rimuovi duplicati in cuts
        if merged_cuts:
            merged_cuts = sorted(set(merged_cuts))
            base_nuis['cuts'] = merged_cuts
        elif 'cuts' in base_nuis:
            del base_nuis['cuts']  # se alla fine non ci sono cuts, rimuovi

        # Aggiorna la nuisance unificata
        base_nuis['samples'] = merged_samples

        # Mantieni la chiave master (es: 'JESAbsolute') se esiste
        master_key = None
        for k in keys:
            if not ('_ele' in k or '_mu' in k):
                master_key = k
                break
        if not master_key:
            master_key = base_key  # fallback

        merged_nuisances[master_key] = base_nuis

    return merged_nuisances

# # # #### Luminosity

# for s in signals:
#     nuisances['PS_ISR_dipole_{}'.format(s)]  = {
#                     'name'  : 'CMS_PS_ISR_dipole',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {   s : ['PSWeight[2]','PSWeight[0]']}
#                 }

#     nuisances['PS_FSR_dipole_{}'.format(s)]  = {
#                     'name'  : 'CMS_PS_FSR_dipole',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {  s : ['PSWeight[3]','PSWeight[1]'] }
#                 }
#     ## add PS renomalized for signal, for the time being it is ok like this


#     ## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
#     variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']

#     # # # #Correlate all signal samples
#     nuisances['QCDscale_{}'.format(s)] = {
#         'name'  : 'QCDscale_{}'.format(s),
#         'kind'  : 'weight_envelope',
#         'type'  : 'shape',
#         'samples': { k: variations for k in signals if s in k },
#     }

#     #### mettere per tutti i sample ma in SR, poi anche in CR per quelli che hanno una CR
#     ## valutare se le cose sono strane con drawnuisances e se sono piatti via di logN

#     # ###### uncomment from here 4 datacards
    
#     nuisances['pdf_weight_{}'.format(s)] = {
#         'name'  : 'pdf_weight_{}'.format(s),
#         'kind'  : 'weight_square',
#         'type'  : 'shape',
#         'samples': { k : [ 'Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103) ] for k in signals if s in k },
#     }


#     # # # nuisances = {k:v for k,v in nuisances.items() if k in ['detavbs_residual', 'zlep_residual']} #if 'PS' in k or 'QCD' in k

#     # # # print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))