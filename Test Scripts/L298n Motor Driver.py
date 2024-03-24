en_a = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(en_a, GPIO.OUT)
    
power_a = GPIO.PWM(en_a, 100)
power_a.start(25)

GPIO.output(19, GPIO.HIGH)