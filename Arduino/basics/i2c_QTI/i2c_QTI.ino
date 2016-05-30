
#include <TinyWireS.h>

const int i2cAddr = 8;
const int qtiPin = 1;

long sensor = 50;

void setup() {
  TinyWireS.begin(i2cAddr);                // join i2c bus with address #8
  //Serial.begin(9600);
}

void loop() {
  sensor = RCtime(qtiPin);
  TinyWireS.send(sensor);
  //TinyWireS.send(189);
  delay(10);
  //Serial.println(sensor);
  //delay(50);
}

long RCtime(int sensPin)
{
   short result = 0;
   pinMode(sensPin, OUTPUT);       // make pin OUTPUT
   digitalWrite(sensPin, HIGH);    // make pin HIGH to discharge capacitor - study the schematic
   delay(1);                       // wait a  ms to make sure cap is discharged

   pinMode(sensPin, INPUT);        // turn pin into an input and time till pin goes low
   digitalWrite(sensPin, LOW);     // turn pullups off - or it won't work
   while(digitalRead(sensPin))
   {    // wait for pin to go low
      result++;
   }

   return result;                   // report results   
} 
