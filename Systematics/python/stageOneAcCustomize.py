import FWCore.ParameterSet.Config as cms

class StageOneAcCustomize():
    """
    Customizaton class for STXS stage 1 analysis
    """
    
    def __init__(self, process, customize, metaConditions):
        self.process = process
        self.customize = customize
        self.metaConditions = metaConditions
        self.modifyForttH = True
        self.tagList = [
            ["LOGICERROR",0], ["NOTAG",0], 
            ["RECO_0J_PTH_0_10_Tag0",0], ["RECO_0J_PTH_0_10_Tag1",0], ["RECO_0J_PTH_0_10_Tag2",0],
            ["RECO_0J_PTH_GT10_Tag0",0], ["RECO_0J_PTH_GT10_Tag1",0],["RECO_0J_PTH_GT10_Tag2",0],
            ["RECO_1J_PTH_0_60_Tag0",0], ["RECO_1J_PTH_0_60_Tag1",0], ["RECO_1J_PTH_0_60_Tag2",0],
            ["RECO_1J_PTH_60_120_Tag0",0], ["RECO_1J_PTH_60_120_Tag1",0], ["RECO_1J_PTH_60_120_Tag2",0],
            ["RECO_1J_PTH_120_200_Tag0",0], ["RECO_1J_PTH_120_200_Tag1",0],["RECO_1J_PTH_120_200_Tag2",0],
            ["RECO_GE2J_PTH_0_60_Tag0",0], ["RECO_GE2J_PTH_0_60_Tag1",0], ["RECO_GE2J_PTH_0_60_Tag2",0],
            ["RECO_GE2J_PTH_60_120_Tag0",0], ["RECO_GE2J_PTH_60_120_Tag1",0], ["RECO_GE2J_PTH_60_120_Tag2",0],
            ["RECO_GE2J_PTH_120_200_Tag0",0], ["RECO_GE2J_PTH_120_200_Tag1",0], ["RECO_GE2J_PTH_120_200_Tag2",0],
            ["RECO_PTH_200_300_Tag0",0], ["RECO_PTH_200_300_Tag1",0],  ["RECO_PTH_300_450_Tag0",0], ["RECO_PTH_300_450_Tag1",0],
            ["RECO_PTH_450_650_Tag0",0], ["RECO_PTH_GT650_Tag0",0],
            ["RECO_VBFTOPO_ACVHHADSM_Tag0",0], ["RECO_VBFTOPO_ACVHHADSM_Tag1",0], ["RECO_VBFTOPO_ACVHHADSM_Tag2",0], 
            ["RECO_VBFTOPO_ACVHHADBSM_Tag0",0], ["RECO_VBFTOPO_ACVHHADBSM_Tag1",0],
            ["RECO_VBFTOPO_ACGGH_Tag0",0], ["RECO_VBFTOPO_ACGGH_Tag1",0],
            ["RECO_VBFTOPO_ACVBFSM_Tag0",0], ["RECO_VBFTOPO_ACVBFBSM_Tag0",0], ["RECO_VBFTOPO_ACVBFBSM_Tag1",0],
            ["RECO_VBFLIKEGGH_Tag0",0], ["RECO_VBFLIKEGGH_Tag1",0], 
            ["RECO_TTH_HAD_PTH_0_60_Tag0",0], ["RECO_TTH_HAD_PTH_0_60_Tag1",0], ["RECO_TTH_HAD_PTH_0_60_Tag2",0],
            ["RECO_TTH_HAD_PTH_60_120_Tag0",0], ["RECO_TTH_HAD_PTH_60_120_Tag1",0], ["RECO_TTH_HAD_PTH_60_120_Tag2",0],
            ["RECO_TTH_HAD_PTH_120_200_Tag0",0], ["RECO_TTH_HAD_PTH_120_200_Tag1",0], ["RECO_TTH_HAD_PTH_120_200_Tag2",0], ["RECO_TTH_HAD_PTH_120_200_Tag3",0],
            ["RECO_TTH_HAD_PTH_200_300_Tag0",0], ["RECO_TTH_HAD_PTH_200_300_Tag1",0], ["RECO_TTH_HAD_PTH_200_300_Tag2",0],
            ["RECO_TTH_HAD_PTH_GT300_Tag0",0], ["RECO_TTH_HAD_PTH_GT300_Tag1",0],
            ["RECO_WH_LEP_Tag0",0], ["RECO_WH_LEP_Tag1",0], ["RECO_WH_LEP_Tag2",0], ["RECO_WH_LEP_Tag3",0],
            ["RECO_ZH_LEP_Tag0",0], ["RECO_ZH_LEP_Tag1",0],
            ["RECO_VH_MET_Tag0",0], ["RECO_VH_MET_Tag1",0], ["RECO_VH_MET_Tag2",0],["RECO_VH_MET_Tag3",0],
            ["RECO_TTH_LEP_PTH_0_60_Tag0",0], ["RECO_TTH_LEP_PTH_0_60_Tag1",0], ["RECO_TTH_LEP_PTH_0_60_Tag2",0],
            ["RECO_TTH_LEP_PTH_60_120_Tag0",0], ["RECO_TTH_LEP_PTH_60_120_Tag1",0], ["RECO_TTH_LEP_PTH_60_120_Tag2",0],
            ["RECO_TTH_LEP_PTH_120_200_Tag0",0], ["RECO_TTH_LEP_PTH_120_200_Tag1",0],
            ["RECO_TTH_LEP_PTH_200_300_Tag0",0],
            ["RECO_TTH_LEP_PTH_GT300_Tag0",0],
            ["RECO_THQ_LEP",0]
        ]
        if self.customize.processId == "Data": 
            self.tagList.pop(1) ## remove NoTag for data
            self.stageOneVariable = []
        else:
            self.stageOneVariable = ["stage1p2bin[57,-8.5,48.5] := tagTruth().HTXSstage1p2orderedBin"]
        self.tagPriorityRanges = cms.VPSet(
            cms.PSet(TagName = cms.InputTag('flashggTHQLeptonicTag')),
            cms.PSet(TagName = cms.InputTag('flashggTTHLeptonicTag')), 
            cms.PSet(TagName = cms.InputTag('flashggZHLeptonicTag')),
            cms.PSet(TagName = cms.InputTag('flashggWHLeptonicTag')),
            cms.PSet(TagName = cms.InputTag('flashggTTHHadronicTag')),   
            cms.PSet(TagName = cms.InputTag('flashggVHMetTag')),
            cms.PSet(TagName = cms.InputTag('flashggStageOneCombinedTag'))
        )
        self.customizeTagSequence()


    def variablesToDump(self,is_signal,fullvars=False):
        ws_variables = []
        ws_variables += self.stageOneVariable 
        ws_variables += [
            "CMS_hgg_mass[160,100,180]:=diPhoton().mass"
        ]
        if is_signal:
            ws_variables += [
                "dZ[40,-20.,20.]:=(tagTruth().genPV().z-diPhoton().vtx().z)",
                "NNLOPSweight[1,-999999.,999999.] := tagTruth().weight(\"NNLOPSweight\")",
                #"btagReshapeNorm_TTH_LEP[1,-999999.,999999.] := weight(\"btagReshapeNorm_TTH_LEP\")",
                #"btagReshapeNorm_TTH_HAD[1,-999999.,999999.] := weight(\"btagReshapeNorm_TTH_HAD\")",
                #"btagReshapeNorm_THQ_LEP[1,-999999.,999999.] := weight(\"btagReshapeNorm_THQ_LEP\")",
                "centralObjectWeight[1,-999999.,999999.] := centralWeight",
                "vbfNLOweight[1,-999999.,999999.] := weight(\"vbfNLOweight\")",
                "vhhadNLOweight[1,-999999.,999999.] := weight(\"vhhadNLOweight\")",
            ]

        import flashgg.Taggers.VBFTagVariables as var
        new_variables = [
            "dipho_pt             := diPhoton.pt",
            "dijet_pt             := VBFMVA.dijet_pt",
            "dijet_n_rec_jets     := GluGluHMVA.n_rec_jets",        
        ]
                
        VBF_mva_probs = [
            "dijet_vbfDNN_pbkg := VBFMVA.vbfDnnResult_prob_bkg()",
            "dijet_vbfDNN_psm  := VBFMVA.vbfDnnResult_prob_sm()",

            "dijet_vbfDNN_pbsm := VBFMVA.vbfDnnResult_prob_bsm()",
            "dijet_D0minus     := VBFMVA.D0minus()",
            "dijet_minDRJetPho    :=  VBFMVA.dijet_minDRJetPho",
            "dijet_centrality_gg  :=  VBFMVA.dijet_centrality_gg",
            "dijet_centrality_j3  :=  VBFMVA.dijet_centrality_j3",
            "dijet_centrality_g   :=  VBFMVA.dijet_centrality_g ",
            "cosThetaStar         :=  VHhadMVA.cosThetaStar",
        ]

        matching_photon = [
            "dijet_jet1_match := leadingJet_match",
            "dijet_jet2_match := subLeadingJet_match",
            "prompt_pho_1 := diPhoton.leadingPhoton.genMatchType()",
            "prompt_pho_2 := diPhoton.subLeadingPhoton.genMatchType()"
        ]
        
        VHhad_dnn_probs = [
            "dnnvh_bkg :=  VHhadACDNN.dnnvh_bkg",
            "dnnvh_sm  :=  VHhadACDNN.dnnvh_sm ",
            "dnnvh_bsm :=  VHhadACDNN.dnnvh_bsm",
        ]

        allNonSigVariables = var.dipho_variables + var.dijet_variables + matching_photon + VBF_mva_probs + VHhad_dnn_probs # + more_jet_vars 
        #ntup_variables = ws_variables + allNonSigVariables
        ntup_variables = ws_variables + allNonSigVariables if (is_signal and fullvars) else ws_variables

        if self.customize.dumpWorkspace:
            return ws_variables
        else:
            return ntup_variables

    def systematicVariables(self):
        systematicVariables = [] 
        systematicVariables += self.stageOneVariable 
        systematicVariables += [
            "CMS_hgg_mass[160,100,180]:=diPhoton().mass"
        ]
        return systematicVariables

    def noTagVariables(self):
        noTagVariables = []
        noTagVariables += self.stageOneVariable
        for direction in ["Up","Down"]:
            noTagVariables.append("THU_ggH_Mu%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Mu%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_Res%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Res%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_Mig01%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Mig01%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_Mig12%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Mig12%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_VBF2j%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_VBF2j%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_VBF3j%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_VBF3j%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_PT60%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_PT60%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_PT120%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_PT120%s01sigma\")" % (direction,direction))
            noTagVariables.append("THU_ggH_qmtop%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_qmtop%s01sigma\")" % (direction,direction))
        return noTagVariables


    def customizeTagSequence(self):
        self.process.load("flashgg.Taggers.flashggStageOneCombinedTag_cfi")

        ## remove unneeded tags
        self.process.flashggTagSequence.remove(self.process.flashggVBFDiPhoDiJetMVA)
        #self.process.flashggTagSequence.remove(self.process.flashggTHQLeptonicTag) ## now included in analysis
        self.process.flashggTagSequence.remove(self.process.flashggTTHDiLeptonTag)
        self.process.flashggTagSequence.remove(self.process.flashggTTHLeptonicTag) ## will be added back in later
        self.process.flashggTagSequence.remove(self.process.flashggTTHHadronicTag) ## will be added back in later
        #self.process.flashggTagSequence.remove(self.process.flashggVHMetTag)      ## now included in analysis
        #self.process.flashggTagSequence.remove(self.process.flashggZHLeptonicTag) ## now included in analysis
        #self.process.flashggTagSequence.remove(self.process.flashggWHLeptonicTag) ## now included in analysis
        self.process.flashggTagSequence.remove(self.process.flashggVHLeptonicLooseTag)
        #self.process.flashggTagSequence.remove(self.process.flashggVHHadronicTag)
        self.process.flashggTagSequence.remove(self.process.flashggVHHadronicACTag)
        self.process.flashggTagSequence.remove(self.process.flashggVBFTag)
        self.process.flashggTagSequence.replace(self.process.flashggUntagged,self.process.flashggStageOneCombinedTag)

        ## customize from meta conditions - category thresholds set here
        self.process.flashggStageOneCombinedTag.rawDiphoBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawDiphoBounds"] )
        self.process.flashggStageOneCombinedTag.rawDijetBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawDijetBounds"] )
        self.process.flashggStageOneCombinedTag.rawGghBounds   = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawGghBounds"] )
        self.process.flashggStageOneCombinedTag.rawVhHadBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawVhHadBounds"] )
        self.process.flashggStageOneCombinedTag.rawVbfpBSMBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawVbfpBSMBounds"] )
        self.process.flashggStageOneCombinedTag.rawVbfpBKGBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawVbfpBKGBounds"] )
        self.process.flashggStageOneCombinedTag.rawVbfpD0MBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawVbfpD0MBounds"] )
        self.process.flashggStageOneCombinedTag.rawVhhaddnnBKGBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawVhhaddnnBKGBounds"] )
        self.process.flashggStageOneCombinedTag.rawVhhaddnnBSMBounds = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["rawVhhaddnnBSMBounds"] )
        self.process.flashggStageOneCombinedTag.nloKfacVbfEdges = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["nloKfacVbfEdges"] )
        self.process.flashggStageOneCombinedTag.nloKfacVbfVals = cms.vdouble( self.metaConditions["stageOneCombinedTag"]["nloKfacVbfVals"] )
        self.process.flashggStageOneCombinedTag.nloKfacVHHadFile = cms.FileInPath( self.metaConditions["stageOneCombinedTag"]["nloKfacVHHadFile"] )

        ## set the pre-firing to be applied
        self.metaConditions["L1Prefiring"]["applyToCentral"] = True

        ## set tag priorities
        self.process.flashggTagSorter.TagPriorityRanges = self.tagPriorityRanges
        self.process.flashggTagSorter.isGluonFusion = cms.bool(bool(self.customize.processId.count("ggh")))
        self.process.flashggTagSorter.applyNNLOPSweight = cms.bool(self.customize.applyNNLOPSweight)
        self.process.flashggTagSorter.storeMELAweights = False

        ## set the tag merging
        self.process.flashggSystTagMerger = cms.EDProducer("TagMerger",src=cms.VInputTag("flashggTagSorter"))

    ## this adds in the ttH tags with their correct, modified systematics workflow
    def modifyWorkflowForttH(self, systlabels, phosystlabels, metsystlabels, jetsystlabels):
        # Set lists of systematics for each tag
        for tag in ["flashggTTHLeptonicTag", "flashggTTHHadronicTag"]:
            getattr(self.process, tag).DiPhotonSuffixes = cms.vstring(phosystlabels)
            getattr(self.process, tag).JetsSuffixes = cms.vstring(jetsystlabels)
            getattr(self.process, tag).MetSuffixes = cms.vstring(metsystlabels)
    
            getattr(self.process, tag).ModifySystematicsWorkflow = cms.bool(True)
            getattr(self.process, tag).UseLargeMVAs = cms.bool(True) # enable memory-intensive MVAs

        self.process.p.remove(self.process.flashggTagSorter)
        self.process.p.replace(self.process.flashggSystTagMerger, cms.Sequence(self.process.flashggTTHLeptonicTag + self.process.flashggTTHHadronicTag)*self.process.flashggTagSorter*self.process.flashggSystTagMerger)
    
        for systlabel in systlabels:
            if systlabel == "":
                continue
            self.process.p.remove(getattr(self.process, 'flashggTagSorter' + systlabel))
            self.process.p.replace(self.process.flashggSystTagMerger, getattr(self.process, 'flashggTagSorter' + systlabel) * self.process.flashggSystTagMerger)
            modifiedPriorityRanges = cms.VPSet(
	              cms.PSet(TagName = cms.InputTag('flashggTHQLeptonicTag'+systlabel)),
                cms.PSet(TagName = cms.InputTag('flashggTTHLeptonicTag', systlabel)),
                cms.PSet(TagName = cms.InputTag('flashggZHLeptonicTag'+systlabel)),
                cms.PSet(TagName = cms.InputTag('flashggWHLeptonicTag'+systlabel)),
                cms.PSet(TagName = cms.InputTag('flashggTTHHadronicTag', systlabel)),
                cms.PSet(TagName = cms.InputTag('flashggVHMetTag'+systlabel)),
                cms.PSet(TagName = cms.InputTag('flashggStageOneCombinedTag'+systlabel))
            )
            setattr(getattr(self.process, 'flashggTagSorter'+systlabel), 'TagPriorityRanges', modifiedPriorityRanges)
