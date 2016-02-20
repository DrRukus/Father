/****************************************************************************************
 * 
 * This program will control multiple seven-segment displays through SIPO circuitry
 * 
 * Design expects 74195 TTL chip with J pin (pin 2) connected to Jout pin (as defined below),
 *   the K input (pin 3) connected to the J input, the CLK pin (pin 10) connected to clk 
 *   (as defined below), and the SH pin (pin 9) connected to +5V.
 * The 4 parallel outputs are then connected to DCBA of a 7447 decoder chip, which is 
 * connected appropriately (per datasheet) to a display module - NTE3078.
 * 
 * Vers: 1/1/16 - Can multiplex output through 2 common-anode 7-segment displays (NTE3078)
 * 
 ****************************************************************************************/

#include <elapsedMillis.h>

elapsedMillis elapsedTime;

const boolean one = HIGH;
const boolean zero = LOW;

const int Jout = 8;
const int clk = 2;
const int onesEnable = 4;
const int tensEnable = 6;
const int period = 100;
const int pingPin = 10;

int initTime;
int nowTime;
int ones = 0;
int tens = 0;
int tensFlag = 0;

boolean binaries[10][4] = {{zero, zero, zero, zero},  // 0 - 0000
                           {zero, zero, zero,  one},  // 1 - 0001
                           {zero, zero,  one, zero},  // 2 - 0010
                           {zero, zero,  one,  one},  // 3 - 0011
                           {zero,  one, zero, zero},  // 4 - 0100
                           {zero,  one, zero,  one},  // 5 - 0101
                           {zero,  one,  one, zero},  // 6 - 0110
                           {zero,  one,  one,  one},  // 7 - 0111
                           { one, zero, zero, zero},  // 8 - 1000
                           { one, zero, zero,  one}}; // 9 - 1001

void setup() {
  Serial.begin(9600);
  pinMode(Jout, OUTPUT);
  pinMode(clk, OUTPUT);
  pinMode(onesEnable, OUTPUT);
  pinMode(tensEnable, OUTPUT);
  initTime = elapsedTime;
}

void loop() {
    long duration = pinger();
    long centies = microsecondsToCentimeters(duration);
    if (centies > 90) { centies = 90; }
    else if (centies < 0) { centies = 0; }
    tens = centies / 10;
    ones = centies % 10;
    tensFlag ? setOutput("tens") : setOutput("ones");
    Serial.print(centies);
    Serial.print("cm");
    Serial.println();
    delay(1);
}

void writeFourBits(boolean bits[4]) {
    for (int i = 0; i < 4; i++) {
        digitalWrite(clk, LOW);
        //delay(1);
        if (bits[i] == HIGH) { digitalWrite(Jout, HIGH); }
        else { digitalWrite(Jout, LOW); }
        digitalWrite(clk, HIGH);
        //delay(1);
    }
}

void setOutput(char place[4]) {
    if (place[0] == 't') {
        writeFourBits(binaries[tens]);
        digitalWrite(onesEnable, LOW);
        digitalWrite(tensEnable, HIGH);
        tensFlag = 0;
    } else if (place[0] == 'o') {
        writeFourBits(binaries[ones]);
        digitalWrite(onesEnable, HIGH);
        digitalWrite(tensEnable, LOW);
        tensFlag = 1;
    }
}

long pinger() {
    long duration, cm;

    // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
    // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
    pinMode(pingPin, OUTPUT);
    digitalWrite(pingPin, LOW);
    delayMicroseconds(2);
    digitalWrite(pingPin, HIGH);
    delayMicroseconds(5);
    digitalWrite(pingPin, LOW);

    // The same pin is used to read the signal from the PING))): a HIGH
    // pulse whose duration is the time (in microseconds) from the sending
    // of the ping to the reception of its echo off of an object.
    pinMode(pingPin, INPUT);
    duration = pulseIn(pingPin, HIGH);

    return duration;
}

long microsecondsToCentimeters(long microseconds) {
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}


