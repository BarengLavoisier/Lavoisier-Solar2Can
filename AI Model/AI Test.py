import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions

# Load the pre-trained model
model = MobileNetV2(weights='imagenet')

# Load your image
img_path = "C:/Users/Great/MobileNetV1 AI/dataset-resized/trash/trash8.jpg"
img = image.load_img(img_path, target_size=(224, 224))  # Resize image

# Preprocess the image for the model
x = image.img_to_array(img)
x = preprocess_input(x, data_format='channels_last')
x = np.expand_dims(x, axis=0)  # Add batch dimension

# Make predictions
predictions = model.predict(x)

# Decode predictions, extracting only the highest match
top_1_pred = decode_predictions(predictions, top=1)[0][0]

# Print the highest match
print(f"Highest Match: {top_1_pred[1]} ({top_1_pred[2]*100:.2f}%)")