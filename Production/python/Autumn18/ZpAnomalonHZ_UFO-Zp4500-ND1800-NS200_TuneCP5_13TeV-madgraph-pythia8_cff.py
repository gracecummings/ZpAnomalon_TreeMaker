import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4500-ND1800-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/C310FA09-6781-0545-B063-982E3F0E7F72.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4500-ND1800-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/EED7DE62-C6AF-B74B-BCFD-EA55A948C220.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp4500-ND1800-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/2810000/13847DB5-8F37-0D47-B87D-40C9520FBB81.root',
] )
