#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/SMP-RunIISummer16NanoAODv7-00246/

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
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 0.4000s
# Threads for each sequence: 2
# Time per event for single thread for each sequence: 2 * 0.4000s = 0.8000s
# Which adds up to 0.8000s per event
# Single core events that fit in validation duration: 23040s / 0.8000s = 28800
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 28800 within 1 and 10000 -> 10000
# It is estimated that this validation will produce: 10000 * 1.0000 = 10000 events
EVENTS=10000


# cmsDriver command
cmsDriver.py  --python_filename SMP-RunIISummer16NanoAODv7-00246_1_cfg.py --eventcontent NANOEDMAOD --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:SMP-RunIISummer16NanoAODv7-00246.root --conditions 102X_mcRun2_asymptotic_v8 --step NANO --filein "dbs:/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM" --era Run2_2016,run2_nanoAOD_94X2016 --no_exec --mc -n $EVENTS || exit $? ;
