#Libraries
import RPi.GPIO as GPIO
import time
import picamera
 
def distance():
    # set Trigger to HIGH
    import time
    GPIO.output(18, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(18, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(24) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(24) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
   
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)
 
    #set GPIO Pins
    GPIO_TRIGGER = 18
    GPIO_ECHO = 24
 
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    camera = picamera.PiCamera()
    servo_pin = 21
    GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin
    p = GPIO.PWM(servo_pin, 50)  
 
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            if dist < 10:
               exec(open("classify_original.py").read())
               #GPIO Mode (BOARD / BCM)
               #GPIO.setmode(GPIO.BCM)
               
               #set GPIO Pins
               #GPIO_TRIGGER = 18
               #GPIO_ECHO = 24

               #set GPIO direction (IN / OUT)
               #GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
               #GPIO.setup(GPIO_ECHO, GPIO.IN)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
