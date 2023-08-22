# plot configuration



# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860


plot['SSWW_new']  = { #same name as in samples.py  
    'color': 400,    # kGreen+2
    'isSignal' : 0, # 0 -> background: all samples with this flag set to 0 are plotted stacked. 
                                # 1 -> is signal: this gets plotted both stacked and superimposed
                                # 2 -> is signal: this gets plotted only superimposed, not stacked. 
    'isData'   : 0, #0/1 with obvious meaning. It is not a duplicate of structure.py. This is used to handle blinding. See below.
    'isBlind' : 0 # if set to 1, all samples with isData = 1 are not shown.
}

plot['SSWW_madgraph']  = { #same name as in samples.py  
    'color': 1,    # kGreen+2
    'isSignal' : 0, # 0 -> background: all samples with this flag set to 0 are plotted stacked. 
                                # 1 -> is signal: this gets plotted both stacked and superimposed
                                # 2 -> is signal: this gets plotted only superimposed, not stacked. 
    'isData'   : 1, #0/1 with obvious meaning. It is not a duplicate of structure.py. This is used to handle blinding. See below.
    'isBlind' : 0 # if set to 1, all samples with isData = 1 are not shown.
}



# additional options
legend['lumi'] = 'L = 59.7/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
