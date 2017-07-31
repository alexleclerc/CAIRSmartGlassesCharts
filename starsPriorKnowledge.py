import matplotlib.pyplot as plt
import numpy as np

#boxplot of photography prior knowledge based on responses from pre-session questionnaire

#data (hard coded is not ideal, but we have a small sample)
milkyway = [3,5,5,3,4,5,1,3,4,2,5,2,4,5,1,3,2]
sevensisters = [1,3,2,1,2,1,1,1,2,1,2,2,1,2,1,1,1]
nasa = [1,5,4,1,4,3,1,1,1,1,2,1,2,1,1,2,1]
moon = [1,2,5,1,3,5,1,1,1,1,5,1,1,1,1,3,1]
galaxies = [1,3,3,1,4,2,1,1,1,1,4,1,1,1,1,3,1]

#a list of the lists above, to easier plot our boxes next to each other.
presession = [milkyway, sevensisters, nasa, moon, galaxies]

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
qnames = ['Milkyway', 'Seven Sisters', 'NASA', 'Moon', 'Galaxies']
ax.set_xticklabels(qnames)
ax.set_title('Prior Knowledge Ratings: Stars')
ax.set_ylabel('Likert Scale - Topic Familiarity')
ax.set_xlabel('Question Topic')

plt.show()
