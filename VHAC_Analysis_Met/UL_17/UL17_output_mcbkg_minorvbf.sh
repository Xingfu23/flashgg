outdir="/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_17/UL17_vbf125"
storedir="/eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset/UL_17/UL17_vbf125"

fggRunJobs.py --load UL17_vbf125.json \
              -d $outdir --stage-to $storedir \
              -n 100 \
              -q testmatch \
              --no-use-tarball \
              --no-copy-proxy -D -P \
              -x cmsRun workspaceStd.py maxEvents=-1 \
                                        doStageOne=True \
                                        doSystematics=False \
                                        dumpWorkspace=False \
                                        dumpTrees=True