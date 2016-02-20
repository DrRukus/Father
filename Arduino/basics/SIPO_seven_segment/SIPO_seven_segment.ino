#include <elapsedMillis.h>

elapsedMillis timeElapsed;

const boolean one = HIGH;
const boolean zero = LOW;

const int Jout = 8;
const int clk = 1;

boolean binaries[10][4] = {{zero, zero, zero, zero}, // 0 - 0000
                           {zero, zero, zero, one},  // 1 - 0001
                           {zero, zero, one, zero},  // 2 - 0010
                           {zero, zero, one, one},   // 3 - 0011
                           {zero, one, zero, zero},  // 4 - 0100
                           {zero, one, zero, one},   // 5 - 0101
                           {zero, one, one, zero},   // 6 - 0110
                           {zero, one, one, one},    // 7 - 0111
                           {one, zero, zero, zero},  // 8 - 1000
                           {one, zero, zero, one}};  // 9 - 1001

void setup() {
  //Serial.begin(9600);
  pinMode(Jout, OUTPUT);
  pinMode(clk, OUTPUT);
}

void loop() {
    for (int i = 0; i < 10; i++) {
        writeFourBits(binaries[i]);
        delay(1000);
        //Serial.println(timeElapsed);
    }
}

void writeFourBits(boolean bits[4]) {
    for (int i = 0; i < 4; i++) {
        digitalWrite(clk, LOW);
        //delay(100);
        if (bits[i] == HIGH) { digitalWrite(Jout, HIGH); }
        else { digitalWrite(Jout, LOW); }
        digitalWrite(clk, HIGH);
        //delay(100);
    }
}


