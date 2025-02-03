#include <TimeLib.h>
#include <TimeAlarms.h>
#include <Adafruit_NeoPixel.h>
#include <Arduino.h>
#include <stdint.h>
#include "SCMD.h"
#include "SCMD_config.h"  //Contains #defines for common SCMD register names and values
#include "Wire.h"


int fan = 8; //fan pin

int pump = 6; //pump pin

int numPixels = 16; //Led / neopixel settings 
int led = 9;
int pixelFormat = NEO_GRB + NEO_KHZ800;

Adafruit_NeoPixel *pixels;

AlarmId id;

SCMD myMotorDriver; //This creates the main object of one motor driver and connected peripherals.

void setup() {
  Serial.begin(9600);
  
  pinMode(8, INPUT_PULLUP); //Use to halt motor movement (ground)
  pinMode(pump, OUTPUT);
  pinMode(fan, OUTPUT);

  pixels = new Adafruit_NeoPixel(numPixels, led, pixelFormat);
  pixels->begin();

    //*****initialize the driver get wait for idle*****//
  while ( myMotorDriver.begin() != 0xA9 ) //Wait until a valid ID word is returned
  {
    Serial.println( "ID mismatch, trying again" );
    delay(500);
  }
  Serial.println( "ID matches 0xA9" );

  setTime(5, 59, 40, 1, 1, 11);  // set time to Saturday 8:29:00am Jan 1 2011

  // create the alarms, to trigger at specific times
  Alarm.alarmRepeat(4, 0, 0, pumpOn);
  Alarm.alarmRepeat(5, 0, 0, fanOn);
  Alarm.alarmRepeat(6, 0, 0, ledOn);
  Alarm.alarmRepeat(18, 0, 0, ledFanOff);
}

void loop() {
  //load bearing void loop dont ask why idfk
}


// functions to be called when an alarm triggers:
void pumpOn() {
  //pump needs to turn on 30s and then wait to let the plant soak up water
  //and then run in reverse to drain
}


void fanOn() {
}

void ledOn() {
  pixels->fill(pixels->Color(214, 83, 211), 0, 15);
  pixels->show();
  Serial.println("turn lights on");
}

void ledFanOff() {
  pixels->clear();
  pixels->show();

  pixels->clear();
  pixels->show();
  digitalWrite(fan, LOW);
  Serial.println("turn lights off");
}


void printDigits(int digits) {
  Serial.print(":");
  if (digits < 10)
    Serial.print('0');
  Serial.print(digits);
}