#!/bin/bash

#############################################################
#   This script is used by McM when it performs automatic   #
#  validation in HTCondor or submits requests to computing  #
#                                                           #
#      !!! THIS FILE IS NOT MEANT TO BE RUN BY YOU !!!      #
# If you want to run validation script yourself you need to #
#     get a "Get test" script which can be retrieved by     #
#  clicking a button next to one you just clicked. It will  #
# say "Get test command" when you hover your mouse over it  #
#      If you try to run this, you will have a bad time     #
#############################################################

# Make voms proxy
voms-proxy-init --voms cms --out $(pwd)/voms_proxy.txt --hours 4
export X509_USER_PROXY=$(pwd)/voms_proxy.txt

export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_6_20_patch1/src ] ; then
  echo release CMSSW_10_6_20_patch1 already exists
else
  scram p CMSSW CMSSW_10_6_20_patch1
fi
cd CMSSW_10_6_20_patch1/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIISummer20UL16wmLHEGENAPV-00298 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIISummer20UL16wmLHEGENAPV-00298-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIISummer20UL16wmLHEGENAPV-00298-fragment.py ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 30%
# Validation duration with margin: 28800 * (1 - 0.30) = 20160s
# Time per event for each sequence: 71.7896s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 71.7896s = 71.7896s
# Which adds up to 71.7896s per event
# Single core events that fit in validation duration: 20160s / 71.7896s = 280
# Produced events limit in McM is 10000
# According to 0.1330 efficiency, validation should run 10000 / 0.1330 = 75187 events to reach the limit of 10000
# Take the minimum of 280 and 75187, but more than 0 -> 280
# It is estimated that this validation will produce: 280 * 0.1330 = 37 events
EVENTS=280


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer20UL16wmLHEGENAPV-00298-fragment.py --python_filename HIG-RunIISummer20UL16wmLHEGENAPV-00298_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:HIG-RunIISummer20UL16wmLHEGENAPV-00298.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step LHE,GEN --geometry DB:Extended --era Run2_2016_HIPM --no_exec --mc -n $EVENTS  --nThreads 1 || exit $? ;
