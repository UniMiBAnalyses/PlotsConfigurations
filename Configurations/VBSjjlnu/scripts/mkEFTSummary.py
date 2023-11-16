import ROOT
from glob import glob
from array import array
import json
from copy import deepcopy
import numpy as np
ROOT.gStyle.SetLineScalePS(1)

def read_ranges(path):
    d = {}
    f = open(path, "r")
    contents = f.readlines()
    current_op = ""
    for line in contents:
        # then its the op name
        if line.startswith("["): 
            op = line.split("\n")[0].split("[")[1].split("]")[0]
            if op not in d.keys(): d[op] = {"var":"", "1s":[], "2s":[]}
            current_op = op
        else:
            l = line.split("\t")
            best_var = l[0].strip(" ")
            one_s = l[1].strip(" ")
            os = [float(one_s.split(",")[0].split("[")[1]), float(one_s.split(",")[1].split("]")[0])]  
            two_s = l[2].split("\n")[0].strip(" ")
            ts = [float(two_s.split(",")[0].split("[")[1]), float(two_s.split(",")[1].split("]")[0])]
            
            d[current_op]["var"] = best_var
            d[current_op]["1s"] = os
            d[current_op]["2s"] = ts
            
    return d



def build_graph(d, shift=0, color=ROOT.kBlack, marker=8):
    
    os_upper = []
    os_lower = []
    
    ts_upper = []
    ts_lower = []
    
    # divide ops in first panel and second panel by hand
    ops_ordered = ['k_cW', 'k_cHW', 'k_cHB', 'k_cHWB','k_cHj1', 'k_cHbox', 'k_cHQ1', 'k_cHl1']

    first = ops_ordered[:4]
    second = ops_ordered[4:]
    
    for key in ops_ordered:
        os_upper.append(abs(d[key]["1s"][0]))
        os_lower.append(abs(d[key]["1s"][1]))
        ts_upper.append(abs(d[key]["2s"][0]))
        ts_lower.append(abs(d[key]["2s"][1]))
        
    xs = np.arange(-0.5 + shift, len(os_upper) + shift, 1)[:-1]
    # print(xs)
    # print(len(xs), len(os_upper))
    ys = np.zeros(len(os_upper))
    
    # print(os_lower, os_upper)
    
    g1 = ROOT.TGraph(len(d.keys()), array('d', xs), array('d', ys))
    g1.SetMarkerStyle(marker)
    g1.SetMarkerSize(2)
    g1.SetMarkerColor(color)
    
    os_lines = []
    ts_lines = []

    up_arrows = []
    down_arrows = []

    limits_first_panel = [-6,6]
    limits_second_panel = [-60,60]
    
    for idx, x in enumerate(xs):
        
        should_arrow_up = False
        should_arrow_down = False

        os_l = -os_lower[idx]
        os_h = os_upper[idx]
        ts_l = -ts_lower[idx]
        ts_h = ts_upper[idx]

        if idx <= 4:
            current_panel = limits_first_panel
            lower = -5.4
            higher = 5.4
        else:
            current_panel = limits_second_panel
            lower = -59
            higher = 59

        if -os_lower[idx] < current_panel[0]:
            should_arrow_down = True
            os_l = lower
            print("--> lower 1s: ", -os_lower[idx], os_l, lower)
        if os_upper[idx] > current_panel[1]: 
            should_arrow_up = True
            os_h = higher
        if -ts_lower[idx] < current_panel[0]:
            should_arrow_down = True
            ts_l = lower
        if ts_upper[idx] > current_panel[1]:
            should_arrow_up = True
            ts_h = higher
        
        # a = ROOT.TArrow(x1, y1, x2, y2, arrowsize=0.05)
        if should_arrow_down:
            if idx <= 4:
                ar = ROOT.TArrow(x, -5.5 , x, -5.85, 0.005, "|>")
            else:
                ar = ROOT.TArrow(x, -59, x, -59.8, 0.005, "|>")

            ar.SetLineColor(color)
            ar.SetFillColor(color)
            ar.SetLineWidth(5)
            down_arrows.append(ar)
                
        if should_arrow_up:
            if idx <= 4:
                #ar = ROOT.TArrow(x, 9.5, x, 9.9, 0.01,"|>")
                ar = ROOT.TArrow(x, 5.5 , x, 5.85, 0.005, "|>")
            else:
                #ar = ROOT.TArrow(x, 59.5, x, 59.9, 0.01, "|>")
                ar = ROOT.TArrow(x, limits_second_panel[1] , x, limits_second_panel[1] + 0.7, 0.005, "|>")

            ar.SetLineColor(color)
            ar.SetFillColor(color)
            ar.SetLineWidth(5)
            down_arrows.append(ar)
            up_arrows.append(ar)
            

        # l1 = ROOT.TLine(x1, y1, x2, y2)
        # print(ops_ordered[idx], os_lower[idx], os_upper[idx], ts_lower[idx], ts_upper[idx])
        print(ops_ordered[idx], os_l, os_h, ts_l, ts_h)
        los = ROOT.TLine(x, os_l, x, os_h)
        lts = ROOT.TLine(x, ts_l, x, ts_h)
        
        los.SetLineStyle(1)
        los.SetLineWidth(5)
        los.SetLineColor(color)
        
        lts.SetLineStyle(3)
        lts.SetLineWidth(5)
        lts.SetLineColor(color)
        
        os_lines.append(los)
        ts_lines.append(lts)

       
    print("-->Returning")
    print(up_arrows+down_arrows)
    return g1, os_lines, ts_lines, up_arrows+down_arrows


