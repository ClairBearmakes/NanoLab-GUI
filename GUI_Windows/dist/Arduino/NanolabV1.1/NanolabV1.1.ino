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

  pixels->fill(pixels->Color(214, 83, 211), 0, 15); //this is the colour the lights glow
                                          //i found the rgb on reddit if its not optimal than ¯\_(ツ)_/¯

  
}

void loop() {

  

 if (Serial.available() > 0) {
    int DoThis = Serial.read();
    
    switch (DoThis) {
      
      case 'R' :
     
      pixels->fill(pixels->Color(214, 83, 211), 0, 15);
      pixels->show();
      
      break;
      
      case 'T' :
     
      Serial.println(pixels->getPixelColor(0));
      
      break;
      
      case 'C' :
        pixels->clear();
        pixels->show();
        
         

        
        break;


    }
  }
}