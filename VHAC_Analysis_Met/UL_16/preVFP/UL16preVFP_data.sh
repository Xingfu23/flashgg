outdir="/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_16/preVFP/UL16preVFP_data_systest"
storedir="/eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset/UL_16/preVFP/UL16preVFP_data2_systest"

fggRunJobs.py --load UL_runII_v1_2016preVFP.json \
              -d $outdir --stage-to $storedir \
              -n 100 \
              -q testmatch \
              --no-use-tarball \
              --no-copy-proxy -D -P \
              -x cmsRun workspaceStd.py maxEvents=-1 \
                                        doStageOne=True \
                                        doPdfWeights=True \
                                        doSystematics=True \
                                        dumpWorkspace=False \
                                        dumpTrees=True