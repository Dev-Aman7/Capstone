int x,y,z;

void joy()
{
  x=analogRead(A0);
  y=analogRead(A1);
  if(  x<600 && y>900)
  {Serial.println("up");}
else if(x<600 && y<200)
  {Serial.println("down");}
else if(x<400 && y<600)
  {Serial.println("left");}
else if(x>600 && y<600)
  {Serial.println("right");}
else
  {Serial.println("stop");}
  Serial.print(x);
  Serial.print("  ");
  Serial.println(y);
  //Serial.println("Down");
}
void setup() {
  Serial.begin(9600);

}
//bool button=false;
void loop() {
  joy();
  delay(100);
}
