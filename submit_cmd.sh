# this is for most of 2017 MC, 2018 MC, 2017 data, 2018 data
# python submit_all.py --tag v0.6_20201021 --skip_local

# redo 2016MC due to last version in 1021 was not having right format
#python submit_all.py --tag v0.6_20201117 --skip_local --filter 2016MC

# add extra DY HT sample
#python submit_all.py --tag v0.6_20201117 --skip_local --dsfilter DYJetsToLL_M-50_HT

# this is for 2017 signal MC
#python submit_all.py --tag v0.1_20201117 --skip_central

# this is for 2016 signal MC
#python submit_all.py --tag v0.1_20201117 --skip_central

# this is for 3 years of ggWW
#python submit_all.py --tag v0.6_20210210 --skip_local --dsfilter GluGluToHHTo2G2l2nu_node_SM
#python submit_all.py --tag v0.6_20210219 --skip_local --dsfilter GluGluToHHTo2G2Qlnu 
#python submit_all.py --tag v0.6_20210219 --skip_local --dsfilter GluGluToHHTo2B2G 

# for 3 yeras of ggZZ
#python submit_all.py --tag v0.6_20210216 --skip_central

# for VBF and resonant HHggtautau
#python submit_all.py --tag v0.1_20210502 --skip_central
#python submit_all.py --tag v0.2_20210502 --skip_central --dsfilter radion

#python submit_all.py --tag v0.1_addrawphopt_20210507 --skip_local --dsfilter 2018D 
#python submit_all.py --tag v0.1_addrawphopt_20210506 --skip_local --dsfilter DYJetsToLL_M-50 
#python submit_all.py --tag v0.1_addrawphopt_20210506 --skip_local --dsfilter ZGToLLG_01J_5f_TuneCP5 
#python submit_all.py --tag v0.1_addrawphopt_20210506 --skip_local --dsfilter TTGJets_TuneCP5_13TeV 


#python submit_all.py --tag v0.2_nanoaodv8_20210510 --skip_local 

#NMSSM samples
python submit_all.py --tag test --skip_local 
