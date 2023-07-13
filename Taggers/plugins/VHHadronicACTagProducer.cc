#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/VHHadronicACTag.h"
#include "flashgg/DataFormats/interface/VHhadACDNNResult.h"

#include "flashgg/DataFormats/interface/VHTagTruth.h"
#include "DataFormats/Common/interface/RefToPtr.h"

#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <TLorentzVector.h>
#include "TMath.h"

using namespace std;
using namespace edm;

typedef std::pair< edm::Ptr<flashgg::Jet>, edm::Ptr<flashgg::Jet> > jetptrpair;


namespace flashgg {

    class VHHadronicACTagProducer : public EDProducer
    {

    public:
        VHHadronicACTagProducer( const ParameterSet & );
    private:

        void produce( Event &, const EventSetup & ) override;
        int chooseCategory(float dnnvh_bkg, float dnnvh_bsm);

        std::vector<edm::EDGetTokenT<View<flashgg::Jet> > > tokenJets_;
        EDGetTokenT<View<DiPhotonCandidate> > diPhotonToken_;
        //EDGetTokenT<View<Jet> > thejetToken_;
        EDGetTokenT<View<VHhadACDNNResult> >  VHhadACDNNResultToken_;
        EDGetTokenT<View<DiPhotonMVAResult> > mvaResultToken_;
        EDGetTokenT<View<reco::GenParticle> > genParticleToken_;
        std::vector<edm::InputTag> inputTagJets_;
        typedef std::vector<edm::Handle<edm::View<flashgg::Jet> > > JetCollectionVector;

        //Thresholds
        double leadPhoOverMassThreshold_;
        double subleadPhoOverMassThreshold_;
        double diphoMVAThreshold_;
        double jetsNumberThreshold_;
        double jetPtThreshold_;
        double jetEtaThreshold_;
        double dRJetToPhoLThreshold_;
        double dRJetToPhoSThreshold_;
        double dijetMassLowThreshold_;
        double dijetMassHighThreshold_;
        double cosThetaStarThreshold_;
        double minPhoIdMVAThreshold_;
        double maxPhoIdMVAThreshold_;

        vector<double> cat_dnnbkg;
        vector<double> cat_dnnbsm;

        string systLabel_;



    };

    VHHadronicACTagProducer::VHHadronicACTagProducer( const ParameterSet &iConfig ) :

        diPhotonToken_( consumes<View<flashgg::DiPhotonCandidate> >( iConfig.getParameter<InputTag> ( "DiPhotonTag" ) ) ),
        //thejetToken_     ( consumes<View<flashgg::Jet> >( iConfig.getParameter<InputTag>( "JetTag" ) ) ),
        VHhadACDNNResultToken_( consumes<View<flashgg::VHhadACDNNResult> >( iConfig.getParameter<InputTag> ( "VHhadACDNNResult" ) ) ),
        mvaResultToken_( consumes<View<flashgg::DiPhotonMVAResult> >( iConfig.getParameter<InputTag> ( "MVAResultTag" ) ) ),
        genParticleToken_( consumes<View<reco::GenParticle> >( iConfig.getParameter<InputTag> ( "GenParticleTag" ) ) ),
        systLabel_( iConfig.getParameter<string> ( "SystLabel" ) )
    {

        // ***** define thresholds ***********************

        leadPhoOverMassThreshold_    = iConfig.getParameter<double>( "leadPhoOverMassThreshold" );
        subleadPhoOverMassThreshold_ = iConfig.getParameter<double>( "subleadPhoOverMassThreshold" );
        diphoMVAThreshold_           = iConfig.getParameter<double>( "diphoMVAThreshold" );
        jetsNumberThreshold_         = iConfig.getParameter<double>( "jetsNumberThreshold" );
        jetPtThreshold_              = iConfig.getParameter<double>( "jetPtThreshold" );
        jetEtaThreshold_             = iConfig.getParameter<double>( "jetEtaThreshold" );
        dRJetToPhoLThreshold_        = iConfig.getParameter<double>( "dRJetToPhoLThreshold" );
        dRJetToPhoSThreshold_        = iConfig.getParameter<double>( "dRJetToPhoSThreshold" );
        dijetMassLowThreshold_       = iConfig.getParameter<double>( "dijetMassLowThreshold" );
        dijetMassHighThreshold_      = iConfig.getParameter<double>( "dijetMassHighThreshold" );
        cosThetaStarThreshold_       = iConfig.getParameter<double>( "cosThetaStarThreshold" );
        minPhoIdMVAThreshold_        = iConfig.getParameter<double>( "minPhoIdMVAThreshold" );
        maxPhoIdMVAThreshold_        = iConfig.getParameter<double>( "maxPhoIdMVAThreshold" );

        cat_dnnbkg = iConfig.getParameter<vector<double > >( "Categories_dnnbkg" );
        cat_dnnbsm = iConfig.getParameter<vector<double > >( "Categories_dnnbsm" );
        
        // yacine: new recipe for flashgg jets
        inputTagJets_                = iConfig.getParameter<std::vector<edm::InputTag> >( "inputTagJets" );

        // *************************************************

        for (unsigned i = 0 ; i < inputTagJets_.size() ; i++) {
            auto token = consumes<View<flashgg::Jet> >(inputTagJets_[i]);
            tokenJets_.push_back(token);
        }
        produces<vector<VHHadronicACTag> >();
        produces<vector<VHTagTruth> >();
    }
    
