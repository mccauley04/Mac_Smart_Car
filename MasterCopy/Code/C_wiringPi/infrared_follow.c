
#include <wiringPi.h>
#include <softPwm.h>

//Definition of Pin
int Left_motor_go = 28;       //AIN2 connects to wiringPi port 28 of Raspberry pi for control Left motor forward 
int Left_motor_back = 29;     //AIN1 connects to wiringPi port 29 of Raspberry pi for control Left motor back 

int Right_motor_go = 24;      //BIN2 connects to wiringPi port 24 of Raspberry pi for control Left motor forward 
int Right_motor_back = 25;    //BIN1 connects to wiringPi port 25 of Raspberry pi for control Left motor back

int Left_motor_pwm = 27;      //PWMA connects to wiringPi port 27 of Raspberry pi for control the speed of the left motor
int Right_motor_pwm = 23;     //PWMA connects to wiringPi port 23 of Raspberry pi for control the speed of the right motor

int key = 10;                 //Key connects to wiringPi port 10 of Raspberry pi 

const int FollowSensorLeft =  26;  //Obstacle avoidance infrared sensor pin on the left is connected to  wiringPi port 26 of Raspberry pi
const int FollowSensorRight = 0;   //Obstacle avoidance infrared sensor pin on the right is connected to  wiringPi port 0 of Raspberry pi


int LeftSensorValue ;              //Define variables to store data collected by each Obstacle avoidance infrared sensor 
int RightSensorValue ;


void run()
{

  digitalWrite(Left_motor_go, HIGH);
  digitalWrite(Left_motor_back, LOW);
  softPwmWrite(Left_motor_pwm, 150);


  digitalWrite(Right_motor_go, HIGH);
  digitalWrite(Right_motor_back, LOW);
  softPwmWrite(Right_motor_pwm, 150);
}

void brake()
{
  digitalWrite(Left_motor_go, LOW);
  digitalWrite(Left_motor_back, LOW);
  digitalWrite(Right_motor_go, LOW);
  digitalWrite(Right_motor_back, LOW);
}


void left()
{

  digitalWrite(Left_motor_go, LOW);
  digitalWrite(Left_motor_back, LOW);
  softPwmWrite(Left_motor_pwm, 0);


  digitalWrite(Right_motor_go, HIGH);
  digitalWrite(Right_motor_back, LOW);
  softPwmWrite(Right_motor_pwm, 100);
}


void right()
{

  digitalWrite(Left_motor_go, HIGH);
  digitalWrite(Left_motor_back, LOW);
  softPwmWrite(Left_motor_pwm, 100);


  digitalWrite(Right_motor_go, LOW);
  digitalWrite(Right_motor_back, LOW);
  softPwmWrite(Right_motor_pwm, 0);
}

void spin_left(int time)
{

  digitalWrite(Left_motor_go, LOW);
  digitalWrite(Left_motor_back, HIGH);
  softPwmWrite(Left_motor_pwm, 150);


  digitalWrite(Right_motor_go, HIGH);
  digitalWrite(Right_motor_back, LOW);
  softPwmWrite(Right_motor_pwm, 150);

  delay(time * 100);
}


void spin_right(int time)
{

  digitalWrite(Left_motor_go, HIGH);
  digitalWrite(Left_motor_back, LOW);
  softPwmWrite(Left_motor_pwm, 150);


  digitalWrite(Right_motor_go, LOW);
  digitalWrite(Right_motor_back, HIGH);
  softPwmWrite(Right_motor_pwm, 150);

  delay(time * 100);
}

void back(int time)
{

  digitalWrite(Left_motor_go, LOW);
  digitalWrite(Left_motor_back, HIGH);
  softPwmWrite(Left_motor_pwm, 150);


  digitalWrite(Right_motor_go, LOW);
  digitalWrite(Right_motor_back, HIGH);
  softPwmWrite(Right_motor_pwm, 150);

  delay(time * 100);
}


void key_scan()
{
  while (digitalRead(key));
  while (!digitalRead(key))
  {
    delay(10);
    if (digitalRead(key)  ==  LOW)
    {
      delay(100);
      while (!digitalRead(key));
    }
  }
}


void main()
{ 

  wiringPiSetup();
  
  pinMode(Left_motor_go, OUTPUT);
  pinMode(Left_motor_back, OUTPUT);
  pinMode(Right_motor_go, OUTPUT);
  pinMode(Right_motor_back, OUTPUT);
  

  softPwmCreate(Left_motor_pwm,0,255); 
  softPwmCreate(Right_motor_pwm,0,255);


  pinMode(key, INPUT);


  pinMode(FollowSensorLeft, INPUT);
  pinMode(FollowSensorRight, INPUT);

  key_scan();
  
  while(1)
  {

    LeftSensorValue  = digitalRead(FollowSensorLeft);
    RightSensorValue = digitalRead(FollowSensorRight);

    if (LeftSensorValue == LOW && RightSensorValue == LOW)
    {
      run();
    }
    else if (LeftSensorValue == LOW && RightSensorValue == HIGH)
    {
      spin_left(2);
    }
    else if (RightSensorValue == LOW && LeftSensorValue == HIGH)
    {
      spin_right(2);
    }
    else if (LeftSensorValue == HIGH && RightSensorValue == HIGH)
    {
      brake();
    }
  }
  return;
}
