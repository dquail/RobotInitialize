import numpy as np
import matplotlib.pyplot as plt

graphWidth = 100
graphHeight = 1

plt.axis([0, graphWidth, 0, graphHeight])
plt.ion()

i = 0

fig = plt.figure(1)
fig.suptitle('Bandit', fontsize=14, fontweight='bold')
ax = fig.add_subplot(211)
titleLabel = "Optimistic Greedy (stationary vs. non)"
ax.set_title(titleLabel)
ax.set_xlabel('Step/Pull')
ax.set_ylabel('Average reward')

#ax.plot(optimalActionsStationary)

#ax.plot(optimalActionsNonStationary)
#plt.show()

while True:
    i+=1
    y = np.random.random()
    """
    if i == 50:
        plt.axis([25, 125, 0, 1])
    plt.scatter(i, y)

    plt.pause(0.15)

    """
    ax.plot()

while True:
    plt.pause(0.05)