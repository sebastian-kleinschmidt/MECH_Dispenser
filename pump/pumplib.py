import time
import RPi.GPIO as GPIO

class PumpController():
    def __init__(self):
        GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
        self.RELAIS_1_GPIO = 6
        self.RELAIS_2_GPIO = 13

        GPIO.setup(self.RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
        GPIO.setup(self.RELAIS_2_GPIO, GPIO.OUT)

        GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH)
        GPIO.output(self.RELAIS_2_GPIO, GPIO.HIGH)

    def toggle_pump(state):
        if state == True:
            GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH)
            GPIO.output(self.RELAIS_2_GPIO, GPIO.HIGH)
        else:
            GPIO.output(self.RELAIS_1_GPIO, GPIO.LOW)
            GPIO.output(self.RELAIS_2_GPIO, GPIO.LOW)

    def demo(self):
        GPIO.output(self.RELAIS_1_GPIO, GPIO.LOW) # aus
        time.sleep(5)
        GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH) # an
        time.sleep(5)
        GPIO.output(self.RELAIS_1_GPIO, GPIO.LOW) # aus

        GPIO.output(self.RELAIS_2_GPIO, GPIO.LOW) # aus
        time.sleep(5)
        GPIO.output(self.RELAIS_2_GPIO, GPIO.HIGH) # an
        time.sleep(5)
        GPIO.output(self.RELAIS_2_GPIO, GPIO.LOW) # aus

	GPIO.cleanup()
