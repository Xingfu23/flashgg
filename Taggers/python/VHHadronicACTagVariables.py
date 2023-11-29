stxs_truth_variables=[
    "HTXSstage0bin := tagTruth().HTXSstage0bin()",
    "HTXSstage1bin := tagTruth().HTXSstage1bin()",
    "HTXSstage1p1bin := tagTruth().HTXSstage1p1bin()",
    "HTXSstage1p1binFine := tagTruth().HTXSstage1p1binFine()",
    "HTXSstage1p2bin := tagTruth().HTXSstage1p2bin()",
    "HTXSstage1p2binFine := tagTruth().HTXSstage1p2binFine()",
    "HTXSnjets := tagTruth().HTXSnjets()",
    "HTXSpTH := tagTruth().HTXSpTH()",
    "HTXSpTV := tagTruth().HTXSpTV()"
    ]

dipho_variables=[
    "dipho_sumpt            := diPhoton.sumPt",
    "dipho_cosphi           := abs(cos(diPhoton.leadingPhoton.phi - diPhoton.subLeadingPhoton.phi))",
    "dipho_mass             := diPhoton.mass",
    "dipho_leadPt           := diPhoton.leadingPhoton.pt",
    "dipho_leadEt           := diPhoton.leadingPhoton.et",
    "dipho_leadEta          := diPhoton.leadingPhoton.eta",
    "dipho_leadPhi          := diPhoton.leadingPhoton.phi",
    "dipho_lead_sieie       := diPhoton.leadingPhoton.sigmaIetaIeta",
    "dipho_lead_hoe         := diPhoton.leadingPhoton.hadronicOverEm",
    "dipho_lead_sigmaEoE    := diPhoton.leadingPhoton.sigEOverE",
    "dipho_lead_ptoM        := diPhoton.leadingPhoton.pt/diPhoton.mass",
    "dipho_leadR9           := diPhoton.leadingPhoton.full5x5_r9",
    "dipho_subleadPt        := diPhoton.subLeadingPhoton.pt",
    "dipho_subleadEt        := diPhoton.subLeadingPhoton.et",
    "dipho_subleadEta       := diPhoton.subLeadingPhoton.eta",
    "dipho_subleadPhi       := diPhoton.subLeadingPhoton.phi",
    "dipho_sublead_sieie    := diPhoton.subLeadingPhoton.sigmaIetaIeta",
    "dipho_sublead_hoe      := diPhoton.subLeadingPhoton.hadronicOverEm",
    "dipho_sublead_sigmaEoE := diPhoton.subLeadingPhoton.sigEOverE",
    "dipho_sublead_ptoM     := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
    "dipho_subleadR9        := diPhoton.subLeadingPhoton.full5x5_r9",
    "dipho_leadIDMVA        := diPhoton.leadingView.phoIdMvaWrtChosenVtx",
    "dipho_subleadIDMVA     := diPhoton.subLeadingView.phoIdMvaWrtChosenVtx",
    "dipho_lead_elveto      := diPhoton.leadingPhoton.passElectronVeto",
    "dipho_sublead_elveto   := diPhoton.subLeadingPhoton.passElectronVeto",
    "result                 := diPhotonMVA.result",
    "dipho_PToM             := diPhoton.pt/diPhoton.mass",
    "sigmarv                := diPhotonMVA.sigmarv",
    "sigmarvDecorr          := diPhotonMVA.decorrSigmarv",
    "sigmawv                := diPhotonMVA.sigmawv",
    "CosPhi                 := diPhotonMVA.CosPhi",
    "vtxprob                := diPhotonMVA.vtxprob",
    "pt                     := diPhoton.pt",
    "leadSCeta              := diPhoton.leadingPhoton.superCluster.eta",
    "subleadSCeta           := diPhoton.subLeadingPhoton.superCluster.eta",
    "dipho_lead_genmatch    := ?(diPhoton().leadingPhoton.hasGenMatchType)? diPhoton().leadingPhoton.genMatchType : -999",
    "dipho_sublead_genmatch := ?(diPhoton().subLeadingPhoton.hasGenMatchType)? diPhoton().subLeadingPhoton.genMatchType : -999"
    ]

