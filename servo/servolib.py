import Adafruit_PCA9685
import time
import math

class ValveController():
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(50)
        self.config = []
        self.config.append([angle_to_pulse(110),angle_to_pulse(20)])
        self.config.append([angle_to_pulse(20),angle_to_pulse(110)])
        self.config.append([angle_to_pulse(20),angle_to_pulse(120)])
    
    def angle_to_pulse(angle):
        pulse = angle*((512.0-102.0)/180.0)+102.0
        return int(pulse)

    def toggle_valve(id, open, config):
        self.pwm.set_pwm(id,0,self.config[id][int(open)])

    def demo():
        for i in range(3):
            #Set to 0 degree
            self.pwm.set_pwm(i,0,self.config[i][0])
            time.sleep(2)
            #Set to 180 degree
            self.pwm.set_pwm(i,0,self.config[i][1])
            time.sleep(2)

    toggle_valve(0, False, config)
    time.sleep(2)
    toggle_valve(1, False, config)
    time.sleep(2)
    toggle_valve(2, False, config)
