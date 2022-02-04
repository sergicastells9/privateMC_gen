#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIIFall17NanoAOD-01820/

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
# Time per event for each sequence: 0.3400s
# Threads for each sequence: 2
# Time per event for single thread for each sequence: 2 * 0.3400s = 0.6800s
# Which adds up to 0.6800s per event
# Single core events that fit in validation duration: 23040s / 0.6800s = 33882
# Produced events limit in McM is 0
# According to 1.0000 efficiency, up to 0 / 1.0000 = 0 events should run
# Clamp (put value) 33882 within 1 and 0 -> 1
# It is estimated that this validation will produce: 1 * 1.0000 = 1 events
EVENTS=1


# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIIFall17NanoAOD-01820_1_cfg.py --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HIG-RunIIFall17NanoAOD-01820.root --conditions 94X_mc2017_realistic_v14 --step NANO --filein file:HIG-RunIIFall17MiniAODv2-01813.root --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --no_exec --mc -n $EVENTS || exit $? ;
