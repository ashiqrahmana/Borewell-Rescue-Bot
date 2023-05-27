//simple Tx on pin D12
//Written By : Mohannad Rawashdeh
// 3:00pm , 13/6/2013
//http://www.genotronex.com/
//..................................
#include <VirtualWire.h>
void setup()
{
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_set_rx_pin(12);
    vw_setup(4000);  // Bits per sec
    pinMode(13, OUTPUT);

    vw_rx_start();       // Start the receiver PLL running
    Serial.begin(9600);
}
    void loop()
{
//  Serial.println("hi");
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;

    if (vw_get_message(buf, &buflen)) // Non-blocking
    {
      if(buf[0]=='0'){
Serial.print("***water level low***");
   Serial.println("   recorded level is below 1cm");
   Serial.println("");
   digitalWrite(13,1);
      }  
   if(buf[0]=='1'){
Serial.print("***water level rising***");
   Serial.println("   recorded level is between 2-5cm");
   Serial.println("");
  digitalWrite(13,0);
    }

     if(buf[0]=='2'){

  Serial.print("***water level rising***");
   Serial.println("   recorded level is between 5-10cm");
   Serial.println("");
   digitalWrite(13,1);
      }  

       if(buf[0]=='3'){

    Serial.print("***allart!!! water lavel passed danger level, get is open now***");
   Serial.println("   recorded level is over 10cm");
   Serial.println("");
   digitalWrite(13,1);
      }  

}
}
