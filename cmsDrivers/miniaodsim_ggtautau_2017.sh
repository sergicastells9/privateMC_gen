#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIIFall17MiniAODv2-01813/

export SCRAM_ARCH=slc6_amd64_gcc630

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_6_patch1/src  ] ; then
      echo release CMSSW_9_4_6_patch1 already exists
  else
        scram p CMSSW CMSSW_9_4_6_patch1
fi
cd CMSSW_9_4_6_patch1/src
eval `scram runtime -sh`

scram b
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 1.2000s
# Threads for each sequence: 4
# Time per event for single thread for each sequence: 4 * 1.2000s = 4.8000s
# Which adds up to 4.8000s per event
# Single core events that fit in validation duration: 23040s / 4.8000s = 4800
# Produced events limit in McM is 0
# According to 1.0000 efficiency, up to 0 / 1.0000 = 0 events should run
# Clamp (put value) 4800 within 1 and 0 -> 1
# It is estimated that this validation will produce: 1 * 1.0000 = 1 events
EVENTS=1


# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIIFall17MiniAODv2-01813_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:HIG-RunIIFall17MiniAODv2-01813.root --conditions 94X_mc2017_realistic_v14 --step PAT --scenario pp --filein file:HIG-RunIIFall17DRPremix-01682.root --era Run2_2017,run2_miniAOD_94XFall17 --runUnscheduled --no_exec --mc -n $EVENTS || exit $? ;
