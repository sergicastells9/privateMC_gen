
universe=Vanilla
+DESIRED_Sites="SDSC-PRP,T2_US_UCSD,T2_US_CALTECH,T2_US_WISCONSIN,T2_US_Florida"
RequestMemory = 2048
RequestCpus = 1
executable=tasks/CMSSWTask_NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1/executable.sh
transfer_executable=True
transfer_input_files=/home/users/fsetti/public_html/privateMC_gen/tasks/CMSSWTask_NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1/pset.py,/hadoop/cms/store/user/fsetti/IC_gridpacks/NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
transfer_output_files = ""
+Owner = undefined
+project_Name = "cmssurfandturf"
log=/home/users/fsetti/public_html/privateMC_gen/tasks/CMSSWTask_NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1/logs/1638498698.log
output=/home/users/fsetti/public_html/privateMC_gen/tasks/CMSSWTask_NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1/logs/std_logs/1e.$(Cluster).$(Process).out
error=/home/users/fsetti/public_html/privateMC_gen/tasks/CMSSWTask_NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1/logs/std_logs/1e.$(Cluster).$(Process).err
notification=Never
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
x509userproxy=/tmp/x509up_u31704
use_x509userproxy = True
requirements = (HAS_SINGULARITY=?=True) && (TARGET.K8SNamespace =!= "abc")
+RequestK8SNamespace="cms-ucsd-t2"
+SingularityImage="/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7"

arguments=/hadoop/cms/store/user/fsetti/nanoAOD_runII_UL/NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1/ output dummyfile 1 pset.py CMSSW_10_6_8 slc7_amd64_gcc700 5 1 -1 None print
+taskname="CMSSWTask_NMSSM_XYH_Y_tautau_H_gg_MX_400_MY_70_STEP1_v1"
+jobnum="1"
+tag="v1"
+metis_retries="1"

queue
