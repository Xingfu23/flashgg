import FWCore.ParameterSet.Config as cms
from flashgg.MicroAOD.flashggJets_cfi import flashggBTag, flashggDeepCSV, flashggDeepJet, UnpackedJetCollectionVInputTag, maxJetCollections

bDiscriminator74X = cms.vdouble(0.605,0.890)
bDiscriminator76X = cms.vdouble(0.460,0.800,0.935)
bDiscriminator80XReReco = cms.vdouble(0.5426,0.8484,0.9535)
bDiscriminator94X= cms.vdouble(0.1522,0.4941,0.8001)

flashggUntagged = cms.EDProducer("FlashggUntaggedTagProducer",
#                                 DiPhotonTag=cms.InputTag('flashggDiPhotons'),
                                 DiPhotonTag    = cms.InputTag('flashggPreselectedDiPhotons'),
                                 SystLabel      = cms.string(""),
                                 MVAResultTag   = cms.InputTag('flashggDiPhotonMVA'),
                                 Boundaries     = cms.vdouble(-0.405,0.204,0.564,0.864), #,1.000),
                                 RequireScaledPtCuts = cms.bool(True)
)

flashggSigmaMoMpToMTag = cms.EDProducer("FlashggSigmaMpTTagPreCleanerProducer",
                                        #                                 DiPhotonTag=cms.InputTag('flashggDiPhotons'),
                                        DiPhotonTag    = cms.InputTag('flashggPreselectedDiPhotons'),
                                        SystLabel      = cms.string(""),
                                        MVAResultTag   = cms.InputTag('flashggDiPhotonMVA'),
                                        GenParticleTag = cms.InputTag( "flashggPrunedGenParticles" ),
                                        BoundariesSigmaMoM  = cms.vdouble(0.,0.00841,0.0116,0.0298), #boundaries have to be provided including lowest and highest
                                        #                                 BoundariespToM      = cms.vdouble(0.,1.02,1.83,10.0), #,1.000), #boundaries have to be provided including lowest and highest
                                        RequireScaledPtCuts = cms.bool(True),
                                        CompositeCandidateTags = cms.PSet()
                                        )

import TTHDNNPreprocessingConstructor, os
ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme_path = os.path.expandvars("$CMSSW_BASE/src/flashgg/Taggers/data/metadata_Hadronic_ttHHadronic_ttH_vs_ttGG_legacy_v1.1_27Nov2020.json")
ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme = TTHDNNPreprocessingConstructor.construct(ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme_path, "Hadronic")

ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme_path = os.path.expandvars("$CMSSW_BASE/src/flashgg/Taggers/data/metadata_Hadronic_ttHHadronic_ttH_vs_dipho_legacy_v1.1_27Nov2020.json")
ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme = TTHDNNPreprocessingConstructor.construct(ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme_path, "Hadronic")

