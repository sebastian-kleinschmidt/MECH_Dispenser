import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 13
RELAIS_2_GPIO = 6

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)

GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
time.sleep(5)
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an
time.sleep(5)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus

GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # aus
time.sleep(5)
GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # an
time.sleep(5)
GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # aus

GPIO.cleanup() 
