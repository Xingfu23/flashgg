import os, json
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from flashggTriggerFilter import getMicroAODHLTFilter
from flashgg.MetaData.MetaConditionsReader import *

class MicroAODCustomize(object):

    def __init__(self,*args,**kwargs):

        super(MicroAODCustomize,self).__init__()

        self.options = VarParsing.VarParsing()

        self.options.register('conditionsJSON',
                               "", # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.string,          # string, int, or float
                              "conditionsJSON")
        self.options.register('fileNames',
                               "", # default value
                              VarParsing.VarParsing.multiplicity.list, # singleton or list
                              VarParsing.VarParsing.varType.string,          # string, int, or float
                              "fileNames")
        self.options.register('datasetName',
                              "", # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.string,          # string, int, or float
                              "datasetName")
        self.options.register('processType',
                              "", # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.string,          # string, int, or float
                              "processType")
        self.options.register('debug',
                              0, # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.int,          # string, int, or float
                              "debug")
        self.options.register('hlt',
                              0, # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.int,          # string, int, or float
                              "hlt")
        self.options.register('muMuGamma',
                              2, # 0 never, 1 always, 2 for DY and DoubleMuon
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.int,          # string, int, or float
                              "muMuGamma")
        self.options.register('timing',
                              0,
                              VarParsing.VarParsing.multiplicity.singleton,
                              VarParsing.VarParsing.varType.int,
                              'timing')
        self.options.register('puppi',
                              0,
                              VarParsing.VarParsing.multiplicity.singleton,
                              VarParsing.VarParsing.varType.int,
                              'puppi')
        self.options.register('bunchSpacing',
                              25,
                              VarParsing.VarParsing.multiplicity.singleton,
                              VarParsing.VarParsing.varType.int,
                              'bunchSpacing'
                              )
        self.options.register('addMicroAODHLTFilter',
                              True,
                              VarParsing.VarParsing.multiplicity.singleton,
                              VarParsing.VarParsing.varType.bool,
                              'addMicroAODHLTFilter'
                              )

    def __getattr__(self,name):
        ## did not manage to inherit from VarParsing, because of some issues in __init__
        ## this allows to use VarParsing methods on JobConfig
        if hasattr(self.options,name):
            return getattr(self.options,name)

        raise AttributeError

    def __call__(self,process):
        self.customize(process)
        self.userCustomize(process)

    # empty default definition for userCustomize
    def userCustomize(self,process):
        pass

    def parse(self):
        self.options.parseArguments()

    # process customization
    def customize(self,process):
        self.parse()

        self.metaConditions = MetaConditionsReader(self.conditionsJSON)

        self.customizePhotons(process)
        self.customizeDiPhotons(process)

        if self.puppi == 0:
            self.customizePFCHS(process)
            self.customizeRemovePuppi(process)
        elif self.puppi == 1:
            self.customizePuppi(process)
            self.customizeRemovePFCHS(process)
        else: # e.g. 2                                                                                                                               
            self.customizePFCHS(process)
            self.customizePuppi(process)
        if self.processType == "data":
            self.customizeData(process)
            if "Mu" in customize.datasetName:
                self.customizeDataMuons(process)
        elif "sig" in self.processType.lower():
            self.customizeSignal(process)
            if "tth" in customize.datasetName.lower():
                self.customizeTTH(process)
            elif "vh" in customize.datasetName.lower() or "wmh" in customize.datasetName.lower() or "wph" in customize.datasetName.lower() or "wh" in customize.datasetName.lower() or "zh" in customize.datasetName.lower():
                self.customizeVH(process)
            elif "ggh" in customize.datasetName.lower() or "glugluh" in customize.datasetName.lower():
                self.customizeGGH(process)
            elif "vbf" in customize.datasetName.lower():
                self.customizeVBF(process)
            elif "thq" in customize.datasetName.lower() or "thw" in customize.datasetName.lower():
                self.customizeTH(process)
            elif "hh" in customize.datasetName.lower():
                self.customizeHH(process)
            else:
                raise Exception,"processType=sig but datasetName does not contain recognized production mechanism - see MicroAODCustomize.py"
        if self.processType == "background" or self.processType == "bkg":
            self.customizeBackground(process)
            if "thq" in customize.datasetName.lower() or "thw" in customize.datasetName.lower():
                raise Exception,"TH samples should now be classfied as signal - see MicroAODCustomize.py"
        if self.debug == 1:
            self.customizeDebug(process)
        if self.hlt == 1:
            self.customizeHLT(process)
        if self.muMuGamma == 1:
            self.customizeMuMuGamma(process)
        elif self.muMuGamma == 2 and ("DY" in customize.datasetName or "DoubleMuon" in customize.datasetName):
            self.customizeMuMuGamma(process)
        if "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8" in customize.datasetName:
            self.customizePDFs(process)
        if self.processType == 'data':
            self.globalTag = self.metaConditions["globalTags"]["data"]
        else:
            self.globalTag = self.metaConditions["globalTags"]["MC"]
        self.customizeGlobalTag(process)
        if len(self.fileNames) >0:
            self.customizeFileNames(process)
        if self.timing == 1:
            self.customizeTiming(process)
        if self.bunchSpacing == 25:
            pass #default
        elif self.bunchSpacing == 50:
            self.customize50ns(process)
        else:
            raise Exception, "Only bunchSpacing=25 and bunchSpacing=50 are supported"

        from flashgg.MicroAOD.flashggMETs_cff import updateMETs
        updateMETs(process, self.options)
        process.p *= process.flashggMetSequence

        # Insert lots of producer/filter modules to cms.task automatically
        self.insertTaskToProcess( process )
        print "Final customized process:",process.p

    # signal specific customization
    def customizeSignal(self,process):
        print "customizeSignal"
        process.flashggGenPhotonsExtra.defaultType = 1

        # if os.environ["CMSSW_VERSION"].count("CMSSW_8_0"):
        #     process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
        #     process.rivetProducerHTXS = cms.EDProducer('HTXSRivetProducer',
        #                                                HepMCCollection = cms.InputTag('myGenerator','unsmeared'),
        #                                                ProductionMode = cms.string('PRODUCTIONMODENOTSET'),
        #                                                )
        #     process.mergedGenParticles = cms.EDProducer("MergedGenParticleProducer",
        #                                                 inputPruned = cms.InputTag("prunedGenParticles"),
        #                                                 inputPacked = cms.InputTag("packedGenParticles"),
        #                                                 )
        #     process.myGenerator = cms.EDProducer("GenParticles2HepMCConverterHTXS",
        #                                          genParticles = cms.InputTag("mergedGenParticles"),
        #                                          genEventInfo = cms.InputTag("generator"),
        #                                          )
        #     process.p *= process.mergedGenParticles
        #     process.p *= process.myGenerator
        #     process.p *= process.rivetProducerHTXS
        #     process.out.outputCommands.append('keep *_HTXSRivetProducer_*_*')

        #raise Exception,"Debugging ongoing for HTXS in CMSSW 9"
        process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
        process.rivetProducerHTXS = cms.EDProducer('HTXSRivetProducer',
                                                   HepMCCollection = cms.InputTag('myGenerator','unsmeared'),
                                                   LHERunInfo = cms.InputTag('externalLHEProducer'),
                                                   ProductionMode = cms.string('AUTO'),
        )

        process.mergedGenParticles = cms.EDProducer("MergedGenParticleProducer",
                                                    inputPruned = cms.InputTag("prunedGenParticles"),
                                                    inputPacked = cms.InputTag("packedGenParticles"),
        )
        process.myGenerator = cms.EDProducer("GenParticles2HepMCConverter",
                                             genParticles = cms.InputTag("mergedGenParticles"),
                                             genEventInfo = cms.InputTag("generator"),
                                             signalParticlePdgIds = cms.vint32(25), ## for the Higgs analysis
        )
        process.p *= process.mergedGenParticles
        process.p *= process.myGenerator
        process.p *= process.rivetProducerHTXS
        process.out.outputCommands.append('keep *_rivetProducerHTXS_*_*')

        self.customizePDFs(process)
        self.customizeHLT(process)

    def customizePDFs(self,process):
        process.load("flashgg/MicroAOD/flashggPDFWeightObject_cfi")
        if "mc2hessianCSV" in self.metaConditions.keys() and self.metaConditions["mc2hessianCSV"] != "":
            setattr(process.flashggPDFWeightObject, "mc2hessianCSV", str(self.metaConditions["mc2hessianCSV"]))
