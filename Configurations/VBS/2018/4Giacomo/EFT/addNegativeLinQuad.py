import ROOT 


ops = ['cW', 'cHDD', 'cHW', 'cHWB', 'cHbox', 'cHj1', 'cHj3', 'cHl1', 'cHl3', 'cll1', 'cjj11', 'cjj31', 'cjj18', 'cjj38']
f = ROOT.TFile("EFTallOp/wzsrEFT_forplots.root", "UPDATE")

for region in [i.GetName() for i in f.GetListOfKeys()]:
    d = f.Get(region)
    f.cd(region)

    for var in [j.GetName() for j in d.GetListOfKeys()]:
        d_ = d.Get(var)
        f.cd(region + "/" + var)

        for shape in ["lin", "quad"]:
            for op in ops:

                s_ = "histo_" + shape + "_" + op 
                new_s_ = "histo_" + shape + "m1_" + op 
                # print (s_)
                h = d_.Get(s_)
                h2 = h.Clone(new_s_)
                h2.Scale(-1)
                h2.SetName(new_s_)

                h2.Write(new_s_)

f.Close()
