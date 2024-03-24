import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD
import os
import time
import Conveyer
import Blynk_DHT11
import IRSensor
import rpiCamera

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

#AI MobileNetV2
import os
from datetime import datetime
import numpy as np
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions

# Load the pre-trained model
#model = MobileNet(weights='imagenet')

# Load your image
#img_path = "C:/Users/Great/Segregation AI/MobileNetV1 AI/dataset-resized/paper/paper2.jpg"
#img = image.load_img(img_path, target_size=(224, 224))  # Resize image

# Preprocess the image for the model
#x = image.img_to_array(img)
#x = preprocess_input(x)
#x = np.expand_dims(x, axis=0)  # Add batch dimension

# Make predictions
#predictions = model.predict(x)
# Decode predictions
#decoded_preds = decode_predictions(predictions, top=3)[0]

# Print top 3 predictions
#for pred in decoded_preds:
    #print(f"Class: {pred[1]} ({pred[2]*100:.2f}%)")

async def main():
  Start_LCD()
  Blynk_DHT11.blynk_connected()
  time.sleep(5)
  
  #try:
  #  IR_Sensor.Sensor_1()
  #  IR_Sensor.Sensor_2()
  #  IR_Sensor.Sensor_3()
  #except KeyboardInterrupt:
  #  GPIO.cleanup()

