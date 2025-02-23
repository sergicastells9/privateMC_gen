#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_22/src  ] ; then 
     echo release CMSSW_10_2_22 already exists
 else
     scram p CMSSW CMSSW_10_2_22
fi
cd CMSSW_10_2_22/src
eval `scram runtime -sh`


scram b
cd ../../
#cmsDriver.py step1 --filein "dbs:/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" --fileout file:HIG-RunIIAutumn18NanoAODv7-01786.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v21 --step NANO --nThreads 2 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename HIG-RunIIAutumn18NanoAODv7-01786_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 
cmsDriver.py step1 --filein "dbs:/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" --fileout file:HIG-RunIIAutumn18NanoAODv7-01786.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v21 --step NANO --nThreads 1 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename HIG-RunIIAutumn18NanoAODv7-01786_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 

