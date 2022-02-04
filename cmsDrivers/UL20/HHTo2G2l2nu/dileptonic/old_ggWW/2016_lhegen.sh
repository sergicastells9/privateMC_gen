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

#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_46/src ] ; then
  echo release CMSSW_7_1_46 already exists
else
  scram p CMSSW CMSSW_7_1_46
fi
cd CMSSW_7_1_46/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIISummer15wmLHEGS-03966 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-03966-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-03966-fragment.py ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 30%
# Validation duration with margin: 28800 * (1 - 0.30) = 20160s
# Time per event for each sequence: 24.9409s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 24.9409s = 24.9409s
# Which adds up to 24.9409s per event
# Single core events that fit in validation duration: 20160s / 24.9409s = 808
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, validation should run 10000 / 1.0000 = 10000 events to reach the limit of 10000
# Take the minimum of 808 and 10000, but more than 0 -> 808
# It is estimated that this validation will produce: 808 * 1.0000 = 808 events
EVENTS=808

# Random seed between 1 and 100 for externalLHEProducer
SEED=$(($(date +%s) % 100 + 1))


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-03966-fragment.py --python_filename HIG-RunIISummer15wmLHEGS-03966_1_cfg.py --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:HIG-RunIISummer15wmLHEGS-03966.root --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --magField 38T_PostLS1 --no_exec --mc -n $EVENTS || exit $? ;


