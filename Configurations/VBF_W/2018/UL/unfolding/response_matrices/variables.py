

##############################################
# now variables to plot
# Include also variables to be plotted

# variables['events']  = {'name': '1',      
#                         'range' : (1,0,2),  
#                         'xaxis' : 'events', 
#                         'fold' : 3,
#                         # 'blind': {
#                         #    'ele_SR' : 'full',
#                         #    'mu_SR' : 'full'
#                         #  }
#                         }


variables['mjj'] = {   'name': 'mjj',
                        'range' : ([ 200., 400., 600., 800., 1000., 1200., 1500., 2000., 3000.],), #variable range  
                        'xaxis' : 'M_{jj} [GeV]',
                        'fold' : 3,
                        # 'blind': {
                        #    'ele_SR' : 'full',
                        #    'mu_SR' : 'full'
                        # }
                      }


# # #### leptons (l, nu, l+nu)