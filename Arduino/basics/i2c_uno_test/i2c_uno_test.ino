
#include <Wire.h>

const int i2cAddr = 8;

void setup() {
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(9600);  // start serial for output
}

void loop() {
  Wire.requestFrom(i2cAddr, 2);    // request 4 bytes from slave device #8
  while (Wire.available()) { // slave may send less than requested
    short num = Wire.read(); // receive a byte as character
    Serial.println(num);         // print the character
  }

  delay(100);
}
