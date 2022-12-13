outdir="/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d1/CMSSW_10_6_8/src/flashgg/VHMET_Analysis/RR_18/Output_file_MCSet1_ZHAC_withnewmodel"
storedir="/eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/testoutput/ZHAC_withmodel"

fggRunJobs.py --load RR_v2_2018_MCSet1_Z_AC.json \
              -d $outdir --stage-to $storedir \
              -n 50 \
              -q testmatch \
              --no-use-tarball --no-copy-proxy -D -P \
              -x cmsRun workspaceStd.py maxEvents=-1 \
                                        doStageOne=True \
                                        doSystematics=False \
                                        dumpWorkspace=False \
                                        dumpTrees=True
