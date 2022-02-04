import os
from metis.CMSSWTask import CMSSWTask
from metis.Sample import DirectorySample, DummySample
from metis.Path import Path
from metis.StatsParser import StatsParser
import time

import sys
sys.path.append("/home/users/fsetti/public_html/privateMC_gen")
from update_pset_NMSSM import edit_pset_NMSSM, edit_pset_gghh, edit_pset_gghh_WW
from allconfig import *

years = ['2016', '2016_APV', '2017', '2018' ]

condor_submit_params={
        #"sites": "SDSC-PRP", # other_sites can be good_sites, your own list, etc.
        "sites": "T2_US_UCSD,T2_US_CALTECH,T2_US_MIT,T2_US_WISCONSIN,T2_US_Vanderbilt,T2_US_Florida", # other_sites can be good_sites, your own list, etc.
        "classads": [
            ["RequestK8SNamespace", "cms-ucsd-t2"], 
            ["SingularityImage", "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7"]
        ],
        #"requirements_line": 'requirements = (HasSingularity==True)',
        "requirements_line": 'requirements = (HAS_SINGULARITY=?=True) && (TARGET.K8SNamespace =!= "abc")',
				#"use_xrootd":True
}

#condor_submit_params = {"sites" : "T2_US_UCSD,T2_US_CALTECH,T2_US_MIT,T2_US_WISCONSIN,T2_US_Nebraska,T2_US_Purdue,T2_US_Vanderbilt,T2_US_Florida",

couplings = [ 'cHHH0' , 'cHHH1' , 'cHHH2p45' , 'cHHH5' ]
decays = [ 'dileptonic' , 'semileptonic' ]
procs = [ "DiPhotonJetsBox_MGG_80toInf", "DiPhotonJetsBox1BJet_MGG_80toInf", "DiPhotonJetsBox_M40_80" ]

