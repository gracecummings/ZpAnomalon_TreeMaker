import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/140000/402B3811-019A-114D-BCE8-72658F05D51B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/140000/6CFC382E-D6A4-2444-B187-CDA4D49EEA50.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/03E28B76-B1A3-FD42-A31B-E0224C5DBCBD.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/CB636FE3-CA07-9146-A19B-248BE633A1FD.root',
] )
