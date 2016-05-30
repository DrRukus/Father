enum binAlias{ D, C, B, A };

const int Dout = 3;
const int Cout = 2;
const int Bout = 1;
const int Aout = 0;
const int seg1 = 10;
const int seg2 = 8;

boolean binaries[10][4] = {{LOW, LOW, LOW, LOW},
                           {LOW, LOW, LOW, HIGH},
                           {LOW, LOW, HIGH, LOW},
                           {LOW, LOW, HIGH, HIGH},
                           {LOW, HIGH, LOW, LOW},
                           {LOW, HIGH, LOW, HIGH},
                           {LOW, HIGH, HIGH, LOW},
                           {LOW, HIGH, HIGH, HIGH},
                           {HIGH, LOW, LOW, LOW},
                           {HIGH, LOW, LOW, HIGH}};

void setup() {
  pinMode(Dout, OUTPUT);
  pinMode(Cout, OUTPUT);
  pinMode(Bout, OUTPUT);
  pinMode(Aout, OUTPUT);
  pinMode(seg1, OUTPUT);
  pinMode(seg2, OUTPUT);
}

void loop() {
  for (int i = 0; i < 10; i++) {
      digitalWrite(Dout, binaries[i][D]);
      digitalWrite(Cout, binaries[i][C]);
      digitalWrite(Bout, binaries[i][B]);
      digitalWrite(Aout, binaries[i][A]);
      digitalWrite(seg1, HIGH);
      //digitalWrite(seg2, LOW);
      delay(1000); }
  
  /*digitalWrite(Dout, LOW);
  digitalWrite(Cout, LOW);
  digitalWrite(Bout, LOW);
  digitalWrite(Aout, HIGH);
  digitalWrite(seg1, LOW);
  digitalWrite(seg2, HIGH);
  delay(10);*/
}