flashggTTHHadronicTag = cms.EDProducer("FlashggTTHHadronicTagProducer",
                                       DiPhotonName=cms.string('flashggPreselectedDiPhotons'),
                                       DiPhotonSuffixes = cms.vstring(''), # nominal and systematic variations
                                       JetsName=cms.string('flashggUnpackedJets'),
                                       SystematicsJetsName=cms.string('flashggJetSystematics'),
                                       JetsCollSize = cms.uint32(maxJetCollections),
                                       JetsSuffixes = cms.vstring(''), # nominal and systematic variations
                                       MetName=cms.string('flashggMets'),
                                       SystematicsMetName=cms.string('flashggMetSystematics'),
                                       MetSuffixes = cms.vstring(''), # nominal and systematic variations
                                       ModifySystematicsWorkflow = cms.bool(False),
                                       UseLargeMVAs = cms.bool(False), # by default, don't use large MVAs that can cause memory crashes
                                       MVAResultName=cms.string('flashggDiPhotonMVA'),
                                       DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                       SystLabel=cms.string(""),
                                       MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                       ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                       MuonTag=cms.InputTag('flashggSelectedMuons'),
                                       VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                       METTag=cms.InputTag('flashggMets'),
                                       rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
#                                       tthMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_tth_hadronic_2017Data_35vars_v0.weights.xml"),
                                       tthMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_tth_hadronic_2017Data_30vars_v0.weights.xml"),
                                       topTaggerXMLfile = cms.FileInPath("flashgg/Taggers/data/resTop_xgb_csv_order_deepCTag.xml"),
                                       tthVsDiphoDNNfile = cms.FileInPath("flashgg/Taggers/data/Hadronic_ttHHadronic_ttH_vs_dipho_legacy_v1.1_27Nov2020_weights.pb"),
                                       tthVsDiphoDNN_global_mean = ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme["global_mean"],
                                       tthVsDiphoDNN_global_stddev = ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme["global_stddev"],
                                       tthVsDiphoDNN_object_mean = ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme["object_mean"],
                                       tthVsDiphoDNN_object_stddev = ttHHadronic_ttH_vs_dipho_DNN_preprocess_scheme["object_stddev"],
                                       tthVsttGGDNNfile = cms.FileInPath("flashgg/Taggers/data/Hadronic_ttHHadronic_ttH_vs_ttGG_legacy_v1.1_27Nov2020_weights.pb"),
                                       tthVsttGGDNN_global_mean = ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme["global_mean"],
                                       tthVsttGGDNN_global_stddev = ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme["global_stddev"],
                                       tthVsttGGDNN_object_mean = ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme["object_mean"],
                                       tthVsttGGDNN_object_stddev = ttHHadronic_ttH_vs_ttGG_DNN_preprocess_scheme["object_stddev"],
                                       tthMVA_RunII_weightfile = cms.FileInPath("flashgg/Taggers/data/Hadronic_legacy_v1.1_27Nov2020_bdt.xml"),
                                       MVAMethod = cms.string("BDT"),     
                                       RECOfilters = cms.InputTag('TriggerResults::RECO'),
                                       leadPhoOverMassThreshold = cms.double(0.33),
                                       leadPhoPtThreshold = cms.double(20),  
                                       leadPhoUseVariableThreshold =  cms.bool(True),
                                       subleadPhoOverMassThreshold = cms.double(0.25),
                                       subleadPhoPtThreshold = cms.double(20),
                                       subleadPhoUseVariableThreshold =  cms.bool(True),
                                       MVAThreshold = cms.double(-1.0),
#                                       PhoMVAThreshold = cms.double(-0.7), ### EDM loose g+jets
                                       PhoMVAThreshold = cms.double(-1.0), ### EDM loose g+jets
                                       inputTagJets= UnpackedJetCollectionVInputTag, 
                                       jetPtThreshold = cms.double(25.),
                                       jetEtaThreshold = cms.double(2.4),
#                                       bDiscriminator = bDiscriminator80XReReco, #bDiscriminator76X
#                                       bTag = cms.string(flashggBTag),
                                       bDiscriminator = bDiscriminator94X,
                                       bTag = cms.string(flashggDeepJet),
                                       jetsNumberThreshold = cms.int32(5),
                                       bjetsNumberThreshold = cms.int32(1),
                                       bjetsLooseNumberThreshold = cms.int32(0),
                                       useTTHHadronicMVA =  cms.bool(True),
                                       applyMETfilters  =  cms.bool(False),
                                       leadPhoOverMassTTHHMVAThreshold = cms.double(0.33),
                                       MVATTHHMVAThreshold = cms.double(-1.),
                                       jetsNumberTTHHMVAThreshold = cms.int32(3),
                                       bjetsNumberTTHHMVAThreshold = cms.int32(0),
                                       bjetsLooseNumberTTHHMVAThreshold = cms.int32(1),  
                                       secondMaxBTagTTHHMVAThreshold = cms.double(0.0),  
                                       #Boundaries = cms.vdouble(0.9675, 0.9937, 0.9971, 0.9991), 
                                       Boundaries = cms.vdouble(0.986025, 0.9948537, 0.9983046, 0.9990729),
                                       Boundaries_pt1 = cms.vdouble(0.9705986,0.99322987,0.994506),
                                       Boundaries_pt2 = cms.vdouble(0.9788471,0.9954657,0.99611914),
                                       Boundaries_pt3 = cms.vdouble(0.96859723,0.9872348,0.99252445,0.9961255),
                                       Boundaries_pt4 = cms.vdouble(0.9824722,0.99405247,0.99727315),
                                       Boundaries_pt5 = cms.vdouble(0.972507,0.99530387),
                                       STXSPtBoundaries_pt1 = cms.vdouble(0,60),
                                       STXSPtBoundaries_pt2 = cms.vdouble(60,120),
                                       STXSPtBoundaries_pt3 = cms.vdouble(120,200),
                                       STXSPtBoundaries_pt4 = cms.vdouble(200,300),
                                       STXSPtBoundaries_pt5 = cms.vdouble(300,13001),
                                       dRJetPhoLeadCut =  cms.double(0.4),
                                       dRJetPhoSubleadCut = cms.double(0.4),                          
                                       MuonEtaCut = cms.double(2.4),
                                       MuonPtCut = cms.double(5),
                                       MuonIsoCut = cms.double(0.25),
                                       MuonPhotonDrCut = cms.double(0.),
                                       EleEtaCuts = cms.vdouble(1.4442,1.566,2.5),
                                       ElePtCut = cms.double(10),
                                       ElePhotonDrCut = cms.double(0.),
                                       ElePhotonZMassCut = cms.double(5),
                                       DeltaRTrkEle = cms.double(0.),
                                       debug = cms.bool(False)
                                       )



from flashgg.Taggers.flashggTagSorter_cfi import HTXSInputTags
flashggVBFTag = cms.EDProducer("FlashggVBFTagProducer",
                               DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                               SystLabel=cms.string(""),
                               MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                               VBFDiPhoDiJetMVAResultTag=cms.InputTag('flashggVBFDiPhoDiJetMVA'),
                               GluGluHMVAResultTag=cms.InputTag('flashggGluGluHMVA'),
                               VHhadMVATag=cms.InputTag('flashggVHhadMVA'),
                               VBFMVAResultTag=cms.InputTag('flashggVBFMVA'),
                               GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                               HTXSTags = HTXSInputTags,
                               GenJetTag = cms.InputTag("slimmedGenJets"),
                               Boundaries_pbsm=cms.vdouble(0.97),
                               Boundaries_pbkg=cms.vdouble(0.05),
                               Boundaries_d0m=cms.vdouble(0.6),
                               #  for the moment we have two categories VBF-0 and VBF-1: to be changed when the diphoton MVA is ready 
                               #Boundaries=cms.vdouble(0.5819, 0.9449)
                               #Boundaries=cms.vdouble(0.62, 0.94),
                               #Boundaries=cms.vdouble(0.634, 0.919),

                               # optimisation of Moriond 17 : 3 VBF categories
                               # These boundaries are recalculated after fixing
                               # the problem with the shape of the BDT output
#                               Boundaries=cms.vdouble(0.215,  0.532,  0.865),
#                               Boundaries=cms.vdouble(0.66633615,  0.89334188,  0.95919197),
#                               Boundaries=cms.vdouble(0.55889473,  0.9087378 ,  0.97044208),
                               #Boundaries = cms.vdouble( 0.553, 0.902, 0.957 ),
                               SetArbitraryNonGoldMC = cms.bool(False),
                               DropNonGoldData = cms.bool(False),
                               RequireVBFPreselection = cms.bool(True),
                               VBFPreselLeadPtMin = cms.double(40.),
                               VBFPreselSubleadPtMin = cms.double(30.),
                               VBFPreselPhoIDMVAMin = cms.double(0.5),
                               GetQCDWeights = cms.bool(False)
                               )


