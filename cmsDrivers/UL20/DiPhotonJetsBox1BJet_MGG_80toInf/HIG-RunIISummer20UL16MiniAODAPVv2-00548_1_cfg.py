# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HIG-RunIISummer20UL16MiniAODAPVv2-00548_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:HIG-RunIISummer20UL16MiniAODAPVv2-00548.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein dbs:/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/RunIISummer20UL16RECOAPV-106X_mcRun2_asymptotic_preVFP_v8-v3/AODSIM --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n 6195 --nThreads 1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_HIPM_cff import Run2_2016_HIPM
from Configuration.ProcessModifiers.run2_miniAOD_UL_cff import run2_miniAOD_UL

process = cms.Process('PAT',Run2_2016_HIPM,run2_miniAOD_UL)

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
    input = cms.untracked.int32(6195)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/02D2E8B7-16E0-EE43-BEBF-98776F15DEA9.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/0987DA3E-B0D3-4E4C-90DF-E32CBF230923.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/0C823A21-F5AB-944A-A7A5-627EEC05EE3D.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/126828AB-A4E0-CA4F-A9B4-FF5CC73BC540.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/156C18A2-9106-3D48-BCB6-7733A036B199.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/17A01A15-0053-1D48-A64D-FC59515F2BB2.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/19C30B79-DB09-C740-B43D-7FD1F1E28181.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/1BAE1040-F622-4040-9CD2-345A7DEF5435.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/1D9A47A0-64AA-E442-83DF-DFC13B48E17B.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/1DE4CB3E-3887-414E-A6E1-16A0F6E4E2F8.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/1EBFEED0-B6AD-A945-B0EC-809E0B5B7D22.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/25800DE0-9D65-AD41-B49A-93AC049571B9.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/29A28EB3-E4C9-6E4D-8AA6-CAA12F159CB6.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/36EA64C8-1FD4-2443-A02D-1E7F1F03A1FB.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/3B384DEA-5662-9E4B-BD71-A6D20857AE74.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/3D565847-ED27-724E-B14F-E7646612CCF3.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/3F853A6C-CC71-EF45-ACA3-61643771A4CF.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/41F590D2-6681-3941-95A9-288D57EEA81C.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/445E5660-83DB-3248-97C6-B75E61356040.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/463FE86D-1184-D542-80A2-E2DBAC009CD0.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/497DCC8E-6C0B-3B42-B389-00F01DC77DD6.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/4B6B789A-F845-7F4B-A9E5-A1A560EEE7E1.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/4CF7F881-40FD-334E-A788-BB9884B4BD95.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/5466D437-43BF-EB45-A95A-BFF985481BB4.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/5B3599CA-35EA-0E47-8DD6-91C216BA316E.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/5EA49937-AE66-B84B-B4FA-75328F9E9D18.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/673BDA80-A1EC-BC4C-8AD6-7F9DE5632878.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/69EC0A28-0760-2A41-A559-454A6A8F57AE.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/6CB60D75-A771-F24B-87EB-E51C75152D22.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/6D4C947A-585A-ED40-B1CE-64BC42DDADDE.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/6FE1CC22-42AA-384C-8CFC-4AA86485710D.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/6FEDE9EF-8F72-8A4F-9489-AC63DF4F2876.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/70E03443-D603-DA4A-9630-9EDD94ABF5EF.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/789BD9ED-5674-9F4F-AD4A-A62B491161F5.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/7B323E64-A397-9F47-84FF-CD18272EAC79.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/80F8A367-E2FF-E642-A728-BF976F0D4BFB.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/8192DE90-4370-CA40-A513-6C81BF9B84B3.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/8626253D-252C-9045-BEE9-9A5FE30D0106.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/86ADE7FA-12D7-564C-A690-153FCB4D897C.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/956B4D6C-34F6-1145-8DE8-C86758B9A985.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/9958BFFC-3552-F248-8F6C-F334ADDE7AD2.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/99B8AE15-8D1C-1441-892E-9E330EB8C154.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/9B46BFA0-AF8C-804C-A32C-82B50FE8AD24.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/9EC6A47B-1FEC-6C48-B7D3-AA5CA6A06277.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/A32545FF-BC6B-9148-9918-ED0389E92EF2.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/A6EABDE2-444C-6148-BE31-59DC2033D159.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/A9A3FB64-C266-2646-946F-4E8D21F92FBC.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/AAF958E3-E361-EA48-A5D7-720E4CCF4331.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/ACEBEF01-0499-8943-AD1E-39248DBCA5D5.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/B6E49DCA-F9DA-1C4E-AF49-3F0AA4CEF0E7.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/BF0A2F0D-9B68-6A4A-AFAD-66CB438E356B.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/D2FC9190-2225-464E-B5EA-27C25395BC03.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/DC8421EA-E031-8B44-BC57-44A0F1A2CAAF.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/DD1EFC6A-D9DE-5846-AF5B-B014CA7943EF.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/DFF204E2-0904-2946-A600-E5F5D82F28B2.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/E035AC3C-BA88-684B-AB2F-53407EB330DB.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/E0C972F6-F45E-EB40-8019-DB27CC437111.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/E1FE7244-040F-E147-89DF-F3818E9B13F1.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/E2E20D6E-CB11-6040-98D9-E0417BC89026.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/E4F4D389-FECE-9A49-98C5-6898F25F080A.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/E82D7D39-7815-3B42-9452-07B0443AA732.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/EBEFBBBE-1F91-1A46-8FC6-F4742BB63681.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/ECDDD11D-EBB5-8547-B1D3-A9018F472CA6.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/FA427BC7-BEFE-E441-9B56-A0535FCD41BB.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/FD541FE5-BBDC-AD47-B004-385ED8E272AC.root', 
        '/store/mc/RunIISummer20UL16RECOAPV/DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-sherpa/AODSIM/106X_mcRun2_asymptotic_preVFP_v8-v3/270000/FFA8A50F-FAC5-4243-B700-2C6D29B2DC14.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:6195'),
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
    fileName = cms.untracked.string('file:HIG-RunIISummer20UL16MiniAODAPVv2-00548.root'),
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
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_preVFP_v11', '')

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
