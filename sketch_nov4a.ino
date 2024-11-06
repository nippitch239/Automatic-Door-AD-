#include <Servo.h>

Servo myServo;
const int servoPin = 9;

void setup() {
    Serial.begin(9600);
    myServo.attach(servoPin);
}

void loop() {
    if (Serial.available()) {
        byte command = Serial.read();
        if (command == 1) {
            myServo.write(0);
        } else if (command == 2) {
            myServo.write(180);
        }
        else if (command == 0){
            myServo.write(120);
        }
    }
}