flashggVHEtTag = cms.EDProducer("FlashggVHEtTagProducer",
                                RECOfilters = cms.InputTag('TriggerResults::RECO'),
                                PATfilters = cms.InputTag('TriggerResults::PAT'),
                                FLASHfilters = cms.InputTag('TriggerResults::FLASHggMicroAOD'),
                                DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                SystLabel=cms.string(""),
                                GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                METTag=cms.InputTag('flashggMets'),   
                                useVertex0only=cms.bool(True),
                                leadPhoOverMassThreshold = cms.double(0.375),
                                subleadPhoOverMassThreshold = cms.double(0.25),
                                metPtThreshold = cms.double(70),
                                dPhiDiphotonMetThreshold = cms.double(2.1),
                                diphoMVAThreshold= cms.double(-1.0),
                                phoIdMVAThreshold= cms.double(-0.9)
                                #Boundaries=cms.vdouble(0.21,0.6,0.81)
)

ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme_path = os.path.expandvars("$CMSSW_BASE/src/flashgg/Taggers/data/metadata_Leptonic_ttHLeptonic_ttH_vs_ttGG_legacy_v1.1_27Nov2020.json")
ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme = TTHDNNPreprocessingConstructor.construct(ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme_path, "Leptonic")

ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme_path = os.path.expandvars("$CMSSW_BASE/src/flashgg/Taggers/data/metadata_Leptonic_ttHLeptonic_ttH_vs_tH_legacy_v1.0_ttH_vs_tH_26Nov2020.json")
ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme = TTHDNNPreprocessingConstructor.construct(ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme_path, "Leptonic", True)

flashggTTHLeptonicTag = cms.EDProducer("FlashggTTHLeptonicTagProducer",
                                       DiPhotonName=cms.string('flashggPreselectedDiPhotons'),
                                       DiPhotonSuffixes = cms.vstring(''), # nominal and systematic variations
                                       JetsName=cms.string('flashggUnpackedJets'),
                                       SystematicsJetsName=cms.string('flashggJetSystematics'),
                                       JetsCollSize = cms.uint32(maxJetCollections),
                                       JetsSuffixes = cms.vstring(''), # nominal and systematic variations
                                       MetName=cms.string('flashggMets'),
                                       SystematicsMetName=cms.string('flashggMetSystematics'),
                                       MetSuffixes = cms.vstring(''), # nominal and systematic variations
                                       ModifySystematicsWorkflow = cms.bool(False),
                                       UseLargeMVAs = cms.bool(False), # by default, don't use large MVAs that can cause memory crashes
                                       MVAResultName=cms.string('flashggDiPhotonMVA'),
                                       DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                       SystLabel=cms.string(""),
                                       MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                       inputTagJets= UnpackedJetCollectionVInputTag,
                                       ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                       MuonTag=cms.InputTag('flashggSelectedMuons'),
                                       MetTag=cms.InputTag( 'flashggMets' ), 
                                       VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                       GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                       rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
                                       MVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_BDT_training_v2.json.weights.xml"),
                                       topTaggerXMLfile = cms.FileInPath("flashgg/Taggers/data/resTop_xgb_csv_order_deepCTag.xml"),
                                       tthVsttGGDNNfile = cms.FileInPath("flashgg/Taggers/data/Leptonic_ttHLeptonic_ttH_vs_ttGG_legacy_v1.1_27Nov2020_weights.pb"),
                                       tthVsttGGDNN_global_mean = ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme["global_mean"],
                                       tthVsttGGDNN_global_stddev = ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme["global_stddev"],
                                       tthVsttGGDNN_object_mean = ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme["object_mean"],
                                       tthVsttGGDNN_object_stddev = ttHLeptonic_ttH_vs_ttGG_DNN_preprocess_scheme["object_stddev"],
                                       tthVstHDNNfile = cms.FileInPath("flashgg/Taggers/data/Leptonic_ttHLeptonic_ttH_vs_tH_legacy_v1.0_ttH_vs_tH_26Nov2020_weights.pb"),
                                       tthVstHDNN_global_mean = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["global_mean"],
                                       tthVstHDNN_global_stddev = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["global_stddev"],
                                       tthVstHDNN_object_mean = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["object_mean"],
                                       tthVstHDNN_object_stddev = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["object_stddev"],
                                       tthMVA_RunII_weightfile = cms.FileInPath("flashgg/Taggers/data/Leptonic_legacy_v1.1_27Nov2020_bdt.xml"),
                                       leadPhoOverMassThreshold = cms.double(0.33),
                                       subleadPhoOverMassThreshold = cms.double(0.25),
                                       #tthVstHThreshold = cms.double(0.13699667), # 97% ttH eff
                                       tthVstHThreshold = cms.double(0.15), #ad hoc

                                       #MVAThreshold = cms.vdouble(0.8435, 0.9346, 0.9625, 0.9890),
                                       MVAThreshold = cms.vdouble(0.8997816, 0.95635754, 0.9725133, 0.9870608),
                                       MVAThreshold_pt1 = cms.vdouble(0.75, 0.9259551, 0.9577374),
                                       MVAThreshold_pt2 = cms.vdouble(0.9, 0.9533934, 0.96331936),
                                       MVAThreshold_pt3 = cms.vdouble(0.9199876, 0.94682026,),
                                       MVAThreshold_pt4 = cms.vdouble(0.9089704),
                                       MVAThreshold_pt5 = cms.vdouble(0.6),
                                       STXSPtBoundaries_pt1 = cms.vdouble(0,60),
                                       STXSPtBoundaries_pt2 = cms.vdouble(60,120),
                                       STXSPtBoundaries_pt3 = cms.vdouble(120,200),
                                       STXSPtBoundaries_pt4 = cms.vdouble(200,300),
                                       STXSPtBoundaries_pt5 = cms.vdouble(200,13001),
                                       PhoMVAThreshold = cms.double(-0.7), 
                                       jetsNumberThreshold = cms.double(1.),
                                       bjetsNumberThreshold = cms.double(0.),
                                       jetPtThreshold = cms.double(25.), 
                                       jetEtaThreshold= cms.double(5.0),
                                       deltaRJetLeadPhoThreshold = cms.double(0.4),
                                       deltaRJetSubLeadPhoThreshold = cms.double(0.4),
                                       deltaRJetLepton = cms.double(0.4),
                                       leadingJetPtThreshold = cms.double(0),
                                       bDiscriminator = bDiscriminator94X, #bDiscriminator76X,
                                       bTag = cms.string(flashggDeepJet),
                                       MinNLep = cms.int32(1),
                                       MaxNLep = cms.int32(10),
                                       MuonEtaCut = cms.double(2.4),
                                       MuonPtCut = cms.double(5),
                                       MuonIsoCut = cms.double(0.25),
                                       MuonPhotonDrCut = cms.double(0.2),
                                       EleEtaCuts = cms.vdouble(1.4442,1.566,2.5),
                                       ElePtCut = cms.double(10),
                                       ElePhotonDrCut = cms.double(0.2),
                                       ElePhotonZMassCut = cms.double(5),
                                       LeptonsZMassCut = cms.double(5),
                                       DiLeptonJetThreshold = cms.double(0),
                                       DiLeptonbJetThreshold = cms.double(1),
                                       DiLeptonMVAThreshold = cms.double(-999),
                                       DeltaRTrkEle = cms.double(0.35),
                                       UseCutBasedDiphoId = cms.bool(False),
                                       SplitDiLeptEv = cms.bool(True),
                                       debug = cms.bool(False),
                                       CutBasedDiphoId = cms.vdouble(0.4,0.3,0.0,-0.5,2.0,2.5)    # pT/m lead, pT/m sublead, leadIdMVA, subleadIdMVA, DeltaEta, DeltaPhi
)

