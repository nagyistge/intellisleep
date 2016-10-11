#include <Wire.h>

#define SENSOR_NUM 6

int norm_min, norm_max;
struct stretch_sensor {

  int pin = -1;
  int min_value = 10000;
  int max_value = 0 ;
  int cur_value;
  byte scaled_value;
};

stretch_sensor sensors[SENSOR_NUM];
byte data[SENSOR_NUM];

void setup() {
  // put your setup code here, to run once:

 Serial.begin(9600); //Setup serial communication
 for(int i = 0; i<SENSOR_NUM; i++) {
  switch(i) {
    case 0: sensors[i].pin = A0; break;
    case 1: sensors[i].pin = A1; break;
    case 2: sensors[i].pin = A2; break;
    case 3: sensors[i].pin = A3; break;
    case 4: sensors[i].pin = A4; break;
    case 5: sensors[i].pin = A5; break;
  } 
 }

}

void loop() {
  // put your main code here, to run repeatedly:
  
for(int i = 0; i<SENSOR_NUM; i++) {
  sensors[i].cur_value = analogRead(sensors[i].pin);
  if(sensors[i].cur_value > sensors[i].max_value) {
    sensors[i].max_value = sensors[i].cur_value;
  }
  else if(sensors[i].cur_value < sensors[i].min_value) {
    sensors[i].min_value = sensors[i].cur_value;
  }
  sensors[i].scaled_value = (255*(sensors[i].cur_value - sensors[i].min_value))/(sensors[i].max_value - sensors[i].min_value);
  data[i] = sensors[i].scaled_value;
  Serial.print(sensors[i].min_value); Serial.print("; "); Serial.print(data[i]); Serial.print("; "); Serial.print(sensors[i].max_value); Serial.print("; ");
}
//Serial.write(data, SENSOR_NUM);
Serial.println();

}
