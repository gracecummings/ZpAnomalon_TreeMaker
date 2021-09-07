import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND400-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/140000/678E297B-1CC9-DE49-B775-A5E51611D033.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND400-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/35DBD433-6BFF-B948-9A41-7D36F74A8B71.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4000-ND400-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/7000609F-4E02-604A-B092-ECA7B1195494.root',
] )
