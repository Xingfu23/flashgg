outdir="/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_17/UL_17_data_test2"
storedir="/eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset/UL_17/UL_17_data_test2"

fggRunJobs.py --load UL_runII_v1_2017_data.json \
              -d $outdir --stage-to $storedir \
              -n 100 \
              -q testmatch \
              --no-use-tarball \
              --no-copy-proxy -D -P \
              -x cmsRun workspaceStd.py maxEvents=10000 \
                                        doStageOne=True \
                                        doSystematics=False \
                                        dumpWorkspace=False \
                                        dumpTrees=True