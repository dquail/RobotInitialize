import time
from pylab import *
from lib_robotis_hack import *
import threading
import json

"""
Usage:
    from RobotMonitor import *
    start()
"""


class RobotMonitors:
    def __init__(self, sensors):
        self.monitors = []
        index = 1
        for sensor in sensors:
            monitor = RobotMonitor(sensor, index)
            index = index + 1
            self.monitors.append(monitor)

    def start(self):
        while True:
            #tell each monitor to plot a measurement
            for monitor in self.monitors:
                monitor.plotCurrent()
                time.sleep(1)



class RobotMonitor:

    def __init__(self, sensor, figureIndex):
        self.figureIndex = figureIndex

        ion() #Turn interactive on
        plt.figure(figureIndex)
        plotTitle = "Servo " + str(figureIndex)
        suptitle(plotTitle, fontsize=14, fontweight='bold')

        """
        angle
        load
        temperature
        voltage
        """
        self.sensor = sensor
        self.currentMeasurementIndex = 0 #The original x coordinate
        self.visibleMeasurements = 100 #the width of the graph

        self.maxTemperature = 100
        self.minTemperature = -100

        self.maxTorque = 100
        self.minTorque = -100

        self.temperatureMeasurements = [0.0] * self.visibleMeasurements
        self.torqueMeasurements = [0.0] * self.visibleMeasurements
        self.angleMeasurements = [0.0] * self.visibleMeasurements
        self.voltageMeasurements = [0.0] * self.visibleMeasurements


        #Initialize the graph

        x = arange(0, self.visibleMeasurements,1);

        # initial plot
        self.temperatureLine, self.torqueLine, self.angleLine, self.voltageLine, = plot(x, self.temperatureMeasurements, 'r', x, self.torqueMeasurements, 'b', x, self.angleMeasurements, 'g', x, self.voltageMeasurements, 'y')
        self.temperatureLine.axes.set_xlim(0, self.visibleMeasurements)
        self.temperatureLine.axes.set_ylim(self.minTemperature, self.maxTemperature)
        self.temperatureLine.set_label("Temperature")
        self.torqueLine.set_label("Torque")
        self.angleLine.set_label("Angle (X 100)")
        self.voltageLine.set_label("Voltage")
        legend()
        grid()
        draw()


    def plotCurrent(self):
        currentTemperature = currentTorque = currentAngle = currentVoltage = 0

        plt.figure(self.figureIndex)


        #take measurements

        #currentTemperature = currentTemperature + 0.1 #replace with actual
        currentTemperature = self.sensor.read_temperature()
        currentTorque = self.sensor.read_load()
        currentAngle = self.sensor.read_angle() * 100
        currentVoltage = self.sensor.read_voltage()
        """
        #Don't actually pop anything. For display we'll actually just display the last self.visibleMeasurements elements
        #pop the oldest element from temperatureMeasurements, torqueMeasurements (beginning of array)

        """
        #add the newest to end of arrays
        self.temperatureMeasurements.append(currentTemperature)
        self.torqueMeasurements.append(currentTorque)
        self.angleMeasurements.append(currentAngle)
        self.voltageMeasurements.append(currentVoltage)

        self.torqueLine.set_ydata(self.torqueMeasurements[-self.visibleMeasurements:])
        self.temperatureLine.set_ydata(self.temperatureMeasurements[-self.visibleMeasurements:])
        self.angleLine.set_ydata(self.angleMeasurements[-self.visibleMeasurements:])
        self.voltageLine.set_ydata(self.angleMeasurements[-self.visibleMeasurements:])

        draw()

        #plot them

        print("Plotting temp: " + str(currentTemperature) + " current torque: " + str(currentTorque) + " current angle: " + str(currentAngle) + " current voltage: " + str(currentVoltage))

        #write to disk if neccessary (every 10 seconds)
        if self.currentMeasurementIndex % 10 == 0:
            js = {'angles': self.angleMeasurements, 'torques':self.torqueMeasurements, 'temperatures':self.temperatureMeasurements, 'voltages':self.voltageMeasurements}
            filename = str(self.figureIndex) + ".json"

            with open(filename, 'w') as fp:
                json.dump(js, fp)

        self.currentMeasurementIndex += 1

    def start(self):
        currentTemperature = 0
        currentTorque = 0


        #take measurements

        while(True):
            #currentTemperature = currentTemperature + 0.1 #replace with actual
            currentTemperature = self.sensor.read_temperature()
            currentTorque = self.sensor.read_load()

            currentTorque = currentTorque = currentTorque - 0.1 #replace with actual

            """
            #Don't actually pop anything. For display we'll actually just display the last self.visibleMeasurements elements
            #pop the oldest element from temperatureMeasurements, torqueMeasurements (beginning of array)

            """
            #add the newest to end of arrays
            self.temperatureMeasurements.append(currentTemperature)
            self.torqueMeasurements.append(currentTorque)

            self.torqueLine.set_ydata(self.torqueMeasurements[-self.visibleMeasurements:])
            self.temperatureLine.set_ydata(self.temperatureMeasurements[-self.visibleMeasurements:])

            draw()

            #plot them

            print("Plotting temp: " + str(currentTemperature) + " current torque: " + str(currentTorque))
            self.currentMeasurementIndex+=1

            time.sleep(1)
            #threading.Timer(1, self.start).start()



def plotFromFile(filename):
    #Get the data from the file

    with open(filename) as jsonDataFile:
        data = json.load(jsonDataFile)

    voltages = data['voltages']
    print('Voltages: ' + str(voltages))

    temperatures = data['temperatures']
    print('Temperatures: ' + str(temperatures))

    angles = data['angles']
    print('Angles: ' + str(angles))

    torques = data['torques']
    print('Torques: ' + str(torques))

    plt.figure(1)
    plotTitle = "Servo " + str(filename)
    suptitle(plotTitle, fontsize=14, fontweight='bold')
    x = arange(0, len(temperatures), 1)
    print('x: ' + str(x))

    temperatureLine, torqueLine, angleLine, voltageLine, = plot(x, temperatures,'r', x, torques,'b', x, angles, 'g',
                                                                                    x, voltages, 'y')
    temperatureLine.axes.set_xlim(0,len(temperatures))
    temperatureLine.axes.set_ylim(-100, 100)

    temperatureLine.set_label("Temperature")
    torqueLine.set_label("Torque")
    angleLine.set_label("Angle (X 100)")
    voltageLine.set_label("Voltage")
    legend()
    grid()
    draw()
    show()

def start():
    D = USB2Dynamixel_Device(dev_name="/dev/ttyUSB0", baudrate=1000000)

    # Identify servos on the bus (should be only ONE at this point)
    # Should return: "FOUND A SERVO @ ID 1"
    s_list = find_servos(D)

    # Make a servo object for this servo
    s1 = Robotis_Servo(D, s_list[0])

    monitor = RobotMonitor(s1)
    monitor.start()
