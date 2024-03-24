import RPi.GPIO as GPIO
import time
import Piston

#IR Sensor Pins
sensor_pin1 = 23
led_pin1 = 24

sensor_pin2 = 25
led_pin2 = 8

sensor_pin3 = 7
led_pin3 = 12

Camsensor_pin = 16
Cam_led_pin = 20

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setup(sensor_pin1, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(sensor_pin2, GPIO.IN)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(sensor_pin3, GPIO.IN)
GPIO.setup(led_pin3, GPIO.OUT)
GPIO.setup(Camsensor_pin, GPIO.IN)
GPIO.setup(Cam_led_pin, GPIO.OUT)

def Sensor_1():
  while True:
    sensor_data1 = GPIO.input(sensor_pin1)

    if sensor_data1 == 0:
      GPIO.output(led_pin1, GPIO.HIGH)
      Piston.piston_Push()
      print("Object detected!", end = "\r")
      lcd.write_string('Biodegradable')
    else:
      GPIO.output(led_pin1, GPIO.LOW)
      print("", end = "\r")
      lcd.clear()
      
def Sensor_2():
  while True:
    sensor_data2 = GPIO.input(sensor_pin2)

    if sensor_data2 == 0:
      GPIO.output(led_pin2, GPIO.HIGH)
      Piston.piston_Push()
      print("Biodegradable", end = "\r")
      lcd.write_string('Non-Biodegradable')
    else:
      GPIO.output(led_pin2, GPIO.LOW)
      print("", end = "\r")
      lcd.clear()

def Sensor_3():
  while True:
    sensor_data3 = GPIO.input(sensor_pin3)

    if sensor_data3 == 0:
      GPIO.output(led_pin3, GPIO.HIGH)
      Piston.piston_Push()
      print("Biodegradable", end = "\r")
      lcd.write_string('Other Waste')
    else:
      GPIO.output(led_pin3, GPIO.LOW)
      print("", end = "\r")
      lcd.clear()
      
def Cam_SensorDetect():
  pass
