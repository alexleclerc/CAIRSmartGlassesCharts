import matplotlib.pyplot as plt
import numpy
from numpy.ma import arange

#in a perfect world this would take a text or csv file but we don't live there so its hard coded.
wglassesEasiness = [numpy.nan, 3.5, 5, numpy.nan, 4, 2, 3, 4, 2, 2, 5, 2.5, 3, 2, 2.5, 1]
wglassesNotes = [0,85,34,0,64,156,61,20,70,102,57,89,40,8,77,62]
woglassesNotes = [17,0,54,0,84,203,96,56,132,149,30,51,57,19,122,88]
pnames = ['P1','P2','P3','P4','P5','P6','P7','P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14','P15','P16']
#0-15 x ticks, using arange instead of range because matplotlib likes floats
x = arange(16)

#Plot with glasses and without glasses
plt.scatter(x, wglassesNotes, label='with glasses')
plt.scatter(x, woglassesNotes, marker='x', label ='without glasses')


#formatting
plt.axes().set_axisbelow(True)
plt.xticks(x)
plt.axes().set_xticklabels(pnames)

plt.title('Comparison of Words Written With and Without Glasses')
plt.ylabel('Number of Words Written')
plt.xlabel('Participant ID')
plt.show()