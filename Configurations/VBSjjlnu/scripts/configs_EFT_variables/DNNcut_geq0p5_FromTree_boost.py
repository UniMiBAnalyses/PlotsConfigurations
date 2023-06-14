conf = {
    # define SR, if will cycle on all the variables it finds in the subfolder and create a datacard for each
    # for now the same variable is assumed in all the SR, in future we can mix but will become computationally expensive
    "SR": ["boost_sig_ele_DNN_geq_0p5", "boost_sig_mu_DNN_geq_0p5"],
    # For the CR the variables to fit should not change as we do not really expect much EFT and 
    # they should be used to measure bkg normalizations
    "CR": {
        "boost_sig_ele_DNN_leq_0p5": "DNNoutput_boost",
        "boost_sig_mu_DNN_leq_0p5": "DNNoutput_boost",
    }
}
