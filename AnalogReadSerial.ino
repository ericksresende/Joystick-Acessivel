void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  Serial.begin(9600);

}
int estado_up;
int estado_left;
int estado_right;
int estado_down;
int estado_pause;
int estado_end;

void loop() {
  estado_up = digitalRead(2);
  estado_left = digitalRead(3);
  estado_right = digitalRead(5);
  estado_down = digitalRead(4);
  estado_pause = digitalRead(12);
  estado_end = digitalRead(13);
  if (estado_up==0){
   Serial.println("up");
  }
  if (estado_left==0){
   Serial.println("left");
  }
  if (estado_right==0){
   Serial.println("right");
  }
  if (estado_down==0){
   Serial.println("down");
  }
  if (estado_pause==0){
   Serial.println("pause");
  }
  if (estado_end==0){
   Serial.println("end");
  }
  _delay_ms(50);
}
