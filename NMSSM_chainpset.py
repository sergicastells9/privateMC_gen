import os
from metis.CMSSWTask import CMSSWTask
from metis.Sample import DirectorySample, DummySample
from metis.Path import Path
from metis.StatsParser import StatsParser
import time

import sys
sys.path.append("/home/users/fsetti/public_html/privateMC_gen")
from update_pset_NMSSM import edit_pset_NMSSM

config = {
"cmssw_v_gen": "CMSSW_10_6_28_patch1",
"pset_gen": "HIG-RunIISummer20UL18wmLHEGEN-03461_1_cfg.py",
"scram_arch_gen": "slc7_amd64_gcc700",

"cmssw_v_sim": "CMSSW_10_6_17_patch1",
"pset_sim": "HIG-RunIISummer20UL18SIM-03039_1_cfg.py",
"scram_arch_sim": "slc7_amd64_gcc700",

"cmssw_v_mix": "CMSSW_10_6_17_patch1",
"pset_mix": "HIG-RunIISummer20UL18DIGIPremix-03020_1_cfg.py",
"scram_arch_mix": "slc7_amd64_gcc700",

"cmssw_v_hlt": "CMSSW_10_2_16_UL",
"pset_hlt": "HIG-RunIISummer20UL18HLT-03039_1_cfg.py",
"scram_arch_hlt": "slc7_amd64_gcc700",

"cmssw_v_reco": "CMSSW_10_6_17_patch1",
"pset_reco": "HIG-RunIISummer20UL18RECO-03039_1_cfg.py",
"scram_arch_reco": "slc7_amd64_gcc700",

"cmssw_v_miniaodsim": "CMSSW_10_6_20",
"pset_miniaodsim": "HIG-RunIISummer20UL18MiniAODv2-03039_1_cfg.py",
"scram_arch_miniaodsim": "slc7_amd64_gcc700",

"cmssw_v_nanoaodsim": "CMSSW_10_6_5",
"pset_nanoaodsim": "HIG-RunIISummer20UL18NanoAOD-00001_1_cfg.py",
"scram_arch_nanoaodsim": "slc7_amd64_gcc700"
}

cmssw_v_gen = config["cmssw_v_gen"] 
pset_gen = config["pset_gen"]
scram_arch_gen = config["scram_arch_gen"]

cmssw_v_sim = config["cmssw_v_sim"] 
pset_sim = config["pset_sim"]
scram_arch_sim = config["scram_arch_sim"]

cmssw_v_mix = config["cmssw_v_mix"] 
pset_mix = config["pset_mix"]
scram_arch_mix = config["scram_arch_mix"]

cmssw_v_hlt = config["cmssw_v_hlt"] 
pset_hlt = config["pset_hlt"]
scram_arch_hlt = config["scram_arch_hlt"]

cmssw_v_reco = config["cmssw_v_reco"] 
pset_reco = config["pset_reco"]
scram_arch_reco = config["scram_arch_reco"]

cmssw_v_miniaodsim = config["cmssw_v_miniaodsim"] 
pset_miniaodsim = config["pset_miniaodsim"]
scram_arch_miniaodsim = config["scram_arch_miniaodsim"]

cmssw_v_nanoaodsim = config["cmssw_v_nanoaodsim"] 
pset_nanoaodsim = config["pset_nanoaodsim"]
scram_arch_nanoaodsim = config["scram_arch_nanoaodsim"]

condor_submit_params={
        "sites": "SDSC-PRP,T2_US_UCSD,T2_US_CALTECH,T2_US_WISCONSIN,T2_US_Florida", # other_sites can be good_sites, your own list, etc.
        "classads": [
            ["RequestK8SNamespace", "cms-ucsd-t2"], 
            ["SingularityImage", "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7"]
        ],
        "requirements_line": 'requirements = (HAS_SINGULARITY=?=True) && (TARGET.K8SNamespace =!= "abc")',
				"use_xrootd":True
}

#condor_submit_params={
#        "sites": "T2_US_UCSD", # other_sites can be good_sites, your own list, etc.
#        "classads": [
#            ["SingularityImage", "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7"]
#        ],
#}
#condor_submit_params = {"sites" : "T2_US_UCSD,T2_US_CALTECH,T2_US_MIT,T2_US_WISCONSIN,T2_US_Nebraska,T2_US_Purdue,T2_US_Vanderbilt,T2_US_Florida",

#mx_values = [400]
#my_values = [70]

mx_values = [300,500,700,1000]
my_values = [70,90,100,125,150,200]

