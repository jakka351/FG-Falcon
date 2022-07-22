//Infered port, connected to Base shield D3.
// This work by Mitchell H
#define SDA_PORT PORTD
#define SDA_PIN 4   //define the SDA pin         
#define SCL_PORT PORTD
#define SCL_PIN 3   //define the SCL pin
#include "MLX90615.h"

#include <mcp_can.h>
#include <SPI.h>
#include <SimpleTimer.h>




//Settings
byte SendAllCanData = 0;
byte MonitorMode = 0;
//Monitor Mode = 1 will stop ACU / ICC Screen codes from being sent by automatic timer.

byte Send851Data = 0;


//Sensor now connected to SWCC Board, disable.
MLX90615 mlx90615; // for infered temp sensor


MCP_CAN CAN(10);                                      // Set CS to pin 9


char incomingserial[50];
int incomingcount = 0;

float tmpcabintemp = 0; //Temp sensor decimal value

//RX Can Codes, Default CAN Data Set

//Headlights
unsigned char code296X1 = 0;
//Indicators
unsigned char code296X4 = 0;
//Vent Status
unsigned char code851X1 = 0;
//AC Temp
unsigned char code851X4 = 0;
//Outside Temp
unsigned char code851X5 = 0;
//Fan Speed
unsigned char code851X8 = 0;
//Body Control Info
unsigned char code1027X1 = 0;
unsigned char code1027X2 = 0;
//Lock State
unsigned char code1027X7 = 0;
//code127 x2 = unlocked with remote, 2=unlocked, 0=locked.
//Ignition State
unsigned char code1030X2 = 0;
//Cabin Lights
unsigned char code1030X3 = 0;



unsigned char Flag_Recv = 0;
unsigned char len = 0;
unsigned char buf[8];

//TX CAN Codes
unsigned char char738[8] = {0, 0, 0, 0, 0, 0, 0, 0};
unsigned char char764[8] = {0, 0, 1, 0, 31, 0, 2, 4};
int reset775 = 0;
int reset789 = 0;
//Default 775 is (0, 0, 0, 128, 0, 0, 0, 0) - set 2nd to 16 to turn AC off at startup
//Removed - restet to default
unsigned char char775[8] = {0, 0, 0, 128, 0, 0, 0, 0};

unsigned char char787[8] = {148, 0, 0, 0, 0, 0, 0, 0};
unsigned char char789[8] = {0, 0, 0, 4, 128, 0, 0, 0};
/*
  789:
  X4 = Follow me home lighting
  X5 = Autoheadlight settings

*/

unsigned char char1372[8] = {1, 2, 0, 0, 0, 0, 0, 0};

//Variable for Steering wheel media controls
byte Code748x7 = 0;

//variables to signal send message
byte Send764 = 0;
byte Send738 = 0;
byte Send775 = 0;
byte Send787 = 0;
byte Send789 = 0;
byte Send1372 = 0;

//ACU Codes
byte Send742 = 0;
byte Send748 = 0;
byte Send751 = 0;
byte Send754 = 0;
byte Send756 = 0;
byte Send761 = 0;
byte Send777 = 0;
byte Send779 = 0;
byte Send781 = 0;
byte Send783 = 0;
byte Send785 = 0;
byte Send791 = 0;
byte Send1292 = 0;
byte Send1788 = 0;

//Timer Objects
SimpleTimer tmr100ms;

//can codes every 100ms
byte cabintempupdate = 0;





void setup()
{
  Serial.begin(115200);
  Serial.println("ICC CAN Interface startup");
  memset(incomingserial, 0, sizeof(incomingserial)); //init serial buffer.
START_INIT:

  if (CAN_OK != CAN.begin(CAN_125KBPS))                  // init can bus : baudrate = 500k
  {
    serialp("ICC CAN Interface Failed");
    delay(100);
    goto START_INIT;
  } else {
    serialp("LS CAN Interface");
  }
  tmr100ms.setInterval(100, SetSend100ms);
  mlx90615.init();
}

