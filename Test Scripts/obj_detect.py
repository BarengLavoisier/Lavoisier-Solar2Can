import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

# Define sensor and LED pins (modify as needed)
sensor_pin = 23
led_pin = 24

in1 = 25
in2 = 8

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

try:
  while True:
    # Read sensor data
    sensor_data = GPIO.input(sensor_pin)

    # If object detected, turn on LED (adjust logic as needed)
    if sensor_data == 0:
      GPIO.output(led_pin, GPIO.HIGH)
      print("Object detected!", end = "\r")
      lcd.write_string('Object Detected')
      GPIO.output(in1, GPIO.HIGH)
    else:
      GPIO.output(led_pin, GPIO.LOW)
      print("", end = "\r")
      lcd.clear()
      GPIO.output(in1, GPIO.LOW)

    # Delay between readings

except KeyboardInterrupt:
  # Clean up GPIO on exit
  GPIO.cleanup()