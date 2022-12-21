#!/bin/bash
export XRD_NETWORKSTACK=IPv4
export X509_USER_PROXY=/afs/cern.ch/user/x/xisu/x509up_u118456
WD=$PWD
echo
echo
echo
cd /afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29
eval $(scram runtime -sh)
cd $WD
mkdir /afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_17/UL_17_data
echo "ls $X509_USER_PROXY"
ls $X509_USER_PROXY
mkdir .dasmaps 
mv das_maps_dbs_prod.js .dasmaps/ 

declare -a jobIdsMap=(0 1)
cmsRun /afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_17/UL_17_data/workspaceStd.py maxEvents=10000 doStageOne=True doSystematics=False dumpWorkspace=False dumpTrees=True campaign=Era2017_legacy_v1_Summer19UL metaConditions=/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/MetaData/data/MetaConditions/Era2017_legacy_v1.json useAAA=True puTarget=6.238e-06,2.614e-05,4.849e-05,9.107e-05,9.776e-05,0.0001416,0.0001553,0.0001637,0.0002213,0.0005245,0.001052,0.001992,0.00317,0.004549,0.006438,0.009079,0.01267,0.01687,0.02103,0.02487,0.02824,0.03097,0.03307,0.03469,0.03608,0.03739,0.03851,0.0392,0.03932,0.03881,0.03775,0.03623,0.03435,0.03215,0.02974,0.0273,0.02494,0.02277,0.02082,0.01917,0.01791,0.01711,0.01682,0.01702,0.01759,0.01836,0.01906,0.01941,0.01917,0.01821,0.01654,0.01433,0.01184,0.009335,0.007048,0.005114,0.003583,0.002435,0.001613,0.001047,0.0006682,0.0004212,0.0002632,0.0001635,0.0001014,6.299e-05,3.93e-05,2.471e-05,1.568e-05,1.006e-05,6.53e-06,4.28e-06,2.83e-06,1.883e-06,1.259e-06,8.436e-07,5.655e-07,3.787e-07,2.53e-07,1.684e-07,1.116e-07,7.359e-08,4.825e-08,3.143e-08,2.033e-08,1.306e-08,8.322e-09,5.261e-09,3.297e-09,2.049e-09,1.262e-09,7.697e-10,4.652e-10,2.785e-10,1.651e-10,9.691e-11,5.632e-11,3.24e-11,1.845e-11 processIdMap=/afs/cern.ch/user/x/xisu/private/local/Analysis_workspace/VH_AC_tmp1/flashgg_d2/CMSSW_10_6_29/src/flashgg/VHAC_Analysis_Met/UL_17/UL_17_data/config.json dataset=/DoubleEG/alesauva-UL_test-10_6_4-v0-Run2017C-09Aug2019_UL2017-v1-53faf905fdb551f89c40f719673e864f/USER outputFile=/eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset/UL_17/UL_17_data/output_DoubleEG_alesauva-UL_test-10_6_4-v0-Run2017C-09Aug2019_UL2017-v1-53faf905fdb551f89c40f719673e864f_USER.root nJobs=2 jobId=${jobIdsMap[${1}]} 
retval=$?
if [[ $retval != 0 ]]; then
    retval=$(( ${jobIdsMap[${1}]} + 1 )) 
fi 
if [[ $retval == 0 ]]; then
    errors=""
    for file in $(find -name '*.root' -or -name '*.xml'); do
        echo "cp -pv ${file} /eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset/UL_17/UL_17_data"
        cp -pv $file /eos/user/x/xisu/WorkSpace/VH_AC_Analysis/flashgg_output/UL_dataset/UL_17/UL_17_data
        if [[ $? != 0 ]]; then
            errors="$errors $file($?)"
        fi
    done
    if [[ -n "$errors" ]]; then
       echo "Errors while staging files"
       echo "$errors"
       exit -2
    fi
fi

exit $retval

