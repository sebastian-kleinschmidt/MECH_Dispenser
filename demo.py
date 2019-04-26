#import os
#import sys
#sys.path.insert(0, os.getcwd())

from servo import servolib
from pump import pumplib

valve_controller = servolib.ValveController()
pump_controller = pumplib.PumpController()

valve_controller.demo()
pump_controller.demo()

