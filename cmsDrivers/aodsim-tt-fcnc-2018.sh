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
cmsDriver.py step1 --fileout file:TOP-RunIIAutumn18DRPremix-00181_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename TOP-RunIIAutumn18DRPremix-00181_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2626 || exit $? ; 

cmsDriver.py step2 --filein file:TOP-RunIIAutumn18DRPremix-00181_step1.root --fileout file:TOP-RunIIAutumn18DRPremix-00181.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --procModifiers premix_stage2 --nThreads 8 --era Run2_2018 --python_filename TOP-RunIIAutumn18DRPremix-00181_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2626 || exit $? ;
