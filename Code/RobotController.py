# 1) Plug in power to the robot's barrell connector
# 2) Plug the USB2Dynamixel (set to TTL) into the USB port of your computer
# 3a) Plug the cable into the proximal servo; make sure only *one* servo is connected to the USB2Dynamixel
# 3b) Plug in servo cable to USB2Dynamixel
# 4) Initialize and try out the first servo as follows

"""
Usage: from RobotController import *
start()
"""

from lib_robotis_hack import *
import threading
from RobotMonitor import *
import random

class RobotController:
    def __init__(self, servo):
        self.secondsAllowedPerAction = 3
        #Do the initialization
        self.servo = servo

    def start(self):
        #Start a loop where an action is taken every interval (time based) based on the policy

        desiredAngle = self.policy()
        try:
            self.servo.move_angle(desiredAngle)

        except:
            print("!!!!!! Error moving servo")
            pass

        threading.Timer(self.secondsAllowedPerAction, self.start).start()

    def policy(self):
        #Rturn the angle to go to
        angle = random.uniform(0.0, 1.0)
        return angle

def startTest():
    D = USB2Dynamixel_Device(dev_name="/dev/ttyUSB0", baudrate=1000000)

    # Identify servos on the bus (should be only ONE at this point)
    # Should return: "FOUND A SERVO @ ID 1"
    s_list = find_servos(D)

    # Make a servo object for this servo
    s1 = Robotis_Servo(D, s_list[0])
    s2 = Robotis_Servo(D, s_list[1])

    print("Creating rc1")
    rc1 = RobotController(s1)
    print("Creatoing rc2")
    rc2 = RobotController(s2)

    print("Starting rc1")
    rc1.start()

    print("Starting rc2")
    rc2.start()

    print("Creating monitors")
    monitors = RobotMonitors([s1, s2])
    print("Starting monitors")
    monitors.start()



    print("Initialized s1 and s2")