#        setattr(process.flashggPDFWeightObject, "pdfset", str(self.metaConditions["PDF"]))
        process.p *= process.flashggPDFWeightObject

    # background specific customization
    def customizeBackground(self,process):

        if "sherpa" in self.datasetName:
            process.flashggGenPhotonsExtra.defaultType = 1

    # data specific customization
    def customizeData(self,process):
        print "CUSTOMIZE DATA"
        ## remove MC-specific modules
        modules = process.flashggMicroAODGenSequence.moduleNames()

        for pathName in process.paths:
            path = getattr(process,pathName)
            for mod in modules:
                path.remove( getattr(process,mod))
            print getattr(process,pathName)
        process.out.outputCommands.append("drop *_*Gen*_*_*")
        process.out.outputCommands.append("keep *_reducedEgamma_*RecHit*_*") # for bad events
        delattr(process,"flashggPrunedGenParticles") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenPhotons") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenPhotonsExtra") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenLeptons") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenLeptonsExtra") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenJetsExtra") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenNeutrinos") # will be run due to unscheduled mode unless deleted
        delattr(process,"flashggGenBCHadrons") # will be run due to unscheduled mode unless deleted
        from flashgg.MicroAOD.flashggJets_cfi import maxJetCollections
        for vtx in range(0,maxJetCollections):
