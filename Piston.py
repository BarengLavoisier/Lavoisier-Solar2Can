import RPI.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
    
def piston_Push():
    GPIO.output(18, 1)
    time.sleep(1)
    GPIO.output(18, 0)