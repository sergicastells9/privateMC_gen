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

#cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/SMP-RunIISummer15wmLHEGS-00020/
#
## Make voms proxy
#voms-proxy-init --voms cms --out $(pwd)/voms_proxy.txt --hours 4
#export X509_USER_PROXY=$(pwd)/voms_proxy.txt
#
## Dump actual test code to a SMP-RunIISummer15wmLHEGS-00020_test.sh file that can be run in Singularity
#cat <<'EndOfTestFile' > SMP-RunIISummer15wmLHEGS-00020_test.sh
#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_21_patch2/src  ] ; then
  echo release CMSSW_7_1_21_patch2 already exists
else
  scram p CMSSW CMSSW_7_1_21_patch2
fi
cd CMSSW_7_1_21_patch2/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIISummer15wmLHEGS-00020 --retry 3 --create-dirs -o Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00020-fragment.py
[ -s Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00020-fragment.py  ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 38.0000s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 38.0000s = 38.0000s
# Which adds up to 38.0000s per event
# Single core events that fit in validation duration: 23040s / 38.0000s = 606
# Produced events limit in McM is 10000
# According to 0.5267 efficiency, up to 10000 / 0.5267 = 18986 events should run
# Clamp (put value) 606 within 1 and 18986 -> 606
# It is estimated that this validation will produce: 606 * 0.5267 = 319 events
EVENTS=606

# Random seed between 1 and 100 for externalLHEProducer
SEED=$(($(date +%s) % 100 + 1))


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00020-fragment.py --python_filename SMP-RunIISummer15wmLHEGS-00020_1_cfg.py --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:SMP-RunIISummer15wmLHEGS-00020.root --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})" --step LHE,GEN,SIM --magField 38T_PostLS1 --no_exec --mc -n $EVENTS || exit $? ;

# End of SMP-RunIISummer15wmLHEGS-00020_test.sh file
EndOfTestFile

# Make file executable
chmod +x SMP-RunIISummer15wmLHEGS-00020_test.sh
./SMP-RunIISummer15wmLHEGS-00020_test.sh

#export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
#singularity run -B /afs -B /cvmfs -B /etc/grid-security --no-home docker://cmssw/slc6:latest $(echo $(pwd)/SMP-RunIISummer15wmLHEGS-00020_test.sh)
