import ROOT as R
import sys

R.gROOT.SetBatch(R.kFALSE)

f = R.TFile(sys.argv[1], "UPDATE")
#sample_name = sys.argv[2]

samples = ['VBS','VBS_dipoleRecoil','top','DATA','Fake','VVV','VV','VgS','Vg','DY','VBF-V', 'ggWW']

VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]

samples += VBS_samples + VV_samples
for ir in range(1,22):
    samples.append("Wjets_res_"+str(ir))
for ir in range(1,8):
    samples.append("Wjets_boost_"+str(ir))

if len(sys.argv)>2:
    samples = sys.argv[2:]

# for now only EFT

samples = ['quad_cHQ1', 'sm_lin_quad_mixed_cW_cHB', 'lin_quad_cHW', 'sm_lin_quad_mixed_cW_cHW', 'quad_cHbox', 'lin_quad_cHB', 'sm_lin_quad_mixed_cHbox_cHB', 'sm_lin_quad_mixed_cHWB_cHQ1', 'sm_lin_quad_mixed_cHW_cHQ1', 'sm_lin_quad_cHl1', 'quad_cHl1', 'lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cW_cHW', 'lin_quad_cW', 'lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cW_cHj1', 'lin_quad_cHWB', 'sm_lin_quad_mixed_cHbox_cHj1', 'lin_cHWB', 'sm_lin_quad_cHWB', 'lin_cHl1', 'sm_lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cHW_cHl1', 'lin_quad_mixed_cW_cHj1', 'sm_lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cHl1_cHB', 'lin_quad_mixed_cW_cHbox', 'sm_lin_quad_mixed_cW_cHWB', 'lin_cHB', 'sm_lin_quad_cW', 'lin_quad_mixed_cHWB_cHQ1', 'quad_cHj1', 'lin_quad_mixed_cHbox_cHj1', 'lin_cHW', 'lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cW_cHbox', 'lin_quad_mixed_cHWB_cHW', 'quad_cHB', 'lin_quad_mixed_cHbox_cHl1', 'quad_cHW', 'lin_cHj1', 'sm_lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cHbox_cHQ1', 'sm_lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cW_cHQ1', 'sm_lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cHW_cHB', 'sm_lin_quad_mixed_cHWB_cHW', 'lin_quad_mixed_cW_cHB', 'lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cW_cHWB', 'lin_quad_cHl1', 'sm_lin_quad_cHQ1', 'sm_lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cHWB_cHj1', 'lin_quad_mixed_cHW_cHB', 'lin_quad_mixed_cHbox_cHQ1', 'quad_cW', 'sm_lin_quad_mixed_cHl1_cHQ1', 'lin_quad_cHbox', 'sm_lin_quad_cHW', 'sm_lin_quad_cHbox', 'sm_lin_quad_cHB', 'lin_quad_mixed_cHWB_cHj1', 'lin_cHQ1', 'sm_lin_quad_mixed_cHl1_cHB', 'sm_lin_quad_mixed_cHbox_cHW', 'lin_quad_mixed_cW_cHQ1', 'lin_quad_cHQ1', 'sm_lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHl1_cHQ1', 'sm_lin_quad_cHj1', 'quad_cHWB', 'sm_lin_quad_mixed_cHW_cHl1', 'sm_lin_quad_mixed_cHWB_cHl1', 'lin_quad_cHj1', 'sm_lin_quad_mixed_cHbox_cHl1', 'lin_cHbox', 'lin_quad_mixed_cHbox_cHB', 'lin_quad_mixed_cHWB_cHl1', 'lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHbox_cHW', 'sm_lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHW_cHQ1', 'lin_cW']

tot = len(samples)

for idx, sample_name in enumerate(samples):
    print(str(idx) + "/" + str(tot))
    for k in f.GetListOfKeys():
        # print("---> " + k.GetName())
        R.gDirectory.Cd(k.GetName())
        for z in R.gDirectory.GetListOfKeys():
            # print("---> " + z.GetName())
            R.gDirectory.Cd(z.GetName())
            for l in R.gDirectory.GetListOfKeys():
                if "histo_" + sample_name == l.GetName():
                    # print ("delete ", l.GetName())
                    R.gDirectory.Delete(l.GetName()+";*")
            R.gDirectory.Cd("../")

        R.gDirectory.Cd("../")

f.Write()
f.Close()
