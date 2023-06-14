import os
import argparse
import ROOT 
import numpy as np
import ast
from array import array
from copy import deepcopy
ROOT.gStyle.SetOptStat(0)

def generateCMSBox():
    tex = ROOT.TLatex(0.13,0.95,"CMS")
    tex.SetNDC()
    tex.SetTextFont(61)
    tex.SetTextSize(0.06)
    tex.SetLineWidth(2)
    tex.SetTextAlign(13)
    return tex

def generatePreliminaryBox():
    tex = ROOT.TLatex  (0.23, 0.95, "Preliminary")
    tex.SetNDC()
    tex.SetTextSize(0.06)
    tex.SetTextFont(52)
    tex.SetTextColor(ROOT.kBlack)
    tex.SetTextAlign(13)
    return tex

def generateLumiBox(lumi):
    tex = ROOT.TLatex(0.72,0.905, lumi)
    tex.SetNDC()
    tex.SetTextAlign(31)
    tex.SetTextFont(42)
    tex.SetTextSize(0.06)
    tex.SetLineWidth(2)
    return tex

def generateTeVBox():
    tex = ROOT.TLatex(0.882,0.907,"(13 TeV)")
    tex.SetNDC()
    tex.SetTextAlign(31)
    tex.SetTextFont(42)
    tex.SetTextSize(0.06)
    tex.SetLineWidth(2)
    return tex


def drawSummary(d, output, ylabel=False, legendlabel=False):
    
    x = array('f', [0.5 + i for i in range(len(d.keys()))])
    # for now assume asimov
    y = array('f', [0]*len(d.keys()))
    one_inf = array('f', [ abs(items["ones"][0]) for var, items in d.items() ])
    one_sup = array('f', [ abs(items["ones"][1]) for var, items in d.items() ])
    two_inf = array('f', [ abs(items["twos"][0]) for var, items in d.items() ])
    two_sup = array('f', [ abs(items["twos"][1]) for var, items in d.items() ])


    max_ = max(two_sup)
    min_ = -max(two_inf)

    c = ROOT.TCanvas("c", "c", 800, 600)
    c.SetGrid()
    leg = ROOT.TLegend(0.15, 0.85, 0.4, 0.7)

    margins = 0.11
    ROOT.gPad.SetRightMargin(margins)
    ROOT.gPad.SetLeftMargin(margins)
    ROOT.gPad.SetBottomMargin(margins)
    ROOT.gPad.SetTopMargin(margins)
    ROOT.gPad.SetFrameLineWidth(3)

    g1 = ROOT.TGraphAsymmErrors(len(x), array('d', x), array('d', y), array('d', [0.16]*len(x)), array('d', [0.16]*len(x)),  array('d', one_inf), array('d', one_sup))
    
    g1.SetMinimum(-10)
    g1.SetMaximum(15)
    g1.SetFillColor(ROOT.kOrange)
    g1.SetLineColor(ROOT.kOrange)
    g1.SetLineWidth(0)
    g1.SetMarkerStyle(24)
    g1.SetMarkerColor(ROOT.kBlue+1)
    g1.SetMarkerSize(2)
    g1.GetYaxis().SetRangeUser(-10,10)


    g2 = ROOT.TGraphAsymmErrors(len(x), array('d', x), array('d', y), array('d', [0.16]*len(x)), array('d', [0.16]*len(x)),  array('d', two_inf), array('d', two_sup))
    g2.SetFillColor(ROOT.kGreen+1)
    g2.SetLineWidth(0)
    g2.SetMarkerStyle(24)
    g2.SetMarkerColor(ROOT.kBlue+1)
    g2.SetMarkerSize(2)
    g2.GetYaxis().SetRangeUser(-15,15)

    leg.AddEntry(g1, "#pm 1#sigma Expected", "F")
    leg.AddEntry(g2, "#pm 2#sigma Expected", "F")
    leg.AddEntry(g1, "Best Fit", "P")
    if not legendlabel and legendlabel != "":
        leg.SetHeader("Operator: " + op)
    elif legendlabel == "":
        pass
    else:
        leg.SetHeader(legendlabel)

    leg.SetBorderSize(2)

    h = ROOT.TH1F("h", "h", len(x)+2, -1, len(x)+1)
    h.SetFillColor(0)
    h.SetCanExtend(ROOT.TH1.kAllAxes)
    h.SetStats(0)
    h.LabelsDeflate("X")
    h.LabelsDeflate("Y")
    h.LabelsOption("v")

    for idx in  range(-1, h.GetNbinsX()):
        if idx == 0: h.GetXaxis().SetBinLabel(idx + 1, "")
        if idx < len(d.keys())+1 and idx > 0: h.GetXaxis().SetBinLabel(idx + 1, d.keys()[idx-1])
        else: h.GetXaxis().SetBinLabel(idx + 1, "")

    if not ylabel and ylabel != "":
        h.GetYaxis().SetTitle(op + " Estimate")
    elif ylabel == "" :
        pass 
    else:
        h.GetYaxis().SetTitle(ylabel)

    h.GetYaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleOffset(0.8)
    h.GetXaxis().SetTitleOffset(0.2)
    ROOT.gStyle.SetLabelSize(.05, "XY")

    h.GetYaxis().SetRangeUser(1.5*min_,2*max_)
    g1.SetHistogram(h)

    h.Draw("AXIS")
    c.SetGrid()
    ROOT.gPad.RedrawAxis("g")
    g2.Draw("2 same")
    g1.Draw("2 same")
    g1.Draw("P same")

    c.SetTicks()
    leg.Draw()

    box = [
        generatePreliminaryBox(),
        generateTeVBox(),
        generateLumiBox("59.74"),
        generateCMSBox()
        ]

    for tex in box:
        tex.Draw("same")

    c.Draw()
    c.Print(output + ".png")
    c.Print(output + ".pdf")



def getBest(d):
    # the score is the mean between 1sigma and twosigma intervals
    scores = {key: ((abs(item["ones"][0]) +  abs(item["ones"][1])) + (abs(item["twos"][0]) +  abs(item["twos"][1]))/2) for key, item in d.items()}
    return min(scores, key=scores.get)


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="Txt file with the ranges for each operator" , type=str)
parser.add_argument("-o","--output", help="output directory where to store the plots" , type=str)
args = parser.parse_args()

if __name__ == "__main__":

    if not os.path.isdir(args.output):
        os.makedirs(args.output)

    f = open(args.file, 'r')

    # parse the range file
    con = [i.split("\n")[0].split("\t") for i in f.readlines()]

    # store results conviniently into a dictionary 
    ranges = {}
    for line in con:
        # if we only have one value then this is the operator header
        if len(line) == 1:
            op = line[0].strip('[').strip(']')
            ranges[op] = {}

        # if we have 3 objects then this stores the variable name, 1sigma range and 2sigma range
        elif len(line) == 3:
            var_name = line[0]
            ones = ast.literal_eval(line[1].strip(" "))
            twos = ast.literal_eval(line[2].strip(" "))

            ranges[op][var_name] = {
                "ones": ones,
                "twos": twos
            }


    # store best values 

    best = {}

    # for each operator plot the variable sensitivity rank

    for op in ranges.keys():
        
        best[op] = ranges[op][getBest(ranges[op])]
        drawSummary(ranges[op], args.output + "/" + op + "_variable_rank")

    # now draw summary for all ops
    drawSummary(best, args.output + "/Operators_rank", "Best Estimate", "")
