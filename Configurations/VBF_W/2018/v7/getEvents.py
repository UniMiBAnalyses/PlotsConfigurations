import ROOT

def Integral2Jets(file):
    return file.GetBinContent(3)

def Integral4Jets(file):
    return file.GetBinContent(5)

def IntegralAllJets(file):
    sum = 0
    for bin in range(0,file.GetNbinsX()):
        sum = sum + file.GetBinContent(bin)   
    return sum

file = ROOT.TFile("/afs/cern.ch/user/a/abulla/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBF_W/2018/rootFile/plots_vbf_wNLO_2018.root")

regions = ['ele_FakeCR','ele_HWJ','ele_PUWJ','ele_SR','mu_FakeCR','mu_HWJ','mu_PUWJ','mu_SR','Z']
NLO_histo = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
HT_histo = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
NLO_integral2 = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
HT_integral2 = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
NLO_integralAll = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
HT_integralAll = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
NLO_integral4 = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}
HT_integral4 = {"mu":{"hardJets":{}, "PUJets":{}}, "ele":{"hardJets":{}, "PUJets":{}}, "Z":{"hardJets":{}, "PUJets":{}}}

# for region in regions:
#     NLO_histo["mu"] = 0
#     histo['_HT_'+region] = 0
#     integral['_HT_'+region] = 0
#     integral['_NLO_'+region] = 0

for region in regions: 
    if region.split("_")[0] == "ele":
        NLO_histo["ele"]["hardJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_NLO_hardJets".format(region))
        NLO_histo["ele"]["PUJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_NLO_PUJets".format(region))
        HT_histo["ele"]["hardJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_HT_hardJets".format(region))
        HT_histo["ele"]["PUJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_HT_PUJets".format(region))
    elif region.split("_")[0] == "mu":
        NLO_histo["mu"]["hardJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_NLO_hardJets".format(region))
        NLO_histo["mu"]["PUJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_NLO_PUJets".format(region))
        HT_histo["mu"]["hardJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_HT_hardJets".format(region))
        HT_histo["mu"]["PUJets"][region.split("_")[1]] = file.Get("{}/njet_30/histo_Wjets_HT_PUJets".format(region))
    # elif region.split("_")[0] == "Z":
    #     NLO_histo["Z"]["hardJets"][region.split("_")[0]] = file.Get("{}/njet_30/histo_Wjets_NLO_hardJets".format(region))
    #     NLO_histo["Z"]["PUJets"][region.split("_")[0]] = file.Get("{}/njet_30/histo_Wjets_NLO_PUJets".format(region))
    #     HT_histo["Z"]["hardJets"][region.split("_")[0]] = file.Get("{}/njet_30/histo_Wjets_HT_hardJets".format(region))
    #     HT_histo["Z"]["PUJets"][region.split("_")[0]] = file.Get("{}/njet_30/histo_Wjets_HT_PUJets".format(region))



for flavor in NLO_histo.keys():
    for sample in NLO_histo[flavor].keys():
        for region in NLO_histo[flavor][sample].keys():
            NLO_integral2[flavor][sample][region] = Integral2Jets(NLO_histo[flavor][sample][region])
            HT_integral2[flavor][sample][region] = Integral2Jets(HT_histo[flavor][sample][region])
            NLO_integralAll[flavor][sample][region] = IntegralAllJets(NLO_histo[flavor][sample][region])
            HT_integralAll[flavor][sample][region] = IntegralAllJets(HT_histo[flavor][sample][region])
            NLO_integral4[flavor][sample][region] = Integral4Jets(NLO_histo[flavor][sample][region])
            HT_integral4[flavor][sample][region] = Integral4Jets(HT_histo[flavor][sample][region])


print(HT_integral2)

# hard_NLO_Z_2 = Integral2Jets(histo["hardJets_NLO_Z"])
# hard_NLO_Z_all = IntegralAllJets(histo["hardJets_NLO_Z"])
matrix2 = {}
matrix4 = {}
matrixAll = {}
rows = []
cols = []

for flavor in NLO_integral2.keys():
    for sample in NLO_integral2[flavor].keys():
        for region in NLO_integral2[flavor][sample].keys():
            nameNLO = "NLO_"+flavor+"_"+sample+"_"+region
            nameHT = "HT_"+flavor+"_"+sample+"_"+region
            rows.append(nameNLO)
            cols.append(nameHT)