flashggTHQLeptonicTag = cms.EDProducer("FlashggTHQLeptonicTagProducer",
                                       DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                       SystLabel=cms.string(""),
                                       MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                       inputTagJets= UnpackedJetCollectionVInputTag,
                                       ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                       MuonTag=cms.InputTag('flashggSelectedMuons'),
                                       METTag=cms.InputTag('flashggMets'),
                                       VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                       GenParticleTag=cms.InputTag('flashggPrunedGenParticles'),
                                       rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
                                       #MVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_BDT_training_v2.json.weights.xml"),
                                       MVAMethod = cms.string("BDT"),
                                       GenJetTag = cms.InputTag("slimmedGenJets"),
                                       muonEtaThreshold = cms.double(2.4),
                                       muonPtThreshold = cms.double(5.0),
                                       electronPtThreshold = cms.double(10.0),                        
                                       electronEtaThresholds = cms.vdouble(1.4442,1.566,2.4),
                                       leadPhoOverMassThreshold = cms.double(0.33),
                                       subleadPhoOverMassThreshold = cms.double(0.25),
                                       MVAThreshold = cms.double(0.3),
                                       Boundaries = cms.vdouble(-0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45 ),
                                       deltaRLepPhoThreshold = cms.double(0.4),
                                       deltaRJetLepThreshold = cms.double(0.4),
                                       jetsNumberThreshold = cms.double(1.),
                                       bjetsNumberThreshold = cms.double(1.),
                                       jetPtThreshold = cms.double(25.),
                                       jetEtaThreshold = cms.double(5),
                                       deltaRJetLeadPhoThreshold = cms.double(0.4),
                                       deltaRJetSubLeadPhoThreshold = cms.double(0.4),
                                       bDiscriminator = bDiscriminator94X, #bDiscriminator76X,
                                       bTag = cms.string(flashggDeepCSV),
                                       muPFIsoSumRelThreshold = cms.double(0.25),
                                       PhoMVAThreshold = cms.double(-0.7),
                                       DeltaRTrkElec = cms.double(0.35),
                                       deltaRPhoElectronThreshold = cms.double(0.4),
                                       DeltaRbjetfwdjet=cms.double(0.4),
                                       DeltaRtHchainfwdjet=cms.double(0.4),
#                                       thqleptonicMVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVA_THQLeptonicTag_tHq_Vs_ttH_BDT.weights.xml"),
#                                      thqCatweightfile_ForNonPeakingBkg = cms.FileInPath("flashgg/Taggers/data/TMVA_THQLeptonicTag_tHq_Vs_NonPeakingBkg_BDT_16.weights.xml"),
				       tthVstHDNNfile = cms.FileInPath("flashgg/Taggers/data/Leptonic_ttHLeptonic_ttH_vs_tH_legacy_v1.0_ttH_vs_tH_26Nov2020_weights.pb"),
                                       tthVstHDNN_global_mean = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["global_mean"],
                                       tthVstHDNN_global_stddev = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["global_stddev"],
                                       tthVstHDNN_object_mean = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["object_mean"],
                                       tthVstHDNN_object_stddev = ttHLeptonic_ttH_vs_tH_DNN_preprocess_scheme["object_stddev"],
				       debug = cms.bool(False),
				       use_MVAs = cms.bool(True),
				       use_tthVstHDNN = cms.bool(True),
				       use_tthVstHBDT = cms.bool(False),
				       MVAThreshold_tHqVsttHDNN = cms.double(0.25),
)



flashggTTHDiLeptonTag = cms.EDProducer("FlashggTTHDiLeptonTagProducer",
                                        DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                       SystLabel=cms.string(""),
                                       MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                       inputTagJets= UnpackedJetCollectionVInputTag,
                                       ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                       MuonTag=cms.InputTag('flashggSelectedMuons'),
				       MetTag=cms.InputTag( 'flashggMets' ), 
                                       VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
				       rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
                                       MVAweightfile = cms.FileInPath("flashgg/Taggers/data/TMVAClassification_BDT_training_v2.json.weights.xml"),
                                       leadPhoOverMassThreshold = cms.double(0.33),
                                       subleadPhoOverMassThreshold = cms.double(0.25),
                                       MVAThreshold = cms.double(0.5),
                                       PhoMVAThreshold = cms.double(-0.2), 
                                       jetsNumberThreshold = cms.double(1.),
                                       bjetsNumberThreshold = cms.double(1.),
                                       jetPtThreshold = cms.double(25.), 
                                       jetEtaThreshold= cms.double(2.4),
                                       deltaRJetLeadPhoThreshold = cms.double(0.4),
                                       deltaRJetSubLeadPhoThreshold = cms.double(0.4),
				       deltaRJetLepton = cms.double(0.4),
				       leadingJetPtThreshold = cms.double(0),
                                       bDiscriminator = bDiscriminator94X, #bDiscriminator76X,
                                       bTag = cms.string(flashggDeepCSV),
				       MuonEtaCut = cms.double(2.4),
				       MuonPtCut = cms.double(5),
				       MuonIsoCut = cms.double(0.25),
				       MuonPhotonDrCut = cms.double(0.2),
				       EleEtaCuts = cms.vdouble(1.4442,1.566,2.5),
				       ElePtCut = cms.double(10),
				       ElePhotonDrCut = cms.double(0.2),
				       ElePhotonZMassCut = cms.double(5),
				       DeltaRTrkEle = cms.double(0.35),
				       LeptonsZMassCut = cms.double(5),
				       UseCutBasedDiphoId = cms.bool(False),
				       debug = cms.bool(False),
				       CutBasedDiphoId = cms.vdouble(0.4,0.3,0.0,-0.5,2.0,2.5),    # pT/m lead, pT/m sublead, leadIdMVA, subleadIdMVA, DeltaEta, DeltaPhi

)


