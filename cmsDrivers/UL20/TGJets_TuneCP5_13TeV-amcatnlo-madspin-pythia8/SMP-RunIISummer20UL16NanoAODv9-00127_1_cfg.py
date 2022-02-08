# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SMP-RunIISummer20UL16NanoAODv9-00127_1_cfg.py --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:SMP-RunIISummer20UL16NanoAODv9-00127.root --conditions 106X_mcRun2_asymptotic_v17 --step NANO --filein dbs:/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v2/MINIAODSIM --era Run2_2016,run2_nanoAOD_106Xv2 --no_exec --mc -n 10000 --nThreads 1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2

process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv2)

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
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/09595236-F10B-DE4A-A286-18DBC665FE09.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/09E35316-DC51-8D40-ABFA-806F044B1442.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/117BFFF4-06AE-B04D-A36E-F412EA25EBB7.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/1E4A839E-056C-EF4E-BB92-A14912289158.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/2FF69894-3C3F-BA40-8278-8D8B70553824.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/31B633F5-42A5-DF44-8FCF-CE39C51CAD1A.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/3B61BE01-BD2E-ED4F-AED1-7F52F7F606E5.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/4CA1E70B-8A3A-5A49-AA92-6D4E29C76C9D.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/6050BB40-FE23-2C47-944A-B44C1A155DB0.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/6264947A-A93E-894B-8607-64FCED980CC3.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/63E9AAC2-E628-3D41-AC81-99C7673955BB.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/648A188A-1167-7D49-8C01-C2FA23463B9E.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/6B9C261F-8B65-A847-B86C-96A2ADB138D8.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/6D5C1EB1-6692-B449-AF5F-FB3041B374D5.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/6DDE7327-8DA2-324A-B3D9-6F2D3CE490B1.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/76568264-2D1C-4145-97B3-D4C65730DB7B.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/77688FD3-7AE8-8641-ADE5-41E271A07BB0.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/7F1BF1C8-33EF-414B-8D04-FCA99EF16F1F.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/893DE43D-1FFC-524B-8520-356CCC009CD0.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/8A8E596C-77BC-7644-8CA3-460B7823CF90.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/8C08E3FF-A94A-754A-8A6A-BFA691866C4C.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/9BFFE22B-9E5D-2F44-9AFA-E303B698B80D.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/9C8FA3FF-A8D2-544F-9C68-5D4CE1AFDD39.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/AB28C4D8-2ECA-3F47-AF8E-E0D0BDE3E421.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/AE2A0F4A-C34F-2B48-B6C6-6E081EA82D85.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/AEDDF10A-FFAB-1A4D-BA3C-027CB16CE33B.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/B0A15A65-D4D9-B24E-B297-BB49503C53B8.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/B499E94E-D9C5-4343-A436-C93D2A58292D.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/B4BD224E-30BD-3747-AE18-6F24D5557406.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/B90C1F1C-583F-3941-94E0-BB2ADAC12569.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/C4CFD77C-7A47-5245-8AAA-3000202DECA3.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/C66F0775-A224-154B-B254-C2CCFCC2FC1C.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/C6C8CF16-637B-044E-8599-1D4E58252209.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/CA4AF934-742F-8A43-A323-09FB8E4ECF2F.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/CAEDA388-A438-A24D-B197-9F0DCC5149EA.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/D7F8492B-FB53-304F-B790-B5B91FE89502.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/DC3A329D-6B7F-1340-8559-1737D5E5FD8E.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/DF0520DA-E42B-C843-B7B5-655106639357.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/E88DCCC4-A0D5-BB4B-A562-7B42FA3E79F1.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/E91FBD86-1F90-C440-AFB3-EC916FC11BF9.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/F4B4DD8E-79BF-3E40-A9A6-326CA94DA11A.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/F9179A02-5904-6A4E-BC72-B9A5AE32119B.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/2540000/FB0DC727-153E-EE47-9879-88E0EAC74117.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/30000/6570758F-A851-1848-A180-CFBA349C4968.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/30000/E8E5D214-B16C-874A-A2DC-834D5CAC95FA.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOEDMAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:SMP-RunIISummer20UL16NanoAODv9-00127.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v17', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOEDMAODSIMoutput_step)
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
