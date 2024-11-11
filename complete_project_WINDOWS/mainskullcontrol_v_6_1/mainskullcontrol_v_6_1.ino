
/*
  Dale Shisler 4/18/2014
  operates Chad the Head
 */




#include <Servo.h> 
 
Servo neck;  // create servo object to control a servo              
int t = 0;
int pos = 0;    // variable to store the servo position 
int mouth = 5;
int eyes = 6;
int lfastness = 255;    // motor speeds
int rfastness = 255;

int in1=8;     // motor pins
int in2=11;
int in3=12;
int in4=13;
int motospedA = 9;
int motospedB = 10;
int talk=0;
int notalk=1;


void setup() {
  // initialize serial communication:
  Serial.begin(115200); 
      
  pinMode(eyes, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(motospedA, OUTPUT);
  pinMode(motospedB, OUTPUT);
  
 
  pinMode(mouth, OUTPUT);
  pinMode(eyes, OUTPUT);
  neck.attach(3);
  pinMode(eyes, OUTPUT);
  pinMode(4, OUTPUT);     
  pinMode(2, OUTPUT);
  
}

void loop() {
  // read the sensor:
 
   talk = analogRead(A5);
  if (talk>32) {

  digitalWrite(mouth, HIGH);  
  delay(15+(talk*2));               // 
  digitalWrite(mouth, LOW);   
  delay(20+(talk*2)); 
 
  }
 
 
 
 
  if (Serial.available() > 0) {      // read incoming information
    int DoThis = Serial.read();      
    
 //----------------------------ping------------------------   
  
  
    
 //--------------------------case-----------------------------------   

    switch (DoThis) {
      
     
    case 'a':    //------------------------a------ eyes on
        digitalWrite(eyes, HIGH);
      break;
    case 'o':    //-------------------------o------eyes off
      digitalWrite(eyes, LOW);
      break;
 
    case 'd':    //---------------------------d----moves neck back
      for(pos = 180; pos > 0; pos -= 1)  {                                  
        neck.write(pos); 
        delay(3);  
        }
    break;
    
    case 'e':    //---------------------------e-----moves neck foward
       for(pos = 0; pos<=180; pos +=1)  {                                
        neck.write(pos);               
        delay(3);                     
        }
     break;
    
     case 'l':    
        digitalWrite(in1,HIGH); // left motor -----f---foward
        digitalWrite(in2, LOW);
         analogWrite(motospedA,lfastness);
      break;
 
     case 'h':    
        digitalWrite(in1,LOW); // left motor -----h----halt
        digitalWrite(in2, LOW);
       
        digitalWrite(in3, LOW);//right motor
        digitalWrite(in4, LOW);
       break;
       
      case 'r':
        digitalWrite(in3,HIGH); // right motor ------r-----right
        digitalWrite(in4, LOW);
        analogWrite(motospedB,rfastness);
       break;
      
       case 'R':
        digitalWrite(in3,LOW); // right motor -----R-----spin backward
        digitalWrite(in4, HIGH);
        analogWrite(motospedB,rfastness);
        break;
       case 'A':
        digitalWrite(in3, LOW);//right motor halt
        digitalWrite(in4, LOW);
         //digitalWrite(motospedB, HIGH);
        break;
       case 'L':
        digitalWrite(in1,LOW); // left motor ------L----spin left
        digitalWrite(in2, HIGH);
         analogWrite(motospedA,lfastness);
         break;
       case 'B':
        digitalWrite(in1, LOW);//right motor
        digitalWrite(in2, LOW);
         //digitalWrite(motospedB, HIGH);
       break;
    case 'b':
        digitalWrite(in1,LOW); // left motor ------b----------backward
        digitalWrite(in2, HIGH);
        analogWrite(motospedB,lfastness);

       digitalWrite(in3, LOW);//right motor
       digitalWrite(in4, HIGH);
       analogWrite(motospedB,rfastness);
       break;
   case 'w':         //---------------------------w------ run eyes back and foth
         
    digitalWrite(eyes,HIGH); 
    delay(500);
    digitalWrite(4,LOW);  
    digitalWrite(2,LOW);  
    digitalWrite(2,HIGH);
    delay(500);  
    digitalWrite(2,LOW);
    delay(1000);
    digitalWrite(4,HIGH);  
      delay(500);
    digitalWrite(4,LOW);
    delay(1000);
  
    digitalWrite(2,HIGH);   
    delay(200);
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(eyes,LOW);
   break;
      
    } 
  }

}
=======
/*
  Dale Shisler 4/18/2014
  operates Chad the Head
 */




#include <Servo.h> 
 
Servo neck;  // create servo object to control a servo              
int t = 0;
int pos = 0;    // variable to store the servo position 
int mouth = 5;
int eyes = 6;
int lfastness = 255;    // motor speeds
int rfastness = 255;

int in1=8;     // motor pins
int in2=11;
int in3=12;
int in4=13;
int motospedA = 9;
int motospedB = 10;
int talk=0;
int notalk=1;


void setup() {
  // initialize serial communication:
  Serial.begin(115200); 
      
  pinMode(eyes, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(motospedA, OUTPUT);
  pinMode(motospedB, OUTPUT);
  
 
  pinMode(mouth, OUTPUT);
  pinMode(eyes, OUTPUT);
  neck.attach(3);
  pinMode(eyes, OUTPUT);
  pinMode(4, OUTPUT);     
  pinMode(2, OUTPUT);
  
}

void loop() {
  // read the sensor:
 
   talk = analogRead(A5);
  if (talk>32) {

  digitalWrite(mouth, HIGH);  
  delay(15+(talk*2));               // 
  digitalWrite(mouth, LOW);   
  delay(20+(talk*2)); 
 
  }
 
 
 
 
  if (Serial.available() > 0) {      // read incoming information
    int DoThis = Serial.read();      
    
 //----------------------------ping------------------------   
  
  
    
 //--------------------------case-----------------------------------   

    switch (DoThis) {
      
     
    case 'a':    //------------------------a------ eyes on
        digitalWrite(eyes, HIGH);
      break;
    case 'o':    //-------------------------o------eyes off
      digitalWrite(eyes, LOW);
      break;
 
    case 'd':    //---------------------------d----moves neck back
      for(pos = 180; pos > 0; pos -= 1)  {                                  
        neck.write(pos); 
        delay(3);  
        }
    break;
    
    case 'e':    //---------------------------e-----moves neck foward
       for(pos = 0; pos<=180; pos +=1)  {                                
        neck.write(pos);               
        delay(3);                     
        }
     break;
    
     case 'l':    
        digitalWrite(in1,HIGH); // left motor -----f---foward
        digitalWrite(in2, LOW);
         analogWrite(motospedA,lfastness);
      break;
 
     case 'h':    
        digitalWrite(in1,LOW); // left motor -----h----halt
        digitalWrite(in2, LOW);
       
        digitalWrite(in3, LOW);//right motor
        digitalWrite(in4, LOW);
       break;
       
      case 'r':
        digitalWrite(in3,HIGH); // right motor ------r-----right
        digitalWrite(in4, LOW);
        analogWrite(motospedB,rfastness);
       break;
      
       case 'R':
        digitalWrite(in3,LOW); // right motor -----R-----spin backward
        digitalWrite(in4, HIGH);
        analogWrite(motospedB,rfastness);
        break;
       case 'A':
        digitalWrite(in3, LOW);//right motor halt
        digitalWrite(in4, LOW);
         //digitalWrite(motospedB, HIGH);
        break;
       case 'L':
        digitalWrite(in1,LOW); // left motor ------L----spin left
        digitalWrite(in2, HIGH);
         analogWrite(motospedA,lfastness);
         break;
       case 'B':
        digitalWrite(in1, LOW);//right motor
        digitalWrite(in2, LOW);
         //digitalWrite(motospedB, HIGH);
       break;
    case 'b':
        digitalWrite(in1,LOW); // left motor ------b----------backward
        digitalWrite(in2, HIGH);
        analogWrite(motospedB,lfastness);

       digitalWrite(in3, LOW);//right motor
       digitalWrite(in4, HIGH);
       analogWrite(motospedB,rfastness);
       break;
   case 'w':         //---------------------------w------ run eyes back and foth
         
    digitalWrite(eyes,HIGH); 
    delay(500);
    digitalWrite(4,LOW);  
    digitalWrite(2,LOW);  
    digitalWrite(2,HIGH);
    delay(500);  
    digitalWrite(2,LOW);
    delay(1000);
    digitalWrite(4,HIGH);  
      delay(500);
    digitalWrite(4,LOW);
    delay(1000);
  
    digitalWrite(2,HIGH);   
    delay(200);
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(eyes,LOW);
   break;
      
    } 
  }

}

