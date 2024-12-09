#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

int pin = 6;

int numPixels =16; 

int pixelFormat = NEO_GRB + NEO_KHZ800;

int i = 0;

int RVar = 0;

int GVar = 0;

int BVar = 0;

Adafruit_NeoPixel *pixels;

#define DELAYVAL 500


void setup() {
  // put your setup code here, to run once:
  pixels = new Adafruit_NeoPixel(numPixels, pin, pixelFormat);

  pixels->begin();

  Serial.begin(9600);

  

  
}

void loop() {

  

 if (Serial.available() > 0) {
    int DoThis = Serial.read();
    
    switch (DoThis) {
      
      case 'R' :
        pixels->clear();
        pixels->show();
          while 
          RVar = Serial.read();

          for(i<numPixels; i++;)
          {
           
            pixels->setPixelColor(i, pixels->Color(RVar, GVar, BVar));
            
            
          
          }
        pixels->show();
      break;

      case 'C' :
        pixels->clear();
        pixels->show();

          RVar = Serial.read();

          {
           
            pixels->setPixelColor(i, pixels->Color(0, 0, 0));
          
          }
        pixels->show();
        break;


    }
  }
}