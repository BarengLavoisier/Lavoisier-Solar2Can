#To Implement Sleep Function
import time

#The Temp and Humid Sensor
import adafruit_dht

#Pin references for the RPI0
import board

#RPI0 Servo Control
from gpiozero import Servo

#For the l298N
import RPi.GPIO as GPIO

#Liquid Crystal Dusplay or LCD for RPI0
import Adafruit_CharLCD as LCD

# RPI0 LCD pin setup
lcd_rs        = 25 
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 26
lcd_d6        = 27
lcd_d7        = 28
lcd_backlight = 4
lcd_columns   = 16
lcd_rows      = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#DHT Pin
dht_device = adafruit_dht.DHT11(board.D3)

#Servo
factory = PiGPIOFactory()
servo = Servo(14, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

angle = 10

#IR Sensor
sensor_pin = 13
led_pin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

def IRread():
    try:
        while True:
            if GPIO.input(sensor_pin):
                # If no object is near
                GPIO.output(led_pin, False)
                while GPIO.input(sensor_pin):
                    time.sleep(0.2)
            else:
                # If an object is detected
                GPIO.output(led_pin, True)
    except KeyboardInterrupt:
        GPIO.cleanup()

#Check Temps and Humidity        
def DHTcheck():
    while True:
        try:
            temperature_c = dht_device.temperature
            temperature_f = temperature_c * (9 / 5) + 32

            humidity = dht_device.humidity

            print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
        except RuntimeError as err:
            print(err.args[0])

        time.sleep(2.0)

#Print Message to LCD    
def LCDdisplay():
    lcd.message('Setup Ready!')
    time.sleep(5.0)
    lcd.clear()

#L298n pins
en_a = 9

def motot_init():    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(en_a, GPIO.OUT)
    
    power_a = GPIO.PWM(en_a, 100)
    power_a.start(50)

#L298n move Motors
def forward(sec):
    init()
    GPIO.output(7, False)
    GPIO.output(8, True)
    
GPI.output(led_pin, GPIO,HIGH)