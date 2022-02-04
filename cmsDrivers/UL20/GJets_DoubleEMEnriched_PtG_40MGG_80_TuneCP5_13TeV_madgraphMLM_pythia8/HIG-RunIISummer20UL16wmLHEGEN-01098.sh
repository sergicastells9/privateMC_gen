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
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIISummer20UL16wmLHEGEN-01098 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIISummer20UL16wmLHEGEN-01098-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIISummer20UL16wmLHEGEN-01098-fragment.py ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 30%
# Validation duration with margin: 28800 * (1 - 0.30) = 20160s
# Time per event for each sequence: 59.8612s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 59.8612s = 59.8612s
# Which adds up to 59.8612s per event
# Single core events that fit in validation duration: 20160s / 59.8612s = 336
# Produced events limit in McM is 10000
# According to 0.1430 efficiency, validation should run 10000 / 0.1430 = 69930 events to reach the limit of 10000
# Take the minimum of 336 and 69930, but more than 0 -> 336
# It is estimated that this validation will produce: 336 * 0.1430 = 48 events
EVENTS=336


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer20UL16wmLHEGEN-01098-fragment.py --python_filename HIG-RunIISummer20UL16wmLHEGEN-01098_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:HIG-RunIISummer20UL16wmLHEGEN-01098.root --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step LHE,GEN --geometry DB:Extended --era Run2_2016 --no_exec --mc -n $EVENTS  --nThreads 1 || exit $? ;