void loop()
{
  tmr100ms.run();

  if (Serial.available())
  {
    ProcessSerialDataIN();
  }

  //if send = yes then send can data.
  if (Send764 == 1)
  {
    code764function();
    Send764 = 0;
  }

  if (Send738 >= 2)
  {
    code738function();
    Send738 = 0;
  }

  if (Send775 >= 5)
  {
    code775function();
    Send775 = 0;
  }

  if (Send787 >= 2)
  {
    //Temperature Function
    code787function();
    Send787 = 0;
  }

  if (Send789 >= 2)
  {
    code789function();
    Send789 = 0;
  }
  if (Send1372 >= 5)
  {
    code1372function();
    Send1372 = 0;
  }

  //acu codes
  if (Send742 >= 2)
  {
    code742function();
    Send742 = 0;
  }

  if (Send748 >= 2)
  {
    code748function();
    Send748 = 0;
  }

  if (Send751 >= 2)
  {
    code751function();
    Send751 = 0;
  }

  if (Send754 >= 2)
  {
    code754function();
    Send754 = 0;
  }

  if (Send756 >= 5)
  {
    code756function();
    Send756 = 0;
  }

  if (Send761 >= 5)
  {
    code761function();
    Send761 = 0;
  }


  if (Send783 >= 2)
  {
    code783function();
    Send783 = 0;
  }

  if (Send785 >= 2)
  {
    code785function();
    Send785 = 0;
  }

  if (Send777 >= 5)
  {
    code777function();
    Send777 = 0;
  }

  if (Send779 >= 5)
  {
    code779function();
    Send779 = 0;
  }

  if (Send781 >= 5)
  {
    code781function();
    Send781 = 0;
  }
  //lowered from 10 to 5
  if (Send791 >= 5)
  {
    code791function();
    Send791 = 0;
  }

  if (Send1292 >= 5)
  {
    code1292function();
    Send1292 = 0;
  }
  //lowered from 10 to 5
  if (Send1788 >= 5)
  {
    code1788function();
    Send1788 = 0;
  }

  //Process CAN Data
  if (CAN_MSGAVAIL == CAN.checkReceive())           // check if data coming
  {
    CAN.readMsgBuf(&len, buf);    // read data,  len: data length, buf: data buf
    //Read CAN Node ID
    int CANNodeID = CAN.getCanId();

    //If Send All CAN Data command is sent, send Raw CAN Data
    if (SendAllCanData == 1)
    {
      String tmpstring = "ICCCAN:" + String(CANNodeID) + ",";
      //Seperate ID and Data
      //Print CAN Data using Loop through Buffer.
      for (int i = 0; i < len; i++) // print the data
      {
        tmpstring +=  String(buf[i]) + " ";

      }
      serialp(tmpstring); //Print String to serial

    }

    //296-X1 = Headlight Setting
    if (CANNodeID == 296)
    {
      //Only use X1, X4
      if (code296X1 != buf[0])
      {
        //Send New Setting
        serialp("Headlights:" + String(buf[0]));
        //Update Code Memory
        code296X1 = buf[0];
      }
      //296-X4 = Indicator Setting
      if (code296X4 != buf[3])
      {
        serialp("Indicators:" + String(buf[3]));
        code296X4 = buf[3];
      }
      //PrintCANMessage(CANNodeID, buf, len);
    }
    else if (CANNodeID == 748)
    {
      Code748x7 == buf[6];
    }
    else if (CANNodeID == 754)
    {
      if (buf[7] == 9)
      {
        serialp("Seek");
      }
      else if (buf[7] == 17)
      {
        serialp("Volume Up");
      }
      else if (buf[7] == 25)
      {
        serialp("Volume Down");
      }
      else if (buf[7] == 1 && buf[6] == 72)
      {
        if (Code748x7 == 16)
        {
          //MODE BUTTON
          serialp("MODE");
        }
      }

      if (buf[6] == 104)
      {
        serialp("Phone");
      }
    }
    else if (CANNodeID == 764) //Media Controls reported by ICC button panel.
    {
      if (buf[0] == 4)
      {
        serialp("Seek Up");
      }
      else if (buf[0] == 8)
      {
        serialp("Seek Down");
      }
      else if (buf[0] == 32)
      {
        serialp("FM/AM");
      }
      else if (buf[0] == 64)
      {
        serialp("SCN/AS");
      }
      else if (buf[0] == 128)
      {
        serialp("CD/AUX");
      }

      if (buf[2] == 33)
      {
        serialp("OK");
      }

      if (buf[3] == 65)
      {
        serialp("Volume Up");
      }
      else if (buf[3] == 129)
      {
        serialp("Volume Down");
      }

    }
    else if (CANNodeID == 851)
    {
      //Vent Status 851-X1
      if (code851X1 != buf[0])
      {
        serialp("VentStatus:" + String(buf[0]));
        code851X1 = buf[0];
      }
      //Temperature Status 851-X4
      if (code851X4 != buf[3])
      {
        serialp("AC Temp:" + String(buf[3]));
        code851X4 = buf[3];
      }
      if (code851X5 != buf[4])
      {
        //Outside Temp
        serialp("OutsideTemp:" + String(buf[4]));
        code851X5 = buf[4];
      }
      //Fan Speed 851-X8
      if (code851X8 != buf[7])
      {
        //update data
        code851X8 = buf[7];
        PrintFANStatus();

      }
      if (Send851Data == 1)
      {
        String tmpstring = "ICCCAN:" + String(CANNodeID) + ",";
        for (int i = 0; i < len; i++)
        {
          tmpstring += String(buf[i]) + " ";
        }
        serialp(tmpstring);
      }
    }
    else if (CANNodeID == 1027)
    {

      //Body Control Information
      //1027-X1 = Door and Demister Status
      if (code1027X1 != buf[0])
      {
        int tmpCode1027X1 = (int)buf[0];
        if (tmpCode1027X1 >= 128)
        {
          //Front Right Door Open, remove Number from increment.
          tmpCode1027X1 = tmpCode1027X1 - 128;
          serialp("Front Right Door: Open");
        } else {
          serialp("Front Right Door: Closed");
        }
        if (tmpCode1027X1 >= 64)
        {
          tmpCode1027X1 = tmpCode1027X1 - 64;
          serialp("Front Left Door: Open");
        } else {
          serialp("Front Left Door: Closed");
        }
        if (tmpCode1027X1 >= 32)
        {
          tmpCode1027X1 = tmpCode1027X1 - 32;
          serialp("Rear Right Door: Open");
        } else {
          serialp("Rear Right Door: Closed");
        }
        if (tmpCode1027X1 >= 16)
        {
          tmpCode1027X1 = tmpCode1027X1 - 16;
          serialp("Rear Left Door: Open");
        } else {
          serialp("Rear Left Door: Closed");
        }
        if (tmpCode1027X1 >= 8)
        {
          tmpCode1027X1 = tmpCode1027X1 - 8;
          //This is an unknown function
          serialp("1027 CAN Unknown Function - X1=8");
        }
        if (tmpCode1027X1 >= 4)
        {
          //Rear Demister On
          tmpCode1027X1 = tmpCode1027X1 - 4;
          serialp("Rear Demister:On");
        } else {
          serialp("Rear Demister:Off");
        }
        //Update 1027 X1 Code
        code1027X1 = buf[0];
      }
      //1027 X2 Code = Indicator Confirmation of Remote Unlock / Locking
      if (code1027X2 != buf[1])
      {
        serialp("1027X2:" + String(buf[1]));
        code1027X2 = buf[1];
      }

      //1027 X7 Code = Lock State of Car
      if (code1027X7 != buf[6])
      {
        serialp("Car Lock State:" + String(code1027X7));
        code1027X7 = buf[6];
      }

    }
    else if (CANNodeID == 1030)
    {
      if (code1030X2 != buf[1])
      {
        code1030X2 = buf[1];
        print_ignition_state();
      }

      if (code1030X3 != buf[2])
      {
        //Update Code
        code1030X3 = buf[2];
        if (code1030X3 == 8)
        {
          serialp("Cabin Lights: On");
        }
        else if (code1030X3 == 0)
        {
          serialp("Cabin Lights: Off");
        }
      }
    }
  }
}

