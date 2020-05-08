import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_0.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_1.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_10.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_11.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_12.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_13.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_14.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_15.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_16.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_17.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_18.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_19.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_2.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_20.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_21.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_22.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_3.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_4.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_5.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_6.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_7.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_8.root',
'store/user/jhakala/ZpAnomalonHZ_Zp2000-ND500-NS1_v2/ZpAnomalonHZ_UFO-Zp2000-ND500-NS1_miniAOD_9.root'
])
