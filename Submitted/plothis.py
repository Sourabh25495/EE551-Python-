import numpy as np
import matplotlib.pyplot as plt
Extract_data = np.loadtxt('/home/sourabh/Documents/writeHere')

sorted_data = np.sort(Extract_data)

yvals=np.arange(len(sorted_data))/float(len(sorted_data))

plt.plot(sorted_data,yvals)

plt.show()
