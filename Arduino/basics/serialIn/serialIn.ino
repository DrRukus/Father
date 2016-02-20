#define sclk 2
#define mosi 3
#define dc   4
#define cs   5
#define rst  6

// Color definitions
#define BLACK           0x0000
#define BLUE            0x001F
#define RED             0xF800
#define GREEN           0x07E0
#define CYAN            0x07FF
#define MAGENTA         0xF81F
#define YELLOW          0xFFE0  
#define WHITE           0xFFFF

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1351.h>
#include <SPI.h>

// Option 1: use any pins but a little slower
Adafruit_SSD1351 tft = Adafruit_SSD1351(cs, dc, mosi, sclk, rst);  

// Option 2: must use the hardware SPI pins 
// (for UNO thats sclk = 13 and sid = 11) and pin 10 must be 
// an output. This is much faster - also required if you want
// to use the microSD card (see the image drawing example)
//Adafruit_SSD1351 tft = Adafruit_SSD1351(cs, dc, rst);

int colors[8] = {BLACK, BLUE, RED, GREEN, CYAN, MAGENTA, YELLOW, WHITE};

const int serialIn = 11;
const int shiftPin = 9;
const int clockPin = 10;
const int outputPin1 = 7;
const int outputPin2 = 8;
const int numBits = 4;

int bits[numBits];

//struct 

void setup(void) {
    Serial.begin(9600);
    pinMode(serialIn, INPUT);
    pinMode(shiftPin, OUTPUT);
    pinMode(clockPin, OUTPUT);
    pinMode(outputPin1, OUTPUT);
    pinMode(outputPin2, OUTPUT);

    digitalWrite(shiftPin, HIGH);
    digitalWrite(clockPin, LOW);
    digitalWrite(clearPin, HIGH);
}

void loop() { 
    // Load parallel
    parallelLoad();
    
    serialLoad(bits, numBits);

    //displayBits();
    
    //delay(10);

    digitalWrite(shiftPin, HIGH);
    digitalWrite(outputPin2, HIGH);
    delay(10);
    
}

void parallelLoad() {
  
    digitalWrite(shiftPin, LOW);     // Enable parallel load
    digitalWrite(outputPin2, LOW);
    delay(10);
    digitalWrite(clockPin, HIGH);   // Clock the data in
    delay(10);
    digitalWrite(clockPin, LOW);    // Complete clock cycle
    digitalWrite(shiftPin, HIGH);   // Enable shift-left mode
    digitalWrite(outputPin2, HIGH);
}

void serialLoad(int bits[], int numBits) {

    // Get first bit
    bits[0] = digitalRead(serialIn);
    
    for (int i = 1; i < numBits; i++) {
        // Shift right
        delay(10);
        digitalWrite(clockPin, HIGH);
        digitalWrite(outputPin1, HIGH);
   
        // Get bit
        bits[i] = digitalRead(serialIn);
   
        delay(10);
        digitalWrite(clockPin, LOW);
        digitalWrite(outputPin1, LOW);
    }
}

void displayBits() {
    Serial.print(bits[3]);
    Serial.print(bits[2]);
    Serial.print(bits[1]);
    Serial.println(bits[0]);
}

