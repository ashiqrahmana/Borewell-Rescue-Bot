void setup() {
  // put your setup code here, to run once:
pinMode(10,INPUT);
pinMode(11,INPUT);
pinMode(3,OUTPUT);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
pinMode(9,OUTPUT);
pinMode(5,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int front=digitalRead(10);
  int side=digitalRead(11);
  if (front==HIGH)
  {
    digitalWrite(3,HIGH);
    digitalWrite(9,LOW);
  }
  else if (front==LOW)
  {
    digitalWrite(3,LOW);
    digitalWrite(9,HIGH);
  }
  if (side== HIGH)
  {
    digitalWrite(5,LOW);
    digitalWrite(9,HIGH); 
  }
  
  else if (side== LOW)
  {
    digitalWrite(5,HIGH);
    digitalWrite(9,LOW); 
  }
  else{
    
    digitalWrite(5,LOW);
    digitalWrite(9,LOW);
    
    digitalWrite(3,LOW);
    digitalWrite(9,LOW);
  }
}
