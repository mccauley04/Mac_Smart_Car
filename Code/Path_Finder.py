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

def pre_check():
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
    '''Set the PWM pin and frequency is 2000hz'''
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

pwm_servo = GPIO.PWM(ServoPin, 50)
pwm_servo.start(0)

''' Button detection '''
def key_scan():
    while GPIO.input(key):
        pass
    while not GPIO.input(key):
        time.sleep(0.01)
        if not GPIO.input(key):
            time.sleep(0.01)
            while not GPIO.input(key):
	        pass


''' Ultrasonic function '''
def Distance_test():
    GPIO.output(TrigPin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin, GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    print
    "distance is %d " % (((t2 - t1) * 340 / 2) * 100)
    time.sleep(0.01)
    return ((t2 - t1) * 340 / 2) * 100

'''The servo rotates to the specified angle'''
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)


def servo_color_carstate():
    ''' RED LIGHT '''
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    back(20, 20)
    time.sleep(0.08)
    brake()

    servo_appointed_detection(0)
    time.sleep(0.8)
    rightdistance = Distance_test()

    servo_appointed_detection(180)
    time.sleep(0.8)
    leftdistance = Distance_test()

    servo_appointed_detection(90)
    time.sleep(0.8)
    frontdistance = Distance_test()


try:
    pre_check()
    key_scan()
    servo_color_carstate()