flashggVHLooseTag = cms.EDProducer("FlashggVHLooseTagProducer",
                                   DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                   SystLabel=cms.string(""),
                                   RECOfilters = cms.InputTag('TriggerResults::RECO'),
                                   PATfilters = cms.InputTag('TriggerResults::PAT'),
                                   FLASHfilters = cms.InputTag('TriggerResults::FLASHggMicroAOD'),
                                   #JetTag=cms.InputTag('flashggSelectedJets'),
                                   inputTagJets= UnpackedJetCollectionVInputTag,
                                   ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                   MuonTag=cms.InputTag('flashggSelectedMuons'),
                                   VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.InputTag('flashggMets'),   
                                   useVertex0only=cms.bool(True),
                                   GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
				                   rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
                                   leptonPtThreshold = cms.double(20),
                                   muonEtaThreshold = cms.double(2.4),
                                   leadPhoOverMassThreshold = cms.double(0.375),
                                   subleadPhoOverMassThreshold = cms.double(0.25),
                                   MVAThreshold = cms.double(0.187), #taken from cat2 boundary
                                   deltaRMuonPhoThreshold = cms.double(0.5),
                                   jetsNumberThreshold = cms.double(3.),
                                   jetPtThreshold = cms.double(20.),
                                   jetEtaThreshold= cms.double(2.4),
                                   deltaRPhoLeadJet = cms.double(0.5),
                                   deltaRPhoSubLeadJet = cms.double(0.5),
                                   muPFIsoSumRelThreshold = cms.double(0.25), 
                                   deltaRJetMuonThreshold = cms.double(0.5),
                                   PuIDCutoffThreshold = cms.double(0.8),
                                   PhoMVAThreshold = cms.double(-0.9),
                                   METThreshold = cms.double(45.),
                                   ElectronPtThreshold = cms.double(20.),
                                   DeltaRTrkElec = cms.double(.4),
                                   TransverseImpactParam = cms.double(0.02),
                                   LongitudinalImpactParam = cms.double(0.2),
                                   deltaRPhoElectronThreshold = cms.double(1.),
                                   deltaMassElectronZThreshold = cms.double(10.),
                                   electronEtaThresholds=cms.vdouble(1.4442,1.566,2.5),
                                   nonTrigMVAThresholds = cms.vdouble(0.913286,0.805013,0.358969),
                                   nonTrigMVAEtaCuts = cms.vdouble(0.8,1.479,2.5),
                                   electronIsoThreshold = cms.double(0.15),
                                   electronNumOfHitsThreshold = cms.double(1),
                                   useElectronMVARecipe = cms.bool(False),
                                   useElectronLooseID = cms.bool(True)
				    )

flashggVHTightTag = cms.EDProducer("FlashggVHTightTagProducer",
                                   DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                   SystLabel=cms.string(""),
                                   RECOfilters = cms.InputTag('TriggerResults::RECO'),
                                   PATfilters = cms.InputTag('TriggerResults::PAT'),
                                   FLASHfilters = cms.InputTag('TriggerResults::FLASHggMicroAOD'),
                                   #JetTag=cms.InputTag('flashggSelectedJets'),
                                   inputTagJets= UnpackedJetCollectionVInputTag,
                                   ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                   MuonTag=cms.InputTag('flashggSelectedMuons'),
                                   VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.InputTag('flashggMets'),   
                                   useVertex0only=cms.bool(True),
                                   GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
				                   rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
                                   leptonPtThreshold = cms.double(20),
                                   muonEtaThreshold = cms.double(2.4),
                                   leadPhoOverMassThreshold = cms.double(0.375),
                                   subleadPhoOverMassThreshold = cms.double(0.25),
                                   MVAThreshold = cms.double(0.187), #taken from cat 3 boundary
                                   deltaRMuonPhoThreshold = cms.double(1),
                                   jetsNumberThreshold = cms.double(3.),
                                   jetPtThreshold = cms.double(20.),
                                   jetEtaThreshold= cms.double(2.4),
                                   muPFIsoSumRelThreshold = cms.double(0.25), 
                                   PuIDCutoffThreshold = cms.double(0.8),
                                   PhoMVAThreshold = cms.double(-0.9),
                                   METThreshold = cms.double(45.),
                                   deltaRJetMuonThreshold = cms.double(0.5),
                                   deltaRJetElectronThreshold = cms.double(0.5),
                                   invMassLepLowThreshold = cms.double(70.),
                                   invMassLepHighThreshold = cms.double(110.),
                                   numberOfLowPtMuonsThreshold = cms.double(2.),
                                   numberOfHighPtMuonsThreshold = cms.double(1.),
                                   leptonLowPtThreshold = cms.double(10.),
                                   deltaRLowPtMuonPhoThreshold = cms.double(0.5),
                                   deltaRPhoLeadJet = cms.double(0.5),
                                   deltaRPhoSubLeadJet = cms.double(0.5),
                                   ElectronPtThreshold = cms.double(20.),
                                   DeltaRTrkElec = cms.double(0.4),
                                   TransverseImpactParam = cms.double(0.02),
                                   LongitudinalImpactParam = cms.double(0.2),
                                   deltaRPhoElectronThreshold = cms.double(1.),
                                   deltaMassElectronZThreshold = cms.double(10.),
                                   electronEtaThresholds=cms.vdouble(1.4442,1.566,2.5),
                                   nonTrigMVAThresholds = cms.vdouble(0.913286,0.805013,0.358969),
                                   nonTrigMVAEtaCuts = cms.vdouble(0.8,1.479,2.5),
                                   electronIsoThreshold = cms.double(0.15),
                                   electronNumOfHitsThreshold = cms.double(1),
                                   useElectronMVARecipe = cms.bool(False),
                                   useElectronLooseID = cms.bool(True)
)