poi_to_label = {
   "k_cHB": "c_{HB} [TeV^{-2}]",
   "k_cHWB": "c_{HWB} [TeV^{-2}]",
   "k_cHl1": "c_{Hl}^{(1)} [TeV^{-2}]",
   "k_cW": "c_{W} [TeV^{-2}]",
   "k_cHW": "c_{HW} [TeV^{-2}]",
   "k_cHQ1": "c_{HQ}^{(1)} [TeV^{-2}]",
   "k_cHj1": "c_{Hj}^{(1)} [TeV^{-2}]",
   "k_cHbox": "c_{HBox} [TeV^{-2}]"
}

d = read_ranges("/eos/user/g/gboldrin/ranges_WV_EFT_Full_Run2/ranges_profiled.txt")
d_quad = read_ranges("/eos/user/g/gboldrin/ranges_WV_EFT_Full_Run2/ranges_quad.txt")
d_lin = read_ranges("/eos/user/g/gboldrin/ranges_WV_EFT_Full_Run2/ranges_lin.txt")

print("--> Profiled")
g, os, ts, arr = build_graph(d, shift = -0.15)
print("--> Quadratics")
g_q, os_q, ts_q, arr_q = build_graph(d_quad, shift = 0.0, color=ROOT.kAzure+1, marker=23)
print("--> Linear")
g_l, os_l, ts_l, arr_l = build_graph(d_lin, shift = +0.15, color=ROOT.kOrange-3, marker=21)

ops_ordered = ['k_cW', 'k_cHW', 'k_cHB', 'k_cHWB','k_cHj1', 'k_cHbox', 'k_cHQ1', 'k_cHl1']

limits_first_panel = [-6,6]
limits_second_panel = [-60,60]

c = ROOT.TCanvas("c", "c", 2000, 1000)

ROOT.gStyle.SetOptStat(0)

margins = 0.11
c.SetRightMargin(margins)
c.SetLeftMargin(margins)
c.SetBottomMargin(margins)
c.SetTopMargin(0.2)
c.SetFrameLineWidth(3)


pad2 = ROOT.TPad("pad3", "20",0.0, 0.0,0.6, 1.0)
pad3 = ROOT.TPad("pad1", "20",0.6, 0.0,1.0, 1.0)

pad3.SetLeftMargin(0.09)
pad3.SetTopMargin(0.18)
pad2.SetRightMargin(0.01)
pad2.SetTopMargin(0.18)

pad2.SetFrameLineWidth(4)
pad3.SetFrameLineWidth(4)


#pad1.Draw()
pad2.Draw()
pad3.Draw()

pad2.cd()


#frame2 = pad2.DrawFrame(-1, -10, 6, 10)

#frame2.GetXaxis().SetTickLength(0)
#frame2.GetXaxis().SetLabelSize(0)

h = ROOT.TH1F("labels", "labels",5, -1, 4)
for idx, i in enumerate(ops_ordered[:5]):
    h.GetXaxis().SetBinLabel(idx+1, poi_to_label[i])   

h.GetYaxis().SetTitle("Parameter value")
h.GetYaxis().SetTitleFont(43)
h.GetYaxis().SetTitleSize(50)
h.GetYaxis().SetTitleOffset(0.9)

l_ = ROOT.TLine(-1,0,4,0)
l_.SetLineColor(ROOT.kGray)
l_.SetLineWidth(3)

