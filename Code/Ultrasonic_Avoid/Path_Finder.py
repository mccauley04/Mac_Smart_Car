#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

#Motor Pins

IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

'''Definition of  key'''
key = 8

'''Definition of  ultrasonic module pins'''
EchoPin = 0
TrigPin = 1

'''Definition of RGB module pins'''
LED_R = 22
LED_G = 27
LED_B = 24

'''Definition of servo pin'''
ServoPin = 23

'''Definition of infrared obstacle avoidance module pins'''
AvoidSensorLeft = 12
AvoidSensorRight = 17

'''Set the GPIO port to BCM encoding mode'''
GPIO.setmode(GPIO.BCM)

'''Ignore warning information'''
GPIO.setwarnings(False)

'''
Motor pins are initialized into output mode
Key pin is initialized into input mode
Ultrasonic pin,RGB pin,servo pin initialization
Infrared obstacle avoidance module pin
'''

def init():
    global pwm_ENA
    global pwm_ENB
    global pwm_servo
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(key,GPIO.IN)
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)
    GPIO.setup(AvoidSensorLeft,GPIO.IN)
    GPIO.setup(AvoidSensorRight,GPIO.IN)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)

#Button detection
def key_scan():
    while GPIO.input(key):
        pass
    while not GPIO.input(key):
        time.sleep(0.01)
        if not GPIO.input(key):
            time.sleep(0.01)
            while not GPIO.input(key):
	        pass