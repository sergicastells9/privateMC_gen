#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIIFall17DRPremix-01682/

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
# Time per event for each sequence: 1.2181s, 2.0704s
# Threads for each sequence: 8, 8
# Time per event for single thread for each sequence: 8 * 1.2181s = 9.7448s, 8 * 2.0704s = 16.5632s
# Which adds up to 26.3080s per event
# Single core events that fit in validation duration: 23040s / 26.3080s = 875
# Produced events limit in McM is 0
# According to 1.0000 efficiency, up to 0 / 1.0000 = 0 events should run
# Clamp (put value) 875 within 1 and 0 -> 1
# It is estimated that this validation will produce: 1 * 1.0000 = 1 events
EVENTS=1


# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIIFall17DRPremix-01682_1_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:HIG-RunIIFall17DRPremix-01682_0.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --filein file:HIG-RunIIFall17wmLHEGS-00429.root --datamix PreMix --era Run2_2017 --no_exec --mc -n $EVENTS || exit $? ;

# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIIFall17DRPremix-01682_2_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:HIG-RunIIFall17DRPremix-01682.root --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --filein file:HIG-RunIIFall17DRPremix-01682_0.root --era Run2_2017 --runUnscheduled --no_exec --mc -n $EVENTS || exit $? ;
