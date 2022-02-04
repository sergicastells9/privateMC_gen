# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename JME-RunIISummer20UL16MiniAODv2-00008_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:JME-RunIISummer20UL16MiniAODv2-00008.root --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein dbs:/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16RECO-106X_mcRun2_asymptotic_v13-v1/AODSIM --era Run2_2016 --runUnscheduled --no_exec --mc -n 8113 --nThreads 1
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
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/007ECC4D-0FC0-754D-BFB8-DBD27DC1AA29.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/0DB12B24-EE6F-EA4F-AC46-A77816551D82.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/0FD8B5F0-4822-B948-8C6C-335652102035.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/12AAB230-B1AB-7540-A1CA-E8F2FEC56B21.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/2115DEA0-F8CD-FD4C-8C48-022E15A81F2A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/22FEAE26-4C6F-7943-9CE2-E6875AD57B4F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/4AAA5E12-84BF-2741-8055-B9C0D21AAC3F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/4C926C16-388C-074C-B0AE-698CF1C0B184.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/4C94C6B8-CFAE-E24F-81E5-8B03A375A0D0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/579DEF7C-E135-224B-85C5-387DB20153A9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/5A318B33-6EC1-BD48-BA3E-E4A776B216FB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/761A8B64-71EF-824E-85EA-EEDD766D6024.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/80763D84-67A0-774C-8023-FDE75510BA38.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/826705F4-8613-3B45-B052-745FEA3BD67B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/83924AC8-1D6E-8A44-9D23-E49C859D91D0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/88CED658-3F12-CB42-9F16-09638A361754.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/B256ADEA-5BEA-6541-AFB0-624372A6BC4B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/BA4F53DB-1F50-F948-B110-3E39BFC8CE60.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/BAF3CA2D-707B-0F47-9DE7-E91B3440361F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/BDB22B8E-77F6-9C40-B061-022AE83B3464.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/C8523830-0723-1546-897B-2452C2E9C72F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/D3A8B4CC-1243-7A4E-AD3E-C349336495C9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/D4C97711-7BBB-844A-9246-0122B33D67C1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/D92006CD-9EFF-6240-A72A-77EB42DCDF35.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/DAFF9E77-2991-0C4A-84E0-1EDCB7E7D487.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/E331EE86-12C1-0445-8558-B544D716E886.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/EDF68E97-280D-194C-8284-EFBB59D9648A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/00000/EE9A3A49-3F09-AF4D-ACE1-E3031584E56E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/06DC6D81-A04E-D442-A464-D49468BF6DD7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/09D8A426-0497-0B4B-AC66-E2D651E741BA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/21159702-42B4-C845-96B3-23283D69B044.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/26F8E4F6-D255-D447-A806-1B5743DEC0A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2C6B5353-B238-CA4C-9AB8-C24AE1FC5E7B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3C92AAC9-2FCA-574B-BAB0-918B120784E0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3EA1154F-BAEC-804A-B479-CA718D280062.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/40A14151-91B0-834C-9A78-C6CFD04B35D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/546DD887-2B3F-0447-8AE2-9CCDCE231CD6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5803C8FF-096D-834F-A0C6-A3E1E33920DA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/645231C1-80DD-C34B-9564-429290DF0B92.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7639D11C-21E5-734C-8FE8-9040F833671A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/79E5D9DE-7444-0146-947A-22FB7E05198F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7A9EBE46-2A61-FF46-A705-1CFD44673B9C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7DACEF61-9436-3B49-BDAC-6C376C3F4256.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/848883AE-AE49-7D49-B01B-06C7477AFE2A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9B55D2A2-B854-A94E-9EBE-ADFA92991628.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C0D5A81A-737D-9E44-826C-6938DE15CACA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C3797527-E6D2-7244-B812-8A5FA91484EA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CE62B848-1D9E-0A48-984A-19F30BCB5CCA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D7C7C7FD-BFF1-BD4D-942D-0905DB822910.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D951F7CA-0C30-2247-8B25-E3FACC1239AF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DEA09FDE-542B-2E42-AAF6-8C7F4F7F1631.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/EF566FB8-B5E7-AC4F-811D-22774BE70366.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/EF8279DA-D579-0145-A5B5-7715837661F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FDD81C00-777A-1241-817D-DCCA627903FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/0818E505-47B9-F441-9F68-9B8FC2CD9A5D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/18854699-7464-DC44-AF30-63D9C6581CA8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/21F3DB05-E8DC-B64E-BA74-973667D72891.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2F739F28-3A94-A748-868A-A213DE331C72.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3DEA4B87-E26B-874D-8F87-6BA0E44DD4D4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/45986146-D1F3-5044-A397-4DE609173C6C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/51C8F23B-0619-0043-B5BE-16C47CCF3930.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/53AC8E6D-88FA-4C40-8640-69AABCC82098.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/5644CEAB-66A3-F041-BCAE-4781633AAFBB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/5A4FDD3D-B549-D64E-B9A3-902D0E10185D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/60F79DC9-5D39-C148-95D1-D0B88F8A8901.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/78F0A3EE-803D-6844-8F08-ED38A4549819.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/81873F90-86DB-0A49-9445-6401E7F6DD91.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/98029C2A-0146-D94B-B120-D1A0D7714A3A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/998EB672-0BDC-0E4A-B0E4-2CF7D8AAAFF8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AD54BD84-660A-D247-A62F-A6DEE172D434.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B9C29053-2727-1B49-9BB6-1D432EE452FB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/BFCBD246-99E8-9E43-AE76-23CB82899906.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C959D4C8-4AA5-EF40-9FE7-FAAC719C5848.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F1774C3F-318F-B042-A4B6-B5F8A2C60C13.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F413AE13-51B3-194B-B6ED-C1382BC488CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FECF1696-2BAB-354D-BB17-C9A767A0BDA4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FFDC6FCE-382F-184F-AC05-3094CFFB7609.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/04FD91D2-4D63-E844-BE5E-BCFCC069C707.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/055EAEC4-71C5-604C-8DC6-BB22D9F7C57A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/05ED9226-77A5-A644-B70E-FC2700B37E5B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/064F0D8D-AE47-E145-BEB5-A41044131F2C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/06E5D578-0E9C-6448-A87A-321E3DB4A9C5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/07D1EE33-EF4C-4444-A8A8-C65835BD349B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/08862D3A-FECF-6D44-8F93-F7830C3BDACE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0B1C6875-12E5-B048-BC77-59A7308B32EB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0BF749B8-AA6A-3D41-A6D1-88CD4D5422FD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0C4C38D5-DAFF-4542-AED5-AC58B950A424.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0C5AC2A7-851F-AE45-9440-B92C32558924.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/114A3CB6-BB25-AC47-B140-DD0F55AEBF6E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/12116BE3-81BD-5845-9088-D48184B23FF3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/180ECBF6-6DA7-634D-ABF1-D74C5C6D2370.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/18628610-E5BF-7A44-A61F-B2CF4B82FC8E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1B747E3A-6002-6144-B21E-2D57C0085D50.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1DE3EE13-112D-B044-A24D-43993C0A89BD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1EA5EDC3-7020-7D45-92D4-89E800CABC28.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1F262DB1-EDB2-CF43-951B-BB48F8E053B8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/212512CA-8C48-E14B-BAEC-A26CFB2C2238.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/23440D94-17E8-4A4C-B00C-1D95F344F26C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/23D928BF-EC64-C142-87D9-FB7AF77A25F1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/262C96AF-2BBB-974A-B54B-3AEF9102B177.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/29774944-AEA4-4B4F-81D9-CCCBC2668C70.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/29D500D5-1A13-4646-97CC-8BA7186FA9C1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2B1B8F68-E8F6-6147-B103-5B55DD416DAC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/312D5431-8672-A44F-92D2-6C53BBA1B548.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/314133BE-FAE4-9242-8678-4DEACDA97842.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3ACEB103-DE9C-004F-95E0-E188C28FA36F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3BD2F7D5-FC18-B84C-9BD4-958184BC450F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4141EAA6-362D-2942-A5DF-271B5955A2F7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/423B56B9-1803-AA4E-8DFC-DC83F08E9791.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4508AA32-589C-3440-A52D-62C90841FE16.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4591AA91-4784-234D-AA98-46C402BA638A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/45EBBEA2-6C79-164A-A744-50D1DCC69238.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/460798B6-84E2-2C4F-919E-DD349A1F4E47.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/469D70BB-42AB-424F-A821-90A0566E31D5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/47C1AE1D-E353-D640-B55A-71FB844D57F3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/484D5FFA-4848-8C4D-A18C-E426D4D4FE05.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4DB1EACA-E8FA-1947-968D-39E7C5750E46.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4E4AB534-8778-4A4B-B364-F781EBAC45A6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4FA50836-BD0C-444A-BF91-949836AC1587.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5196CE64-4B0C-6F43-83A2-0BE5F9FA1298.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/534EF0C7-04A6-BC41-BBFB-818704380E3E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/595AEDA1-3674-6745-B311-D8041D4469F9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/59E3A88A-AD5F-ED47-9876-2DF824D9E968.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/59FF08BD-5D87-A74B-A3CE-67D407DAD22B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5E849D2E-4436-A148-8929-4EA88DD77044.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/60449111-E792-DB44-958E-82305D6FC12A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/613E1F21-8468-7E4C-8BDB-F2A94CE3D05E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/629E23A3-8CF2-2E43-8543-13D5E52E600E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6670A271-125F-0C46-B165-E2D5254548E4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/68072496-99DA-0F43-8403-13F9DD395377.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6AD9F158-FD56-4A49-B15F-51A2DC697016.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6BC78974-E3B3-E641-A454-52841BDD64E2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6EF233DD-A7F3-9548-B662-312FFDE8B43D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/739BE30B-0F64-C844-8D04-7D655036934C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7BC27C4C-967A-F74B-853B-30BB2CC6895F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7FA138FB-7787-5C4A-87B4-3E928352AC71.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7FF1AB2A-1627-AE47-BD37-D0052355137F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/827F6C84-60DD-D144-9BCE-A06B05E33975.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/85B21610-E34B-8342-BF47-3756AEF188E7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/88034F43-69FF-2143-9D27-348674380502.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8D088F4D-D780-6347-9439-68EADC8C850D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/94F7F831-B77F-E647-A3B2-0ADD088269C9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9CFA2BB5-25C7-F74F-98D2-142B25DD7D25.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9E9A7567-9536-C146-B2D0-212FCB2B620B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A1612A3D-920A-C44F-B576-097BC0BFE641.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AD4410FA-7547-1B4F-A191-3CE7048564B6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AE199008-DB44-B344-B628-5BCF59F0C90D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B5D4985D-48AE-A14F-B0DF-ACF64984F6D4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B9738B4B-59C1-184D-80C4-61E1814184ED.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BB0F732A-629E-5146-92FA-408DCACF6E06.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BFDBBC13-2C98-2F44-9675-DFCA392540D1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C1086417-2AF4-1F42-A16A-B49BD7B239E9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C22FB3A3-2571-7A47-880B-3CA63ACB745D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C73D88A0-FE87-5840-BB21-B741C76B9171.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D24A2BD3-F1C4-4A43-A607-9A91C14FE5D2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D471C047-0B7C-644D-865A-09527E39BA47.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D518EB1C-FB08-174E-9982-12B0F5B53827.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D621B321-649D-7E44-AB3C-C5B9D7492A88.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DC2330DA-A2C9-F146-85C3-BD7333AE7CBC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DC8A2BBD-14FE-8F41-9CFD-2FEEDE39CADF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DD2FEF39-56B9-9542-B3D2-AA7201BE99EA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DE52DE9F-E82E-B943-88F5-9FDAFCECCB13.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DECEBDF6-4A57-054C-AA0F-184284F1B18A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E0C6D0EA-CCF6-B44D-8BE6-37CFE282055B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E1030A91-CEF1-FE41-857A-7919C7AF9264.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E2E3DEEE-47DB-1442-9283-6162FB3FC0A7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E4158D62-1E2F-2248-855F-7AE170314243.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E5B9CF38-8503-1347-A268-0F0473961D62.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E739A547-87B9-D94A-A53F-BF9913AFB6F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E8EDAEB9-C2E8-0040-A3F2-004C7551737D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EAE69512-0B98-9E46-8012-8898F5BDF8B8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EB936803-0621-3740-A377-52731CBC10CD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EBAC464E-2005-B74C-B435-962D7782FD1F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EC63CB8D-4209-3549-B0B9-7A714956E462.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F960FA6C-DEB5-FA46-AE79-BE4305101C5C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F9D25BA5-5DFB-6241-BC94-1FDE0158053A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F9E2D1C1-3B7D-354B-95A9-1FC5AED3F71C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/280000/FA22CAA4-6F31-874F-A8AA-464502C788C8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/011F7C3C-6493-1543-864F-926CF2496386.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/013829CA-5320-FA48-BC53-CBEEFDC83E52.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0144805A-8C9B-ED49-BD9C-C423F6A8C63C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/01D8A633-2A9B-1F45-87DF-FE7EE9FE510D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/01F74987-61AC-2D46-9570-0584896FC41E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/02264353-9AB0-7543-92B1-79E5FBBB8FF1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/03F7F072-B003-C64A-B03B-8FC67EC8FB5E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/04DC56D1-AB6E-A345-A2D4-E612CB31B17D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/05C6DC1A-CD50-794B-B3C5-DDF26B40EB10.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/064B630D-5EEA-7F48-80E0-EE6C8225D3DC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/06590DAD-B1B9-0045-A3AE-44E5C749DBD1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/072BFC1E-3BBB-F648-B4FB-340F4FB4B6EE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/07E7A82C-4497-6B4F-A3C6-324213B1B854.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/09663A4F-A0AA-B64B-9B19-A133D5D8BC59.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0A50886E-BBDC-1246-895D-46E84B6BBD4D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0B63819E-7D70-4E43-9BC6-234C93FC8D0B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0CCC6A4A-F68B-A44C-8F38-0F63D744DB7F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0D612DAB-112F-3545-B77C-20C118CB5F4D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0D7EF722-5155-A245-826F-BEF99465BE1F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0E386042-7B92-494B-8B9B-50B76FBFB48C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/0E6E046A-48EE-8848-AC22-9ACD715F7886.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/100CD4FC-694E-D741-ADFB-F2471775D1FF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/11594A57-57F0-324D-B2F6-970707A7592E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/122474E8-D4BE-5641-8B55-51953B66774C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/151EC091-4698-CF44-A50C-1F2DCD8D8119.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/156F2342-554C-F14A-B069-790F630956B9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/15B49EE3-BAA1-C743-B61C-9F80C4B9E2A5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/15B5B121-0ACC-A141-9419-354A1D944095.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/19A4085F-5309-D14C-9690-38993B46EA6B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/19F932AB-7030-F34D-8F34-1C6EC135A4DF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1A5865B4-4C03-0C49-82B0-4C74DC2B68D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1BC0048E-1C74-B744-B1FC-D398FA8DC046.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1BF17C1E-D2B9-984E-8411-4B6BB75E2319.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1C16F12F-BC27-A641-922C-7C19DFB14B18.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1CD00E32-B42A-1446-990C-46B7E404317F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/1D30A0E1-A01F-B44E-9218-720C17199959.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/20073171-1B1D-D941-BFEB-0CA06122240C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2322F922-745B-AE49-81D1-A001EE6DD8EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/239AE600-98ED-0F4A-85BA-D96F170923E5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2671C8C1-26E8-394E-A094-EE9DE4C72F94.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/269B2589-9F63-4D43-8F8C-45287B65333E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/26B114A9-E62D-894B-9F42-CAD2828FE2F7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2731E412-B6E2-8843-81BF-00C474F270A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/28B62CB9-946C-DF4B-AE17-A7830DB995F1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2A957967-992A-904B-B73D-C3288AFE2403.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2AF723BD-7A31-3A41-A962-64135A2F5B34.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2BABCF12-9C3E-4848-987E-2816F2B7D842.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2BBC74D3-28AE-CA4F-8F40-8227029C355E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2BCB19EF-88AB-0449-9049-0124C0E15EE0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2BDA60C0-4351-F843-82E8-E61A9C66DC2F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2CD0CAB3-7736-A74F-9888-1464F5A57C15.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2CE4161A-8C14-0B42-98C1-CAE2894F8671.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2D42F4A7-C665-8B45-BA85-6F15A0CC59A8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2D8EDE03-D588-6345-9094-A238FCE2D662.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2EDC1C77-65AE-AB4E-B2C3-F4CEE5889C6C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2F3CE4B9-51F3-194D-AA3E-43117FFBF2B2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2F4ADB0C-9FED-A646-8A8A-0E7A2E9C6C74.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2F72A023-9D81-C747-933F-6D4C379F5FAC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2FBBA6DF-794D-F945-9495-045124315E86.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/2FDC525B-C244-AB40-B509-52EA022E1020.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/30EB4E0D-CA78-254D-995F-962DD6C076E3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3106858B-BE12-AE48-97F5-1251E7AD73F7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/328B1A1E-A2DD-4543-9620-9D877602B4F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/32C0F948-C3F2-F844-A532-FC8440224DAC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/32C35146-8AC9-D64C-85D7-0268F0B44508.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/34F54CA9-287B-A542-B054-8354075F21D7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/35EDF786-5B36-8543-AF81-797EAA00825E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/364FE247-34DA-8342-90FA-DE1996AD428B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3795E34F-0BBE-8148-959F-CBA64568A87D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/39339694-4D17-5B40-AF27-CDCD0D2B9608.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/39FD8A26-4F54-B242-898E-B74ED170F84F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3B9D84FA-745D-AE46-BF3D-7964E0BE3DAC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3CA8B2AB-D436-364B-BE9E-9CCFE1AC860B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3D65BBED-682E-AC47-88DA-7CE1F315D2CE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3DF1C571-D2B1-E146-9F2C-C15432F89E1B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/3E8B768F-0A9D-2E4D-8F82-1C631C06487B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4108F452-6A74-054C-8C23-B5A0C23ED830.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/432E4D18-E54C-D840-AF87-6EA39B24FCE8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/44C7655F-B7DB-6F49-8FF1-AA832AFD3A6D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/492DD31A-A639-1748-A4A4-6E4437A94667.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4A05479A-F15D-F549-A3CD-FF217D23018E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4B6D399D-BE49-E540-97F9-5AFFBF217374.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4D1CE6FD-4AD1-FE44-B55A-1CF52BFEAEA6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4D4B47F5-114F-274D-81E2-9D2DB3984269.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4D616E36-B491-A34E-97F5-B117683A5B85.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4D73EFDE-E19C-CF45-8DA2-88A5AE637F54.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4D8DD7CF-4725-4F40-801A-A788BF978991.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4E06A3A4-4458-664B-A0F1-0325A10B4AD6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4ED7371B-8C94-2042-97DB-CB92AE3E54F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4F230BF7-5F2D-ED43-B626-944F1E815187.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4FE458B9-9330-BA4A-9ADB-904F3D4CB118.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/4FE6270F-C441-744E-BA33-A5C4BD10BA6A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/51A7D44B-DD97-E247-BE79-1F1EA4B8603C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/52284484-CAA8-4348-8314-168A4F0AC0A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/52D9B331-6649-5347-BA15-CD20167CF1CD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/535CC9C3-38E5-A349-9552-8C379456D8B2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/540DD58A-0552-A040-94C2-0E252A9B1F6B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/54ACB552-F64F-4E46-A6A7-5017DA4ACEE3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/54D1A533-94E2-E64C-93F2-2A7243D8EFCA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/55E20F30-6A92-E24A-9F48-F1F7DD212D12.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/56BDC343-4E42-3A47-827C-5F6DE6DA712E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/575A6E1F-6F5B-2E48-BAA2-D2E31EB218E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/589680EC-419B-9548-8E18-AA9E1CCCB80B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/59A00883-787A-8344-B0F7-3DD07A2964DA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5A772729-A9E0-B54E-A295-C0BB02194096.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5A9265D5-676A-9145-9D7E-1FD36C381196.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5AA1BA8A-35AF-F946-ABD9-BEF3654A393E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5ADAFCEC-57A9-9945-A462-D50B89617A31.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5AE4628B-46D2-2147-8D63-F0AF6FDCAFFC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5B01D44B-45E6-5143-AE18-C95F4DEE3221.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5B78C560-DD6C-1144-B9D7-B410B57E5012.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5C570FAA-11A8-C841-9361-DF18C5C83646.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5CA4B0F0-EA13-F648-9B62-FFDEB370E9F5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5DC1E948-57ED-F041-BAC7-C0C1C629CB31.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5DD08BAA-9157-D64B-B8AD-047FA9494EF9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5E0BBC6E-2749-8F40-9497-7D5E6B7D0948.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5E8EB0A6-22EB-AE48-86A7-60BC499CFB51.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5F3E6129-1652-6243-9458-2ECD58C2232C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5F43F5FD-5774-1042-827F-867E0D414B29.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5F68DC8C-40DD-E640-99EF-23B05C25F29E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/5FC957C6-1D95-764B-920D-952922241444.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6215E447-4986-1144-9902-6043A3D4E44D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/63415D3F-B7F3-0E45-B37F-E707AD8AA8F5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/63808F45-D60F-8D4B-8140-CC2349FAEA96.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/63B0F16B-3E71-B842-B5E0-55EDAC315022.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/648975CC-6981-E645-8334-42AA536B856A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/64DCC4E4-6035-F74C-9434-6DA077E1A772.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/65276D87-C941-374E-BFDA-B782E646927A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/66CC316D-282D-7845-902D-B70D38E52F6A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/680DD54F-EF86-8344-978E-81E0C4DAE1F1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/687B10DD-C166-F043-AF02-AB2FB2F5CB06.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/69323CAC-F56F-5E42-97B8-7996AB5B93B8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/69CD811E-E52A-144B-8F66-31191FA4F34E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6C3ED2A2-12DE-C643-ACE5-6DBEFCCC3024.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6D88FAD3-3C2C-2B43-96F5-80B8A0ED46BE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6E8D9411-15E3-2743-867F-D6C994F1A962.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/6F12544E-7AFE-1540-BDBC-5127B5385900.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/703943E5-4316-2040-9E66-B876A689951F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/71612032-AC27-6E46-A4F1-3DF455876F26.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/71BE3600-D72B-3340-B869-5CE504A7093F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/71F0319C-B3D2-FE40-893C-3153F350575A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7218BC65-A613-EB4F-8E76-158CF7F2315A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/72A78B71-F71B-9549-ABEA-8F5CE063C1F3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/73B8DD10-CC68-A740-871F-E3395828CAB1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/73E5A426-E4C1-804F-AB15-A9F64E8FB577.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/73F0C7D2-794B-1942-BB9B-22E8E9277A9F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/743BB651-0706-9345-8622-FC90DBDCC783.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7493B9E9-6C0D-3948-9982-2465663867A9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/74ED47B9-9E5F-3A47-8CC4-919CCC68806E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7521ACBC-EEC5-754D-AF58-F6AAC8C3DEE8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/76344719-EBFA-2C41-8D0F-23AD64591BC5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/76E03E66-D420-1943-82A0-80C3AFAC1ED0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/79079177-A5AA-104A-959C-A76A60A1905F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/79159FA4-0FE4-B948-B8D0-D172EA2EEB22.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7A0A3641-ECE7-5E45-A019-091EEE64FBAE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7B46C778-7AE7-2845-B06D-A049A939100C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7B8E7E33-59AC-B248-9E7F-DB9077B5010E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7BF7FBE2-0DEE-8048-85E0-6795968A1557.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7CC3A652-00B4-FF40-912A-8B444F89B945.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7E7EF29B-B731-0144-A48A-010F07629749.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/7E8BF510-D7A8-4B44-98A0-735CD3ABF389.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/812E066B-47D0-3C47-A864-F060CAE72208.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/81D48CC4-EE76-DE46-B510-98AD74ACB23D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/81FB47D8-6EE4-E944-80C5-45C59434FE71.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/82B84BE3-80B6-3B40-B734-28C54FABE1A7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/846DF598-21E0-144B-AB01-EB7DCFD40CBD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/84D6C87C-9500-1947-8464-2487381CE1E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/85CF5B9A-3DD2-784F-BABA-6BECCDDD77FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/85D19B5E-A6EF-D84F-8062-2A1BE90BD027.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8635BA76-3D86-9445-9E2D-29E9EE1855D0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/87B25A41-F73C-8D44-8322-AD6CF7CD4905.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/885C30A5-8B5E-DC44-A927-96C18CDF13CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8870D07A-2EA1-504C-8493-BF1059CD17BB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8892A7E7-2DB9-3C43-88BA-0099A7073B70.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8B3FE530-5A2E-094B-9B7D-051C98350E94.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8C12C873-AD1A-5645-88C9-CDFD7F4B34C6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8C6A0E8D-88C7-1844-8787-FC33CBD79D21.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8C9B1548-63AD-634B-B01C-53659EF7C5B7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8D7381AB-C61C-5B47-AF2E-465C49C9D97C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8D780D56-712E-8440-8E5D-59AE442A993F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8D822A3B-B5A4-6C46-97F6-EF2B2B03E03D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8DD0B6E9-A4B6-9544-95EA-7BE9EF6C6BE3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8EB8BB93-9E69-4640-B6C5-8D4DD6B0A57E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/8FF77946-0906-644A-A157-04D45B283867.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/90AA2DA2-BD8E-6542-89E7-33C255992FF2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/90E88E68-13E7-854F-9C51-6FC29CC65624.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/91980DCC-F508-AC43-9074-2EB34BA88A28.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/91AFB31F-E096-924C-818F-7A0B5FD8BB45.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/924768BC-2AA0-5941-813F-272D2EF1D4EE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/93AF2127-EEFD-C94C-A241-54033E4981B4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/95B53C0C-9A1A-814F-A9DD-83E926A12F10.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/95DBD9C5-4C89-1049-A024-2253AD0320E9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/961FD474-897F-5441-BC71-35D312B8F283.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/96222B25-7A3E-9D46-A56D-FB218398AF81.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/96843DCA-E774-4247-9313-7EE6723F12CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/96BF21FE-6DAE-6848-895A-16F7D01491BC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/97071355-5018-AE4C-897C-5BCA8AAF4CB3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/98ED611C-F07D-4A4B-8643-58C5AE7C20FC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/99271798-5588-B64E-8C1C-B0C305FD36C0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/998217E0-5534-ED4B-8633-858DCB22461C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9A5DE63D-6BEB-6D42-BD43-69C35A4E642B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9B76A8D2-7DD6-994A-9220-1E2BB866B46B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9D1C9D40-CBCB-1044-A678-6CD5CE70FF3F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9E5BDF2F-163A-AB47-B390-FB93BFA9438C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9E736564-0CE1-0649-8ED4-B14A453AEC43.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9F28750B-5624-4B46-82E6-D5D4CA47C974.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9F95C09C-0B41-C04C-AD0A-AFAC6A545DC7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/9FDA9A35-743E-2C45-8FB6-751871D0AB27.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A03DE223-E82F-F543-BBA3-D8F5E3138448.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A053017C-0075-E24F-B537-8971551D75D1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A056850F-D24C-644B-AF2E-A333BCC8E123.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A118FC1A-72CC-6845-BBE3-038DFE16C526.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A1BFD6A3-6118-784B-8721-30B33D23A302.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A1E6FA98-F3B8-5F43-A0AC-A47EAAF6017E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A2F8D07D-35AA-6C45-8F9E-FEAD1EE675F1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A3CFBDA4-345F-7345-8B8A-FF3ECC116BBC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A3F7739B-F217-C34F-9170-8ADBC0AE9BA6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A5306A74-07CB-C14E-86B5-761D49AF336B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A53770D9-346D-A247-ACF1-ACE6AE6DA6E3.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A62576D1-8F12-104D-9421-AB9BED43CB4D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A62D1AFA-D374-A240-A8DC-292D908675FD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A69947B9-7BA9-BF49-8433-38158B41F016.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A8103124-A859-1843-8670-A1C0481AA053.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A83B58FE-5B37-D840-8DA2-986F9C9D75AD.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/A96EECA5-9614-9843-8EC3-DE9AA93A00AC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AA623797-FA09-1F41-82D9-48518115FE81.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AB01A602-3D3D-6C4E-9921-37E77EDF64FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AB80CAB2-C355-304B-BE82-2C20233DFC89.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AB9AFF0B-9BEF-7849-8298-111911E88F62.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AC05F292-CA19-D743-8CE2-454C34263CAB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/AF32A4BB-F533-0349-BFBC-320716FAA0BC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B01991D8-8681-E547-8E13-34BE3172DC69.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B0B2D3AC-BE6A-C64C-9111-BD08A4C4BAEB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B11D0E88-82D3-CC4E-8177-79964A6E4859.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B1F4F51D-187B-A641-BB81-714AF496C47E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B1FCA4BC-28F5-7440-AFB5-845FA0D5E446.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B3F5997C-F321-F847-97C1-3ECDA8D3C15C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B58C16E1-FCE7-8B44-A5D5-DEEE3D93E267.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B5C8B527-9351-2B4D-AC3F-94C006190A7B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B5E729D8-0005-4B4F-9A6E-96D957340E0F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B5F2DEE4-E685-344D-860B-A7B046B9DFD6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B6B28DE2-FE6D-7C4D-A4A5-BA3F43B6E89C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B70C42F0-BC37-3C42-A863-1453771AC336.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/B8C5C3C9-CCED-6F46-AF27-D976FB336EDF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BA1CDDED-AA1E-1044-8689-6854D9538A0C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BD9FAE21-53E8-724D-ABE2-88ED930203B0.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/BDACA8F6-ECFA-3148-9901-230C1BC1E5DC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C034B575-8660-3947-9A47-B2791F29E0C4.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C1DD1A20-ED16-E048-8B43-E9C387085E5F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C22483F8-527F-944B-8C72-4CCFA99B2BE8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C2A699F9-1269-064E-814D-71E2504622AF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C411A5C4-BE4E-E245-A89B-B4D11E5F8A67.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C5A44E2A-A50B-D347-A5FB-E3D4A03791D9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C678FBA7-E5A2-5446-A483-16860574C63F.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C91504A0-CBD1-D841-8CBF-65EC446C1008.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/C96EAD14-2FE5-8349-BE09-D9ECAF834B6C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CA73055B-9C8A-1949-9629-07D70E53B505.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CBD527C4-83A8-F547-A768-52B5539D6AD5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CCC0C9C3-B697-4E4B-9DAF-05692BD0E0A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CE1DE889-E0BF-4E49-BC25-ECAAD74CFFA6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CE7762F7-12EF-4B4E-ABA7-2D195EBB508B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CE942035-42F5-8541-84B8-BD56D00F9624.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CEA3A96A-9BFB-624D-B47C-9BD8073D6189.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CEFFF1D5-D937-1244-A77D-837AC3846688.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/CFED6487-D4A5-9140-B4F1-1BD98E0CB0F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D1A6BAE7-F8C0-6B43-9E16-A2BF36CA4D75.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D2A8DAEF-ED51-3849-A366-51BA27896919.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D2F7B42A-4494-B544-A7DF-56F006214E68.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D2FBBDE2-23E4-6047-AB8F-02369B5E2BEC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D425F939-AD0C-1443-B126-3281C218403A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D45D2785-FAF8-5848-B2D7-5E58EE744968.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D48D35F9-BB79-874D-8C91-3286FA32D2EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D5C10BBE-981E-8E4E-8DCC-03A22F2FB1AB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D6F6DCEA-D20C-844D-90E8-AC8407FFDC78.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D7A7E95A-AE39-B846-96C5-6C5962725E93.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D7BA858F-60E7-054E-ABB2-2B73C3378D10.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D7C8B7C1-14B9-074D-B6E0-BDD5AB5C5FDA.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D7EE6A7D-728F-234F-A94F-60BEB4460769.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D8AB03FC-7405-D147-8D0E-C604A013A328.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D8DBEC4E-B1DB-684A-99C7-DABD6BFA3F8D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D8E22103-53A2-C248-9B16-4544776DCDED.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D9BD4C77-708D-AC43-B334-BD680D6920A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/D9D69836-306E-C34F-9152-3906B80AA821.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DA15F2EF-C787-C944-B80B-C5A8CAAE5269.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DA754D58-2349-B241-AEB5-F4C5FFCB331D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DAA3DC08-8D78-1C47-B683-3E513F93BD3B.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DDDB6FD6-54E3-FD4D-A56B-A1D119F4E7FB.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DE98CA67-55BC-9647-9F08-E3AEA96DE877.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DEC84FF2-A87F-DF43-AD8F-44D867F977CF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/DFF82E74-08F9-3742-9F5B-672D1E9DC221.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E03DD382-D6CC-EC48-B76D-4EAC30EE664D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E058D079-4282-2C4E-8315-650F08D4AFA7.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E073F288-8B65-CF40-82E8-58A9F2056EF1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E097D0D4-5EAC-8640-8EF4-5C1CE3E79FF9.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E0B4219C-F53E-5748-97E2-9444B50566C8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E1158B91-D89E-2940-8DAE-C1B94F4448E1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E1398E37-DE4F-054D-9FB8-984470FDF57D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E19B1B65-335C-114E-AB3F-D754D98AF2C8.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E397D3C4-97BB-3645-9CA2-AD982518A15D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E409DA62-1678-7D48-837F-33743000A444.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E46D0A85-0DF3-1844-A9E7-D783448388B1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E479F428-8396-7340-B3EC-52EC6536BE2C.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E688A150-1634-6049-B41F-D5B0108B0AED.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E6D3DC18-9DB8-9345-8787-704F7FDC6986.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E6ED19A7-4F5F-6D4B-9343-465DEBCCBE45.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E7D58FD6-24E0-A743-B1A9-470D35292908.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E7D6DE81-95A1-DC46-819B-3D7E109C94E1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E7FE933D-952F-6B42-8624-759BC6FFD569.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E8AB36F7-1D13-1B45-B3BC-6AD235B32E51.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/E906A813-8B55-E84C-BDE5-B848A4E8718A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EA227536-3111-064A-8051-9200E1AEC678.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EAA22A89-2D15-9F44-A435-D3ED844A6B56.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EB21E1E3-F721-104F-80FC-B4AB3042BBD1.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EB7E9E8B-038F-CC45-9775-25E02DBD038E.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/ECE2FE67-95C3-914A-A211-BBD9D1686E64.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/ED87F815-5D27-6C4C-B89B-624AB1AE3783.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EF55BCAF-8328-E24E-B71B-C4196939D3B5.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/EF6FC1C9-F701-9A40-8426-9BD7BD62A8AE.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F229F211-6C55-2C48-AAF4-F2067B4C7205.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F35A26B9-4DCD-7446-BE7A-74BE38497179.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F460D299-A3E9-6444-ACEF-6FFC129B2418.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F4B7374E-8F71-774B-B2A4-78FCF1F932EF.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F6B84A07-9598-DC49-B439-CF9308F07580.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F6E5CA35-26F1-8A4B-8960-C942B7918A95.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/F8FF5717-88F0-A842-B204-D1750484162A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FC6540E1-FC8B-3341-A4AD-B0EFF3C8D995.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FCF76371-45F6-7843-B60C-EC07AE0F4B79.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FE2D3FB9-F3DE-DD42-BC76-FEEB036C6738.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FE40D503-9FE0-2845-BF15-A0CBA8F8445D.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FE9F3819-6D47-2D43-A2D7-FE1FA6F6588A.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FEA8E450-0307-4141-B05E-0987D0E0DD18.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FEB96CFD-FA25-7B47-85BC-261BDDEDA391.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FEEEC449-A7BA-224C-B69C-A99D5A3BE201.root', 
        '/store/mc/RunIISummer20UL16RECO/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v1/50000/FFBFC6DC-A6A6-3F4F-B35A-23682E8FF2DB.root'
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
    fileName = cms.untracked.string('file:JME-RunIISummer20UL16MiniAODv2-00008.root'),
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
