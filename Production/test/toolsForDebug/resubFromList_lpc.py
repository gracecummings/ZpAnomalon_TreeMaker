#This is a scrip to resubmit jobs to condor that have only the index and the sample listed 
#This script is designed to take the output of the `countOutput_listToResub.py` script
#This simply reads in a txt file, and resubmits the jobs with only good sites
#Directions for use are as follows
#Example follows example detailed in `countOutput_ListToResub.py`
#Step 1: copy the .txt file with the list to resubmit to the condor submission directory
#    example command: cp filesForSubmission_Autumn18_TTToSemiLeptonic_2021-06-18.text ../ttbarsub/.
#Step 2: copy this script to the same condor submission directory
#Step 3: Resubmit the jobs
#   example command: python resubFromList_lpc.py -f filesForSubmission_Autumn18_TTToSemiLeptonic_2021-06-18.text -e tt_semilep_had_may2021
#    -f is the list of files to resubmit
#    -e is the destination eos directory for the ntuple output
#the `lpc` version of the script is designed to work on the lpc, and uses the local tarball
#LPC DESIRED SITES LIST HAS NOT BEEN TESTED, COMMENTED OUT
#the `cmsconnect` version of the script is designed to work on cms connect, and will use the tarball
# the is in the eos directory given as the -e option. If changes to TreeMaker have been done
# prior to a new submission, a new tarball should be copied with ./checkVomstar.sh as usual
#eos output directory presumed to be in the lpcboostres group area

import glob
import os
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--fname",type=str)
    parser.add_argument("-e","--outputeosdir",type=str)
    args = parser.parse_args()

    f = open(args.fname)
    lines = f.readlines()

    for l in lines:
        fdescrip = l.split(" ")[0]
        fidx = l.split(" ")[1][:-1]
        eosdir = args.outputeosdir
        #eosdir = 'tt_semilep_had_may2021'

        jdlName = fdescrip+"_"+fidx+"_countresub.jdl"
        jdl = open(jdlName,"w")
        jdl.write("universe = vanilla\n")
        jdl.write("Executable = jobExecCondor.sh\n")
        jdl.write('+REQUIRED_OS = "rhel7"\n')
        jdl.write("request_disk = 1000000\n")
        jdl.write("request_memory = 3800\n")
        jdl.write("request_cpus = 1\n")
        jdl.write("Should_Transfer_Files = YES\n")
        jdl.write("WhenToTransferOutput = ON_EXIT_OR_EVICT\n")
        jdl.write("Transfer_Input_Files = jobExecCondor.sh, step1.sh,step2.sh, CMSSW_10_2_21.tar.gz, input/args_"+fdescrip+"_"+fidx+".txt\n")
        jdl.write("Output = {0}_{1}_{2}_out.stdout\n".format(fdescrip,fidx,"countresub"))
        jdl.write("Error = {0}_{1}_{2}_err.stder\n".format(fdescrip,fidx,"countresub"))
        jdl.write("Log = {0}_{1}_{2}_log.log\n".format(fdescrip,fidx,"countresub"))
        jdl.write("Arguments = -S step1.sh,step2.sh -C CMSSW_10_2_21 -j {0} -p {1} -o root://cmseos.fnal.gov//store/group/lpcboostres/{2}\n".format(fdescrip,fidx,eosdir))
        jdl.write("want_graceful_removal = true\n")
        jdl.write("on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n")
        jdl.write("on_exit_hold = ( (ExitBySignal == True) || (ExitCode != 0) )\n")
        jdl.write("\n")
        #jdl.write('+DESIRED_Sites="T3_US_Baylor,T2_US_Caltech,T3_US_Colorado,T3_US_Cornell,T3_US_FIT,T1_US_FNAL,T3_US_FNALLPC,T3_US_Omaha,T3_US_JHU,T3_US_Kansas,T2_US_MIT,T3_US_NotreDame,T2_US_Nebraska,T3_US_NU,T3_US_OSU,T3_US_Princeton_ICSE,T2_US_Purdue,T3_US_Rice,T3_US_Rutgers,T3_US_MIT,T3_US_NERSC,T3_US_SDSC,T3_US_FIU,T3_US_FSU,T3_US_OSG,T3_US_TAMU,T3_US_TTU,T3_US_UCD,T3_US_UCSB,T2_US_UCSD,T3_US_UMD,T3_US_UMiss,T2_US_Vanderbilt,T2_US_Wisconsin"')
        #jdl.write("\n")
        jdl.write("Queue 1\n")#Not sure about this one
        jdl.close()
        os.system("condor_submit {0}".format(jdlName))
        
