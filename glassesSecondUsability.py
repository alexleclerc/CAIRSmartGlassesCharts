import matplotlib.pyplot as plt
import numpy
from numpy.ma import arange

#chart comparing likert easiness responses for with glasses and without, of participants who used the glasses second

#data setup
#here, numpy.nan is preferred to 0 or null to keep the chart clean
wglasses = [numpy.nan, numpy.nan, 3, 4, 2, 5, 3, 2.5]
woglasses = [2, numpy.nan, 1, 4, 3, 3, 1, 3]
x = arange(8)
pnames = ['P2','P3','P5','P6','P10','P12','P14','P16']

#plot the with glasses and then without
plt.scatter(x, wglasses, c='b', label='with glasses')
plt.scatter(x, woglasses, c='r', marker='x', label='without glasses')

#formatting
plt.gca().invert_yaxis()
plt.grid()
plt.axes().set_axisbelow(True)
plt.xticks(arange(8))
plt.axes().set_xticklabels(pnames)
plt.ylabel('Likert Rating')
plt.xlabel('Participants')
plt.title('Participants with Glasses as First Condition')

plt.show()
