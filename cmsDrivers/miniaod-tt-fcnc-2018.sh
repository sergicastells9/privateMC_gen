#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_5/src ] ; then 
 echo release CMSSW_10_2_5 already exists
else
scram p CMSSW CMSSW_10_2_5
fi
cd CMSSW_10_2_5/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/RunIIAutumn18DRPremix-tauDecays_102X_upgrade2018_realistic_v15-v1/AODSIM" --fileout file:TOP-RunIIAutumn18MiniAOD-00188.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename TOP-RunIIAutumn18MiniAOD-00188_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 8597 || exit $? ; 
