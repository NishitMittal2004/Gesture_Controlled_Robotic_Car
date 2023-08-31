char command;  // Variable to store the received command

int IN1 = 5;
int IN2 = 6;

int IN3 = 7;
int IN4 = 8;


void setup() {
  Serial.begin(9600);  
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();  // Read the incoming command
    Serial.print("Received: ");
    Serial.println(command);
    
    
    switch (command) {
      case 'L':
        // Code to perform action for 'Left' gesture
        digitalWrite(5, HIGH);
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(8, HIGH);
        // delay(1000);                    
        break;
      case 'R':
        // Code to perform action for 'Right' gesture
        digitalWrite(5,LOW);
        digitalWrite(6,HIGH);
        digitalWrite(7,HIGH);
        digitalWrite(8,LOW);
        // delay(1000);                      
        break;
      case 'F':
        // Code to perform action for 'Forward' gesture
        digitalWrite(5,LOW);
        digitalWrite(6,HIGH);
        digitalWrite(7,LOW);
        digitalWrite(8,HIGH);
        // delay(1000);                  
        break;
      case 'B':
        // Code to perform action for 'Backward' gesture
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        // delay(1000);
        break;
      // ... (other cases if needed)
      case 'S':
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        // delay(1000);                      
        break;
    }
  }
  
  // ... (other loop code)
}
