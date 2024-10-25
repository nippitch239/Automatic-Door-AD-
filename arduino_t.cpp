int analog = A1;
int led = 7;
int val = 0;

void setup()
{
  pinMode(analog, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  val = analogRead(analog);
  Serial.print("val = ");
  Serial.println(val);
  if (val > 500) {
  	digitalWrite(led, HIGH);
  }
  else {
  	digitalWrite(led, LOW);
  }
  delay(100);
}