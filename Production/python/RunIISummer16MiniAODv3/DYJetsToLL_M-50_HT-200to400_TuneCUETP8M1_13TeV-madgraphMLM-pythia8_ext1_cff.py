import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0E0C6373-F4E9-E811-9BD8-5065F37D7121.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0E72AF75-F4E9-E811-9966-24BE05CEEDE1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/1675D05A-01EA-E811-92A1-5065F3818261.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/1AEC5D09-F5E9-E811-A56D-24BE05BDCEF1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2099957B-F2E9-E811-A478-5065F38182E1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/22E88E3B-3DEA-E811-8818-E0071B7A58B0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/24B639AB-F3E9-E811-AD33-E0071B791111.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/26BF254E-F5E9-E811-BEF3-24BE05CEDCF1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2817F006-F5E9-E811-BF01-5065F381F1C1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/281F4F27-F5E9-E811-8125-24BE05C618F1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2E43F93C-BAEA-E811-BD80-24BE05CE5D21.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/32332D26-F5E9-E811-9FCD-E0071B7A5650.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/32DA7055-F4E9-E811-812A-506B4BB16016.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/3C5C206F-F4E9-E811-94C3-24BE05C4D821.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/3EAE1732-F5E9-E811-9140-506B4BB166CE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/440CF073-F4E9-E811-802C-24BE05C4D821.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/48BB1AD3-F3E9-E811-81B0-24BE05C666B1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/4CD483F1-F4E9-E811-A512-24BE05CECB81.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/508327AB-F3E9-E811-9831-E0071B791111.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/5ECD5169-F4E9-E811-ADEC-506B4BB16016.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6868F385-F5E9-E811-A7C4-506B4BB166AE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6A1F1C68-F5E9-E811-BA08-24BE05C4D821.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6A218B41-ECE9-E811-A76C-000008EAFE80.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6A73F67D-F2E9-E811-9AF9-24BE05BDAE61.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6C56383A-F1E9-E811-9A6B-24BE05C6C7E1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/748B4500-F5E9-E811-8939-5065F381F1C1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/74C27A71-F4E9-E811-9D16-5065F37D7121.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/78F34ADC-F2E9-E811-B2C0-24BE05CE5D21.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/7C90D17B-F4E9-E811-BFE4-24BE05CEEDE1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/82430719-F5E9-E811-AF48-24BE05C666B1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8482C378-F2E9-E811-820D-5065F381C1D1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9A6C784D-F5E9-E811-A127-5065F3812201.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9C9FE706-F2E9-E811-964A-24BE05C666B1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A4C071F4-05EA-E811-82D9-E0071B745DC0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A8CEC43A-F1E9-E811-9B30-24BE05C6C7E1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A8EF3851-F5E9-E811-BB57-24BE05CEDCF1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/AE2DFB7A-F2E9-E811-841C-24BE05CEEDD1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/AE31E75A-F5E9-E811-9FD4-5065F3812291.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/AE688987-F4E9-E811-BF0A-E0071B7A5650.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BA96208E-F4E9-E811-BFEB-E0071B7A5650.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BAC1149C-12EA-E811-BA20-506B4BB16ADE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BC0FF8AF-F3E9-E811-AAF6-5065F3812291.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BEA4690F-F5E9-E811-B63F-24BE05BDCEF1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/C2F83160-F2E9-E811-A0AE-24BE05BDAE61.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/C8BE2520-F5E9-E811-9D8B-E0071B791111.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/CE02EC19-F5E9-E811-801B-E0071B7A5650.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/CE59FCD1-F3E9-E811-A807-24BE05C666B1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D0D8C367-F2E9-E811-8FBA-24BE05CEEDD1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D22C8FF3-F4E9-E811-9E1F-24BE05CECB81.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D26552F7-F4E9-E811-8840-24BE05CE2D41.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D2DDD70A-0CEA-E811-A5CF-B8CA3A70A410.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D40E90DB-F0E9-E811-A865-24BE05CEEDA1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/DA16B936-F0E9-E811-873B-24BE05CEEC21.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/DE95F09A-12EA-E811-BB0B-E0071B6C9DB0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E0EB4131-B4EA-E811-AD34-506B4BB166AE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E2E8E368-F5E9-E811-898B-24BE05C4D821.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E2EC6213-F5E9-E811-AA88-24BE05C666B1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/EAE4D665-F2E9-E811-8D7F-5065F381C1D1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/EE61CD4F-F5E9-E811-90A0-5065F3812201.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F4454EAF-F3E9-E811-8B43-5065F3812291.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F48EF312-F2E9-E811-B9D5-24BE05C666B1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F4A58EEF-F4E9-E811-BC21-24BE05CE2D41.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F83E35E5-F2E9-E811-B817-24BE05CE5D21.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FA71C583-F8E9-E811-9CD7-24BE05C48831.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FA728A78-F2E9-E811-A148-5065F38182E1.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FAF6DC21-F5E9-E811-B21B-E0071B791111.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FC434FCF-BCEA-E811-8084-24BE05CECB81.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FECA045A-F4E9-E811-8FE5-506B4BB16016.root',
] )