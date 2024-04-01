import os
import picamera
import time

camera = picamera.PiCamera()

base_name = "Sample"

def capture_image(base_name, folder_path):
    # Find the next available file name
    index = 0
    while True:
        file_name = f"{base_name}{index}.jpg" if index else f"{base_name}.jpg"
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            break
        index += 1
    
    # Capture the image
    camera.start_preview()
    sleep(3)  # Camera warm-up time
    camera.capture(file_path)
    camera.stop_preview()
    return file_name