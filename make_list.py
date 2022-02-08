#basepath = "/hadoop/cms/store/user/hmei/nanoaod_runII/HHggtautau/"
#tag = '_v0.6_20201021'
#name = '/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM'
#name_split = name.split('/')
#name_new = '_'.join([name_split[i] for i in range(1,4)]) + tag
#
##import concurrent.futures
#import glob
#import uproot
#filelist = glob.glob(basepath + name_new + "/*")
#treename = "Events"
#
#nevents = 0 
##executor = None if len(filelist) < 5 else concurrent.futures.ThreadPoolExecutor(min(workers, len(filelist)))
##for fn, nentries in uproot.numentries(filelist, treename, total=False, executor=executor).items():
#for fn, nentries in uproot.numentries(filelist, treename, total=False).items():
#    nevents += nentries
#
#print (name_new, nevents)
f = open("samplelist_all.txt", "w")

skip_keys = ["HHggtautau_Era2017_private", "HHggtautau_Era2018_private"]
global_tags = {"RunIIFall17MiniAODv2": "102X_mc2017_realistic_v8",
               "RunIIAutumn18MiniAODi" : "102X_upgrade2018_realistic_v21",
               "RunIISummer16": "102X_mcRun2_asymptotic_v8",
               "Run2016": "102X_dataRun2_v13", 
               "Run2017": "102X_dataRun2_v13",
               "Run2018": "102X_dataRun2_v13"}
lumi_byrun = {"2018A":14.0, "2018B":7.1, "2018C":6.9 , "2018D": 31.93, "2017B": 4.8, "2017C": 9.7, "2017D": 4.3, "2017E": 9.3, "2017F": 13.5, "2016B": 5.9, "2016C": 2.6, "2016D": 4.4, "2016E": 4.1, "2016F": 3.1, "2016G": 7.6, "2016H": 8.7}
nanoaodversion = "v7"

import json
with open('cross_sections.json') as json_xs:
    xsall = json.load(json_xs)

with open('web_summary.json') as json_file:
    data = json.load(json_file)
    for task in data["tasks"]:
        info = task["general"]
        ds_nano = info["dataset"].replace("/MINIAODSIM", "_PRIVATE/NANOAODSIM").encode('utf-8')
        # this step is for data
        ds_nano = info["dataset"].replace("/MINIAOD", "_PRIVATE/NANOAOD").encode('utf-8')
        outpath = info["output_dir"].encode('utf-8')
        nevts = info["nevents_total"]
        #print (ds_nano.split("/"))
        xs = "FIXME"
        if len(ds_nano.split("/")) >= 2:
            if ds_nano.split("/")[1] in xsall: 
                xs = xsall[ds_nano.split("/")[1]]["xs"] 
        globaltag = "FIXME"
        lumi = 0
        for key in lumi_byrun:
            if key in ds_nano:
                lumi = lumi_byrun[key]
        for key in global_tags:
            if key in ds_nano:
                globaltag = global_tags[key]
        #print (ds_nano, outpath, nevts, xs, globaltag, nanoaodversion)
        outinfo = [ds_nano, outpath, ' ', str(nevts), str(xs), globaltag, nanoaodversion] 
        if "NANOAODSIM" not in ds_nano:
            outinfo = [ds_nano, outpath, str(nevts), str(lumi), globaltag, nanoaodversion] 

        f.write('|' + '|'.join(outinfo) + '| |\n')

f.close()

