#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/StageOneCombinedTag.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

using namespace flashgg;

StageOneCombinedTag::StageOneCombinedTag() {}

StageOneCombinedTag::~StageOneCombinedTag() {}

StageOneCombinedTag::StageOneCombinedTag( edm::Ptr<flashgg::DiPhotonCandidate> diPho, edm::Ptr<DiPhotonMVAResult> mvaRes ) :
    StageOneCombinedTag::StageOneCombinedTag( diPho, *mvaRes ) {}

StageOneCombinedTag::StageOneCombinedTag( edm::Ptr<DiPhotonCandidate> dipho, DiPhotonMVAResult mvares ) :
    DiPhotonTagBase::DiPhotonTagBase( dipho, mvares ) {
}

StageOneCombinedTag::StageOneCombinedTag( edm::Ptr<flashgg::DiPhotonCandidate> diPho, edm::Ptr<DiPhotonMVAResult> mvaRes, edm::Ptr<VBFMVAResult> vbf_mvaRes, edm::Ptr<VHhadMVAResult> vhHad_mvaRes, edm::Ptr<VHhadACDNNResult> vhHadAC_dnnRes, edm::Ptr<GluGluHMVAResult> ggh_mvaRes ) :
    StageOneCombinedTag::StageOneCombinedTag( diPho, *mvaRes, *vbf_mvaRes, *vhHad_mvaRes, *vhHadAC_dnnRes, *ggh_mvaRes ) {}

StageOneCombinedTag::StageOneCombinedTag( edm::Ptr<DiPhotonCandidate> dipho, DiPhotonMVAResult mvares, VBFMVAResult vbf_mvaRes, VHhadMVAResult vhHad_mvaRes, VHhadACDNNResult vhHadAC_dnnRes, GluGluHMVAResult ggh_mvaRes ) :
    StageOneCombinedTag::StageOneCombinedTag( dipho, mvares )
{
    vbfmva_result_ = vbf_mvaRes;
    vhhadmva_result_ = vhHad_mvaRes;
    vhhadacdnn_result_ = vhHadAC_dnnRes;
    gghmva_result_ = ggh_mvaRes;
}

const VBFMVAResult StageOneCombinedTag::VBFMVA() const
{
    return vbfmva_result_;

}

const VHhadMVAResult StageOneCombinedTag::VHhadMVA() const
{
    return vhhadmva_result_;
}

const VHhadACDNNResult StageOneCombinedTag::VHhadACDNN() const
{
    return vhhadacdnn_result_;
}

const GluGluHMVAResult StageOneCombinedTag::GluGluHMVA() const
{
    return gghmva_result_;
}


// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

