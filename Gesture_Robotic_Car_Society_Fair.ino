char command;  // Variable to store the received command

// Motor control pins
int BR_enA = 6;  // Speed control for Motor A
int BL_enB = 3;   // Speed control for Motor B
int BR_IN1 = 5;  // Direction control for Motor A
int BR_IN2 = 4;  
int BL_IN3 = 2;   // Direction control for Motor B
int BL_IN4 = 7;
int FR_enA = 10;  // Speed control for Motor A
int FL_enB = 9;   // Speed control for Motor B
int FR_IN1 = 13;  // Direction control for Motor A
int FR_IN2 = 12;  
int FL_IN3 = 11;   // Direction control for Motor B
int FL_IN4 = 8;

void setup() {
  Serial.begin(9600);

  // Set all the motor control pins as outputs
  pinMode(BR_enA, OUTPUT);
  pinMode(BL_enB, OUTPUT);
  pinMode(BR_IN1, OUTPUT);
  pinMode(BR_IN2, OUTPUT);
  pinMode(BL_IN3, OUTPUT);
  pinMode(BL_IN4, OUTPUT);

  pinMode(FR_enA, OUTPUT);
  pinMode(FL_enB, OUTPUT);
  pinMode(FR_IN1, OUTPUT);
  pinMode(FR_IN2, OUTPUT);
  pinMode(FL_IN3, OUTPUT);
  pinMode(FL_IN4, OUTPUT);

  // Initially stop both motors
  digitalWrite(BR_IN1, LOW);
  digitalWrite(BR_IN2, LOW);
  digitalWrite(BL_IN3, LOW);
  digitalWrite(BL_IN4, LOW);

  digitalWrite(FR_IN1, LOW);
  digitalWrite(FR_IN2, LOW);
  digitalWrite(FL_IN3, LOW);
  digitalWrite(FL_IN4, LOW);

  // Set the speed of the motors
  analogWrite(BR_enA, 75);  // Max speed for Motor A
  analogWrite(BL_enB, 75);  // Max speed for Motor B

  analogWrite(FR_enA, 75);  // Max speed for Motor A
  analogWrite(FL_enB, 75);  // Max speed for Motor B
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();  // Read the incoming command
    // Serial.print("Received: ");
    // Serial.println(command);

    // Reset all motor direction pins before executing a new command
    // digitalWrite(IN1, LOW);
    // digitalWrite(IN2, LOW);
    // digitalWrite(IN3, LOW);
    // digitalWrite(IN4, LOW);
    
    switch (command) {
      case 'L':
        // Move Left (Rotate Motor A forward, Motor B backward)
        // digitalWrite(IN1, HIGH);
        // digitalWrite(IN2, LOW);
        // digitalWrite(IN3, LOW);
        // digitalWrite(IN4, HIGH);

        digitalWrite(BR_IN1, HIGH);
        digitalWrite(BR_IN2, LOW);
        digitalWrite(BL_IN3, LOW);
        digitalWrite(BL_IN4, HIGH);

        digitalWrite(FR_IN1, HIGH);
        digitalWrite(FR_IN2, LOW);
        digitalWrite(FL_IN3, LOW);
        digitalWrite(FL_IN4, HIGH);
        break;
        
      case 'R':
        // Move Right (Rotate Motor A backward, Motor B forward)
        // digitalWrite(IN1, LOW);
        // digitalWrite(IN2, HIGH);
        // digitalWrite(IN3, HIGH);
        // digitalWrite(IN4, LOW);

        digitalWrite(BR_IN1, LOW);
        digitalWrite(BR_IN2, HIGH);
        digitalWrite(BL_IN3, HIGH);
        digitalWrite(BL_IN4, LOW);

        digitalWrite(FR_IN1, LOW);
        digitalWrite(FR_IN2, HIGH);
        digitalWrite(FL_IN3, HIGH);
        digitalWrite(FL_IN4, LOW);
        break;
        
      case 'F':
        // Move Forward (Rotate both motors forward)
        // digitalWrite(IN1, HIGH);
        // digitalWrite(IN2, LOW);
        // digitalWrite(IN3, HIGH);
        // digitalWrite(IN4, LOW);

        digitalWrite(BR_IN1, HIGH);
        digitalWrite(BR_IN2, LOW);
        digitalWrite(BL_IN3, HIGH);
        digitalWrite(BL_IN4, LOW);

        digitalWrite(FR_IN1, HIGH);
        digitalWrite(FR_IN2, LOW);
        digitalWrite(FL_IN3, HIGH);
        digitalWrite(FL_IN4, LOW);
        break;
        
      case 'B':
        // Move Backward (Rotate both motors backward)
        // digitalWrite(IN1, LOW);
        // digitalWrite(IN2, HIGH);
        // digitalWrite(IN3, LOW);
        // digitalWrite(IN4, HIGH);

        digitalWrite(BR_IN1, LOW);
        digitalWrite(BR_IN2, HIGH);
        digitalWrite(BL_IN3, LOW);
        digitalWrite(BL_IN4, HIGH);

        digitalWrite(FR_IN1, LOW);
        digitalWrite(FR_IN2, HIGH);
        digitalWrite(FL_IN3, LOW);
        digitalWrite(FL_IN4, HIGH);
        break;
        
      case 'S':
        // Stop both motors
        // digitalWrite(IN1, LOW);
        // digitalWrite(IN2, LOW);
        // digitalWrite(IN3, LOW);
        // digitalWrite(IN4, LOW);

        digitalWrite(BR_IN1, LOW);
        digitalWrite(BR_IN2, LOW);
        digitalWrite(BL_IN3, LOW);
        digitalWrite(BL_IN4, LOW);

        digitalWrite(FR_IN1, LOW);
        digitalWrite(FR_IN2, LOW);
        digitalWrite(FL_IN3, LOW);
        digitalWrite(FL_IN4, LOW);
        break;
      
    }
  }
}