#            getattr(process,"flashggPFCHSJets%i"%vtx).Debug = True
            delattr(process,"patJetGenJetMatchAK4PFCHSLeg%i"%vtx)
            delattr(process,"patJetFlavourAssociationAK4PFCHSLeg%i"%vtx)
            delattr(process,"patJetPartons%i"%vtx)
            delattr(process,"patJetPartonMatchAK4PFCHSLeg%i"%vtx)
        self.customizeHighMassIsolations(process)
        process.load("flashgg/MicroAOD/flashggDiPhotonFilter_cfi")
        process.flashggDiPhotonFilterSequence += process.diPhotonSelector
        process.flashggDiPhotonFilterSequence += process.diPhotonFilter # Do not continue running events with 0 diphotons passing pt cuts
        process.p1 = cms.Path(process.diPhotonFilter) # Do not save events with 0 diphotons passing pt cuts
        process.out.SelectEvents = cms.untracked.PSet(SelectEvents=cms.vstring('p1'))

        ###---Add HLT filter as first step of MicroAOD sequence
        if self.addMicroAODHLTFilter:
            process.triggerFilterModule = getMicroAODHLTFilter(customize.datasetName, self.metaConditions)
            if process.triggerFilterModule:
                process.p = cms.Path(process.triggerFilterModule*process.p._seq)
                process.p1 = cms.Path(process.triggerFilterModule*process.p1._seq)

    def customizeDataMuons(self,process):
        process.diPhotonFilter.src = "flashggSelectedMuons"
        process.diPhotonFilter.minNumber = 2
        process.flashggDiPhotonFilterSequence.remove(process.diPhotonSelector)
        process.flashggDiPhotonFilterSequence.remove(process.diPhotonFilter)
        process.flashggMuonFilterSequence += process.diPhotonFilter

    def customizeHighMassIsolations(self,process):
        # for isolation cones
        process.vetoPhotons = cms.EDFilter("CandPtrSelector",
                                           src=cms.InputTag("flashggPhotons"),
                                           cut=cms.string("pt>10"),
                                           )
        process.vetoJets = cms.EDFilter("CandPtrSelector",
                                        src=cms.InputTag("slimmedJets"),
                                        cut=cms.string("pt>30"),
                                        )

        process.flashggPhotons.extraIsolations.extend([
                cms.PSet(
                    algo=cms.string("FlashggRandomConeIsolationAlgo"),
                    name=cms.string("rnd03"),
                    coneSize=cms.double(0.3), doOverlapRemoval=cms.bool(False),
                    charged=cms.vdouble(0.02,0.02,0.1),
                    photon=cms.vdouble(0.0, 0.070, 0.015, 0.0, 0.0, 0.0),
                    vetoCollections_=cms.VInputTag(cms.InputTag("vetoPhotons"),cms.InputTag("vetoJets")),
                    veto=cms.double(0.699),
                    ),
                ###          cms.PSet(
                ###              algo=cms.string("DiphotonsFootPrintRemovedIsolationAlgo"),
                ###              name=cms.string("fpr03"),
                ###              coneSize=cms.double(0.3), doRandomCone=cms.bool(False), removePhotonsInMap=cms.int32(1),
                ###              rechitLinkEnlargement=cms.double(0.25),
                ###              charged=cms.vdouble(0.02,0.02,0.1),
                ###              photon=cms.vdouble(0.0, 0.070, 0.015, 0.0, 0.0, 0.0),
                ###              ),
                cms.PSet(
                    algo=cms.string("DiphotonsFootPrintRemovedIsolationAlgo"),
                    name=cms.string("fprNoMap03"),
                    coneSize=cms.double(0.3), doRandomCone=cms.bool(False), removePhotonsInMap=cms.int32(0),
                    rechitLinkEnlargement=cms.double(0.25),
                    photon=cms.vdouble(0.0, 0.070, 0.015, 0.0, 0.0, 0.0),
                    charged=cms.vdouble(0.02,0.02,0.1),
                    ),
                #### cms.PSet(
                ####     algo=cms.string("DiphotonsFootPrintRemovedIsolationAlgo"),
                ####     name=cms.string("fprRnd03"),
                ####     coneSize=cms.double(0.3), doRandomCone=cms.bool(True), removePhotonsInMap=cms.int32(1),
                ####     rechitLinkEnlargement=cms.double(0.25),
                ####     charged=cms.vdouble(0.02,0.02,0.1),
                ####     vetoCollections_=cms.VInputTag(cms.InputTag("vetoPhotons"),cms.InputTag("vetoJets")),
                ####     veto=cms.double(0.699),
                ####     ),
                ]
          )

        for icone,dphi in enumerate( [0.7,1.3,1.9,2.5,3.1,-2.5,-1.9,-1.3,-0.7] ):
            process.flashggPhotons.extraIsolations.append(
                cms.PSet(
                    algo=cms.string("FlashggRandomConeIsolationAlgo"),
                    name=cms.string("rnd03_%d" % icone), deltaPhi=cms.double(dphi),
                    coneSize=cms.double(0.3), doOverlapRemoval=cms.bool(False),
                    charged=cms.vdouble(0.02,0.02,0.1),
                    photon=cms.vdouble(0.0, 0.070, 0.015, 0.0, 0.0, 0.0),
                    vetoCollections_=cms.VInputTag(cms.InputTag("vetoPhotons"),cms.InputTag("vetoJets")),
                    veto=cms.double(0.699),
                    ## maxVtx=cms.int32(1), computeWorstVtx=cms.bool(False)
                    ),
                )

    # Add debug collections    
    def customizeDebug(self,process):
        from flashgg.MicroAOD.flashggMicroAODOutputCommands_cff import microAODDebugOutputCommand
        process.out.outputCommands += microAODDebugOutputCommand # extra items for debugging

    # Add HLT collections    
    def customizeHLT(self,process):
        from flashgg.MicroAOD.flashggMicroAODOutputCommands_cff import microAODHLTOutputCommand
        process.out.outputCommands += microAODHLTOutputCommand # extra items for HLT efficiency

    def customizeMuMuGamma(self,process):
        process.load("flashgg/MicroAOD/flashggDiMuons_cfi")
        process.load("flashgg/MicroAOD/flashggMuMuGamma_cfi")
        process.p *= process.flashggDiMuons*process.flashggMuMuGamma

    def customizeTTH(self,process):
        process.load("flashgg/MicroAOD/ttHGGFilter_cfi")
        process.ttHFilter = cms.Path(process.ttHGGFilter)
        process.out.SelectEvents = cms.untracked.PSet(SelectEvents=cms.vstring('ttHFilter'))

    def customizeVBF(self,process):
        process.rivetProducerHTXS.ProductionMode = "VBF"

    def customizeVH(self,process):
        # from CMSSW_10_5_0 VH is apparently no longer supported, one should specify either ZH or WH, using auto instead
        process.rivetProducerHTXS.ProductionMode = "AUTO"

    def customizeGGH(self,process):
        process.rivetProducerHTXS.ProductionMode = "GGF"

    def customizeHH(self,process):
        print "using HH sample, treating them as signals"



    def customizeTH(self,process):
        print "customizeTH"
        cross_sections=["$CMSSW_BASE/src/flashgg/MetaData/data/cross_sections.json"]
        cross_sections_ = {}
        LHESourceName = None
        for xsecFile in cross_sections:
            fname = os.path.expanduser( os.path.expandvars(xsecFile) )
            cross_sections_.update( json.loads( open(fname).read() ) )
        if customize.datasetName.count("/"):
            dsName = customize.datasetName.split("/")[1]
        else:
            dsName = customize.datasetName
        if dsName in cross_sections_.keys() :
            xsec_info = cross_sections_[dsName]
            if "LHESourceName" in xsec_info.keys() :
                LHESourceName = str( xsec_info["LHESourceName"] )

        if LHESourceName :
            print "the LHESource %s is set to be kept for dataset %s" % (LHESourceName , dsName)
            process.out.outputCommands.append("keep %s" % (LHESourceName) ) #*_source_*_LHEFile")
        else :
            print "for TH sample of %s, no LHESource is found to be kept" % (dsName)
        # process.rivetProducerHTXS.ProductionMode = "TH"
