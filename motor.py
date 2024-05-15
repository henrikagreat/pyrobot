import RPi.GPIO as GPIO 

class Motor():
    def __init__(self): 
        self.pin_a = 14
        self.pin_b = 15
        self.pin_c = 18
        self.pin_d = 23

        GPIO.setwarnings(False) 
        GPIO.setmode(GPIO.BCM) 

        GPIO.setup(self.pin_a, GPIO.OUT)
        GPIO.setup(self.pin_b, GPIO.OUT)
        GPIO.setup(self.pin_c, GPIO.OUT)
        GPIO.setup(self.pin_d, GPIO.OUT)
    
    def left_forward(self):
        GPIO.output(self.pin_a, True)
        GPIO.output(self.pin_b, False)
    
    def left_reverse(self):
        GPIO.output(self.pin_a, False)
        GPIO.output(self.pin_b, True)
    
    def right_forward(self):
        GPIO.output(self.pin_c, True)
        GPIO.output(self.pin_d, False)
    
    def right_reverse(self):
        GPIO.output(self.pin_c, False)
        GPIO.output(self.pin_d, True)
    
    def stop(self):
        GPIO.output(self.pin_a, False)
        GPIO.output(self.pin_b, False)
        GPIO.output(self.pin_c, False)
        GPIO.output(self.pin_d, False)
    
    def forward(self):
        self.right_forward()
        self.left_forward()

    def reverse(self):
        self.right_reverse()
        self.left_reverse()    
    
    def turn_left(self):
        self.left_reverse()
        self.right_forward()
    
    def turn_right(self):
        self.left_forward()
        self.right_reverse()

    def __del__(self):
        GPIO.cleanup() # this ensures a clean exit  
