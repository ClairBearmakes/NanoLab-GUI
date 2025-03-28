#include <dummy.h>

#include <TimeLib.h>
#include <TimeAlarms.h>
#include <Adafruit_NeoPixel.h>
#include <Arduino.h>
#include <stdint.h>
#include "SCMD.h"
#include "SCMD_config.h"  //Contains #defines for common SCMD register names and values
#include "Wire.h"
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

File dataFile;

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

  //SD Card ******************************//
  if (!SD.begin(5)) {
    Serial.println("No SD card");
    while (1)
      ;
  }
  Serial.println("SD Connected");  //this check passes

  const int numReadings = 10;   // Size of the array
  char dataArray[numReadings];  // Array to hold the file contents (adjust size as needed)


  // Settings Load Function ******************//
  File dataFile = SD.open("data.txt" FILE_WRITE);  // i dont know why but this wont open the file? i dont have a solution atm


  if (dataFile) {
    int index = 0;

    while (dataFile.available() && index < sizeof(dataArray) - 1) {
      dataArray[index] = dataFile.read();  // Read character by character
      index++;
    }

    dataArray[index] = '\0';  // Null-terminate the array
    dataFile.close();


    Serial.println(dataArray);
  } else {
    Serial.println("Error opening data.txt");
  }


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
  Serial.println("Done.");
  Serial.println();     

  */
}

#define PUMP_MOTOR 0
#define FAN 1

void loop() {                    //This is general functions for manual control of the NanoLab
  if (Serial.available() > 0) {  //Serial functions, it waits for the serial port to be avilible
    int DoThis = Serial.read();  // then switches case based on set the character sent

    switch (DoThis) {

      case 'I':   // Maxwell, can you help me understand why this function wont enter the 'while' loop? the intent is to iterate throught the sent imformation and asign it to the array.
        Serial.println("Beginning Settings download");

        while (i >= numReadings) {
          //if (Serial.available() > 0) {
            Serial.println("reciveing . . .");
            float reading = Serial.parseFloat();  // Read incoming data
            // Store the reading in the array

            sensorReadings[i] = reading;

            Serial.println(sensorReadings[i]);

            i++;

            if (i >= numReadings) {

              saveToSD();

              i == 0;  // Reset i after saving
            }
          //}
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



void saveToSD() {

  File dataFile = SD.open("data.txt", FILE_WRITE);
  if (!dataFile) {
    Serial.println("unable to open file");
  } else {
    Serial.print("File opened");
  }

  if (dataFile) {

    for (int i = 0; i < numReadings; i++) {

      dataFile.print(sensorReadings[i]);

      dataFile.print(",");  // CSV format
    }

    dataFile.println();  // New line after each batch of readings

    dataFile.close();

    Serial.println("Data saved to SD card.");

  } else {

    Serial.println("Error opening file on SD card.");
  }
}
