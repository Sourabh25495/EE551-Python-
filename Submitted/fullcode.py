import numpy as np
import matplotlib.pyplot as plt

textfile=open('/home/sourabh/Documents/demo','r')
line1=textfile.readline()
textfile.close()



for line in open('/home/sourabh/Documents/demo'):
    doSplit=line.split(" ")
    l=len(doSplit)
    reqColumn=doSplit[l-2]
    c=reqColumn[5:9]
    #print(c)
    f1 = open('/home/sourabh/Documents/writeHere','a')
    f1.write(c) 
    f1.write('\n')
    f1.close() 



