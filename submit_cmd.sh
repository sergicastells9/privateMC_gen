# this is for most of 2017 MC, 2018 MC, 2017 data, 2018 data
# python submit_all.py --tag v0.6_20201021 --skip_local

# redo 2016MC due to last version in 1021 was not having right format
# python submit_all.py --tag v0.6_20201117 --skip_local --filter 2016MC

# add extra DY HT sample
python submit_all.py --tag v0.6_20201117 --skip_local --dsfilter DYJetsToLL_M-50_HT

# this is for 2017 signal MC
#python submit_all.py --tag v0.1_20201117 --skip_central
