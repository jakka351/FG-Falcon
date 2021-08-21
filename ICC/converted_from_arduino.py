#!/usr/bin/python3
#can0fdim fg falcon swc-can adapter
#https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/icc
#based off Mitchell H's work 
############################
#import modules
############################
import can
import time
import os
import logging
import queue
import threading
from threading import Thread
import sys, traceback
from can import bus
############################
#Global Variables
############################
c                      = ''
count                  = 0  

try:
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
except OSError:
    sys.exit()
#############################
#//Settings
SendAllCanData = 0
MonitorMode = 0  #//Monitor Mode = 1 will stop ACU / ICC Screen codes from being sent by automatic timer.
Send851Data = 0 #msg incomingserial[50];
incomingcount = 0
InteriorActualTemperature = 0 # //Temp sensor decimal value
InstrumentClust296X1 = 0
InstrumentClust296X4 = 0 #//Indicators
HvacVentStatus851X1 = 0 #//Vent Status
HvacTargetTemp851X4 = 0 #//AC Temp
HvacExteriorTemp851X5 = 0 #//Outside Temp
HvacFanSpeed851X8 = 0 #//Fan Speed
BodyElectricModule1027X1 = 0 #//Body Control Info
BodyElectricModule1027X2 = 0 #//code1027 x2 = unlocked with remote, 2=unlocked, 0=locked.
BodyElectricModule1027X7 = 0 #//Lock State
BodyElectricModule1030X2 = 0 #//Ignition State
BodyElectricModule1030X3 = 0 #//Cabin Lights
#//TX CAN Codes
msg738 = can.Message(arbitration_id=0x2E2, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
msg764 = can.Message(arbitration_id=0x2FC, data=[0, 0, 1, 0, 31, 0, 2, 4], is_extended_id=False)
msg775 = can.Message(arbitration_id=0x307, data=[0, 0, 0, 128, 0, 0, 0, 0], is_extended_id=False)
msg787 = can.Message(arbitration_id=0x313, data=[148, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
msg789 = can.Message(arbitration_id=0x315, data=[0, 0, 0, 4, 128, 0, 0, 0], is_extended_id=False)
msg1372 = can.Message(arbitration_id=0x55C, data=[1, 2, 0, 0, 0, 0, 0, 0], is_extended_id=False)
Code748x7 = 0
Send764 = 0
Send738 = 0
Send775 = 0
Send787 = 0
Send789 = 0
Send1372 = 0
Send742 = 0
Send748 = 0
Send751 = 0
Send754 = 0
Send756 = 0
Send761 = 0
Send777 = 0
Send779 = 0
Send781 = 0
Send783 = 0
Send785 = 0
Send791 = 0
Send1292 = 0
Send1788 = 0
reset775 = 0
reset789 = 0
cabintempupdate = 0

q                      = queue.Queue()                       #

############################
#bus setup
############################
def setup():
    try:
        bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
    except OSError:
        sys.exit()
############################
#msgbuffer
############################
def msgbuffer():\
global message, q                                             
while True:
      message = bus.recv()
      if message.arbitration_id == 296:                        
        q.put(message)
      if message.arbitration_id == 748:                        
        q.put(message)
      if message.arbitration_id == 754:                      
        q.put(message)
      if message.arbitration_id == 765:                        
        q.put(message)
      if message.arbitration_id == 851:                        
        q.put(message)
      if message.arbitration_id == 1027:                        
        q.put(message)
      if message.arbitration_id == 1030:                        
        q.put(message)
    
def loop():
  if Send764 == 1:
    code764function()
    Send764 = 0
  
  elif Send738 >= 2:
    code738function()
    Send738 = 0
  
  elif Send775 >= 5:
    code775function()
    Send775 = 0
  
  elif Send787 >= 2:
    #Temperature Function
    code787function()
    Send787 = 0

  elif Send789 >= 2:
    code789function()
    Send789 = 0

  elif Send1372 >= 5:
    code1372function()
    Send1372 = 0

  #acu codes
  elif Send742 >= 2:
    code742function()
    Send742 = 0

  elif Send748 >= 2:
    code748function()
    Send748 = 0

  elif Send751 >= 2:
    code751function()
    Send751 = 0

  elif Send754 >= 2:
    code754function()
    Send754 = 0

  elif Send756 >= 5:
    code756function()
    Send756 = 0
  
  elif Send761 >= 5:
    code761function()
    Send761 = 0 

  elif Send783 >= 2:
    code783function()
    Send783 = 0

  elif Send785 >= 2:
    code785function()
    Send785 = 0

  elif Send777 >= 5:
    code777function()
    Send777 = 0
  
  elif Send779 >= 5:
    code779function()
    Send779 = 0

  elif Send781 >= 5:
    code781function()
    Send781 = 0
  
  elif Send791 >= 5:
    code791function()
    Send791 = 0

  elif Send1292 >= 5:
    code1292function()
    Send1292 = 0
  
  elif Send1788 >= 5:
    code1788function()
    Send1788 = 0

###############################################
#
###############################################
def GetStatus():
  #  //Headlights
  print("Headlights:", InstrumentClust296X1)
  #  //Indicators
  print("Indicators:", InstrumentClust296X4)
  # //Vent Status
  print("VentStatus:", HvacVentStatus851X1)
  #  //AC Temperature
  print("AC Temp:", HvacIntegModule851X4)
  #  //Outside Temp
  print("OutsideTemp:", HvacIntegModuleExteriorTemp)

###############################################
#
###############################################
def main():
    try:
        while True:
            for i in range(8):
                while(q.empty() == True):                               # wait for messages to queue
                    pass
                message = q.get()   
                if message.arbitration_id == 1027 and message.data[1] > 1:
                    Send764 = 1
                    Send775 =1
                    Send1372 =1
            #//200ms
                    Send738 =1
                    Send787 =1
                    Send789 =1
                    #//ACU
                    #//200ms
                    Send742 =1
                    Send748 =1
                    Send751 =1
                    Send754 =1
                    Send783 =1
                    Send785 =1
                    #//500ms
                    Send756=1
                    Send761=1
                    Send777=1
                    Send779=1
                    Send781=1
                    Send1292=1
             
                  # //1000 (Lowered from 1000 to 500)
                    Send791=1
                    Send1788=1
        
               # print_ignition_state()
                if message.arbitration_id == 1027:
                    BodyElectricModule1030X2 = message.data[1]
                    if BodyElectricModule1030X2 == 1:
                        print("Ignition State: Off")
                    elif BodyElectricModule1030X2 == 2:
                        print("Ignition State: Acc")
                    elif BodyElectricModule1030X2 == 4:
                        print("Ignition State: On")
               
                if message.arbitration_id == 0x353:
                    fanspeedcode = message.data[7]
                    #print("fanspeedcode:", fanspeedcode)
                    AutoFan = 0
                    if fanspeedcode >= 128:
                      AutoFan = 1
                      fanspeedcode = fanspeedcode - 128
                    elif fanspeedcode >= 16:
                      fanspeedcode = fanspeedcode - 16
                    print("Fan Speed:" ,fanspeedcode)
                    tmpstring = "Fan Speed Mode:" #  //Send Fan Speed mode. 
                    if AutoFan == 1:
                        tmpstring += "Auto"
                    else:
                        tmpstring += "Manual"
                    print(tmpstring)
                loop()

    except KeyboardInterrupt:
        sys.exit(0)                                              # quit if ctl + c is hit
    except Exception:
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
        sys.exit()
    except OSError:
        sys.exit()                                               # quit if there is a system issue
    

###############################################
#
################
###############################################
def SetSend100ms():
    if cabintempupdate == 5:
        InteriorActualTemperature = 12
        print("CabinTemp:", InteriorActualTemperature)
        cabintempupdate = 0

    #if MonitorMode == 0:  
#    //Only send CAN data while car is turned on.
#    //if (BodyElectricModule1030X2 > 1) is untested, possibility that bem will not communication without
 #  //initial can data sent, may need to remove if issues.

################################################
#
###############################################
def HazardLights():
  #msg775 = message.data[2]
  msg775[2] = 1
  reset775 = 1

def InteriorLights():
  msg775[3] = message.data[3]
  msg775[3] = 160
  reset775 = 1

def DSCButton():
  msg775[3] = 144
  reset775 = 1

def LockCar():
  msg775[3] = 192
  reset775 = 1

def UnlockCar():
  msg775[3] = 132
  reset775 = 1
def IncreaseTemp():
  msg775[2] = 128
  reset775 = 1
  Send775 = 10

def LowerTemp():
  msg775[2] = 64
  reset775 = 1
  Send775 = 10

def RearDemister():
  msg775[0] = 32
  reset775 = 1

def CycleVents():
  msg775[1] = 128
  reset775 = 1

def WindowDefog():
  msg775[0] = 2
  reset775 = 1

def ACAuto():
  msg775[1] = 32
  reset775 = 1

def ACOnOff():
  msg775[0] = 128
  reset775 = 1

def AllOff():
  msg775[1] = 16
  reset775 = 1

def CycleCabin():
  msg775[0] = 64
  reset775 = 1

def FanDecrease():
  msg775[1] = 4
  reset775 = 1
  Send775 = 10

def FanIncrease():
  msg775[1] = 8
  reset775 = 1
  Send775 = 10


###################################
#
###################################
#//Function GetCabinTemp runs every 500ms, sets the 787[0] code to the integer value reported from the thermistor sensor.
#//Thermistor sensor connected to analog pin 0
def ProcessSerialDataIN():
  newdata = Serial.read()
  if newdata <= 32:
    if newdata == 13:
      ActionSerialCommand()  # //a line of serial data has been rx, send to action sub.
      memset(incomingserial, 0, sizeof(incomingserial))  # //reset serial buffer.
      incomingcount = 0
    
  elif newdata <= 128:
    incomingserial[incomingcount] = newdata
    incomingcount = +1 
"""
def ActionSerialCommand():
    print("abc")
    if incomingserial, "SENDCAN" == 0:
    #  //Send all CAN Bus Data
        SendAllCanData = 1
    elif incomingserial, "STOPCAN" == 0:
    #  //Stop sending CAN Bus Data
        SendAllCanData = 0
    elif strcmp(incomingserial, "SEND851") == 0:
        print("SEND851")
        Send851Data = 1
    elif strcmp(incomingserial, "STOP851") == 0:
      print("STOP851")
      Send851Data = 0
    elif strcmp(incomingserial, "MONITORMODEON") == 0:
#    //CAN Monitor Mode, does not send CAN messages.
        MonitorMode == 1
    elif strcmp(incomingserial, "MONITORMODEOFF") == 0:
        MonitorMode == 0
    elif strcmp(incomingserial, "GetStatus") == 0:  
        GetStatus()
    elif strcmp(incomingserial, "fan-") == 0:
        FanDecrease()
    elif strcmp(incomingserial, "fan+") == 0:
        FanIncrease()
    elif strcmp(incomingserial, "cyclecabin") == 0:
        CycleCabin()
    elif strcmp(incomingserial, "alloff") == 0:
        AllOff()
    elif strcmp(incomingserial, "aconoff") == 0:
        ACOnOff()
    elif strcmp(incomingserial, "acauto") == 0:
        ACAuto()
    elif strcmp(incomingserial, "windowdefog") == 0: 
        WindowDefog()
    elif strcmp(incomingserial, "cyclevents") == 0:
        CycleVents()
    elif strcmp(incomingserial, "reardemist") == 0:
        RearDemister()
    elif strcmp(incomingserial, "lowertemp") == 0:
        LowerTemp()
    elif strcmp(incomingserial, "increasetemp") == 0:
        IncreaseTemp()
    elif strcmp(incomingserial, "unlock") == 0:
        UnlockCar()
    elif strcmp(incomingserial, "lock") == 0:
        LockCar()
    elif strcmp(incomingserial, "dsc") == 0:
        DSCButton()
    elif strcmp(incomingserial, "interiorlights") == 0:
        InteriorLights()
    elif strcmp(incomingserial, "hazardlights") == 0:
        HazardLights()
    elif strcmp(incomingserial, "ILReset") == 0:
        ResetInteriorLights()
    elif strcmp(incomingserial, "ILIgnitionOff") == 0:
        ILIGNOFF()
    elif strcmp(incomingserial, "ILKeyOut") == 0:
        ILKEYOUT()
    elif strcmp(incomingserial, "ILDoorOpen") == 0:
        ILDoorOpen()
   elif strcmp(incomingserial, "ILKeyUnlock") == 0:
        ILKeyUnlock()

"""
###############################################
#
###############################################
def code742unction():
    msg742 = can.Message(arbitration_id=0x2E6, data=[4, 227, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    task742 = bus.send_periodic(msg742, 0.20)
    assert isinstance(task742, can.CyclicSendTaskABC)
    
def code748function():
    msg748 = can.Message(arbitration_id=0x748, data=[0, 159, 3, 3, 3, 202, 0, 0], is_extended_id=False)
    task748 = bus.send_periodic(msg748, 0.20)
    assert isinstance(task748, can.CyclicSendTaskABC)
    

def code751function():
    msg751= can.Message(arbitration_id=0x751, data=[4, 227, 6, 78, 8, 29, 0, 0], is_extended_id=False)
    task751 = bus.send_periodic(msg751, 0.20)
    assert isinstance(task751, can.CyclicSendTaskABC)
    
def code754function():
    msg754 = can.Message(arbitration_id=754, data=[4, 10, 13, 10, 9, 73, 72, 5], is_extended_id=False)
    task754 = bus.send_periodic(msg754, 0.20)
    assert isinstance(task754, can.CyclicSendTaskABC)
    
def code756function():
    msg756 = can.Message(arbitration_id=756, data=[0, 0, 255, 255, 255, 252, 0, 0], is_extended_id=False)
    task756 = bus.send_periodic(msg756, 0.20)
    assert isinstance(task756, can.CyclicSendTaskABC)
    
def code761function():
    msg761 = can.Message(arbitration_id=761, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    task761 = bus.send_periodic(msg761, 0.20)
    assert isinstance(task761, can.CyclicSendTaskABC)
    
def code1292function():
    msg1292 = can.Message(arbitration_id=1292, data=[17, 2, 110, 0, 0, 0, 0, 0], is_extended_id=False)
    task1292 = bus.send_periodic(msg1292, 0.20)
    assert isinstance(task1292, can.CyclicSendTaskABC)
    
def code1788function():
    msg1788 = can.Message(arbitration_id=1788, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    task1788 = bus.send_periodic(msg1788, 0.20)
    assert isinstance(task1788, can.CyclicSendTaskABC)
    
def code781function():
    msg781 = can.Message(arbitration_id=781, data=[0, 0, 0, 1, 0, 22, 0, 0], is_extended_id=False)
    task781 = bus.send_periodic(msg781, 0.20)
    assert isinstance(task781, can.CyclicSendTaskABC)
    
def code791function():
    msg791 = can.Message(arbitration_id=791, data=[87, 66, 68, 51, 48, 53, 50, 51], is_extended_id=False)
    task791 = bus.send_periodic(msg791, 0.20)
    assert isinstance(task791, can.CyclicSendTaskABC)
    
#//ICC SCREEN CAN CODES
def code738function():
    msg738 = can.Message(arbitration_id=0x001, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    task738 = bus.send_periodic(msg738, 0.20)
    assert isinstance(task738, can.CyclicSendTaskABC)
    
def code764function():
    msg764 = can.Message(arbitration_id=0x2FC, data=[0, 0, 1, 0, 31, 0, 2, 4], is_extended_id=False)
    task764 = bus.send_periodic(msg764, 0.20)
    assert isinstance(task764, can.CyclicSendTaskABC)
    

def code783function():
    msg783 = can.Message(arbitration_id=0x783, data=[31, 31, 31, 31, 31, 0, 0, 0], is_extended_id=False)
    task783 = bus.send_periodic(msg783, 0.20)
    assert isinstance(task783, can.CyclicSendTaskABC)

def code785function():
    msg785 = can.Message(arbitration_id=0x785, data=[31, 148, 31, 31, 31, 31, 0, 33], is_extended_id=False)
    task785 = bus.send_periodic(msg785, 0.20)
    assert isinstance(task785, can.CyclicSendTaskABC)
    
def code777function():
    msg777 = can.Message(arbitration_id=0x777, data=[32, 32, 32, 32, 32, 32, 32, 32], is_extended_id=False)
    task777 = bus.send_periodic(msg777, 0.20)
    assert isinstance(task777, can.CyclicSendTaskABC)
    
def code779function():
    msg779 = can.Message(arbitration_id=0x779, data=[0, 0, 2, 0, 0, 3, 8, 0], is_extended_id=False)
    task779 = bus.send_periodic(msg779, 0.20)
    assert isinstance(task779, can.CyclicSendTaskABC)
    
def code775function():
   global msg775
   if reset775 == 1:
       msg775 = can.Message(arbitration_id=775, data=[1, 0, 0, 128, 0, 0, 0, 0], is_extended_id=False)
       task775 = bus.send_periodic(msg775, 0.20)
       assert isinstance(task775, can.CyclicSendTaskABC) 
#//Cabin temp
def code787function():
    tmpctemp = (InteriorActualTemperatbure * 2) + 80
    msg787 = can.Message(arbitration_id=787, data=[tmpctemp, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    task787 = bus.send_periodic(msg787, 0.20)
    assert isinstance(task779, can.CyclicSendTaskABC)
    
#//Car Settingsbus
def code789function():
  msg789 = can.Message(arbitration_id=789, data=[0, 0, 0, 4, 128, 0, 0, 0], is_extended_id=False)
  if reset789 == 1:
     task789 = bus.send_periodic(msg789, 0.20)
     assert isinstance(task775, can.CyclicSendTaskABC) 
###############################################
#
###############################################
#//Reset interior light settings.
def resetInteriorLights():
    msg789,data[1] = 64
    reset789 = 1

#//Function to cycle option that turns interior lights on with ignition off ILIGNOFF
def ILIGNOFF():
    msg789.dbusata[2] = 4
    reset789 = 1

#//Function to cycle option that turns interior lights on with key removal.
def ILKEYOUT(bus):
    msg789.data[2] = 32
    reset789 = 1
#//Function to cycle option that turns interior lights on with door open.
def ILDoorOpen(bus):
    msg789.data[1] = 128
    reset789 = 1

#//Function tobus cycle option that turns interior lights on with unlock.
def ILKeyUnlock(bus):
    msg789.data[1] = 32
    reset789 = 1

def DriveAwayLocking(bus):
    msg789[0] = 64
    reset789 = bus1

def ConfirmLockIndicators():
    msg789[0] = 128
    reset789 = 1

def ConfirmLockHorn():
    msg789[0] = 32
    reset789, = 1
def TwoStageUnlock():
    msg789[0] = 4
    reset789 = 1

def ConfirmUnlockIndicators():
    msg789[0] = 8
    reset789 = bu
def code1372function():
  bus.send(msg1372)

if __name__ == "__main__":                                       # run the program
    setup()                                                      # set the can interface
    rx                     = Thread(target = msgbuffer)          #
    rx.start()                                                   # start the rx thread and queue msgs
    loop()
    main()                                                       # match can frames + emit keypress