def runall(special_dir, total_nevents, events_per_output):

 for _ in range(2500):

  proc_tag = "v1"

  for mx in mx_values:
   for my in my_values:

    if mx == 300 and my == 200:
     continue

    #Start of Y_tautau_Hgg Section
    tag = 'NMSSM_XYH_Y_tautau_H_gg_MX_'+str(mx)+'_MY_'+str(my) 

    #for some reason the directories are not created in the script :( 
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP1_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP2_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP3_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP4_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP5_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP6_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP7_%s"%(special_dir,tag,proc_tag))

    edit_pset_NMSSM( tag  , 'NMSSM_XYH_Y_gg_H_tautau_MX_300_MY_100' )	

    step1 = CMSSWTask(
            # Change dataset to something more meaningful (but keep STEP1, as we use this 
            # for string replacement later); keep N=1
            sample = DummySample(N=1, dataset="/"+ tag+ "_STEP1"),
            # A unique identifier
            tag = proc_tag,
            special_dir = special_dir,
            # Probably want to beef up the below two numbers to control splitting,
            # but note that step2 is the bottleneck, so don't put too many events
            # in one output file here
            events_per_output = events_per_output,
            total_nevents = total_nevents,
            # We have one input dummy file, so this must be True
            split_within_files = True,
            pset = "cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg_" + tag + ".py",
            additional_input_files = [ "/hadoop/cms/store/user/fsetti/IC_gridpacks/"+ tag + "_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz" ],
            cmssw_version = cmssw_v_gen,
            scram_arch = scram_arch_gen,
            condor_submit_params =  condor_submit_params
           )

    step2 = CMSSWTask(
            sample = DirectorySample(
                location = step1.get_outputdir(),
                dataset = step1.get_sample().get_datasetname().replace("STEP1","STEP2"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            pset = "cmsDrivers/NMSSM/" + pset_sim,
            cmssw_version = cmssw_v_sim,
            scram_arch = scram_arch_sim,
            condor_submit_params =  condor_submit_params
            )

    step3 = CMSSWTask(
            sample = DirectorySample(
                location = step2.get_outputdir(),
                dataset = step2.get_sample().get_datasetname().replace("STEP2","STEP3"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            pset = "cmsDrivers/NMSSM/" + pset_mix,
            cmssw_version = cmssw_v_mix,
            scram_arch = scram_arch_mix,
            condor_submit_params =  condor_submit_params
            )

    step4 = CMSSWTask(
            sample = DirectorySample(
                location = step3.get_outputdir(),
                dataset = step3.get_sample().get_datasetname().replace("STEP3","STEP4"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            #files_per_output = 1,
            files_per_output = 2,
            #output_name = "step4.root",
            pset = "cmsDrivers/NMSSM/" + pset_hlt,
            cmssw_version = cmssw_v_hlt,
            scram_arch = scram_arch_hlt,
            condor_submit_params =  condor_submit_params
            )

    step5 = CMSSWTask(
            sample = DirectorySample(
                location = step4.get_outputdir(),
                dataset = step4.get_sample().get_datasetname().replace("STEP4","STEP5"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            #files_per_output = 1,
            files_per_output = 2,
            pset = "cmsDrivers/NMSSM/" + pset_reco,
            cmssw_version = cmssw_v_reco,
            scram_arch = scram_arch_reco,
            condor_submit_params =  condor_submit_params
            )

    step6 = CMSSWTask(
            sample = DirectorySample(
                location = step5.get_outputdir(),
                dataset = step5.get_sample().get_datasetname().replace("STEP5","STEP6"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            #files_per_output = 1,
            files_per_output = 2,
            #output_name = "step6.root",
            pset = "cmsDrivers/NMSSM/" + pset_miniaodsim,
            cmssw_version = cmssw_v_miniaodsim,
            scram_arch = scram_arch_miniaodsim,
            condor_submit_params =  condor_submit_params
            )

    step7 = CMSSWTask(
            sample = DirectorySample(
                location = step6.get_outputdir(),
                dataset = step6.get_sample().get_datasetname().replace("STEP6","STEP7"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            #output_name = "step7.root",
            pset = "cmsDrivers/NMSSM/" + pset_nanoaodsim,
            cmssw_version = cmssw_v_nanoaodsim,
            scram_arch = scram_arch_nanoaodsim,
            condor_submit_params =  condor_submit_params
            )
    #End of Y_tautau_Hgg Section


    #Start of Y_gg_Htautau Section
    tag = 'NMSSM_XYH_Y_gg_H_tautau_MX_'+str(mx)+'_MY_'+str(my) 

    #for some reason the directories are not created in the script :( 
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP1_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP2_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP3_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP4_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP5_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP6_%s"%(special_dir,tag,proc_tag))
    os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP7_%s"%(special_dir,tag,proc_tag))

    edit_pset_NMSSM( tag  , 'NMSSM_XYH_Y_gg_H_tautau_MX_300_MY_100' )	

    step_1 = CMSSWTask(
            # Change dataset to something more meaningful (but keep STEP1, as we use this 
            # for string replacement later); keep N=1
            sample = DummySample(N=1, dataset="/"+ tag+ "_STEP1"),
            # A unique identifier
            tag = proc_tag,
            special_dir = special_dir,
            # Probably want to beef up the below two numbers to control splitting,
            # but note that step2 is the bottleneck, so don't put too many events
            # in one output file here
            events_per_output = events_per_output,
            total_nevents = total_nevents,
            # We have one input dummy file, so this must be True
            split_within_files = True,
            pset = "cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg_" + tag + ".py",
            additional_input_files = [ "/hadoop/cms/store/user/fsetti/IC_gridpacks/"+ tag + "_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz" ],
            cmssw_version = cmssw_v_gen,
            scram_arch = scram_arch_gen,
            condor_submit_params =  condor_submit_params
            )

    step_2 = CMSSWTask(
            sample = DirectorySample(
                location = step_1.get_outputdir(),
                dataset = step_1.get_sample().get_datasetname().replace("STEP1","STEP2"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            pset = "cmsDrivers/NMSSM/" + pset_sim,
            cmssw_version = cmssw_v_sim,
            scram_arch = scram_arch_sim,
            condor_submit_params =  condor_submit_params
            )

    step_3 = CMSSWTask(
            sample = DirectorySample(
                location = step_2.get_outputdir(),
                dataset = step_2.get_sample().get_datasetname().replace("STEP2","STEP3"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            pset = "cmsDrivers/NMSSM/" + pset_mix,
            cmssw_version = cmssw_v_mix,
            scram_arch = scram_arch_mix,
            condor_submit_params =  condor_submit_params
            )

    step_4 = CMSSWTask(
            sample = DirectorySample(
                location = step_3.get_outputdir(),
                dataset = step_3.get_sample().get_datasetname().replace("STEP3","STEP4"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 2,
            #files_per_output = 1,
            #output_name = "step4.root",
            pset = "cmsDrivers/NMSSM/" + pset_hlt,
            cmssw_version = cmssw_v_hlt,
            scram_arch = scram_arch_hlt,
            condor_submit_params =  condor_submit_params
            )

    step_5 = CMSSWTask(
            sample = DirectorySample(
                location = step_4.get_outputdir(),
                dataset = step_4.get_sample().get_datasetname().replace("STEP4","STEP5"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 2,
            #files_per_output = 1,
            pset = "cmsDrivers/NMSSM/" + pset_reco,
            cmssw_version = cmssw_v_reco,
            scram_arch = scram_arch_reco,
            condor_submit_params =  condor_submit_params
            )

    step_6 = CMSSWTask(
            sample = DirectorySample(
                location = step_5.get_outputdir(),
                dataset = step_5.get_sample().get_datasetname().replace("STEP5","STEP6"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 2,
            #files_per_output = 1,
            #output_name = "step6.root",
            pset = "cmsDrivers/NMSSM/" + pset_miniaodsim,
            cmssw_version = cmssw_v_miniaodsim,
            scram_arch = scram_arch_miniaodsim,
            condor_submit_params =  condor_submit_params
            )

    step_7 = CMSSWTask(
            sample = DirectorySample(
                location = step_6.get_outputdir(),
                dataset = step_6.get_sample().get_datasetname().replace("STEP6","STEP7"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            #output_name = "step7.root",
            pset = "cmsDrivers/NMSSM/" + pset_nanoaodsim,
            cmssw_version = cmssw_v_nanoaodsim,
            scram_arch = scram_arch_nanoaodsim,
            condor_submit_params =  condor_submit_params
            )

    total_summary = {}
    #for task in [step1,step2,step3,step4,step5,step6,step7]:
    for task in [step1,step2,step3,step4,step5,step6,step7,step_1,step_2,step_3,step_4,step_5,step_6,step_7]:
        task.process()
        summary = task.get_task_summary()
        total_summary[task.get_sample().get_datasetname()] = summary
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis/").do()

 

  time.sleep(90*60)


runall("nanoAOD_runII_UL", 250000, 250)
#runall("nanoAOD_runII_UL_test", 400000, 250)
