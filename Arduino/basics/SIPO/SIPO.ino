enum binAlias{ D, C, B, A };

const int Jout = 8;
const int Kout = 9;
const int shift = 0;
const int clk = 1;

/*boolean binaries[10][4] = {{LOW, LOW, LOW, LOW},
                           {LOW, LOW, LOW, HIGH},
                           {LOW, LOW, HIGH, LOW},
                           {LOW, LOW, HIGH, HIGH},
                           {LOW, HIGH, LOW, LOW},
                           {LOW, HIGH, LOW, HIGH},
                           {LOW, HIGH, HIGH, LOW},
                           {LOW, HIGH, HIGH, HIGH},
                           {HIGH, LOW, LOW, LOW},
                           {HIGH, LOW, LOW, HIGH}};*/

void setup() {
  pinMode(Jout, OUTPUT);
  pinMode(Kout, OUTPUT);
  pinMode(shift, OUTPUT);
  pinMode(clk, OUTPUT);
  digitalWrite(shift, HIGH);
}

void loop() {
    digitalWrite(clk, LOW);
    delay(500);
    dataHigh();
    digitalWrite(clk, HIGH);
    delay(500);
    digitalWrite(clk, LOW);
    delay(500);
    dataLow();
    digitalWrite(clk, HIGH);
    delay(500);
    digitalWrite(clk, LOW);
    delay(500);
    dataHigh();
    digitalWrite(clk, HIGH);
    delay(500);
    digitalWrite(clk, LOW);
    delay(500);
    dataLow();
    digitalWrite(clk, HIGH);
    delay(500);
    digitalWrite(clk, LOW);
    delay(500);
    dataHigh();
    digitalWrite(clk, HIGH);
    delay(500);
    digitalWrite(clk, LOW);
    delay(500);
    dataLow();
    digitalWrite(clk, HIGH);
    delay(500);
    digitalWrite(clk, LOW);
    delay(500);
    dataLow();
    digitalWrite(clk, HIGH);
    delay(500);
}

void dataHigh() {
    digitalWrite(Jout, HIGH);
    digitalWrite(Kout, HIGH);
}

void dataLow() {
    digitalWrite(Jout, LOW);
    digitalWrite(Kout, LOW);
}


