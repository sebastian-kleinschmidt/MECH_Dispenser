import Adafruit_PCA9685
import time
import math

def angle_to_pulse(angle):
	pulse = angle*((512.0-102.0)/180.0)+102.0
	return int(pulse)

def valve(id, open, config):
	pwm.set_pwm(id,0,config[id][int(open)])

pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)

config = []
config.append([angle_to_pulse(110),angle_to_pulse(20)])
config.append([angle_to_pulse(20),angle_to_pulse(110)])
config.append([angle_to_pulse(20),angle_to_pulse(120)])

for i in range(3):
	#Set to 0 degree
	pwm.set_pwm(i,0,config[i][0])
	time.sleep(2)
	#Set to 180 degree
	pwm.set_pwm(i,0,config[i][1])
	time.sleep(2)

valve(0, False, config)
time.sleep(2)
valve(1, False, config)
time.sleep(2)
valve(2, False, config)
