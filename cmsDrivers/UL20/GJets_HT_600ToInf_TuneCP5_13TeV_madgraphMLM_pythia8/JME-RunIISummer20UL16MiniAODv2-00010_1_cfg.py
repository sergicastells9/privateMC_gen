# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename JME-RunIISummer20UL16MiniAODv2-00010_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:JME-RunIISummer20UL16MiniAODv2-00010.root --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein dbs:/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16RECO-106X_mcRun2_asymptotic_v13-v1/AODSIM --era Run2_2016 --runUnscheduled --no_exec --mc -n 8113 --nThreads 1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.ProcessModifiers.run2_miniAOD_UL_cff import run2_miniAOD_UL

process = cms.Process('PAT',Run2_2016,run2_miniAOD_UL)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(8113)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( (
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/0B8D880A-5E46-A54A-BD71-1E03E6E04241.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/101AF5C3-1C85-0349-A9C8-B8CB30680536.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/2A0F2B32-4BC6-784C-BF99-B05B5C7AFB43.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/2DD683FF-4971-644D-BDD1-73CE283F8E2E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/3CDC021C-40B2-B740-A767-64CE351EDB9C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/AA725B83-2C24-7E4E-AF64-33FE60C6ED67.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/020000/30A86FA3-C547-2949-BD67-0BEA106A3E8C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/020000/64CBD35D-513E-6C4F-A697-4C6900485B54.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/020000/923DD0ED-EF56-3846-AA72-54F14CC6FFAD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/020000/C518F296-9593-5A4F-8E58-217F88B2811D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/240000/B3B07D08-FE61-A741-AD35-063212E5E1A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/14805CA9-17C4-3742-9524-D23520961368.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/254C0B90-46FD-584E-AA10-D0D2452AE636.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2DFF7580-0398-8846-ADDE-12A251AE4769.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3A078191-BDE2-D54D-8859-ABD385D19FEF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/492EB093-2427-4547-AD95-618371C89385.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/52A119B5-D1B9-D24B-919A-CB0FBB7C985F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/57AC31A1-C126-E749-8BD4-28C274AB0DF2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6C1B1F77-B353-A448-969B-0E7EA413A0ED.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6D5B7E7D-5AEF-CF44-A032-A990EEA1421F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/767F22F5-FE61-DA45-9297-3038B3127416.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/800EFC7C-A82F-6043-A47B-CCF3667DEB6E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/84218A46-3C55-C647-992D-C51F3D42D676.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9D4C8F63-858C-0C43-B4E6-B09167302C02.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A07EF672-A352-694E-B513-5B24D694BF79.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A2D937B2-D71E-F942-9DE2-C22AE2F2580D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A6325AB0-52D8-A747-A52F-8D996C0056CA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BB6FFCA5-51A5-494C-9F04-09D20507465E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D0C20CF5-44D6-4E40-9F16-92E35DC633A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D42D0CBF-F6F8-5240-ACDB-598EC305F54D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DC448580-A391-8243-B7BB-7E3F22E564FF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F3F809F1-BEC6-DD44-8EE7-0C6F6B01FD27.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/01DEA5D0-2787-4245-B8F0-C8657F903B28.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/1A424CB5-A879-A24B-AD5F-295EE76ED116.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/1C5540A9-94C9-CF40-938D-639621868CFF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/21667717-ECFB-FB4D-8AAB-FB481807346E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/22DB2C31-E19F-0C4B-8836-9B268E2862E2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2576A9A3-4AD8-AE4D-B8C1-A2E5928343E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2EBA44BD-48D6-CC48-98F9-569EEA8C442F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/302E9089-AEE1-DA40-BF50-154548F56222.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3A3A0949-C9CD-8A46-90FD-56E117E4B9D4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/40E06844-12D5-F34F-8BE1-01C2D2EAA14A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4477758D-C991-994D-9898-5A68D027C9A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/5A9139A4-07BE-FF40-94F5-6D4D82CED4DD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/5C4A9CFF-69CE-F946-A0EC-7B2B7BD018E0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/6808B104-78F0-6245-BBFC-A3C7B996F2D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/8C4B898B-7447-7B45-AD65-B7ED9608B7D9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A49D6CE6-0EF3-524C-B0E5-157C080562F8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/ADD755CB-FB4A-E049-A112-6FA4672CB51E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AE4DAB75-5862-2642-B042-58BE408F60A9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B08B1F03-9D8F-764D-8897-E189FC12A965.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B32D8F52-99A3-7B4A-8D99-CB666F0C7426.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B43C7DEB-4828-044A-8663-50914A9C2198.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B5CB8989-EEFA-F64D-A62A-7758BB54EC76.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B6A865EF-6F9C-EC42-896A-7959388579AA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/BCABE856-94EA-EF4A-B47D-B353AC12C421.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C0D9152B-2BD3-974D-B8F8-FBDCF41C0C25.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/DB7E856C-8AF7-964A-8425-14CF8BBEA1A8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E82178AF-3C67-6348-8127-8796C935DB60.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E9818078-1396-0E45-AD08-855F3AE9A091.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/EBEF79D9-BE5C-ED45-A08D-FC79946D78E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/02E56720-4F48-1546-B647-A70E3B894744.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/03B3661D-6D1D-A143-A184-7C4417F73E91.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/04B4B7FA-821C-B946-A7EF-49A9F01C7F63.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/05AA3626-A969-E34C-839F-20CA6E335947.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/05BEF6EE-B721-9D46-B6F9-9BBF163D9083.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/05C709E0-0DD4-A647-B66F-96A1AD63734C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/05F66449-0E56-214F-A094-853A9F692E77.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/06CB7EF1-9535-134F-B708-4917660CEA5A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/070A1347-A145-DE46-8F00-F409165EA55D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0AA8392E-259A-8D4C-985A-70F27D35C731.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0AB9E12D-FB40-744F-B7F9-49937596A629.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0DF9F209-1354-E542-98B0-36ED1A39C756.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0F1FD90F-B078-8E4F-A635-7D8195ACB451.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0F8FFA7A-2662-E84E-9F00-80FC495841BF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0FFED6E9-DD7A-484B-9A7E-8633212BE29F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/136AC90E-5F04-C646-8B97-94176E6A72AF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1426C099-F98E-5C41-956A-6426DDC760E4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1651F00A-B402-8342-8C4C-B22321699514.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/19837B6B-9619-D04D-94BB-A50C5B798153.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1A6FE8D7-2277-5C47-BD71-6DE69EFD66C3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1A7FF917-9039-C24D-B3D2-6A16C59BCF5F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1BECE5C2-2E7B-D74E-B52F-848966010930.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1C7D8674-7B42-4B4D-9002-83B1E30E4E4E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1D3766D9-E575-6649-B20C-B8B78D2FA7B6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1F15E8DF-F6FA-E940-8BC3-52143D519BDA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/21BB0A97-8549-224E-AE35-972247689066.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/22987F64-ED3D-F94B-AAA8-6C316A1DBF22.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/23499E3F-EA73-8F40-8F0D-1CFD7A18B3D3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/234DD615-9982-D746-9363-74451014CF00.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/25C78DA8-7195-E44B-8F77-F999E7C7C463.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2C09C5A8-18CA-5D44-9416-9738DE1EBED6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2C76DE17-E80C-7341-81B1-729208CC56A8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2CBD0D1E-C7ED-4945-8CAF-A4111DD80DCE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/30998DA9-BFAD-D648-851B-4B8C0887CC39.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/33C3E7FB-AF79-7E49-A391-3F77C993F3EA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/36D459D0-D101-7347-99C1-1CBDC4158678.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3879FBCB-4B6E-5A49-BEDD-145256BB1EA9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/397530EB-A496-6B4F-83D8-C04771FC159F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/39D6A124-6749-6B42-8656-449C2C2B4652.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3A983254-9BF2-A446-8007-984548649890.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3CF253B6-ADC4-6845-AEE1-73BF04E1DBED.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3D5F1CAB-9C32-074D-B31B-A4C7479431E3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4131856F-2AA6-AD46-A4FA-0F4CD4C06BA8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/43FE5B63-65DE-B343-8F02-53DA038271AB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/48A441A2-6ABC-AB47-BD45-B5990C2ADF36.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4ADE46B5-6D46-0F41-B741-53D45BD88C1D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4B1CE64C-A9A6-B746-8E42-AAADBF989D2D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4BD36A73-1E15-3C46-A816-E0EA27C9BB00.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4D630BB5-115A-D049-A259-96FD07A60E02.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4FA7AFEA-B7D6-924B-9CF0-CB3E38F13BAA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4FAFB45A-BE05-9942-A901-3E74C7AD9779.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5152A09B-0904-DB43-96A0-34F6B8EFE22C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/51760F18-2723-0F41-9A10-72C33E73B435.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/519002DE-DEB5-3A40-98F9-1EE54634F8FF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5443957D-8C7F-F041-9EBA-5EA4F7B44356.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/54F7A505-8B4E-5741-92E0-1526CE6B635C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/55E3FD7A-D133-2F42-9748-6D0862E074F8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/563B04F5-D353-8A41-A949-6F859CDFF059.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/56CD81F9-D8FA-6E4E-B684-9DB793692336.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/59BB68F4-4BC6-6E4E-9317-B7A5B9C5DFDA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5B3A2905-2DD3-4C4E-85E5-406282E56F4E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5C47E2FF-CA09-ED44-B85E-2B5D110014BD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5EA44828-FA99-964C-AC6E-10BFEF85F03E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5FF71ABC-86F8-FB4F-9917-2A61471D3BFD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6152FB5E-942A-3347-AA6B-26BD632E68C1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/660AB06B-C0C2-FE48-9B1A-3967BD05C635.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/67D1A032-D689-2749-96C2-B2D4254E5064.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6BECCD3A-0859-7940-B1F2-C6FCBBACE323.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6C207938-7968-4046-BED4-94D50B136730.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6C248B1D-6F7E-6F4F-A96C-14B3A7F224AD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7710E80C-C8AB-0A45-8432-50A2A38319A3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/79AF987E-9764-244B-AD4D-09489866C9F1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/79E4067A-F0FA-CF42-BF73-064122664C24.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7B434D92-E20C-8243-9AD4-C376787478F7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7C3F3F3D-2573-B842-B862-696AC8FBDF35.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7C5259F1-F1F4-A74E-BB4F-28FBC3C9F4F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7CA99D48-1945-5445-B063-893ED48BA156.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7CEF1B20-1D9B-A748-857B-C31A121B988E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7EC398D5-B395-D44E-B0B4-5A3FEF5EA852.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/80861F53-4B28-6C40-A72E-EFC9AE866D68.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8358C74D-5975-2C4F-B198-8D51A9EFB3D7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/83972510-42F3-AB47-99EA-3E78C5868597.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/85947283-771B-A845-B0DE-FC10153C6AB9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/88C68CED-91AD-0A4D-9DF1-EC1E6D4BA24B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8C7CCE54-F4E6-E44D-A1E4-58B1749B182A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8F9DE322-D522-C44B-8A37-941E7E1B5541.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8FBC988C-4FF2-2A4B-B1B8-3ECF24856133.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9059AB13-8425-E34E-8A3E-CE46983425CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/906152B7-3E9C-134F-A919-34530AFFF4A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/92B5FFEC-FD3C-3142-B550-164053ABA65F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/986EBE9D-079A-FE45-A9F9-735BC9F9CCC8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/98F8F54B-4B7B-0847-9298-D4B05DF4E5D5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/996A06AE-2E99-5245-AD01-9531C377A4FB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9B142A11-378A-704A-A2CC-7188D5AADC0D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9B790722-7AC2-3749-B570-B9199950E093.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9C0EC627-9791-D849-950F-DB3CD3DC2F77.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9C2D337C-AFBC-404B-8491-CE7E2366B2F9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9D01CB1B-E0F1-914A-931C-60C9CB2A5550.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9DDDF21C-7E7A-0E43-9371-A993574903FA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9E3EEC68-9928-F541-BF65-A569BD3D6570.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9E907DED-CDC3-0A48-A73C-78FB4BC27DB3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A11C1B62-40CC-1F40-9636-4D6376A5316B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A2D4E856-6202-AB44-B735-F3369B197A07.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A2F531F9-5184-9A44-B6F2-6635C1C7D727.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A7229E42-0438-BE41-A9A4-13A4AEB523B7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A72394D2-F26D-934D-80FA-9E14290AEE2A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A75329E6-11DA-E048-895F-5DBA164A6892.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A76E6AF5-477E-5543-BED3-58B4BFD0C2EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A919AB82-4014-2841-912C-9CAC49D85912.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AB257866-9333-B349-98B0-A256FE23B333.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AB29F620-B399-E245-A728-A4D8BD937D62.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AD1BF429-5106-F449-ADDB-6E7F706FCFEE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AD79BBF4-9EB8-2944-8D5A-7C94C9C70D58.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AF7E9230-0235-5045-A81E-0A30AA79012F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AFA160E8-A92A-5440-BFCA-BF635A3ABE6E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B06DB23E-A59D-DD4C-A1DE-3E576F4EBD9C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B0978E36-AF62-2E4D-91EA-1770E5676664.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B4C13C86-6ABA-B948-981B-013B31A22C8F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B7688818-D939-9747-B195-ECD701912EF9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BAA97358-70AB-4B42-9BF5-E3758B307B06.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BAAEEDCD-D5A5-A149-BBA6-B84526D60BE4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BB1283C8-31C1-4843-A048-DB8AF104BEA9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BB7E9CB2-569E-4F44-8040-AB01ED4EED0C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BE7660D2-81E1-774D-BB66-DD13BEDF3B01.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BF041BD1-0181-4F40-BD6D-66B4A115263C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C0AAE197-A2D1-704F-BA60-50BF8EBD167F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C5D7F175-5B88-A54E-9FC4-A45F3CF8A807.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C8EF80FD-FCD0-7043-95E4-426E6406F3A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C9919D92-C377-9744-866E-5BF06401C6D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C9C5BC1C-C696-1941-B0B5-3D069DA30903.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/CDF0F171-AE67-C646-A8E2-50DC15E9D55F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/CE1A26BD-5461-F24D-AF31-54D2528A081D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/CE3FE632-DECE-E542-A208-997546E1609F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D1AF168E-8EF4-EB4A-B9D4-EFCB5150EA27.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D2F7F876-0FF9-484B-BDCB-F5F0079BE07E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D3FC52AC-7897-5444-BCD1-AE92B9E16101.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D4260F1D-C8BA-E34C-A7A1-1BE35816C8EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D63DD3BD-2CEF-4D47-B8F6-7449B8D70725.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D68068EF-FCB2-E74D-A055-9C2E98D1B2F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D856326A-7049-CE40-873E-3EF509F5C847.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DEEAD8E8-8F3A-5D43-99D8-F14B745C1BFE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DF0A2865-9253-4645-9504-02E2A3B59CE3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DF4E138C-99D7-4047-89FB-1D0D490F018B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E04938F6-B710-2249-8529-32CE61F2EE79.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E294FE99-D137-F643-A1CA-527D6FBCB0F5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E6556200-1F45-7349-9F06-979D4BE0C116.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E75BDBD1-5874-BF47-B753-A3916144A3FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E9125871-296D-EE48-BE4F-2ECD71B2B958.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E93E94CF-7994-1446-BA31-683C2073E2D2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EA01FC06-C900-6545-B3D4-56544EDA2129.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EC49D7C1-FE90-044D-AB9F-8430BE48D448.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/ECB9565B-AA6E-5D40-B380-021EDF27053D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EE7C1514-31F9-F540-B1EF-1B2078F7466F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EF01BBDF-17D2-E645-9F1C-D3DB52E57D86.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F010A8C3-D584-B946-B389-5FBA482B7601.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F019BE10-F5CD-3140-B1ED-40F80327EC2D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F0B0D7AE-D122-6A4F-943C-E02B054FC5D4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F142D0EA-6EC8-FD47-B182-2928E4FB9461.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F3538354-F68F-2242-BE56-5AA0D3435F2C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F4D8E7DF-F26A-4A49-86D3-7C4A9797DF0A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F5A6CF24-F9A0-174C-8E88-72A2CBBE3A20.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F6627045-4EA3-444D-8AEA-9B8834194715.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F7D73230-81D4-5849-9FA4-0F6154DD7B19.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F84EA163-8BB3-2D45-8626-09ACCC259F9F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/04AE556D-983B-C849-9D21-1813C8F69EFA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/1071AD7C-B1FA-6D4B-80B3-961CD71AF197.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/109AF954-37F7-0E4B-BCE7-3DDC63C971F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/12A195BD-7DB3-5946-99D6-0A0F94F70176.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/21B76D6B-B9F6-B049-BCA7-3D5B0DF266A6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2203A678-F473-F24C-A4D7-0D2502D6306C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/254C78A2-D259-3641-B4BA-253261713956.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2886026C-23A5-0B47-BF52-7D1FEC386E94.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2B69D76A-8E85-4F47-9CB8-235D8F1AC6C4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2BD2765D-1E3A-764F-AF56-2DA025428070.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/2F2F286B-FE76-5845-8C8D-B51846874A30.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/317D718C-AC25-8D45-B299-4988B53C55E5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3457A838-76B8-7E47-9D6C-85048F1E34D2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/37EF7623-68FA-2D42-83F2-AF19CEDF2A38.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/38B83BB0-A46B-A14B-856F-E80DA7DB1714.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3A882D98-8933-4E40-9FAE-9809013B6DF9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3AD1EF0B-295E-8D4E-A9D4-C3BCA22B6A88.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3EFCBBBA-D28B-4B45-BE8C-BC2B5DF6FDC7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/3FB007A5-159F-B345-B084-0128E86A9A31.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/44861C05-98DA-3843-BAA3-CEEB29D39B3F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/44E7A85A-1DD9-B942-93BD-A4B55100C4ED.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/44FD56FA-9BD1-FF4A-888C-291642C003F7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/465CED70-33A8-FA4D-BE80-273E8B6CFC4A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/49BDD354-CA92-E44B-BBCA-39A81991A12D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/5294FB36-AE99-484C-B23D-E8258AAEAB53.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/54B58A9A-01ED-364C-A225-7744E21100FF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/5661DBB2-780C-BB49-8009-FE33616C56D5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/569C3492-F616-5B44-957C-9E77FA46793F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/56AB5C7F-5708-1E45-BDCA-982ADE8AFBFC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/5827FCCD-F06A-2048-855B-56C4E6BBCB54.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/5DC96A63-0E4E-0542-B548-AC8B4B642C58.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/5E86D2B7-AEAA-8E40-8FF0-015FE33A5163.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/636B0044-B9F4-2C48-ACD4-7C18E5730789.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/646F66B5-E447-A244-A377-458961A5AC96.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/64879CF3-E996-1143-84CE-E0FE7D9E8B47.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/651E18E0-733F-F845-94DD-82C0B0C0DA73.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/65BF84EC-BC69-A24A-BAD1-4FC1EB8239D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/66C376A9-CAC1-6F40-AAB4-AAB70B8AEDDE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/66DE31F1-9DEF-B745-A338-22C3C97F9E3D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/695EA6FD-457C-F44E-AE30-124753022164.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/69650E23-459D-4244-B72B-517402527A10.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/69C04948-A9F1-E04E-BCCA-805EB0E743B8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/74723F00-837F-FF49-9C3F-1D49D9887F03.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/77A08DD9-E781-4F4C-8F98-5C512C99ADA1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/797D2BC9-93D9-FA43-B462-AE4151F84F73.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/7B33E51B-FE7C-F04A-815A-9C01E26EF715.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/7DAD952F-2B01-9544-80FD-6F62E9B04D6F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/7FDDEC5A-09A2-AE4A-B392-0B01F09A0E0B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/80DDB222-48D1-4D4A-A88D-631429A323EF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/8398988D-863C-B94C-B488-44C4DE125FB8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/84E93C3A-9DDD-EE44-A946-A0C9631447BC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/85BA5D4B-9498-4748-9274-3C142A2BE411.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/8B9D92C6-C865-0D4C-8CCB-05A4DA539142.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/8D730EAA-926A-F240-A097-7771693ADD79.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/8F1999D8-9F27-E347-A446-41B2889E971B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/8F5CEA20-E560-A842-B66B-A7596CC68752.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/912CAF84-92CF-534C-9BDA-E13E92F22CB7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/912FE4B8-2D2C-7C43-9D60-78CBB66D6F9E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/94B5EEE2-0089-CA45-AB98-A392A03E08BA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/956A175B-A41A-A943-A754-31AF79A97B13.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/972C6E4A-7852-454E-9EB1-9388D7835E3E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/9A52E108-4A89-414B-9AEB-4C2C5FCF3A98.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/A1757EC0-65B6-EA4B-BED5-4C400ABA9400.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/A4F9B13D-1F90-F249-ADDD-D9D8E1F94BF3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/AAE3A526-A9E4-364A-BC23-7C7417B0F820.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/B4E741B7-898C-C94C-A055-3FE51C3C1937.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/B5793BA2-D1E2-D249-BEA7-B96B23266D00.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/BB427281-9D11-8D43-9A01-CE63EE2938F4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/BC936FC7-9B80-E041-A45B-22DC9535F303.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/C6CE64A0-62AB-024B-96C0-F45B55C339E0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/C7CD7790-74B5-4645-AF97-24F9B13E4456.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/CBF32973-A980-6D4F-B449-74C4FBCB896D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D07152BD-C038-1341-9DDF-BEB0C9A5F624.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D271DE14-303A-7F4A-BD52-5BC03EE11E0D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D2D8BCD0-F025-0B42-BA54-97336AF2A2DE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D3ADDEE1-863D-B343-887B-26E31F83329E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D5E52B91-2356-5B46-81B8-DEFD24B8A78A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/D96773FC-7630-DE44-A4A4-7466F09A1D17.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/DCF4DB0A-C0BC-2D47-85DE-E58FBF5E6592.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E19374BA-AF03-7A41-AE5D-6B7016A61579.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E32803CE-A5A4-3E46-851C-51457EFD9181.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E44243AD-D920-7A41-8B26-D8EDA5D50F31.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E57FA2DB-5865-D24B-A1B3-BD4E57BF9EB9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E7ED0B1D-127F-9F41-8176-AE0F29A4B7AA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/E9540260-1F8C-414D-B9D0-01A05CD0A2CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/EC97B9C3-C0DA-B14A-B996-502C2068B06E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F0F28E91-0A84-F64D-B47F-64068FCDFE51.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F17FEE2A-4F16-BB47-8860-6EF7ECB83B3D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/F86A7019-BEA6-AE4F-B4F5-2DEA73FBD2BF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/40000/FC0D30C8-D845-F841-9B8E-DA87798C5B18.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0031632F-D84B-FA48-B3D5-C2BCA4811B05.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/01B16045-95AE-E048-9F4D-27CA4FF61B39.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/02164F68-2C86-064F-8903-FEBD8D9E6197.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/037A0618-1F67-C047-90AB-AACA2C5FED6C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/068F40FD-27FF-8443-A75E-72B1B36709B7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/06C69DA2-D9DB-084D-8CF1-86A16BA38FCC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0A29CDD3-82B5-8A42-BA4A-832BE87EE63D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0B46D3E4-E76D-D94F-AF7A-F7E156CA0ECC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0B481776-9077-8B42-9579-19054ED09BE6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0C03C4D9-1DA5-9144-B931-EA96AFB91FA1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/108FC02B-586F-EF4B-8700-DBBEE9F68070.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/12894580-550B-524C-A507-065DB9522C6B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/12D97690-0E33-D640-8F96-B81D33667456.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/14082CE6-DA05-CF47-A0FA-6D44C459834E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/165C7860-7E49-1240-A05F-AE4A44241397.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/16F9A58E-CFCD-CD4B-9B0B-33774F446AAB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/19084DF6-465E-BF46-BAD5-1F9797B11EE0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1ACADA79-81AC-914B-805D-FB7645A9BCFD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1AE86654-DC2F-6645-B085-D9B2D14A5F68.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1AFF4B40-6D75-7243-9ACD-707F155D7E13.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1E1713BB-901B-9045-81DA-B55DBD8E48B7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1E4ECC67-4A18-034E-AC81-0E3C08804006.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/205A3C78-5C29-0249-BE08-15D5CDCB3BF2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/213B22A4-B3EE-4543-8A1D-042AD3AD0BE4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/22A70B16-05AE-9749-B06A-9C142346C082.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/23209755-372F-CE42-9392-49E9202C88B6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/237F76EB-CC0E-3048-9CE0-8907DEE1CFF9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/242FA457-8389-344C-9476-CB50B90196F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/25DAF40C-027C-4A45-9AAB-746D5D78BF1B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/27D11B40-5943-5D46-8888-52FF005C8A0D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2884EF47-E014-A24C-840B-9AB754D6D0F2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2B25A36B-B403-8B4A-91D0-824695C7ED7A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2CCE33D6-43FD-894C-A789-28B25805CBD1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/30B03F07-EE12-2843-A3A5-5FF1A4DD0E81.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3120AB5F-7441-5C4D-9D76-ED92F4E0FF48.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/340303CD-3B3B-7F4E-BA09-F302A6CD35B7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/362DE39A-7C33-344F-BC85-E5FF8D0EA4D3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/36C5D6AD-B6FC-8348-811A-06ADF0E765A6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/36ECAC93-B114-8A4A-8B1D-9733A0A6043C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/39DC143B-6EBC-784C-B83E-F7FCE80C8940.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3B3A1336-9DFD-B84D-8020-EA2F97B56D6D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3B844E55-1647-8E4D-A854-3C70B22D6C35.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3DF213CB-DA77-AA40-9431-B9934B420BC0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3F544E0B-8ABF-EE4A-8CCC-37A8BEF5F513.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3F8CF00B-B0D1-4544-8F07-0672FEB6EED9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/408821C0-4985-A042-ADC8-3B61F7980294.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/40DC5436-CB88-1D4B-B7C1-827A83C6DF07.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/418B2986-09B3-944E-B295-8F5827FBC09E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/450F62E1-4CCE-4645-8094-C9EA594C2998.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/46727989-8678-1B4F-A1F4-82977603D1E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/47B637F2-AD1F-A845-8102-05CCD37929A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/47F41232-E5F0-0E4B-AAEA-6A15A14E07D1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/48E0C884-C7D1-C544-8FDD-5FFF5BB558BE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4A1C6F28-16E0-F844-BDFF-BB5AD386BC17.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4D8870FE-0DB7-5F46-A408-7C6862A5FA5B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/500FB5BF-95A5-704B-A863-1BEAE6DF9D3E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/577D510F-E7C0-3541-8906-1E8515B422A8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5783DCE8-189E-D846-9D90-34807C1DFC73.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/593CF7FB-AF61-E748-9352-C22EF5A64240.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5A97999A-ECB4-5344-8CFC-C9B1BE73538B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5B65FF9B-56E6-304C-8DE7-F3E63FC39C28.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5C7BC847-5A4B-E443-83F0-F5CBC1C60D35.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/60AA98EE-809A-794A-BC41-89414B1E8B92.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6112CE90-F895-B642-8457-30D8D32704FF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6139E76B-7793-A648-A426-F09FBEC33B2A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6261FF15-08E5-4E4A-B388-65C78868755D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6341C461-0C48-E646-8390-9D26E0567AD8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/63D8B7F0-F3E7-AE4B-9172-1A620BFE282C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/643AAC1A-5753-1746-A379-C4775737B2DC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/68F18057-8F1C-894F-9ADD-6ECC80A65A80.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6969CCBE-8ECC-824A-94F4-7CAC7123E3E1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/697D64FF-F30C-884B-9D5C-58D027AE64CA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6B35DE10-55A0-1F48-AAD1-093AF0125914.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6C718C9A-4960-654E-BF5B-F4ABD18CBAF9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6E72117D-03E6-544D-88E3-9EE8636919FA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6F5F5D00-CC58-F743-9C27-A43AC16FECDF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7061A2F6-7B84-CF4F-8E3D-C7195CEFD5F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/706CB479-0377-1749-9005-5C36EADA40B3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7083538D-BBC6-074C-833E-8C9924DBEFC0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/73C119E7-3431-674A-8863-F830269328BB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/75D56165-3397-8C4C-9AD7-A93EDE9F330D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/76D0D3F3-13EE-254D-89C7-8A948624E1F3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/77353EC1-85EC-2743-84FF-94B813F2B81C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/77C50DE7-7C48-C54A-A22F-74E642C4D726.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/78FE7E51-1B3D-134D-A4FF-89B4E18584E6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7AB0AA27-3B85-AD45-93BF-C30D3481AB76.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7C80DCEE-2BCF-904A-AFE5-7D86A20B09BD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7CC18D6B-6DA5-6B4F-B222-D92BE1F0FF81.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7FE26BB7-891E-1E41-9157-06D868D3DE6E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7FFB2BD0-7D0A-4747-A0E1-D47923D310F9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8240538C-5011-1F41-8652-CBD7F3440B2C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/84149102-813A-C14D-896F-E13DA9786FBD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8503A324-478E-C248-8245-70C2C200108D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8578358A-3429-6743-BDA3-7D65F01607E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/864B8271-8E97-DB46-91DB-F260F7603A4D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8B653741-FB6B-3A4B-B7E7-D874391E9DA8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8B73F9CE-3B51-1A47-B658-C7BD6A68868B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8BD8B6A5-206D-334C-A698-0EA04472365D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8C9C5A2F-C418-854F-8FCE-4FF111783D27.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8D2E729B-92C9-8943-A47C-DA93F173E98B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8D4BF623-6A2E-B44A-865A-DE3FE916841F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8EE80D43-056F-0945-B73D-B926E26BD76D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8F497C25-959F-D945-B9FF-FA458447E8EA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8F649347-F627-A64A-A7BA-1AAC2B4D8B56.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9122D4C3-3B83-3149-9F54-E2BC088EED69.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/925D60F2-DB19-5444-A064-A129E607A730.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9485A904-26F5-7D4D-90F9-C685A9355FE1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/964E87AB-D042-B549-BD57-03E188C6D10F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/965C57AB-2E2B-3747-95E4-6A06B12522E6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9757C44A-31C5-8342-8FF2-95BD08B80A16.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9DC9167C-C877-8943-8A28-D0FDBD629F97.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9F8130E7-E64E-D047-83AF-970497B7B673.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A03ADBD0-AF53-214D-9A9E-703394002690.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A05744F6-6B32-9743-867B-056F075271C3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A2FF7184-7E62-5548-B870-728534119424.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A30153A2-231B-6643-BDF0-8E559F0872F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A3D8E313-D297-3046-8FFF-AE90195456CA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A49EBDD3-572A-7F48-9FD5-43065F96A5E0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A58DFEAB-87EB-C248-920B-C62B10B9C431.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A6E2CF47-083C-4D4C-AF1B-BA2BE15E8331.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A7594DD0-B3F1-9A44-BBFD-7A815D58BCC8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A831852D-4F28-9A4E-A3EE-B3FE91AEFC9D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A8CC06CD-299B-714C-BC61-F717C37C2BCC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AA1D58FA-1FDF-EF4C-A847-7640243AA67B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AC326573-6B81-814A-B061-2A4396AFD24E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B0F21C4F-17A7-0E4F-87A1-48FC5DA17093.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B3371F3C-F39B-4043-9DB2-CCE01958AE21.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B5661C6A-03E3-5743-AA3A-85A6894F008A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B6789E24-54DF-F143-AFF2-C84D35793636.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B702FD04-3322-2E42-BF9D-58392415A1CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B8D1DB07-A842-F64C-9862-C6C939BDC6E6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B972FA7E-D6F4-F745-A169-5E525AA95A03.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B9ADFB17-94F0-E64C-B1F5-3E2766703833.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BA148CC1-5F48-E842-A724-E6A84D3F8C7E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BB66FBF1-6C5F-2D4B-9BBE-06FA1A8E45F8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BC900453-BD80-D64C-B848-ECF8F9F1017C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BDE22763-7A18-164E-B1F7-549C09368C85.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BDF85517-2331-6342-A783-8C9477DD78BF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BE3E18C5-695B-3241-8A25-7C63C9650A65.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BED6E5EB-1883-2141-8E47-5D70D747A016.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BED7E7EC-700B-734E-958E-3FBFDD0D7ADD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BFC8A0FA-B74B-ED44-808C-E2E42DBA6702.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C0AEBB10-691D-AE4C-89E0-3C7417F5F3D1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C0F3D594-7C22-3F4D-BCA1-0631A3C1BD90.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C1F81401-534A-3640-8718-5D9366750A5F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C648E92D-EBBE-1A42-ABEF-A8D8C241CE8C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C66856A6-A75F-354B-BF64-9BA596998CA2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CB482FBC-7CA0-6F48-A01D-8058656CDB06.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CC2012B1-A8B9-8A42-96F6-3CB1AA2D493B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CD5FE372-383F-E24A-ABBE-67C4B51FDBC3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CDE54812-578A-784C-A4F1-65F8CED3435E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CE118A7F-4F96-A742-8307-D6BCB616890A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CE5B8AEC-FD55-9E45-ACAA-E130D600596C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CE90240D-1571-1945-AFD3-08F2CEC31020.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CED6DAFD-3D24-794C-9D3E-807FE27BC848.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CF0BCF9F-D3F8-EC44-8A18-0D1203CB169E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D14563F3-9D93-F843-94EC-35F69C892560.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D2C9CB68-283D-C046-80EF-A2E8CCB02A67.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D4F6B277-5E1D-A241-B725-C92B2B28A246.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D51B884F-DF06-4141-BA85-A13180C1AC69.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D530357F-E257-B541-87DD-E15A69799C9F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D5FA60AE-45A0-6246-AA6D-8C181A1ACFC2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D7526F7D-39D4-FA41-8697-AC4BAAC66033.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D7A002A5-6150-984C-B90B-CAFF2242DED2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D90FB3C4-8C91-5E48-B04D-F41AD2870DF3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DA3D6928-5CF6-2B4B-9F20-590AE434FB9B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DB02BB0A-7D5F-964B-9395-2C50089D3B44.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DB40652A-3050-6744-9D84-4FFAC0A3D4DA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DB4396BE-DE72-374E-A72A-D5F15867916D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DDF0E254-FD2E-F94B-9DB4-BC10AD47CA96.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E0285E62-97F6-9844-A564-5926E476D4E5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E0954902-6767-3F4D-B3E9-6C06CDC7777F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E2F1AEB3-AED7-9D4F-BDD7-B7A3C1877905.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E4FBE9AD-D842-1448-82B3-B85113223E94.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E56FAAA0-690F-6542-B279-BD5AF8C3A8D4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E63CFBF3-D300-2F47-9B82-93E07A6C5D01.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E674F38C-C81C-7045-82A6-D61437FD41FD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E6ECFE60-DDAB-994F-A174-1441130541C0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E752FCCB-264B-F440-9CC0-D3DF4B607643.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E8904D32-4910-5844-B843-C7E7F3E2203E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/ECAB28BD-1061-5248-B739-E7BE441EA9C3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EEB2234A-FF97-4C42-B227-E10E83ACC32A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EF7614DB-DE86-1C49-A923-E2333C688E7E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F16382B8-21F0-BD46-B5C3-1CB1FB405E53.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F218BBC0-70DB-9D42-A09A-F3F7D5BE20A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F24A295D-4429-BD4E-A48A-733F53EF96A3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F510C94D-B469-BD47-B95A-7D76A72F48E4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F55A8839-28FA-CD4C-A15E-D7F479FBA5B9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F580C19C-5C71-994D-B375-DA6CA612F8C1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F6DC3145-2903-874A-8D2A-F82125026B69.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F7674E57-3C2E-DC48-BD15-24C14AF704C7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FBFB3467-9200-F049-B254-FA99834A9EE6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FCFB5FD4-18A8-8B44-802B-A2E04A5671D2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FE2C2BBF-3479-8842-A9AA-47917E9F3D96.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FEE3DABE-3D44-814B-8132-3D5CF17DEBB9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FF7E96A1-9EBA-954D-B34D-3935EEDB0E78.root'
     ) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:8113'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:JME-RunIISummer20UL16MiniAODv2-00010.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v17', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_hfNoisyHitsFilter = cms.Path(process.hfNoisyHitsFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.Flag_BadPFMuonDzFilter = cms.Path(process.BadPFMuonDzFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadPFMuonDzFilter,process.Flag_hfNoisyHitsFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
