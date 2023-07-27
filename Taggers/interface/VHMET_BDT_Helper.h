#ifndef _VHMET_BDT_HELPER_
#define _VHMET_BDT_HELPER_

#include <fstream>
#include <string>

#include <TMath.h>
#include <TMatrixD.h>
#include <TVectorD.h>
#include <TVector3.h>
#include <TLorentzVector.h>
#include "TMVA/Reader.h"

namespace flashgg {

// structure InputVariables{{{
typedef struct{
    float pho1_eta;
    float pho2_eta;
    float pho1_phi;
    float pho2_phi;
    float pho1_ptoM;
    float pho2_ptoM;
    float dipho_cosphi;
    float dipho_deltaeta;
    float met;
    float met_phi;
    float met_sumEt;
    float dphi_pho1_met;
    float dphi_pho2_met;
    float pt_balance;
    float njet;
    float max_jet_pt;
    float min_dphi_jet_met;
} InputVariables;
//}}}

class VHMET_BDT_Helper {
public:
  VHMET_BDT_Helper(const string& mva_algo, const std::string& weight_file_name);
  virtual ~VHMET_BDT_Helper(){};
  InputVariables varList_;
  double evaluate(const std::string& tag, const InputVariables& varList);
  double convert_tmva_to_prob(double score);

  void print_details(InputVariables var);
  void print_details_cout(InputVariables var);

private:
  std::shared_ptr<TMVA::Reader> reader_ = nullptr;
};

// constructor{{{
VHMET_BDT_Helper::VHMET_BDT_Helper(const string& mva_algo, const std::string& weight_file_name)
{
  reader_ = std::make_shared<TMVA::Reader>( "!Color:!Silent" );

  reader_->AddVariable("pho1_eta"         , &varList_.pho1_eta         );
  reader_->AddVariable("pho2_eta"         , &varList_.pho2_eta         );
  reader_->AddVariable("pho1_phi"         , &varList_.pho1_phi         );
  reader_->AddVariable("pho2_phi"         , &varList_.pho2_phi         );
  reader_->AddVariable("pho1_ptoM"        , &varList_.pho1_ptoM        );
  reader_->AddVariable("pho2_ptoM"        , &varList_.pho2_ptoM        );
  reader_->AddVariable("dipho_cosphi"     , &varList_.dipho_cosphi     );
  reader_->AddVariable("dipho_deltaeta"   , &varList_.dipho_deltaeta   );
  reader_->AddVariable("met"              , &varList_.met              );
  reader_->AddVariable("met_phi"          , &varList_.met_phi          );
  reader_->AddVariable("met_sumEt"        , &varList_.met_sumEt        );
  reader_->AddVariable("dphi_pho1_met"    , &varList_.dphi_pho1_met    );
  reader_->AddVariable("dphi_pho2_met"    , &varList_.dphi_pho2_met    );
  reader_->AddVariable("pt_balance"       , &varList_.pt_balance       );
  reader_->AddVariable("njet"             , &varList_.njet             );
  reader_->AddVariable("max_jet_pt"       , &varList_.max_jet_pt       );
  reader_->AddVariable("min_dphi_jet_met" , &varList_.min_dphi_jet_met );

  reader_->BookMVA(mva_algo.c_str(), weight_file_name);
}
//}}}

double VHMET_BDT_Helper::evaluate(const string& mva_algo, const InputVariables& varList) {
  memcpy(&varList_, &varList, sizeof(varList)); // use move syntax here                                                                                                      
  return reader_->EvaluateMVA(mva_algo.c_str());
}

double VHMET_BDT_Helper::convert_tmva_to_prob(double score)
{
  // this function will convert BDT output scores from [-1, 1] to [0, 1]

  // Undo TMVA transformation
  double raw_score = -0.5 * log( (2 / (score + 1)) - 1);

  // Apply logistic (sigmoid) transformation
  double prob = 1 / (1 + exp(-raw_score));

  return prob;
}

// print details{{{
inline
void VHMET_BDT_Helper::print_details(InputVariables var)
{
    printf("%s: %.10f , " , "pho1_eta"         , var.pho1_eta         );
    printf("%s: %.10f , " , "pho2_eta"         , var.pho2_eta         );
    printf("%s: %.10f , " , "pho1_phi"         , var.pho1_phi         );
    printf("%s: %.10f , " , "pho2_phi"         , var.pho2_phi         );
    printf("%s: %.10f , " , "pho1_ptoM"        , var.pho1_ptoM        );
    printf("%s: %.10f , " , "pho2_ptoM"        , var.pho2_ptoM        );   
    printf("%s: %.10f , " , "dipho_cosphi"     , var.dipho_cosphi     );
    printf("%s: %.10f , " , "dipho_deltaeta"   , var.dipho_deltaeta   );
    printf("%s: %.10f , " , "met"              , var.met              );
    printf("%s: %.10f , " , "met_phi"          , var.met_phi          );
    printf("%s: %.10f , " , "met_sumEt"        , var.met_sumEt        );
    printf("%s: %.10f , " , "dphi_pho1_met"    , var.dphi_pho1_met    );
    printf("%s: %.10f , " , "dphi_pho2_met"    , var.dphi_pho2_met    );
    printf("%s: %.10f , " , "pt_balance"       , var.pt_balance       );
    printf("%s: %.10f , " , "njet"             , var.njet             );
    printf("%s: %.10f , " , "max_jet_pt"       , var.max_jet_pt       );
    printf("%s: %.10f , " , "min_dphi_jet_met" , var.min_dphi_jet_met );
};
//}}}
// print details cout{{{
inline
void VHMET_BDT_Helper::print_details_cout(InputVariables var)
{
    std::cout << "pho1_eta: "         << var.pho1_eta         << ", ";
    std::cout << "pho2_eta: "         << var.pho2_eta         << ", ";
    std::cout << "pho1_phi: "         << var.pho1_phi         << ", ";
    std::cout << "pho2_phi: "         << var.pho2_phi         << ", ";
    std::cout << "pho1_ptoM: "        << var.pho1_ptoM        << ", ";
    std::cout << "pho2_ptoM: "        << var.pho2_ptoM        << ", ";
    std::cout << "dipho_cosphi: "     << var.dipho_cosphi     << ", ";
    std::cout << "dipho_deltaeta: "   << var.dipho_deltaeta   << ", ";
    std::cout << "met: "              << var.met              << ", ";
    std::cout << "met_phi: "          << var.met_phi          << ", ";
    std::cout << "met_sumEt: "        << var.met_sumEt        << ", ";
    std::cout << "dphi_pho1_met: "    << var.dphi_pho1_met    << ", ";
    std::cout << "dphi_pho2_met: "    << var.dphi_pho2_met    << ", ";
    std::cout << "pt_balance: "       << var.pt_balance       << ", ";
    std::cout << "njet: "             << var.njet             << ", ";
    std::cout << "max_jet_pt: "       << var.max_jet_pt       << ", ";
    std::cout << "min_dphi_jet_met: " << var.min_dphi_jet_met << ", ";
};
//}}}

} // end of namespace

#endif // _VHMET_BDT_HELPER_