void print_ignition_state()
{
  if (code1030X2 == 1)
  {
    serialp("Ignition State: Off");
  }
  else if (code1030X2 == 2)
  {
    serialp("Ignition State: Acc");
  }
  else if (code1030X2 == 4)
  {
    serialp("Ignition State: On");
  }
}

void PrintFANStatus()
{
  int fanspeedcode = code851X8;
  serialp("fanspeedcode:" + String(fanspeedcode));
  byte AutoFan = 0;
  if (fanspeedcode >= 128)
  {
    //Above 128 = Automatic Fan Speed
    AutoFan = 1;
    //fanspeedcode = fanspeedcode - 128;
  } else if (fanspeedcode >= 16) {
    //Increment of 16 - Unknown function - Possible Semi-Auto
    //fanspeedcode = fanspeedcode - 16;
  }

  //Send Fan Speed Level
  serialp("Fan Speed:" + String(fanspeedcode));

  //Send Fan Speed mode.
  String tmpstring = "Fan Speed Mode:";
  if (AutoFan == 1)
  {
    tmpstring += "Auto";
  } else {
    tmpstring += "Manual";
  }
  serialp(tmpstring);
}



void SetSend100ms()
{
  cabintempupdate++;
  //update cabin temp variable.

  if (cabintempupdate == 5)
  {
    tmpcabintemp = mlx90615.getTemperature(MLX90615_AMBIENT_TEMPERATURE);
    serialp("CabinTemp:" + String(tmpcabintemp));
    cabintempupdate = 0;
  }


  if (MonitorMode == 0)
  {
    //Only send CAN data while car is turned on.
    //if (code1030X2 > 1) is untested, possibility that bem will not communication without
    //initial can data sent, may need to remove if issues.
    //if (code1030X2 > 1)
    //{
    Send764 = 1;
    //500ms
    Send775++;
    Send1372++;
    //200ms
    Send738++;
    Send787++;
    Send789++;

    //ACU
    //200ms
    Send742++;
    Send748++;
    Send751++;
    Send754++;
    Send783++;
    Send785++;

    //500ms
    Send756++;
    Send761++;
    Send777++;
    Send779++;
    Send781++;
    Send1292++;

    //1000 (Lowered from 1000 to 500)
    Send791++;
    Send1788++;
  }
}