h.GetXaxis().SetLabelFont(43)
h.GetXaxis().SetLabelSize(30)
h.GetYaxis().SetLabelFont(43)
h.GetYaxis().SetLabelSize(40)

h.SetTitle("")
h.SetMaximum(limits_first_panel[1])
h.SetMinimum(limits_first_panel[0])
h.SetLineColor(0)
h.Draw()
l_.Draw("L same")
g.Draw("P")
g_q.Draw("P")
g_l.Draw("P")


for line in os + os_q + os_l: line.Draw("same")
for line in ts + ts_q + ts_l: line.Draw("same")

for a in arr + arr_l + arr_q: 
    print(a)
    a.Draw()

tex = ROOT.TLatex(-0.9, limits_first_panel[1] + .5, "CMS")
tex.SetTextFont(62)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()

tex1 = ROOT.TLatex(-0.2, limits_first_panel[1] + .5,"Preliminary")
tex1.SetTextFont(52)
tex1.SetTextSize(0.06)
tex1.SetLineWidth(2)
tex1.Draw()

tex3 = ROOT.TLatex(1.5, limits_first_panel[1] + .5, "#sqrt{s} = 13 TeV, 137 fb^{-1}, #Lambda = 1 TeV")
tex3.SetTextFont(52)
tex3.SetTextSize(0.04)
tex3.SetLineWidth(2)
tex3.Draw()


# now build the legend


leg = ROOT.TLegend(0.11, 0.83, 0.9, 0.99)
leg.SetBorderSize(0)
leg.SetNColumns(2)


l = ROOT.TLine(0, 0, 1, 1)
l.SetLineStyle(1)
l.SetLineWidth(4)
l.SetLineColor(ROOT.kBlack)

l2 = ROOT.TLine(0, 0, 1, 1)
l2.SetLineStyle(3)
l2.SetLineWidth(4)
l2.SetLineColor(ROOT.kBlack)

gf = g.Clone("gf")
gf_q = g_q.Clone("gf_q")
gf_l = g_l.Clone("gf_l")

gf.SetLineColor(ROOT.kBlack)
gf_q.SetLineColor(ROOT.kAzure+1)
gf_l.SetLineColor(ROOT.kOrange+2)

gf.SetLineWidth(3)
gf_q.SetLineWidth(3)
gf_l.SetLineWidth(3)

leg.AddEntry(l, "68% C.L.", "L")
leg.AddEntry(l2, "95% C.L.", "L")
leg.AddEntry(gf, "Profiled #Lambda^{-4}", "PL")
leg.AddEntry(gf_q, "Individual #Lambda^{-4}", "PL")
leg.AddEntry(gf_l, "Individual #Lambda^{-2}", "PL")


#leg.Draw()

pad2.SetTicks()

pad2.RedrawAxis()
pad2.SetGridx()

# Draw

c.Update()
c.Draw()

pad3.cd()


h2 = ROOT.TH1F("labels_2", "labels_2",3, 4, 7)
for idx, i in enumerate(ops_ordered[5:]):
    h2.GetXaxis().SetBinLabel(idx+1, poi_to_label[i])
    
l2_ = ROOT.TLine(4,0,7,0)
l2_.SetLineColor(ROOT.kGray)
l2_.SetLineWidth(3)

h2.GetXaxis().SetLabelFont(43)
h2.GetXaxis().SetLabelSize(30)
h2.GetYaxis().SetLabelFont(43)
h2.GetYaxis().SetLabelSize(40)
h2.SetTitle("")
h2.SetMaximum(limits_second_panel[1])
h2.SetMinimum(limits_second_panel[0])
h2.SetLineColor(0)

h2.Draw()
l2_.Draw("same")
g.Draw("P")
g_q.Draw("P")
g_l.Draw("P")
for line in os + os_q + os_l: line.Draw("same")
for line in ts + ts_q + ts_l: line.Draw("same")

leg.Draw()
    
pad3.SetTicks()

pad3.RedrawAxis()
pad3.SetGridx()

c.Update()
c.Draw()

c.Print("/eos/user/g/gboldrin/www/2018_2017_2016_EFT_FullOps_DNNcut_geq0p5_mWW_10_cHB_cW_cHW_cHWB_cHj1_cHbox_cHl1_cHQ1/summary/summary_WV_Run2.png")
c.Print("/eos/user/g/gboldrin/www/2018_2017_2016_EFT_FullOps_DNNcut_geq0p5_mWW_10_cHB_cW_cHW_cHWB_cHj1_cHbox_cHl1_cHQ1/summary/summary_WV_Run2.pdf")
