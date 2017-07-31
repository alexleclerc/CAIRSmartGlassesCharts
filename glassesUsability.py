import matplotlib.pyplot as plt
import numpy
import numpy as numpy
from numpy.ma import arange

#data setup
#here, numpy.nan is preferred to 0 or null to keep the chart clean and
#   works better with floats
wglasses = [numpy.nan, 3.5, 5, numpy.nan,4,2,3,4,2,2,5,2.5,3,2,2.5,1]
woglasses = [2,5,3, numpy.nan,4,4,1,4,3,3,3,4,1,5,3,4]
x = arange(16)
pnames = ['P1','P2','P3','P4','P5','P6','P7','P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14','P15','P16']

#plot the with glasses and then without
plt.scatter(x, wglasses, c='b', label='with glasses')
plt.scatter(x, woglasses, c='r', marker='x', label='without glasses')


#*****formatting

#1 easiest, invert the axis so it is toward the top
plt.gca().invert_yaxis()
plt.grid()
plt.axes().set_axisbelow(True)
plt.xticks(arange(16))
plt.axes().set_xticklabels(pnames)
plt.ylabel('Likert Rating')
plt.xlabel('Participants')
plt.title('Comparison of Participants Easiness Rating of Smart Glasses')

plt.show()