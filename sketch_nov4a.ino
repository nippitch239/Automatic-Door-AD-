#include <Servo.h>

Servo myServo;
const int servoPin = 9;

void setup() {
    Serial.begin(9600);
    myServo.attach(servoPin);
}

void loop() {
    myServo.write(0);
    if (Serial.available()) {
        byte command = Serial.read();
        if (command == 1) {
            myServo.write(90);
            delay(1500);
        }
    }
}
