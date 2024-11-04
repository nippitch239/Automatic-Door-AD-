#include <Servo.h>

int x;
Servo myServo;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);

  myServo.attach(3);
}

void  loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  if (x == 5) {
    myServo.write(90);
  } else {
    myServo.write(0);
  }
}
