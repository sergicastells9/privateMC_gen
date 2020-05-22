from metis.CMSSWTask import CMSSWTask
from metis.Sample import DirectorySample, DummySample
from metis.Path import Path
from metis.StatsParser import StatsParser
import time


for _ in range(25):

    proc_tag = "v3"
    special_dir = "workflowtest/ProjectMetis"
    step1 = CMSSWTask(
            # Change dataset to something more meaningful (but keep STEP1, as we use this 
            # for string replacement later); keep N=1
            sample = DummySample(N=1, dataset="/test/ttHH_v2/STEP1"),
            # A unique identifier
            tag = proc_tag,
            special_dir = special_dir,
            # Probably want to beef up the below two numbers to control splitting,
            # but note that step2 is the bottleneck, so don't put too many events
            # in one output file here
            events_per_output = 50,
            total_nevents = 1000,
            # We have one input dummy file, so this must be True
            split_within_files = True,
            pset = "psets/TOP-RunIIFall17wmLHEGS-00072_1_cfg.py",
            cmssw_version = "CMSSW_9_3_4",
            scram_arch = "slc6_amd64_gcc630",
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
            pset = "psets/TOP-RunIIFall17DRPremix-00159_1_cfg.py",
            cmssw_version = "CMSSW_9_4_0",
            scram_arch = "slc6_amd64_gcc630",
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
            pset = "psets/TOP-RunIIFall17DRPremix-00159_2_cfg.py",
            cmssw_version = "CMSSW_9_4_0",
            scram_arch = "slc6_amd64_gcc630",
            )

    step4 = CMSSWTask(
            sample = DirectorySample(
                location = step3.get_outputdir(),
                dataset = step3.get_sample().get_datasetname().replace("STEP3","STEP4"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            pset = "psets/TOP-RunIIFall17MiniAODv2-00217_1_cfg.py",
            # The below two lines should match output file names in the pset
            output_name = "step4.root",
            #other_outputs = ["step3_inMINIAODSIM.root","step3_inDQM.root"],
            cmssw_version = "CMSSW_9_4_6",
            scram_arch = "slc6_amd64_gcc630",
            # condor_submit_params = {"sites":"UAF,UCSD"},
            )

    step5 = CMSSWTask(
            sample = DirectorySample(
                location = step4.get_outputdir(),
                dataset = step4.get_sample().get_datasetname().replace("STEP4","STEP5"),
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            files_per_output = 1,
            pset = "psets/TOP-RunIIFall17NanoAODv7-00001_1_cfg.py",
            # The below two lines should match output file names in the pset
            output_name = "step5.root",
            #other_outputs = ["step3_inMINIAODSIM.root","step3_inDQM.root"],
            cmssw_version = "CMSSW_10_2_22",
            scram_arch = "slc6_amd64_gcc700",
            # condor_submit_params = {"sites":"UAF,UCSD"},
            )

    '''step4 = CMSSWTask(
            sample = DirectorySample(
                location = step3.get_outputdir(),
                dataset = step3.get_sample().get_datasetname().replace("STEP3","STEP4"),
                globber = "*inDQM*.root",
                ),
            tag = proc_tag,
            special_dir = special_dir,
            open_dataset = True,
            # Can probably increase this, as DQM is fast to run
            files_per_output = 1,
            pset = "psets/step4.py",
            # The pset doesn't actually have an output file, but the below name
            # is what ends up getting output anyway
            output_name = "DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root",
            cmssw_version = "CMSSW_10_0_0_pre1",
            scram_arch = "slc6_amd64_gcc630",
            # DQM outputs hists, not trees, so don't crash if we expect trees
            # and also use different executable that doesn't do various checks
            is_tree_output = False,
            executable = "ProjectMetis/metis/executables/condor_cmssw_exe_nocheck.sh",
            # condor_submit_params = {"sites":"UAF,UCSD"},
            )
    '''

    #for _ in range(25):
    total_summary = {}
    for task in [step1,step2,step3,step4,step5]:
        task.process()
        summary = task.get_task_summary()
        total_summary[task.get_sample().get_datasetname()] = summary
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis/").do()
    time.sleep(600)
