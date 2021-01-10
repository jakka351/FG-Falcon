// This file is part of Ford FG HVAC Display.

// Ford FG HVAC Display is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// Ford FG HVAC Display is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with Ford FG HVAC Display.  If not, see <https://www.gnu.org/licenses/>.

 
// Ford FG HVAC Display - CAN to Serial
// 
// Heavily derived from MitchellH's source code available at https://fordforums.com.au/showthread.php?t=11430769
// 
// Created by Kyle May in 2018.

#include "df_can.h"
#include <SPI.h>
#include <SimpleTimer.h>

#define SDA_PORT PORTD
#define SCL_PORT PORTD
#define SDA_PIN 4
#define SCL_PIN 3

MCPCAN CAN(10);

// Vent Status
unsigned char ventCAN = 0b10101010;
// AC Temp
double acTempCAN = 25;
// Outside Temp
unsigned char outsideTempCAN = 12;
// Fan Speed
unsigned char fanSpeedCAN = 6;

unsigned char len = 0;
unsigned char buf[8];

// Variables to signal send message
byte Send738 = 0;
byte Send783 = 0;
byte Send785 = 0;
byte Send775 = 0;
byte Send777 = 0;
byte Send779 = 0;
byte Send1372 = 0;

//SimpleTimer tmr100ms;


void setup() {
  Serial.begin(115200);
START_INIT:
    CAN.init();
    if (CAN_OK != CAN.begin(CAN_500KBPS)) // init can bus : baudrate = 500k
    {
        serialp("ERROR:Failed to initialize CAN");
        delay(10);
        goto START_INIT;
    } else {
        serialp("INFO:LS CAN ready");
    }

//    tmr100ms.setInterval(100, SetSend100ms);
}

void loop() {
    if(Serial.available()) {
        String incomingserial = Serial.readString();
        if (incomingserial.equals("SENDALLDATA") || incomingserial.equals("SENDALLDATA\n") || incomingserial.equals("'SENDALLDATA'") || incomingserial.equals("b'SENDALLDATA'")) {
            serialp("VENT:" + String(ventCAN));
            serialp("ACTEMP:" + String(acTempCAN, 1));
            serialp("OUTSIDETEMP:" + String(outsideTempCAN));
            serialp("FANSPEED:" + String(fanSpeedCAN));
        } else {
          serialp("ERROR: Unknown request" + incomingserial);
        }
    }

    requestHVAC();
  //  tmr100ms.run();

    //Process CAN Data
    if (CAN_MSGAVAIL == CAN.checkReceive()) {
        CAN.readMsgBuf(&len, buf);        // read data,    len: data length, buf: data buf

        //Read CAN Node ID
        int CANNodeID = CAN.getCanId();

        // HVAC
        if (CANNodeID == 851) {    
            //Vent Status
            if (ventCAN != buf[0]) {
                ventCAN = buf[0];
                serialp("VENT:" + String(ventCAN));
            }

            double val = (double)buf[3] / 2.0;
            // Temperature Status
            if (acTempCAN != val) {
                acTempCAN = val;
                serialp("ACTEMP:" + String(acTempCAN, 1));
            }

            // Outside Temp
            if (outsideTempCAN != buf[4]) {
                outsideTempCAN = buf[4];
                serialp("OUTSIDETEMP:" + String(outsideTempCAN));
            }

            //Fan Speed
            if (fanSpeedCAN != buf[7]) {
                //update data
                fanSpeedCAN = buf[7];
                serialp("FANSPEED:" + String(fanSpeedCAN));
            }
        }
    }
}

// Requests HVAC info from BEM
void requestHVAC() {

    if (Send738 >= 2) {
        code738function();
        Send738 = 0;
    }

    if (Send775 >= 5) {
        code775function();
        Send775 = 0;
    }

    if (Send783 >= 2) {
        code783function();
        Send783 = 0;
    }

    if (Send785 >= 2) {
        code785function();
        Send785 = 0;
    }

    if (Send777 >= 5) {
        code777function();
        Send777 = 0;
    }

    if (Send779 >= 5) {
        code779function();
        Send779 = 0;
    }
    
    if (Send1372 >= 5) {
        code1372function();
        Send1372 = 0;
    }
}

// Every 100ms updates timer increments for each function
void SetSend100ms() {
    // 200ms
    Send738++;
    Send783++;
    Send785++;

    // 500ms
    Send775++;
    Send777++;
    Send779++;
    Send1372++;
}

// ICC Unit Data Requests:

int reset775 = 0;

void code738function() {
    unsigned char char738[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    CAN.sendMsgBuf(0x2E2, 0, 8, char738);
}

void code1372function() {
    unsigned char char1372[8] = {1, 2, 0, 0, 0, 0, 0, 0};
    CAN.sendMsgBuf(0x55C, 0, 8, char1372);
}

void code783function() {
    unsigned char char783[8] = {31, 31, 31, 31, 31, 0, 0, 0};
    CAN.sendMsgBuf(0x30F, 0, 8, char783);
}

void code785function() {
    unsigned char char785[8] = {31, 148, 31, 31, 31, 31, 0, 33};
    CAN.sendMsgBuf(0x311, 0, 8, char785);
}

void code777function() {
    unsigned char char777[8] = {32, 32, 32, 32, 32, 32, 32, 32};
    CAN.sendMsgBuf(0x309, 0, 8, char777);
}

void code779function() {
    unsigned char char779[8] = {0, 0, 2, 0, 0, 3, 8, 0};
    CAN.sendMsgBuf(0x30B, 0, 8, char779);
}

void code775function() {
    unsigned char char775[8] = {0, 0, 0, 128, 0, 0, 0, 0};
    CAN.sendMsgBuf(0x307, 0, 8, char775);
    if (reset775 == 1) {
        char775[0] = 0;
        char775[1] = 0;
        char775[2] = 0;
        char775[3] = 128;
        char775[4] = 0;
        char775[5] = 0;
        char775[6] = 0;
        char775[7] = 0;
        reset775 = 0;
    }
}

// Serial print function
void serialp(String inputline) {
    String tmpstringoutput = "SL:" + inputline + ":EL";
    Serial.println(tmpstringoutput);
}
