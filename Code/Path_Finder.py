# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

'Definition of  motor pins'
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

'Definition of  key'
key = 8

'Definition of  ultrasonic module pins'
EchoPin = 0
TrigPin = 1

'Definition of RGB module pins'
LED_R = 22
LED_G = 27
LED_B = 24

'Definition of servo pin'
ServoPin = 23

'Definition of infrared obstacle avoidance module pins'
AvoidSensorLeft = 12
AvoidSensorRight = 17

'Set the GPIO port to BCM encoding mode'
GPIO.setmode(GPIO.BCM)

'Ignore warning information'
GPIO.setwarnings(False)

'Motor pins are initialized into output mode'
'Key pin is initialized into input mode'
'Ultrasonic pin,RGB pin,servo pin initialization'
'infrared obstacle avoidance module pin'


def pre_checks():
    global pwm_ENA
    global pwm_ENB
    global pwm_servo
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(key, GPIO.IN)
    GPIO.setup(EchoPin, GPIO.IN)
    GPIO.setup(TrigPin, GPIO.OUT)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)
    GPIO.setup(AvoidSensorLeft, GPIO.IN)
    GPIO.setup(AvoidSensorRight, GPIO.IN)
    'Set the PWM pin and frequency is 2000hz'
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)


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


def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)



scan_dl = []


def servo_color_carstate():
    'RED LIGHT'
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)

    angles = [0, 30, 60, 90, 120, 150, 180, 90]

    for index in range(8):
        servo_appointed_detection(angles[index])
        time.sleep(.4)

        scan_dl.append(int(round(Distance_test(), 2)))
        print(scan_dl)


def decision_time():
    'YELLOW'

    #check

    right_side = scan_dl[0] + scan_dl[1] + scan_dl[2] + scan_dl[3]
    left_side = scan_dl[3] + scan_dl[4] + scan_dl[5] + scan_dl[6]

    print(right_side)
    print(left_side)

    #If i line everything up I could ideally define a certian degree of a turn.

    #Right side


    test1 = [n for n, i in enumerate(scan_dl) if i > scan_dl[0]][0]
    print(test1)

try:
    pre_checks()
    servo_color_carstate()
    decision_time()

except KeyboardInterrupt:
    pass

pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()