dijet_variables=[
    "n_rec_jets             :=  VHhadACDNN.n_rec_jets       ",
    "dijet_abs_dEta         :=  abs(VHhadACDNN.dijet_leadEta - VHhadACDNN.dijet_subleadEta)",
    "dijet_leadEta          :=  VHhadACDNN.dijet_leadEta    ",
    "dijet_subleadEta       :=  VHhadACDNN.dijet_subleadEta ",
    "dijet_leadPhi          :=  leadingJet.phi              ",
    "dijet_subleadPhi       :=  subLeadingJet.phi           ",
    "dijet_leady            :=  VHhadACDNN.dijet_leady      ",
    "dijet_subleady         :=  VHhadACDNN.dijet_subleady   ",
    "dijet_leadPt           :=  VHhadACDNN.dijet_LeadJPt    ",
    "dijet_subleadPt        :=  VHhadACDNN.dijet_SubJPt     ",
    "dijet_Zep              :=  VHhadACDNN.dijet_Zep        ",
    "dijet_Mjj              :=  VHhadACDNN.dijet_Mjj        ",
    "dipho_PToM_vbfmva      :=  VHhadACDNN.dipho_PToM       ",
    "leadPho_PToM           :=  VHhadACDNN.leadPho_PToM     ",
    "sublPho_PToM           :=  VHhadACDNN.sublPho_PToM     ",
    "dijet_dipho_dphi_trunc :=  VHhadACDNN.dijet_dphi_trunc ",
    "dijet_dipho_pt         :=  VHhadACDNN.dijet_dipho_pt   ",
    "dijet_dphi             :=  abs(deltaPhi(VHhadACDNN.leadJet.phi, VHhadACDNN.subleadJet.phi))",
    "dijet_dipho_dphi       :=  VHhadACDNN.dijet_dipho_dphi ",
    "dijet_dPhi_trunc       :=  VHhadACDNN.dijet_dphi_trunc ",
    "cos_dijet_dipho_dphi   :=  cos(VHhadACDNN.dijet_dipho_dphi)",
    "dijet_minDRJetPho      :=  VHhadACDNN.dijet_minDRJetPho",
    "cos_thetastar          :=  VHhadACDNN.cosThetaStar",
    #"has3Jet                :=  hasValidVBFTriJet",
    #"dijet_mva              :=  VBFMVA.VBFMVAValue",
    #"dijet_mva_prob_VBF     :=  VBFMVA.vbfMvaResult_prob_VBF",
    #"dijet_mva_prob_ggH     :=  VBFMVA.vbfMvaResult_prob_ggH",
    #"dijet_mva_prob_bkg     :=  VBFMVA.vbfMvaResult_prob_bkg",
    #"dipho_dijet_MVA        :=  VBFDiPhoDiJetMVA.VBFDiPhoDiJetMVAValue()",
    "dipho_mva              :=  diPhotonMVA.mvaValue()",
    # new variables
    "jet1_pt             := leadingJet.pt",
    "jet2_pt             := subLeadingJet.pt",
    #"jet3_pt             := subSubLeadingJet.pt",
    #"jet4_pt             := fourthJet.pt",
    "jet1_eta            := leadingJet.eta",
    "jet2_eta            := subLeadingJet.eta",
    #"jet3_eta            := subSubLeadingJet.eta",
    #"jet4_eta            := fourthJet.eta",
    "Mjj := sqrt((leadingJet.energy+subLeadingJet.energy)^2-(leadingJet.px+subLeadingJet.px)^2-(leadingJet.py+subLeadingJet.py)^2-(leadingJet.pz+subLeadingJet.pz)^2)",
    #"jet1_rawPt          := leading_rawPt",
    #"jet2_rawPt          := subLeading_rawPt",
    #"jet1_HFHadronEnergyFraction := leading_HFHadronEnergyFraction",
    #"jet1_HFEMEnergyFraction := leading_HFEMEnergyFraction",
    #"jet1_HFHadronEnergy := leading_HFHadronEnergy",
    #"jet1_HFEMEnergy := leading_HFEMEnergy",
    #"jet1_HFHadronMultiplicity := leading_HFHadronMultiplicity",
    #"jet1_HFEMMultiplicity := leading_HFEMMultiplicity",
    #"jet2_HFHadronEnergyFraction := subleading_HFHadronEnergyFraction",
    #"jet2_HFEMEnergyFraction := subleading_HFEMEnergyFraction",
    #"jet2_HFHadronEnergy := subleading_HFHadronEnergy",
    #"jet2_HFEMEnergy := subleading_HFEMEnergy",
    #"jet2_HFHadronMultiplicity := subleading_HFHadronMultiplicity",
    #"jet2_HFEMMultiplicity := subleading_HFEMMultiplicity",
    "dijet_nj := VHhadACDNN.n_rec_jets",
    #"dipho_dijet_ptHjj := ptHjj",
    # Quark-Gluon-Likelihood
    #"jet1_qgtag := leading_QGL()",
    #"jet2_qgtag := subLeading_QGL()",
    #"jet3_qgtag := subSubLeading_QGL()",
    #"jet4_qgtag := fourth_QGL()",
    # BTag
    "jet1_btag := leadingJet.bDiscriminator('pfDeepCSVJetTags:probb') + leadingJet.bDiscriminator('pfDeepCSVJetTags:probbb')",
    "jet2_btag := subLeadingJet.bDiscriminator('pfDeepCSVJetTags:probb') + subLeadingJet.bDiscriminator('pfDeepCSVJetTags:probbb')",
    #"jet3_btag := subSubLeading_BTag()",
    #"jet4_btag := fourth_BTag()",

]

