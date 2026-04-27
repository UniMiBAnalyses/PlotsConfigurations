from pprint import pprint
import re
import json
# # # name of samples here must match keys in samples.py


madgraph = [c for c in samples if "MG" in c or "POWHEG" in c]
sherpa = [s for s in samples if "SHERPA" in s]


variations_madgraph   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']
variations_sherpa = [
    # 'Alt$(PSWeight[5],1.)',
    'Alt$(PSWeight[6],1.)',
    'Alt$(PSWeight[7],1.)',
    'Alt$(PSWeight[8],1.)',
    'Alt$(PSWeight[9],1.)',
    'Alt$(PSWeight[10],1.)'
]

# ########################### THEORY UNCERTAINTIES ###########################

# ########################## MADGRAPH SAMPLES ##########################
# for s in madgraph:
#     nuisances['QCDscale_{}'.format(s)] = {
#         'name'  : 'QCDscale_{}'.format(s),
#         'kind'  : 'weight_envelope',
#         'type'  : 'shape',
#         'samples': { k: variations_madgraph for k in madgraph if s in k },
#     }

#     nuisances['pdf_weight_{}'.format(s)] = {
#         'name'  : 'pdf_weight_{}'.format(s),
#         'kind'  : 'weight_square',
#         'type'  : 'shape',
#         'samples': {
#             k: [
#                 'Alt$(LHEPdfWeight[{}], 1.)'.format(i)
#                 for i in range(0, 103)
#             ]
#             for k in madgraph if s in k 
#         }
#     }

#     nuisances['PS_ISR_{}'.format(s)]  = {
#         'name'  : 'CMS_PS_ISR_{}'.format(s),
#         'kind'  : 'weight',
#         'type'  : 'shape',
#         'samples'  : { 
#              k: [
#                 "PSWeight[{}]".format(i)
#                 for i in [2,0]
#             ] for k in madgraph if s in k
#         }
#     }

#     nuisances['PS_FSR_{}'.format(s)]  = {
#         'name'  : 'CMS_PS_FSR_{}'.format(s),
#         'kind'  : 'weight',
#         'type'  : 'shape',
#         'samples'  : { 
#              k: [
#                 "PSWeight[{}]".format(i)
#                 for i in [3,1]
#             ] for k in madgraph if s in k
#         }
#     }
    

# ########################## SHERPA SAMPLES ##########################
# for s in sherpa:
#     nuisances['QCDscale_{}'.format(s)] = {
#         'name':  'QCDscale_{}'.format(s),
#         'kind':  'weight_envelope',
#         'type':  'shape',
#         'samples': {k: variations_sherpa for k in sherpa if s in k},
#     }

#     # --- PDF replicas ---
#     # pdf_weights = ['Alt$(PSWeight[{}],1.)'.format(i) for i in range(7, 108)]
#     pdf_weights = ['Alt$(PSWeight[{}],1.)'.format(i) for i in range(11, 111)]

#     nuisances['pdf_weight_{}'.format(s)] = {
#         'name':  'pdf_weight_{}'.format(s),
#         'kind':  'weight_square',
#         'type':  'shape',
#         'samples': {k: pdf_weights for k in sherpa if s in k},
#     }



for n in nuisances.values():
    n['skipCMS'] = 1
