from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc_sm = ["sm", "Wjets_HT_hardJets", "Wjets_HT_PUJets" , "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]

mc_bkg = [c for c in mc_sm if "sm" not in c]
mc_eft = [c for c in samples if any(substring in c for substring in ["lin", "quad", "mixed"])]
signals = [c for c in samples if "sm" in c and c not in mc_eft]
mc = mc_sm + mc_eft
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","mu_topcr","ele_topcr","ele_FakeCR","mu_FakeCR"]
regions = ["ele_SR","mu_SR", "ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr"]
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]
phase_spaces_tot_sr_top = [ c for c in regions if 'SR' in c or "topcr" in c]
wj_region = [ c for c in regions if 'HWJ' in c]


# # # # ######################
# # # # # Theory nuisance
# # # # #
# # # # # PS and UE
# # # # # #
# # # # #### USE this for producing shapes

nuisances['PS_ISR']  = {
                'name'  : 'CMS_PS_ISR',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft}
            }

nuisances['PS_FSR']  = {
                'name'  : 'CMS_PS_FSR',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {     
                    sample : ['PSWeight[3]','PSWeight[1]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft}
            }

# # # ##############
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']

for sample in mc_bkg :
        nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind'  : 'weight_envelope',
            # 'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { sample: variations }
        }


# # #### mettere per tutti i sample ma in SR, poi anche in CR per quelli che hanno una CR
# # ## valutare se le cose sono strane con drawnuisances e se sono piatti via di logN

for sample in mc_bkg :
    nuisances['pdf_weight_{}'.format(sample)] = {
        'name'  : 'pdf_weight_{}'.format(sample),
        'kind'  : 'weight_envelope',
        # 'kind'  : 'weight',
        'type'  : 'shape',
        'samples' :  { sample: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)]},
    }


# # # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # # And we don't observe any dependency of UE variations on njet

### TO BE  FIXED FOR COMBINATION
jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2','JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal','JESRelativeSample_2017']

for js in jes_systs:
    nuisances[js] = {
        'name': 'CMS_scale_'+js,
        'kind': 'suffix',
        'type': 'shape',
        'mapUp': js+'up',
        'mapDown': js+'do',
        'samples': dict((skey, ['1.', '1.']) for skey in mc ),
        'folderUp': mcDirectoryLat+'__JESup_suffix',
        'folderDown': mcDirectoryLat+'__JESdo_suffix'
    }

# # # # # ##### MET energy scale
nuisances['MET']  = {
                'name'  : 'CMS_scale_met_2017_UL',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp':   'METup',
                'mapDown': 'METdo', 
                'samples': dict((skey, ['1.','1.']) for skey in mc ),
                'folderUp' : mcDirectoryLat+'__METup_suffix',
                'folderDown' : mcDirectoryLat+'__METdo_suffix'
}
