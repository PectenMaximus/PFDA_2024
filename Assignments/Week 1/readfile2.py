#Author Alec Reid
# import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))


import os
print(os.getcwd()) # Tells you current working directory
os.chdir ("c:/AlecProjects/PFDA_2024/Assignments/Week 1") # Allows you to change to directory you want, path name must be given as string

print(os.getcwd()) 

import csv
FILENAME = "data.csv"
DATADIR = "../Week 1/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if linecount == 0: # Should be header row???
            print (f"{line}\n_______________") # This has only half worked it why is it double printing header line?
        else: # meant to be all other rows?
            total += int(line[0])
        print (line)
        linecount += 1