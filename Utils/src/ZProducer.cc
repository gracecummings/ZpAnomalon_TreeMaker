// system include files
#include <memory>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// new includes
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"

class ZProducer : public edm::global::EDProducer<> {
public:
	explicit ZProducer(const edm::ParameterSet&);
private:
   void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
   edm::InputTag ElectronTag_;
   edm::InputTag MuonTag_;
   edm::EDGetTokenT<std::vector<pat::Electron>> ElectronTok_;
   edm::EDGetTokenT<std::vector<pat::Muon>> MuonTok_;
};

ZProducer::ZProducer(const edm::ParameterSet& iConfig)
{
   ElectronTag_ = iConfig.getParameter<edm::InputTag>("ElectronTag");
   MuonTag_ = iConfig.getParameter<edm::InputTag>("MuonTag");
   
   ElectronTok_ = consumes<std::vector<pat::Electron>>(ElectronTag_);
   MuonTok_ = consumes<std::vector<pat::Muon>>(MuonTag_);
   
   produces<pat::CompositeCandidateCollection>("ZCandidates");
   produces<std::vector<pat::Muon>>("SelectedMuons");
   produces<std::vector<pat::Electron>>("SelectedElectrons");
}

void ZProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
   auto ZCandidates     = std::make_unique<pat::CompositeCandidateCollection>();
   auto SelectedMuons   = std::make_unique<std::vector<pat::Muon>>();
   auto SelectedElectrons   = std::make_unique<std::vector<pat::Electron>>();

   bool findZ = false;
   pat::CompositeCandidate theZ;
   pat::CompositeCandidate aZ;
   std::list<pat::CompositeCandidate> aZlist;
   std::list<pat::CompositeCandidate>::iterator zit;

   //The actual Z selection, not just the candidates
   int zIdx = 0;
   double baseMassZdiff = 99999;

   // select Zmumu
   edm::Handle<std::vector<pat::Muon>> muonHandle;
   iEvent.getByToken(MuonTok_, muonHandle);
   const std::vector<pat::Muon> * muons = muonHandle.product();
   pat::Muon mu1;
   pat::Muon mu2;
   std::list<pat::Muon> leadMuons;
   std::list<pat::Muon> subMuons;

   for (std::vector<pat::Muon>::const_iterator iL1 = muons->begin(); iL1 != muons->end(); ++iL1) {
       if (iL1->pt() > 60.0) { // pat collection is pT-ordered
          for (const auto & muon : *muons) {
	       if (iL1->charge()*muon.charge() > 0) continue;
	       mu1 = *(iL1->clone());
	       mu2 = muon;
	       aZ.setP4(mu1.p4()+muon.p4());
	       //if ((aZ.mass() <=110) && (aZ.mass()) >= 70){
		  aZlist.push_back(aZ);
		  leadMuons.push_back(mu1);
		  subMuons.push_back(mu2);
                  findZ = true;
		  //}
	  }
      }
   }

   for (zit = aZlist.begin(); zit != aZlist.end(); ++zit) {
     double massZdiff = std::abs(91.18 - zit->mass());
     if (massZdiff < baseMassZdiff) {
       baseMassZdiff = massZdiff;
       theZ.setP4(zit->p4());
       zIdx = std::distance(aZlist.begin(),zit);//THIS NEEDS ATTENTION
     }
   }
   
   if(findZ){
   std::list<pat::Muon>::iterator mu1it = leadMuons.begin();
   std::list<pat::Muon>::iterator mu2it = subMuons.begin();
   ZCandidates->push_back(theZ);
   std::advance(mu1it,zIdx);
   std::advance(mu2it,zIdx);
   SelectedMuons->push_back(*mu1it);
   SelectedMuons->push_back(*mu2it);
   }

   // reset
   aZlist.clear(); 
   leadMuons.clear();
   subMuons.clear();
   zIdx = 0;
   baseMassZdiff = 99999;
   findZ = false;

   // Zee selection
   edm::Handle<std::vector<pat::Electron>> electronHandle;
   iEvent.getByToken(ElectronTok_, electronHandle);
   const std::vector<pat::Electron> * electrons = electronHandle.product();
   pat::Electron e1;
   pat::Electron e2;
   std::list<pat::Electron> leadElectrons;
   std::list<pat::Electron> subElectrons;

   for (std::vector<pat::Electron>::const_iterator iL1 = electrons->begin(); iL1 != electrons->end(); ++iL1) {
       if (iL1->pt() > 120.0) { // pat collection is pT-ordered
          for (const auto & electron : *electrons) {
               if (iL1->charge()*electron.charge() > 0) continue;
               e1 = *(iL1->clone());
               e2 = electron;
               aZ.setP4(e1.p4()+e2.p4());
               if ( aZ.mass() <= 110 && aZ.mass() >= 70){
                  aZlist.push_back(aZ);
                  leadElectrons.push_back(e1);
                  subElectrons.push_back(e2);
                  findZ = true;
               }
          }
      }
   }
   for (zit = aZlist.begin(); zit != aZlist.end(); ++zit) {
     double massZdiff = std::abs(91.18 - zit->mass());
     if (massZdiff < baseMassZdiff) {
       baseMassZdiff = massZdiff;
       theZ.setP4(zit->p4());
       zIdx = std::distance(aZlist.begin(),zit);//THIS NEEDS ATTENTION
     }
   }
   if(findZ){
   std::list<pat::Electron>::iterator e1it = leadElectrons.begin();
   std::list<pat::Electron>::iterator e2it = subElectrons.begin();
   ZCandidates->push_back(theZ);
   std::advance(e1it,zIdx);
   std::advance(e2it,zIdx);
   SelectedElectrons->push_back(*e1it);
   SelectedElectrons->push_back(*e2it);
   }

   // add the Z candidates to the event
   iEvent.put(std::move(ZCandidates), std::string("ZCandidates"));
   iEvent.put(std::move(SelectedMuons), std::string("SelectedMuons"));
   iEvent.put(std::move(SelectedElectrons), std::string("SelectedElectrons"));

}

//define this as a plug-in
DEFINE_FWK_MODULE(ZProducer);

