import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp3000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1D31BBDB-3FD2-0248-BE81-3534A70C5183.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp3000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/27432BCC-C594-5147-85C0-6AA357BED59C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp3000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/972E8D6D-1A69-C74D-9254-7505F0020D93.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp3000-ND1200-NS1_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/70000/B4650A96-C798-514E-AB1B-8E39CD500D83.root',
] )
