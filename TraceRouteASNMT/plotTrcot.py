import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('/home/sourabh/Desktop/saveTheLine1')

sorted_data = np.sort(data)

yvals=np.arange(len(sorted_data))/float(len(sorted_data))

plt.plot(sorted_data,yvals)

plt.show()
