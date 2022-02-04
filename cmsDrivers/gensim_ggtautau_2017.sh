#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIIFall17wmLHEGS-00429/

export SCRAM_ARCH=slc6_amd64_gcc630

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_3_6/src  ] ; then
      echo release CMSSW_9_3_6 already exists
  else
        scram p CMSSW CMSSW_9_3_6
fi
cd CMSSW_9_3_6/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIIFall17wmLHEGS-00429 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-00429-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-00429-fragment.py  ] || exit $?;
scram b
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 6.0518s
# Threads for each sequence: 8
# Time per event for single thread for each sequence: 8 * 6.0518s = 48.4144s
# Which adds up to 48.4144s per event
# Single core events that fit in validation duration: 23040s / 48.4144s = 475
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 475 within 1 and 10000 -> 475
# It is estimated that this validation will produce: 475 * 1.0000 = 475 events
EVENTS=475

# Random seed between 1 and 100 for externalLHEProducer
SEED=$(($(date +%s) % 100 + 1))


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-00429-fragment.py --python_filename HIG-RunIIFall17wmLHEGS-00429_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:HIG-RunIIFall17wmLHEGS-00429.root --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --no_exec --mc -n $EVENTS || exit $? ;
