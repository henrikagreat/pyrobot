import RPi.GPIO as GPIO 

class Motor():
    def __init__(self):

        GPIO.setwarnings(False) 
 
        pin_a = 14
        pin_b = 15
        pin_c = 18
        pin_d = 23

        a = True
        b = False
        c = True
        d = False

        GPIO.setmode(GPIO.BCM) 

        GPIO.setup(pin_a, GPIO.OUT)
        GPIO.setup(pin_b, GPIO.OUT)
        GPIO.setup(pin_c, GPIO.OUT)
        GPIO.setup(pin_d, GPIO.OUT)
    
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
    
    def run_forward(self):
        self.right_forward()
        self.left_forward()

    def run_reverse(self):
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
