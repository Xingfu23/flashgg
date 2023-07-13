#include "flashgg/DataFormats/interface/VHHadronicACTag.h"

using namespace flashgg;

VHHadronicACTag::VHHadronicACTag() : DiPhotonTagBase::DiPhotonTagBase()
{}

VHHadronicACTag::~VHHadronicACTag()
{}


VHHadronicACTag::VHHadronicACTag( edm::Ptr<DiPhotonCandidate> diPho, DiPhotonMVAResult mvares, VHhadACDNNResult vhhadac_dnnres ) : DiPhotonTagBase::DiPhotonTagBase( diPho, mvares ) 
{
    vhhadac_dnnres_ = vhhadac_dnnres;
}

VHHadronicACTag::VHHadronicACTag( edm::Ptr<DiPhotonCandidate> diPho, edm::Ptr<DiPhotonMVAResult> mvares, edm::Ptr<VHhadACDNNResult> vhhadac_dnnres ) : VHHadronicACTag::VHHadronicACTag( diPho, *mvares, *vhhadac_dnnres ){}

const VHhadACDNNResult VHHadronicACTag::VHhadACDNN() const
{
    return vhhadac_dnnres_;
}

void VHHadronicACTag::setJets( edm::Ptr<flashgg::Jet> ljet, edm::Ptr<flashgg::Jet> sjet )
{
    leadingJet_    = ljet;
    subleadingJet_ = sjet;
}


VHHadronicACTag *VHHadronicACTag::clone() const
{
    VHHadronicACTag *result = new VHHadronicACTag( *this );
    return result;
}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

