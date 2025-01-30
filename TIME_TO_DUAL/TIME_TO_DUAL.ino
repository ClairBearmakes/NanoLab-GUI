//Written by Ruben Marc Speybrouck
#include <Adafruit_NeoPixel.h>

int Ptime = 15;

int pin = 4;

int numPixels =16;

int pixelFormat = NEO_GRB + NEO_KHZ800;

int i = 0;

Adafruit_NeoPixel *pixels;

#define DELAYVAL 500

int pump = 16;

int fan = 17;

unsigned long bootSeconds = 0;

unsigned long bootSecondsLast = 0;

//Time start Settings:

int startingHour = 5;

// set your starting hour here, not below at int hour. This ensures accurate daily correction of time

int seconds = 0;

int minutes = 58;

int hours = startingHour;

int days = 0;

//Accuracy settings

int dailyErrorFast = 0; // set the average number of milliseconds your microcontroller's time is fast on a daily basis

int dailyErrorBehind = 0; // set the average number of milliseconds your microcontroller's time is behind on a daily basis

int correctedToday = 1; // do not change this variable, one means that the time has already been corrected today for the error in your boards crystal. This is true for the first day because you just set the time when you uploaded the sketch.

/////////////////////////////////////////////////
// declare time-tracking functions for later use
/////////////////////////////////////////////////

bool incrSeconds();
bool incrMinutes();
bool incrHours();
bool incrDays();

///////////////////////////////////////////////////
// NOTE: I changed indentation to be clearer below
///////////////////////////////////////////////////

void setup() { // put your setup code here, to run once:

    pinMode(pump, OUTPUT);

    pixels = new Adafruit_NeoPixel(numPixels, pin, pixelFormat);

    pixels->begin();

    Serial.begin(115200); 

    pixels->fill(pixels->Color(84, 64, 205)); //this is the colour the lights glow
                                              //i found the rgb on reddit if its not optimal than ¯\_(ツ)_/¯

}


void loop() { // put your main code here, to run repeatedly:

    // NOTE: millis() is a special system function
    //
    //      "Returns the number of milliseconds passed since the Arduino
    //      board began running the current program.  This number will overflow
    //      (go back to zero), after approximately 50 days."
    //

    // update the total seconds after boot.  (NOTE: okay that it stores same value on most loops)
    bootSeconds = millis()/1000; // keep always-correct count on booted seconds, but it will roll back to zero

    // 
    // update "event" flags for use later
    //
    bool newSecond =              incrSeconds();
    bool newMinute = newSecond && incrMinutes();
    bool newHour   = newMinute && incrHours();
    bool newDay    = newHour   && incrDays();

    // NOW: runs only *once* for each new second, minute, hour, day  
    //    if (newSecond)  ....
    //    if (newMinute)  ....
    //    if (newHour)  ....
    //    if (newDay)  ....

    ///////////////////////////////////////////////////////////////////////////////////
    // vvvvvvvvvvvvvvvvvvvvv CHANGE BELOW TO USE EVENT-FLAGS vvvvvvvvvvvvvvvvvvvvv
    ///////////////////////////////////////////////////////////////////////////////////

    //if 24 hours have passed, add one day

    if (hours ==(24 - startingHour) && correctedToday == 0){

        delay(dailyErrorFast*1000);

        seconds = seconds + dailyErrorBehind;

        correctedToday = 1; } 

    //every time 24 hours have passed since the initial starting time
    // and it has not been reset this day before, add milliseconds or
    // delay the program with some milliseconds.

    //Change these varialbes according to the error of your board.

    // The only way to find out how far off your boards internal clock is,
    // is by uploading this sketch at exactly the same time as the real time,
    // letting it run for a few days and then determining how many
    // seconds slow/fast your boards internal clock is on a daily
    // average. (24 hours).

    // Let the sketch know that a new day has started for what concerns
    // correction, if this line was not here the arduiono would continue
    // to correct for an entire hour that is 24 - startingHour.

    if (hours == 24 - startingHour + 2) {

        correctedToday = 0; }

    //let the sketch know that a new day has started for what concerns
    // correction, if this line was not here the arduiono would continue
    // to correct for an entire hour that is 24 - startingHour.

    switch (hours) {

        case 4:
          /// FIXME: DANGER DANGER DANGER.  loop() is already a good-enough loop!!!
          //
          //  ALL SUB-LOOPS MUST *START* AND *END* THEMSELVES WITH ONLY IN-LOOP CODE ALONE.
          //  Repeated actions in a loop need very good reason to BLOCK all other code. 
          //
          //  Most repeated things normally work by *sharing* one huge "event-loop" and turning on 
          //  and off what is needed to repeat.   These "on" and "off" decisions are then all that are
          //  needed to do correctly.  No more sub-loops are needed unless one task requires 
          //  everything else wait.
          //
          //  NOTE: any across-loop-iteration memory must be declared *outside* the loop() function to 
          //  stay the same.   Anything declared inside the loop() function is forgotten each time.
          // 
          //  Many activities can all *share* one large "event-loop" to keep any housekeeping activities.
          //  Things we think of can use it:  Delays, Spacing work out, Detecting big events.  One big loop.
          ////////
          while (minutes >= Ptime){ //turns the pump on for whatever Ptime is = too
            digitalWrite(pump, HIGH);
          }
          digitalWrite(pump, LOW);

          break;

        case 6: //this turns the light ring on
          pixels->setBrightness(255);
          pixels->show();
        break;

        case 8: //fan on 
          digitalWrite(fan, HIGH);
        break;


        case 18: //this turns the light ring off
          pixels->setBrightness(0);
          pixels->show();
        break; 

    }

    if (Serial.available() > 0) { //Serial functions, it waits for the serial port to be avilible 
        int DoThis = Serial.read(); // then switches case based on set the character sent

        switch (DoThis) {

          case 'L' : 
              pixels->setBrightness(50);
              pixels->show();
              break;

          case 'T' :
              Serial.print("The time is: ");

              Serial.print(days);

              Serial.print(":");

              Serial.print(hours);

              Serial.print(":");

              Serial.print(minutes);

              Serial.print(":");

              Serial.println(seconds);
              break;

        }

    }
}

bool incrSeconds() // the number of milliseconds that have passed since boot
{
    // same second?
    if (bootSeconds == bootSecondsLast) return false;          //// RETURN false

    ++seconds;         // jump normal seconds forward
    ++bootSecondsLast; // jump *handled* bootSeconds forward
    return true;
}

bool incrMinutes()
{
    // same minute?
    if (seconds < 60) return false;                            //// RETURN false

    ++minutes;
    seconds -= 60; // grab out one minute from seconds
    return true;
}

bool incrHours()
{
   /// try writing this using "minutes" "hours" and 60
}

bool incrDays()
{
   /// try writing this using "hours" "days" and 24
}
