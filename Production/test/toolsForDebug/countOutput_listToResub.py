#this is a script to count if all of the files possible have generated ntuples
#It compares a text file with the generated ntuples listed (only ntuple names, not full eos path)
#to the config file used to submit the job
#The output is another text file with the sample description and the index of the file missed
#these the only inputs needed to resubmit the missed jobs
#Step-by-step instructions follow

#Step 1: generate a text file that dumps the output eos directory
#       example command: eosls /store/user/lpcboostres/tt2l2nu_may2021 | grep Autumn18.TTToSemiLep > samplesToSkim_tt2l2nu_may2021_Autumn18_TTToSemiLeptonic.txt 
#Step 2: run this script from the /TreeMaker/Production/Test/toolsForDebug directory
#      example command: python countOutPut_listToResub.py -f samplesToSkim_tt2l2nu_may2021_Autumn18_TTToSemiLeptonic.txt
#This generates the output file `filesForSubmission_Autumn18_TTToSemiLeptonic_2021-06-18.txt`
#The date will be the date you ran it
#The output is just a list that will need to be copied to the job submission directory
#The directions for how to resubmit the jobs are in the `resubFromList_*.py` scripts

import argparse
import glob
import os
from datetime import date


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--fname",type=str)
    args = parser.parse_args()

    f = open(args.fname,"r")
    fl = f.readlines()
        
    mcdir = fl[0].split(".")[0]
    iniidx  = fl[0].split(".")[1].split("_RA")[0][-1]
    samp = fl[0].split(".")[1].split("_"+iniidx+"_RA")[0]
    name = samp
    
    print "Counting for sample ",name

    #print"Some debug for 2016 counting"
    #print"   An example file: ",fl[0]
    #print"   Gathering the directory of the files: ",mcdir
    #print"   The index: ",iniidx

    if "Run" in mcdir:
        fl.sort(key = lambda x:x.split("_")[1])
        #print fl[:10]
        flnums = [x.split("_")[-2] for x in fl]
        #print flnums[:10]
    else:
        fl.sort(key = lambda x:x.split('pythia8_')[-1].split("_RA")[0])
        flnums = [x.split('pythia8_')[-1].split("_RA")[0] for x in fl]
        if "new_pmx" in samp:
            samp = samp.split("_new_pmx")[0]
            flnums = [x.split('pythia8_new_pmx_')[-1].split("_RA")[0] for x in fl]

    print "Number of files produced: ",len(fl)


    #fchecknames = glob.glob("../../python/"+mcdir+"/"+samp+"*")
    fchecknames = glob.glob("/uscms/home/gcumming/nobackup/work_2019_summer/TreeMakerGarden/CMSSW_10_2_21/src/TreeMaker/Production/python/"+mcdir+"/"+samp+"*")

    print "Comparing the count to file ",fchecknames[0]
    fcheck = open(fchecknames[0],"r")
    fcheckl = fcheck.readlines()
    numberfiles = 0
    nstrl = []
    for l,line in enumerate(fcheckl):
        if samp in line:
            numberfiles += 1
            nstrl.append(str(numberfiles-1))

    nstrl.sort()
    print "Number of files in config: ",numberfiles

    
    settrue = set(nstrl)
    setmade = set(flnums)
    setmiss = settrue-setmade

    print "missing files: ",setmiss
    
    if len(setmiss) > 0:
        listToSub = open("filesForSubmission_"+mcdir+"_"+name+"_"+str(date.today())+".txt","w")
        for idx in setmiss:
            listToSub.write(mcdir+"."+name+" "+idx+"\n")
