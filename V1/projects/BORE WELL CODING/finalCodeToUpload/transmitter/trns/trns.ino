#include <VirtualWire.h>
#include <NewPing.h>
#define TRIGGER_PIN  6   // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     9  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
int a=0;
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.




char *controller;
void setup() {
Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
  pinMode(11,OUTPUT);
  pinMode(13,OUTPUT);
vw_set_ptt_inverted(true); //
vw_set_tx_pin(12);
vw_setup(4000);// speed of data transfer Kbps
}

void loop(){
  a=sonar.ping_cm();
  Serial.println(a);
delay(2000);
  if(a>58){
  controller="0";
vw_send((uint8_t *)controller, strlen(controller));
vw_wait_tx(); // Wait until the whole message is gone

digitalWrite(11,0);
    }
    delay(500);
if (a>55 && a<59 ){
    controller="1"  ;
vw_send((uint8_t *)controller, strlen(controller));
vw_wait_tx(); // Wait until the whole message is gone

digitalWrite(11,0);
  }
delay(500);

if( a>50 && a<56){
   controller="2"  ;
vw_send((uint8_t *)controller, strlen(controller));
vw_wait_tx(); // Wait until the whole message is gone

digitalWrite(11,0);
 }
 delay(500);
 if(a<51){controller="3"  ;
vw_send((uint8_t *)controller, strlen(controller));
vw_wait_tx(); // Wait until the whole message is gone

digitalWrite(11,1);

}
 delay(500);


}
