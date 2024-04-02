from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

def capture_image():
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
    picam2.configure(camera_config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file("./Cam-Input/test.png")
    time.sleep(1)
    picam2.stop()