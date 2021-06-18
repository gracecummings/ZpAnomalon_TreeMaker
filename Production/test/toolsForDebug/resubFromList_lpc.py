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
        #id = l.split(" ")[0]
        #cluster = id.split(".")[0]
        #fidx    = id.split(".")[1]
        #outf    = glob.glob('*_'+fidx+'_'+cluster+'.condor')
        #fdescrip  = outf[0].split('_'+fidx)[0]
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
        jdl.write("Queue 1\n")#Not sure about this one
        jdl.close()
        os.system("condor_submit {0}".format(jdlName))
        #os.system("condor_rm -name lpcschedd1.fnal.gov {0}".format(id))
        
