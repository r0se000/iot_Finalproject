import RPi.GPIO as GPIO
import time

def LED(hum):
    if 60<hum: #red
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18,True)

    if hum<40: #yellow
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23,GPIO.OUT)
        GPIO.output(23,True)

    if 40<hum<60: # Green
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24,GPIO.OUT)
        GPIO.output(24,True)
