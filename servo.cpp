#include <Servo.h>

void setup()
{
  myservo.attach(9);
}
void loop()
{
  myservo.write(0);
}