flashggVHMetTag = cms.EDProducer("FlashggVHMetTagProducer",
                                    DiPhotonTag                 = cms.InputTag('flashggPreselectedDiPhotons'),
                                    SystLabel                   = cms.string(""),
                                    ElectronTag                 = cms.InputTag('flashggSelectedElectrons'),
                                    MuonTag                     = cms.InputTag('flashggSelectedMuons'),
                                    inputTagJets                = UnpackedJetCollectionVInputTag,
                                    METTag                      = cms.InputTag('flashggMets'),
                                    VertexTag                   = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                    rhoTag                      = cms.InputTag('fixedGridRhoFastjetAll'),
                                    MVAResultTag                = cms.InputTag('flashggDiPhotonMVA'),
                                    GenParticleTag              = cms.InputTag('flashggPrunedGenParticles' ),
                                    VHMetMVAweightfile          = cms.FileInPath("flashgg/Taggers/data/TMVA_VHMetTag_BDT_ULv1.weights.xml"),
                                    Boundaries                  = cms.vdouble(0.64612,0.766,0.85024),
                                    AC_types                    = cms.vstring("fa3"),
                                    AC_STXS_boundaries_fa3      = cms.vdouble(0.6192,0.798176),
                                    AC_boundaries_fa3_bin0      = cms.vdouble(0.86),          
                                    AC_boundaries_fa3_bin1      = cms.vdouble(0.92),
                                    # AC_STXS_boundaries_fa3      = cms.vdouble(-1,-1), # for Z->ee Validation
                                    # AC_boundaries_fa3_bin0      = cms.vdouble(-1),    # for Z->ee Validation         
                                    # AC_boundaries_fa3_bin1      = cms.vdouble(-1),    # for Z->ee Validation
                                    AC_STXS_boundaries_fa2      = cms.vdouble(0.6192,0.76288), 
                                    AC_boundaries_fa2_bin0      = cms.vdouble(0.80),          
                                    AC_boundaries_fa2_bin1      = cms.vdouble(0.88),          
                                    AC_STXS_boundaries_fL1      = cms.vdouble(0.6192,0.798176),
                                    AC_boundaries_fL1_bin0      = cms.vdouble(0.80),          
                                    AC_boundaries_fL1_bin1      = cms.vdouble(0.94),          
                                    leadPhoOverMassThreshold    = cms.double(0.333333),
                                    subleadPhoOverMassThreshold = cms.double(0.2),
                                    phoIdMVAThreshold           = cms.double(-0.7),
                                    diphoMVAThreshold           = cms.double(-1.),
                                    metPtThreshold              = cms.double(50.),
                                    dPhiDiphotonMetThreshold    = cms.double(2.0),
                                    jetPtThreshold              = cms.double(20.),
                                    jetEtaThreshold             = cms.double(2.4),
                                    deltaRJetPhoThreshold       = cms.double(0.4),
                                    vhmetanom_fa3_bdt_xmlfile   = cms.FileInPath('flashgg/Taggers/data/VH_Anomalous/VHMet/v2/VHMET_VHiggs0MToGG_EraALL_model.xml'),  
                                    vhmetanom_fa2_bdt_xmlfile   = cms.FileInPath('flashgg/Taggers/data/VH_Anomalous/VHMet/v2/VHMET_VHiggs0PHToGG_EraALL_model.xml'),
                                    vhmetanom_fL1_bdt_xmlfile   = cms.FileInPath('flashgg/Taggers/data/VH_Anomalous/VHMet/v2/VHMET_VHiggs0L1ToGG_EraALL_model.xml')
)

