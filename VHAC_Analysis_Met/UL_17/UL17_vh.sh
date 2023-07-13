outdir="/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_acvhlep/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_17/UL17_vh_sys_test"
storedir="/eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset_aclep/UL_17/UL17_vh_sys_test"

fggRunJobs.py --load json/UL17_vh125.json \
              -d $outdir --stage-to $storedir \
              -n 100 \
              -q testmatch \
              --no-use-tarball \
              --no-copy-proxy -D -P \
              -x cmsRun workspaceVbf.py maxEvents=1000 \
                                        doStageOne=True \
                                        doSystematics=True \
                                        doPdfWeights=True \
                                        dumpWorkspace=False \
                                        dumpTrees=True \
                                        disableJEC=True \