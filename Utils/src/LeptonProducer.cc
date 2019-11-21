// -*- C++ -*-
//
// Package:    LeptonProducer
// Class:      LeptonProducer
//
/**\class LeptonProducer LeptonProducer.cc RA2Classic/LeptonProducer/src/LeptonProducer.cc
 * 
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files

#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
// math tools in CMSSW
#include "DataFormats/Math/interface/deltaR.h"

#include "TVector2.h"

#include "TreeMaker/Utils/interface/get_isolation_activity.h"
//
// class declaration
//

class LeptonProducer : public edm::global::EDProducer<> {
  enum elecIDLevel {VETO, LOOSE, MEDIUM, TIGHT};
public:
  explicit LeptonProducer(const edm::ParameterSet&);
  ~LeptonProducer() override;
        
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  float MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi) const;
  //https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Identification
  bool MuonIDhighPt(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool MuonIDtrackerHighPt(const pat::Muon & muon, const reco::Vertex& vtx) const;

  bool MuonIDloose(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool MuonIDmedium(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool MuonIDtight(const pat::Muon & muon, const reco::Vertex& vtx) const;
  bool ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level, const double rho = 0.0) const;
  double GetEffectiveArea(const double absEta) const;        

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
        
  // ----------member data ---------------------------
  edm::InputTag MuonTag_, ElecTag_, PrimVtxTag_, metTag_, PFCandTag_, RhoTag_;
  edm::EDGetTokenT<edm::View<pat::Muon>> MuonTok_;
  edm::EDGetTokenT<edm::View<pat::Electron>> ElecTok_;
  edm::EDGetTokenT<reco::VertexCollection> PrimVtxTok_;
  edm::EDGetTokenT<edm::View<pat::MET>> metTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> PFCandTok_;
  edm::EDGetTokenT<double> RhoTok_;
  double minElecPt_, maxElecEta_, elecIsoValue_;
  bool useEleMVAId_, useMiniIsolation_;
  std::string eleMVAIdWP_;
  std::vector<double> eb_ieta_cut_, eb_deta_cut_, eb_dphi_cut_, eb_hovere_cut_, eb_hovere_cut2_, eb_hovere_cut3_, eb_ooeminusoop_cut_, eb_d0_cut_, eb_dz_cut_, eb_relIsoWithEA_cut_, eb_relIsoWithEA_cut2_;
  std::vector<int> eb_misshits_cut_;
  std::vector<double> ee_ieta_cut_, ee_deta_cut_, ee_dphi_cut_, ee_hovere_cut_, ee_hovere_cut2_, ee_hovere_cut3_, ee_ooeminusoop_cut_, ee_d0_cut_, ee_dz_cut_, ee_relIsoWithEA_cut_, ee_relIsoWithEA_cut2_;
  std::vector<int> ee_misshits_cut_;
  bool hovere_constant_, relIsoWithEA_constant_;
  double minMuPt_, maxMuEta_, muIsoValue_;
  bool usePFIsoDeltaBetaCorr_, useTrackerBasedIso_;
  double muNormalizedChi2Max_, muChi2LocalPositionMax_, muTrkKink_, muValidFractionMin_;
  std::vector<double> muSegmentCompatibilityMin_;
  double mudBMax_, mudZMax_;
  double tightMuNormalizedChi2Max_;
  int tightMuNumberOfValidMuonHitsMin_, tightMuNumberOfMatchedStationsMin_;
  double tightMudBMax_, tightMudZMax_;
  int tightMuNumberOfValidPixelHitsMin_, tightMuTrackerLayersWithMeasurementMin_;
  std::vector<double> electronEAValues_, muonEAValues_;
  SUSYIsolation SUSYIsolationHelper;
};

//
// constructors and destructor
//
LeptonProducer::LeptonProducer(const edm::ParameterSet& iConfig):
  //register your products
  MuonTag_                               (iConfig.getParameter<edm::InputTag>("MuonTag")),
  ElecTag_                               (iConfig.getParameter<edm::InputTag>("ElectronTag")),
  PrimVtxTag_                            (iConfig.getParameter<edm::InputTag>("PrimaryVertex")),
  metTag_                                (iConfig.getParameter<edm::InputTag> ("METTag")),
  PFCandTag_                             (edm::InputTag("packedPFCandidates")),
  RhoTag_                                (edm::InputTag("fixedGridRhoFastjetCentralNeutral")),
  MuonTok_                               (consumes<edm::View<pat::Muon>>(MuonTag_)),
  ElecTok_                               (consumes<edm::View<pat::Electron>>(ElecTag_)),
  PrimVtxTok_                            (consumes<reco::VertexCollection>(PrimVtxTag_)),
  metTok_                                (consumes<edm::View<pat::MET>>(metTag_)),
  PFCandTok_                             (consumes<pat::PackedCandidateCollection>(PFCandTag_)),
  RhoTok_                                (consumes<double>(RhoTag_)),
  minElecPt_                             (iConfig.getParameter<double>("minElecPt")),
  maxElecEta_                            (iConfig.getParameter<double>("maxElecEta")),
  elecIsoValue_                          (iConfig.getParameter<double>("elecIsoValue")),
  useEleMVAId_                           (iConfig.getParameter<bool>("UseEleMVAId")),
  useMiniIsolation_                      (iConfig.getParameter<bool>("UseMiniIsolation")),
  eleMVAIdWP_                            (iConfig.getParameter<std::string>("eleMVAIdWP")),
  eb_ieta_cut_                           (iConfig.getParameter<std::vector<double>>("eb_ieta_cut")),
  eb_deta_cut_                           (iConfig.getParameter<std::vector<double>>("eb_deta_cut")),
  eb_dphi_cut_                           (iConfig.getParameter<std::vector<double>>("eb_dphi_cut")),
  eb_hovere_cut_                         (iConfig.getParameter<std::vector<double>>("eb_hovere_cut")),
  eb_ooeminusoop_cut_                    (iConfig.getParameter<std::vector<double>>("eb_ooeminusoop_cut")),
  eb_d0_cut_                             (iConfig.getParameter<std::vector<double>>("eb_d0_cut")),
  eb_dz_cut_                             (iConfig.getParameter<std::vector<double>>("eb_dz_cut")),
  eb_relIsoWithEA_cut_                   (iConfig.getParameter<std::vector<double>>("eb_relIsoWithEA_cut")),
  eb_misshits_cut_                       (iConfig.getParameter<std::vector<int>>("eb_misshits_cut")),
  ee_ieta_cut_                           (iConfig.getParameter<std::vector<double>>("ee_ieta_cut")),
  ee_deta_cut_                           (iConfig.getParameter<std::vector<double>>("ee_deta_cut")),
  ee_dphi_cut_                           (iConfig.getParameter<std::vector<double>>("ee_dphi_cut")),
  ee_hovere_cut_                         (iConfig.getParameter<std::vector<double>>("ee_hovere_cut")),
  ee_ooeminusoop_cut_                    (iConfig.getParameter<std::vector<double>>("ee_ooeminusoop_cut")),
  ee_d0_cut_                             (iConfig.getParameter<std::vector<double>>("ee_d0_cut")),
  ee_dz_cut_                             (iConfig.getParameter<std::vector<double>>("ee_dz_cut")),
  ee_relIsoWithEA_cut_                   (iConfig.getParameter<std::vector<double>>("ee_relIsoWithEA_cut")),
  ee_misshits_cut_                       (iConfig.getParameter<std::vector<int>>("ee_misshits_cut")),
  hovere_constant_                       (iConfig.getParameter<bool>("hovere_constant")),
  relIsoWithEA_constant_                 (iConfig.getParameter<bool>("relIsoWithEA_constant")),
  minMuPt_                               (iConfig.getParameter<double>("minMuPt")),
  maxMuEta_                              (iConfig.getParameter<double>("maxMuEta")),
  muIsoValue_                            (iConfig.getParameter<double>("muIsoValue")),
  usePFIsoDeltaBetaCorr_                 (iConfig.getParameter<bool>("UsePFIsoDeltaBetaCorr")),
  useTrackerBasedIso_                    (iConfig.getParameter<bool>("UseTrackerBasedIso")),
  muNormalizedChi2Max_                   (iConfig.getParameter<double>("muNormalizedChi2Max")),
  muChi2LocalPositionMax_                (iConfig.getParameter<double>("muChi2LocalPositionMax")),
  muTrkKink_                             (iConfig.getParameter<double>("muTrkKink")),
  muValidFractionMin_                    (iConfig.getParameter<double>("muValidFractionMin")),
  muSegmentCompatibilityMin_             (iConfig.getParameter<std::vector<double>>("muSegmentCompatibilityMin")),
  mudBMax_                               (iConfig.getParameter<double>("mudBMax")),
  mudZMax_                               (iConfig.getParameter<double>("mudZMax")),
  tightMuNormalizedChi2Max_              (iConfig.getParameter<double>("tightMuNormalizedChi2Max")),
  tightMuNumberOfValidMuonHitsMin_       (iConfig.getParameter<int>("tightMuNumberOfValidMuonHitsMin")),
  tightMuNumberOfMatchedStationsMin_     (iConfig.getParameter<int>("tightMuNumberOfMatchedStationsMin")),
  tightMudBMax_                          (iConfig.getParameter<double>("tightMudBMax")),
  tightMudZMax_                          (iConfig.getParameter<double>("tightMudZMax")),
  tightMuNumberOfValidPixelHitsMin_      (iConfig.getParameter<int>("tightMuNumberOfValidPixelHitsMin")),
  tightMuTrackerLayersWithMeasurementMin_(iConfig.getParameter<int>("tightMuTrackerLayersWithMeasurementMin")),
  electronEAValues_                      (iConfig.getParameter<std::vector<double>>("electronEAValues")),
  muonEAValues_                          (iConfig.getParameter<std::vector<double>>("muonEAValues"))
{

  if(!hovere_constant_){
    eb_hovere_cut2_ = iConfig.getParameter<std::vector<double>>("eb_hovere_cut2");
    eb_hovere_cut3_ = iConfig.getParameter<std::vector<double>>("eb_hovere_cut3");
    ee_hovere_cut2_ = iConfig.getParameter<std::vector<double>>("ee_hovere_cut2");
    ee_hovere_cut3_ = iConfig.getParameter<std::vector<double>>("ee_hovere_cut3");
  }

  if(!relIsoWithEA_constant_){
    eb_relIsoWithEA_cut2_ = iConfig.getParameter<std::vector<double>>("eb_relIsoWithEA_cut2");
    ee_relIsoWithEA_cut2_ = iConfig.getParameter<std::vector<double>>("ee_relIsoWithEA_cut2");
  }

  SUSYIsolationHelper.SetEAVectors(electronEAValues_, muonEAValues_);

  produces<std::vector<pat::Muon>>("IdMuon");

  produces<std::vector<bool>>("IdMuonMediumID");
  produces<std::vector<bool>>("IdMuonTightID");
  produces<std::vector<int>>("IdMuonCharge");
  produces<std::vector<double>>("IdMuonMTW");
  produces<std::vector<bool>>("IdMuonPassIso");
  produces<std::vector<pat::Muon>>("IdIsoMuon");
  produces<int>("IdIsoMuonNum");

  produces<std::vector<pat::Electron>>("IdElectron");
  produces<std::vector<bool>>("IdElectronMediumID");
  produces<std::vector<bool>>("IdElectronTightID");
  produces<std::vector<int>>("IdElectronCharge");
  produces<std::vector<double>>("IdElectronEnergyCorr");
  produces<std::vector<double>>("IdElectronTrkEnergyCorr");
  produces<std::vector<double>>("IdElectronMTW");
  produces<std::vector<bool>>("IdElectronPassIso");
  produces<std::vector<pat::Electron>>("IdIsoElectron");
  produces<int>("IdIsoElectronNum");
  
  produces<int>("");        
}


LeptonProducer::~LeptonProducer()
{
        
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
        
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void LeptonProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;

  auto idisoElectrons = std::make_unique<std::vector<pat::Electron>>();
  auto idElectrons = std::make_unique<std::vector<pat::Electron>>();
  auto idMuons = std::make_unique<std::vector<pat::Muon>>();
  auto idisoMuons = std::make_unique<std::vector<pat::Muon>>();  

  auto MuonCharge = std::make_unique<std::vector<int>>();
  auto ElectronCharge = std::make_unique<std::vector<int>>();

  auto muIDMTW = std::make_unique<std::vector<double>>();
  auto muIDMedium = std::make_unique<std::vector<bool>>();
  auto muIDTight = std::make_unique<std::vector<bool>>();
  auto muIDPassIso = std::make_unique<std::vector<bool>>();
  auto elecIDEnergyCorr = std::make_unique<std::vector<double>>();
  auto elecIDTrkEnergyCorr = std::make_unique<std::vector<double>>();
  auto elecIDMTW = std::make_unique<std::vector<double>>();
  auto elecIDMedium = std::make_unique<std::vector<bool>>();
  auto elecIDTight = std::make_unique<std::vector<bool>>();
  auto elecIDPassIso = std::make_unique<std::vector<bool>>();

  int nmuons = 0;
  int nelectrons = 0;

  edm::Handle< edm::View<pat::MET> > MET;
  iEvent.getByToken(metTok_,MET); 
  reco::MET::LorentzVector metLorentz(0,0,0,0);
  if(MET.isValid() )
    {
      metLorentz=MET->at(0).p4();
    } else edm::LogWarning("TreeMaker")<<"LeptonProducer::MetTag Invalid Tag: "<<metTag_;

  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(PFCandTok_, pfcands);

  edm::Handle< double > rho_;
  iEvent.getByToken(RhoTok_, rho_); // Central rho recommended for SUSY
  double rho = *rho_;

  edm::Handle<reco::VertexCollection> vtx_h;
  iEvent.getByToken(PrimVtxTok_, vtx_h);
  edm::Handle<edm::View<pat::Muon> > muonHandle;
  iEvent.getByToken(MuonTok_, muonHandle);
  if(muonHandle.isValid())
    {
      for(const auto & muon : *muonHandle)
        {
          pat::Muon aMu = muon;
          // will have some muon momentum correction before the pT cut
          if(aMu.pt()<minMuPt_ || fabs(aMu.eta())>maxMuEta_) continue;

          if(MuonIDtight(aMu,vtx_h->at(0))){
              idMuons->push_back(aMu);
              muIDMedium->push_back(MuonIDmedium(aMu,vtx_h->at(0)));
              muIDTight->push_back(MuonIDtight(aMu,vtx_h->at(0)));
              muIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),aMu.pt(),aMu.phi()));
              MuonCharge->push_back(aMu.charge());
              nmuons++;
          }

          //highPt or trackerHighPt ID
          //https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#HighPt_Muon
          //https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#HighPt_Tracker_Muon
          if( muon::isHighPtMuon(aMu,vtx_h->at(0)) || muon::isTrackerHighPtMuon(aMu,vtx_h->at(0)) ) 
            {
              //https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Particle_Flow_isolation
              if(usePFIsoDeltaBetaCorr_){
                  double pfiso = aMu.pfIsolationR03().sumChargedHadronPt +
                                 std::max(0.0, aMu.pfIsolationR03().sumNeutralHadronEt + aMu.pfIsolationR03().sumPhotonEt - 0.5*aMu.pfIsolationR03().sumPUPt);
                  double relpfiso = pfiso/aMu.pt(); 
                  if(relpfiso < 0.35 /*reco::Muon::PFIsoLoose*/) idisoMuons->push_back(aMu);
              }
              //https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Tracker_based_Isolation
              else if(useTrackerBasedIso_)
                  {
                    double trackerIso = aMu.isolationR03().sumPt; 
                    //subtrack other muons' inner track pts from the cone
                    for(const auto & bMu : *muonHandle)
                       {
                        if (!MuonIDhighPt(bMu,vtx_h->at(0)) && !MuonIDtrackerHighPt(bMu,vtx_h->at(0))) continue;
                        if (&bMu != &aMu && reco::deltaR(bMu,aMu)<0.3)
                            trackerIso -= bMu.innerTrack()->pt();        
                    } 
                    if(trackerIso/aMu.pt() < 0.1 /*reco::Muon::TkIsoLoose*/) idisoMuons->push_back(aMu);
              }
              else{ 
                   //no other iso options for the moment
                   idisoMuons->push_back(aMu);
              }

          }//highPt or trackerHighPt ID

        }//const auto & aMu : *muonHandle

  }//muonHandle.isValid()
  else edm::LogWarning("TreeMaker")<<"LeptonProducer::MuonTag Invalid Tag: "<<MuonTag_;


  edm::Handle<edm::View<pat::Electron> > eleHandle;
  iEvent.getByToken(ElecTok_, eleHandle);
  if(eleHandle.isValid())
    {
      for(const auto & ele : *eleHandle)
        {
          pat::Electron aEle = ele;
          if(fabs(aEle.superCluster()->eta())>maxElecEta_) continue;
          if(aEle.hasUserFloat("ecalTrkEnergyPostCorr")){
             auto corrP4  = aEle.p4() * aEle.userFloat("ecalTrkEnergyPostCorr") / aEle.energy();
             aEle.setP4(corrP4);
          }

          if(fabs(aEle.superCluster()->eta())>maxElecEta_ || aEle.pt()<minElecPt_) continue;
          const reco::Vertex vtx = vtx_h->at(0);

          double miniIso = 0.0;
          double mt2_act = 0.0;
          SUSYIsolationHelper.GetMiniIsolation(pfcands, &aEle, SUSYIsolation::electron, rho, miniIso, mt2_act);

          //if use cut-based ID
          if(ElectronID(aEle, vtx, LOOSE, rho) and !useEleMVAId_) // check LOOSE id
            {
              // id passed
              idElectrons->push_back(aEle);

              elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),aEle.pt(),aEle.phi()));
              elecIDMedium->push_back(ElectronID(aEle, vtx, MEDIUM, rho));
              elecIDTight->push_back(ElectronID(aEle, vtx, TIGHT, rho));
              ElectronCharge->push_back(aEle.charge());
              elecIDEnergyCorr->push_back(aEle.hasUserFloat("ecalEnergyPostCorr") ? aEle.userFloat("ecalEnergyPostCorr") : -1);
              elecIDTrkEnergyCorr->push_back(aEle.hasUserFloat("ecalTrkEnergyPostCorr") ? aEle.userFloat("ecalTrkEnergyPostCorr") : -1);
              elecIDPassIso->push_back(useMiniIsolation_ ? miniIso<elecIsoValue_ : true);

              if(elecIDPassIso->back())
                {
                  // iso passed
                  idisoElectrons->push_back(aEle);
                  nelectrons++;
                }
            }

          //if use MVA ID
          if(useEleMVAId_){
              if(!aEle.electronID(eleMVAIdWP_)) continue;
              // id passed
              idElectrons->push_back(aEle);

              elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),aEle.pt(),aEle.phi()));
              elecIDMedium->push_back(ElectronID(aEle, vtx, MEDIUM, rho));
              elecIDTight->push_back(ElectronID(aEle, vtx, TIGHT, rho));
              ElectronCharge->push_back(aEle.charge());
              elecIDEnergyCorr->push_back(aEle.hasUserFloat("ecalEnergyPostCorr") ? aEle.userFloat("ecalEnergyPostCorr") : -1);
              elecIDTrkEnergyCorr->push_back(aEle.hasUserFloat("ecalTrkEnergyPostCorr") ? aEle.userFloat("ecalTrkEnergyPostCorr") : -1);

              double absEta = std::abs(aEle.superCluster()->eta());
              auto pfIso  = aEle.pfIsolationVariables();
              double isoWithEA  = pfIso.sumChargedHadronPt +
                            std::max(0.0, pfIso.sumNeutralHadronEt + pfIso.sumPhotonEt - rho*GetEffectiveArea(absEta));
              
              elecIDPassIso->push_back(isoWithEA/aEle.pt() < 0.35);
              if(elecIDPassIso->back()){
                  // iso passed
                  idisoElectrons->push_back(aEle);
                  nelectrons++;
              }

          }// use MVA ID

        } // loop over electrons

    } // valid electron collection
    else edm::LogWarning("TreeMaker")<<"LeptonProducer::ElectronTag Invalid Tag: "<<ElecTag_;

  auto htp1 = std::make_unique<int>(nmuons+nelectrons);
  auto htp2 = std::make_unique<int>(nmuons);
  auto htp3 = std::make_unique<int>(nelectrons);
  iEvent.put(std::move(htp1));
  iEvent.put(std::move(htp2),"IdIsoMuonNum");
  iEvent.put(std::move(htp3),"IdIsoElectronNum");
  iEvent.put(std::move(idMuons),"IdMuon");
  iEvent.put(std::move(idisoMuons),"IdIsoMuon");

  iEvent.put(std::move(idElectrons),"IdElectron");
  iEvent.put(std::move(idisoElectrons),"IdIsoElectron");

  iEvent.put(std::move(ElectronCharge),"IdElectronCharge");
  iEvent.put(std::move(MuonCharge),"IdMuonCharge");

  iEvent.put(std::move(muIDMTW),"IdMuonMTW");
  iEvent.put(std::move(muIDMedium),"IdMuonMediumID");
  iEvent.put(std::move(muIDTight),"IdMuonTightID");
  iEvent.put(std::move(muIDPassIso),"IdMuonPassIso");
  iEvent.put(std::move(elecIDMTW),"IdElectronMTW");
  iEvent.put(std::move(elecIDEnergyCorr),"IdElectronEnergyCorr");
  iEvent.put(std::move(elecIDTrkEnergyCorr),"IdElectronTrkEnergyCorr");
  iEvent.put(std::move(elecIDMedium),"IdElectronMediumID");
  iEvent.put(std::move(elecIDTight),"IdElectronTightID");
  iEvent.put(std::move(elecIDPassIso),"IdElectronPassIso");

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

