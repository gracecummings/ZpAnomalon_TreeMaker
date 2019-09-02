import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
        '/store/user/jhakala/ZpAnomalonHZ_Zp2000-ND800-NS200/ZpAnomalonHZ_UFO-Zp2000-ND800-NS200_miniAOD_0.root'
 ] )
