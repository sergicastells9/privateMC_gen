# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/RunIIAutumn18DRPremix-tauDecays_102X_upgrade2018_realistic_v15-v1/AODSIM --fileout file:TOP-RunIIAutumn18MiniAOD-00188.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename TOP-RunIIAutumn18MiniAOD-00188_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 8597
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
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/C1D5962F-9126-1A47-8208-DD50065BFA7B.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/AFBAAF8B-58B1-DB4D-9A46-62533026C6C2.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/4FE56F35-CE73-9E4D-9B06-8734F0654803.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/02E8C11B-138D-6147-8961-74C7DCC45BBB.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/0BC73165-4035-0648-96A6-E4B3602E153D.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/FE389FE1-847D-204B-8E10-953D30F63E1C.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/7B7636B1-1774-7F40-856B-12FC238E3B28.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/F34C35A0-0596-3B43-9316-7EE2945A30B2.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/363F3D6A-D947-AD44-881F-1FE2CFB09FBB.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/C1AF8461-45D7-FC42-BC51-9CE44E3A3328.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/88D792FE-555E-E54E-8D54-EE304F6C0BCB.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/CA6711CB-73A0-2348-8AC1-FD4D19181397.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/78AD31F4-AB46-FC40-A100-B82873B3255F.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/9438D6CA-B74D-794F-928A-3D21DBF0F9DF.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/D1978D1E-4B0E-BF45-8A8E-E45B485D4EAF.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/004D008F-26A9-B34F-8DE3-A2057C0844F7.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/665B9265-0A84-7E47-AA99-D7C740672CDC.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/31CB1B22-420E-2241-9799-A59D535A22F0.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/4B8A8EF6-8A90-D94E-9E76-E4B90939DCC0.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/00E92D41-095F-0049-8063-42DDBCF703AC.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/095B38BA-0648-F54E-AFD7-634EDD291F5E.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/9255E7DF-5053-6D44-A710-53C5DC30981C.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/75708D58-F3EE-7845-AE52-EE2137B74198.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/03871F4F-8D3B-944B-8CE2-941726CF8816.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/7BE2264E-6D96-3249-ABA3-9F68FC1210E5.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/77E3D83C-38B8-7745-BBC9-62E6AB53EC11.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/6C9E8963-BFA7-DC46-B3F8-E57991DC1655.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/4A11EBCC-8DDF-9C49-A99A-07A6E66A7237.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/075C1936-EF53-AD45-9753-118B7BC378CE.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/468AA680-20C1-194C-8142-378AF39F305C.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/E44C99EF-15D4-8243-B69C-540D0D37360F.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/0EBF7A46-424B-5B43-836A-E1F980E12108.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/CA1C1988-06DA-6443-95FB-73A47F7C7A75.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/78E6A791-7514-7B40-8A0B-5C260D472F01.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/CA0C9DB6-BCF9-FD40-9EBB-AAD86459B52D.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/89F13991-1DAC-B749-9117-6159F62F7E1B.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/11678CA2-BB45-3D41-9961-3160C0BC1FBB.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/C2F98DFC-1E08-DA47-8135-1B02B6413564.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/499BAFFA-55E1-1147-AD23-E80A5D926890.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/E42A3C4A-C85D-1248-8E61-82CB37060BE9.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/3FC93135-D5B2-AC44-AFA0-E7FAC9EE8B0E.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/50A7A0FE-3457-904A-BC5B-58EDD535F97F.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/211A613A-A801-CB4B-B682-6CF898304145.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/6EC023B2-1964-FC43-903E-855BFE95ACEB.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/53A975FC-8EBC-8044-85DC-E9821395C264.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/46CF57CF-2C00-6C4F-9ADE-722B509A12D2.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/14278B22-054C-BB45-971A-43437A816B23.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/6B8AF314-F241-204C-A5FE-085A00DE85C1.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/9DBA2B26-6392-154D-989B-9268235940EC.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/220C8705-114D-9341-9EB6-E2A98B98B0D4.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/504980B0-5AFF-1847-B0D3-2E52194AED47.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/50000/604F8A46-8133-4845-AAE2-021ACBC16F1A.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/0E2BC75F-F5B1-F048-993A-A3E1389A85C2.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/50000/9FEC0570-D80D-6545-A3F6-8080467A89A7.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/50000/57D2AC59-CC08-AA42-BC92-041B6FAB4551.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/50000/C56D25AE-16BD-9445-8ECC-F0B7DD2BE32C.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/50000/50FF7623-7D6E-7F48-8771-92E1C7478ED1.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/50000/C2780A63-F3BA-4E42-B534-A93DB296A2F4.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/3F142952-8E61-2D4D-8BFC-A6E993D98453.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/06967DB9-4078-8C45-A34F-72A790694E4B.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/91A2AE12-400F-AE48-BC5E-3ABBD461D5AD.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/C895455B-EABB-D640-8872-AB42D764F944.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/78241EE4-B15B-C147-9ABF-FF21F2C8646B.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/250000/6668CF5A-12FE-CC42-BFF5-93E8FC591F12.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/510000/5FD8D4B9-8D54-F34B-8F1D-31AAFD85C408.root', 
        '/store/mc/RunIIAutumn18DRPremix/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut_TuneCP5-MadGraph5-pythia8/AODSIM/tauDecays_102X_upgrade2018_realistic_v15-v1/510000/A1D62879-2242-AE40-B171-9059A3D17D20.root'
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
    fileName = cms.untracked.string('file:TOP-RunIIAutumn18MiniAOD-00188.root'),
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