float LeptonProducer::MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi) const
{
  if(std::isnan(lepPhi) || std::isnan(metPhi)) return 0.;
  float deltaPhi =TVector2::Phi_mpi_pi(lepPhi-metPhi);
  return sqrt(2*lepPt*metPt*(1-cos(deltaPhi)) );
}

bool LeptonProducer::MuonIDloose(const pat::Muon & muon, const reco::Vertex& vtx) const {
  return muon.isLooseMuon();
}

bool LeptonProducer::MuonIDmedium(const pat::Muon & muon, const reco::Vertex& vtx) const {
  //medium WP + dz/dxy cuts
  bool goodGlob      = muon.isGlobalMuon() && 
                       muon.globalTrack()->normalizedChi2() < muNormalizedChi2Max_ && 
                       muon.combinedQuality().chi2LocalPosition < muChi2LocalPositionMax_ && 
                       muon.combinedQuality().trkKink < muTrkKink_; 
  bool isMedium      = muon.isLooseMuon() && 
                       muon.innerTrack()->validFraction() > muValidFractionMin_ && 
                       muon.segmentCompatibility() > (goodGlob ? muSegmentCompatibilityMin_[0] : muSegmentCompatibilityMin_[1]);
  bool susyIP2DLoose = muon.dB() < mudBMax_ && fabs(muon.muonBestTrack()->dz(vtx.position())) < mudZMax_;
  bool isMediumPlus  = isMedium && susyIP2DLoose;
  return isMediumPlus; 
}

