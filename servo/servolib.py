import Adafruit_PCA9685
import time
import math

class ValveController():
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(50)
        self.config = []
        self.config.append([self.angle_to_pulse(110),self.angle_to_pulse(20)])
        self.config.append([self.angle_to_pulse(20),self.angle_to_pulse(110)])
        self.config.append([self.angle_to_pulse(20),self.angle_to_pulse(120)])
        self.config.append([self.angle_to_pulse(90),self.angle_to_pulse(180)])
        self.config.append([self.angle_to_pulse(70),self.angle_to_pulse(160)])
        self.config.append([self.angle_to_pulse(110),self.angle_to_pulse(200)])
    @staticmethod
    def angle_to_pulse(angle):
        pulse = angle*((512.0-102.0)/180.0)+102.0
        return int(pulse)
    @staticmethod
    def toggle_valve(self,id, open, config):
        self.pwm.set_pwm(id,0,self.config[id][int(open)])

    def demo(self):
        for i in range(6):
            #Set to 0 degree
            self.pwm.set_pwm(i,0,self.config[i][0])
            time.sleep(2)
            #Set to 180 degree
            self.pwm.set_pwm(i,0,self.config[i][1])
            time.sleep(2)

    	self.toggle_valve(self, 0, False, self.config)
    	time.sleep(2)
    	self.toggle_valve(self, 1, False, self.config)
    	time.sleep(2)
    	self.toggle_valve(self, 2, False, self.config)
    	time.sleep(2)
    	self.toggle_valve(self, 3, False, self.config)
    	time.sleep(2)
    	self.toggle_valve(self, 4, False, self.config)
    	time.sleep(2)
    	self.toggle_valve(self, 5, False, self.config)
