import ROOT

# Open the ROOT file
file = ROOT.TFile.Open("/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/rootFile/w_interference/plots_vbf_w_2018w_interference.root", "READ")

# samples = {}
# handle = open("samples.py")
# exec(handle)
# handle.close()


# cHWB = [c for c in samples if "quad_cHWB" in c or "lin_cHWB" in c]
# cHDD = [c for c in samples if "quad_cHDD" in c or "lin_cHDD" in c]
# mixed = [c for c in samples if "mixed_cHWB_cHDD" in c or "mixed_cHDD_cHWB" in c]
# due = [c for c in cHWB + cHDD + mixed if "sm_lin_quad" not in c and "til" not in c]


# Get the directory containing the histograms
toPlot = []
# histo = file.Get("ele_SR_highDNN/Dphijet1jet2PU/histo_mixed_cHDD_cHWB")
# toPlot.append(histo)
histo = file.Get("ele_SR/DNNoutput_ALLbin4/histo_WLNuJJ_inter")
toPlot.append(histo)
histo = file.Get("ele_SR/DNNoutput_ALLbin4/histo_WLNuJJ")
toPlot.append(histo)

# # Loop over all the objects in the directory
# for key in directory.GetListOfKeys():
#     obj = key.ReadObj()
    
#     # Check if the object is a histogram
#     if isinstance(obj, ROOT.TH1):
#         # Do something with the histogram
#         ## look for histos with op in the name and plot them
#         if obj.GetName() in due:
#             toPlot.append(obj)

canvas = ROOT.TCanvas("canvas", "canvas", 800, 600) 
histo = toPlot[0]
histo.SetLineColor(1)
histo.SetLineWidth(2)
histo.SetStats(False)
histo.Scale(1. / histo.Integral()) 
histo.Draw("hist e")

histo2 = toPlot[1]
histo2.SetLineColor(2)
histo2.SetLineWidth(2)
histo2.SetStats(False)
histo2.Scale(1. / histo2.Integral()) 
histo2.Draw("hist e same")

# for i, histo in enumerate(toPlot):
#     histo.SetLineColor(i+1)
#     histo.SetLineWidth(2)
#     if i == 0:
#         histo.Draw("hist e")
#     else:
#         histo.Draw("same")

# Crea una legenda e aggiungi le voci per gli istogrammi
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)  # Coordinate per la posizione della legenda nel canvas
legend.AddEntry(histo2, "Signal", "l")  # Aggiungi una voce per histo1 con etichetta "Histogram 1"
legend.AddEntry(histo, "Interference", "l")  # Aggiungi una voce per histo2 con etichetta "Histogram 2"

legend.Draw()  # Disegna la legenda sul canvas

canvas.logy = True
canvas.SaveAs("/eos/user/a/abulla/www/public/VBF_W/EFT/shapes/histos_test_ele.png")