bool LeptonProducer::MuonIDtight(const pat::Muon & muon, const reco::Vertex& vtx) const {
  //tight WP
  bool isTight = muon.isGlobalMuon() &&
                 muon.isPFMuon() &&
                 muon.globalTrack()->normalizedChi2() < tightMuNormalizedChi2Max_ &&
                 muon.globalTrack()->hitPattern().numberOfValidMuonHits() > tightMuNumberOfValidMuonHitsMin_ &&
                 muon.numberOfMatchedStations() > tightMuNumberOfMatchedStationsMin_ &&
                 muon.dB() < tightMudBMax_ &&
                 fabs(muon.muonBestTrack()->dz(vtx.position())) < tightMudZMax_ &&
                 muon.innerTrack()->hitPattern().numberOfValidPixelHits() > tightMuNumberOfValidPixelHitsMin_ &&
                 muon.innerTrack()->hitPattern().trackerLayersWithMeasurement() > tightMuTrackerLayersWithMeasurementMin_;

  return isTight;
}

//https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Identification
bool LeptonProducer::MuonIDhighPt(const pat::Muon & muon, const reco::Vertex& vtx) const {
     bool isHighPt = muon.isGlobalMuon() &&
                     muon.globalTrack()->hitPattern().numberOfValidMuonHits() > 0 &&
                     muon.numberOfMatchedStations() > 1 &&
                     muon.tunePMuonBestTrack()->ptError()/muon.tunePMuonBestTrack()->pt() < 0.3 &&
                     fabs(muon.innerTrack()->dxy(vtx.position())) < 0.2 &&
                     fabs(muon.innerTrack()->dz(vtx.position())) < 0.5 &&
                     muon.innerTrack()->hitPattern().numberOfValidPixelHits() > 0 &&
                     muon.innerTrack()->hitPattern().trackerLayersWithMeasurement() > 5;

  return isHighPt;
}