flashggZHLeptonicTag = cms.EDProducer("FlashggZHLeptonicTagProducer",
                                    DiPhotonTag                 = cms.InputTag('flashggPreselectedDiPhotons'),
                                    SystLabel                   = cms.string(""),
                                    ElectronTag                 = cms.InputTag('flashggSelectedElectrons'),
                                    MuonTag                     = cms.InputTag('flashggSelectedMuons'),
                                    inputTagJets                = UnpackedJetCollectionVInputTag,
                                    METTag                      = cms.InputTag('flashggMets'),
                                    VertexTag                   = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                    rhoTag                      = cms.InputTag('fixedGridRhoFastjetAll'),
                                    MVAResultTag                = cms.InputTag('flashggDiPhotonMVA'),
                                    GenParticleTag              = cms.InputTag( "flashggPrunedGenParticles" ),
                                    ZHMVAweightfile             = cms.FileInPath("flashgg/Taggers/data/TMVA_ZHLeptonicTag_BDT_ULv1.weights.xml"),
                                    Boundaries                  = cms.vdouble(0.2307, 0.342),
                                    leadPhoOverMassThreshold    = cms.double(0.),
                                    subleadPhoOverMassThreshold = cms.double(0.),
                                    MVAThreshold                = cms.double(-1.0),
                                    PhoMVAThreshold             = cms.double(-0.9),
                                    electronPtThreshold         = cms.double(10),
                                    invMassLepLowThreshold      = cms.double(60.),
                                    invMassLepHighThreshold     = cms.double(120.),
                                    electronEtaThresholds       = cms.vdouble(1.4442,1.566,2.5),
                                    DeltaRTrkElec               = cms.double(0.2),
                                    deltaRPhoElectronThreshold  = cms.double(0.2),
                                    deltaMassElectronZThreshold = cms.double(-1.),
                                    muonPtThreshold             = cms.double(10),
                                    muonEtaThreshold            = cms.double(2.4),
                                    deltaRMuonPhoThreshold      = cms.double(0.2),
                                    muPFIsoSumRelThreshold      = cms.double(0.25),
                                    jetPtThreshold              = cms.double(20),
                                    jetEtaThreshold             = cms.double(2.4),
                                    deltaRJetPhoThreshold       = cms.double(0.4),
                                    deltaRJetLepThreshold       = cms.double(0.4),

                                    ZHiggs0MToGG_weights        = cms.FileInPath("flashgg/Taggers/data/VH_Anomalous/2023_02_23_BDTv3/ZHiggs0MToGG_EraALL_model.xml"),  
                                    ZHiggs0PHToGG_weights       = cms.FileInPath("flashgg/Taggers/data/VH_Anomalous/2023_02_23_BDTv3/ZHiggs0PHToGG_EraALL_model.xml"),   
                                    ZHiggs0L1ToGG_weights       = cms.FileInPath("flashgg/Taggers/data/VH_Anomalous/2023_02_23_BDTv3/ZHiggs0L1ToGG_EraALL_model.xml"),

                                    acBoundaries                = cms.vdouble(
                                                                    #Tag 0
                                                                    1.0,0.229, #STXSBDT
                                                                    1.0,-0.68, #ACBDT
                                                                    #Tag 1
                                                                    0.229,-0.135, #STXSBDT
                                                                    1.0,-0.16, #ACBDT
                                                                    # #Tag 0
                                                                    # 1.0,-1.0, #STXSBDT
                                                                    # 1.0,-1.0, #ACBDT
                                                                    # #Tag 1
                                                                    # 0.229,-1.0, #STXSBDT
                                                                    # 1.0,-1.0, #ACBDT
                                                                ),

)

flashggWHLeptonicTag = cms.EDProducer("FlashggWHLeptonicTagProducer",
                                    DiPhotonTag                 = cms.InputTag('flashggPreselectedDiPhotons'),
                                    SystLabel                   = cms.string(""),
                                    ElectronTag                 = cms.InputTag('flashggSelectedElectrons'),
                                    MuonTag                     = cms.InputTag('flashggSelectedMuons'),
                                    inputTagJets                = UnpackedJetCollectionVInputTag,
                                    METTag                      = cms.InputTag('flashggMets'),
                                    VertexTag                   = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                    rhoTag                      = cms.InputTag('fixedGridRhoFastjetAll'),
                                    MVAResultTag                = cms.InputTag('flashggDiPhotonMVA'),
                                    GenParticleTag              = cms.InputTag( "flashggPrunedGenParticles" ),
                                    WHMVAweightfile             = cms.FileInPath("flashgg/Taggers/data/TMVA_WHLeptonicTag_BDT_ULv1.weights.xml"),
                                    Boundaries_GT150            = cms.vdouble(0.454),
                                    Boundaries_75_150           = cms.vdouble(0.27914, 0.482),
                                    Boundaries_0_75             = cms.vdouble(0.18438, 0.402),
                                    leadPhoOverMassThreshold    = cms.double(0.),
                                    subleadPhoOverMassThreshold = cms.double(0.),
                                    PhoMVAThreshold             = cms.double(-0.4),
                                    MVAThreshold                = cms.double(-1.),
                                    electronPtThreshold         = cms.double(15),
                                    electronEtaThresholds       = cms.vdouble(1.4442, 1.566, 2.5),
                                    deltaRPhoElectronThreshold  = cms.double(0.2),
                                    DeltaRTrkElec               = cms.double(0.2),
                                    deltaMassElectronZThreshold = cms.double(5.),
                                    muonPtThreshold             = cms.double(15),
                                    muonEtaThreshold            = cms.double(2.4),
                                    muPFIsoSumRelThreshold      = cms.double(0.25),
                                    deltaRMuonPhoThreshold      = cms.double(0.2),
                                    jetsNumberThreshold         = cms.double(999),
                                    jetPtThreshold              = cms.double(20.),
                                    jetEtaThreshold             = cms.double(2.4),
                                    deltaRJetPhoThreshold       = cms.double(0.4),
                                    deltaRJetLepThreshold       = cms.double(0.4),
                                    METThreshold                = cms.double(0.),

                                    WHiggs0MToGG_weights        = cms.FileInPath("flashgg/Taggers/data/VH_Anomalous/2023_02_23_BDTv3/WHiggs0MToGG_EraALL_model.xml"),   
                                    WHiggs0PHToGG_weights       = cms.FileInPath("flashgg/Taggers/data/VH_Anomalous/2023_02_23_BDTv3/WHiggs0PHToGG_EraALL_model.xml"),    
                                    WHiggs0L1ToGG_weights       = cms.FileInPath("flashgg/Taggers/data/VH_Anomalous/2023_02_23_BDTv3/WHiggs0L1ToGG_EraALL_model.xml"),

                                    acBoundaries               = cms.vdouble(
                                        # Tag 0
                                        1.0,0.385, #STXSBDT
                                        1.0,0.79, #ACBDT
                                        #Tag 1
                                        1.0,0.38541667, #STXSBDT
                                        0.79,-0.68, #ACBDT
                                        #Tag 2                                                                               
                                        0.385,0.125, #STXSBDT
                                        1.0,0.89, #ACBDT
                                        #Tag 3
                                        0.385,0.125, #STXSBDT
                                        0.89,-0.68, #ACBDT
                                        # # Tag 0
                                        # 1.0,-1.0, #STXSBDT
                                        # 1.0,-1.0, #ACBDT
                                        # #Tag 1
                                        # 1.0,0.38541667, #STXSBDT
                                        # 0.79,-0.68, #ACBDT
                                        # #Tag 2                                                                               
                                        # 0.385,0.125, #STXSBDT
                                        # 1.0,0.89, #ACBDT
                                        # #Tag 3
                                        # 0.385,0.125, #STXSBDT
                                        # 0.89,-0.68, #ACBDT
                                        ),
                                    )

