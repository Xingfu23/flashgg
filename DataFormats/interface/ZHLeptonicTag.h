#ifndef FLASHgg_ZHLeptonicTag_h
#define FLASHgg_ZHLeptonicTag_h

#include "flashgg/DataFormats/interface/DiPhotonTagBase.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/DataFormats/interface/Met.h"
#include "flashgg/DataFormats/interface/Electron.h"
#include "flashgg/DataFormats/interface/Muon.h"

namespace flashgg {

    class ZHLeptonicTag: public DiPhotonTagBase
    {
    public:
        ZHLeptonicTag();
        ZHLeptonicTag( edm::Ptr<DiPhotonCandidate>, edm::Ptr<DiPhotonMVAResult> );
        ZHLeptonicTag( edm::Ptr<DiPhotonCandidate>, DiPhotonMVAResult );
        ~ZHLeptonicTag();

        ZHLeptonicTag *clone() const override { return ( new ZHLeptonicTag( *this ) ); }
        
        const std::vector<edm::Ptr<Muon> > muons() const { return Muons_;}
        const std::vector<edm::Ptr<flashgg::Electron> > electrons() const {return Electrons_;}
        const std::vector<edm::Ptr<Jet> > jets() const { return Jets_;}
        const edm::Ptr<flashgg::Met>  met() const { return MET_;}

        const bool associatedZ() const { return associatedZ_; }
        const bool associatedW() const { return associatedW_; }
        const bool VhasNeutrinos() const { return VhasNeutrinos_; }
        const bool VhasLeptons() const { return VhasLeptons_; }
        const bool VhasHadrons() const { return VhasHadrons_; }
        const float Vpt() const { return Vpt_; }

        void setJets( std::vector<edm::Ptr<Jet> > Jets ) { Jets_ = Jets; }
        void setMuons( std::vector<edm::Ptr<Muon> > Muons ) {Muons_ = Muons;}
        void setMET( edm::Ptr<flashgg::Met> MET ) {MET_ = MET;}
        void setElectrons( std::vector<edm::Ptr<Electron> > Electrons ) {Electrons_ = Electrons;}

        void setAssociatedZ( const bool &val ) { associatedZ_ = val; }
        void setAssociatedW( const bool &val ) { associatedW_ = val; }
        void setVhasNeutrinos( const bool &val ) { VhasNeutrinos_ = val; }
        void setVhasLeptons( const bool &val ) { VhasLeptons_ = val; }
        void setVhasHadrons( const bool &val ) { VhasHadrons_ = val; }
        void setVpt( const float &val ) { Vpt_ = val; }

        DiPhotonTagBase::tag_t tagEnum() const override {return DiPhotonTagBase::kZHLeptonic; }

        //Custom variable for Anomalous Studies
        const float VHmva() const { return VH_mva;};
        const float ZHiggs0MToGG_mva()          const {return ZHiggs0MToGG_MVA;};
        const float ZHiggs0PHToGG_mva()         const {return ZHiggs0PHToGG_MVA;};
        const float ZHiggs0L1ToGG_mva()         const {return ZHiggs0L1ToGG_MVA;};
        const float ZHiggs0L1ZgToGG_mva()       const {return ZHiggs0L1ZgToGG_MVA;};

        //Functions to set the variables
        void set_VHmva(const float &val) {VH_mva=val;};
        void set_ZHiggs0MToGG_MVA(const float &val)           { ZHiggs0MToGG_MVA = val;};
        void set_ZHiggs0PHToGG_MVA(const float &val)          { ZHiggs0PHToGG_MVA = val;};
        void set_ZHiggs0L1ToGG_MVA(const float &val)          { ZHiggs0L1ToGG_MVA = val;};
        void set_ZHiggs0L1ZgToGG_MVA(const float &val)        { ZHiggs0L1ZgToGG_MVA = val;};

    private:
        std::vector<edm::Ptr<Muon> > Muons_;
        std::vector<edm::Ptr<Electron> > Electrons_;
        std::vector<edm::Ptr<Jet> > Jets_;
        edm::Ptr<flashgg::Met> MET_;

        bool associatedZ_;
        bool associatedW_;
        bool VhasNeutrinos_;
        bool VhasLeptons_;
        bool VhasHadrons_;
        float Vpt_;

        float VH_mva = -999;
        float ZHiggs0MToGG_MVA =-999;
        float ZHiggs0PHToGG_MVA =-999;
        float ZHiggs0L1ToGG_MVA =-999;
        float ZHiggs0L1ZgToGG_MVA =-999;

    };
}

#endif

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

