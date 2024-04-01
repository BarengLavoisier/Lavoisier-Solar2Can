#AI MobileNetV2
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
import shutil

import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

img_path = "./Cam-Input"

output_folders = {
    'Biodegradable': './Data-Out/Biodegradable',
    'Non-Biodegradable': './Data-Out/Non-Biodegradable',
    'Other Waste': './Data-Out/Other Waste'
}

# Load the pre-trained model
model = load_model('./AI-MOdel/Solar2Can.keras')

class_labels = ['Biodegradable', 'Non-Biodegradable', 'Other Waste']

def classify_Waste(img_path):
  img = image.load_img(img_path, target_size=(224, 224))  # Resize image

  # Preprocess the image for the model
  x = image.img_to_array(img)
  x = preprocess_input(x, data_format='channels_last')
  x = np.expand_dims(x, axis=0)  # Add batch dimension

  # Make predictions
  predictions = model.predict(x)

  # Get the index of the highest prediction
  highest_pred_index = np.argmax(predictions)
  
  highest_pred_label = class_labels[highest_pred_index]

  # Get the corresponding class label
  return highest_pred_label, predictions[0][highest_pred_index]

def classify_images_in_folder(folder_path):
    for img_file in os.listdir(folder_path):
        if img_file.endswith('.jpg'):  # Check for .jpg files
            img_path = os.path.join(folder_path, img_file)
            label, confidence = classify_waste(img_path)
            output_folder = output_folders[label]
            shutil.move(img_path, os.path.join(output_folder, img_file))
            lcd.write_string(f"{label}: {confidence*100:.2f}%")
            lcd.crlf()