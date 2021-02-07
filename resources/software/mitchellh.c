#include "/home/pi/ArduinoCore-avr/libraries/SPI/src/SPI.h
#include "/home/pi/CAN_BUS_Shield/mcp_can.h"
#include "socketcan_cpp/socketcan_cpp.h"
#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>

#include <linux/can.h>
#include <linux/can/raw.h>

unsigned char len = 0;
unsigned char buf[8];

byte GearPos = 0;
byte StickCode = 0;

byte SportsShift = 0;
int Throttle = 0;
int RPM = 0;
int Speed = 0;
byte Brakes = 0;
double SteeringAngle = 0;

byte sendprimarycan = 0;

char serialinputbuffer[500];
int serialinputbuffercount = 0;


void setup() {
  // put your setup code here, to run once:
//  Serial.begin(115200);
//  memset(&serialinputbuffer[0], 0, sizeof(serialinputbuffer)); //init serial buffer

//START_INIT:

  //if (CAN_OK == CAN.begin(CAN_500KBPS))                  // init can bus : baudrate = 500k
 // {
 //   Serial.println("HS CAN Shield Startup OK");
 // }
 // else
 // {
 //   Serial.println("HS CAN Shield Failed Startup");
 //   Serial.println("HS CAN Shield Retry Startup");
 //   delay(100);
 // /  goto START_INIT;
 // }
int main(int argc, char **argv)
{
	int s, i; 
	int nbytes;
	struct sockaddr_can addr;
	struct ifreq ifr;
	struct can_frame frame;

	printf("CAN Sockets Receive Demo\r\n");

	if ((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
		perror("Socket");
		return 1;
	}

	strcpy(ifr.ifr_name, "vcan0" );
	ioctl(s, SIOCGIFINDEX, &ifr);

	memset(&addr, 0, sizeof(addr));
	addr.can_family = AF_CAN;
	addr.can_ifindex = ifr.ifr_ifindex;

	if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("Bind");
		return 1;
	}

	nbytes = read(s, &frame, sizeof(struct can_frame));

 	if (nbytes < 0) {
		perror("Read");
		return 1;
	}

	printf("0x%03X [%d] ",frame.can_id, frame.can_dlc);

	for (i = 0; i < frame.can_dlc; i++)
		printf("%02X ",frame.data[i]);

	printf("\r\n");

	if (close(s) < 0) {
		perror("Close");
		return 1;
	}

	return 0;
}

}



