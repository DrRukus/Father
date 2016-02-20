/*
   I/O capabilities demonstration
*/
const int greenLedPin = 0;
const int orangeLedPin = 3;
const int wait = 500;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(greenLedPin, OUTPUT);
  pinMode(orangeLedPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(orangeLedPin, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(greenLedPin, LOW);    // turn the LED off by making the voltage LOW
  delay(wait);              // wait
  digitalWrite(orangeLedPin, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(greenLedPin, HIGH);    // turn the LED off by making the voltage LOW
  delay(wait); 
}
