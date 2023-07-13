#ifndef FLASHgg_VHHadronicACTag_h
#define FLASHgg_VHHadronicACTag_h

#include "flashgg/DataFormats/interface/DiPhotonTagBase.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/DataFormats/interface/VHhadACDNNResult.h"


namespace flashgg {

    class VHHadronicACTag: public DiPhotonTagBase
    {

    public:

        VHHadronicACTag();
        VHHadronicACTag( edm::Ptr<DiPhotonCandidate>, DiPhotonMVAResult, VHhadACDNNResult );
        VHHadronicACTag( edm::Ptr<DiPhotonCandidate>, edm::Ptr<DiPhotonMVAResult>, edm::Ptr<VHhadACDNNResult> );
        VHHadronicACTag *clone() const override;
        ~VHHadronicACTag();

        const VHhadACDNNResult VHhadACDNN() const;

        const edm::Ptr<flashgg::Jet>      leadingJet()  const  { return leadingJet_; }
        const edm::Ptr<flashgg::Jet>      subLeadingJet() const { return subleadingJet_; }
        const edm::Ptr<DiPhotonCandidate> diPhotonCandidate() const { return theDiPhotonCandidate_;}
        //const edm::Ptr<DiPhotonMVAResult> diPhotonMVAResult() const { return theDiPhotonMVAResult_;} // doesn't work for some reason

        void setJets( edm::Ptr<flashgg::Jet>, edm::Ptr<flashgg::Jet> );

        DiPhotonTagBase::tag_t tagEnum() const override {return DiPhotonTagBase::kVHHadronicAC; }

    private:
        edm::Ptr<DiPhotonCandidate> theDiPhotonCandidate_;
        //edm::Ptr<DiPhotonMVAResult> theDiPhotonMVAResult_;
        //std::pair<edm::Ptr<flashgg::Jet>,edm::Ptr<flashgg::Jet> > JetPair_;
        edm::Ptr<flashgg::Jet> leadingJet_;
        edm::Ptr<flashgg::Jet> subleadingJet_;
        VHhadACDNNResult vhhadac_dnnres_;

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

