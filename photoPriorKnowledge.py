import matplotlib.pyplot as plt
import numpy as np

overexposure = [2,1,2,4,4,4,2,1,2,1,5,4,4,2,2,3,1]
confidence = [1,4,3,3,5,4,4,1,1,1,4,4,2,4,3,3,1]
frequent = [5,3,3,2,4,2,3,2,1,1,1,3,4,5,2,1,4]

#a list of the lists above, to easier plot our boxes next to each other.
presession = [overexposure, confidence, frequent]

#set up an instance of a figure, with a plot inside it
fig = plt.figure(1,figsize=(9,6))
ax = fig.add_subplot(111)

boxplt = ax.boxplot(presession)

#***formatting***

#if you don't do this, with this small range, matplotlib will
#try to put a tick and every half (.5) mark
ax.yaxis.set_ticks(np.arange(1, 6, 1.0))
ax.yaxis.grid(linestyle='dotted')
ax.set_axisbelow(True)

#label names
qnames = ['Overexposure', 'Confidence with Cameras', 'Use Frequency']
ax.set_xticklabels(qnames)
ax.set_title('Prior Knowledge Ratings: Photography')
ax.set_ylabel('Likert Scale - Topic Familiarity')
ax.set_xlabel('Question Topic')

plt.show()