import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/885DADE0-E11C-714B-B99C-55EC9C2B99BC.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/2710000/9CFB0B9C-8A8A-024B-8194-9D34C9F68A64.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/007FB873-C876-8C4A-9B5D-ED676FB5AF7D.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/63232CD1-EE47-8046-A65A-EB786D349A83.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7F20FE7A-3637-0840-977F-876588948F73.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/890EC027-A3FE-BC45-92F4-D6F8F2563604.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/EE771910-3FDA-EC4C-A363-BE7AAFF6BFD2.root',
    '/store/mc/RunIIAutumn18MiniAOD/ZpAnomalonHZ_UFO-Zp5500-ND600-NS200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F48C34C8-1EAC-2F45-8E02-22F3F967CC39.root',
])
