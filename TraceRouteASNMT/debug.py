#This code is used only if the data still remains unstructured after extraction from the file where the traceroute data has been stored else continue with normal execution od trcout123.py and plotrcot.py


with open("/home/sourabh/Desktop/finalValuesToPlot", "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if "*" in line: 
        for l in searchlines[i:i+1]: 
            print(line)


with open("/home/sourabh/Desktop/finalValuesToPlot", "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if "." in line: 
        for l in searchlines[i:i+1]: 
            #print(line)
            f1 = open('/home/sourabh/Desktop/saveTheLine1','a')
            f1.write(line)
            f1.write('\n')
            f1.close()
