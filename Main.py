import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD
import os
import time
from ScriptLibs import Conveyer, IRSensor, MobileAI

#LCD 2x16
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

def Start_LCD():
  lcd.cursor_pos = (0, 0)
  lcd.write_string('Solar2Can')
  lcd.cursor_pos = (1, 0)
  lcd.write_string("A project by Group 4")
  time.sleep(5)
  lcd.clear

async def main():
  Start_LCD()
  time.sleep(5)
  IRSensor.Cam_SensorDetect()

