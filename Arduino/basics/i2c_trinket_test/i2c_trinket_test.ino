
#include <TinyWireS.h>

const int i2cAddr = 8;
const int potPin = 3;
const int ledPin = 1;

int potValue = 0;
int outputValue = 0;

void setup() {
  TinyWireS.begin(i2cAddr);                // join i2c bus with address #8
}

void loop() {
  //potValue = analogRead(potPin);
  //outputValue = map(potValue, 0, 128, 0, 255);
  for (int i=0; i<256; i++) {
    analogWrite(ledPin, i);
    TinyWireS.send(i);
    //delay(5);
  }
  //delay(100);
}
