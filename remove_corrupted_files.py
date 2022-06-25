import os
import sys
import ROOT as r
from glob import glob

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_0_C3_1_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_1_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_2_C3_1_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/ggF_cHHH0_HHggtautau_*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_0_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_0_5_C2V_1_C3_1_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_2_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_5_C2V_1_C3_1_HHggtautau_*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/ggF_cHHH1_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/ggF_cHHH2p45_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/ggF_cHHH5_HHggtautau_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/res_Graviton_M300*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/res_Graviton_M400*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/res_Graviton_M500*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/res_Graviton_M800*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII/res_Graviton_M1000*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_UL/NMSSM_XYH_Y_tautau_H_gg_MX_*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_UL/NMSSM_XYH_Y_gg_H_tautau_MX_*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH0*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH1*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH2p45*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2Tau_node_cHHH5*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*dileptonic*cHHH0*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*dileptonic*SM*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*dileptonic*cHHH2p45*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*dileptonic*cHHH5*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*semileptonic*cHHH0*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*semileptonic*SM*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*semileptonic*cHHH2p45*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToHHTo2G2W_*semileptonic*cHHH5*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/DiPhoton*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GJets_DoubleEMEnriched_PtG_20MGG_40To80*/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GJets_DoubleEMEnriched_PtG_20MGG-80*/*.root'

#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M1*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M2*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M3*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M4*v2/*.root'
check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M5*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M6*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M7*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M8*v2/*.root'
#check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M9*v2/*.root'

for ifile in glob(check_dir):
	try:
		rfile = r.TFile(ifile)
		nEvents = rfile.Get("Events").GetEntries()
		rfile.Close()
	except:
		os.system("rm {}".format(ifile))
