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
if [ -r CMSSW_10_6_27/src ] ; then
  echo release CMSSW_10_6_27 already exists
else
  scram p CMSSW CMSSW_10_6_27
fi
cd CMSSW_10_6_27/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIISummer20UL18wmLHEGEN-02774 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIISummer20UL18wmLHEGEN-02774-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIISummer20UL18wmLHEGEN-02774-fragment.py ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 30%
# Validation duration with margin: 28800 * (1 - 0.30) = 20160s
# Time per event for each sequence: 3.9803s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 3.9803s = 3.9803s
# Which adds up to 3.9803s per event
# Single core events that fit in validation duration: 20160s / 3.9803s = 5064
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, validation should run 10000 / 1.0000 = 10000 events to reach the limit of 10000
# Take the minimum of 5064 and 10000, but more than 0 -> 5064
# It is estimated that this validation will produce: 5064 * 1.0000 = 5064 events
EVENTS=5064


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer20UL18wmLHEGEN-02774-fragment.py --python_filename HIG-RunIISummer20UL18wmLHEGEN-02774_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:HIG-RunIISummer20UL18wmLHEGEN-02774.root --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN --geometry DB:Extended --era Run2_2018 --no_exec --mc -n $EVENTS  --nThreads 1 || exit $? ;
