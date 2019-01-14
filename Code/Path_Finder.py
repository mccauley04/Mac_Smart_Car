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


'Advance'
def run(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


'Back'
def back(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


'Turn left'
def left(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


'Turn right'
def right(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


'Turn left in place'
def spin_left(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


'Turn right in place'
def spin_right(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


'Break'
def brake():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

'Button detection'
def key_scan():
    while GPIO.input(key):
        pass
    while not GPIO.input(key):
        time.sleep(0.01)
        if not GPIO.input(key):
            time.sleep(0.01)
            while not GPIO.input(key):
                pass


'Ultrasonic function'
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


'The servo rotates to the specified angle'
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)


def servo_color_carstate():
    'RED LIGHT'
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)

    'back(20, 20)' 'Not sure why we move the car before Analyzing the suroundings'

    brake()
    'Apply the break to make sure the car is not moving during this time'

    time.sleep(0.08)

    servo_appointed_detection(0)
    time.sleep(0.25)
    'First line of code had a time.sleep state of 0.8'
    scan_distance_0 = Distance_test()

    servo_appointed_detection(30)
    time.sleep(0.25)
    scan_distance_30 = Distance_test()

    rside_distance = scan_distance_0 + scan_distance_30

    servo_appointed_detection(60)
    time.sleep(0.25)
    scan_distance_60 = Distance_test()

    servo_appointed_detection(90)
    time.sleep(0.25)
    scan_distance_90 = Distance_test()

    rmiddle_distance = scan_distance_60 + scan_distance_90
    rdistance = rmiddle_distance + rside_distance

    servo_appointed_detection(90)
    time.sleep(0.25)
    scan_distance_90 = Distance_test()

    servo_appointed_detection(120)
    time.sleep(0.25)
    scan_distance_120 = Distance_test()

    lmiddle_distance = scan_distance_90 + scan_distance_120

    servo_appointed_detection(150)
    time.sleep(0.25)
    scan_distance_150 = Distance_test()

    servo_appointed_detection(180)
    time.sleep(0.25)
    scan_distance_180 = Distance_test()

    lside_distance = scan_distance_150 + scan_distance_180
    ldistance = lside_distance + lmiddle_distance

    if ldistance < 35 and rdistance < 35:

    # if leftdistance < 30 and rightdistance < 30 and frontdistance < 30: 'Magenta'
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)

        spin_right(25, 25)
        time.sleep(0.58)

    elif lside_distance >= lmiddle_distance:

        # elif leftdistance >= rightdistance: 'Blue'
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_left(25, 25) #35,35
        time.sleep(0.28)

    elif lmiddle_distance >= rmiddle_distance:

    # elif leftdistance <= rightdistance:
        'Blue'
        GPIO.output(LED_R, GPIO.Low)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_left(25, 25) #35,35
        time.sleep(0.28)

    elif rmiddle_distance >= rside_distance:

        # elif leftdistance <= rightdistance:
        'Blue'
        GPIO.output(LED_R, GPIO.Low)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_right(25, 25) #35,35
        time.sleep(0.28)


# delay 2s
time.sleep(2)

'''The try/except statement is used to detect errors in the try block.
The except statement catches the exception information and processes it.'''


try:
    pre_checks()
    key_scan()
    while True:
        distance = Distance_test()
        if distance > 50:

            'There is obstacle, the indicator light of the infrared obstacle avoidance module is on, and the port level is LOW'
            'There is no obstacle, the indicator light of the infrared obstacle avoidance module is off, and the port level is HIGH'


            LeftSensorValue = GPIO.input(AvoidSensorLeft)
            RightSensorValue = GPIO.input(AvoidSensorRight)

            if LeftSensorValue == True and RightSensorValue == True:
                run(50, 50)
            elif LeftSensorValue == True and RightSensorValue == False:
                spin_left(35, 35)
                time.sleep(0.002)
            elif RightSensorValue == True and LeftSensorValue == False:
                spin_right(35, 35)
                time.sleep(0.002)
            elif RightSensorValue == False and LeftSensorValue == False:
                spin_right(35, 35)
                time.sleep(0.002)
                run(100, 100)

                GPIO.output(LED_R, GPIO.LOW)
                GPIO.output(LED_G, GPIO.HIGH)
                GPIO.output(LED_B, GPIO.LOW)

        elif 30 <= distance <= 50:

            'There is obstacle, the indicator light of the infrared obstacle avoidance module is on, and the port level is LOW'
            'There is no obstacle, the indicator light of the infrared obstacle avoidance module is off, and the port level is HIGH'

            LeftSensorValue = GPIO.input(AvoidSensorLeft)
            RightSensorValue = GPIO.input(AvoidSensorRight)

            if LeftSensorValue == True and RightSensorValue == True:
                run(50, 50)
            elif LeftSensorValue == True and RightSensorValue == False:
                spin_left(35, 35)
                time.sleep(0.002)
            elif RightSensorValue == True and LeftSensorValue == False:
                spin_right(35, 35)
                time.sleep(0.002)
            elif RightSensorValue == False and LeftSensorValue == False:
                spin_right(35, 35)
                time.sleep(0.002)
                run(50, 50)

        elif distance < 30:
            servo_color_carstate()

except KeyboardInterrupt:
    pass
pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()
