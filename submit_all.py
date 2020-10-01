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
parser.add_argument("--soft_rerun", help = "don't remake tarball", action="store_true")
parser.add_argument("--skip_local", help = "don't submit jobs for local samples", action = "store_true")
parser.add_argument("--skip_central", help = "don't submit jobs for central samples", action = "store_true")
args = parser.parse_args()

job_dir = "miniaod_runII/test_metis/"
job_tag = args.tag
hadoop_path = "{0}".format(job_dir)

cmssw_ver = "CMSSW_10_2_22"

DOSKIM = False 

#exec_path = "condor_exe_%s.sh" % args.tag
exec_path = "condor_exe.sh"
tar_path = "nanoAOD_package_%s.tar.gz" % args.tag

if not args.soft_rerun:
    os.system("rm -rf tasks/*" + args.tag + "*")
    os.system("rm package.tar.gz")
    os.system("XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s" % cmssw_ver)

    #os.system("cp package.tar.gz /hadoop/cms/store/user/smay/FCNC/tarballs/%s" % tar_path)
    #os.system("hadoop fs -setrep -R 30 /cms/store/user/smay/FCNC/tarballs/%s" % tar_path)

#with open("condor_exe.sh", "r") as f_in:
#    lines = f_in.readlines()

#with open(exec_path, "w") as f_out:
#    for i in range(len(lines)):
#        if "FIXME" in lines[i]:
#            lines[i] = lines[i].replace("FIXME", tar_path)
#    for line in lines:
#        f_out.write(line)

def getArgs(pid, dataset, json):
    datasetName = dataset.split("/")[1]
    if "EGamma" in datasetName:
      datasetName += "_2018"
    args = "processType={0} datasetName={1} conditionsJSON={2}".format(pid, datasetName, json)
    args = args.replace("processType=sig_vh", "processType=AUTO")
    return args

dsdefs = []

'''
these are useful when producing microaod from central miniaod

conds_dict = {
	"datasets_RunIISummer16.json" : "MetaData/data/MetaConditions/Era2016_RR-17Jul2018_v1.json",
	"datasets_RunIIFall17.json" : "MetaData/data/MetaConditions/Era2017_RR-31Mar2018_v1.json",
	"datasets_RunIIAutumn18.json" : "MetaData/data/MetaConditions/Era2018_RR-17Sep2018_v1.json", 
    "datasets_short.json" : "MetaData/data/MetaConditions/Era2017_RR-31Mar2018_v1.json",
    "datasets_RunIISummer16_22May2020.json" : "MetaData/data/MetaConditions/Era2016_RR-17Jul2018_v1.json",
    "datasets_RunIIFall17_22May2020.json" : "MetaData/data/MetaConditions/Era2017_RR-31Mar2018_v1.json",
    "datasets_RunIIAutumn18_22May2020.json" : "MetaData/data/MetaConditions/Era2018_RR-17Sep2018_v1.json"
}

job_jsons = ["datasets_RunIISummer16_22May2020.json", "datasets_RunIIFall17_22May2020.json", "datasets_RunIIAutumn18_22May2020.json"]

if not args.skip_central:
    for js in job_jsons:
        jobs = json.load(open(js))
        for pid in jobs["processes"]:
            fpo = jobs["processes"][pid]["filesPerOutput"]
            for ds in jobs["processes"][pid]["datasets"]:
                argus = getArgs(pid, ds, conds_dict[js])                
                print argus
                dsdefs.append((ds, fpo, argus))
'''
local_sets = []

if not args.skip_local:
    local_sets = [
        ("test_mking_nano", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggtautau_2018_20200930_v1_STEP4_v1/", 10, "")
    ]


total_summary = {}
while True:
    allcomplete = True

    # Loop through central samples
    #for ds,fpo,args in dsdefs[:]:
    #    
    #    sample = DBSSample( dataset=ds )
    #    print(ds, args)

    #    task = CondorTask(
    #            sample = sample,
    #            open_dataset = False,
    #            files_per_output = fpo,
    #            output_name = "test_skim.root" if DOSKIM else "myMicroAODOutputFile.root",
    #            tag = job_tag,
    #    		cmssw_version = cmssw_ver,
    #            executable = exec_path,
    #            tarfile = "empty",
    #            condor_submit_params = {"sites" : "T2_US_UCSD,T2_US_CALTECH,T2_US_MIT,T2_US_WISCONSIN,T2_US_Nebraska,T2_US_Purdue,T2_US_Vanderbilt,T2_US_Florida"},
    #            special_dir = hadoop_path,
    #            arguments = args.replace(" ","|")
    #            )
    #    task.process()
    #    allcomplete = allcomplete and task.complete()
    #    # save some information for the dashboard
    #    total_summary[ds] = task.get_task_summary()

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
                output_name = "test_nanoaod.root",
                tag = job_tag,
                cmssw_version = cmssw_ver,
                executable = exec_path,
                tarfile = "./package.tar.gz",
                condor_submit_params = {"sites" : "T2_US_UCSD"},
                special_dir = hadoop_path,
                arguments = args.replace(" ","|")
        )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary_nanoaod.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)


    # parse the total summary and write out the dashboard
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_nanoaod_fcnc/").do()
    os.system("chmod -R 755 ~/public_html/dump/metis_nanoaod_fcnc")
    if allcomplete:
        print ""
        print "Job={} finished".format(job_tag)
        print ""
        break
    print "Sleeping 1000 seconds ..."
    time.sleep(1000)
