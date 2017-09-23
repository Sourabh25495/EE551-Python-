import numpy as np
import matplotlib.pyplot as plt
import linecache
import sys


with open("/home/sourabh/Desktop/dumpfile", "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if "8  " in line: 
        for l in searchlines[i:i+1]: 
            #print(line)
            f1 = open('/home/sourabh/Desktop/saveTheLine','a')
            f1.write(line)
            f1.write('\n')
            f1.close()

for line in open('/home/sourabh/Desktop/saveTheLine'):
    doSplit=line.split(" ")
    l=len(doSplit)
    reqColumn=doSplit[l-2]
    c=reqColumn[0:5]
    #print(c)
    f1 = open('/home/sourabh/Desktop/finalValuesToPlot','a')
    f1.write(c) 
    #f1.write('\n')
    f1.close()










      
















              
          
