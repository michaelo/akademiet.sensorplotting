int sensePin = A0;
int sensorInput = 0;
double temp = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorInput = analogRead(sensePin);
  temp = ((double)sensorInput / 1024) * 5;
  temp = (temp-0.5)*100;
  Serial.println(temp);
  delay(1000);
}
