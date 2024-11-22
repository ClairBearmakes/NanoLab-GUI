#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

int pin = 6;

int numPixels =16; 

int pixelFormat = NEO_GRB + NEO_KHZ800;

int i = 0;

int p = 0;

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

          for(i<numPixels; i++;)
          {
           
            pixels->setPixelColor(i, pixels->Color(50, 0, 0));
            
            delay(10);
          }
        pixels->show();
      break;

      case 'O' :
        pixels->clear();
        pixels->show();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(50, 10, 0));
            
          }
        pixels->show();
      break;

      case 'Y' :
        pixels->clear();
        pixels->show();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(50, 25, 0));
            
          }
        pixels->show();
      break;

      case 'G' :
        pixels->clear();
        pixels->show();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(0, 50, 0));
          }
        pixels->show();
      break;
      
      case 'B' :
        pixels->clear();
        pixels->show();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(0, 0, 50));
          }
        pixels->show();
        
      break;

      case 'P' :
        pixels->clear();
        pixels->show();
          for(i<numPixels; i++;)
          {
            pixels->setPixelColor(i, pixels->Color(50, 0, 50));
            
          }
        pixels->show();
      break;



      case 'C' :
        i = 0;
        pixels->clear();
        pixels->show();
      break;

    }


 }

}