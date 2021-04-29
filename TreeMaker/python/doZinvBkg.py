import FWCore.ParameterSet.Config as cms

def reclusterZinv(self, process, cleanedCandidates, suff):
    # skip all jet smearing for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    doJERsmearing = self.geninfo

    ### AK8 detour

    # https://twiki.cern.ch/CMS/JetToolbox
    from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
    listBTagInfos = ['pfInclusiveSecondaryVertexFinderTagInfos','pfImpactParameterTagInfos']
    listBtagDiscriminatorsAK8 = ['pfBoostedDoubleSecondaryVertexAK8BJetTags','pfMassIndependentDeepDoubleBvLJetTags:probHbb']
    JETCorrLevels = ['L2Relative', 'L3Absolute', 'L2L3Residual']
    #JETCorrLevels = ['L2Relative', 'L2L3Residual']
    reclusterAK8JetPostFix='CleanedWithZ'
    jetToolbox(process, 'ak8', 'dummySeqAK8', 'noOutput',
               PUMethod='Puppi', JETCorrPayload='AK8PFPuppi', JETCorrLevels=JETCorrLevels,
               Cut='pt > 170.0 && abs(rapidity()) < 2.4',
               miniAOD=True, runOnMC=self.geninfo,
               postFix=reclusterAK8JetPostFix,
               newPFCollection = True,
               nameNewPFCollection = cleanedCandidates.value(),
               addSoftDrop=True, addSoftDropSubjets=True, 
               addNsub=True, maxTau=3,
               bTagInfos = listBTagInfos, bTagDiscriminators = listBtagDiscriminatorsAK8,
               subJETCorrPayload='AK4PFPuppi', subJETCorrLevels=JETCorrLevels,
               verbosity = 0 #if self.verbose else 0
    )

    # add deep taggers
    #Follows Option 2
    from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
    from RecoBTag.MXNet.pfDeepBoostedJet_cff import _pfDeepBoostedJetTagsAll

    #Trying V2 update
    from RecoBTag.MXNet.pfDeepBoostedJet_cff import pfDeepBoostedJetTags, pfMassDecorrelatedDeepBoostedJetTags
    from RecoBTag.MXNet.Parameters.V02.pfDeepBoostedJetPreprocessParams_cfi import pfDeepBoostedJetPreprocessParams as pfDeepBoostedJetPreprocessParamsV02
    from RecoBTag.MXNet.Parameters.V02.pfMassDecorrelatedDeepBoostedJetPreprocessParams_cfi import pfMassDecorrelatedDeepBoostedJetPreprocessParams as pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02
    pfDeepBoostedJetTags.preprocessParams = pfDeepBoostedJetPreprocessParamsV02
    pfDeepBoostedJetTags.model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-symbol.json'
    pfDeepBoostedJetTags.param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-0000.params'
    pfMassDecorrelatedDeepBoostedJetTags.preprocessParams = pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02
    pfMassDecorrelatedDeepBoostedJetTags.model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-symbol.json'
    pfMassDecorrelatedDeepBoostedJetTags.param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-0000.params'

    updateJetCollection(
        process,
        jetSource=cms.InputTag('packedPatJetsAK8PFPuppi'+reclusterAK8JetPostFix+'SoftDrop'),
        pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
        svSource = cms.InputTag('slimmedSecondaryVertices'),
        rParam=0.8,
        jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
        #jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L2L3Residual']), 'None'),
        btagDiscriminators = _pfDeepBoostedJetTagsAll,
        postfix='AK8CleanedWithZWithPuppiDaughters',   # !!! postfix must contain "WithPuppiDaughter" !!!
        printWarning = False
    )
    #end option 2

    #back to originial treemaker
    #jecCheckString = "TransientCorrected"
    JetAK8CleanTag=cms.InputTag("selectedUpdatedPatJetsAK8"+reclusterAK8JetPostFix+"WithPuppiDaughters")
    #JetAK8CleanTag=cms.InputTag("updatedPatJets"+jecCheckString+"AK8"+reclusterAK8JetPostFix+"WithPuppiDaughters")#This one does not have deeptaggers!!

    if doJERsmearing:
        # do central smearing and replace jet tag
        process, _, JetAK8CleanTag = JetDepot(process,
            JetTag=JetAK8CleanTag,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0,
            storeJer=2,
        )

    # get puppi-specific multiplicities
    from PhysicsTools.PatAlgos.patPuppiJetSpecificProducer_cfi import patPuppiJetSpecificProducer
    process.puppiSpecificAK8Clean = patPuppiJetSpecificProducer.clone(
        src = JetAK8CleanTag
    )
    # update userfloats (used for jet ID, including ID for JEC/JER variations)
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo
    process, JetAK8CleanTag = addJetInfo(process, JetAK8CleanTag,
        ['puppiSpecificAK8Clean:puppiMultiplicity','puppiSpecificAK8Clean:neutralPuppiMultiplicity','puppiSpecificAK8Clean:neutralHadronPuppiMultiplicity',
         'puppiSpecificAK8Clean:photonPuppiMultiplicity','puppiSpecificAK8Clean:HFHadronPuppiMultiplicity','puppiSpecificAK8Clean:HFEMPuppiMultiplicity'])

    process = self.makeJetVarsAK8(process,
        JetTag=JetAK8CleanTag,
        suff='AK8Clean',
        storeProperties=2,
        doECFs=False, # currently disabled
        #doDeepAK8=False, # currently disabled
        doDeepAK8=True, 
        doDeepDoubleB=True, #Toggled from original 
        puppiSpecific="puppiSpecificAK8Clean",
    )

    # update some userfloat names
    process.JetPropertiesAK8Clean.softDropMass = cms.vstring('SoftDrop')
    process.JetPropertiesAK8Clean.subjets = cms.vstring('SoftDrop')
    process.JetPropertiesAK8Clean.NsubjettinessTau1 = cms.vstring('NjettinessAK8Puppi'+reclusterAK8JetPostFix+':tau1')
    process.JetPropertiesAK8Clean.NsubjettinessTau2 = cms.vstring('NjettinessAK8Puppi'+reclusterAK8JetPostFix+':tau2')
    process.JetPropertiesAK8Clean.NsubjettinessTau3 = cms.vstring('NjettinessAK8Puppi'+reclusterAK8JetPostFix+':tau3')
    process.JetPropertiesAK8Clean.SJbDiscriminatorCSV = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetPropertiesAK8Clean.neutralHadronPuppiMultiplicity = cms.vstring("puppiSpecificAK8Clean:neutralHadronPuppiMultiplicity")
    process.JetPropertiesAK8Clean.neutralPuppiMultiplicity = cms.vstring("puppiSpecificAK8Clean:neutralPuppiMultiplicity")
    process.JetPropertiesAK8Clean.photonPuppiMultiplicity = cms.vstring("puppiSpecificAK8Clean:photonPuppiMultiplicity")

    ### end AK8 detour

    # do CHS for jet clustering
    cleanedCandidatesCHS = cms.EDFilter("CandPtrSelector",
        src = cleanedCandidates,
        cut = cms.string("fromPV")
    )
    setattr(process,"cleanedCandidatesCHS"+suff,cleanedCandidatesCHS)

    # make the RECO jets 
    from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
    ak4PFJetsClean = ak4PFJets.clone(
        src = cms.InputTag("cleanedCandidatesCHS"+suff),
        doAreaFastjet = True
    )
    setattr(process,"ak4PFJetsClean"+suff,ak4PFJetsClean)

    # turn the RECO jets into PAT jets
    # for a full list & description of parameters see:
    # PhysicsTools/PatAlgos/python/tools/jetTools.py
    from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
    jecLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    if self.residual: jecLevels.append("L2L3Residual")
    btagDiscs = ['pfCombinedInclusiveSecondaryVertexV2BJetTags','pfDeepCSVDiscriminatorsJetTags:BvsAll']
    addJetCollection(
       process,
       labelName = 'AK4PFCLEAN'+suff,
       jetSource = cms.InputTag('ak4PFJetsClean'+suff),
       pfCandidates = cleanedCandidates,
       pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
       svSource = cms.InputTag('slimmedSecondaryVertices'),
       algo = 'AK',
       rParam = 0.4,
       getJetMCFlavour = True, # seems to be enough for hadronFlavour()
       #genJetCollection = cms.InputTag('slimmedGenJets'),
       genParticles = cms.InputTag('prunedGenParticles'), # likely needed for hadronFlavour()....
       jetCorrections = ('AK4PFchs', jecLevels, 'None'),
       btagDiscriminators = btagDiscs,
       muSource = cms.InputTag("slimmedMuons"),
       elSource = cms.InputTag("slimmedElectrons")
    )
    # turn on/off GEN matching
    getattr(process,'patJetsAK4PFCLEAN'+suff).addGenPartonMatch = cms.bool(False)
    getattr(process,'patJetsAK4PFCLEAN'+suff).addGenJetMatch = cms.bool(False)
    # turn off some flags for data
    getattr(process,'patJetsAK4PFCLEAN'+suff).addJetFlavourInfo = cms.bool(self.geninfo)
    getattr(process,'patJetsAK4PFCLEAN'+suff).getJetMCFlavour = cms.bool(self.geninfo)

    # apply pt cut to final jet collection (done in slimmedJets)
    reclusteredJets = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("patJetsAK4PFCLEAN"+suff),
        cut = cms.string("pt>10.")
    )
    setattr(process,'reclusteredJets'+suff,reclusteredJets)
    JetTagClean = cms.InputTag("reclusteredJets"+suff)

    # recalculate MET from cleaned candidates and reclustered jets
    postfix="clean"+suff
    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
    runMetCorAndUncFromMiniAOD(
        process,
        isData=not self.geninfo, # controls gen met
        jetCollUnskimmed='patJetsAK4PFCLEAN'+suff,
        pfCandColl=cleanedCandidates.value(),
        recoMetFromPFCs=True, # to recompute
        reclusterJets=False, # without reclustering
        reapplyJEC=False,
        fixEE2017=self.doMETfix,
        postfix=postfix,
    )
    METTag = cms.InputTag('slimmedMETs'+postfix)
    if self.doMETfix:
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not self.geninfo, # controls gen met
            jetCollUnskimmed='patJetsAK4PFCLEAN'+suff,
            pfCandColl=cleanedCandidates.value(),
            recoMetFromPFCs=True, # to recompute
            reclusterJets=False, # without reclustering
            reapplyJEC=False,
            postfix=postfix+'Orig',
            computeMETSignificance=False,
        )
        METTagOrig = cms.InputTag('slimmedMETs'+postfix+'Orig')
    else:
        METTagOrig = None
    
    # isolated tracks
    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

    IsolatedElectronTracksVetoClean = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cleanedCandidates,
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2),
        pdgId               = cms.int32(11),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )
    setattr(process,"IsolatedElectronTracksVetoClean"+suff,IsolatedElectronTracksVetoClean)

    IsolatedMuonTracksVetoClean = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cleanedCandidates,
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2), 
        pdgId               = cms.int32(13),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )
    setattr(process,"IsolatedMuonTracksVetoClean"+suff,IsolatedMuonTracksVetoClean)
    
    IsolatedPionTracksVetoClean = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cleanedCandidates,
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(10.0),
        isoCut              = cms.double(0.1),
        pdgId               = cms.int32(211),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )
    setattr(process,"IsolatedPionTracksVetoClean"+suff,IsolatedPionTracksVetoClean)

    self.VarsInt.extend(['IsolatedElectronTracksVetoClean'+suff+':isoTracks(isoElectronTracksclean'+suff+')'])
    self.VarsInt.extend(['IsolatedMuonTracksVetoClean'+suff+':isoTracks(isoMuonTracksclean'+suff+')'])
    self.VarsInt.extend(['IsolatedPionTracksVetoClean'+suff+':isoTracks(isoPionTracksclean'+suff+')'])

    if doJERsmearing:
        # do central smearing and replace jet tag
        process, _, JetTagClean = JetDepot(process,
            JetTag=JetTagClean,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0,
            storeJer=2,
        )
    
    # make the event variables
    process = self.makeJetVars(
        process,
        JetTag = JetTagClean,
        suff=postfix,
        storeProperties=1,
        METfix=self.doMETfix,
    )

    from TreeMaker.Utils.metdouble_cfi import metdouble
    METclean = metdouble.clone(
       METTag = METTag,
       JetTag = cms.InputTag('HTJets'+postfix)
    )
    setattr(process,"METclean"+suff,METclean)
    self.VarsDouble.extend(['METclean'+suff+':Pt(METclean'+suff+')','METclean'+suff+':Phi(METPhiclean'+suff+')','METclean'+suff+':Significance(METSignificanceclean'+suff+')'])
