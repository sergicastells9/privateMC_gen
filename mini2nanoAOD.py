import sys, os
import time
import itertools
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

from dsdefs_centralminiaod_UL import dsdefs_h4g
# for local inputs
local_sets = []

# some job configurations
job_dir = "test/"
job_tag = args.tag
job_filter = args.filter
ds_filter = args.dsfilter
skip_central = args.skip_central
hadoop_path = "{0}".format(job_dir)

cmssw_ver = "CMSSW_10_6_26"

DOSKIM = False 

exec_path = "condor_exe_%s.sh" % args.tag
#exec_path = "condor_exe_ceph.sh"
#tar_path = "nanoAOD_package_%s.tar.gz" % args.tag

if not args.soft_rerun:
#    os.system("rm -rf tasks/*" + args.tag + "*")
    os.system("rm package.tar.gz")
    os.system("XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s" % cmssw_ver)

total_summary = {}
while True:
    allcomplete = True

    # Loop through central samples
    for ds,fpo,args in dsdefs_h4g[:] :
        if skip_central: continue
        if (job_filter != "") and (args not in job_filter) : continue         
        if (ds_filter != "") and (ds_filter not in ds) : continue         
        sample = DBSSample( dataset=ds )
        print(ds, args)

        task = CondorTask(
                sample = sample,
                open_dataset = False,
                files_per_output = fpo,
                output_name = "nanoaod.root",
                tag = job_tag,
								cmssw_version = cmssw_ver,
                executable = exec_path,
                tarfile = "./package.tar.gz",
                condor_submit_params = {"sites": "T3_US_NotreDame", # other_sites can be good_sites, your own list, etc.
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]],
										"use_xrootd":True
								},
                special_dir = hadoop_path,
                arguments = args.replace(" ","|")
                )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)



    # parse the total summary and write out the dashboard
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_nanoaod_v9/").do()
    os.system("chmod -R 755 ~/public_html/dump/metis_nanoaod_v9")
    if allcomplete:
        print ""
        print "Job={} finished".format(job_tag)
        print ""
        break
    sleep_time	= 90 * 60 ## CHANGE THIS BACK TO 90*60
    print "Sleeping " + str(sleep_time / 60) + " minutes ..."
    time.sleep(sleep_time)
