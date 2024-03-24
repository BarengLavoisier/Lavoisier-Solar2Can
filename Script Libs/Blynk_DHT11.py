import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import board
import adafruit_dht
import time
import main

DHT_SENSOR1 = adafruit_dht.DHT11(board.D26)
DHT_SENSOR2 = adafruit_dht.DHT11(board.D5)
DHT_SENSOR3 = adafruit_dht.DHT11(board.D22)

#define BLYNK_AUTH_TOKEN "I8Gi0XgiBzJTx6soYbZXIV5A8lJK7ijh"
BLYNK_AUTH_TOKEN = "I8Gi0XgiBzJTx6soYbZXIV5A8lJK7ijh"

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

timer = BlynkTimer

@blynk.on("connected")
def blynk_connected():
    main.lcd.cursor_pos = (0, 0)
    print("Blynk Initiated and Synchronized")
    main.lcd.write_string('Blynk Initiated')
    main.lcd.cursor_pos = (1, 0)
    print("Solar2Can Online")
    print("................................")
    print("........Solar2Can Online........")
    time.sleep(4)
    main.lcd.clear()
    
def DHT1_Data():
    temperature = DHT_SENSOR1.temperature
    humidity = DHT_SENSOR1.humidity
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
        
    blynk.virtual_write(2, humidity)
    blynk.virtual_write(3, temperature)
    print("Values updated")
    
def DHT3_Data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT3_PIN)
    if humidity is not None and temperature is not None:
        print("TEMP={0:0.1f}C HUMIDITY={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor not detecting, Check wiring");
        
    blynk.virtual_write(4, humidity)
    blynk.virtual_write(5, temperature)
    print("Values updated")

timer.set_interval(2, DHT1_Data)
#timer.set_interval(2, DHT2_Data)
#timer.set_interval(2, DHT3_Data)