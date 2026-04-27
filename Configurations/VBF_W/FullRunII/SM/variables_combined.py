variables['DNN0p0Joined10'] = {
    'name': 'DNN0p0Joined10',
    'range': (10, 0.0000, 1.0000),
    'xaxis': 'DNN output',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['DNN0p3Joined10'] = {
    'name': 'DNN0p3Joined10',
    'range': (10, 0.3000, 1.0000),
    'xaxis': 'DNN output (score > 0.3)',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['DNN0p5Joined10'] = {
    'name': 'DNN0p5Joined10',
    'range': (10, 0.5000, 1.0000),
    'xaxis': 'DNN output',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['DNN0p5Joined20'] = {
    'name': 'DNN0p5Joined20',
    'range': (20, 0.5000, 1.0000),
    'xaxis': 'DNN output (score > 0.5)',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['DNN0p5Joined5'] = {
    'name': 'DNN0p5Joined5',
    'range': (5, 0.5000, 1.0000),
    'xaxis': 'DNN output',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['DNN0p8Joined10'] = {
    'name': 'DNN0p8Joined10',
    'range': (10, 0.8000, 1.0000),
    'xaxis': 'DNN output (score > 0.8)',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['R'] = {
    'name': 'R',
    'range': (25, 0.0000, 0.5000),
    'xaxis': 'R',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['RPU'] = {
    'name': 'RPU',
    'range': (20, 0.0000, 1.0000),
    'xaxis': 'R',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['Zl1bin3'] = {
    'name': 'Zl1bin3',
    'range': (40, -5.0000, 5.0000),
    'xaxis': 'Z_{l1}',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['Zl1bin4'] = {
    'name': 'Zl1bin4',
    'range': (20, -5.0000, 5.0000),
    'xaxis': 'Z_{l1}',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['detajj'] = {
    'name': 'detajj',
    'range': (40, 2.0000, 10.0000),
    'xaxis': '#Delta#eta_{jj}',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['events'] = {
    'name': 'events',
    'range': (1, 0.0000, 2.0000),
    'xaxis': 'Events',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['highDNN0p5events'] = {
    'name': 'highDNN0p5events',
    'range': (1, 0.5000, 1.0000),
    'xaxis': 'Events (DNN > 0.5)',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['jetpt1'] = {
    'name': 'jetpt1',
    'range': (70, 40.0000, 350.0000),
    'xaxis': 'p_{T}^{jet1} [GeV]',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['jetpt1PU'] = {
    'name': 'jetpt1PU',
    'range': (20, 40.0000, 350.0000),
    'xaxis': 'p_{T}^{jet1} [GeV]',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['leppt'] = {
    'name': 'leppt',
    'range': (35, 0.0000, 200.0000),
    'xaxis': 'p_{T}^{l} [GeV]',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['mjj'] = {
    'name': 'mjj',
    'range': (27, 300.0000, 3000.0000),
    'xaxis': 'm_{jj} [GeV]',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['mjj2'] = {
    'name': 'mjj2',
    'range': (27, 300.0000, 1000.0000),
    'xaxis': 'm_{jj} [GeV]',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}

variables['ptW'] = {
    'name': 'ptW',
    'range': (30, 0.0000, 300.0000),
    'xaxis': 'p_{T}^{W} [GeV]',
    'fold': 3,
    'blind':{
        'ele_SR' : 'significance=5',
        'mu_SR'  : 'significance=5',
    }
}