void HazardLights()
{
  char775[2] = 1;
  reset775 = 1;
}

void InteriorLights()
{
  char775[3] = 160;
  reset775 = 1;

}

void DSCButton()
{
  char775[3] = 144;
  reset775 = 1;

}

void LockCar()
{
  char775[3] = 192;
  reset775 = 1;

}
void UnlockCar()
{
  char775[3] = 132;
  reset775 = 1;

}

void IncreaseTemp()
{
  char775[2] = 128;
  reset775 = 1;
  Send775 = 10;

}

void LowerTemp()
{
  char775[2] = 64;
  reset775 = 1;
  Send775 = 10;

}
void RearDemister()
{
  char775[0] = 32;
  reset775 = 1;

}

void CycleVents()
{
  char775[1] = 128;
  reset775 = 1;

}
void WindowDefog()
{
  char775[0] = 2;
  reset775 = 1;

}
void ACAuto()
{
  char775[1] = 32;
  reset775 = 1;

}
void ACOnOff()
{
  char775[0] = 128;
  reset775 = 1;

}

void AllOff()
{
  char775[1] = 16;
  reset775 = 1;

}


void CycleCabin()
{
  char775[0] = 64;
  reset775 = 1;

}

void FanDecrease()
{
  char775[1] = 4;
  reset775 = 1;
  Send775 = 10;
}

