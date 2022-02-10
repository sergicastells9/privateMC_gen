import os

def edit_pset_NMSSM( new , old ):
	os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg_tmp.py')
	os.system('sed -i "s/%s/%s/g" /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg_tmp.py'%(old,new))
	os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/NMSSM/HIG-RunIISummer19UL18wmLHEGEN-00265_1_cfg_%s.py'%(new))

def edit_pset_gghh( new , old , year):
	if year == "2016":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_%s.py'%(new))
	elif year == "2016_APV":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_%s.py'%(new))
	elif year == "2017":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_%s.py'%(new))
	elif year == "2018":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/ggf/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_%s.py'%(new))

def edit_pset_gghh_WW( new , old , year, decay):
	if year == "2016":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/%s/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_tmp.py'%(old,new,decay))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGEN-03485_1_cfg_%s.py'%(new))
	elif year == "2016_APV":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/%s/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_tmp.py'%(old,new,decay))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL16wmLHEGENAPV-03182_1_cfg_%s.py'%(new))
	elif year == "2017":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/%s/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_tmp.py'%(old,new,decay))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL17wmLHEGEN-03413_1_cfg_%s.py'%(new))
	elif year == "2018":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/%s/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_tmp.py'%(old,new,decay))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/HHTo2G2l2nu/'+decay+'/HIG-RunIISummer20UL18wmLHEGEN-03457_1_cfg_%s.py'%(new))

def edit_pset_EFT( new , old , year):
	if year == "2016":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGEN-03479_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGEN-03479_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGEN-03479_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGEN-03479_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGEN-03479_1_cfg_%s.py'%(new))
	elif year == "2016_APV":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGENAPV-01195_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGENAPV-01195_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGENAPV-01195_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGENAPV-01195_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL16wmLHEGENAPV-01195_1_cfg_%s.py'%(new))
	elif year == "2017":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL17wmLHEGEN-01655_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL17wmLHEGEN-01655_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL17wmLHEGEN-01655_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL17wmLHEGEN-01655_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL17wmLHEGEN-01655_1_cfg_%s.py'%(new))
	elif year == "2018":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL18wmLHEGEN-01693_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL18wmLHEGEN-01693_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL18wmLHEGEN-01693_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL18wmLHEGEN-01693_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToHHTo2G2Tau_node_EFT_TuneCP5_PSWeights_13TeV-madgraph-pythia8/HIG-RunIISummer20UL18wmLHEGEN-01693_1_cfg_%s.py'%(new))

def edit_pset_graviton( new , old , year):
	if year == "2016":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGEN-01295_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGEN-01295_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGEN-01295_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGEN-01295_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGEN-01295_1_cfg_%s.py'%(new))
	elif year == "2016_APV":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGENAPV-00493_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGENAPV-00493_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGENAPV-00493_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGENAPV-00493_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL16wmLHEGENAPV-00493_1_cfg_%s.py'%(new))
	elif year == "2017":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL17wmLHEGEN-00945_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL17wmLHEGEN-00945_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL17wmLHEGEN-00945_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL17wmLHEGEN-00945_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL17wmLHEGEN-00945_1_cfg_%s.py'%(new))
	elif year == "2018":
		os.system('cp /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL18wmLHEGEN-01243_1_cfg.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL18wmLHEGEN-01243_1_cfg_tmp.py')
		os.system('sed -i "s/%s/%s/g"  /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL18wmLHEGEN-01243_1_cfg_tmp.py'%(old,new))
		os.system('mv /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL18wmLHEGEN-01243_1_cfg_tmp.py /home/users/fsetti/public_html/privateMC_gen/cmsDrivers/UL20/GluGluToBulkGravitonToHHTo2G2Tau/HIG-RunIISummer20UL18wmLHEGEN-01243_1_cfg_%s.py'%(new))
