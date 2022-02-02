# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/HIG-RunIISummer20UL16GENAPV-00061-fragment.py --python_filename HIG-RunIISummer20UL16GENAPV-00061_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --fileout file:HIG-RunIISummer20UL16GENAPV-00061.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step GEN --geometry DB:Extended --era Run2_2016_HIPM --no_exec --mc -n 4087 --nThreads 1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_HIPM_cff import Run2_2016_HIPM

process = cms.Process('GEN',Run2_2016_HIPM)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4087)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/HIG-RunIISummer20UL16GENAPV-00061-fragment.py nevts:4087'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:HIG-RunIISummer20UL16GENAPV-00061.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_preVFP_v8', '')

process.generator = cms.EDFilter("SherpaGeneratorFilter",
    FetchSherpack = cms.bool(True),
    SherpaDefaultWeight = cms.double(1.0),
    SherpaParameters = cms.PSet(
        MPI_Cross_Sections = cms.vstring(
            ' MPIs in Sherpa, Model = Amisic:', 
            ' semihard xsec = 39.062 mb,', 
            ' non-diffractive xsec = 17.0318 mb with nd factor = 0.3142.'
        ),
        Run = cms.vstring(
            ' (run){', 
            ' EVENTS 1000;', 
            ' EVENT_MODE HepMC;', 
            ' ME_SIGNAL_GENERATOR Comix Internal;', 
            ' EVENT_GENERATION_MODE Unweighted;', 
            ' BEAM_1 2212; BEAM_ENERGY_1 6500.;', 
            ' BEAM_2 2212; BEAM_ENERGY_2 6500.;', 
            ' PDF_LIBRARY     LHAPDFSherpa;', 
            ' PDF_SET         NNPDF30_nnlo_as_0118;', 
            ' PDF_SET_VERSION 0;', 
            ' PDF_GRID_PATH   PDFsets;', 
            ' CSS_EW_MODE 1;', 
            ' ME_QED Off;', 
            '}(run)', 
            ' (processes){', 
            ' Process 93 93 -> 22 22 5 93{2};', 
            ' Order (*,2);', 
            ' Enhance_Factor 2 {3};', 
            ' Enhance_Factor 5 {4};', 
            ' Enhance_Factor 10 {5};', 
            ' CKKW sqr(20./E_CMS);', 
            ' Integration_Error 0.005 {3};', 
            ' Integration_Error 0.03 {4};', 
            ' Integration_Error 0.05 {5};', 
            ' End process;', 
            ' Process 93 93 -> 22 22 -5 93{2};', 
            ' Order (*,2);', 
            ' Enhance_Factor 2 {3};', 
            ' Enhance_Factor 5 {4};', 
            ' Enhance_Factor 10 {5};', 
            ' CKKW sqr(20./E_CMS);', 
            ' Integration_Error 0.005 {3};', 
            ' Integration_Error 0.03 {4};', 
            ' Integration_Error 0.05 {5};', 
            ' End process;', 
            '}(processes)', 
            ' (selector){', 
            ' Mass  22 22 80. E_CMS.;', 
            ' PT 22 10. E_CMS;', 
            ' PT 5 10. E_CMS;', 
            ' PT -5 10. E_CMS;', 
            ' PT 93 10. E_CMS;', 
            ' DeltaR 22 22 0.3 10', 
            ' DeltaR 93 93 0.3 10', 
            ' DeltaR 22 5 0.3 10', 
            ' DeltaR 22 -5 0.3 10', 
            ' DeltaR 5 -5 0.1 10', 
            ' DeltaR 5 93 0.1 10', 
            ' DeltaR -5 93 0.1 10', 
            ' PseudoRapidity 93 -6 6', 
            '}(selector)'
        ),
        parameterSets = cms.vstring(
            'MPI_Cross_Sections', 
            'Run'
        )
    ),
    SherpaPath = cms.string('./'),
    SherpaPathPiece = cms.string('./'),
    SherpaProcess = cms.string('sherpa_13TeV_ggbjj_Mgg80-13000'),
    SherpaResultDir = cms.string('Result'),
    SherpackChecksum = cms.string('d35231914e0786e289b20c634edaf110'),
    SherpackLocation = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/sherpa/V2.2.5/sherpa_13TeV_ggbjj_Mgg80-13000_MASTER/v1'),
    crossSection = cms.untracked.double(0.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.int32(0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

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