    int VHHadronicACTagProducer::chooseCategory( float dnnvh_bkg, float dnnvh_bsm ) {
        //0 = Bkg, 1 = SM1, 2 = SM2, 3 = SM3, 4 = BSM1, 5 = BSM2
        int cat = 0;

        if( (double)dnnvh_bkg < 0.0 || (double)dnnvh_bsm < 0.0 ){
            cat = -1;
        } else if( (double)dnnvh_bkg < cat_dnnbkg[0] && (double)dnnvh_bsm < cat_dnnbsm[0] ){
            cat = 1;
        } else if( (double)dnnvh_bkg > cat_dnnbkg[0] && (double)dnnvh_bkg < cat_dnnbkg[1] && (double)dnnvh_bsm < cat_dnnbsm[1] ){ 
            cat = 2;
        } else if( (double)dnnvh_bkg > cat_dnnbkg[1] && (double)dnnvh_bkg < cat_dnnbkg[2] && (double)dnnvh_bsm < cat_dnnbsm[2] ){ 
            cat = 3;
        } else if( (double)dnnvh_bkg < cat_dnnbkg[3] && (double)dnnvh_bsm > cat_dnnbsm[3] ){ 
            cat = 4;
        } else if( (double)dnnvh_bkg < cat_dnnbkg[4] && (double)dnnvh_bsm > cat_dnnbsm[4] && ((double)dnnvh_bkg > cat_dnnbkg[3] || (double)dnnvh_bsm < cat_dnnbsm[3]) ){ 
            cat = 5;
        }

        return cat;
    }

