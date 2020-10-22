#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIISummer15GS-00976/

export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_20_patch2/src  ] ; then
      echo release CMSSW_7_1_20_patch2 already exists
  else
        scram p CMSSW CMSSW_7_1_20_patch2
fi
cd CMSSW_7_1_20_patch2/src
eval `scram runtime -sh`

# Retrieve fragment from github and ensure it is there
curl  -s https://raw.githubusercontent.com/cms-sw/genproductions/071218017779916161e47643e07a49ea18433425/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --retry 2 --create-dirs -o Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py 
[ -s Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py  ] || exit $?;
scram b
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 71.0000s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 71.0000s = 71.0000s
# Which adds up to 71.0000s per event
# Single core events that fit in validation duration: 23040s / 71.0000s = 324
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 324 within 1 and 10000 -> 324
# It is estimated that this validation will produce: 324 * 1.0000 = 324 events
EVENTS=324


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --python_filename HIG-RunIISummer15GS-00976_1_cfg.py --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:HIG-RunIISummer15GS-00976.root --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --filein "dbs:/GluGluToHHTo2B2G_node_SM_13TeV-madgraph/RunIIWinter15wmLHE-MCRUN2_71_V1-v1/LHE" --no_exec --mc -n $EVENTS || exit $? ;
