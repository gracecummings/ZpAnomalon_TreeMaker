import glob 
import os

f = open('hold-134106.txt')
lines = f.readlines()

segs = 0
nintysixers = 0
jtbsux = 0
atefivers = 0
atefurers = 0
for line in lines:
    parts = line.split()
    code = parts[-1]
    job = parts[0]
    cluster = job.split(".")[0]
    fnum    = job.split(".")[1]
    fint    =  glob.glob("*_"+fnum+"_"+cluster+".stdout")[0]
    if "undefined" in code:
        continue
    if float(code) == 96:
        nintysixers += 1
        readcheck = open(fint)
        checklines = readcheck.readlines()
        if "jettoolbox.root" in checklines[-8]:
            if "failure" in checklines[-7]:
                if "xrdcp -f Run" in checklines[-9]: 
                    jtbsux += 1
                    #print checklines[-9]
                    #print checklines[-8]
                    #print checklines[-7]
                    #os.system("echo 'jettoolbox broke xdcrp, but file fine'")
                    #os.system("condor_rm "+job)
                    os.system("condor_rm "+job)
        #else:
        #    print job
        readcheck.close()
    if float(code) == 85:
        atefivers +=1
        os.system("condor_release "+job)
    if float(code) == 84:
        atefurers +=1
        os.system("condor_release "+job)
    if float(code) == 139:
        segs +=1
        fails = open("cluster_fails.txt","a")
        nom = fint.split("_")[0]
        print "failed: {0} {1} {2}".format(nom,fnum,cluster)
        fails.write("{0} {1} {2}\n".format(nom,fnum,cluster))
        os.system("condor_rm "+job)
    if float(code) == 68:
        os.system("condor_release "+job)

print "total number of held files:   ",len(lines)
print "number of files with code 96: ",nintysixers
print "number of files with code 85: ",atefivers
print "number of files with code 84: ",atefurers
print "number of files with code 139: ",segs
