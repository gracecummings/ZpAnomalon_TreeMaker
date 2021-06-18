#This script takes the editted output of the  `condor_q --held command`, and resubmits the job
#This script should be executed in the condor submission  directory
#Step 1: pipe the output of your held jobs into a text file
#    example command: condor_q --held > holds.txt
#Step 2: edit the output file (holds.txt) to only have the lines relevant to your jobs
#    example first line: 12629352.116 gcumming        5/5  03:26 Job held by PERIODIC_HOLD due to memory usage 2000000 greater than requested 2000000.
#    This example held is a critical failure. 
#    Delete the extra lines at the end of the output as well.
#Step 3: Determine if you want this script to also remove the job you want to resubmit automatically
#      If yes, uncomment the last line and edit for a lpcschedd
#Step 4: Run the script and resubmit your jobs
#      example commant: python resubFrom_condor_q_Output.py -f holds.txt -e eosdirname4output
#This script only works on the lpc condor batch system
#LPC DESIRED SITES LIST HAS NOT BEEN TESTED, COMMENTED OUT
#This coult be combined with options from exampleHoldDecisions.py if some jobs just should
#just be released, and others removed and resubmitted

import glob
import os
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--fname",type=str)
    parser.add_argument("-e","--outputeosdir",type=str)
    args = parser.parse_args()

    eosdir = args.outputeosdir
    f = open(args.fname)
    lines = f.readlines()

    for l in lines:
        id = l.split(" ")[0]
        cluster = id.split(".")[0]
        fidx    = id.split(".")[1]
        outf    = glob.glob('*_'+fidx+'_'+cluster+'.condor')
        fdescrip  = outf[0].split('_'+fidx)[0]

        jdlName = fdescrip+"_"+fidx+"_held.jdl"
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
        jdl.write("Output = {0}_{1}_{2}_out.stdout\n".format(fdescrip,fidx,"prevheld"))
        jdl.write("Error = {0}_{1}_{2}_err.stder\n".format(fdescrip,fidx,"prevheld"))
        jdl.write("Log = {0}_{1}_{2}_log.log\n".format(fdescrip,fidx,"prevheld"))
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
        #os.system("condor_rm -name lpcschedd1.fnal.gov {0}".format(id))
        
