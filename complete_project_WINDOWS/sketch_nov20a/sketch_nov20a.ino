#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

int pin = 6;

int numPixels =16; 

int pixelFormat = NEO_GRB + NEO_KHZ800;

int i = 0;

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
      
      case '1' :
        pixels->clear();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(50, 0, 0));
            
          }
        pixels->show();
      break;

      case '2' :
        pixels->clear();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(0, 50, 0));
          }
        pixels->show();
      break;
      
      case '3' :
        pixels->clear();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(0, 0, 50));
          }
        pixels->show();
      break;

      case '0' :
        i = 0;
        pixels->clear();
        pixels->show();
      break;

    }


 }

}