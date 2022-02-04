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

#cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/SMP-RunIIFall18wmLHEGS-00239/
#
## Make voms proxy
#voms-proxy-init --voms cms --out $(pwd)/voms_proxy.txt --hours 4
#export X509_USER_PROXY=$(pwd)/voms_proxy.txt
#
## Dump actual test code to a SMP-RunIIFall18wmLHEGS-00239_test.sh file that can be run in Singularity
#cat <<'EndOfTestFile' > SMP-RunIIFall18wmLHEGS-00239_test.sh
#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_22/src  ] ; then
  echo release CMSSW_10_2_22 already exists
else
  scram p CMSSW CMSSW_10_2_22
fi
cd CMSSW_10_2_22/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIIFall18wmLHEGS-00239 --retry 3 --create-dirs -o Configuration/GenProduction/python/SMP-RunIIFall18wmLHEGS-00239-fragment.py
[ -s Configuration/GenProduction/python/SMP-RunIIFall18wmLHEGS-00239-fragment.py  ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 1.8263s
# Threads for each sequence: 8
# Time per event for single thread for each sequence: 8 * 1.8263s = 14.6103s
# Which adds up to 14.6103s per event
# Single core events that fit in validation duration: 23040s / 14.6103s = 1576
# Produced events limit in McM is 10000
# According to 0.5310 efficiency, up to 10000 / 0.5310 = 18832 events should run
# Clamp (put value) 1576 within 1 and 18832 -> 1576
# It is estimated that this validation will produce: 1576 * 0.5310 = 836 events
EVENTS=1576

# Random seed between 1 and 100 for externalLHEProducer
SEED=$(($(date +%s) % 100 + 1))


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/SMP-RunIIFall18wmLHEGS-00239-fragment.py --python_filename SMP-RunIIFall18wmLHEGS-00239_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:SMP-RunIIFall18wmLHEGS-00239.root --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc -n $EVENTS || exit $? ;

# End of SMP-RunIIFall18wmLHEGS-00239_test.sh file
EndOfTestFile

# Make file executable
chmod +x SMP-RunIIFall18wmLHEGS-00239_test.sh

#export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
#singularity run -B /afs -B /cvmfs -B /etc/grid-security --no-home docker://cmssw/slc6:latest $(echo $(pwd)/SMP-RunIIFall18wmLHEGS-00239_test.sh)