void FanIncrease()
{
  char775[1] = 8;
  reset775 = 1;
  Send775 = 10;
}


//Function GetCabinTemp runs every 500ms, sets the 787[0] code to the integer value reported from the thermistor sensor.
//Thermistor sensor connected to analog pin 0



void ProcessSerialDataIN()
{
  int newdata = Serial.read();
  if (newdata < 32)
  {
    if (newdata == 13)
    {
      ActionSerialCommand(); //a line of serial data has been rx, send to action sub.
      memset(incomingserial, 0, sizeof(incomingserial)); //reset serial buffer.
      incomingcount = 0;
    }

  }
  else if (newdata < 128)
  {
    incomingserial[incomingcount] = newdata;
    incomingcount++;
  }
}

void ActionSerialCommand()
{
  //strcmp if == 0 then strings are equal.

  if (strcmp(incomingserial, "SENDCAN") == 0)
  {
    //Send all CAN Bus Data
    SendAllCanData = 1;
  }
  else if (strcmp(incomingserial, "STOPCAN") == 0)
  {
    //Stop sending CAN Bus Data
    SendAllCanData = 0;
  }
  else if (strcmp(incomingserial, "SEND851") == 0)
  {
    serialp("SEND851");
    Send851Data = 1;
  }
  else if (strcmp(incomingserial, "STOP851") == 0)
  {
    serialp("STOP851");
    Send851Data = 0;
  }
  else if (strcmp(incomingserial, "MONITORMODEON") == 0)
  {
    //CAN Monitor Mode, does not send CAN messages.
    MonitorMode == 1;
  }
  else if (strcmp(incomingserial, "MONITORMODEOFF") == 0)
  {
    MonitorMode == 0;
  }
  else if (strcmp(incomingserial, "GetStatus") == 0)
  {
    GetStatus();
  }
  else if (strcmp(incomingserial, "fan-") == 0)
  {
    FanDecrease();
  }
  else if (strcmp(incomingserial, "fan+") == 0)
  {
    FanIncrease();
  }
  else if (strcmp(incomingserial, "cyclecabin") == 0)
  {
    CycleCabin();
  }
  else if (strcmp(incomingserial, "alloff") == 0)
  {
    AllOff();
  }
  else if (strcmp(incomingserial, "aconoff") == 0)
  {
    ACOnOff();
  }
  else if (strcmp(incomingserial, "acauto") == 0)
  {
    ACAuto();
  }
  else if (strcmp(incomingserial, "windowdefog") == 0)
  {
    WindowDefog();
  }
  else if (strcmp(incomingserial, "cyclevents") == 0)
  {
    CycleVents();
  }
  else if (strcmp(incomingserial, "reardemist") == 0)
  {
    RearDemister();
  }
  else if (strcmp(incomingserial, "lowertemp") == 0)
  {
    LowerTemp();
  }
  else if (strcmp(incomingserial, "increasetemp") == 0)
  {
    IncreaseTemp();
  }
  else if (strcmp(incomingserial, "unlock") == 0)
  {
    UnlockCar();
  }
  else if (strcmp(incomingserial, "lock") == 0)
  {
    LockCar();
  }
  else if (strcmp(incomingserial, "dsc") == 0)
  {
    DSCButton();
  }
  else if (strcmp(incomingserial, "interiorlights") == 0)
  {
    InteriorLights();
  }
  else if (strcmp(incomingserial, "hazardlights") == 0)
  {
    HazardLights();
  }
  else if (strcmp(incomingserial, "ILReset") == 0)
  {
    ResetInteriorLights();
  }
  else if (strcmp(incomingserial, "ILIgnitionOff") == 0)
  {
    ILIGNOFF();
  }
  else if (strcmp(incomingserial, "ILKeyOut") == 0)
  {
    ILKEYOUT();
  }
  else if (strcmp(incomingserial, "ILDoorOpen") == 0)
  {
    ILDoorOpen();
  }
  else if (strcmp(incomingserial, "ILKeyUnlock") == 0)
  {
    ILKeyUnlock();
  }
}



