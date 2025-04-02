#include <dummy.h>

#include <TimeLib.h>
#include <TimeAlarms.h>
#include <Adafruit_NeoPixel.h>
#include <Arduino.h>
#include <stdint.h>
#include "SCMD.h"
#include "SCMD_config.h"  //Contains #defines for common SCMD register names and values
#include "Wire.h"
#include <FS.h>
#include <SPI.h>
#include <SD.h>


int fan = 32;  //fan pin

int i = 0;

int numPixels = 16;  //Led / neopixel settings
int led = 14;
int ledP = 33;
int pixelFormat = NEO_GRB + NEO_KHZ800;

Adafruit_NeoPixel *pixels;

AlarmId id;

SCMD myMotorDriver;  //This creates the main object of one motor driver and connected peripherals.

File settings;

const int numReadings = 10;   // Size of the array
char dataArray[numReadings];  // Array to hold the file contents (adjust size as needed)
float sensorReadings[numReadings];

void setup() {
  Serial.begin(115200);
  SD.begin(5);
  //while(!Serial);

  pinMode(27, INPUT_PULLUP);  //Use to halt motor movement (ground)



  pinMode(fan, OUTPUT);



  //NeoPixels ********************************************//
  pixels = new Adafruit_NeoPixel(numPixels, led, pixelFormat);
  pixels->begin();
  pinMode(ledP, OUTPUT);
  digitalWrite(ledP, HIGH);  //by default we want this set to high and then flash it to low to wipe pixels.
  //did this because the pixels wouldn't clear when told too and instead were displaying random garbled barf!





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




  Alarm.timerRepeat(dataArray[4], 0, 0, pumpFlush);
  Alarm.timerRepeat(dataArray[1], 0, 0, fanOn);
  Alarm.timerRepeat(dataArray[2], 0, 0, fanOff);
  Alarm.timerRepeat(dataArray[3], 0, 0, ledOn);
  Alarm.timerRepeat(dataArray[3], 0, 0, ledOff);

  Serial.print("Checking for Motor Controller");
  //*****initialize the driver get wait for idle*****//
  /*  while (myMotorDriver.begin() != 0xA9)  //Wait until a valid ID word is returned
  {
    Serial.println("ID mismatch, trying again");
    delay(500);
  }
  Serial.println("ID matches 0xA9");

  //  Check to make sure the driver is done looking for peripherals before beginning
  Serial.print("Waiting for enumeration...");
  while (myMotorDriver.ready() == false)
    ;
  Serial.println("Done.");*/
  Serial.println();

  SDtoArray(SD);  //moved the onstart file read to array to its own function
  arrayToSet();
}

#define PUMP_MOTOR 0
#define FAN 1

void loop() {                    //This is general functions for manual control of the NanoLab
  if (Serial.available() > 0) {  //Serial functions, it waits for the serial port to be avilible
    int DoThis = Serial.read();  // then switches case based on set the character sent.
                                 //mostly just for quickly turning something off/on to check if it works.
                                 //maxwell said 'yeehaw' to this and i dont know why
    switch (DoThis) {

      case 'I':
        Serial.println("Beginning Settings download");
        SD.remove("settings.txt");
        while (i <= numReadings) {
          if (Serial.available() > 0) {
            Serial.println("reciveing . . .");
            float reading = Serial.parseFloat();  // Read incoming settings

            // Store the reading in the array

            sensorReadings[i] = reading;

            Serial.println(sensorReadings[i]);

            i++;

            if (i >= numReadings) {

              saveToSD(SD);

              i == 0;  // Reset i after saving
            }
          }
        }
        Serial.println("download done");
        break;

      case 'L':
        pixels->fill(pixels->Color(214, 83, 211), 0, 15);
        delay(10000);
        digitalWrite(ledP, LOW);
        delay(1000);
        digitalWrite(ledP, HIGH);

        break;

      case 'P':
        myMotorDriver.setDrive(PUMP_MOTOR, 0, 50);
        delay(3000);
        myMotorDriver.setDrive(PUMP_MOTOR, 0, 0);
        delay(1000);
        myMotorDriver.setDrive(PUMP_MOTOR, 1, 50);
        delay(3000);
        myMotorDriver.setDrive(PUMP_MOTOR, 0, 0);

        break;

      case 'F':
        myMotorDriver.setDrive(FAN, 0, 50);
        delay(3000);
        myMotorDriver.setDrive(FAN, 0, 0);

        break;
    }
  }
}

