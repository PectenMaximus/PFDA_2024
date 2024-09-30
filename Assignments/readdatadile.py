# Author: Alec Reid 30/09/2024

import csv

Filename = "data.csv"
DATADIR = "../PFDA_2024/"

with open(DATADIR + Filename, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)