//Print Current Status (if requested by serial command)
void GetStatus()
{
  //Headlights
  serialp("Headlights:" + String(code296X1));

  //Indicators
  serialp("Indicators:" + String(code296X4));

  //Vent Status
  serialp("VentStatus:" + String(code851X1));

  //AC Temperature
  serialp("AC Temp:" + String(code851X4));

  //Outside Temp
  serialp("OutsideTemp:" + String(code851X5));

  //Fan Speed
  PrintFANStatus();

 print_ignition_state();
  int tmpcode1027X1 = (int)code1027X1;
  //Doors and Demister Info
  if (tmpcode1027X1 >= 128)
  {
    //Front Right Door Open, remove Number from increment.

    tmpcode1027X1 = tmpcode1027X1 - 128;
    serialp("Front Right Door: Open");
  } else {
  }
  if (tmpcode1027X1 >= 64)
  {
    tmpcode1027X1 = tmpcode1027X1 - 64;
    serialp("Front Left Door: Open");
  } else {
    serialp("Front Left Door: Closed");
  }
  if (tmpcode1027X1 >= 32)
  {
    tmpcode1027X1 = tmpcode1027X1 - 32;
    serialp("Rear Right Door: Open");
  } else {
    serialp("Rear Right Door: Closed");
  }
  if (tmpcode1027X1 >= 16)
  {
    tmpcode1027X1 = tmpcode1027X1 - 16;
    serialp("Rear Left Door: Open");
  } else {
    serialp("Rear Left Door: Closed");
  }
  if (tmpcode1027X1 >= 8)
  {
    tmpcode1027X1 = tmpcode1027X1 - 8;
    //This is an unknown function
    serialp("1027 CAN Unknown Function - X1=8");
  }
  if (tmpcode1027X1 >= 4)
  {
    //Rear Demister On
    tmpcode1027X1 = tmpcode1027X1 - 4;
    serialp("Rear Demister:On");
  } else {
    serialp("Rear Demister:Off");
  }

  //Car Lock State
  serialp("Car Lock State:" + String(code1027X7));

  if (code1030X3 == 8)
  {
    serialp("Cabin Lights: On");
  }
  else if (code1030X3 == 0)
  {
    serialp("Cabin Lights: Off");
  }
}

//ACU CAN CODES
void code742function()
{
  unsigned char char742[8] = {4, 227, 0, 0, 0, 0, 0, 0};
  CAN.sendMsgBuf(0x2E6, 0, 8, char742);
}

void code748function()
{
  unsigned char char748[8] = {2, 159, 3, 3, 3, 202, 0, 0};
  CAN.sendMsgBuf(0x2EC, 0, 8, char748);
}

void code751function()
{
  unsigned char char751[8] = {4, 227, 6, 78, 8, 29, 0, 0};
  CAN.sendMsgBuf(0x2EF, 0, 8, char751);
}

void code754function()
{
  unsigned char char754[8] = {4, 10, 13, 10, 9, 73, 72, 5};
  CAN.sendMsgBuf(0x2F2, 0, 8, char754);
}

void code756function()
{
  unsigned char char756[8] = {0, 0, 255, 255, 255, 252, 0, 0};
  CAN.sendMsgBuf(0x2F4, 0, 8, char756);
}

void code761function()
{
  unsigned char char761[8] = {0, 0, 0, 0, 0, 0, 0, 0};
  CAN.sendMsgBuf(0x2F9, 0, 8, char761);
}

void code1292function()
{
  unsigned char char1292[8] = {17, 2, 110, 0, 0, 0, 0, 0};
  CAN.sendMsgBuf(0x50C, 0, 8, char1292);
}