# print(matrix)
for row in rows:
    matrix2[row] = {}
    matrix4[row] = {}
    matrixAll[row] = {}
    for col in cols:
        value2 = 1
        value4 = 1
        valueAll = 1
        if row.split("_")[1:] == col.split("_")[1:]:
            value2 = NLO_integral2[row.split("_")[1]][row.split("_")[2]][row.split("_")[3]]/HT_integral2[row.split("_")[1]][row.split("_")[2]][row.split("_")[3]]
            value4 = NLO_integral4[row.split("_")[1]][row.split("_")[2]][row.split("_")[3]]/HT_integral4[row.split("_")[1]][row.split("_")[2]][row.split("_")[3]]
            valueAll = NLO_integralAll[row.split("_")[1]][row.split("_")[2]][row.split("_")[3]]/HT_integralAll[row.split("_")[1]][row.split("_")[2]][row.split("_")[3]]
        matrix2[row][col] = value2
        matrix4[row][col] = value4
        matrixAll[row][col] = valueAll

import matplotlib.pyplot as plt
import numpy as np

# print(matrix)

# Crea una matrice casuale di dimensioni 4x4
# matrix = np.random.rand(4, 4)

# # Visualizza la matrice come un grafico con colori
# plt.imshow(matrix, cmap='coolwarm', interpolation='nearest')
# plt.colorbar()

# # Salva il grafico in un file PDF
# plt.savefig('my_plot.pdf')

import pandas as pd
df2 = pd.DataFrame(matrix2)
matrix2 = df2.values
df4 = pd.DataFrame(matrix4)
matrix4 = df4.values
dfAll = pd.DataFrame(matrixAll)
matrixAll = dfAll.values


# creare un grafico della matrice di colore con gli headers del dataframe
fig, ax = plt.subplots(figsize=(15, 12))
im = ax.imshow(matrix2, cmap='YlGn')

# impostare i ticks dell'asse x e y
ax.set_xticks(np.arange(len(df2.columns)))
ax.set_yticks(np.arange(len(df2.index)))

# impostare le labels dell'asse x e y con gli headers del dataframe
ax.set_xticklabels(df2.columns)
ax.set_yticklabels(df2.index)

# ruotare gli headers dell'asse x di 45 gradi
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# aggiungere la barra dei colori
cbar = ax.figure.colorbar(im, ax=ax)

# aggiungere un titolo
ax.set_title("NLO / HT region for region Integral = 2 jets")

# salva il plot in un file PDF
plt.savefig('plots/grafico2_OK.pdf')



# creare un grafico della matrice di colore con gli headers del dataframe
fig, ax = plt.subplots(figsize=(15, 12))
im = ax.imshow(matrix4, cmap='YlGn')

# impostare i ticks dell'asse x e y
ax.set_xticks(np.arange(len(df4.columns)))
ax.set_yticks(np.arange(len(df4.index)))

# impostare le labels dell'asse x e y con gli headers del dataframe
ax.set_xticklabels(df4.columns)
ax.set_yticklabels(df4.index)

# ruotare gli headers dell'asse x di 45 gradi
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# aggiungere la barra dei colori
cbar = ax.figure.colorbar(im, ax=ax)

# aggiungere un titolo
ax.set_title("NLO / HT region for region Integral = 4 jets")

# salva il plot in un file PDF
plt.savefig('plots/grafico4_OK.pdf')


# creare un grafico della matrice di colore con gli headers del dataframe
fig, ax = plt.subplots(figsize=(15, 12))
im = ax.imshow(matrixAll, cmap='YlGn')

# impostare i ticks dell'asse x e y
ax.set_xticks(np.arange(len(dfAll.columns)))
ax.set_yticks(np.arange(len(dfAll.index)))

# impostare le labels dell'asse x e y con gli headers del dataframe
ax.set_xticklabels(dfAll.columns)
ax.set_yticklabels(dfAll.index)

# ruotare gli headers dell'asse x di 45 gradi
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# aggiungere la barra dei colori
cbar = ax.figure.colorbar(im, ax=ax)

# aggiungere un titolo
ax.set_title("NLO / HT region for region Integral >= 2 jets")

# salva il plot in un file PDF
plt.savefig('plots/graficoAll_OK.pdf')