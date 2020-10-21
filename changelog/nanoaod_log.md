# 20201021

## signal MC HH->gammgagammatautau privately produced
- based on signal sample used in HIG-19-018 (HH->bbgammagamma)
- change to the following block in pythia setting:

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
