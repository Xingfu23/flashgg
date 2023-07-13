#ifndef FLASHgg_VHhadACDNNResult_h
#define FLASHgg_VHhadACDNNResult_h

#include "DataFormats/Common/interface/Ptr.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/Jet.h"

namespace flashgg {
    
    class VHhadACDNNResult
    {
        
    public:
        VHhadACDNNResult();
        VHhadACDNNResult( edm::Ptr<VHhadACDNNResult> );
        virtual ~VHhadACDNNResult() {}
        // diJet Info
        //flashgg::Jet leadJet;
        //flashgg::Jet subleadJet;
        // 3rd jet
        //flashgg::Jet subsubleadJet;
        reco::Candidate::LorentzVector leadJet;
        reco::Candidate::LorentzVector subleadJet;
        reco::Candidate::LorentzVector subsubleadJet;
        reco::Candidate::LorentzVector fourthJet;
        
        edm::Ptr<flashgg::Jet> leadJet_ptr;
        edm::Ptr<flashgg::Jet> subleadJet_ptr;
        // 3rd and 4th jet
        edm::Ptr<flashgg::Jet> subsubleadJet_ptr; 
        edm::Ptr<flashgg::Jet> fourthJet_ptr; 
        // 4-vec of the 3 jets
        
        
        bool hasValidVHhadTriJet;
        bool hasValidVHhadTetraJet;
        
        // di-photon info 
        // flashgg::DiPhotonCandidate diphoton;
        
        // event based variables
        int  n_rec_jets;
        int  n_gen_jets;
        int  n_diphotons;
        
        // Input variables
        float dijet_leadEta ;
        float dijet_subleadEta;
        float dijet_abs_dEta;
        float dijet_LeadJPt ;
        float dijet_pt ;
        float dijet_SubJPt;
        float dijet_Zep;
        float dijet_dphi_trunc;
        float dijet_dipho_dphi;
        float dijet_dphi;
        float dijet_Mjj;
        float dijet_dy;
        float dijet_leady ;
        float dijet_subleady;
        float dijet_dipho_pt;
        float dijet_minDRJetPho;
        float dijet_centrality_gg;
        float dijet_centrality_j3;
        float dijet_centrality_g ;
        float cosThetaStar;
        
        float dipho_PToM;
        float leadPho_PToM;
        float sublPho_PToM;

        // DNN for VH had anomalous couplings 
        float dnnvh_bkg_value() const {return dnnvh_bkg;}
        float dnnvh_sm_value() const {return dnnvh_sm;}
        float dnnvh_bsm_value() const {return dnnvh_bsm;}

        // Output
        float dnnvh_bkg;
        float dnnvh_sm;
        float dnnvh_bsm;
    };
    
    typedef std::map<edm::Ptr<DiPhotonCandidate>, VHhadACDNNResult> VHhadACDNNResultMap;
    
}

#endif
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

