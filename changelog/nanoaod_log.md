## 20201021

1. Signal MC HH->gammgagammatautau privately produced

- based on signal sample used in HIG-19-018 (HH->bbgammagamma)
- change to the following block in pythia setting:

```
    processParameters = cms.vstring(
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 22 22',
            '25:onIfMatch = 15 -15',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on',
            'ResonanceDecayFilter:mothers = 25',
            'ResonanceDecayFilter:daughters = 22,22,15,15'
        ),
```

2. The following MC samples are based on miniAOD used in ttH paper (HIG-19-013)

3. Psets used for nanoAOD generation are copied from these 3 examples for each year

- 2016:

```
    /ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM

```
- 2017:

```
    /ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM
```
- 2018:

```
    /ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
```
