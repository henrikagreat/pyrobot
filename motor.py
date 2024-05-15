import RPi.GPIO as GPIO 
from time import sleep

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

def run(direction):
    if direction==1:
        GPIO.output(pin_a, a) #left forward
        GPIO.output(pin_b, b) #left reverse
        GPIO.output(pin_c, c) #right forward
        GPIO.output(pin_d, d) #right reverse
    else:
        GPIO.output(pin_a, not a) #left forward
        GPIO.output(pin_b, not b) #left reverse
        GPIO.output(pin_c, not c) #right forward
        GPIO.output(pin_d, not d) #right reverse

def stop():
    GPIO.output(pin_a, False)
    GPIO.output(pin_b, False)
    GPIO.output(pin_c, False)
    GPIO.output(pin_d, False)
    
    GPIO.cleanup() # this ensures a clean exit  

def main():
    direction=1
    try:  
        while True:
            direction=1-direction
            
            run(direction)
            
            sleep(1)
      
    except:  
        # this catches ALL other exceptions including errors.  
        # You won't get any error messages for debugging  
        # so only use it once your code is working  
        print("Other error or exception occurred!")
      
    finally:
        stop()

if __name__=="__main__":
    main()
