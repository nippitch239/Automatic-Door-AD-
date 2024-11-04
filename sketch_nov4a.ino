#include <Servo.h>

Servo myServo;  // Create a Servo object
const int servoPin = 9;  // Pin connected to the servo

void setup() {
    Serial.begin(9600);  // Start serial communication at 9600 baud
    myServo.attach(servoPin);  // Attach the servo to the specified pin
}

void loop() {
    if (Serial.available()) {
        // Read a byte from the serial port
        byte command = Serial.read();

        // Check the command received and take action
        if (command == 1) {  // If command is 1, turn left
            myServo.write(0);  // Adjust this angle for your servo
        } else if (command == 2) {  // If command is 2, turn right
            myServo.write(180);  // Adjust this angle for your servo
        }
        else if (command == 0){
            myServo.write(120);  // Adjust this angle for your servo
        }
        // You can add more commands if needed
    }
}
