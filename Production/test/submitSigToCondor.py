import os

f = open('sigSamples_list.txt')
samps = f.readlines()

for s in samps:
    name = s.split("_cff.py")[0]
    print(name)

    newjdl = ftype+"_"+fnum+"_segfault.jdl"
    jdl = open(newjdl,"w")
    jdl.write("universe = vanilla\n")
    jdl.write("Executable = jobExecCondor.sh\n")
    jdl.write('+REQUIRED_OS = "rhel7"\n')
    jdl.write("request_disk = 1000000\n")
    jdl.write("request_memory = 3800\n")
    jdl.write("request_cpus = 1\n")
    jdl.write("Should_Transfer_Files = YES\n")
    jdl.write("WhenToTransferOutput = ON_EXIT_OR_EVICT\n")
    jdl.write("Transfer_Input_Files = jobExecCondor.sh, step1.sh,step2.sh, input/args_"+ftype+"_"+fnum+".txt\n")
    jdl.write("Output = {0}_{1}_{2}_out.stdout\n".format(ftype,fnum,"segfault"))
    jdl.write("Error = {0}_{1}_{2}_err.stder\n".format(ftype,fnum,"segfault"))
    jdl.write("Log = {0}_{1}_{2}_log.log\n".format(ftype,fnum,"segfault"))
    jdl.write("Arguments = -S step1.sh,step2.sh -C CMSSW_10_2_21 -X root://cmseos.fnal.gov//store/user/lpcboostres/ZpAnomalonHZ_SignalNtuples/ -j {0} -p {1} -o root://cmseos.fnal.gov//store/user/lpcboostres/ZpAnomalonHZ_SignalNtuples/".format(ftype,fnum))
    jdl.write("want_graceful_removal = true\n")
    jdl.write("on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n")
    jdl.write("on_exit_hold = ( (ExitBySignal == True) || (ExitCode != 0) )\n")
    jdl.write('+DESIRED_Sites="T3_US_Baylor,T2_US_Caltech,T3_US_Colorado,T3_US_Cornell,T3_US_FIT,T1_US_FNAL,T3_US_FNALLPC,T3_US_Omaha,T3_US_JHU,T3_US_Kansas,T2_US_MIT,T3_US_NotreDame,T2_US_Nebraska,T3_US_NU,T3_US_OSU,T3_US_Princeton_ICSE,T2_US_Purdue,T3_US_Rice,T3_US_Rutgers,T3_US_MIT,T3_US_NERSC,T3_US_SDSC,T3_US_FIU,T3_US_FSU,T3_US_OSG,T3_US_TAMU,T3_US_TTU,T3_US_UCD,T3_US_UCSB,T2_US_UCSD,T3_US_UMD,T3_US_UMiss,T2_US_Vanderbilt,T2_US_Wisconsin"')
    jdl.write("\n")
    jdl.write("Queue 1\n")#Not sure about this one                                                   
    jdl.close()

    #os.system("condor_sumbit {0}".format(newjdl)
