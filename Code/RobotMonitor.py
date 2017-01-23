import time
from pylab import *

class RobotMonitor:

    def __init__(self, sensors):

        ion() #Turn interactive on
        """
        angle
        load
        temperature
        voltage
        """
        self.sensors = sensors
        self.currentMeasurementIndex = 0 #The original x coordinate
        self.visibleMeasurements = 100 #the width of the graph

        self.maxTemperature = 100
        self.minTemperature = -100

        self.maxTorque = 100
        self.minTorque = -100

        self.temperatureMeasurements = [0.0] * self.visibleMeasurements
        self.torqueMeasurements = [0.0] * self.visibleMeasurements

        #Initialize the graph

        x = arange(0, self.visibleMeasurements,1);

        # initial plot
        self.temperatureLine, self.torqueLine, = plot(x, self.temperatureMeasurements, 'r', x, self.torqueMeasurements, 'b')
        self.temperatureLine.axes.set_xlim(0, self.visibleMeasurements)
        self.temperatureLine.axes.set_ylim(self.minTemperature, self.maxTemperature)
        self.temperatureLine.set_label("Temperature")
        self.torqueLine.set_label("Torque")
        legend()
        grid()
        draw()



    def startMonitoring(self):
        currentTemperature = 0
        currentTorque = 0

        while True:

            #take measurements

            currentTemperature = currentTemperature + 0.1 #replace with actual
            currentTorque = currentTorque = currentTorque - 0.1 #replace with actual

            #pop the oldest element from temperatureMeasurements, torqueMeasurements (beginning of array)
            self.temperatureMeasurements.pop(0)
            self.torqueMeasurements.pop(0)

            #add the newest to end of arrays
            self.temperatureMeasurements.append(currentTemperature)
            self.torqueMeasurements.append(currentTorque)

            self.torqueLine.set_ydata(self.torqueMeasurements)
            self.temperatureLine.set_ydata(self.temperatureMeasurements)
            draw()

            #plot them

            time.sleep(1)
            self.currentMeasurementIndex+=1





