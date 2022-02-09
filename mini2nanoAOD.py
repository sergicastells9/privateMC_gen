import sys, os
import time
import itertools
import numpy
import json

from metis.Sample import DBSSample, DirectorySample, Sample
from metis.CondorTask import CondorTask
from metis.StatsParser import StatsParser

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this set of babies", type=str)
parser.add_argument("--filter", help = "only process mc/data with some requirement (e.g. 2016MC, 2017Data)", default="", type=str)
parser.add_argument("--dsfilter", help = "only process mc/data with some name pattern(e.g. DY***)", default="", type=str)
parser.add_argument("--soft_rerun", help = "don't remake tarball", action="store_true")
parser.add_argument("--skip_local", help = "don't submit jobs for local samples", action = "store_true")
parser.add_argument("--skip_central", help = "don't submit jobs for central samples", action = "store_true")
args = parser.parse_args()

# for central inputs
#dsdefs = []
## datasetname, filesPerOutput, filtername
from dsdefs_centralminiaod_UL import dsdefs
# for local inputs
local_sets = []


if not args.skip_local:
    local_sets = [
        ("DiPhotonJetsBox1BJet_MGG_80toInf_2016", "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/DiPhotonJetsBox1BJet_MGG_80toInf_2016_APV_STEP6_v1/", 1, "2016_MC"),
    ]

# some job configurations
job_dir = "nanoaod_runII_20UL/nanoAODv9/"
job_tag = args.tag
job_filter = args.filter
ds_filter = args.dsfilter
skip_central = args.skip_central
hadoop_path = "{0}".format(job_dir)

cmssw_ver = "CMSSW_10_6_26"

DOSKIM = False 

#exec_path = "condor_exe_%s.sh" % args.tag
exec_path = "condor_exe.sh"
#tar_path = "nanoAOD_package_%s.tar.gz" % args.tag

if not args.soft_rerun:
#    os.system("rm -rf tasks/*" + args.tag + "*")
    os.system("rm package.tar.gz")
    os.system("XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s" % cmssw_ver)

    #os.system("cp package.tar.gz /hadoop/cms/store/user/smay/FCNC/tarballs/%s" % tar_path)
    #os.system("hadoop fs -setrep -R 30 /cms/store/user/smay/FCNC/tarballs/%s" % tar_path)

total_summary = {}
while True:
    allcomplete = True

    # Loop through local samples
    for ds,loc,fpo,args in local_sets[:]:
        sample = DirectorySample( dataset = ds, location = loc )
        files = [f.name for f in sample.get_files()]
        print "For sample %s in directory %s, there are %d input files" % (ds, loc, len(files))
        #for file in files:
        #    print file

        task = CondorTask(
                sample = sample,
                open_dataset = True,
                files_per_output = fpo,
                output_name = "nanoaod.root",
                tag = job_tag,
                cmssw_version = cmssw_ver,
                executable = exec_path,
                tarfile = "./package.tar.gz",
                condor_submit_params = {"sites" : "T2_US_UCSD",
                    #"classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6-m202006"]]},
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]]},
                special_dir = hadoop_path,
								#additional_input_files = [ "/home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/miniAOD_to_nanoAOD/HIG-RunIISummer20UL16NanoAODv9-00678_1_cfg.py" ],
                arguments = args.replace(" ","|")
        )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)


    # parse the total summary and write out the dashboard
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_nanoaod_v8/").do()
    os.system("chmod -R 755 ~/public_html/dump/metis_nanoaod_v8")
    if allcomplete:
        print ""
        print "Job={} finished".format(job_tag)
        print ""
        break
    print "Sleeping 10 minutes ..."
    time.sleep(10*60)