void code1788function()
{
  unsigned char char1788[8] = {0, 0, 0, 0, 0, 0, 0, 0};
  CAN.sendMsgBuf(0x6FC, 0, 8, char1788);
}

void code781function()
{
  unsigned char char781[8] = {0, 0, 0, 1, 0, 22, 0, 0};
  CAN.sendMsgBuf(0x30D, 0, 8, char781);
}

void code791function()
{
  unsigned char char791[8] = {87, 66, 68, 51, 48, 53, 50, 51};
  CAN.sendMsgBuf(0x317, 0, 8, char791);
}


//ICC SCREEN CAN CODES
void code738function()
{
  CAN.sendMsgBuf(0x2E2, 0, 8, char738);
}



void code764function()
{
  CAN.sendMsgBuf(0x2FC, 0, 8, char764);
}

void code783function()
{
  unsigned char char783[8] = {31, 31, 31, 31, 31, 0, 0, 0};
  CAN.sendMsgBuf(0x30F, 0, 8, char783);
}

void code785function()
{
  unsigned char char785[8] = {31, 148, 31, 31, 31, 31, 0, 33};
  CAN.sendMsgBuf(0x311, 0, 8, char785);
}

void code777function()
{
  unsigned char char777[8] = {32, 32, 32, 32, 32, 32, 32, 32};
  CAN.sendMsgBuf(0x309, 0, 8, char777);
}

void code779function()
{
  unsigned char char779[8] = {0, 0, 2, 0, 0, 3, 8, 0};
  CAN.sendMsgBuf(0x30B, 0, 8, char779);
}



void code775function()
{
  CAN.sendMsgBuf(0x307, 0, 8, char775);
  if (reset775 == 1)
  {
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


//Cabin temp
void code787function()
{
  float tmpctemp = (tmpcabintemp * 2) + 80;
  char787[0] = (int)tmpctemp;
  //serialp("Code787:" + String(char787[0]));

  CAN.sendMsgBuf(0x313, 0, 8, char787);

}


//Car Settings
void code789function()
{
  CAN.sendMsgBuf(0x315, 0, 8, char789);
  if (reset789 == 1)
  {
    char789[0] = 0;
    char789[1] = 0;
    char789[2] = 0;
    char789[3] = 4;
    char789[4] = 128;
    char789[5] = 0;
    char789[6] = 0;
    char789[7] = 0;
    reset789 = 0;
  }
}
//Reset interior light settings.
void ResetInteriorLights()
{
  char789[1] = 64;
  reset789 = 1;
}
//Function to cycle option that turns interior lights on with ignition off ILIGNOFF
void ILIGNOFF()
{
  char789[2] = 4;
  reset789 = 1;
}
//Function to cycle option that turns interior lights on with key removal.
void ILKEYOUT()
{
  char789[2] = 32;
  reset789 = 1;
}
//Function to cycle option that turns interior lights on with door open.
void ILDoorOpen()
{
  char789[1] = 128;
  reset789 = 1;
}
//Function to cycle option that turns interior lights on with unlock.
void ILKeyUnlock()
{
  char789[1] = 32;
  reset789 = 1;
}

void DriveAwayLocking()
{
  char789[0] = 64;
  reset789 = 1;
}

void ConfirmLockIndicators()
{
  char789[0] = 128;
  reset789 = 1;
}

void ConfirmLockHorn()
{
  char789[0] = 32;
  reset789 = 1;
}

void TwoStageUnlock()
{
  char789[0] = 4;
  reset789 = 1;
}

void ConfirmUnlockIndicators()
{
  char789[0] = 8;
  reset789 = 1;
}




void code1372function()
{
  CAN.sendMsgBuf(0x55C, 0, 8, char1372);
}



//Serial print function
void serialp(String inputline)
{
  String tmpstringoutput = "SL:" + inputline + ":EL";
  Serial.println(tmpstringoutput);
}
