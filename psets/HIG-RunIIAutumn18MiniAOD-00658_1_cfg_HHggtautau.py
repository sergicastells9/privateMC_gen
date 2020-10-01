# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM --fileout file:HIG-RunIIAutumn18MiniAOD-00658.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename HIG-RunIIAutumn18MiniAOD-00658_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 8597
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PAT',eras.Run2_2018)

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
    input = cms.untracked.int32(8597)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/5A468BB0-E80A-0044-8D37-89B83808505B.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/32729F23-5FE1-F744-A76B-35CEFB7D9B3D.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/AB561A02-872E-3741-A331-E382F73CE9DD.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/AF258D94-52E8-7B4A-BA73-8ED1A8D242C5.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/D04BB678-BD1A-C142-A0BE-064E054C0A53.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/1D3B6F91-07E3-7546-B764-7387810A4CA8.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/94222857-0D31-F243-9772-B538062B32D4.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/366DBFE3-5676-CB43-AC3B-C70374E0938F.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/51EE3114-5532-AA47-8BF2-624C1460AA5D.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/39668508-FF01-794E-A86E-8BE15A6D886D.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/58DB080A-CE0E-E34B-B5BC-FE1E9C8C002F.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/B2E40E29-C418-0E42-8637-446F07C263F9.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/8FFBA04D-522C-AA40-A77F-52F277E92484.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/0D74F678-9A8B-EE4F-9430-04DF393A5EC4.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/D2603DB0-7F49-AF4C-A671-652CEF8CDBC8.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/4F427913-56F5-4549-AB27-D13A87AE0922.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/734AF984-ADE9-FF4C-9C83-5DBFF8F9E5CE.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/0CCE8A35-EC4D-164A-ABC0-B4C62AF83F3C.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/FEDEC1C9-A634-5046-8B94-46F842CBEBC8.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/6FACD015-8C99-7A4F-A8DC-B870E25615A1.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/2EF1EA5A-A244-9740-9C6A-B7DC02F6C49E.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/166D9140-C26E-9B41-85B3-35C2D8BF0FAF.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/95D2C2B1-55D5-0246-9ABB-B6A1A803D788.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/87600937-DE8F-7E4E-ABED-5295DC9AC47D.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/E55CB265-8C37-934D-98C3-81372D1A2B02.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/D435B0FE-C65B-9F4C-851B-46F8CB343FF3.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/FB7ABC51-61B9-954F-8E2F-A6A42ED90ECE.root', 
        '/store/mc/RunIIAutumn18DRPremix/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/70000/F3DA8179-775D-4243-85D6-9CAC9D4DE3CA.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:8597'),
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
    fileName = cms.untracked.string('file:HIG-RunIIAutumn18MiniAOD-00658.root'),
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
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
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
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)

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
