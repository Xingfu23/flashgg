#ifndef FLASHgg_WHLeptonicTag_h
#define FLASHgg_WHLeptonicTag_h

#include "flashgg/DataFormats/interface/DiPhotonTagBase.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/DataFormats/interface/Met.h"
#include "flashgg/DataFormats/interface/Electron.h"
#include "flashgg/DataFormats/interface/Muon.h"

namespace flashgg {

    class WHLeptonicTag: public DiPhotonTagBase
    {
    public:
        WHLeptonicTag();
        WHLeptonicTag( edm::Ptr<DiPhotonCandidate>, edm::Ptr<DiPhotonMVAResult> );
        WHLeptonicTag( edm::Ptr<DiPhotonCandidate>, DiPhotonMVAResult );
        ~WHLeptonicTag();

        WHLeptonicTag *clone() const override { return ( new WHLeptonicTag( *this ) ); }

        const std::vector<edm::Ptr<Muon> > muons() const { return Muons_;}
        const std::vector<edm::Ptr<flashgg::Electron> > electrons() const {return Electrons_;}
        const std::vector<edm::Ptr<Jet> > jets() const { return Jets_;}
        const edm::Ptr<flashgg::Met> met() const { return MET_;}

        const bool associatedZ() const { return associatedZ_; }
        const bool associatedW() const { return associatedW_; }
        const bool VhasNeutrinos() const { return VhasNeutrinos_; }
        const bool VhasLeptons() const { return VhasLeptons_; }
        const bool VhasHadrons() const { return VhasHadrons_; }
        const float Vpt() const { return Vpt_; }

        void setJets( std::vector<edm::Ptr<Jet> > Jets ) { Jets_ = Jets; }
        void setMuons( std::vector<edm::Ptr<Muon> >Muons ) {Muons_ = Muons;}
        void setMET( edm::Ptr<flashgg::Met>  MET ) {MET_ = MET;}
        void setElectrons( std::vector<edm::Ptr<Electron> > Electrons ) {Electrons_ = Electrons;}

        void setAssociatedZ( const bool &val ) { associatedZ_ = val; }
        void setAssociatedW( const bool &val ) { associatedW_ = val; }
        void setVhasNeutrinos( const bool &val ) { VhasNeutrinos_ = val; }
        void setVhasLeptons( const bool &val ) { VhasLeptons_ = val; }
        void setVhasHadrons( const bool &val ) { VhasHadrons_ = val; }
        void setVpt( const float &val ) { Vpt_ = val; }

        //STXS & AC MVA Get Functions...
        const float VHmva() const { return VH_mva;};
        const float WHiggs0MToGG_mva()          const { return WHiggs0MToGG_MVA;};
        const float WHiggs0PHToGG_mva()         const { return WHiggs0PHToGG_MVA;};
        const float WHiggs0L1ToGG_mva()         const { return WHiggs0L1ToGG_MVA;};
        
        //STXS & AC MVA Set Functions...
        void set_VHmva(const float &val) {VH_mva=val;};
        void set_WHiggs0MToGG_MVA(const float &val)           { WHiggs0MToGG_MVA = val;};
        void set_WHiggs0PHToGG_MVA(const float &val)          { WHiggs0PHToGG_MVA = val;};
        void set_WHiggs0L1ToGG_MVA(const float &val)          { WHiggs0L1ToGG_MVA = val;};

        DiPhotonTagBase::tag_t tagEnum() const override {return DiPhotonTagBase::kWHLeptonic; }

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
        //Private Variables for get/set functions with initial values of -999
        float VH_mva = -999;
        float WHiggs0MToGG_MVA = -999;
        float WHiggs0PHToGG_MVA = -999;
        float WHiggs0L1ToGG_MVA = -999;
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

