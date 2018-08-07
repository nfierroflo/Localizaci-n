import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
o1=(0,0)
circle1 = plt.Circle(o1, 1,alpha=0.5,lw=1, color='r')
circle2 = plt.Circle((0.5, 0.5), 1,alpha=0.5,lw=1, color='g')
circle3 = plt.Circle((1, 0), 1, alpha=0.5, lw=1,edgecolor='#000000')
point=plt.Circle((1, 0), 0.1, alpha=1, lw=1,color='#000000')
fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()
ax = plt.axes()
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(point)
ax.set_xlim((-5, 5))
ax.set_ylim((-5, 5))
plt.show()
#fig.savefig('plotcircles.png')