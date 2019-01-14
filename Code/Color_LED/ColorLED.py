# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Definition of RGB module pin
LED_R = 22
LED_G = 27
LED_B = 24

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#Definition of Ultrasonic Module Pins
EchoPin = 0
TrigPin = 1

#Definition of servo pin
ServoPin = 23

#RGB pins are initialized into output mode
global pwm_ENA
global pwm_ENB
global pwm_servo
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(ServoPin, GPIO.OUT)
pwm_servo = GPIO.PWM(ServoPin, 50)
pwm_servo.start(0)


#The servo rotates to the specified angle
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)


#Display 7 color LED
try:
    while True:
        # Red for 1 Second
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        servo_appointed_detection(0)
        time.sleep(1)


        # Green for 1 Second
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        servo_appointed_detection(180)
        time.sleep(1)


        # Blue for 1 Second
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        servo_appointed_detection(90)
        time.sleep(1)

except:
    print "except"


GPIO.cleanup()
