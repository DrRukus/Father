#include <Wire.h>

#define SLAVE_ADDRESS 0x04
#define LED_PIN 13
int freq = 1;

void setup() {
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);

  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  Serial.println("Ready!");

  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (freq != 0) {
    digitalWrite(LED_PIN, HIGH);
    delay(freq * 100);
    digitalWrite(LED_PIN, LOW);
    delay(freq * 100);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
}

// callback for received data
void receiveData(int byteCount){

  while(Wire.available()) {
    freq = Wire.read();
    Serial.print("Value Received: ");
    Serial.println(freq);
  }
}

// callback for sending data
void sendData(){
  Serial.print("Value sending: ");
  Serial.println(freq);
  Wire.write(freq);
}
