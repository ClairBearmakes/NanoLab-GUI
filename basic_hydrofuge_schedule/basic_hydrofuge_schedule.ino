#include <TimeLib.h>
#include <TimeAlarms.h>
#include <Adafruit_NeoPixel.h>
#include <Arduino.h>
#include <stdint.h>
#include "SCMD.h"
#include "SCMD_config.h"  //Contains #defines for common SCMD register names and values
#include "Wire.h"


int fan = 8;  //fan pin

int pump = 6;  //pump pin

int numPixels = 16;  //Led / neopixel settings
int led = 9;
int pixelFormat = NEO_GRB + NEO_KHZ800;

Adafruit_NeoPixel *pixels;

AlarmId id;

SCMD myMotorDriver;  //This creates the main object of one motor driver and connected peripherals.

void setup() {
  Serial.begin(9600);

  pinMode(8, INPUT_PULLUP);  //Use to halt motor movement (ground)
  pinMode(pump, OUTPUT);
  pinMode(fan, OUTPUT);
  
  //NeoPixels ********************************************//
  pixels = new Adafruit_NeoPixel(numPixels, led, pixelFormat);
  pixels->begin();



  //***** Configure the Motor Driver's Settings *****//
  //  .commInter face is I2C_MODE
  myMotorDriver.settings.commInterface = I2C_MODE;

  //  set address if I2C configuration selected with the config jumpers
  myMotorDriver.settings.I2CAddress = 0x5D;  //config pattern is "1000" (default) on board for address 0x5D

  //  set chip select if SPI selected with the config jumpers
  myMotorDriver.settings.chipSelectPin = 10;


  //Time And date and Alarms ******************************//
  setTime(5, 59, 40, 1, 1, 11);  // set time to Saturday 8:29:00am Jan 1 2011
  // create the alarms, to trigger at specific times
  Alarm.alarmRepeat(4, 0, 0, pumpOn);
  Alarm.alarmRepeat(5, 0, 0, fanOn);
  Alarm.alarmRepeat(6, 0, 0, ledOn);
  Alarm.alarmRepeat(18, 0, 0, ledFanOff);



  //*****initialize the driver get wait for idle*****//
  while (myMotorDriver.begin() != 0xA9)  //Wait until a valid ID word is returned
  {
    Serial.println("ID mismatch, trying again");
    delay(500);
  }
  Serial.println("ID matches 0xA9");

  //  Check to make sure the driver is done looking for peripherals before beginning
  Serial.print("Waiting for enumeration...");
  while (myMotorDriver.ready() == false)
    ;
  Serial.println("Done.");
  Serial.println();
}

#define LEFT_MOTOR 0
#define RIGHT_MOTOR 1

void () {}
  //load bearing void loop dont ask why idfk


// functions to be called when an alarm triggers ************//

void pumpOn() {
  //pump needs to turn on 30s and then wait to let the plant soak up water
  //and then run in reverse to drain
  myMotorDriver.setDrive(LEFT_MOTOR, 0, 50);
  delay(30000);
  myMotorDriver.setDrive(LEFT_MOTOR, 0, 0);
  delay(120000);
  myMotorDriver.setDrive(LEFT_MOTOR, 1, 50);
  delay(30000);
  myMotorDriver.setDrive(LEFT_MOTOR, 0, 0);
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