#        process.flashggPDFWeightObject.LHEEventTag = "source"
#        process.flashggPDFWeightObject.LHERunLabel = "source"
        # process.flashggPDFWeightObject.isStandardSample = False
        # process.flashggPDFWeightObject.isThqSample = True

    def customizePhotons(self, process):
        for opt, value in self.metaConditions["flashggPhotons"].items():
            if isinstance(value, unicode):
                setattr(process.flashggPhotons, opt, str(value))
            else:
                setattr(process.flashggPhotons, opt, value)

    def customizeDiPhotons(self, process):
        for opt, value in self.metaConditions["flashggDiPhotons"].items():
            if isinstance(value, unicode):
                setattr(process.flashggDiPhotons, opt, str(value))
            else:
                setattr(process.flashggDiPhotons, opt, value)

    def customizeGlobalTag(self,process):
        from Configuration.AlCa.GlobalTag import GlobalTag
        process.GlobalTag = GlobalTag(process.GlobalTag, self.globalTag, '')

    def customizeFileNames(self,process):
        process.source.fileNames = cms.untracked.vstring(self.fileNames)

    def customizeTiming(self,process):
        from Validation.Performance.TimeMemoryInfo import customise as TimeMemoryCustomize
        TimeMemoryCustomize(process)
        process.MessageLogger.cerr.threshold = 'WARNING'

    def customizePFCHS(self,process):
        # need to allow unscheduled processes otherwise reclustering function will fail
        if not hasattr(process,"options"):
            process.options = cms.untracked.PSet()
        process.options.allowUnscheduled = cms.untracked.bool(True)
        from flashgg.MicroAOD.flashggJets_cfi import addFlashggPFCHSJets
        from flashgg.MicroAOD.flashggJets_cfi import maxJetCollections
        for vtx in range(0,maxJetCollections):
            addFlashggPFCHSJets (process = process,
                                 DeepJet = self.metaConditions['DeepJet'],
                                 isData=(self.processType == "data"),
                                 vertexIndex =vtx,
                                 #doQGTagging = True,
                                 label = '' + str(vtx))

    def customizePuppi(self,process):
        # need to allow unscheduled processes otherwise reclustering function will fail                                                            
        if not hasattr(process,"options"):
            process.options = cms.untracked.PSet()
        process.options.allowUnscheduled = cms.untracked.bool(True)
        from flashgg.MicroAOD.flashggJets_cfi import addFlashggPuppiJets
        from flashgg.MicroAOD.flashggJets_cfi import maxJetCollections
        for vtx in range(0,maxJetCollections):
            addFlashggPuppiJets (process     = process,
                                 vertexIndex = vtx,
                                 debug       = False,
                                 label = '' + str(vtx))

    def customizeRemovePFCHS(self,process):
        for pathName in process.paths:
            path = getattr(process,pathName)
            path.remove(process.flashggVertexMapForCHS)
            path.remove(process.flashggFinalJets)
        process.out.outputCommands.append('drop *_flashggFinalJets_*_*')

    def customizeRemovePuppi(self,process):
        for pathName in process.paths:
            path = getattr(process,pathName)
            path.remove(process.flashggVertexMapForPUPPI)
            path.remove(process.flashggFinalPuppiJets)
        process.out.outputCommands.append('drop *_flashggFinalPuppiJets_*_*')

    def customize50ns(self,process):
        process.flashggPhotons.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/MicroAOD/data/MVAweights_Spring15_50ns_barrel.xml")
        process.flashggPhotons.photonIdMVAweightfile_EE = cms.FileInPath("flashgg/MicroAOD/data/MVAweights_Spring15_50ns_endcap.xml")

    def insertTaskToProcess(self,process):

        # Hack for Jets
        process.task = createTaskWithAllProducersAndFilters(process)
        process.p.associate(process.task)

def createTaskWithAllProducersAndFilters(process):
   from FWCore.ParameterSet.Config import Task
   l = [ p for p in process.producers.itervalues()]
   l.extend( (f for f in process.filters.itervalues()) )
   return Task(*l)

# customization object
customize = MicroAODCustomize()
