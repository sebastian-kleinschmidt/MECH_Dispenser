#import os
#import sys
#sys.path.insert(0, os.getcwd())

from servo import servolib
from pump import pumplib
from scale import scalelib

valve_controller = servolib.ValveController()
pump_controller = pumplib.PumpController()
scale_controller = scalelib.ScaleController(5,6)

valve_controller.demo()
pump_controller.demo()

scalelib.demo()
