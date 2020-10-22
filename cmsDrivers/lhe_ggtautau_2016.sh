#!/bin/bash

cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/HIG-RunIIWinter15wmLHE-00576/

export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_20/src  ] ; then
      echo release CMSSW_7_1_20 already exists
  else
        scram p CMSSW CMSSW_7_1_20
fi
cd CMSSW_7_1_20/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIIWinter15wmLHE-00576 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIIWinter15wmLHE-00576-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIIWinter15wmLHE-00576-fragment.py  ] || exit $?;
scram b
cd ../..

# PdmV proxy
export X509_USER_PROXY=/afs/cern.ch/user/p/pdmvserv/private/$HOSTNAME/voms_proxy.cert

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 0.3842s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 0.3842s = 0.3842s
# Which adds up to 0.3842s per event
# Single core events that fit in validation duration: 23040s / 0.3842s = 59968
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 59968 within 1 and 10000 -> 10000
# It is estimated that this validation will produce: 10000 * 1.0000 = 10000 events
EVENTS=10000


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/HIG-RunIIWinter15wmLHE-00576-fragment.py --python_filename HIG-RunIIWinter15wmLHE-00576_1_cfg.py --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --fileout file:HIG-RunIIWinter15wmLHE-00576.root --conditions MCRUN2_71_V1::All --step LHE --no_exec --mc -n $EVENTS || exit $? ;