//https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Identification
bool LeptonProducer::MuonIDtrackerHighPt(const pat::Muon & muon, const reco::Vertex& vtx) const {
     bool isTrackerHighPt = muon.isTrackerMuon() &&
                            muon.track().isNonnull() &&
                            muon.numberOfMatchedStations() > 1 &&
                            muon.tunePMuonBestTrack()->ptError()/muon.tunePMuonBestTrack()->pt() < 0.3 &&
                            fabs(muon.innerTrack()->dxy(vtx.position())) < 0.2 &&
                            fabs(muon.innerTrack()->dz(vtx.position())) < 0.5 &&
                            muon.innerTrack()->hitPattern().numberOfValidPixelHits() > 0 &&
                            muon.innerTrack()->hitPattern().trackerLayersWithMeasurement() > 5;

  return isTrackerHighPt;
}

bool LeptonProducer::ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level, const double rho) const {
  // electron ID cuts
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
  double sieie = electron.full5x5_sigmaIetaIeta();
  bool convVeto = electron.passConversionVeto();
  int mhits = electron.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);;
  double dEtaIn  = electron.deltaEtaSuperClusterTrackAtVtx();
  double dPhiIn  = electron.deltaPhiSuperClusterTrackAtVtx();
  double hoe   = electron.hadronicOverEm();
  double ooemoop = fabs(1.0/electron.ecalEnergy() - electron.eSuperClusterOverP()/electron.ecalEnergy());
  double d0vtx = electron.gsfTrack()->dxy(vtx.position());
  double dzvtx = electron.gsfTrack()->dz(vtx.position());
  bool hovere_pass = false;
  bool relIsoWithEA_pass = false;
  bool reqConvVeto[4] = {true, true, true, true};

  //isolation is part of ID
  double absEta = std::abs(electron.superCluster()->eta());
  auto pfIso  = electron.pfIsolationVariables();
  double isoWithEA  = pfIso.sumChargedHadronPt +
                      std::max(0.0, pfIso.sumNeutralHadronEt + pfIso.sumPhotonEt - rho*GetEffectiveArea(absEta));
  double relIsoWithEA = isoWithEA/electron.pt();

  if (electron.isEB()) {
    hovere_pass = (hovere_constant_) ? eb_hovere_cut_[level] > hoe : eb_hovere_cut_[level] + (eb_hovere_cut2_[level]/electron.energy()) + (eb_hovere_cut3_[level]*rho/electron.energy()) > hoe;
    relIsoWithEA_pass = (relIsoWithEA_constant_) ? eb_relIsoWithEA_cut_[level] > relIsoWithEA : eb_relIsoWithEA_cut_[level] + (eb_relIsoWithEA_cut2_[level]/electron.pt()) > relIsoWithEA;
    return eb_deta_cut_[level] > fabs(dEtaIn)
      && eb_dphi_cut_[level] > fabs(dPhiIn)
      && eb_ieta_cut_[level] > sieie
      && hovere_pass
      && relIsoWithEA_pass
      && eb_d0_cut_[level] > fabs(d0vtx)
      && eb_dz_cut_[level] > fabs(dzvtx)
      && eb_ooeminusoop_cut_[level] > fabs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (eb_misshits_cut_[level] >= mhits);
  } else if (electron.isEE()) {
    hovere_pass = (hovere_constant_) ? ee_hovere_cut_[level] > hoe : ee_hovere_cut_[level] + (ee_hovere_cut2_[level]/electron.energy()) + (ee_hovere_cut3_[level]*rho/electron.energy()) > hoe;
    relIsoWithEA_pass = (relIsoWithEA_constant_) ? ee_relIsoWithEA_cut_[level] > relIsoWithEA : ee_relIsoWithEA_cut_[level] + (ee_relIsoWithEA_cut2_[level]/electron.pt()) > relIsoWithEA;
    return ee_deta_cut_[level] > fabs(dEtaIn)
      && ee_dphi_cut_[level] > fabs(dPhiIn)
      && ee_ieta_cut_[level] > sieie
      && hovere_pass
      && relIsoWithEA_pass
      && ee_d0_cut_[level] > fabs(d0vtx)
      && ee_dz_cut_[level] > fabs(dzvtx)
      && ee_ooeminusoop_cut_[level] > fabs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (ee_misshits_cut_[level] >= mhits);
  } else return false;

}

//https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_X/RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt
double LeptonProducer::GetEffectiveArea(const double absEta) const{

       if(absEta<0) std::runtime_error("LeptonProducer electron EA calculation uses negative abs SC eta!");

       if(absEta<1.0) return 0.1440;
       else if(absEta<1.479) return 0.1562;
       else if(absEta<2.000) return 0.1032;
       else if(absEta<2.200) return 0.0859;
       else if(absEta<2.300) return 0.1116;
       else if(absEta<2.400) return 0.1321;
       else if(absEta<2.500) return 0.1654;
       else return 0.1654;
       //else std::runtime_error("LeptonProducer electron EA calculation encounter max abs SC eta! > 2.5");

}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonProducer);
