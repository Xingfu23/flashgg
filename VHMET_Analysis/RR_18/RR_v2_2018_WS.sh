outdir="/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d1/CMSSW_10_6_8/src/flashgg/VHMET_Analysis/RR_18/Output_file_MCSet1_WH130_WS5"
storedir="/eos/user/x/xisu/Work_files/VH_AnomalousCoupling/Output_File_RR_18/RR_18_v2_d1/Output_file_MCSet1_WH130_WS5"

fggRunJobs.py --load RR_v2_2018_MCSet1_W130_WS.json \
              -d $outdir --stage-to $storedir \
              -n 50 \
              -q testmatch \
              --no-use-tarball --no-copy-proxy -D -P \
              -x cmsRun workspaceStd.py maxEvents=-1 \
                                        doStageOne=True \
                                        doSystematics=True \
                                        dumpWorkspace=True \
                                        dumpTrees=False \
                                        doPdfWeights=False \
                                        useParentDataset=True 