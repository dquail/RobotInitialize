import time
from pylab import *

ion() # turn interactive mode on

# initial data
x = arange(-8, 8, 0.1);
y1 = sin(x)
y2 = cos(x)

# initial plot
line1, line2, = plot(x, y1, 'r', x, y2, 'b')
line1.axes.set_xlim(-10, 10)
line1.axes.set_ylim(-2, 2)
line1.set_label("line1")
line2.set_label("line2")
legend()
grid()
draw()

# update line 1
for i in xrange(50):
    print("In first")
    time.sleep(0.1)

    # update data
    y1 = sin(x + float(i) / 10)

    # update plot
    line1.set_ydata(y1)
    draw()

# update line 2
for i in xrange(50):
    print("In second")
    time.sleep(0.1)

    # update data
    y2 = cos(x + float(i) / 10)
    #y2 = [0.0 + i/50] *160
    # update plot
    line2.set_ydata(y2)
    draw()