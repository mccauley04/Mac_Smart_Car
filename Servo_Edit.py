create a loop statement

Loop Type & Description
1	while loop
Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

2	for loop
Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

3	nested loops
You can use one or more loop inside any another while, for or do..while loop.

Control Statement & Description
1	break statement
Terminates the loop statement and transfers execution to the statement immediately following the loop.

2	continue statement
Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.

3	pass statement
The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.



while (distance_test() < 30):
   GPIO.output(LED_R, GPIO.HIGH)
   GPIO.output(LED_G, GPIO.LOW)
   GPIO.output(LED_B, GPIO.LOW)
   brake()
   print 'The count is:', count
   count = count + 1

print "Good bye!"



def servo_color_carstate():

    'RED LIGHT'
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)

    'back(20, 20)' 'Not sure why we move the car before Analyzing the suroundings'

    brake() 'Apply the break to make sure the car is not moving during this time'
    
    time.sleep(0.08)
    
    servo_appointed_detection(0)
    time.sleep(0.25) 'First line of code had a time.sleep state of 0.8'
    scan_distance_0 = Distance_test()
    
    servo_appointed_detection(30)
    time.sleep(0.25)
    scan_distance_30 = Distance_test()
    
    rside_distance =  scan_distance_0 + scan_distance_30
       
    servo_appointed_detection(60)
    time.sleep(0.25)
    scan_distance_
    
60 = Distance_test()
    
    servo_appointed_detection(90)
    time.sleep(0.25)
    scan_distance_90 = Distance_test()
    
    rmiddle_distance = scan_distance_60 + scan_distance_90
    rdistance = rmiddle_distance+ rside_distance

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

    lside_distance =  scan_distance_150 + scan_distance_180
    ldistance = lside_distance + lmiddle_distance
    
    
  
    if lside_distance < 35 and lmiddle_distance < 35 and rmiddle_distance < 35 and rside_distance < 35:

    'if leftdistance < 30 and rightdistance < 30 and frontdistance < 30:'
    
        'Magenta'
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)

        'Slowly move back at tad and do a 180'
        back(10,10)
        time.sleep(.58)
        
        spin_right(25, 25)
        time.sleep(0.58)

    elif lside_distance >= lmiddle_distance:

    'elif leftdistance >= rightdistance:'
        'Blue'
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_left(25, 25) '35,35'
        time.sleep(0.28)

    elif lmiddle_distance >= rmiddle_distance:
        
    'elif leftdistance <= rightdistance:'
        'Blue'
        GPIO.output(LED_R, GPIO.Low)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_left(25, 25) '35,35'
        time.sleep(0.28)

    elif rmiddle_distance >= rside_distance:
        
    'elif leftdistance <= rightdistance:'
        'Blue'
        GPIO.output(LED_R, GPIO.Low)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_right(25, 25) '35,35'
        time.sleep(0.28)