#    self.VarsDouble.extend(['METclean'+suff+':RawPt(RawMETclean'+suff+')','METclean'+suff+':RawPhi(RawMETPhiclean'+suff+')'])

    if self.doMETfix:
        METcleanOrig = METclean.clone(
            METTag = METTagOrig
        )
        setattr(process,"METclean"+suff+"Orig",METcleanOrig)
        self.VarsDouble.extend(['METclean'+suff+'Orig:Pt(METclean'+suff+'Orig)','METclean'+suff+'Orig:Phi(METPhiclean'+suff+'Orig)'])
#        self.VarsDouble.extend(['METclean'+suff+'Orig:RawPt(RawMETclean'+suff+'Orig)','METclean'+suff+'Orig:RawPhi(RawMETPhiclean'+suff+'Orig)'])

    return process

def doZinvBkg(self,process):
    ## ----------------------------------------------------------------------------------------------
    ## Photons
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.photonidisoproducer_cfi import PhotonIDisoProducer
    process.goodPhotons = PhotonIDisoProducer.clone(
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",self.tagname)
    )
    
    ##### add branches for photon studies
    self.VectorRecoCand.append("goodPhotons(Photons)")
    self.VectorDouble.append("goodPhotons:isEB(Photons_isEB)")
    self.VectorDouble.append("goodPhotons:genMatched(Photons_genMatched)")
    self.VectorDouble.append("goodPhotons:hadTowOverEM(Photons_hadTowOverEM)")
    self.VectorBool.append("goodPhotons:hasPixelSeed(Photons_hasPixelSeed)")
    self.VectorDouble.append("goodPhotons:passElectronVeto(Photons_passElectronVeto)")
    self.VectorDouble.append("goodPhotons:pfChargedIso(Photons_pfChargedIso)")
    self.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(Photons_pfChargedIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:pfGammaIso(Photons_pfGammaIso)")
    self.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(Photons_pfGammaIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:pfNeutralIso(Photons_pfNeutralIso)")
    self.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(Photons_pfNeutralIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:sigmaIetaIeta(Photons_sigmaIetaIeta)")
    self.VectorBool.append("goodPhotons:nonPrompt(Photons_nonPrompt)")
    self.VectorBool.append("goodPhotons:fullID(Photons_fullID)")
    self.VectorBool.append("goodPhotons:electronFakes(Photons_electronFakes)")
    self.VarsBool.append("goodPhotons:hasGenPromptPhoton(hasGenPromptPhoton)")

    ## add MadGraph-level deltaR between photon or Z and status 23 partons
    if self.geninfo:
        process.madMinPhotonDeltaR = cms.EDProducer("MinDeltaRDouble")
        self.VarsDouble.extend(['madMinPhotonDeltaR:madMinPhotonDeltaR(madMinPhotonDeltaR)'])
        self.VarsInt.extend([   'madMinPhotonDeltaR:madMinDeltaRStatus(madMinDeltaRStatus)'])

    from TreeMaker.Utils.zproducer_cfi import ZProducer
    process.makeTheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdElectron'),
        MuonTag     = cms.InputTag('LeptonsNew:IdMuon')
    )
    self.VectorRecoCand.append("makeTheZs:ZCandidates")
    self.VectorRecoCand.append("makeTheZs:ZCandidatesMuMu")
    self.VectorRecoCand.append("makeTheZs:ZCandidatesEE")
    self.VectorRecoCand.append("makeTheZs:ZCandidatesEU")
    self.VectorRecoCand.append("makeTheZs:SelectedMuons")
    self.VectorRecoCand.append("makeTheZs:SelectedElectrons")
    

    ###
    # do the new cleaning
    ###

    # combine leptons
    # GEC - might be able to do both electronca and muons here in hte future
    process.selectedZleptons = cms.EDProducer("CandViewMerger",
        #src = cms.VInputTag("LeptonsNew:IdIsoElectron","LeptonsNew:IdMuon")
        src = cms.VInputTag("makeTheZs:SelectedMuons","makeTheZs:SelectedElectrons")
    )
        # if there are no leptons in the event, just remove high-pt photons (GJet)
    # otherwise, just remove leptons (DY)
    process.selectedXons = cms.EDProducer("CandPtrPrefer",
        first = cms.InputTag("selectedZleptons"), second = cms.InputTag("goodPhotons","highpt")
    )
    
    # do the removal
    # if putEmpty is set to true, this will output an empty collection if the "veto" collection is empty
    # this avoids pointless reclustering of an identical candidate collection
    # "clean" branches in the ntuple will not be filled in this case; (e.g. Jetsclean.size()==0)
    # the corresponding non-clean branches should be used instead for those events
    process.cleanedCandidates =  cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedXons"),
        putEmpty = cms.bool(False)
    )
    
    # make reclustered jets
    process = self.reclusterZinv(
        process,
        cms.InputTag("cleanedCandidates"),
        "",
    )
    
    return process
