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

float pi = 3.1415926;
int colors[8] = {BLACK, BLUE, RED, GREEN, CYAN, MAGENTA, YELLOW, WHITE};
const int pingPin = 7;
const int inputPin = 10;
const int outputPin1 = 7;
const int outputPin2 = 8;
const int screenSwitch = 13;
int toggle = 1;
int dist100, dist10, dist1;
boolean screenOn;

long newDistance;
long oldDistance;
boolean isBreach;

//struct 

void setup(void) {
  Serial.begin(9600);
  tft.begin();
  tft.fillRect(0, 0, 128, 128, BLACK);
  pinMode(inputPin, INPUT);
  pinMode(screenSwitch, INPUT);
  pinMode(outputPin1, OUTPUT);
  pinMode(outputPin2, OUTPUT);
}

void loop() { 
    // Check if screen is switched on
    if (digitalRead(screenSwitch)) { screenOn = true; }
    else { screenOn = false; }

    // Check windows
    isBreach = windowMonitor(screenOn);
    //distanceDisplay(screenOn);
      
    delay(100);
}

void distanceDisplay(boolean screenOn) {
    newDistance = microsecondsToCentimeters(pinger());
    if (screenOn) {
        if (newDistance != oldDistance) {
            dist100 = newDistance / 100;       // Hundreds digit
            dist10 = (newDistance % 100) / 10; // Tens digit
            dist1 = newDistance % 10;          // Ones digit

            // Blank out previous distance
            tft.fillRect(60, 20, 75, 30, BLACK);
            tft.setCursor(0,20);
            tft.setTextColor(GREEN);
            tft.print("Distance: ");
            
            // Set hundreds digit - black if zero
            tft.setCursor(60, 20);
            if (dist100 == 0) { tft.setTextColor(BLACK); }
            else { tft.setTextColor(GREEN); }
            tft.print(dist100);
            
            // Set tens digit - black if zero
            if (dist10 == 0) { tft.setTextColor(BLACK); }
            else { tft.setTextColor(GREEN); }
            tft.print(dist10);

            // Set ones digit
            tft.setTextColor(GREEN);
            tft.print(dist1);
            tft.setCursor(75, 20);
            tft.print(" cm");
        }
    } else { tft.fillRect(0, 0, 128, 128, BLACK); }
    oldDistance = newDistance;
}

boolean windowMonitor(boolean screenOn) {
    int in = digitalRead(inputPin);
    if (in == 0) { 
        digitalWrite(outputPin1, LOW);
        digitalWrite(outputPin2, HIGH);
        if (screenOn) {
            if (toggle) { 
                tft.fillRect(0, 0, 128, 20, BLACK);
                toggle = 0;
            } 
            tft.setCursor(0,0);
            tft.setTextColor(BLUE);
            tft.print("Window secure"); 
        }
        return true;
    } else { 
        digitalWrite(outputPin1, HIGH);
        digitalWrite(outputPin2, LOW);
        if (screenOn) {
            if (!toggle) {
                tft.fillRect(0, 0, 128, 20, BLACK);
                toggle = 1;
            }
            tft.setCursor(0,10);
            tft.setTextColor(RED);
            tft.print("Intrusion detected");
        }
        return false;
    }  
}

long pinger() {
    long duration, inches, cm;

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

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

void fillpixelbypixel(uint16_t color) {
  for (uint8_t x=0; x < tft.width(); x++) {
    for (uint8_t y=0; y < tft.height(); y++) {
      tft.drawPixel(x, y, color);
    }
  }
  delay(100);
}

//void printer(char* text, int16_t x, int16_t y) {
//}

void drawtext(char *text, uint16_t color, uint16_t line) {
  if (line < 12 && line > 0) {
      tft.setCursor(0,line * 10);
      tft.setTextColor(color);
      tft.print(text);
  } else {
      tft.print("Invalid line number given!");
  }
}

void mediabuttons() {
 // play
  tft.fillScreen(BLACK);
  tft.fillRoundRect(25, 10, 78, 60, 8, WHITE);
  tft.fillTriangle(42, 20, 42, 60, 90, 40, RED);
  delay(500);
  // pause
  tft.fillRoundRect(25, 90, 78, 60, 8, WHITE);
  tft.fillRoundRect(39, 98, 20, 45, 5, GREEN);
  tft.fillRoundRect(69, 98, 20, 45, 5, GREEN);
  delay(500);
  // play color
  tft.fillTriangle(42, 20, 42, 60, 90, 40, BLUE);
  delay(50);
  // pause color
  tft.fillRoundRect(39, 98, 20, 45, 5, RED);
  tft.fillRoundRect(69, 98, 20, 45, 5, RED);
  // play color
  tft.fillTriangle(42, 20, 42, 60, 90, 40, GREEN);
}

/**************************************************************************/
/*! 
    @brief  Renders a simple test pattern on the LCD
*/
/**************************************************************************/
void lcdTestPattern(void)
{
  uint32_t i,j;
  tft.goTo(0, 0);
  
  for(i=0;i<64;i++)
  {
    for(j=0;j<128;j++)
    {
      if(i<16){tft.writeData(RED>>8); tft.writeData(RED);}
      else if(i<32) {tft.writeData(YELLOW>>8);tft.writeData(YELLOW);}
      else if(i<48){tft.writeData(GREEN>>8);tft.writeData(GREEN);}
      else if(i<64){tft.writeData(CYAN>>8);tft.writeData(CYAN);}
      else if(i<80){tft.writeData(BLUE>>8);tft.writeData(BLUE);}
      else if(i<96){tft.writeData(MAGENTA>>8);tft.writeData(MAGENTA);}
      else if(i<112){tft.writeData(BLACK>>8);tft.writeData(BLACK);}
      else {tft.writeData(WHITE>>8);tft.writeData(WHITE);}
    }
  }
}
