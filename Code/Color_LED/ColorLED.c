#include <wiringPi.h>

#define ON 1     
#define OFF 0    

//Definition of Pin
int LED_R = 3;           //LED_R is connected to  wiringPi port 3 of Raspberry pi
int LED_G = 2;           //LED_G is connected to  wiringPi port 2 of Raspberry pi
int LED_B = 5;           //LED_B is connected to  wiringPi port 5 of Raspberry pi

void color_led(int v_iRed, int v_iGreen, int v_iBlue)
{
  v_iRed == ON ? digitalWrite(LED_R, HIGH): digitalWrite(LED_R, LOW);
 
  v_iGreen == ON ? digitalWrite(LED_G, HIGH) : digitalWrite(LED_G, LOW);

  v_iBlue == ON ? digitalWrite(LED_B, HIGH) : digitalWrite(LED_B, LOW);
}

int main()
{
	wiringPiSetup();
	
	//Initialize the RGB IO as the output mode
	pinMode(LED_R, OUTPUT);
	pinMode(LED_G, OUTPUT);
	pinMode(LED_B, OUTPUT);
	
	while (1)
	{                        //   LED_R   LED_G    LED_B
    color_led(ON, OFF, OFF); //   1        0        0
    delay(3000);
    /// This configuration produces a steady Red Light.

    color_led(OFF, ON, OFF); //   0        1        0
    delay(2000);
    /// This configuration produces a steady Green Light.

   /// color_led(OFF, OFF, ON); //   0        0        1
   /// delay(1000);
   /// color_led(ON, ON, OFF);  //   1        1        0
   /// delay(1000);
   /// color_led(ON, OFF, ON);  //   1        0        1
  ///  delay(1000);
  ///  color_led(OFF, ON, ON);  //   0        1        1
   /// delay(1000);
  ///  color_led(ON, ON, ON);   //   1        1        1

	}
   return 0;	
}