    void VHHadronicACTagProducer::produce( Event &evt, const EventSetup & )
    {
        Handle<View<flashgg::DiPhotonCandidate> > diPhotons;
        evt.getByToken( diPhotonToken_, diPhotons );
        //  const PtrVector<flashgg::DiPhotonCandidate>& diPhotonPointers = diPhotons->ptrVector();

        //  Yacine : this is not longer supported
        //  Handle<View<flashgg::Jet> > theJets;
        //  evt.getByToken( thejetToken_, theJets );
        //  const PtrVector<flashgg::Jet>& jetPointers = theJets->ptrVector();

        JetCollectionVector Jets( inputTagJets_.size() );
        for( size_t j = 0; j < inputTagJets_.size(); ++j ) {
            evt.getByToken( tokenJets_[j], Jets[j] );
        }

        Handle<View<flashgg::VHhadACDNNResult> > VHhadACDNNs;
        evt.getByToken( VHhadACDNNResultToken_, VHhadACDNNs );

        Handle<View<flashgg::DiPhotonMVAResult> > mvaResults;
        evt.getByToken( mvaResultToken_, mvaResults );
        //   const PtrVector<flashgg::DiPhotonMVAResult>& mvaResultPointers = mvaResults->ptrVector();

        Handle<View<reco::GenParticle> > genParticles;

        std::unique_ptr<vector<VHHadronicACTag> > vhhadactags( new vector<VHHadronicACTag> );
        std::unique_ptr<vector<VHTagTruth> > truths( new vector<VHTagTruth> );
        
        bool associatedZ=0;
        bool associatedW=0;
        bool VhasDaughters=0;
        bool VhasNeutrinos=0;
        bool VhasLeptons=0;
        bool VhasHadrons=0;
        bool VhasMissingLeptons=0;
        float Vpt=0;

        if( ! evt.isRealData() )
            {
                evt.getByToken( genParticleToken_, genParticles );
                for( unsigned int genLoop = 0 ; genLoop < genParticles->size(); genLoop++ )
                    {
                        int pdgid = genParticles->ptrAt( genLoop )->pdgId();
                        int dpdgid[2] = {0,0};
                        if(pdgid ==23) //z-boson
                            {
                                associatedZ=1;
                                if( genParticles->ptrAt( genLoop )->numberOfDaughters()==2)
                                    {
                                        VhasDaughters=1;
                                        dpdgid[0]=genParticles->ptrAt(genLoop)->daughter(0)->pdgId();
                                        //dpdgid[1]=genParticles->ptrAt(genLoop)->daughter(1)->pdgId();
                                        Vpt=genParticles->ptrAt( genLoop )->pt();
                                        if(fabs(dpdgid[0])==12||fabs(dpdgid[0])==14||fabs(dpdgid[0])==16) //look for neutrino decay of Z
                                            {
                                                VhasNeutrinos=1;
                                            }
                                        if(fabs(dpdgid[0])==11||fabs(dpdgid[0])==13||fabs(dpdgid[0])==15) //look for lepton decay of Z  
                                            {
                                                VhasLeptons=1;
                                            }
                                        if(fabs(dpdgid[0])>0&&fabs(dpdgid[0])<9) //look for quark decay of Z   
                                            {
                                                VhasHadrons=1;
                                            }
                                    }
                            }
                        if(fabs(pdgid)==24) //look for W      
                            {
                                associatedW=1;
                                if( genParticles->ptrAt( genLoop )->numberOfDaughters()==2)
                                    {
                                        VhasDaughters=1;
                                        Vpt=genParticles->ptrAt( genLoop )->pt();
                                        dpdgid[0]=genParticles->ptrAt(genLoop)->daughter(0)->pdgId();
                                        //dpdgid[1]=genParticles->ptrAt(genLoop)->daughter(1)->pdgId();
                                        if(fabs(dpdgid[0])==12||fabs(dpdgid[0])==14||fabs(dpdgid[0])==16) //look for neutrino decay of W
                                            {
                                                VhasNeutrinos=1;
                                                VhasLeptons=1;
                                            }
                                        if(fabs(dpdgid[0])==11||fabs(dpdgid[0])==13||fabs(dpdgid[0])==15) //look for lepton decay of W  
                                            {
                                                VhasNeutrinos=1;
                                                VhasLeptons=1;
                                            }
                                        if(fabs(dpdgid[0])>0&&fabs(dpdgid[0])<9) //look for quark decay of W  
                                            {
                                                VhasHadrons=1;
                                            }

                                    }
                            }
                    }
            }


        edm::RefProd<vector<VHTagTruth> > rTagTruth = evt.getRefBeforePut<vector<VHTagTruth> >();
        unsigned int idx = 0;

        assert( diPhotons->size() == mvaResults->size() );
        double idmva1 = 0.;
        double idmva2 = 0.;
        for( unsigned int diphoIndex = 0; diphoIndex < diPhotons->size(); diphoIndex++ ) {

            edm::Ptr<flashgg::DiPhotonCandidate>   dipho = diPhotons->ptrAt( diphoIndex );
            edm::Ptr<flashgg::DiPhotonMVAResult>  mvares = mvaResults->ptrAt( diphoIndex );
            edm::Ptr<flashgg::VHhadACDNNResult> vhhadac_dnnres = VHhadACDNNs->ptrAt( diphoIndex );

            // ********** photon ID and diphoton requirements: *********

            if( dipho->leadingPhoton()->pt() < ( dipho->mass() )*leadPhoOverMassThreshold_ ) { continue; }
            if( dipho->subLeadingPhoton()->pt() < ( dipho->mass() )*subleadPhoOverMassThreshold_ ) { continue; }

            idmva1 = dipho->leadingPhoton()->phoIdMvaDWrtVtx( dipho->vtx() );
            idmva2 = dipho->subLeadingPhoton()->phoIdMvaDWrtVtx( dipho->vtx() );
            if( idmva1 <= idmva2 && (idmva1 <= minPhoIdMVAThreshold_ || idmva2 <= maxPhoIdMVAThreshold_) ) { continue; }
            if( idmva1 > idmva2 && (idmva1 <= maxPhoIdMVAThreshold_ || idmva2 <= minPhoIdMVAThreshold_) ) { continue; }

            if( mvares->result < diphoMVAThreshold_ ) { continue; }
            
            // cut on pt_gg / m_gg
            //if( dipho->pt() / dipho->mass() < 1. )   {
            //    std::cout << "dipho pt / m not passed..." << std::endl;
            //    continue;}
            
            std::vector<edm::Ptr<flashgg::Jet> > goodJets;

            unsigned int jetCollectionIndex = diPhotons->ptrAt( diphoIndex )->jetCollectionIndex();
            
            for( size_t ijet = 0; ijet < Jets[jetCollectionIndex]->size(); ijet++ ) {

                edm::Ptr<flashgg::Jet> thejet = Jets[jetCollectionIndex]->ptrAt( ijet );
                
                if(!thejet->passesJetID  ( flashgg::Tight2017 ) ) { continue; }
                if( fabs( thejet->eta() ) > jetEtaThreshold_ )    { continue; }
                if( thejet->pt() < jetPtThreshold_ )              { continue; }

                float dPhiJetToPhoL = deltaPhi( dipho->leadingPhoton()->phi(), thejet->phi() );
                float dEtaJetToPhoL = dipho->leadingPhoton()->eta() - thejet->eta();
                float dRJetToPhoL   = sqrt( dEtaJetToPhoL * dEtaJetToPhoL + dPhiJetToPhoL * dPhiJetToPhoL );

                float dPhiJetToPhoS = deltaPhi( dipho->subLeadingPhoton()->phi(), thejet->phi() );
                float dEtaJetToPhoS = dipho->subLeadingPhoton()->eta() - thejet->eta();
                float dRJetToPhoS   = sqrt( dEtaJetToPhoS * dEtaJetToPhoS + dPhiJetToPhoS * dPhiJetToPhoS );

                if( abs( dRJetToPhoL ) < dRJetToPhoLThreshold_ )            { continue; }
                if( abs( dRJetToPhoS ) < dRJetToPhoSThreshold_ )            { continue; }

                goodJets.push_back( thejet );
            }
            
            // *********************************************************************
            //            std::cout << "-----------------------------------------------------number of jets: " << goodJets.size() << std::endl;
            if( goodJets.size() < 2 ) { continue; }

            TLorentzVector jetl, jets, dijet, phol, phos, diphoton, vstar;

            phol.SetPtEtaPhiE( dipho->leadingPhoton()->pt(), dipho->leadingPhoton()->eta(), dipho->leadingPhoton()->phi(), dipho->leadingPhoton()->energy() );
            phos.SetPtEtaPhiE( dipho->subLeadingPhoton()->pt(), dipho->subLeadingPhoton()->eta(), dipho->subLeadingPhoton()->phi(), dipho->subLeadingPhoton()->energy() );
            jetl.SetPtEtaPhiE( goodJets[0]->pt(), goodJets[0]->eta(), goodJets[0]->phi(), goodJets[0]->energy() );
            jets.SetPtEtaPhiE( goodJets[1]->pt(), goodJets[1]->eta(), goodJets[1]->phi(), goodJets[1]->energy() );

            diphoton = phol + phos;
            dijet = jetl + jets;
            vstar = diphoton + dijet;

            float invmass = dijet.M();

            if( invmass <= dijetMassLowThreshold_ || invmass > dijetMassHighThreshold_ ) { continue; }  // go out of diphoton loop

            diphoton.Boost( -vstar.BoostVector() );
            float costhetastar = -diphoton.CosTheta();
            if( abs( costhetastar ) < cosThetaStarThreshold_ ) { continue; }

            VHHadronicACTag vhhadactag_obj( dipho, mvares, vhhadac_dnnres );
            vhhadactag_obj.includeWeights( *dipho );
            vhhadactag_obj.setJets( goodJets[0], goodJets[1] );
            vhhadactag_obj.setDiPhotonIndex( diphoIndex );
            vhhadactag_obj.setSystLabel( systLabel_ );
            float dnn_bkg = vhhadac_dnnres->dnnvh_bkg_value();
            float dnn_bsm = vhhadac_dnnres->dnnvh_bsm_value();
            int catnum = chooseCategory(dnn_bkg, dnn_bsm);
            vhhadactag_obj.setCategoryNumber( catnum );
            if( vhhadactag_obj.categoryNumber() >= 0 ){
                vhhadactags->push_back( vhhadactag_obj );
                
                if( ! evt.isRealData() ) {
                    VHTagTruth truth_obj;
                    truth_obj.setAssociatedZ( associatedZ );
                    truth_obj.setAssociatedW( associatedW );
                    truth_obj.setVhasDaughters( VhasDaughters );
                    truth_obj.setVhasNeutrinos( VhasNeutrinos );
                    truth_obj.setVhasLeptons( VhasLeptons );
                    truth_obj.setVhasHadrons( VhasHadrons );
                    truth_obj.setVhasMissingLeptons( VhasMissingLeptons );
                    truth_obj.setVpt( Vpt );
                    truths->push_back( truth_obj );
                    vhhadactags->back().setTagTruth( edm::refToPtr( edm::Ref<vector<VHTagTruth> >( rTagTruth, idx++ ) ) );
                }
            }
        }
        evt.put( std::move( vhhadactags ) );
        evt.put( std::move( truths ) );
    }
}
typedef flashgg::VHHadronicACTagProducer FlashggVHHadronicACTagProducer;
DEFINE_FWK_MODULE( FlashggVHHadronicACTagProducer );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

