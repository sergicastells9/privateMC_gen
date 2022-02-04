# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM --fileout file:TOP-RunIISummer16MiniAODv3-00104.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mcRun2_asymptotic_v3 --step PAT --nThreads 8 --era Run2_2016,run2_miniAOD_80XLegacy --python_filename TOP-RunIISummer16MiniAODv3-00104_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PAT',eras.Run2_2016,eras.run2_miniAOD_80XLegacy)

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
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/92CFAE68-22E0-E611-B693-90E2BACBAE58.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6C89BC76-22E0-E611-A9CA-002590FD030A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A0358B77-22E0-E611-B658-D8D385AF8ADC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA1AE36F-2AE0-E611-AD98-34E6D7BDDEC1.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A045B682-1CE1-E611-9F84-90E2BACBAA90.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/20B468F4-C4DF-E611-9E78-1866DAEB1FCC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/609E3AFD-C4DF-E611-8B31-B083FED40671.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C27A4DBB-D3DF-E611-895A-90B11C0BCD75.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6E0A0BB4-FADF-E611-9CCE-1866DAEB296C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/34BA9344-57E0-E611-9232-1866DAEA7D94.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CC91C02A-29E1-E611-B082-1866DAEA8808.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0072FA5E-2AE0-E611-B98C-70106F48B8DA.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DEF18183-3EE0-E611-878B-047D7B881DAE.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E87D49AF-D8DF-E611-954F-0025905B8582.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EC1F83A3-D7DF-E611-8C92-0025905A6122.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/94E362AC-D8DF-E611-83C3-0CC47A4D7630.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F23B8EAC-D8DF-E611-861D-0CC47A745294.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EE7EFAAB-D8DF-E611-BC31-0CC47A7452DA.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3854A9B0-D8DF-E611-97F5-0CC47A7C3428.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/048F8F9C-D7DF-E611-ACA9-0CC47A4D7616.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CC2D69AB-D8DF-E611-B464-0CC47A78A2F6.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E4E8E9AC-D8DF-E611-B146-0CC47A4D767C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F2C4EEAE-D8DF-E611-AB0C-0CC47A74527A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/303BED65-D8DF-E611-8318-0CC47A78A30E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0CCE1EAC-D8DF-E611-AB70-0CC47A4D7640.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4CA4D9A8-D8DF-E611-BE9E-0CC47A7C3610.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8887FDAB-D8DF-E611-9E74-0CC47A7C3432.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E8814FAA-D8DF-E611-95DF-0CC47A4C8E16.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2C0817B9-D8DF-E611-848F-0025905B8598.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96B1BBAB-D8DF-E611-981A-0CC47A4D7634.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/02C730B0-D8DF-E611-AE20-0025905B855C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A0B903B1-D8DF-E611-8F04-0025905A60B6.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F68507A9-D8DF-E611-8E37-0CC47A4D761A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/44B144AC-D8DF-E611-ABB0-0CC47A4D7634.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/029719A7-D8DF-E611-9ACF-0CC47A4C8EC8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/06E1B3AF-D8DF-E611-B6B8-0025905B85BC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2E4FA2B2-D8DF-E611-8759-0025905B860E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/783F83E1-F2DF-E611-A81D-0CC47A7C3610.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/702B1CE2-F2DF-E611-87F7-0CC47A78A41C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/383B90E1-F2DF-E611-89D5-0CC47A7C35A4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BEEF8CE1-F2DF-E611-9F0E-0025905B8606.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/485F42E2-F2DF-E611-8B4F-0CC47A78A41C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A465C1E2-F2DF-E611-999A-0025905A6138.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EE10E845-FBDF-E611-AA03-0CC47A4D7692.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D6E0DA40-FBDF-E611-B33B-0CC47A4C8EE2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0CBE3B3B-FBDF-E611-B87C-0CC47A4D7602.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9EAD573E-FBDF-E611-8E79-0CC47A4C8E5E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7CEA2F46-FBDF-E611-BCD5-0CC47A7C34D0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C2649845-FBDF-E611-BCE4-0CC47A4D76D2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BECB2A46-FBDF-E611-872F-0CC47A4D76A2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96E29640-FBDF-E611-920C-0CC47A78A4BA.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B862DA46-FBDF-E611-BA04-0CC47A78A30E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6475C448-FBDF-E611-B65E-0CC47A7C3628.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/125E4342-FBDF-E611-B1B2-0CC47A4D7668.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DCC4B143-FBDF-E611-ACA8-0CC47A78A414.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F4B9D440-FBDF-E611-9C48-0CC47A7C3610.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/82A44741-FBDF-E611-95E4-0CC47A78A42E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9C17E449-FBDF-E611-86CC-0CC47A4D76D0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C8162E3E-FBDF-E611-B83D-0CC47A4D76A0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3C6C2848-FBDF-E611-927C-0025905B8562.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/16D97E41-FBDF-E611-8A89-0CC47A745294.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/121A7C43-FBDF-E611-8F91-0025905A6066.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/76E9F84C-FBDF-E611-A4D0-0025905A6060.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0AC8854D-FBDF-E611-BA29-0025905A60B4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/10363A48-FBDF-E611-A1B5-0025905B859A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C2A76044-FBDF-E611-952F-0CC47A4C8E2E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0CBF7E47-FBDF-E611-B397-0025905A60D2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA5853EB-05E0-E611-8A2B-0CC47A78A33E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/82D14FED-05E0-E611-887C-0025905A608C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/346ABAE1-F2DF-E611-91B3-0CC47A78A41C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/980ED245-FBDF-E611-81B4-0CC47A4C8E56.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/382D42D4-D3E0-E611-8FBF-0CC47A7C3612.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9444E6E9-D3E0-E611-A5CC-0CC47A745294.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D873673E-F0DF-E611-9924-FA163EC24F89.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1C506D91-EFDF-E611-8D78-FA163E4A717D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/264C61A6-EFDF-E611-9385-FA163EC24F89.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EE5EF35B-F0DF-E611-8832-FA163EBB5087.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/66B76D38-F1DF-E611-A4B7-0025904B2012.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/42AFCA9A-EFDF-E611-94A8-FA163E1EF6B1.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/38F0E92E-F1DF-E611-A2CA-02163E012DB7.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B4C075C6-EFDF-E611-BD6F-FA163EB3C2FD.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E033DC0F-FBDF-E611-A08C-FA163E2881AF.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/200924FA-EFDF-E611-B960-FA163ED9CE3F.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50DBCD66-F0DF-E611-83B7-FA163ED43C50.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/64BDFBBB-5DE0-E611-B908-FA163E1BAAF8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/000CC993-BEE0-E611-9AA0-FA163EB918A1.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5C3C7E36-2AE1-E611-925A-FA163E52A5D8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/58C11F9C-34E0-E611-B98B-002481CFB40E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/965F9B6C-2AE0-E611-AC23-0CC47A5FC281.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D471F783-2AE0-E611-B89D-0CC47A5FA215.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/86155594-34E0-E611-82E1-0017A4770440.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/74C10A9C-FFE0-E611-B771-002481DE4BFC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A2EF7B09-75E0-E611-90DB-003048CF6578.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50EFFE67-7CE0-E611-A0C9-5C260AFFFB72.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/00103489-82E0-E611-8921-003048CF662C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D626899A-8EE0-E611-B9AD-A0369FC51394.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D4D87A64-91E0-E611-898F-A0369FC52390.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/18D06ECD-61E1-E611-B3B2-003048CDCDD2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7250CF89-DCE2-E611-8808-5C260AFCAA3C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9EF5C995-EEDF-E611-AB37-001E6757E03C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96604848-FBDF-E611-BEAD-AC162DABCAF8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/12D5590A-2DE0-E611-8750-6CC2173BBAA0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D266F2A1-32E0-E611-9BA3-AC162DABCAF8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E0703841-E0DF-E611-91BE-001E6750489D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/626D1540-E0DF-E611-BBC0-001E67504445.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B8AB629B-EEDF-E611-9449-00259021A3D2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B864FBBA-FADF-E611-A335-00259021A306.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/74FE89BD-FADF-E611-8DEB-20CF3019DEF2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E6D577DA-05E0-E611-BC0E-901B0E5427AE.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3ACC1B01-CDE0-E611-A14F-00144F3FFB6C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E29FDB3E-68E0-E611-9200-0025905C3DCE.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/88EC9AB0-62E0-E611-8D01-0025905C42A8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3E9CDD3E-68E0-E611-9B1F-0025905C3D6C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DA830444-68E0-E611-9A18-0025905C54D8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/568DA73E-68E0-E611-A1FB-0025905C54C4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C6E7C589-38E1-E611-B12F-0025905C5488.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/46696A00-FADF-E611-BE66-002590DE6C48.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AE4AE202-FADF-E611-8EE0-002590DE6C48.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9ED0FFE0-05E0-E611-8BFF-C45444922949.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F64EE886-0FE0-E611-9FD9-002590DE6E7C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A47A4087-0FE0-E611-A47C-0025904B7FC4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1668A018-DCE0-E611-9EB1-C45444922C46.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/40DEAA2B-33E0-E611-B3FA-28924A33AFF6.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/30288AC5-06E1-E611-8682-28924A38DC1E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AA69E21C-D4DF-E611-80F7-A4BF01013D12.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B629F4DF-D3DF-E611-9164-001E67A3FB91.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/963C74A5-E1DF-E611-BE16-A4BF01013D80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/366F348B-22E0-E611-95CA-7845C4FC39C5.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9256E37A-22E0-E611-BD85-3417EBE644B9.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6001BD78-22E0-E611-B6FC-7845C4FC39CB.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D8A84EFE-22E0-E611-933D-3417EBE64B9D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8288B756-23E0-E611-9B6D-848F69FD4EFB.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FA3F50BE-2FE0-E611-A369-008CFA008D4C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E49147CC-2FE0-E611-9430-7845C4FC378B.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/46A15111-60E0-E611-81BF-7845C4FC3779.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/42134D1B-32E1-E611-BE58-7845C4FBB6A4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5C30C521-4DE3-E611-8E08-7845C4FC3A19.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2EE22EC0-5CE3-E611-8BAA-7845C4FC3B0F.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BA58F33A-22E1-E611-BBB5-7845C4FC3B8D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8097BDB3-F1E2-E611-9251-A0369F5BE308.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/949049AC-EFDF-E611-B05F-002590E7D5AE.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F291B7AC-EFDF-E611-8E50-002590E7DEBE.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D0F867AD-EFDF-E611-BDA0-0CC47A1DF81C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F0706CE0-06E0-E611-8B2F-0CC47A1E048A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2E21DD03-07E0-E611-9CCE-002590E7DFD6.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A675D30F-1AE0-E611-9CD4-0CC47ABB517C.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/869E263C-04E1-E611-844F-002590E7DDE6.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/828EFED1-19E0-E611-BAC9-D4AE526A0922.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/98FC7458-E3E0-E611-918D-1CC1DE18CFEA.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5255FA20-ACDF-E611-9885-E0071B7A68F0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C8198D7C-BADF-E611-9F5D-24BE05C656A1.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F42C800D-C5DF-E611-B258-24BE05CEEB81.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/24F88D53-C6DF-E611-BC69-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2C531F73-C6DF-E611-B9E2-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4C5C0177-C6DF-E611-977F-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/369E5A5B-C6DF-E611-8C08-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/66587574-C6DF-E611-AEB4-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B2B6D604-C6DF-E611-9487-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A2535486-C6DF-E611-BFCA-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AAC84B76-C6DF-E611-9918-4C79BA18126D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/44916E54-21E0-E611-BDFC-A0000420FE80.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/28634065-E3DF-E611-A3EE-0CC47AD991FA.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A047561B-C5DF-E611-9C1E-0CC47A13D0BC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/042FCCC3-D3DF-E611-8CA9-0CC47AD99144.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D6AD0A25-D4DF-E611-808A-0CC47A6C1034.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AA293590-06E1-E611-A20E-0CC47AD98BCC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B0DFF8E5-D2DF-E611-8ADF-008CFA1113F8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F46F1E2C-92E0-E611-9197-008CFA111270.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C274C7F4-B7DF-E611-8944-0CC47A57CEB4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/986A2D02-C4DF-E611-BCC6-0025907D2430.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8676BAFD-D2DF-E611-8855-00259075D72E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5CA7DDA5-91E0-E611-B6C6-0CC47A57CB8E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2E4EE354-E2DF-E611-8894-002590D4FC42.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/40DEDEBC-FADF-E611-929A-B083FED04276.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DA531CB6-FADF-E611-B886-B083FECFD4F0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3A7168A9-C4E0-E611-831A-141877642F9D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/108B9DCA-EDDF-E611-B65C-001E67E6F80A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3A511B1A-21E0-E611-AE62-001E67E71CB3.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8A57A152-2AE0-E611-A32E-001E677928B6.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/289E0275-F8E0-E611-BD20-001E677926C0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5A37D9EA-D2DF-E611-9D27-ECF4BBE16468.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/54E8EFF1-D2DF-E611-8B29-001E674FBFC2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/72B7D8F3-D2DF-E611-B876-001E67346BA1.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EAAFADF9-D2DF-E611-954E-001E674FBEC8.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D68B95E0-D2DF-E611-9E54-001E674FB24D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/18F44DF6-D2DF-E611-A349-001E67397DF5.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/448C9D3A-EEDF-E611-9F7C-001E67444EAC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4E3B7BC6-ACE0-E611-A28C-001E674DA83D.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/820BBAC5-EDDF-E611-852C-0090FAA582E4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/92B36CBC-0EE0-E611-A59F-0090FAA573F0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/72E56359-22E0-E611-A92E-0090FAA577A0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3AF9DE4F-2AE0-E611-B8E0-0090FAA57AE0.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/04417C55-2AE0-E611-8454-20CF305616EC.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/162E6955-2AE0-E611-8A79-00259073E45E.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DCF4DBD5-31E0-E611-B55E-0090FAA58BF4.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/36CB772C-FFE0-E611-90C4-0090FAA57F14.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CCC4BFB5-AFE8-E611-951A-02163E011A49.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BC3B6443-E2E0-E611-B02E-549F358EB789.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6EE39CE2-B7E8-E611-A580-02163E011E17.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/80F17CED-A7E8-E611-90E7-02163E0137B2.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/421B7889-ACE8-E611-ACAE-02163E014504.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AA1521C5-ABE8-E611-9292-02163E013490.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E2B4C889-AEE8-E611-8506-02163E019C0B.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1A8B2F4D-ADE8-E611-9FC2-02163E019DB5.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4C7848B4-A9E8-E611-AD8B-02163E011AD7.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/90F6041A-B1E8-E611-BA15-02163E011942.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C017775A-ADE8-E611-91A2-02163E011857.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7A965656-ADE8-E611-A8D4-02163E013576.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5AE60684-AEE8-E611-BB37-02163E019DDB.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/60475B56-ADE8-E611-B543-02163E011C84.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B27CF3CE-ABE8-E611-864B-02163E011A2F.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/44408FBF-ABE8-E611-AC03-02163E019D21.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7690778E-AEE8-E611-958D-02163E01468A.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5CB75488-ACE8-E611-BFF7-02163E014693.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EC60D68B-ACE8-E611-9DC9-02163E0134E7.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3830E190-AEE8-E611-8578-02163E0143F3.root', 
        '/store/mc/RunIISummer16DR80Premix/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/40E554B9-AFE8-E611-94FF-02163E019B72.root'),
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
    fileName = cms.untracked.string('file:TOP-RunIISummer16MiniAODv3-00104.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(cms.untracked.PSet(
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
        )),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mcRun2_asymptotic_v3', '')

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
process.options.numberOfThreads=cms.untracked.uint32(8)
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
