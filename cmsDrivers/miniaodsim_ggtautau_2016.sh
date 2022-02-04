#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIISummer16MiniAODv3-03284/

export SCRAM_ARCH=slc6_amd64_gcc630

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_9/src  ] ; then
      echo release CMSSW_9_4_9 already exists
  else
        scram p CMSSW CMSSW_9_4_9
fi
cd CMSSW_9_4_9/src
eval `scram runtime -sh`

scram b
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 0.1985s
# Threads for each sequence: 8
# Time per event for single thread for each sequence: 8 * 0.1985s = 1.5880s
# Which adds up to 1.5880s per event
# Single core events that fit in validation duration: 23040s / 1.5880s = 14508
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 14508 within 1 and 10000 -> 10000
# It is estimated that this validation will produce: 10000 * 1.0000 = 10000 events
EVENTS=10000


# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIISummer16MiniAODv3-03284_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:HIG-RunIISummer16MiniAODv3-03284.root --conditions 94X_mcRun2_asymptotic_v3 --step PAT --filein "dbs:/GluGluToHHTo2B2G_node_SM_13TeV-madgraph/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM" --era Run2_2016,run2_miniAOD_80XLegacy --runUnscheduled --no_exec --mc -n $EVENTS || exit $? ;
