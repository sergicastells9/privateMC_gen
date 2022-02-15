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

from dsdefs_centralminiaod_UL import dsdefs_data
# for local inputs
local_sets = []


if not args.skip_local:
 	local_sets = [
		("DiPhotonJetsBox1BJet_MGG_80toInf_2016_APV"																						, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/DiPhotonJetsBox1BJet_MGG_80toInf_2016_APV_STEP6_v1/"																			, 10, "2016_APV_MC"),
		("DiPhotonJetsBox_M40_80_2016_APV"																											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/DiPhotonJetsBox_M40_80_2016_APV_STEP6_v1/"																								, 10, "2016_APV_MC"),
		("DiPhotonJetsBox_M40_80_2016"																													, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/DiPhotonJetsBox_M40_80_2016_STEP6_v1/"																										, 10, "2016_MC"),
		("DiPhotonJetsBox_MGG_80toInf_2016_APV"																									, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/DiPhotonJetsBox_MGG_80toInf_2016_APV_STEP6_v1/"																						, 10, "2016_APV_MC"),
		("GJets_DoubleEMEnriched_PtG_20MGG_40To80_TuneCP5_13TeV_madgraphMLM_pythia8_2016_APV"		, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GJets_DoubleEMEnriched_PtG_20MGG_40To80_TuneCP5_13TeV_madgraphMLM_pythia8_2016_APV_STEP6_v1/", 10, "2016_APV_MC"),
		("GJets_DoubleEMEnriched_PtG_20MGG_40To80_TuneCP5_13TeV_madgraphMLM_pythia8_2016"				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GJets_DoubleEMEnriched_PtG_20MGG_40To80_TuneCP5_13TeV_madgraphMLM_pythia8_2016_STEP6_v1/"	, 10, "2016_MC"),
		("GJets_DoubleEMEnriched_PtG_40MGG_80_TuneCP5_13TeV_madgraphMLM_pythia8_2016_APV"				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GJets_DoubleEMEnriched_PtG_40MGG_80_TuneCP5_13TeV_madgraphMLM_pythia8_2016_APV_STEP6_v1/"	, 10, "2016_APV_MC"),
		("GJets_DoubleEMEnriched_PtG_40MGG_80_TuneCP5_13TeV_madgraphMLM_pythia8_2016"						, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GJets_DoubleEMEnriched_PtG_40MGG_80_TuneCP5_13TeV_madgraphMLM_pythia8_2016_STEP6_v1/"			, 10, "2016_MC"),
		("TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8_2016"																		, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8_2016_STEP6_v1/"											, 10, "2016_MC"),
		
		("GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2016_APV"									, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2016_APV_STEP6_v1/"		, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2016"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2016_STEP6_v1/"				, 10, "2016_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2017"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2017_STEP6_v1/"				, 10, "2017_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2018"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH0_TuneCP5_13TeV-powheg-pythia8_2018_STEP6_v1/"				, 10, "2018_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2016_APV"									, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2016_APV_STEP6_v1/"		, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2016"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2016_STEP6_v1/"				, 10, "2016_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2017"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2017_STEP6_v1/"				, 10, "2017_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2018"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH1_TuneCP5_13TeV-powheg-pythia8_2018_STEP6_v1/"				, 10, "2018_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2016_APV"								, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2016_APV_STEP6_v1/"	, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2016"										, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2016_STEP6_v1/"			, 10, "2016_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2017"										, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2017_STEP6_v1/"			, 10, "2017_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2018"										, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH2p45_TuneCP5_13TeV-powheg-pythia8_2018_STEP6_v1/"			, 10, "2018_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2016_APV"									, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2016_APV_STEP6_v1/"		, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2016"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2016_STEP6_v1/"				, 10, "2016_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2017"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2017_STEP6_v1/"				, 10, "2017_MC"),
		("GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2018"											, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH5_TuneCP5_13TeV-powheg-pythia8_2018_STEP6_v1/"				, 10, "2018_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH0_2016_APV"																			, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH0_2016_APV_STEP6_v1/"												, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH0_2016"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH0_2016_STEP6_v1/"														, 10, "2016_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH0_2017"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH0_2017_STEP6_v1/"														, 10, "2017_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH0_2018"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH0_2018_STEP6_v1/"														, 10, "2018_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_SM_2016_APV"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_SM_2016_APV_STEP6_v1/"														, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_SM_2016"																							, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_SM_2016_STEP6_v1/"																, 10, "2016_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_SM_2017"																							, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_SM_2017_STEP6_v1/"																, 10, "2017_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_SM_2018"																							, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_SM_2018_STEP6_v1/"																, 10, "2018_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2016_APV"																		, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2016_APV_STEP6_v1/"											, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2016"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2016_STEP6_v1/"													, 10, "2016_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2017"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2017_STEP6_v1/"													, 10, "2017_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2018"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH2p45_2018_STEP6_v1/"													, 10, "2018_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH5_2016_APV"																			, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH5_2016_APV_STEP6_v1/"												, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH5_2016"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH5_2016_STEP6_v1/"														, 10, "2016_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH5_2017"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH5_2017_STEP6_v1/"														, 10, "2017_MC"),
		("GluGluToHHTo2G2W_dileptonic_node_cHHH5_2018"																					, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_dileptonic_node_cHHH5_2018_STEP6_v1/"														, 10, "2018_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH0_2016_APV"																		, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH0_2016_APV_STEP6_v1/"											, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH0_2016"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH0_2016_STEP6_v1/"													, 10, "2016_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH0_2017"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH0_2017_STEP6_v1/"													, 10, "2017_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH0_2018"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH0_2018_STEP6_v1/"													, 10, "2018_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_SM_2016_APV"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_SM_2016_APV_STEP6_v1/"													, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_SM_2016"																						, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_SM_2016_STEP6_v1/"															, 10, "2016_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_SM_2017"																						, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_SM_2017_STEP6_v1/"															, 10, "2017_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_SM_2018"																						, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_SM_2018_STEP6_v1/"															, 10, "2018_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2016_APV"																	, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2016_APV_STEP6_v1/"										, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2016"																			, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2016_STEP6_v1/"												, 10, "2016_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2017"																			, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2017_STEP6_v1/"												, 10, "2017_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2018"																			, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH2p45_2018_STEP6_v1/"												, 10, "2018_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH5_2016_APV"																		, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH5_2016_APV_STEP6_v1/"											, 10, "2016_APV_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH5_2016"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH5_2016_STEP6_v1/"													, 10, "2016_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH5_2017"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH5_2017_STEP6_v1/"													, 10, "2017_MC"),
		("GluGluToHHTo2G2W_semileptonic_node_cHHH5_2018"																				, "/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_semileptonic_node_cHHH5_2018_STEP6_v1/"													, 10, "2018_MC"),
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
exec_path = "condor_exe.sh"
#tar_path = "nanoAOD_package_%s.tar.gz" % args.tag

if not args.soft_rerun:
#    os.system("rm -rf tasks/*" + args.tag + "*")
    os.system("rm package.tar.gz")
    os.system("XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s" % cmssw_ver)

total_summary = {}
while True:
    allcomplete = True

    # Loop through central samples
    for ds,fpo,args in dsdefs_data[:]:
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
                condor_submit_params = {"sites": "T2_US_UCSD,T2_US_CALTECH,T2_US_WISCONSIN,T2_US_Vanderbilt,T2_US_Florida", # other_sites can be good_sites, your own list, etc.
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]],
										"use_xrootd":True},
                special_dir = hadoop_path,
                arguments = args.replace(" ","|")
                )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)

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
                condor_submit_params = {"sites": "T2_US_UCSD,T2_US_CALTECH,T2_US_WISCONSIN,T2_US_Florida", # other_sites can be good_sites, your own list, etc.
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]]},
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
    print "Sleeping 30 minutes ..."
    time.sleep(60*60)
