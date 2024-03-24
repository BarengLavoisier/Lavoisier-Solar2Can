import BLynklib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import machine
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT1_PIN = 26
DHT2_Pin = 5
DHT3_pin = 22

#define BLYNK_AUTH_TOKEN "I8Gi0XgiBzJTx6soYbZXIV5A8lJK7ijh"
BLYNK_AUTH_TOKEN = "I8Gi0XgiBzJTx6soYbZXIV5A8lJK7ijh"

blynk = Blynklib.Blynk(BLYNK_AUTH_TOKEN)

timer = BlynkTimer

@blynk.on("connected")
def blynk_connected():
    print("Blynk Initiated and Synchronized")
    print("................................")
    print("........Solar2Can Online........")
    time.sleep(2);
    
def DHT1_Data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT1_PIN)
    if humidity is not None and temperature is not None:
        print("TEMP={0:0.1f}C HUMIDITY={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor not detecting, Check wiring");
        
    blynk.virtual_write(0, humidity)
    blynk.virtual_write(1, temperature)
    print("Values updated")

def DHT2_Data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT2_PIN)
    if humidity is not None and temperature is not None:
        print("TEMP={0:0.1f}C HUMIDITY={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor not detecting, Check wiring");
        
    blynk.virtual_write(0, humidity)
    blynk.virtual_write(1, temperature)
    print("Values updated")
    
def DHT3_Data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT3_PIN)
    if humidity is not None and temperature is not None:
        print("TEMP={0:0.1f}C HUMIDITY={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor not detecting, Check wiring");
        
    blynk.virtual_write(0, humidity)
    blynk.virtual_write(1, temperature)
    print("Values updated")

timer.set_interval(2, DHT1_Data)
#timer.set_interval(2, DHT2_Data)
#timer.set_interval(2, DHT3_Data)

while True:
    blynk_connected.run()
    DHT1_Data.run()