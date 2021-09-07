import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/52185944-0127-7F4F-AFCE-35BB33DB71FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/6A29953A-5614-B04B-A0E1-09821D9BA99D.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/A55D5781-462A-F64F-8F49-97E75367E859.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/BA7EB93D-A0B5-B646-808F-23D6AFD37646.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/01D507D5-5560-434E-8177-F265DFEB1317.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2F678AA2-AF15-7E4A-8827-A19440311E80.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A1BDEE90-85F8-F749-90F1-A270049A7903.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CE01BB6E-8EEC-EA4C-A398-E4D7B3570C25.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5000-ND200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CF045903-58A1-1545-917B-53D066E50624.root',
] )
