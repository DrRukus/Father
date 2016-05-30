//#include <TinyWireM.h>
//#include <USI_TWI_Master.h>
//#include <Wire.h>


const int potPin = 3;
const int ledPin = 1;

int potValue = 0;
int outputValue = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  //pinMode(potPin, INPUT);
  //pinMode(ledPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  potValue = analogRead(potPin);
  //outputValue = map(potValue, 0, 1023, 0, 255);
  analogWrite(ledPin, potValue);
  delay(1);
}
