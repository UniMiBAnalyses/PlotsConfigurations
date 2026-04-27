#!/bin/bash

# Configura l'ambiente
export X509_USER_PROXY=/afs/cern.ch/user/a/abulla/.proxy
export EOS_MGM_URL=root://eoscms.cern.ch
voms-proxy-info
export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/cern.ch/user/a/abulla/CMSSW_11_1_4
eval `scramv1 ru -sh`
ulimit -c 0 -s unlimited

# Passaggio alla directory temporanea
cd $TMPDIR
echo "Current directory: $(pwd)"
echo "Contents of $TMPDIR:"
ls -l

# Copia dei file necessari nella directory temporanea
cp /afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/SymmetrizeByHand.py .
cp /afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/ALL/jet1pt/samples_jet1pt.py .
cp /afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/ALL/jet1pt/variables_jet1pt.py .
cp /afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/ALL/jet1pt/nuisances.py .
xrdcp /eos/user/a/abulla/www/public/VBF_W/2018/sys/rootFile/unfolding_final_v11_jet1pt/fixed_plots_vbf_w_2018unfolding_final_v11_jet1pt.root .
ls -l

# Controllo input
if [ ! -f "fixed_plots_vbf_w_2018unfolding_final_v11_jet1pt.root" ]; then
  echo "[ERROR] File di input non trovato in TMPDIR!"
  exit 1
fi

# Esecuzione dello script Python
python SymmetrizeByHand.py \
  --input fixed_plots_vbf_w_2018unfolding_final_v11_jet1pt.root \
  --samples samples_jet1pt.py \
  --nuisances nuisances.py \
  --onlyVar variables_jet1pt.py \
  --mode fix_empty \
  --update

# Controllo se lo script Python ha avuto successo
if [ -f "fixed_plots_vbf_w_2018unfolding_final_v11_jet1pt.root" ]; then
  echo "[INFO] Output ROOT file creato."
else
  echo "[ERROR] Nessun file di output creato!"
  exit 1
fi

# Copia finale su EOS se tutto è andato a buon fine
if [ $? -eq 0 ]; then
  echo "[INFO] Script completato con successo, copio l'output su EOS..."
  xrdcp -f fixed_plots_vbf_w_2018unfolding_final_v11_jet1pt.root /eos/user/a/abulla/www/public/VBF_W/2018/sys/rootFile/unfolding_final_v11_jet1pt/fixed_plots_vbf_w_2018unfolding_final_v11_jet1pt.root
echo "[INFO] Copia completata."
else
  echo "[ERROR] Script Python fallito, nessun file copiato!"
  exit 1
fi
