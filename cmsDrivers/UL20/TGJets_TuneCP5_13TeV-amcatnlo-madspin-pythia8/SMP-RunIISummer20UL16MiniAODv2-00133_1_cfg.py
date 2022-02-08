# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SMP-RunIISummer20UL16MiniAODv2-00133_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:SMP-RunIISummer20UL16MiniAODv2-00133.root --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein dbs:/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL16RECO-106X_mcRun2_asymptotic_v13_ext1-v2/AODSIM --era Run2_2016 --runUnscheduled --no_exec --mc -n 8113 --nThreads 1
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
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/019DD889-1E7E-444D-B867-71E5C716AF2B.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/01ADFBF4-FA0E-CE4F-8646-F90BC3776603.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/02F049E4-23A3-2D42-98BB-D06B71F60AA0.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/044DAB19-4883-1F40-9473-FF0AE8A0CEE8.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/08753FAD-B27B-FB4A-8D75-D1BF48271719.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/0AC7CD82-718F-6A46-B160-D50528709535.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/0C4677AD-288D-DA4F-8A96-87ABC3BAB63A.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/0E99D8C0-CE5E-C443-AD71-69CC1481BC3D.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/102955A4-5589-754A-A1BF-C359CE42B06D.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/1451AB28-904F-DB4C-AFF7-D2CD93ABA933.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/1727B69D-51BE-D44D-85CF-A169852E3F69.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/18BD768C-9877-EF45-8008-B81A274ACEDC.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/1A95FDA2-D65C-7648-BBAA-4B4A757380DA.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/1F3CBDD2-D9A6-DE40-87F3-FD51E779EABE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/207F1CAE-2B63-6D48-8CBD-C08243E2824B.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/254C4EAC-89C1-D748-88EE-5B4A0DFC231B.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/25A3E08D-FE08-8D43-A754-8B6B2FA1EF85.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/298DF4EB-389B-EB49-85BD-122748844C67.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/2CB312B3-C0FC-F648-AFC8-65A99A106797.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/2DD57FDD-BF30-3E4E-A6E9-130C3EFA9B29.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/329893F9-C6C8-0C40-BE19-1D669A583753.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/335BCC4D-7651-4149-8F2E-0F3EF3DA166B.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/33F2E3EA-B1DB-E24A-9976-186215CC7B74.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/3726051C-C7C0-0348-8038-912480BC863D.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/3A8479B7-388A-8242-8BA5-D64F0CD4B63C.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/3E3EF355-329C-2A4D-9B4F-336D92777C6F.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/3FA4E46B-4F36-F047-ACCE-0BF19AF73E66.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/4071A1E4-A07D-AD44-AD9D-1DA1444E2CA9.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/454635B9-CCD1-114D-A523-C2D07DAF0920.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/4A85F329-F555-D140-8A64-7091CAECE3AC.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/4EC5E1FA-0094-5B4F-8D92-CDCF81C6F975.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/515E46D5-7C6E-FA47-ABE9-A1E2607574C7.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/519072A4-B628-E14E-B490-999961BC4730.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/5BD301D6-4EBF-C24B-8ACD-41D6DD290AB7.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/5BF23A20-AF02-554A-A4D8-68571AD8CF83.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/5CF7E8AF-DE1D-C047-93B8-D8F5823EF3FC.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/5DB1A3BB-AD74-4346-B595-3A24B763B3EB.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/5F8BE423-5264-6C41-A7F3-A7D756968893.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/61B88E06-48D4-9245-BB30-AA4BA1805C71.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/61BFE8A0-1A73-7F49-B629-A62F0A911E42.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/6614AAB0-3189-1C4A-B966-2D3494A18E1E.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/6CDB2FE6-5F77-074C-B5E3-B2E1B228B8E8.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/76486462-72C5-BC4A-9953-8A2EAC674A95.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/76C27D66-0234-B44A-809F-9C7CB3CA1073.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/7A4A670B-0F61-C94E-B748-3C870CD533CD.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/7ADDB36A-D627-F14F-B76C-1410A3F8D832.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/7BA0D044-0C04-CA46-B7E8-4E96AD9F9BD0.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/7D1EB9C8-16D0-054E-8954-8151482525CC.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/7DD1CD2D-3A2E-0040-9A98-078D8DCF8EC2.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/7E9DF0DC-2640-634D-B789-07BE32271D01.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/83088BA6-C620-C643-B95D-0C3535D87DC1.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/84FAC219-56F2-7B45-B571-F78C793BBF0F.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/87A0FD1A-FF08-2542-A631-B04F21151ABC.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/89AF3D6D-B13E-5643-835C-AE35E163F8F1.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/8B678A87-8768-414E-B3AA-A12529EA4779.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/8CFE9D77-F8F2-0B4F-A7E7-FD713FF6AD47.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/8D2678BF-F1B6-FE46-93CD-3FCD57071667.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/8E3F5A04-517C-4C4A-AF9B-534B9B086CDC.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/8F7E6DED-36E2-4949-8917-1229FC3659E4.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/91C2278F-5469-D744-A198-E5DD193B7912.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/970232C3-2EF7-9A4B-8112-10ACF6459359.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/97DA2EEE-7D95-0B49-A23D-8E0217C5F239.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/9C11A1BE-323E-8A42-A7C6-61C58967EF19.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/9D9D9ED7-25DB-354A-A7D0-753A46EBFEF8.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/A2444FD3-A5BA-E04C-B317-0764AF8DD750.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/A248E396-CB8D-EC40-9391-548DDF1D8B6F.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/A5E06955-6DBB-2942-BD99-14BBDE5AB8BB.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/A9D40C5E-2D29-6C47-84C6-00F6B25D3DAE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/B201AA6C-9D2B-3E4A-8303-698786B8F0DB.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/B3F12D08-1246-914C-ACEA-0053F16B3217.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/B566FBB7-F028-6743-99A4-2A1BBB9D1C08.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/B5D15BFB-16FA-9E45-A160-14B1BD5D9BDE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/B8FC280C-7780-6F45-A13F-BF449E6A32EB.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/B96D9F0D-FC26-2046-9B33-4BC16345A932.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/BBC46FC5-8D00-B54B-AAF1-6008333652F5.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C196367A-A3C7-504C-99EA-E6EFA416B61C.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C1CF2B0E-41F6-3247-8056-484E3B22CDCE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C217A59D-BC17-AE4F-BA62-46E8F17B8C0F.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C339774C-29DD-824F-8BC6-EE39D9DE9AC1.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C4ECEC44-A8BA-5145-AF7D-05D44EB36FE9.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C531854E-F9F9-7948-A22D-CF0C11561EC7.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C709F787-DC6A-6D46-8614-2C631AFC522C.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/C8E60089-CB1A-9C47-BA40-9255A1540C82.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/D1DCC967-5CBC-4D42-803E-8AFCE86401D9.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/D2065FFA-91E2-544D-B062-5F5C581F2381.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/D363E92D-9B6C-9340-A54D-86B05DC8D863.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/D857F684-062A-DE4C-A1C9-ED1FF6D40938.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/D9C181A8-E21D-1543-8601-0C6C261AD629.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/DCC5575C-2F6E-A64B-B25F-050D825037CE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/DEC01FFA-4D91-B248-8C25-1E63C4CB7ACF.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/DF4F8D22-952C-B642-AE90-434853909E41.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/DF8ABFA5-CF0A-B946-BD24-DF551C42F2FE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E2402479-D421-5345-B51B-8556D532EC34.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E28D1FE4-90F1-AA41-AC0D-885EA8F30FFE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E2C669C9-3D10-8044-AC14-29EA1EF70D97.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E37275DC-14C8-F74E-94E8-89CF62FA08F4.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E46E9B9B-7DCB-8147-8005-FC363F7F32A2.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E4D16A73-02A9-BE4D-ADB5-76527E0C3642.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/E7F8BB7F-C530-5C4C-A91F-50331B26A0DA.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/EB6CFCAC-4829-784E-9AF2-FC1EC5332C79.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/EBD0DCC8-CDC2-D741-8927-0A23D4E71AC9.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F3B638AE-BFD9-8243-92E1-46CFF2C0141C.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F448FC58-7C4A-3C4A-93BC-CC6A8B6CFEC3.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F48D0E68-4547-6946-B323-6AF81FD7D7DF.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F55EF8F5-D687-2F43-909D-7A0D783A004E.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F56F1C44-A11B-2742-9789-A9576F5D41C1.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F6053714-D3B9-2F4B-82B0-CBDC37A913ED.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F6488E8B-2D63-C94A-9530-416FABBAA191.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F6F9E483-7DF0-4547-B387-D2C8167EBEA8.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/F8E489A5-42CF-1E49-A401-178213928F95.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/FB4812DF-FE76-5941-A03C-BD7E48C52FCB.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/2540000/FE527CE5-77A7-0845-AD53-A7691F305DB9.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/30000/241D1740-882B-924F-839A-5EAD3F708C91.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/30000/3C430435-82B1-1B4E-A8BF-1193D196E1BE.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/30000/703AAAD4-ECDA-EF46-AD37-5261C2598859.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/30000/F533517C-27D3-EA48-983D-B54748930BCD.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/30000/FDA123A9-D6BE-E140-96C2-CB204580CBC6.root', 
        '/store/mc/RunIISummer20UL16RECO/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/AODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/310000/87904267-63ED-044D-92C8-69B254EE9C89.root'
    ),
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
    fileName = cms.untracked.string('file:SMP-RunIISummer20UL16MiniAODv2-00133.root'),
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
