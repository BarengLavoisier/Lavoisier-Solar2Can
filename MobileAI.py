import os
import glob
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
import shutil
import unicodedata

# Configuration (move these outside functions)
IMG_FOLDER_PATH = "./Cam-Input/"
OUTPUT_FOLDERS = {
    'Biodegradable': './Data-Out/Biodegradable/',
    'Non-Biodegradable': './Data-Out/Non-Biodegradable/',
    'Other Waste': './Data-Out/Other Waste/'
}
CLASS_LABELS = ['Biodegradable', 'Non-Biodegradable', 'Other Waste']


def load_waste_classification_model():
    """Loads the pre-trained waste classification model."""
    return load_model('./AI-Model/Solar2Can.keras')


def classify_waste(img):
    """
    Classifies a waste image using the pre-trained model.

    Args:
        img: The image to classify (as a PIL image object).

    Returns:
        A tuple containing the predicted class label and confidence score.
    """
    model = load_waste_classification_model()  # Load model on first call

    x = image.img_to_array(img)
    x = preprocess_input(x, data_format='channels_last')
    x = np.expand_dims(x, axis=0)

    predictions = model.predict(x)
    highest_pred_index = np.argmax(predictions)
    highest_pred_label = CLASS_LABELS[highest_pred_index]
    confidence = predictions[0][highest_pred_index]

    return highest_pred_label, confidence


def normalize_filename(filename):
    """
    Normalizes a filename by removing special characters.

    Args:
        filename: The filename to normalize.

    Returns:
        The normalized filename.
    """
    normalized_filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('utf-8')
    return normalized_filename


def classify_images_in_folder():
    """
    Classifies images in a folder and moves them to respective output folders.

    Logs messages and handles errors during processing.
    """
    import logging

    logging.basicConfig(level=logging.INFO)

    # Get all image files in the folder
    image_files = glob.glob(f"{IMG_FOLDER_PATH}*.jpg")

    for image_path in image_files:
        try:
            # Load the image as a PIL object
            img = image.load_img(image_path, target_size=(224, 224))

            label, confidence = classify_waste(img)
            output_folder = OUTPUT_FOLDERS[label]

            normalized_filename, ext = os.path.splitext(normalize_filename(image_path.split("/")[-1]))  # Extract filename and extension

            # Guard for filename collisions
            i = 1
            new_img_file = f"{normalized_filename}_{i}{ext}"
            while os.path.exists(f"{output_folder}/{new_img_file}"):
                i += 1
                new_img_file = f"{normalized_filename}_{i}{ext}"

            # Move the image to the output folder
            shutil.move(image_path, f"{output_folder}/{new_img_file}")
            logging.info(f"{label}: {confidence*100:.2f}%")
        except (UnicodeEncodeError, FileNotFoundError) as e:
            logging.error(f"Error processing image {image_path}: {e}")


if __name__ == "__main__":
    classify_images_in_folder()