truth_variables=[
    "J1J2_mjj            := tagTruth().mjj_J1J2_FggJet()",
    "J1J3_mjj            := tagTruth().mjj_J1J3_FggJet()",
    "J2J3_mjj            := tagTruth().mjj_J2J3_FggJet()",
    "Mjjj                := tagTruth().mjjj_FggJet()",
    "J1J2_dEta           := tagTruth().dEta_J1J2_FggJet()",
    "J1J3_dEta           := tagTruth().dEta_J1J3_FggJet()",
    "J2J3_dEta           := tagTruth().dEta_J2J3_FggJet()",
    "J1J2_Zep            := tagTruth().zepjj_J1J2_FggJet()",
    "J1J3_Zep            := tagTruth().zepjj_J1J3_FggJet()",
    "J2J3_Zep            := tagTruth().zepjj_J2J3_FggJet()",
    "J1J2J3_Zep          := tagTruth().zepjjj_FggJet()",

    "J1J2_dipho_dPhi     := tagTruth().dPhijj_J1J2_FggJet()",
    "J1J3_dipho_dPhi     := tagTruth().dPhijj_J1J3_FggJet()",
    "J2J3_dipho_dPhi     := tagTruth().dPhijj_J2J3_FggJet()",

    "J1J2_dipho_dPhi_Gen     := tagTruth().dPhijj_J1J2_GenJet()",
    
    "J1J2J3_dipho_dPhi   := tagTruth().dPhijjj_FggJet()",
    
    "J1J2_dR             := tagTruth().dR_J1J2_FggJet()",
    "J1J3_dR             := tagTruth().dR_J1J3_FggJet()",
    "J2J3_dR             := tagTruth().dR_J2J3_FggJet()",
    
    "dEta_J1_J2J3        := tagTruth().dEta_J1J2J3_FggJet()",
    "dEta_J2_J3J1        := tagTruth().dEta_J2J3J1_FggJet()",
    "dEta_J3_J1J2        := tagTruth().dEta_J3J1J2_FggJet()",

    "dEta_dJ1_J2J3       := tagTruth().dEta_dJ1_J2J3_FggJet()",
    "dEta_dJ2_J3J1       := tagTruth().dEta_dJ2_J3J1_FggJet()",
    "dEta_dJ3_J1J2       := tagTruth().dEta_dJ3_J1J2_FggJet()",

    "dMjj_d12_13plus23   := tagTruth().mjj_d12_13plus23_FggJet()",
    "dMjj_d12_13         := tagTruth().mjj_d12_13_FggJet()",
    "dMjj_d12_23         := tagTruth().mjj_d12_23_FggJet()",
    "dMjj_d13_23         := tagTruth().mjj_d13_23_FggJet()",

    "dR_dipho_dijet12    := tagTruth().dR_DP_12_FggJet()",
    "dR_dipho_dijet13    := tagTruth().dR_DP_13_FggJet()",
    "dR_dipho_dijet23    := tagTruth().dR_DP_23_FggJet()",

    "dR_Photon1_J1       := tagTruth().dR_Ph1_1_FggJet()",
    "dR_Photon1_J2       := tagTruth().dR_Ph1_2_FggJet()",
    "dR_Photon1_J3       := tagTruth().dR_Ph1_3_FggJet()",
    "dR_Photon2_J1       := tagTruth().dR_Ph2_1_FggJet()",
    "dR_Photon2_J2       := tagTruth().dR_Ph2_2_FggJet()",
    "dR_Photon2_J3       := tagTruth().dR_Ph2_3_FggJet()",
    
    "dR_dipho_trijet     := tagTruth().dR_DP_123_FggJet()",

    "misPt_dPhi_3J       := tagTruth().missingP4_dPhi_jjj_FggJet()",
    "misPt_dPhi_2J       := tagTruth().missingP4_dPhi_jj_FggJet()",
    "misPt_mag_3J        := tagTruth().missingP4_Pt_jjj_FggJet()",
    "misPt_mag_2J        := tagTruth().missingP4_Pt_jj_FggJet()",

    "misPt_dPhi_d3J2J    := tagTruth().missingP4_dPhi_d3J2J_FggJet()",
    "misPt_mag_d3J2J     := tagTruth().missingP4_Pt_d3J2J_FggJet()",

    "dPhi_J1_J2          := tagTruth().dPhi_12_FggJet()",
    "dPhi_J1_J3          := tagTruth().dPhi_13_FggJet()",
    "dPhi_J2_J3          := tagTruth().dPhi_23_FggJet()",

    "dPhi_max_jets       := tagTruth().dPhi_max_FggJet()",
    "dPhi_min_jets       := tagTruth().dPhi_min_FggJet()",

    "momentum4Volume     := tagTruth().simplex_volume_DP_12_FggJet()",
    
    "dR_min_J12J23       := tagTruth().dR_min_J13J23_FggJet()",

    "dRToNearestPartonJ1 := tagTruth().dR_partonMatchingToJ1()",
    "dRToNearestPartonJ2 := tagTruth().dR_partonMatchingToJ2()",
    "dRToNearestPartonJ3 := tagTruth().dR_partonMatchingToJ3()",
    
    "numberOfMatches     := tagTruth().numberOfMatchesAfterDRCut(0.5)",
    
    # tag truth information
    "genZ                                 := tagTruth().genPV().z", # try that !!
    "pt_genJetMatchingToJ1                := tagTruth().pt_genJetMatchingToJ1",
    "pt_genJetMatchingToJ2                := tagTruth().pt_genJetMatchingToJ2",
    "pt_genJetMatchingToJ3                := tagTruth().pt_genJetMatchingToJ3",
    "eta_genJetMatchingToJ1               := tagTruth().eta_genJetMatchingToJ1",
    "eta_genJetMatchingToJ2               := tagTruth().eta_genJetMatchingToJ2",
    "eta_genJetMatchingToJ3               := tagTruth().eta_genJetMatchingToJ3",
    "hasClosestGenJetToLeadingJet         := tagTruth().hasClosestGenJetToLeadingJet",
    "hasClosestGenJetToSubLeadingJet      := tagTruth().hasClosestGenJetToSubLeadingJet",
    "hasClosestParticleToLeadingJet       := tagTruth().hasClosestParticleToLeadingJet",
    "hasClosestParticleToSubLeadingJet    := tagTruth().hasClosestParticleToSubLeadingJet",
    "hasClosestParticleToLeadingPhoton    := tagTruth().hasClosestParticleToLeadingPhoton",
    "hasClosestParticleToSubLeadingPhoton := tagTruth().hasClosestParticleToSubLeadingPhoton"
    
    ]