flashggVHLeptonicLooseTag = cms.EDProducer("FlashggVHLeptonicLooseTagProducer",
                                   DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                   SystLabel=cms.string(""),
                                   RECOfilters = cms.InputTag('TriggerResults::RECO'),
                                   PATfilters = cms.InputTag('TriggerResults::PAT'),
                                   FLASHfilters = cms.InputTag('TriggerResults::FLASHggMicroAOD'),
                                   inputTagJets= UnpackedJetCollectionVInputTag,
                                   ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                   MuonTag=cms.InputTag('flashggSelectedMuons'),
                                   VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.InputTag('flashggMets'),
                                   useVertex0only=cms.bool(False),
                                   GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                   rhoTag = cms.InputTag('fixedGridRhoFastjetAll'),
				   leptonPtThreshold = cms.double(20),
                                   muonEtaThreshold = cms.double(2.4),
                                   leadPhoOverMassThreshold = cms.double(0.375),
                                   subleadPhoOverMassThreshold = cms.double(0.25),
                                   MVAThreshold = cms.double(0.0),
                                   deltaRMuonPhoThreshold = cms.double(1),
                                   jetsNumberThreshold = cms.double(3.),
                                   jetPtThreshold = cms.double(20.),
                                   jetEtaThreshold= cms.double(2.4),
                                   muPFIsoSumRelThreshold = cms.double(0.25),
                                   PuIDCutoffThreshold = cms.double(0.8),
                                   PhoMVAThreshold = cms.double(-0.9),
                                   METThreshold = cms.double(45.),
                                   deltaRJetMuonThreshold = cms.double(0.4),
                                   deltaRJetElectronThreshold = cms.double(0.4),
                                   invMassLepLowThreshold = cms.double(70.),
                                   invMassLepHighThreshold = cms.double(110.),
                                   deltaRPhoLeadJet = cms.double(0.4),
                                   deltaRPhoSubLeadJet = cms.double(0.4),
                                   DeltaRTrkElec = cms.double(0.4),
                                   TransverseImpactParam = cms.double(0.02),
                                   LongitudinalImpactParam = cms.double(0.2),
                                   deltaRPhoElectronThreshold = cms.double(1.),
                                   deltaMassElectronZThreshold = cms.double(10.),
                                   electronEtaThresholds=cms.vdouble(1.4442,1.566,2.5),
                                   nonTrigMVAThresholds = cms.vdouble(0.913286,0.805013,0.358969),
                                   nonTrigMVAEtaCuts = cms.vdouble(0.8,1.479,2.5),
                                   electronIsoThreshold = cms.double(0.15),
                                   electronNumOfHitsThreshold = cms.double(1),
                                   useElectronMVARecipe = cms.bool(False),
                                   useElectronLooseID = cms.bool(True)
)



flashggVHHadronicTag = cms.EDProducer("FlashggVHHadronicTagProducer",
                                      DiPhotonTag = cms.InputTag('flashggPreselectedDiPhotons'),
                                      SystLabel=cms.string(""),
                                      MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                      #JetTag = cms.InputTag('flashggSelectedJets'),
                                      inputTagJets= UnpackedJetCollectionVInputTag,
                                      GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                      leadPhoOverMassThreshold = cms.double(0.5),
                                      subleadPhoOverMassThreshold = cms.double(0.25),
                                      diphoMVAThreshold = cms.double(0.6),
                                      jetsNumberThreshold = cms.double(2.),
                                      jetPtThreshold = cms.double(40.),
                                      jetEtaThreshold= cms.double(2.4),
                                      dRJetToPhoLThreshold = cms.double(0.4),
                                      dRJetToPhoSThreshold = cms.double(0.4),
                                      dijetMassLowThreshold = cms.double(60.),
                                      dijetMassHighThreshold = cms.double(120.),
                                      cosThetaStarThreshold = cms.double(0.5),
                                      phoIdMVAThreshold = cms.double(-0.9)
)

flashggVHHadronicACTag = cms.EDProducer("FlashggVHHadronicACTagProducer",
                                        DiPhotonTag = cms.InputTag('flashggPreselectedDiPhotons'),
                                        SystLabel=cms.string(""),
                                        MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                        VHhadACDNNResult=cms.InputTag('flashggVHhadACDNN'),
                                        #JetTag = cms.InputTag('flashggSelectedJets'),
                                        inputTagJets= UnpackedJetCollectionVInputTag,
                                        GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                        leadPhoOverMassThreshold = cms.double(1./3),
                                        subleadPhoOverMassThreshold = cms.double(0.25),
                                        diphoMVAThreshold = cms.double(0.6),
                                        jetsNumberThreshold = cms.double(2.),
                                        jetPtThreshold = cms.double(30.),
                                        jetEtaThreshold= cms.double(2.6),
                                        dRJetToPhoLThreshold = cms.double(0.4),
                                        dRJetToPhoSThreshold = cms.double(0.4),
                                        dijetMassLowThreshold = cms.double(0.),
                                        dijetMassHighThreshold = cms.double(250.),
                                        cosThetaStarThreshold = cms.double(-1.),
                                        maxPhoIdMVAThreshold = cms.double(0.0),
                                        minPhoIdMVAThreshold = cms.double(0.0),
                                        Categories_dnnbkg = cms.vdouble(0.082085, 0.252840, 0.535261, 0.065729, 1.0),
                                        Categories_dnnbsm = cms.vdouble(0.5625, 0.45, 0.2875, 0.889, 0.747)
)

# Tag is for jet studies only, not in default sequence
flashggZPlusJetTag = cms.EDProducer("FlashggZPlusJetTagProducer",
                                    DiPhotonTag    = cms.InputTag('flashggPreselectedDiPhotons'),
                                    SystLabel      = cms.string(""),
                                    MVAResultTag   = cms.InputTag('flashggDiPhotonMVA'),
                                    inputTagJets= UnpackedJetCollectionVInputTag,
                                    GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                    GenJetTag = cms.InputTag("slimmedGenJets")
                                    )


