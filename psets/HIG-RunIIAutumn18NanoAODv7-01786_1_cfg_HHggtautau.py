# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM --fileout file:HIG-RunIIAutumn18NanoAODv7-01786.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v21 --step NANO --nThreads 1 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename HIG-RunIIAutumn18NanoAODv7-01786_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2018,eras.run2_nanoAOD_102Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/098F48DF-3235-3F4B-A243-8E7DC20DCB0F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/68DC984C-500E-6643-B67F-877FCFFE414B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/77E7197A-5266-5048-860D-2A94E59EDD63.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/FBC68401-35E1-FE4A-8E0C-48A9ABC2B71B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/40BF0198-D2E8-A348-88E3-5D4FDF2D593E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/075BE895-C7BE-9348-A0C0-4C34A5EBB468.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/4DD5FDDD-D261-9348-87BD-AB23C67B9E9D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/B90F5817-5234-5F40-AB4D-B19F8C51524F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/9BE048BF-8C98-984C-83A8-F11A189F9C9F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/CBA9DB0E-ABA1-1446-8AC2-3001E7179677.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/4D276804-9E27-1643-B94C-8E612BDE0CC3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/6D041E21-8576-6D44-A83E-A3C671C898FF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/BF719698-5C3A-384D-8A83-609D09F79899.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/235F1025-C87A-8B47-8B3F-D2B57084C4EF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/F79AD898-3541-F64A-B891-F76F2148BFE7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/EC8491C7-DF98-F045-90D0-E81FD6FBEE8B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/4D854EC4-4B73-8F4E-B952-961F6C4856AC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluToHHTo2B2G_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/A9E51BBA-DABF-CC48-9906-42F78A4B6610.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:HIG-RunIIAutumn18NanoAODv7-01786.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v21', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
