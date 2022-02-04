#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIISummer16DR80Premix-00867/

export SCRAM_ARCH=slc6_amd64_gcc530

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_8_0_21/src  ] ; then
      echo release CMSSW_8_0_21 already exists
  else
        scram p CMSSW CMSSW_8_0_21
fi
cd CMSSW_8_0_21/src
eval `scram runtime -sh`

scram b
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 17.0000s, 17.0000s
# Threads for each sequence: 4, 4
# Time per event for single thread for each sequence: 4 * 17.0000s = 68.0000s, 4 * 17.0000s = 68.0000s
# Which adds up to 136.0000s per event
# Single core events that fit in validation duration: 23040s / 136.0000s = 169
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 169 within 1 and 10000 -> 169
# It is estimated that this validation will produce: 169 * 1.0000 = 169 events
EVENTS=169


# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIISummer16DR80Premix-00867_1_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:HIG-RunIISummer16DR80Premix-00867_0.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --filein "dbs:/GluGluToHHTo2B2G_node_SM_13TeV-madgraph/RunIISummer15GS-MCRUN2_71_V1-v1/GEN-SIM" --datamix PreMix --era Run2_2016 --no_exec --mc -n $EVENTS || exit $? ;

# cmsDriver command
cmsDriver.py  --python_filename HIG-RunIISummer16DR80Premix-00867_2_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:HIG-RunIISummer16DR80Premix-00867.root --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --filein file:HIG-RunIISummer16DR80Premix-00867_0.root --era Run2_2016 --runUnscheduled --no_exec --mc -n $EVENTS || exit $? ;