// functions to be called when an alarm triggers ************//

void pumpFlush() {
  //pump needs to turn on 30s and then wait to let the plant soak up water
  //and then run in reverse to drain
  myMotorDriver.setDrive(PUMP_MOTOR, 0, 50);
  delay(dataArray[3]);
  myMotorDriver.setDrive(PUMP_MOTOR, 0, 0);
  delay(dataArray[5]);
  myMotorDriver.setDrive(PUMP_MOTOR, 1, 50);
  delay(dataArray[3]);
  myMotorDriver.setDrive(PUMP_MOTOR, 0, 0);
}


void fanOn() {
  digitalWrite(fan, HIGH);
}

void fanOff() {
  digitalWrite(fan, LOW);
}

void ledOn() {
  pixels->fill(pixels->Color(214, 83, 211), 0, 15);
  pixels->show();
  Serial.println("turn lights on");
}

void ledOff() {
  digitalWrite(ledP, LOW);
  delay(100);
  digitalWrite(ledP, HIGH);
  Serial.println("turn lights off");
}



//SD Card ******************************//
void SDtoArray(fs::FS &fs) {

  if (!SD.begin(5)) {
    Serial.println("No SD card");
    while (1)
      ;
  }
  Serial.println("SD Connected");  //this check passes

  const int numReadings = 10;   // Size of the array
  char dataArray[numReadings];  // Array to hold the file contents (adjust size as needed)


  // Settings Load Function ******************//
  settings = fs.open("settings.txt" FILE_WRITE);  // i dont know why but this wont open the file? i dont have a solution atm
  //im attempting to use file open directly from the FS library like how SD_test does, because it actually works for some reason, but im clearly missing something.
  //also i wonder if SD_test is referencing another sketch.


  if (settings) {
    int index = 0;

    while (settings.available() && index < sizeof(dataArray) - 1) {
      dataArray[index] = settings.read();  // Read character by character
      index++;
    }

    dataArray[index] = '\0';  // Null-terminate the array
    settings.close();


    Serial.println(dataArray);
  } else {
    Serial.println("Error opening settings.txt");
  }
}



void arrayToSet() {
  //Time And date and Alarms ******************************//
  setTime(5, 59, 40, 1, 1, 11);  // set time to Saturday 8:29:00am Jan 1 2011
  // create the alarms, to trigger at specific times
  Alarm.timerRepeat(dataArray[4], 0, 0, pumpFlush);
  Alarm.timerRepeat(dataArray[1], 0, 0, fanOn);
  Alarm.timerRepeat(dataArray[2], 0, 0, fanOff);
  Alarm.timerRepeat(dataArray[3], 0, 0, ledOn);
  Alarm.timerRepeat(dataArray[3], 0, 0, ledOff);  //arrays are 0 indexed, the 0th possition is used to check if the array has been loaded or not
}



void saveToSD(fs::FS &fs) {

  File settings = fs.open("settings.txt", FILE_WRITE);
  if (!settings) {
    Serial.println("unable to open file");
  } else {
    Serial.print("File opened");
  }

  if (settings) {

    for (int i = 0; i < numReadings; i++) {

      settings.print(sensorReadings[i]);

      settings.print(",");  // CSV format
    }

    settings.println();  // New line after each batch of readings

    settings.close();

    Serial.println("Data saved to SD card.");

  } else {

    Serial.println("Error opening file on SD card.");
  }
}
