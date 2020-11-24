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

#cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/SMP-RunIIFall17wmLHEGS-00030/
#
## Make voms proxy
#voms-proxy-init --voms cms --out $(pwd)/voms_proxy.txt --hours 4
#export X509_USER_PROXY=$(pwd)/voms_proxy.txt

# Dump actual test code to a SMP-RunIIFall17wmLHEGS-00030_test.sh file that can be run in Singularity
cat <<'EndOfTestFile' > SMP-RunIIFall17wmLHEGS-00030_test.sh
#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc630

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_3_4/src  ] ; then
  echo release CMSSW_9_3_4 already exists
else
  scram p CMSSW CMSSW_9_3_4
fi
cd CMSSW_9_3_4/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIIFall17wmLHEGS-00030 --retry 3 --create-dirs -o Configuration/GenProduction/python/SMP-RunIIFall17wmLHEGS-00030-fragment.py
[ -s Configuration/GenProduction/python/SMP-RunIIFall17wmLHEGS-00030-fragment.py  ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 6.0115s
# Threads for each sequence: 4
# Time per event for single thread for each sequence: 4 * 6.0115s = 24.0458s
# Which adds up to 24.0458s per event
# Single core events that fit in validation duration: 23040s / 24.0458s = 958
# Produced events limit in McM is 10000
# According to 0.5040 efficiency, up to 10000 / 0.5040 = 19841 events should run
# Clamp (put value) 958 within 1 and 19841 -> 958
# It is estimated that this validation will produce: 958 * 0.5040 = 482 events
EVENTS=958

# Random seed between 1 and 100 for externalLHEProducer
SEED=$(($(date +%s) % 100 + 1))


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/SMP-RunIIFall17wmLHEGS-00030-fragment.py --python_filename SMP-RunIIFall17wmLHEGS-00030_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:SMP-RunIIFall17wmLHEGS-00030.root --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --no_exec --mc -n $EVENTS || exit $? ;

# End of SMP-RunIIFall17wmLHEGS-00030_test.sh file
EndOfTestFile

# Make file executable
chmod +x SMP-RunIIFall17wmLHEGS-00030_test.sh
./SMP-RunIIFall17wmLHEGS-00030_test.sh
#export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
#singularity run -B /afs -B /cvmfs -B /etc/grid-security --no-home docker://cmssw/slc6:latest $(echo $(pwd)/SMP-RunIIFall17wmLHEGS-00030_test.sh)