def runall(special_dir, total_nevents, events_per_output):

	for _ in range(2500):

		proc_tag = "v1"

		for proc in missing_UL_bkgs.keys():
			for year in years:

				#still to figure out how to start production from miniAOD
				if proc == 'GJets_HT_600ToInf_TuneCP5_13TeV_madgraphMLM_pythia8' or proc == 'GJets_HT_400To600_TuneCP5_13TeV_madgraphMLM_pythia8':
					continue

				tag = str(proc) + "_" + year
				total_nevents_tmp = total_nevents				
				steps = []

				if '2016' in year:
					total_nevents_tmp /= 2

				try:
					cmssw_v_gen = missing_UL_bkgs[proc][year]["cmssw_v_gen"] 
					pset_gen = missing_UL_bkgs[proc][year]["pset_gen"]
					scram_arch_gen = missing_UL_bkgs[proc][year]["scram_arch_gen"]
					
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP1_%s"%(special_dir,tag,proc_tag))
				
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
					        total_nevents = total_nevents_tmp,
					        # We have one input dummy file, so this must be True
					        split_within_files = True,
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_gen,
					        cmssw_version = cmssw_v_gen,
					        scram_arch = scram_arch_gen,
					        condor_submit_params =  condor_submit_params
					       )
					steps += [ step1 ]

				except:
					print("Could not process STEP1 for: " + proc + " for " + year )


				try:
					cmssw_v_sim = missing_UL_bkgs[proc][year]["cmssw_v_sim"] 
					pset_sim = missing_UL_bkgs[proc][year]["pset_sim"]
					scram_arch_sim = missing_UL_bkgs[proc][year]["scram_arch_sim"]
					
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP2_%s"%(special_dir,tag,proc_tag))
				
					step2 = CMSSWTask(
					        sample = DirectorySample(
					            location = step1.get_outputdir(),
					            dataset = step1.get_sample().get_datasetname().replace("STEP1","STEP2"),
					            ),
					        tag = proc_tag,
					        special_dir = special_dir,
					        open_dataset = True,
					        files_per_output = 1,
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_sim,
					        cmssw_version = cmssw_v_sim,
					        scram_arch = scram_arch_sim,
					        condor_submit_params =  condor_submit_params
					        )
					steps += [ step2 ]

				except:
					print("Could not process STEP2 for: " + proc + " for " + year )

				try:
					cmssw_v_mix = missing_UL_bkgs[proc][year]["cmssw_v_mix"] 
					pset_mix = missing_UL_bkgs[proc][year]["pset_mix"]
					scram_arch_mix = missing_UL_bkgs[proc][year]["scram_arch_mix"]
					
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP3_%s"%(special_dir,tag,proc_tag))
				
					step3 = CMSSWTask(
					        sample = DirectorySample(
					            location = step2.get_outputdir(),
					            dataset = step2.get_sample().get_datasetname().replace("STEP2","STEP3"),
					            ),
					        tag = proc_tag,
					        special_dir = special_dir,
					        open_dataset = True,
					        files_per_output = 1,
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_mix,
					        cmssw_version = cmssw_v_mix,
					        scram_arch = scram_arch_mix,
					        condor_submit_params =  condor_submit_params
					        )
					steps += [ step3 ]

				except:
					print("Could not process STEP3 for: " + proc + " for " + year )

				try:
					cmssw_v_hlt = missing_UL_bkgs[proc][year]["cmssw_v_hlt"] 
					pset_hlt = missing_UL_bkgs[proc][year]["pset_hlt"]
					scram_arch_hlt = missing_UL_bkgs[proc][year]["scram_arch_hlt"]
					
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP4_%s"%(special_dir,tag,proc_tag))
				
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
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_hlt,
					        cmssw_version = cmssw_v_hlt,
					        scram_arch = scram_arch_hlt,
					        condor_submit_params =  condor_submit_params
					        )

					steps += [ step4 ]

				except:
					print("Could not process STEP4 for: " + proc + " for " + year )

				try:
					cmssw_v_reco = missing_UL_bkgs[proc][year]["cmssw_v_reco"] 
					pset_reco = missing_UL_bkgs[proc][year]["pset_reco"]
					scram_arch_reco = missing_UL_bkgs[proc][year]["scram_arch_reco"]
					
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP5_%s"%(special_dir,tag,proc_tag))
				
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
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_reco,
					        cmssw_version = cmssw_v_reco,
					        scram_arch = scram_arch_reco,
					        condor_submit_params =  condor_submit_params
					        )

					steps += [ step5 ]

				except:
					print("Could not process STEP5 for: " + proc + " for " + year )

				try:
					cmssw_v_miniaodsim = missing_UL_bkgs[proc][year]["cmssw_v_miniaodsim"] 
					pset_miniaodsim = missing_UL_bkgs[proc][year]["pset_miniaodsim"]
					scram_arch_miniaodsim = missing_UL_bkgs[proc][year]["scram_arch_miniaodsim"]

					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP6_%s"%(special_dir,tag,proc_tag))
				
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
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_miniaodsim,
					        cmssw_version = cmssw_v_miniaodsim,
					        scram_arch = scram_arch_miniaodsim,
					        condor_submit_params =  condor_submit_params
					        )

					steps += [ step6 ]

				except:
					print("Could not process STEP6 for: " + proc + " for " + year )

				try:					
					cmssw_v_nanoaodsim = missing_UL_bkgs[proc][year]["cmssw_v_nanoaodsim"] 
					pset_nanoaodsim = missing_UL_bkgs[proc][year]["pset_nanoaodsim"]
					scram_arch_nanoaodsim = missing_UL_bkgs[proc][year]["scram_arch_nanoaodsim"]

					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP7_%s"%(special_dir,tag,proc_tag))
				
					step7 = CMSSWTask(
					        sample = DirectorySample(
					            location = step6.get_outputdir(),
					            dataset = step6.get_sample().get_datasetname().replace("STEP6","STEP7"),
					            ),
					        tag = proc_tag,
					        special_dir = special_dir,
					        open_dataset = True,
					        #files_per_output = 1,
					        files_per_output = 2,
					        #output_name = "step7.root",
					        pset = "cmsDrivers/UL20/"+proc+"/" + pset_nanoaodsim,
					        cmssw_version = cmssw_v_nanoaodsim,
					        scram_arch = scram_arch_nanoaodsim,
					        condor_submit_params =  condor_submit_params
					        )

					steps += [ step7 ]

				except:
					print("Could not process STEP7 for: " + proc + " for " + year )
					
				total_summary = {}
				for task in steps:
				    task.process()
				    summary = task.get_task_summary()
				    total_summary[task.get_sample().get_datasetname()] = summary
				StatsParser(data=total_summary, webdir="~/public_html/dump/metis/").do()    


		for coupling in couplings:
			for year in years:
			
				cmssw_v_gen = signal_UL20[year]["cmssw_v_gen"] 
				pset_gen = signal_UL20[year]["pset_gen"]
				pset_gen.replace('_1_cfg.py','_1_cfg_%s.py'%(coupling))
				scram_arch_gen = signal_UL20[year]["scram_arch_gen"]
				
				cmssw_v_sim = signal_UL20[year]["cmssw_v_sim"] 
				pset_sim = signal_UL20[year]["pset_sim"]
				scram_arch_sim = signal_UL20[year]["scram_arch_sim"]
				
				cmssw_v_mix = signal_UL20[year]["cmssw_v_mix"] 
				pset_mix = signal_UL20[year]["pset_mix"]
				scram_arch_mix = signal_UL20[year]["scram_arch_mix"]
				
				cmssw_v_hlt = signal_UL20[year]["cmssw_v_hlt"] 
				pset_hlt = signal_UL20[year]["pset_hlt"]
				scram_arch_hlt = signal_UL20[year]["scram_arch_hlt"]
				
				cmssw_v_reco = signal_UL20[year]["cmssw_v_reco"] 
				pset_reco = signal_UL20[year]["pset_reco"]
				scram_arch_reco = signal_UL20[year]["scram_arch_reco"]
				
				cmssw_v_miniaodsim = signal_UL20[year]["cmssw_v_miniaodsim"] 
				pset_miniaodsim = signal_UL20[year]["pset_miniaodsim"]
				scram_arch_miniaodsim = signal_UL20[year]["scram_arch_miniaodsim"]
				
				cmssw_v_nanoaodsim = signal_UL20[year]["cmssw_v_nanoaodsim"] 
				pset_nanoaodsim = signal_UL20[year]["pset_nanoaodsim"]
				scram_arch_nanoaodsim = signal_UL20[year]["scram_arch_nanoaodsim"]
				
				#Start of Y_tautau_Hgg Section
				tag = 'GluGluToHHTo2G2Tau_node_' + coupling + '_TuneCP5_13TeV-powheg-pythia8_' + year
				
				#for some reason the directories are not created in the script :( 
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP1_%s"%(special_dir,tag,proc_tag))
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP2_%s"%(special_dir,tag,proc_tag))
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP3_%s"%(special_dir,tag,proc_tag))
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP4_%s"%(special_dir,tag,proc_tag))
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP5_%s"%(special_dir,tag,proc_tag))
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP6_%s"%(special_dir,tag,proc_tag))
				os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP7_%s"%(special_dir,tag,proc_tag))
				
				edit_pset_gghh( coupling, 'cHHH1' , year  )	
				
				total_nevents_tmp = total_nevents
				
				if '2016' in year:
					total_nevents_tmp /= 2
				
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
				        total_nevents = total_nevents_tmp,
				        # We have one input dummy file, so this must be True
				        split_within_files = True,
				        pset = "cmsDrivers/UL20/ggf/" + pset_gen,
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
				        pset = "cmsDrivers/UL20/ggf/" + pset_sim,
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
				        pset = "cmsDrivers/UL20/ggf/" + pset_mix,
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
				        pset = "cmsDrivers/UL20/ggf/" + pset_hlt,
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
				        pset = "cmsDrivers/UL20/ggf/" + pset_reco,
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
				        pset = "cmsDrivers/UL20/ggf/" + pset_miniaodsim,
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
				        files_per_output = 2,
				        #output_name = "step7.root",
				        pset = "cmsDrivers/UL20/ggf/" + pset_nanoaodsim,
				        cmssw_version = cmssw_v_nanoaodsim,
				        scram_arch = scram_arch_nanoaodsim,
				        condor_submit_params =  condor_submit_params
				        )
				
				total_summary = {}
				for task in [step1,step2,step3,step4,step5,step6,step7]:
				    task.process()
				    summary = task.get_task_summary()
				    total_summary[task.get_sample().get_datasetname()] = summary
				StatsParser(data=total_summary, webdir="~/public_html/dump/metis/").do()    


			#Start of HH->ggWW dileptonic & semileptonic
			for decay in decays:
				for year in years:
	
					cmssw_v_gen = signal_UL20[year]["cmssw_v_gen"] 
					pset_gen = signal_UL20[year]["pset_gen"]
					pset_gen.replace('_1_cfg.py','_1_cfg_%s.py'%(coupling))
					scram_arch_gen = signal_UL20[year]["scram_arch_gen"]
					
					cmssw_v_sim = signal_UL20[year]["cmssw_v_sim"] 
					pset_sim = signal_UL20[year]["pset_sim"]
					scram_arch_sim = signal_UL20[year]["scram_arch_sim"]
					
					cmssw_v_mix = signal_UL20[year]["cmssw_v_mix"] 
					pset_mix = signal_UL20[year]["pset_mix"]
					scram_arch_mix = signal_UL20[year]["scram_arch_mix"]
					
					cmssw_v_hlt = signal_UL20[year]["cmssw_v_hlt"] 
					pset_hlt = signal_UL20[year]["pset_hlt"]
					scram_arch_hlt = signal_UL20[year]["scram_arch_hlt"]
					
					cmssw_v_reco = signal_UL20[year]["cmssw_v_reco"] 
					pset_reco = signal_UL20[year]["pset_reco"]
					scram_arch_reco = signal_UL20[year]["scram_arch_reco"]
					
					cmssw_v_miniaodsim = signal_UL20[year]["cmssw_v_miniaodsim"] 
					pset_miniaodsim = signal_UL20[year]["pset_miniaodsim"]
					scram_arch_miniaodsim = signal_UL20[year]["scram_arch_miniaodsim"]
					
					cmssw_v_nanoaodsim = signal_UL20[year]["cmssw_v_nanoaodsim"] 
					pset_nanoaodsim = signal_UL20[year]["pset_nanoaodsim"]
					scram_arch_nanoaodsim = signal_UL20[year]["scram_arch_nanoaodsim"]
					
					edit_pset_gghh_WW( coupling, 'cHHH1' , year, decay  )	

					tag = ''					
					if coupling == 'cHHH1':
						tag = 'GluGluToHHTo2G2W_' + decay + '_node_SM_'+ year
					else :
						tag = 'GluGluToHHTo2G2W_' + decay + '_node_' + str(coupling) + '_'+ year
					
					#for some reason the directories are not created in the script :( 
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP1_%s"%(special_dir,tag,proc_tag))
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP2_%s"%(special_dir,tag,proc_tag))
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP3_%s"%(special_dir,tag,proc_tag))
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP4_%s"%(special_dir,tag,proc_tag))
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP5_%s"%(special_dir,tag,proc_tag))
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP6_%s"%(special_dir,tag,proc_tag))
					os.system("mkdir -p /hadoop/cms/store/user/fsetti/%s/%s_STEP7_%s"%(special_dir,tag,proc_tag))
					
					total_nevents_tmp = total_nevents
					
					if '2016' in year:
						total_nevents_tmp /= 2
					
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
					        total_nevents = total_nevents_tmp,
					        # We have one input dummy file, so this must be True
					        split_within_files = True,
					        pset = "cmsDrivers/UL20/HHTo2G2l2nu/"+decay+"/" + pset_gen,
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
					        pset = "cmsDrivers/UL20/ggf/" + pset_sim,
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
					        pset = "cmsDrivers/UL20/ggf/" + pset_mix,
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
					        pset = "cmsDrivers/UL20/ggf/" + pset_hlt,
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
					        pset = "cmsDrivers/UL20/ggf/" + pset_reco,
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
					        pset = "cmsDrivers/UL20/ggf/" + pset_miniaodsim,
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
					        files_per_output = 2,
					        #output_name = "step7.root",
					        pset = "cmsDrivers/UL20/ggf/" + pset_nanoaodsim,
					        cmssw_version = cmssw_v_nanoaodsim,
					        scram_arch = scram_arch_nanoaodsim,
					        condor_submit_params =  condor_submit_params
					        )
					
					total_summary = {}
					for task in [step1,step2,step3,step4,step5,step6,step7]:
					#for task in [step1,step2,step3,step4,step5,step6]:
					    task.process()
					    summary = task.get_task_summary()
					    total_summary[task.get_sample().get_datasetname()] = summary
					StatsParser(data=total_summary, webdir="~/public_html/dump/metis/").do()
 

		time.sleep(5*60)


runall("nanoAOD_runII_20UL", 400000, 250)
#runall("nanoAOD_runII_20UL_test", 10000, 250)