void loop() {


  if (CAN_MSGAVAIL == CAN.checkReceive())           // check if data coming
  {

    CAN.readMsgBuf(&len, buf);    // read data,  len: data length, buf: data buf
    int NodeID = CAN.getCanId();
    if (sendprimarycan == 1)
    {
      Serial.print("CAN:");
      Serial.print(NodeID);
      Serial.print(",");
      for (int i = 0; i < len; i++) // print the data
      {
        Serial.print(buf[i]);
        Serial.print(" ");
      }
      Serial.println();
    }
// start of fg data
    if (NodeID == 133)
    {
      Serial.print("CAN:");
      Serial.print(NodeID);
      Serial.print(",");
      for (int i = 0; i < len; i++) // print the data
      {
        Serial.print(buf[i]);
        Serial.print(" ");
      }
      Serial.println();
    }

    if (NodeID == 144)
    {
      int MultiVal = buf[0];
      int FineVal = buf[1];
      double TotalVal;

      if (MultiVal > 127)
      {
        MultiVal = ((MultiVal - 255) * -1) * 255;
        FineVal = (FineVal - 255) * -1;
        TotalVal = (MultiVal + FineVal) * -1; //Change to Negative

      } else {

        MultiVal = MultiVal * 255;
        TotalVal = MultiVal + FineVal;

      }
      Serial.print("Steering:");
      Serial.println(TotalVal);

    }


    if (NodeID == 301)
    {
      //301X3 = Throttle
      int tmpThrottle = (int)((int)(buf[2]) / 2);
      if (tmpThrottle != Throttle)
      {
        Throttle = tmpThrottle;
        Serial.print("Throttle:");
        Serial.println(Throttle);
      }
      //RPM = ((X5 * 255) + X6) / 4
      int Valx5 = (int)buf[4];
      int Valx6 = (int)buf[5];
      float rawRPM = ((Valx5 * 255) + Valx6) / 4;
      int tmpRPM = (int)rawRPM;
      if (tmpRPM != RPM)
      {
        RPM = tmpRPM;
        Serial.print("RPM:");
        Serial.println(RPM);
      }

      if (Brakes != buf[7])
      {
        Brakes = buf[7];
        if (Brakes == 1)
        {
          Serial.println("Brakes:ON");
        } else {


          Serial.println("Brakes:OFF");
        }
      }

    }


    if (NodeID == 519)
    {
      int Valx5 = (int)buf[4];
      int Valx6 = (int)buf[5];
      float tmpSpeed = (Valx5 + (Valx6 / 255)) * 2;
      if (tmpSpeed != Speed)
      {
        Speed = tmpSpeed;
        Serial.print("Speed:");
        Serial.println(Speed);
      }


    }

    if (NodeID == 560)
    {
      int Valx2 = buf[1];
      int tmpGearPos = 0;
      if (Valx2 == 255)
      {
        tmpGearPos = 1;
      }
      else if (Valx2 == 149)
      {
        tmpGearPos = 2;
      }
      else if (Valx2 == 97)
      {
        tmpGearPos = 3;
      }
      else if (Valx2 == 72)
      {
        tmpGearPos = 4;
      }
      else if (Valx2 == 55)
      {
        tmpGearPos = 5;
      }
      else if (Valx2 == 44)
      {
        tmpGearPos = 6;
      }

      if (tmpGearPos != GearPos)
      {
        GearPos = tmpGearPos;
        Serial.print("transgear:");
        Serial.println(GearPos);
      }


    }

    if (NodeID == 1001)
    {

      if (StickCode != buf[0])
      {
        StickCode = buf[0];
        Serial.print("gearstickpos:");
        Serial.println(StickCode);
      }



    }

    if (NodeID == 1079)
    {
      Serial.print("fuelstatus:");
      Serial.print(buf[0]);
      Serial.print(",");
      Serial.println(buf[1]);
    }


    if (NodeID == 1200)
    {
      int FrontLeft = (buf[0] * 255) + buf[1];
      int FrontRight = (buf[2] * 255) + buf[3];
      int RearLeft = (buf[4] * 255) + buf[5];
      int RearRight = (buf[6] * 255) + buf[7];

      Serial.print("wheelspeed:");
      Serial.print(FrontLeft);
      Serial.print(",");
      Serial.print(FrontRight);
      Serial.print(",");
      Serial.print(RearLeft);
      Serial.print(",");
      Serial.println(RearRight);
    }




    //OBD CAN ID
    if (NodeID == 2024)
    {
      Serial.print("CAN:");
      Serial.print(NodeID);
      Serial.print(",");
      for (int i = 0; i < len; i++) // print the data
      {
        Serial.print(buf[i]);
        Serial.print(" ");
      }
      Serial.println();
    }


    //OBD CAN ID
    if (NodeID == 2025)
    {
      Serial.print("CAN:");
      Serial.print(NodeID);
      Serial.print(",");
      for (int i = 0; i < len; i++) // print the data
      {
        Serial.print(buf[i]);
        Serial.print(" ");
      }
      Serial.println();
    }






  }


  if (Serial.available())
  {
    //lower than 32 is a command char.
    int byteread = Serial.read();
    if (byteread < 32)
    {
      //13 = command finished, cr.
      if (byteread == 13)
      {

        //Action then clear input buffer.
        if (strcmp(serialinputbuffer, "SENDMAINCAN") == 0)
        {
          sendprimarycan = 1;
        }
        else if (strcmp(serialinputbuffer, "STOPMAINCAN") == 0)
        {
          sendprimarycan = 0;
        }
        else if (strcmp(serialinputbuffer, "OBDCOOLANT") == 0)
        {
          //obd = additional bytes, current data/freeframe,PID,3-7 unused
          //2 additional bytes = current data and pid
          unsigned char msgtemp[8] = {2, 1, 5, 0, 0, 0, 0, 0};
          CAN.sendMsgBuf(0x7DF, 0, 8, msgtemp);

          Serial.println("CAN MESSAGE SENT FOR OBD COOLANT");
        }
        else if (strcmp(serialinputbuffer, "OBDINTAKETEMP") == 0)
        {
          unsigned char msgtemp[8] = {2, 1, 15, 0, 0, 0, 0, 0};
          CAN.sendMsgBuf(0x7DF, 0, 8, msgtemp);
          Serial.println("CAN MESSAGE SENT FOR INTAKE TEMP");
        }
        else if (strcmp(serialinputbuffer, "OBDINTAKEPSI") == 0)
        {
          unsigned char msgtemp[8] = {2, 1, 11, 0, 0, 0, 0, 0};
          CAN.sendMsgBuf(0x7DF, 0, 8, msgtemp);
          Serial.println("CAN MESSAGE SENT FOR OBD COOLANT");
        }
        else if (strcmp(serialinputbuffer, "OBDAIRTEMP") == 0)
        {
          unsigned char msgtemp[8] = {2, 1, 70, 0, 0, 0, 0, 0};
          CAN.sendMsgBuf(0x7DF, 0, 8, msgtemp);
          Serial.println("CAN MESSAGE SENT FOR OBD AMBIENT AIR TEMP");
        }
        else if (strcmp(serialinputbuffer, "OBDECUVOLTAGE") == 0)
        {
          unsigned char msgtemp[8] = {2, 1, 66, 0, 0, 0, 0, 0};
          CAN.sendMsgBuf(0x7DF, 0, 8, msgtemp);
          Serial.println("CAN MESSAGE SENT FOR OBD ECU VOLTAGE");
        }
        else if (strcmp(serialinputbuffer, "GetStatus") == 0)
        {
          getstatus();
        }
        memset(&serialinputbuffer[0], 0, sizeof(serialinputbuffer));
        serialinputbuffercount = 0;
      }


    }
    else if (byteread < 128)
    {
      //Valid characters.
      serialinputbuffer[serialinputbuffercount] = byteread;
      serialinputbuffercount++;
    }
  }
}


void getstatus()
{
  Serial.print("transgear:");
  Serial.println(GearPos);
  Serial.print("gearstickpos:");
  Serial.println(StickCode);


  if (Brakes == 1)
  {
    Serial.println("Brakes:ON");
  } else {
    Serial.println("Brakes:OFF");
  }


}

