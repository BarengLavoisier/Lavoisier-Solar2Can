import picamera
import time

camera = picamera.PiCamera()

def take_Pic():
    camera.start_preview()
    time.sleep(5)
    camera.capture()
    camera.stop_preview()