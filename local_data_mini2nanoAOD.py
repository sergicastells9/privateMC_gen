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

from dsdefs_centralminiaod_UL import dsdefs_data, dsdefs_MC_latest
# for local inputs
local_sets = []


if not args.skip_local:
 	local_sets = [
		("DoubleEG_Run2016B-ver2_HIPM_UL2016_MiniAODv2-v3_MINIAOD_final"								, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016B-ver2_HIPM_UL2016_MiniAODv2-v3_MINIAOD_final"		, 1, "2016_Data"),
		("DoubleEG_Run2016C-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"											, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016C-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"					, 1, "2016_Data"),
		("DoubleEG_Run2016D-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"											, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016D-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"					, 1, "2016_Data"),
		("DoubleEG_Run2016E-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"											, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016E-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"					, 1, "2016_Data"),
		("DoubleEG_Run2016F-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"											, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016F-HIPM_UL2016_MiniAODv2-v1_MINIAOD_final"					, 1, "2016_Data"),
		("DoubleEG_Run2016G-UL2016_MiniAODv2-v1_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016G-UL2016_MiniAODv2-v1_MINIAOD_final"							, 1, "2016_Data"),
		("DoubleEG_Run2016H-UL2016_MiniAODv2-v1_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2016H-UL2016_MiniAODv2-v1_MINIAOD_final"							, 1, "2016_Data"),
		("DoubleEG_Run2017B-UL2017_MiniAODv2-v1_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2017B-UL2017_MiniAODv2-v1_MINIAOD_final"							, 1, "2017_Data"),
		("DoubleEG_Run2017C-UL2017_MiniAODv2-v2_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2017C-UL2017_MiniAODv2-v2_MINIAOD_final"							, 1, "2017_Data"),
		("DoubleEG_Run2017D-UL2017_MiniAODv2-v1_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2017D-UL2017_MiniAODv2-v1_MINIAOD_final"							, 1, "2017_Data"),
		("DoubleEG_Run2017E-UL2017_MiniAODv2-v1_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2017E-UL2017_MiniAODv2-v1_MINIAOD_final"							, 1, "2017_Data"),
		("DoubleEG_Run2017F-UL2017_MiniAODv2-v2_MINIAOD_final"													, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/DoubleEG_Run2017F-UL2017_MiniAODv2-v2_MINIAOD_final"							, 1, "2017_Data"),
		("EGamma_Run2018A-UL2018_MiniAODv2-v1_MINIAOD_final"														, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/EGamma_Run2018A-UL2018_MiniAODv2-v1_MINIAOD_final"								, 1, "2018_Data"),
		("EGamma_Run2018C-UL2018_MiniAODv2-v1_MINIAOD_final"														, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/EGamma_Run2018C-UL2018_MiniAODv2-v1_MINIAOD_final"								, 1, "2018_Data"),
		("EGamma_Run2018D-UL2018_MiniAODv2-v2_MINIAOD_final"														, "/ceph/cms/store/user/fsetti/failing_UL_Data_jobs/EGamma_Run2018D-UL2018_MiniAODv2-v2_MINIAOD_final"								, 1, "2018_Data"),
]

# some job configurations
job_dir = "Summer20UL_nanoAODv9/"
job_tag = args.tag
job_filter = args.filter
ds_filter = args.dsfilter
skip_central = args.skip_central
hadoop_path = "{0}".format(job_dir)

cmssw_ver = "CMSSW_10_6_26"

DOSKIM = False 

#exec_path = "condor_exe_%s.sh" % args.tag
exec_path = "condor_exe_ceph.sh"
#tar_path = "nanoAOD_package_%s.tar.gz" % args.tag


if not args.soft_rerun:
    os.system("rm no_fixedGridRho_CMSSW/package.tar.gz")
    os.system(" cd no_fixedGridRho_CMSSW; XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s; cd .." % cmssw_ver)

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
                tarfile = "no_fixedGridRho_CMSSW/package.tar.gz",
                condor_submit_params = {"sites": "T2_US_UCSD,T2_US_CALTECH,T2_US_WISCONSIN,T2_US_Florida", # other_sites can be good_sites, your own list, etc.
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]]},
                special_dir = hadoop_path,
                arguments = args.replace(" ","|"),
        )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary_local_data.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)

    # parse the total summary and write out the dashboard
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_nanoaod_v9_local_data/").do()
    os.system("chmod -R 755 ~/public_html/dump/metis_nanoaod_v9_local_data")
    if allcomplete:
        print ""
        print "Job={} finished".format(job_tag)
        print ""
        break
    sleep_time	= 90 * 60
    print "Sleeping " + str(sleep_time / 60) + " minutes ..."
    time.sleep(sleep_time)
