import FWCore.ParameterSet.Config as cms

from flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag
from flashgg.Taggers.flashggVBFMVA_cff import pujidPtBin1_loose, pujidPtBin2_loose, pujidPtBin1_medium, pujidPtBin2_medium, pujidPtBin1_tight, pujidPtBin2_tight 

# legacy VHhad MVA
flashggVHhadACDNN = cms.EDProducer('FlashggVHhadACDNNProducer',
                                 DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                 #JetTag=cms.InputTag('flashggSelectedJets'),
                                 inputTagJets= UnpackedJetCollectionVInputTag,
                                 UsePuJetID  = cms.bool(False),
                                 UseJetID    = cms.bool(True),
                                 merge3rdJet = cms.bool(False),
                                 thirdJetDRCut = cms.double(1.8),
                                 JetIDLevel    = cms.string("Tight2017"),
                                 ## define the pujid working point 
                                 pujidWpPtBin1 = cms.vdouble(pujidPtBin1_tight), ## WP for 20 < pT < 30 
                                 pujidWpPtBin2 = cms.vdouble(pujidPtBin2_tight), ## WP for 30 < pT < 50
                                 rmsforwardCut = cms.double(3.0), # default was 0.03 , running on loose pujid
                                 MinDijetMinv  = cms.double(0.0),
                                 DrJetPhoton   = cms.double(0.4), # Keep the same value for now, should be set later to 0.4
                                 vhHadDNNweightfile = cms.FileInPath("flashgg/Taggers/data/vhHadAC_DNN.pb"),
                                 vhHadDNNInputVars = cms.vstring(
                                     "dipho_lead_ptoM", 
                                     "dipho_leadEta", 
                                     "dipho_leadIDMVA", 
                                     "dipho_sublead_ptoM", 
                                     "dipho_subleadEta",
                                     "dipho_subleadIDMVA", 
                                     "dipho_abs_dEta", 
                                     "dipho_abs_dPhi", 
                                     "dijet_leadPt", 
                                     "dijet_leadEta", 
                                     "dijet_leadPhi",
                                     "jet1_btag", 
                                     "dijet_subleadPt", 
                                     "dijet_subleadEta", 
                                     "dijet_subleadPhi", 
                                     "jet2_btag",
                                     "dijet_Mjj", 
                                     "dijet_abs_dEta", 
                                     "cos_thetastar",
                                     "dijet_minDRJetPho"
                                 ),
                                 vhHadDNNOutputClasses = cms.vstring(
                                     "DNNbkg",
                                     "DNNsm",
                                     "DNNbsm"
                                 ),
                                 vhHadDNNInputShift = cms.vdouble(
                                     3.3333361e-01, 
                                     -2.4999402e+00,  
                                     3.1545820e-05,  
                                     2.5000080e-01,
                                     -2.4999561e+00,  
                                     2.4640800e-05,  
                                     4.4107437e-06,  
                                     2.3841858e-07,
                                     3.0052135e+01, 
                                     -2.5999346e+00, 
                                     -3.1415610e+00,  
                                     1.0962687e-09,
                                     3.0000008e+01, 
                                     -2.5999997e+00, 
                                     -3.1415558e+00,  
                                     4.3596118e-04,
                                     1.5547302e+01,  
                                     8.8289380e-07, 
                                     -1.0000000e+00,  
                                     4.0009633e-01
                                 ),
                                 vhHadDNNInputScale = cms.vdouble(
                                     1.1902543e+01, 
                                     4.9999208e+00, 
                                     9.9858880e-01, 
                                     4.7079101e+00,
                                     4.9999199e+00, 
                                     9.9880183e-01, 
                                     2.6217351e+00, 
                                     3.1415904e+00,
                                     1.3495651e+03, 
                                     5.1998301e+00, 
                                     6.2831383e+00, 
                                     9.9999982e-01,
                                     3.8039117e+02, 
                                     5.1999993e+00, 
                                     6.2831349e+00, 
                                     9.9956357e-01,
                                     2.3445207e+02, 
                                     4.1364079e+00, 
                                     1.9999985e+00, 
                                     4.8827949e+00
                                 ),
)
