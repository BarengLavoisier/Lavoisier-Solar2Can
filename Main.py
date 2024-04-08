import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD
import os
import time
import Conveyer, rpiCamera, MobileAI
import asyncio

#LCD 2x16
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

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
  while True:
    cam_Sense = GPIO.input(Camsensor_pin)

    if cam_Sense == 0:
      lcd.clear()
      rpiCamera.capture_image()
      time.sleep(5)
    else:
      lcd.write_string("Place Trash Here")

def Start_LCD():
  lcd.cursor_pos = (0, 0)
  lcd.write_string('Solar2Can')
  lcd.cursor_pos = (1, 0)
  lcd.write_string("by Group 4")
  time.sleep(5)
  lcd.clear

async def main():
  Start_LCD()
  time.sleep(5)

try:
  asyncio.run(main())
except KeyboardInterrupt:
  print("Quit")
  GPIO.cleanup()
