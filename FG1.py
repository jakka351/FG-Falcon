#!/usr/bin/python3
#coding:utf-8
#################################################################################################################
# FG1ECUComms.py
# https://github.com/jakka351/FG-Falcon
#################################################################################################################
# Notes
#  1. This software can only be distributed with my written permission. It is for my own educational purposes and 
#     is potentially dangerous to ECU health and safety. 
#################################################################################################################
'''__    ___________    ____  /\     ___________             _________                                   __   
  / /    \_   _____/___/_   | \ \    \_   _____/ ____  __ __ \_   ___ \  ____   _____   _____   ______   \ \  
 / /      |    __)/ ___\|   |  \ \    |    __)__/ ___\|  |  \/    \  \/ /  _ \ /     \ /     \ /  ___/    \ \ 
 \ \      |     \/ /_/  >   |   \ \   |        \  \___|  |  /\     \___(  <_> )  Y Y  \  Y Y  \\___ \     / / 
  \_\     \___  /\___  /|___|    \ \ /_______  /\___  >____/  \______  /\____/|__|_|  /__|_|  /____  >   /_/  
              \//_____/           \/         \/     \/               \/             \/      \/     \/         
 Falcon Diagnostic Utility - [FG1ECUComms]'''
#############################################################################################################
'''
    Hooning through the sun...
    In a four-hundred-horsepower sleigh...
    O’er the roads we go...
    Boosting all the way...
    
    Bells on ford forums ring...
    Making spirits bright...
    Oh what fun it is to splice and hack...
    Jason's o'er the eeprom tonight!
    
    Oh!
    Jingle bells, Kayhan Smells,
    ASL all the way! (Dont Pay)
    Roland yells, Whiteford smells,
    Nigel laid an egg.
    
    Oh!
    ...what fun it is to ride
    In a pcm-tec-tuned sleigh.
    Hey!

    Jingle bells, Kayhan Smells,
    ASL all the way! (Dont Pay)
    Hey! 

    Oh what fun it is to ride...
    with red and flashing blue ... 
    chasing after you! 
    
'''
#############################################################################################################
# library imports
#############################################################################################################
import os, sys, time, queue, traceback
import PySimpleGUI as sg
from threading import *
from threading import Thread
from array import array
#############################################################################################################
# library imports
#############################################################################################################
import can 
#############################################################################################################
# Splash Image // pysimplegui // base 64
#############################################################################################################
#print = sg.Print  
#sg.theme('DarkTeal2')
#sg.set_options(element_padding=(1, 1))
#################################################################################################################
def splash():
    DISPLAY_TIME_MILLISECONDS = 500
    sg.Window('Window Title', [[sg.Image(data=splash)]], transparent_color=sg.theme_background_color(), no_titlebar=True, keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)

#splash()
#################################################################################################################
# GNU/Linux socketcan canbus interfaces //
# // vcan0 is virtual socket for testing on linux socketcan
# // virtualcan is https://github.com/windelbouwman/virtualcan cross platform
#################################################################################################################
businput     = 'socketcan'
channelinput = 'can0'
bitrateinput = '125000'
MidSpeedCan  = can.interface.Bus(channel=channelinput, bustype=businput, bitrate=bitrateinput) # MS CAN
#HighSpeedCan  = can.interface.Bus(channel='com4', bustype=businput, bitrate=bitrateinput) # HS CAN
#################################################################################################################
# Message Length Carrier - byte 0 of diagnostic CAN messages 
# CAN_ID-DLC-[BYTE0]-BYTE1-BYTE2-BYTE3-BYTE4-BYTE5-BYTE6-BYTE7
#################################################################################################################
'''Len                                                   = {}
SingleFrame                                           = 0x00
Len[SingleFrame]                                      =[SingleFrame, 'Frame type: Single Frame', 0x0]
FirstFrame                                            = 0x10
Len[FirstFrame]                                       =[FirstFrame, 'Frame type: First Frame', 0x1]
ConsecutiveFrame                                      = 0x20
Len[ConsecutiveFrame]                                 =[ConsecutiveFrame, 'Frame type: Consecutive Frame', 0x2]
FlowControl                                           = 0x30
Len[FlowControl]                                      = [FlowControl, 'Frame type: FlowControl', 0x3]'''
#############################################################################################################
'''“Hi Jack,
With the way the FG2 ICC / Cluster thread is going, I've quickly lost interest in having the GTF signal configuration. 
My version of getting the gauges working includes reading the vehicle speed, drawing a speed history graph and 
reporting any 0-100 times (micro-controller timed) in big letters if it's under 10 seconds (I get 4.9 when the 
car only has me in it, or 5.3 if the car is full of people).  As I've already mentioned, I'm not going to change 
the way it works now, this was all just out of interest while I'm on holidays (for the next couple of weeks anyway).
I'm happy for you to use my software as already discussed, I've made some enhancements (remember, I don't take 
requests, but having used it over the past few days there were some things I wanted to improve - like fully 
implementing 1M-2M Ks EEPROM odo setting, which wasn't really super important.. Right-click on the find image
button to allow you to select the start address (instead of always being 0x15000 start of firmware) in case 
you know where it is, to find it faster..  Police mode override (I was leaving that out because of Forscan's 
ability to change it, but screw it, it's in now)..  Probably some more things too, but I've forgotten, oh - i
mage gamma adjust, but that's really dangerous and needs to be written down if you use it so you can re-find
the image without flashing the original firmware back.'''
#############################################################################################################
# ECU Rx & Tx CAN ID Dictionary 
#################################################################################################################
DiagSig_Tx                                            = dict()
DiagSig_Rx                                            = dict()
#################################################################################################################
# Antilock Brake Module     
ABS_DiagSig_Rx                                        = 0x760
DiagSig_Rx[ABS_DiagSig_Rx]                            = (ABS_DiagSig_Rx, "1. ABS 0x760", "Antilock Brake Module")
ABS_DiagSig_Tx                                        = 0x768
DiagSig_Tx[ABS_DiagSig_Tx]                            = [ABS_DiagSig_Tx, "ABS 0x768", "Antilock Brake Module"]
# Audio Control Module
ACM_DiagSig_Rx                                        = 0x727
DiagSig_Rx[ACM_DiagSig_Rx]                            = [ACM_DiagSig_Rx, "2. ACM 0x727", "Audio Control Module"]
ACM_DiagSig_Tx                                        = 0x72F
DiagSig_Tx[ACM_DiagSig_Tx]                            = [ACM_DiagSig_Tx, "ACM 0x72F", "Audio Control Module"]
# ACM_RadioDiag                                        = 0x6FC
#DiagSig_Rx[ACM_RadioDiag]                             = [ACM_RadioDiag, "ACM Radio Data System Diagnostics"]
# Audio Interface Module
AIM_DiagSig_Rx                                        = 0x767
DiagSig_Rx[AIM_DiagSig_Rx]                            = [AIM_DiagSig_Rx, "3. AIM 0x767", "Audio Inteface Module"]
AIM_DiagSig_Tx                                        = 0x76E
DiagSig_Tx[AIM_DiagSig_Tx]                            = [AIM_DiagSig_Tx, "AIM 0x76F", "Audio Inteface Module"]
# Body Electronics Module
BEM_DiagSig_Rx                                        = 0x726
DiagSig_Rx[BEM_DiagSig_Rx]                            = [BEM_DiagSig_Rx, "4. BEM 0x726", "Body Electronic Module"]
BEM_DiagSig_Tx                                        = 0x72E
DiagSig_Tx[BEM_DiagSig_Tx]                            = [BEM_DiagSig_Tx, "BEM 0x72E", "Body Electronic Module"]
# Bluetooth Phone Module
BPM_DiagSig_Rx                                        = 0x781
DiagSig_Rx[BPM_DiagSig_Rx]                            = [BPM_DiagSig_Rx, "5. BPM 0x781", "Bluetooth Phone Module"]
BPM_DiagSig_Tx                                        = 0x789
DiagSig_Tx[BPM_DiagSig_Tx]                            = [BEM_DiagSig_Tx, "BPM 0x789", "Bluetooth Phone Module"]
# Instrument Cluster
IC_DiagSig_Rx                                         = 0x720
DiagSig_Rx[IC_DiagSig_Rx]                             = [IC_DiagSig_Rx, "6. IPC 0x720", "Instrument Cluster"]
IC_DiagSig_Tx                                         = 0x728
DiagSig_Tx[IC_DiagSig_Tx]                             = [IC_DiagSig_Tx, "IPC 0x728", "Instrument Cluster"]
# Front Display Interface Module
FDIM_DiagSig_Rx                                       = 0x7A6
DiagSig_Rx[FDIM_DiagSig_Rx]                           = [FDIM_DiagSig_Rx, "7. FDIM 0x767", "Front Display Interface Module"]
FDIM_DiagSig_Tx                                       = 0x7AE
DiagSig_Tx[FDIM_DiagSig_Tx]                           = [FDIM_DiagSig_Tx, "FDIM 0x76F", "Front Display Interface Module"]
# HVAC Integrated Module
HIM_DiagSig_Rx                                        = 0x733
DiagSig_Rx[HIM_DiagSig_Rx]                            = [HIM_DiagSig_Rx, "8. HIM 0x733", "HVAC IntegratedModule"]
HIM_DiagSig_Tx                                        = 0x73B
DiagSig_Tx[HIM_DiagSig_Tx]                            = [HIM_DiagSig_Tx, "HIM 0x73B", "HVAC IntegratedModule"]
# Parking Aid Module
PAM_DiagSig_Rx                                        = 0x736
DiagSig_Rx[PAM_DiagSig_Rx]                            = [PAM_DiagSig_Rx, "9. PAM 0x736", "Parking Aid Module"]
PAM_DiagSig_Tx                                        = 0x73E
DiagSig_Tx[PAM_DiagSig_Tx]                            = [PAM_DiagSig_Tx, "PAM 0x73E", "Parking Aid Module"]
# Powertrain Control Module
PCM_DiagSig_Rx                                        = 0x7E0
DiagSig_Rx[PCM_DiagSig_Rx]                            = [PCM_DiagSig_Rx, "10. PCM 0x7E0", "Powertrain Contol Module Module"]
PCM_DiagSig_Tx                                        = 0x7E8
DiagSig_Tx[PCM_DiagSig_Tx]                            = [PCM_DiagSig_Tx, "PCM 0x7E8", "Powertrain Contol Module Module"]
#PcmRapidData1                                         = 0x6A0
#DiagSig_Tx[PcmRapidData1]                             = [PCM_DiagSig_Tx, PcmRapidData1, "Rapid Data"]
#PcmRapidData2                                         = 0x6A1
#DiagSig_Tx[PcmRapidData2]                             = [PCM_DiagSig_Tx, PcmRapidData2, "Rapid Data"]
# Powertrain Control Module[OnBoardDiagnostics] - EOBD
OBD_DiagSig_Rx                                        = 0x7DF
DiagSig_Rx[OBD_DiagSig_Rx]                            = [OBD_DiagSig_Rx, "11. OBDII 7DF", "On Board Diagnostics Emission Protocol"]
# Restaints Control Module
#RCM_DiagSig_Rx                                        = 0x737
#DiagSig_Rx[RCM_DiagSig_Rx]                            = [RCM_DiagSig_Rx, "RCM 0x736", "Restraints Control Module"]
#RCM_DiagSig_Tx                                        = 0x73F
#DiagSig_Tx[RCM_DiagSig_Tx]                            = [RCM_DiagSig_Tx, "RCM 0x73F", "Restraints Control Module"]
# Transmssion Control Module
TCM_DiagSig_Rx                                        = 0x7E1
DiagSig_Rx[TCM_DiagSig_Rx]                            = [TCM_DiagSig_Rx, "12. TCM 0x7E1", "Transmission Control Module"]
TCM_DiagSig_Tx                                        = 0x7E9
DiagSig_Tx[TCM_DiagSig_Tx]                            = [TCM_DiagSig_Tx, "TCM 0x7E9", "Transmission Control Module"]
# Steering Angle Sensor | Not sure about how this is accessed - suspect ABS module acts as gateway via hscan-private
#SAS_DiagSig_Rx                                        = 0x797
#DiagSig_Rx[SAS_DiagSig_Rx]                            = [SAS_DiagSig_Rx, "SAS 0x797", "Steering Angle Sensor"]
#SAS_DiagSig_Tx                                        = 0x79F
#DiagSig_Tx[SAS_DiagSig_Tx]                            = [SAS_DiagSig_Tx, "SAS 0x79F", "Steering Angle Sensor"]
#################################################################################################################
'''class FordCAN(object):
    def __init__(self, channel = 'com3', bustype = 'serial'):
        self.MidSpeedCan = can.interface.Bus(channel=channel, bustype=bustype, can_filters = [
          {"can_id": DiagSig_Rx.keys(), "can_mask": 0x7F, "extended": False},    
          {"can_id": DiagSig_Tx.keys(), "can_mask": 0x7F, "extended": False},    
          ])

'''
# ecuOption() selection menu - selects DiagSig_Rx for diagnostic service functions
#################################################################################################################
# _DiagSig_Rx = DiagSig_Rx[key]
#################################################################################################################
def ecuOption():
    global _DiagSig_Rx, fixed
    while(True):
        for key in DiagSig_Rx.keys(): print(DiagSig_Rx[key], ']' )
        _DiagSig_Rx = 0
        option      = ''
        try:
            option  = int(input(' Ecu Selection Options: '))
        except:
            print('   Wrong input. Please enter a number ...')
        if option      == 1:  
            _DiagSig_Rx = 0x760
            fixed       = 0x0 
            return _DiagSig_Rx, fixed
        elif option    == 2:  
            _DiagSig_Rx = 0x727
            fixed       = 0x4272616457
            return _DiagSig_Rx, fixed
        elif option    == 3:  
            _DiagSig_Rx = 0x767
            fixed       = 0x4272616457
            return _DiagSig_Rx, fixed
        elif option    == 4:  
            _DiagSig_Rx = 0x726 
            fixed       = 0x4272616457
            return _DiagSig_Rx, fixed
        elif option    == 5:  
            _DiagSig_Rx = 0x781 
            fixed       = 0x4272616457
            return _DiagSig_Rx, fixed
        elif option    == 6:  
            _DiagSig_Rx = 0x720 
            fixed       = 0x434F4C494E
            #MK1IPC1  = 0x434F4C494E
            #MKIIIPC1 = 0x21836A41D0                               
            #MKIIIPC3 = 0x40E234995F
            #MKIIIPC5 = 0x0926F26388
            return _DiagSig_Rx, fixed
        elif option    == 7:  
            _DiagSig_Rx = 0x7A6 
            fixed       = 0x4272616457
            return _DiagSig_Rx, fixed
        elif option    == 8:  
            _DiagSig_Rx = 0x733 
            fixed       = 0x0
            return _DiagSig_Rx, fixed
        elif option    == 9:  
            _DiagSig_Rx = 0x736 
            fixed       = 0x0
            return _DiagSig_Rx, fixed
        elif option    == 10: 
            _DiagSig_Rx = 0x7E0 
            fixed       = 0x0
            return _DiagSig_Rx, fixed
        elif option    == 11: 
            _DiagSig_Rx = 0x7DF 
            return _DiagSig_Rx
        elif option    == 12: 
            _DiagSig_Rx = 0x7E1 
            fixed       = 0x0
            return _DiagSig_Rx, fixed
        elif option == 13: 
            return
        else: print('Invalid option. Try again.')    
#################################################################################################################
# Ahhhah! The Secret Keys  
#################################################################################################################

'''
  fermec: 0x50c86a49f1 'icc seed key'
    // BA_BF_FG_SX_SY_Flash_Reader.Form1
  // Token: 0x04000104 RID: 260
  private byte[] EcuKey = new byte[]
  {
    8,
    0x30,
    0x61,
    0xA4,
    0xC5
  };

  0x720: {0x01: 0x434f4c494e, 0x03: 0x40E234995F, 0x11: 0x0926F26388},
  0x720: {0x01: 0xfa5fc0, 0x03: 0x92c13b},
  0x7A6: {0x01: 0x4272616457, 0x11: 0x128665},
  0x727: {0x01: 0x4272616457},
  0x781: {0x01: 0x4272616457},
  0x731: {0x01: 0x672a70, 0x11: 0x462a71},
  0x760: {0x01: 0x582613, 0x03: 0x76807f, 0x11: 0x06316b}
  0x720: {0x01: 0xBFA49056CD, 0x03: 0x40E234995F, 0x11: 0x0926F26388},
  0x730: {0x01: 0x9b2533},
  0x731: {0x01: 0x672a70, 0x11: 0x462a71},
  0x760: {0x01: 0x582613, 0x03: 0x76807f, 0x11: 0x06316b
  0x720vdo: {0x01: 0xbfa49056cd},
  0x7A6: {0x01: 0x4272616457}
  focus keys
    0x720: {0x01: 0xfa5fc0, 0x03: 0x92c13b},
    0x726: {0x01: 0xfaa8bd, 0x11: 0x128665},
    0x727: {0x03: 0x4ad0fb},
    0x7A6: {0x01: 0x9b2533},
    0x731: {0x01: 0x672a70, 0x11: 0x462a71},
    0x760: {0x01: 0x582613, 0x03: 0x76807f, 0x11: 0x06316b} 41 41 4A 47 53 57 39
  vcan0  72E   [8]  22 45 38 36 31 30 31 00'''
#################################################################################################################
# SocketCAN Message buffers - to run after DiagSig_Rx/Tx has been set
#################################################################################################################
'''I'll probably just put the new version in the github repository sometime next week with a note saying not to
use it, as I've bricked my Cluster with it once already, but with some advice to seek out professionals who
can do it for you and reflash the firmware if needed.  Something like that.
Just to reiterate, I don't want the GTF firmware anymore.  Enjoy using the software when you get your dongle. 
It's funny (weird) isn't it, so I think I'll just keep my distance from abs351. Jakka's a good guy though, 
he did seem to want my software working on his FG(I) but I don't think you can update the firmware on those, 
I can't download any from the Ford site - at least guessing the filenames. 
I can get into mode 0x87 (adjust) with 5 byte key "COLIN" but no other modes at all (like 0x02/0x85 firmware 
update). If I request security a 2nd time, it then says my key is not correct - so there may be something 
there. If you have any details on this, I'd like to try and get it working for Jakka?”'''
#################################################################################################################
# SocketCAN Message buffers - to run after DiagSig_Rx/Tx has been set
#################################################################################################################
def MidSpeedBuffer():
    global message, DiagSig_Tx, DiagSig_Rx
    while True:
        for i in range(8):
                message = MidSpeedCan.recv()
                if message.arbitration_id in DiagSig_Rx.keys():
                    return message
                if message.arbitration_id in DiagSig_Tx.keys():
                    return message
             
#################################################################################################################
# J2534 Message Buffers  - to run after DiagSig_Rx/Tx has been set
#################################################################################################################
'''even without J2534 support. If I want to extract the firmware more quickly, I'll use my micro-controller that
already runs as fast as an FG2/X Cluster can provide it the data, where that solid MC code base was the template f
or the ELM327 exe version. I put the exe there (and updated it today with more error handling) so the "ordinary guy"
can get the data. I've not included the code to produce a valid ".vbf" Ford firmware file, as I hope that "
guy" will give me their raw data to do so - and I can upload more firmwares to the github repo.
But I'm glad you noticed 
JasonACT is offline'''
#################################################################################################################
def service(_DiagSig_Rx, var1, var2):
    var1 = ServiceRequest.keys()
    var2 = {
        sessionType.keys(),
        resetType.keys(),
        securityLevel.keys(),
        routine.keys(),
        responseType.keys(),
        _controlDTCSetting.keys(),
        commandB1.keys()     
    }  
    msg = can.Message(arbitration_id = _DiagSig_Rx,
                                data = [0x02, var1, var2, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id = False)
    try:
        MidSpeedCan.send(msg)
    except can.CanError:
        pass
#################################################################################################################
# SocketCAN Diagnostic Message Parser - only parses diagnostic tx/rx messages
#################################################################################################################
def Parser(message):
    global MidSpeedCan
    messageSent = 0
    responsePos = 0
    responseNeg = 0
    try:   
        while True:
            for i in range(1):
                if message.arbitration_id in DiagSig_Rx.keys() and message.data[1] in ServiceRequest.keys():
                    messageSent = 1
                    print("   [ >>-------->> Rx ECU:")
                    print("   [ DiagSig_Rx:", DiagSig_Rx[message.arbitration_id], " Service Request:  ", ServiceRequest[message.data[1]], "  ]  ")
                    print("   [", message, "]")
                    print("   [ ________________________________________________________________________________________________________________    ] // ")  
                    return messageSent

                elif message.arbitration_id not in DiagSig_Rx.keys():
                    pass 

                if message.arbitration_id in DiagSig_Tx.keys() and (message.data[1] - 0x40) in ServiceRequest.keys():
                    responsePos = 1
                    print("   [ <<--------<< Tx ECU:")
                    print("   [ DiagSig_Tx:", DiagSig_Tx[message.arbitration_id], "Positive Response:  ", ServiceRequest[message.data[1] - 0x40], "  ]  ")
                    print("   [", message, "]")
                    print("   [ ______________________________________________________________________________________________________________________] //  ")
                    return responsePos
                elif message.arbitration_id in DiagSig_Tx.keys() and message.data[1] == 0x7F and (message.data[2] - 0x40) in ServiceRequest.keys() and message.data[3] in NegativeResponseCode.keys():
                    responseNeg = 1 
                    print("   [   Negative Response Code:", NegativeResponseCode[message.data[3]], "                                                                                                           ] ")
                    print("   [ <<--------<< Tx ECU:")
                    print("   [", message, "]")
                    print("   [ DiagSig_Tx:", DiagSig_Tx[message.arbitration_id], "[ 0x7F Negative Response:", ServiceRequest[(message.data[2] - 0x40)], "Error Code:",  NegativeResponseCode[message.data[3]], "]")
                    print("   ------//FG1ECUComms.py         |            6FPA-util  ---//")
                    return responseNeg
                elif message.arbitration_id not in DiagSig_Tx.keys():
                    pass 

    except KeyError:
        pass
    except KeyboardInterrupt:
        sys.exit(0)  
    except can.CanError:
        print("can error")                   
    except Exception:
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
    except OSError:
        sys.exit()
#################################################################################################################
# SocketCAN parser results
#################################################################################################################
def PARSER_RESPONSE(_DiagSig_Rx): 
   Parser()
   if messageSent == 1: 
       print("request sent onto canbus for", DiagSig_Rx[_DiagSig_Rx])
   if responsePos == 1:
       print("recieved positive response to request from:", DiagSig_Tx[(_DiagSig_Rx + 0x08)], " for Service:", ServiceRequest )
   if responseNeg == 1:
       print("recieved negative response code from ecu:",  DiagSig_Tx[(_DiagSig_Rx + 0x08)] )
   return 
   
# WIP
#################################################################################################################
# SocketCAN HighSpeed Can parser - describes all messages on the highspeed bus in real time
#################################################################################################################
# WIP
#################################################################################################################
# Diagnostic Services Dictionary
#################################################################################################################
ServiceRequest                                            = dict()
#################################################################################################################
# On Board Diagnostics - EOBD - DiagSig_Rx 0x7DF - DiagSig_Tx 0x7E8    
#################################################################################################################
# use external library for obd2
#################################################################################################################
'''
startDiagnosticSession (ref. KWP-GRP-1.5, 6.1.1)
The parameters values supported for the diagnosticMode parameter of the startDiagnosticSession
service are listed in Table 5. No other diagnosticMode values shall be supported.
The baudrateIdentifier parameter shall not be used with this or any service.
One and only one diagnostic session shall be active in an ECU at all times. Diagnostic session $81
shall be active by default upon power-up of an ECU (i.e., a tester request message shall not be
required). A tester shall have the capability of changing from any one diagnostic session to another
without performing any type of security access (refer to section 2.2.2.7.6 for additional details).
Diagnostic session $87 (ECUAdjustmentMode), if implemented, shall be an extended diagnostic
session that is a superset of the diagnostic functionality supported in diagnostic session $81.
Diagnostic session $85 (ECUProgrammingMode), if implemented, shall be used only for Method 3
file download and shall be the implementation of the Method 3 programming requirements as
described in MC-v2003.0.
When an ECU transitions from any diagnostic session to another diagnostic session, the ECU shall
reset all active diagnostic functionality that is not supported in the new diagnostic session (e.g.,
security access, I/O control), with the exception of changes written to long term memory. For
example, if an ECU only supports service $2F (inputOutputControlByCommonID) in diagnostic
session $87 then any actively controlled inputs or outputs shall revert back to the normal value as
determined by the control system upon a transition from session $87 to session $81.
An ECU is allowed a 750ms re-initialization period upon returning to the default diagnostic session
($81) from any other diagnostic session. During this re-initialization period the ECU is not required to
respond to any diagnostic requests.
The only defined vehicleManufacturerSpecific diagnostic session is $F0 and is defined as
EOLExtendedDiagnosticSession. Any ECU that needs to grant special privileges to an End of Line
test tool shall implement diagnostic session $F0 to provide access to these privileges. For example, an
ABS module that normally exits to the defaultDiagnosticSession when vehicle speed is greater than a
given value may maintain the EOLExtendedDiagnosticSession (despite the vehicle speed). Diagnostic
session $F0 shall be reserved only for use by End of Line test tools in assembly plants and shall be
implemented only when needed to verify communication with an End of Line tester. This
EOLExtendedDiagnosticSession shall grant access to all functionality (e.g., diagnostic services,
privileges, input/output control, etc.) that is necessary during the assembly testing and shall contain a
superset of the diagnostic functionality supported in diagnostic session $87 (ECUAdjustmentMode).
SystemSupplierSpecific diagnostic sessions shall not be supported by Ford test tools. All implemented
systemSupplierSpecific diagnostic sessions shall be specified by the module designer and documented
in the ECU's Subsystem Specific Diagnostic Specification (SSDS/Part 2).''' 
#################################################################################################################
# Open Diagnostic Session Request - Dictionary
#################################################################################################################
# ServiceRequest dict
startDiagnosticSession                                = 0x10
ServiceRequest[startDiagnosticSession]                = [startDiagnosticSession, "startDiagnosticSession", "0x10"]
reportDiagnosticState                                 = 0x50
ServiceRequest[reportDiagnosticState]                 = [reportDiagnosticState, "reportDiagnosticState", "Ecu Response"]
# sub-dict sessionType
sessionType                                           = dict()
standardDiagnosticSession                             = 0x81
sessionType[standardDiagnosticSession]                = ["1", standardDiagnosticSession, "standardDiagnosticSession"]
ecuProgrammingSession                                 = 0x85
sessionType[ecuProgrammingSession]                    = ["2", ecuProgrammingSession, "ecuProgrammingSession"]
ecuAdjustmentSession                                  = 0x87
sessionType[ecuAdjustmentSession]                     = ["3", ecuAdjustmentSession, "ecuAdjustmentSession"]
vehicleManufacturerSpecific                           = 0xF0
sessionType[vehicleManufacturerSpecific]              = ["4", vehicleManufacturerSpecific, "vehicleManufacturerSpecific"]
systemSupplierSpecific                                = 0xFA
sessionType[systemSupplierSpecific]                   = ["5", systemSupplierSpecific, "systemSupplierSpecific"]
#################################################################################################################
# The function that sends the Diagnostic Service Request:
#     to use - "startDiagnosticSession({CAN_ID}, {sessionType}"
#     where can ID is sent from tester to ecu ala _DiagSig_Rx
#     ecuOption() is used to fill _DiagSig_Rx
#################################################################################################################
def startDiagnosticSession(_DiagSig_Rx, sessionType):
    msg = can.Message(arbitration_id = _DiagSig_Rx,
                                data = [0x02, 0x10, sessionType, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id = False)
    try:
        response = MidSpeedCan.recv()
        MidSpeedCan.send(msg)
        Parser(response)
        return
    except can.CanError:
        sg.Print("Message NOT sent")
        time.sleep(10)
        return
##################################################################################################################
# The selection menu that appears in the terminal 
#      ecuOption() is responsible for selecting the CAN_ID/DiagSigRx that ends up in startDiagnosticSession(DiagSig_Rx, sessionType) 
#################################################################################################################
def startDiagnosticSessionMenu():
    ecuOption()    
    while(True):
        for key in sessionType.keys(): print ('     ', key, '-', sessionType[key], ']' )
        option = ''
        try:
            option = int(input(' Input number 1-5 to select diagnostic session type:  [6 to return] '))
        except:
            print('   Wrong input. Please enter a number ...')
        if option == 1:
            cleanscreen()
            startDiagnosticSession(_DiagSig_Rx, standardDiagnosticSession)
        elif option == 2: 
            cleanscreen()
            startDiagnosticSession(_DiagSig_Rx, ecuProgrammingSession)
        elif option == 3:
            cleanscreen()
            startDiagnosticSession(_DiagSig_Rx, ecuAdjustmentSession)
        elif option == 4:
            cleanscreen()
            startDiagnosticSession(_DiagSig_Rx, vehicleManufacturerSpecific)
        elif option == 5:
            cleanscreen()
            startDiagnosticSession(_DiagSig_Rx, systemSupplierSpecific)
        elif option == 6:
            return
        else:
            print('Invalid option. Try again')
#################################################################################################################
'''ECUReset 
    z eOnly the powerOn value of the resetMode (RM_) parameter shall be supported. The resetStatus (RS_)
parameter shall not be supported.
The positive response to an ECUReset (service $11) request shall occur before the ECU performs the
reset. An ECU is allowed a 750ms re-initialization period after providing a positive response to an
ECUReset request. During this re-initialization period the ECU is not required to respond to any
diagnostic requests.'''
#################################################################################################################
# ecuReset SID 0x11 - Dictionary 
#################################################################################################################
ecuReset                                              = 0x11
ServiceRequest[ecuReset]                              = [ecuReset, "ecuReset", "0x11"]
resetType                                             = dict()
softReset                                             = 0x01
resetType[softReset]                                  = [softReset, "1. ecuReset Soft Reset", "0x1101"]
hardReset                                             = 0x02
resetType[hardReset]                                  = [hardReset, "2. ecuReset Hard Reset", "0x1102"]
#################################################################################################################
# ecuReset SID 0x11 - Function 
#################################################################################################################
def ecuReset():
    def Reset(_DiagSig_Rx, resetType):
        msg = can.Message(arbitration_id = _DiagSig_Rx,
                          data           = [0x02, 0x11, resetType, 0, 0, 0, 0, 0], is_extended_id = False)
        try:
            response = MidSpeedCan.recv()
            MidSpeedCan.send(msg)
            Parser(response)
            return
        except can.CanError:
            print("Message NOT sent")
        

    ecuOption()
    def resetOption():
        for key in resetType.keys(): print ('     ', key, '-', resetType[key], ']' )
    while(True):
        resetOption()
        option = ''
        try:
            option = int(input(' Select Reset Type:  // Type [3] to return'))
        except:
            print('   Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            cleanscreen()
            Reset(_DiagSig_Rx, 0x01)
        elif option == 2:
            cleanscreen() 
            Reset(_DiagSig_Rx, 0x02)
        elif option == 3:
            cleanscreen()
            menu()
        else:
            print('Invalid option. Try again')
#################################################################################################################
# Troubleshooting SID's
# Diagnostic Information + DTCs 
#################################################################################################################
readFreezeFrameData                                   = 0x12
ServiceRequest[readFreezeFrameData]                   = [readFreezeFrameData, "readFreezeFrameData", "0x12"]
reportFreezeFrameData                                 = 0x52
ServiceRequest[reportFreezeFrameData]                 = [reportFreezeFrameData, "0x52"]
requestStoredCodes                                    = 0x13
ServiceRequest[requestStoredCodes]                    = [requestStoredCodes, "requestStoredCodes", "0x13"] 
clearDiagnosticInformation                            = 0x14
ServiceRequest[clearDiagnosticInformation]            = [clearDiagnosticInformation, "clearDiagnosticInformation", "0x14"]
readDTCByStatus                                       = 0x18
ServiceRequest[readDTCByStatus]                       = [readDTCByStatus, "readDTCByStatus", "0x18"]
def ReadDtc(_DiagSig_Rx):
    msg = can.Message(arbitration_id = _DiagSig_Rx,
                      data           = [0x02, readDTCByStatus, 0x00, 0xFF, 0, 0, 0, 0], is_extended_id = False)
    try:
        response = MidSpeedCan.recv()
        MidSpeedCan.send(msg)
        Parser(response)
        return
    except can.CanError:
        print("Message NOT sent")

def clearDtc(_DiagSig_Rx): 
    msg = can.Message(arbitration_id = DiagSig_Rx.keys(),
                      data           = [0x02, clearDiagnosticInformation, 0, 0, 0, 0, 0, 0], is_extended_id = False)
    # // clear dtc information for all the modules
    for keys in DiagSig_Rx.keys():
        try:
            MidSpeedCan.send(msg)
            PARSER_RESPONSE(_DiagSig_Rx)    
        except can.CanError:
            print("Message NOT sent")
        Parser()
#################################################################################################################
# SID 0x20 Return to standard ECU operating state
#################################################################################################################
operationalStateEntryRequest                          = 0x20
ServiceRequest[operationalStateEntryRequest]          = [operationalStateEntryRequest, "operationalStateEntryRequest", "0x20"]
#################################################################################################################
''' example reading VIN number on BPM:
  vcan0  781   [8]  02 21 00 00 00 00 00 00 request service 21
  vcan0  789   [8]  10 13 61 00 36 46 50 41 here  you go msg 1
  vcan0  781   [8]  30 00 00 00 00 00 00 00              thanks!
  vcan0  789   [8]  21 41 41 4A 47 53 57 39              msg2
  vcan0  789   [8]  22 45 38 36 31 30 31 00              msg3
  vcan0  781   [8]  02 10 81 00 00 00 00 00 take me back to standard state
  vcan0  789   [8]  02 50 81 00 00 00 00 00 yes okay no problem
'''
#################################################################################################################
# SID 0x21 readDataByLocalID
#################################################################################################################
readDataByLocalID                                     = 0x21
ServiceRequest[readDataByLocalID]                     = [readDataByLocalID, "readDataByLocalID", "0x21"]
dataIndentifier                                       = dict()
vehicleIndentificationNumber                          = 0x00
dataIndentifier[vehicleIndentificationNumber]         = [vehicleIndentificationNumber]
#################################################################################################################
# Service 0x21 readDataByLocalID Function  // Read vehicleIdentificationNumber from ECU (_DiagSig_Rx)
#################################################################################################################
def readDataByLocalID(_DiagSig_Rx, DID):
    msg  = can.Message(arbitration_id = _DiagSig_Rx,
                           data           = [0x02, readDTCByStatus, vehicleIndentificationNumber, 0, 0, 0, 0, 0], is_extended_id = False)
    fctl = can.Message(arbitration_id = _DiagSig_Rx,
                           data           = [0x30, 0, 0, 0, 0, 0, 0, 0], is_extended_id = False)  
    try:
        MidSpeedCan.send(msg)
        response = MidspeedCan.recv()
        Parser(response)
        if response.data[0] == 0x10:
            vin0 = response.data
            MidSpeedCan.send(fctl)
        if response.data[0] == 0x21:
            vin1 = response.data 
        if response.data[0] == 0x22:
           vin2 = response.data
        if response.data[0] == 0x23:
           vin3 = response.data
        vin = (vin0, vin1, vin2, vin3)
        print("VIN:", vin)  
    except can.CanError:
        print("Message NOT sent")
    Parser()
#########################################################################################################
# SID 0x22 readMemoryByCommonID - Mode 22 Requests - VIN, Firmware revision, live data
#################################################################################################################
readMemoryByCommonID                                  = 0x22
ServiceRequest[readMemoryByCommonID]                  = [readMemoryByCommonID, "readMemoryByCommonID", "0x22"]
CommonID                                              = dict()
#CommonID[0xD100]
#CommonID[0xE200]
CommonID[0xE400]                                      = ["FNOS CAN Driver Version Number", ""]
CommonID[0xE402]                                      = ["FNOS NM Junior/Node Management Version Number", ""]
CommonID[0xE403]                                      = ["FNOS Interaction Layer Version Number", ""]
CommonID[0xE404]                                      = ["FNOS Network Initialization Version Number", ""]
CommonID[0xE405]                                      = ["FNOS Transport Layer Version Number", ""]
CommonID[0xE406]                                      = ["FNOS Diagnostics Version Number", "" ]
CommonID[0xE407]                                      = ["FNOS Generation Tool Version Number", "" ]
CommonID[0xE408]                                      = ["FNOS Bootloader Version Number", "" ]
CommonID[0xE409]                                      = ["FNOS Database Version Number", "" ] 
# these all worked with mk1 ipc :) 
#cansend can0 736#0325E2005500000000
#################################################################################################################
# SID 0x23 readMemoryByAddress
#################################################################################################################
readMemoryByAddress                                   = 0x23
ServiceRequest[readMemoryByAddress]                   = [readMemoryByAddress, "readMemoryByAddress", "0x23"] 
#################################################################################################################
# SID 0x24 
#################################################################################################################
requestCommonIDScalingMasking                         = 0x24
ServiceRequest[requestCommonIDScalingMasking]         = [requestCommonIDScalingMasking, "requestCommonIDScalingMasking", "0x24"] 
#################################################################################################################
# SID 0x25
#################################################################################################################
stopTransmittingRequestedData                         = 0x25
ServiceRequest[stopTransmittingRequestedData]         = [stopTransmittingRequestedData, "stopTransmittingRequestedData", "0x25"] 
#############################################################################################################
'''The Phantom Function
Attack of the VCM Clones
Revenge of the Flash
A New Code
The EEPROM Strikes Back
Return of the Faultcode
You sent
my best post ever
jakka351'''
#################################################################################################################
# SID 0x27 SecurityAccess request
#################################################################################################################
requestSecurityAccess                                 = 0x27
ServiceRequest[requestSecurityAccess]                 = [requestSecurityAccess, "requestSecurityAccess", "0x27"]
reportSecurityAccess                                  = 0x67
ServiceRequest[reportSecurityAccess]                  = [reportSecurityAccess, "reportSecurityAccess", "0x27 Ecu Response"]
# the level of access in the request
securityLevel                                         = dict()
levelOne                                              = 0x01
securityLevel[levelOne]                               = [levelOne, "Security Access Level 1, 0x2701"]
levelTwo                                              = 0x03
securityLevel[levelTwo]                               = [levelTwo, "Security Access Level 2, 0x2703"]
#################################################################################################################
# Usage: requestSecurityAccess(DiagSig_Rx, securityLevel)
#
#################################################################################################################
def requestSecurityAccess(_DiagSix_Rx, securityLevel):
    ecuOption()  
    #socketcan
    msg = can.Message(arbitration_id = _DiagSig_Rx,
                      data           = [0x02, 0x27, securityLevel, 0, 0, 0, 0, 0] , is_extended_id=False)
    try:
        message    = MidSpeedCan.recv()
        MidSpeedCan.send(msg)
        if messsage.arbitration_id == (_DiagSig_Rx + 8) and message.data[1] == 0x67:
            print(message)
            seed    = message.data[1], message.data[2], message.data[3]
            seed[0] = message.data[1]
            seed[1] = message.data[2]
            seed[2] = message.data[3]
            print("Got Seed: ", seed)
            return seed
        else:
            pass
    except can.CanError():
        print("Service 0x27 requestSecurityAccess failed.")
#############################################################################################################
# function that generates the key
#############################################################################################################
def KeyGen(seed, fixed):
    seed   = requestSecurityAccess(_DiagSix_Rx, 0x01)
    try: 
        challengeCode = array('Q')
        challengeCode.append(fixed & 0xff)
        challengeCode.append((fixed >> 8) & 0xff)
        challengeCode.append((fixed >> 16) & 0xff)
        challengeCode.append((fixed >> 24) & 0xff)
        challengeCode.append((fixed >> 32) & 0xff)
        challengeCode.append(seed[2])
        challengeCode.append(seed[1])
        challengeCode.append(seed[0])
        temp1 = 0xC541A9
        for i in range(64):
            abit = temp1 & 0x01
            chbit = challengeCode[7] & 0x01
            bbit = abit ^ chbit
            temp2 = (temp1 >> 1) + bbit * 0x800000 & -1
            temp1 = (temp2 ^ 0x109028 * bbit) & -1
            challengeCode[7] = challengeCode[7] >> 1 & 0xff
            for a in range(7, 0, -1):
                challengeCode[a] = challengeCode[a] + (challengeCode[a - 1] & 1) * 128 & 0xff
                challengeCode[a - 1] = challengeCode[a - 1] >> 1
        key = [ temp1 >> 4 & 0xff, ((temp1 >> 12 & 0x0f) << 4) + (temp1 >> 20 & 0x0f), (temp1 >> 16 & 0x0f) + ((temp1 & 0x0f) << 4) ]
        print("Succesfully got key: {key}")
        return key
    except can.CanError():
        print("CAN Error")            
#############################################################################################################
# function to send key 
# Usage: SendKey(key) should be all that needs to be called.
#############################################################################################################
def SendKey(key):
    key = Keygen(seed)
    keyResponse   = can.Message(arbitration_id = _DiagSig_Rx,
                          data           = [0x02, 0x27, key[0], key[1], key[2], 0, 0, 0], is_extended_id = False)
    try:
        message    = MidSpeedCan.recv()
        MidSpeedCan.send(keyResponse)
        if messsage.arbitration_id == (_DiagSig_Rx + 8)  and message.data[1] == 0x67:
            print(message)
            return
        else:
            pass
    except can.CanError():
        print("CAN Error")            

    '''j2534 == 1:
        msg = J2534.ptTxMsg(ProtocolID.CAN, 0)
        msg.setIDandData(DiagSig_Rx, [0x02, 0x27, securityLevel, 0, 0, 0, 0, 0])
        try:
            J2534.ptWtiteMsgs(channelID, msg, 1, 100)
            print(msg, " sent on {}".format(ChannelID))
            
        seedResponse = MidSpeedCan.recv()
        # use message buffer to get msgs
        if seedResponse.data[1] == 0x67:
            seed = seedResponse.data[bytearray(b'\xFA\x01\x02'
            
            print(seedResponse)
            print(seed)
            return seed
            keygen(seed, fixedbytes)
            sendKey()
        else:
            pass
    except can.CanError:
        print("Message NOT sent")'''
#################################################################################################################
# SID 0x28 requestCommunicationControl
#################################################################################################################
requestCommunicationControl                           = 0x28
ServiceRequest[requestCommunicationControl]           = [requestCommunicationControl, "requestCommunicationControl", "0x28"]    
#################################################################################################################
# SID 0x2A requestDiagnosticDataPacket
#################################################################################################################
requestDiagnosticdataPacket                           = 0x2A
ServiceRequest[requestDiagnosticdataPacket]           = [requestDiagnosticdataPacket, "requestDiagnosticdataPacket", "0x2A"]   
#################################################################################################################
# SID 0x2C dynamicallyDefineDiagnosticDataPacket
#################################################################################################################
dynamicallyDefineDiagnosticDataPacket                 = 0x2C
ServiceRequest[dynamicallyDefineDiagnosticDataPacket] = [dynamicallyDefineDiagnosticDataPacket, "dynamicallyDefineDiagnosticDataPacket","0x2C"]
#################################################################################################################
# SID 0x2E writeDataByCommonID
#################################################################################################################
writeDataByCommonID                                   = 0x2E
ServiceRequest[writeDataByCommonID]                   = [writeDataByCommonID, "writeDataByCommonID","0x2E"]
#################################################################################################################
# SID 0x2F inputOutputControlByLocalID
#################################################################################################################
inputOutputControlByLocalID                           = 0x2F
ServiceRequest[inputOutputControlByLocalID]           = [inputOutputControlByLocalID, "inputOutputControlByLocalID","0x2F"]
#################################################################################################################
# SID 0x31/0x32 start/stopRoutineByLocalIdentifier - Self Test & Assembly Self Test
#################################################################################################################
startRoutineByLocalIdentifier                         = 0x31    
ServiceRequest[startRoutineByLocalIdentifier]         = [startRoutineByLocalIdentifier, "startRoutineByLocalIdentifier","0x31"]    
stopRoutineByLocalIdentifier                          = 0x32
ServiceRequest[stopRoutineByLocalIdentifier]          = [stopRoutineByLocalIdentifier, "stopRoutineByLocalIdentifier","0x32"]
routine                                               = dict()
onDemandSelfTest                                      = 0x02
routine[onDemandSelfTest]                             = [onDemandSelfTest, "On Demand Self-Test, routine 0x02"]
executeDownloadedRoutine                              = 0x05
routine[executeDownloadedRoutine]                     = [executeDownloadedRoutine, "executeDownloadedRoutine"]
assemblySelfTest                                      = 0x11 # need to check this
routine[assemblySelfTest]                             = [assemblySelfTest, "Assembly Self Test, routine 0x11"]
keyOnEngineOff                                        = 0x00
routine[keyOnEngineOff]                               = [keyOnEngineOff]
keyOnEngineRunning                                    = 0x00
routine[keyOnEngineRunning]                           = [keyOnEngineRunning, ""]
audioControlModuleCalibration                         = 0x00
routine[audioControlModuleCalibration]                = [audioControlModuleCalibration, ""]
#################################################################################################################
# On-Demand Self Test
#################################################################################################################
def selfTest():
    print("please select the module to self-test:")
    ecuOption()
    selfTest = can.Message(arbitration_id =_DiagSig_Rx, 
                           data           = [0x03, 0x31, onDemandSelfTest, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    try:
        print("Starting On-Demand Module Self Test for ", _DiagSig_Rx)
        MidSpeedCan.send(selfTest)
        print("Testing...")
        print("Message sent on {}".format(MidSpeedCan.channel_info))
        print(selfTest)
        Parser() # pehaps change this to a threading thread rx.start type
        selfTestResult()      
    except can.CanError:
        print("Message NOT sent")
#################################################################################################################
# SID 0x33 requestRoutineResultsByLocalID   
#################################################################################################################
requestRoutineResultsByLocalID                        = 0x33
ServiceRequest[requestRoutineResultsByLocalID]        = [requestRoutineResultsByLocalID, "requestRoutineResultsByLocalID","0x33"]
def selfTestResult():
    selfTestResult = can.Message(arbitration_id =_DiagSig_Rx, 
                                 data           =[0x03, 0x33, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    try:
        MidSpeedCan.send(selfTestResult)
        print("Message sent on {}".format(MidSpeedCan.channel_info))
        print(selfTestResult)
        # need to put a readDtc() here
    except can.CanError:
        print("Message NOT sent")
#################################################################################################################
# SID 0x34 requestDownload
#################################################################################################################
requestDownload                                       = 0x34
ServiceRequest[requestDownload]                       = [requestDownload, "requestDownload","0x34"]
#################################################################################################################
# SID 0x35 requestUpload
#################################################################################################################
requestUpload                                         = 0x35
ServiceRequest[requestUpload]                         = [requestUpload, "requestUpload","0x35"]
#################################################################################################################
# SID 0x36 transferData
#################################################################################################################
transferData                                          = 0x36
ServiceRequest[transferData]                          = [transferData, "transferData","0x36"]
#################################################################################################################
# SID 0x37 requestTransferExit
#################################################################################################################
requestTransferExit                                   = 0x37
ServiceRequest[requestTransferExit]                   = [requestTransferExit, "requestTransferExit","0x37"]
#################################################################################################################
# SID 0x3B writeDataByLocalId
#################################################################################################################
writeDataByLocalId                                    = 0x3B
ServiceRequest[writeDataByLocalId]                    = [writeDataByLocalId, "writeDataByLocalId","0x3B"]
#################################################################################################################
# SID 0x3C requestReadMemoryBlock
#################################################################################################################
requestReadMemoryBlock                                = 0x3C
ServiceRequest[requestReadMemoryBlock]                = [requestReadMemoryBlock, "requestReadMemoryBlock","0x3C"]
#################################################################################################################
# SID 0x3D writeMemoryByAddress
#################################################################################################################
writeMemoryByAddress                                  = 0x3D
ServiceRequest[writeMemoryByAddress]                  = [writeMemoryByAddress, "writeMemoryByAddress","0x3D"]
#################################################################################################################
# SID 0x3E tester present signal
#################################################################################################################
testerPresent                                         = 0x3E
ServiceRequest[testerPresent]                         = [testerPresent, "testerPresent", "0x3E"]
# request a response/no response from ecu
responseType                                          = dict()
requestResponse                                       = 0x01
responseType[requestResponse]                         = ["01 Request Response"]
suppressResponse                                      = 0x02
responseType[suppressResponse]                        = ["02 Suppress Response"]
#############################################################################################################
#testerPresent Function - DiagSig_Rx pulled from ecuOption() menu
#############################################################################################################
def testerPresent(_DiagSig_Rx, responseType):
    tester = can.Message(arbitration_id = _DiagSig_Rx,
                        data           = [0x02, 0x3E, responseType, 0, 0, 0, 0, 0],
                        is_extended_id = False)
    try:
        task = MidSpeedCan.send_periodic(tester, 2)
        print("Message sent on {}".format(MidSpeedCan.channel_info))
        print(tester)
        print("testerPresent message being sent every 2 seconds...")
    except can.CanError:
        print("Message NOT sent")
#############################################################################################################
# Service 0x85 controlDTCsetting
#############################################################################################################
controlDTCSetting                                     = 0x85
ServiceRequest[controlDTCSetting]                     = [controlDTCSetting, "controlDTCSetting", "0x85"] 
#############################################################################################################
_controlDTCSetting                                    = dict()
settingOn                                             = 0x01
_controlDTCSetting[settingOn]                         = [settingOn, 'controlDTCSet to On,' '0x85']
settingOff                                            = 0x02
_controlDTCSetting[settingOn]                         = [settingOff, 'controlDTCSet to Off,' '0x85']
#############################################################################################################
# Service Id 0x85 controlDtcSetting function
#############################################################################################################
def controlDTCSetting(_DiagSig_Rx, _controlDTCSetting):
    controlDTC = can.Message(arbitration_id = _DiagSig_Rx,
                             data           = [0x02, 0x85, _controlDTCSetting, 0, 0, 0, 0, 0], is_extended_id = False)
    try:
        MidSpeedCan.send(controlDTC)
        Parser()
        if messageSent == 1: 
            print("request sent onto canbus for", DiagSig_Rx[_DiagSig_Rx])
        if responsePos == 1:
            print("recieved positive response to request from:", DiagSig_Tx[(_DiagSig_Rx + 0x08)] )
        if responseNeg == 1:
            print("recieved negative response code from ecu:",  DiagSig_Tx[(_DiagSig_Rx + 0x08)] )
    except can.CanError:
        print("Message NOT sent")
#############################################################################################################
requestDiagnosticDataPacket                           = 0xA0
ServiceRequest[requestDiagnosticdataPacket]           = [requestDiagnosticdataPacket, "requestDiagnosticdataPacket", "0xA0"]
#############################################################################################################
dynamicallyDefineDataPacket                           = 0xA1
ServiceRequest[dynamicallyDefineDataPacket]           = [dynamicallyDefineDataPacket, "dynamicallyDefineDataPacket", "0xA1"]
#############################################################################################################
# sumitomo wiring systems australia
# fdim acm bpm aim modules
# firmware 
swsaManufacturerStateEntry                             = 0x00
ServiceRequest[swsaManufacturerStateEntry]             = ["SWSA", "ICC Firmware Update"]
# firmware upload/download
def fdimFirmware():
    #securityAccess
    #sec. bootloader
    pass
#############################################################################################################
noStoredCodesLoggingStateEntry                        = 0xB0
ServiceRequest[noStoredCodesLoggingStateEntry]        = ["noStoredCodesLoggingStateEntry", "0xB0"]
#############################################################################################################
'''15.7 Supplier Reserved Command Range
The range of commands from $F000 through $FFFF are reserved for use by ECU suppliers. Supplier
reserved commands do not need to be approved by the R&VT EESE Network Communication Core
Section. All supplier reserved commands shall be defined in the ECUs Subsystem Specific Diagnostic
Specification. The exceptions to the supplier reserved range are commands $F001, $F004, $F010, and
$FACE. These four commands are already assigned specific functionality by Ford Motor Company and
are not available for use as supplier specific.
NOTE: Supplier reserved commands are not supported by Ford diagnostic service tools.'''
#############################################################################################################
# Service 0xB1 diagnosticCommand 
#############################################################################################################
diagnosticCommand                                     = 0xB1
ServiceRequest[diagnosticCommand]                     = ["diagnosticCommand", "0xB1"]

commandB1                                             = dict()
flashErase                                            = 0x0000
commandB1[flashErase]                                 = [flashErase]
operationalStrategyControl                            = 0x0050
commandB1[operationalStrategyControl]                 = [operationalStrategyControl]
FACE                                                  = 0xFACE
F001                                                  = 0xF001
F004                                                  = 0xF004
F010                                                  = 0xF010
#############################################################################################################
# Service 0xB1 diagnosticCommand function 
#############################################################################################################
def diagnosticCommand(_DiagSig_Rx, command):
    command = can.Message(arbitration_id = _DiagSig_Rx,
                          data           = [0x00, 0xB1, commandB1, 0, 0, 0, 0, 0], is_extended_id = False)
    try:
        MidSpeedCan.send(command)
        responseParser(_DiagSig_Rx)
        
    except can.CanError:
        print("Message NOT sent")
#############################################################################################################
inputIntegrityTestStateEntry                          = 0xB2
ServiceRequest[inputIntegrityTestStateEntry]          = ["inputIntegrityTestStateEntry", "0xB2"]
#############################################################################################################
# gds v2003 spec
requestManufacturerStateEntry                         = 0xB4
ServiceRequest[requestManufacturerStateEntry]         = ["requestManufacturerStateEntry", "0xB4"]
#############################################################################################################
# Firmware
#############################################################################################################
Firmware                                                = dict()
FDIM                                                    = '8R29-14D017-AC.phf'
Firmware[FDIM]                                          = ['8R29-14D017-AC.phf']
#############################################################################################################
#  
#############################################################################################################
'''“Sadly, those documents only confirm this won't work on an FG(I).
On all these devices, you request the diags mode you want with "0x10 mode" and if you enter the programming 
mode, the screen and/or LEDs turn off because, as I can see in the FG2 Primary Boot Loader firmware, it stops 
calling the entry-routine in the extended-firmware that you are about to update.
The FG(I) Clusters I have (a 2008 G6E, and a late 2010 FPV supercharged - which has an updated 2010 part 
number) only support 0x10 modes of: 0x81 and 0x87 - and those documents say 0x81 is normal-mode and 0x87 is
the superset diags-mode.  To go into programming mode it needs to accept 0x85 (or 0x02 on the FG2 where they
went more standard). You can ask Jakka to send some can bus signals to his Cluster:
              [0x02, 0x10, 0x81], [0x02, 0x10, 0x85], [0x02, 0x10, 0x87]
But only the first and last will be accepted, and his cluster will not "turn off" the screen and/or LEDs -
so it is still running the firmware without worrying that it's about to be updated. I've tried all the other 
numbers too, only 0x81 and 0x87 work. Sad but true - you can't update the firmware in an FG(I) Cluster.
Regards, JasonACT.”'''
#############################################################################################################
# enter into a systemSupplierSpecific diagnostic state [VDO METHOD 0x10FA] 
# FG1IPCComms
#############################################################################################################
vdoManufacturerStateEntry                             = 0xBA
ServiceRequest[vdoManufacturerStateEntry]             = ["VDO", "IPC Programming Mode"]
vdoGodModeKey  = { 0xbf, 0xa4, 0x90, 0x56, 0xcd }         
#############################################################################################################
# enter into a systemSupplierSpecific state function: 
# usage:
#      'vdoGodModeKey()'
# triggers:
#       hidden seed & key exchange, opens diag sessiob 0x10FAm starts testerPresent task
#############################################################################################################
def enterManufacturerState():
    global seed
    readCommonId   = can.Message(
                          arbitration_id = 0x720, 
                          data           = [0x03, readMemoryByCommonID, 0xE2, 0x00, 0xDD, 0x00, 0x00, 0x00], is_extended_id = False)
    ba0b           = can.Message(
                          arbitration_id = 0x720, 
                          data           = [0x02, vdoManufacturerStateEntry, 0x0B, 0x00, 0xDD, 0x00, 0x00, 0x00], is_extended_id = False)
    ba07           = can.Message(
                          arbitration_id = 0x720, 
                          data           = [0x02, vdoManufacturerStateEntry, 0x07, 0x00, 0xDD, 0x00, 0x00, 0x00], is_extended_id = False)
    try:
        message    = MidSpeedCan.recv()
        MidSpeedCan.send(readCommonId)
        if messsage.arbitration_id == 0x728 and message.data[1] == 0x62:
            print(message)
            time.sleep(0.25)
        else:
            pass
        MidSpeedCan.send(ba0b)
        if messsage.arbitration_id == 0x728 and message.data[1] == 0x7F:
            print(message)
            time.sleep(0.025)
        MidSpeedCan.Send(ba07)
        if messsage.arbitration_id == 0x728 and message.data[0] == 0xFA:
            print(message)
            seed    = message.data[1], message.data[2], message.data[3]
            seed[0] = message.data[1]
            seed[1] = message.data[2]
            seed[2] = message.data[3]
            return seed

    except can.CanError():
        print("CAN Error")            
#############################################################################################################
# function that generates the key
#############################################################################################################
def supplierKeyGen(seed):
    fixed  = 0xBFA49056CD
    try: 
        challengeCode = array('Q')
        challengeCode.append(fixed & 0xff)
        challengeCode.append((fixed >> 8) & 0xff)
        challengeCode.append((fixed >> 16) & 0xff)
        challengeCode.append((fixed >> 24) & 0xff)
        challengeCode.append((fixed >> 32) & 0xff)
        challengeCode.append(seed[2])
        challengeCode.append(seed[1])
        challengeCode.append(seed[0])
        temp1 = 0xC541A9
        for i in range(64):
            abit = temp1 & 0x01
            chbit = challengeCode[7] & 0x01
            bbit = abit ^ chbit
            temp2 = (temp1 >> 1) + bbit * 0x800000 & -1
            temp1 = (temp2 ^ 0x109028 * bbit) & -1
            challengeCode[7] = challengeCode[7] >> 1 & 0xff
            for a in range(7, 0, -1):
                 challengeCode[a] = challengeCode[a] + (challengeCode[a - 1] & 1) * 128 & 0xff
                 challengeCode[a - 1] = challengeCode[a - 1] >> 1
        key = [ temp1 >> 4 & 0xff, ((temp1 >> 12 & 0x0f) << 4) + (temp1 >> 20 & 0x0f), (temp1 >> 16 & 0x0f) + ((temp1 & 0x0f) << 4) ]
        print("Succesfully got key: {key}")
        return key
    except can.CanError():
        print("CAN Error")            
#############################################################################################################
# function to send key & open session
#############################################################################################################
def systemSupplierSpecificSendKey(key):
    keyResponse   = can.Message(
                          arbitration_id = 0x720, 
                          data           = [0x04, vdoManufacturerStateEntry, key[0], key[1], key[2], 0x00, 0x00, 0x00], is_extended_id = False)
    fa            = can.Message(
                          arbitration_id = 0x720, 
                          data           = [0x02, 0x10, 0xFA, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id = False)
    try:
        message    = MidSpeedCan.recv()
        MidSpeedCan.send(keyResponse)
        MidSpeedCan.send(fa)
        if messsage.arbitration_id == 0x728 and message.data[1] == 0x50 and message.data[2] == 0xFA:
            print(message)
            time.sleep(0.25)
            print("systemSupplierSpecific diagnostic session opened")
            return
        else:
            pass
    except can.CanError():
        print("CAN Error")            
#############################################################################################################
# main collector function; see usage note above
#############################################################################################################
def vdoGodModeKey():
    global seed, key
    enterManufacturerState()
    supplierKeyGen(seed)
    systemSupplierSpecificSendKey(key)
    testerPresent(0x720, suppressResponse)
#############################################################################################################
# ipc factory programming mode; 3 can messages and you have the firmware, no security at all
#############################################################################################################
'''Specs: MS bus, 125000 BAUD, send on 0x720, receive on 0x728 (all totally standard).
Send: B2 AA BB CC DD EE 11 22 repeatedly until you get back a 4 byte short packet: 05 50 00 00
You are now in programing mode'''
# JasonACT
#############################################################################################################
def enterProgrammingMode():
    openSesame = can.Message(
                             arbitration_id = 0x720, 
                             data           = [0xB2, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0x11, 0x22], is_extended_id = False)
    try:
        print("Message Buffer Stacrted on {MidSpeedCan.channel_info}")
        task = MidSpeedCan.send_periodic(openSesame, 0.20)
        print("Attempting to Enter VDO IPC Programming Mode...")
        time.sleep(1)
        print("Power Cycling...")
        ecuReset(0x720, 0x01)
        time.sleep(0.0002)
        print("Attempting to bypass bootloader...")
        assert isinstance(task, can.CyclicSendTaskABC)
        time.sleep(0.0002)
        print("Power Cycling...")
        ecuReset(0x720, 0x01)
        MidSpeedMessage = MidSpeedCan.recv()
        if MidSpeedMessage.arbitration_id == 0x728 and MidSpeedMessage.dlc == 4:
            task.stop()
            print("IPC Programming Mode Active - Use Caution.")
            return
        else:
            pass        
    except can.CanError:
        print("Message NOT sent")
#############################################################################################################
'''Send: B3... to read I.E. address 0x000003FC, 8 bytes => B3 FC 3F 00 00 01 00 00 (min)
Send: B3... to read I.E. address 0x000003FC, 16 bytes => B3 FC 3F 00 00 02 00 00
Send: B3... to read I.E. address 0x000003FC, 17 bytes => B3 FC 3F 00 00 03 00 00
Send: B3... to read I.E. address 0x000003FC, 0x3C004 bytes => B3 FC 3F 00 00 01 78 00 (the entire firmware)
jakka351 notes its easier to start sending B2AABBCCDDEE1122 and then send 021101 to cause a reset, then the
first thing that the cluster gets on boot is instruction to go to programming mode
That produces 0x3C00A bytes returned... The last 2 (always in a short 2 byte packet) seem to be a checksum..
So there's 3C008 left, but we know you can only make requests in multiples of 8. I.E. 01 78 00 means
0x007801 * 8 so the format is B3 AA AA AA AA LL LL LL (AAAAAAAA=Address, LLLLLL=Length/8 rounded up)'''
# cansend can0 720#B2AABBCCDDEE1122
# cansend can0 720#B3FC3F0000017800
#############################################################################################################
# download firmware dump
#############################################################################################################
def downloadFirmware():
    # firmware_file      = 
    download           = can.Message(
        arbitration_id = 0x720, 
        data           = [0xB3, 0xFC, 0x3F, 0x00, 0x00, 0x01, 0x78, 0x00], is_extended_id = False
        )
    try:
        MidSpeedCan.send(download)
        print(f"Message sent on {MidSpeedCan.channel_info}")
        return
    except can.CanError:
        print("Message NOT sent")

#############################################################################################################
'''Send: AA 5A 5A 5A 5A 5A 5A 5A to leave the mode, once you are done. “There are ACK CAN packets that the
Cluster will send back for most things, and I don't know what they are, but then again if the process went 
smoothly (no noise on the wires) then not checking for them probably wouldn't affect much, other than knowing
when to continue.  These units will stay in the pgm mode indefinitely without any activity on the CANBUS -
and I don't see any issues with getting back into that mode if the Cluster firmware part was erased (not the
bootloader obviously). Information on the chip that might be of use: 256KB Flash, starts at 0x00000000 goes 
to 0x0003FFFF, bootloader is at 0x00000000-0x00003FFB according to the file, firmware starts at 0x00003FFC,
but the erase blocks command in the file is actually set for 64 blocks @ 0x00004000 (one block is 0x1000 
[4KB] bytes long).  That actually puts the erase 16KB past the end of flash memory - I guess they didn't
care since it doesn't exist, and if they wanted to start at 0, it would still erase all the flash with that length.”
Talking Re: FORD technical service bulletin : ICC touch screen display'''
# JasonACT
#############################################################################################################
def leaveProgrammingMode():
    closeSesame        = can.Message(
        arbitration_id = 0x720, 
        data           = [0xAA, 0x5A, 0x5A, 0x5A, 0x5A, 0x5A, 0x5A, 0x5A], is_extended_id = False
        )
    try:
        MidSpeedCan.send(closeSesame)
        print(f"Message sent on {MidSpeedCan.channel_info}")
        return
    except can.CanError:
        print("Message NOT sent")

#############################################################################################################
'''Jack Whiteford
“FG(I) Read and Write the entire EEPROM:
### < send to Cluster
### > Cluster responds
03 22 E2 00 < Request data by ID
06 62 E2 00 17 0B 6C > Data is 170B6C - might be checking model?
02 BA 0B < Quickly jam in these two..
02 BA 07 < ..requests that "fail" (you will get en error)
FA 11 88 57 > 3 byte challenge key appears out of nowhere
(If it doesn't appear, try again from BA0B)
04 BA 8E 5C 8D < Respond with 3 byte key generated with { 0xbf, 0xa4, 0x90, 0x56, 0xcd }
02 10 FA < Don't wait, just do
02 50 FA > Success!
BA 01 02 00 00 < Read 2 bytes at EEPROM address 0x0000
FA 01 02 15 A1 > !!! 0xA1 is byte 0, 0x15 is byte 1 in the EEPROM.
BA 02 02 00 00 16 A1 < !!! Write 2 bytes at address 0x0000
!!! 16 was 15 increased by 1 as a test
FA 02 02 > Happy days
(FYI)
BA 01 02 00 02 < Read 2 bytes at address 0x0002, next two bytes
...and on it goes...
BA 01 02 01 FE < Read 2 bytes at address 0x01FE the last EEPROM address
(I say last, but I also assume the 02 means two byte read/write)
(You probably/might be able to read and write 1 byte at a time)
02 10 81 < Request to leave secure mode
02 50 81 > Left secure mode
Please forward onto Jakka - I expect him to come up with a neat script to do all the things I did for the FGII”
#   JasonACT'''
#############################################################################################################
# read write the eeprom
#############################################################################################################        
'''def eeprom():
    ipcResponse            = MidSpeedCan.recv()    
    eepromLocations = can.Message(arbitration_id = 0x720, 
                                  data           = [0x05, 0xBA, 0x01, 0x20, i, 0x00, 0x00], extended_id=False)
    while True:
        for i in range:(0x00, 0x1FF0, [0x20])
            eepromLocations.data[4,5] = i
            MidSpeedCan.send(eepromLocations)
            return i
    
    if ipcResponse.arbitration_id == 0x728 and ipcResponse.data[2,3,4] == 0xFA0102:               
        for h in range(ipcResponse.data[4], ipcResponse.data[5]):   
            h                  = ipcResponse.data[4,5]
            EEPROM             = [h]
            return h                 
    
    return EEPROM
   '''
#############################################################################################################
'''     BA 01 02 00 00 < Read 2 bytes at EEPROM address 0x0000
        FA 01 02 15 A1 > !!! 0xA1 is byte 0, 0x15 is byte 1 in the EEPROM.
        BA 02 02 00 00 16 A1 < !!! Write 2 bytes at address 0x0000
        !!! 16 was 15 increased by 1 as a test
        FA 02 02 > Happy days
        (FYI)
        BA 01 02 00 02 < Read 2 bytes at address 0x0002, next two bytes
        ...and on it goes...
        BA 01 02 01 FE < Read 2 bytes at address 0x01FE the last EEPROM address
                        (I say last, but I also assume the 02 means two byte read/write)
                        (You probably/might be able to read and write 1 byte at a time)
        

        def writeEeprom():
            pass
    
        def flash():
            if message.arbitration_id == SOC_SOH_ID:
                state_of_charge = int.from_bytes(message.data[0:2], 'little')
                state_of_health = int.from_bytes(message.data[2:4], 'little')
                state_of_charge_hi_res = 0.01 * int.from_bytes(message.data[4:6], 'little')
                soc_soh_updated = True

            if message.arbitration_id == RATED_CAPACITY:
                rated_capacity = int.from_bytes(message.data[0:2], 'little')
            if rated_capacity > 250:
                rated_capacity += 1
                rated_capacity_updated = True'''


#############################################################################################################
# [NRC] NEGATIVE RESPONSE CODE DEFINITIONS - 0x7F
#############################################################################################################
NegativeResponseCode                                  = dict()
#############################################################################################################
generalReject                                         = 0x10
NegativeResponseCode[generalReject]                   = [generalReject, "GR", "General Reject"]
serviceNotSupported                                   = 0x11
NegativeResponseCode[serviceNotSupported]             = [serviceNotSupported, "SNS", "Service Not Supported"]
subFunctionNotSupported                               = 0x12
NegativeResponseCode[subFunctionNotSupported]         = [subFunctionNotSupported, "SFNS", "Subfunction Not Supported: Service exists but not supported by subfunction"]
responseTooLong                                       = 0x14
NegativeResponseCode[responseTooLong]                 = [responseTooLong, "RTL", "Response Too Long"]
busyRepeatRequest                                     = 0x21
NegativeResponseCode[busyRepeatRequest]               = [busyRepeatRequest, "BRR", "Busy Repeat Request"]
conditionsNotCorrect                                  = 0x22
NegativeResponseCode[conditionsNotCorrect]            = [conditionsNotCorrect, "CNC", "Conditions Not Correct"]
requestSequenceError                                  = 0x24
NegativeResponseCode[requestSequenceError]            = [requestSequenceError, "RSE", "Request Sequence Error: Server expectes different sequence of request messages"]
requestOutOfRange                                     = 0x31
NegativeResponseCode[requestOutOfRange]               = [requestOutOfRange, "ROOR", "Request of out Range: There exists a parameter which is out of range"]
securityAccessDenied                                  = 0x33
NegativeResponseCode[securityAccessDenied]            = [securityAccessDenied, "SAD", "Security Access Denied: Either 1) Test conditions not met 2) invalid sequence (try DiagSession) 3) requires unlocking of server"]
invalidKey                                            = 0x35
NegativeResponseCode[invalidKey]                      = [invalidKey, "IK", "Invalid Key"]
exceedNumberOfAttempts                                = 0x36
NegativeResponseCode[exceedNumberOfAttempts]          = [exceedNumberOfAttempts, "ENOA", "Exceeded Number of Security Access Attempts"]
requiredTimeDelayNotExpired                           = 0x37
NegativeResponseCode[requiredTimeDelayNotExpired]     = [requiredTimeDelayNotExpired, "RTDNE", "Required Time Delay Not Expired: Client attempting to access security too quickly"]
uploadDownloadNotAccepted                             = 0x70
NegativeResponseCode[uploadDownloadNotAccepted]       = [uploadDownloadNotAccepted, "UDNA", "Upload / Download Not Accepted"]
generalProgrammingFailure                             = 0x72
NegativeResponseCode[generalProgrammingFailure]       = [generalProgrammingFailure, "GPF", "General Programming Failure"]
requestCorrectlyReceived_ResponsePending              = 0x78
NegativeResponseCode[requestCorrectlyReceived_ResponsePending] = [requestCorrectlyReceived_ResponsePending, "RCRRP", "Request Correctly Received Response Pending: Wait for response"]
subFuncionNotSupportedInActiveSession                 = 0x7E
NegativeResponseCode[subFuncionNotSupportedInActiveSession]    = [subFuncionNotSupportedInActiveSession, "SFNSIAS", "Subfunction Not Supported in Active Session"]
serviceNotSupportedInActiveSession                    = 0x7F
NegativeResponseCode[serviceNotSupportedInActiveSession]       = [serviceNotSupportedInActiveSession, "SNSIAS", "Service Not Supported"]
rpmTooHigh                                            = 0x81
NegativeResponseCode[rpmTooHigh]                      = [rpmTooHigh, "Engine RPM too high"]
rpmTooLow                                             = 0x82
NegativeResponseCode[rpmTooLow]                       = [rpmTooLow, "Emgine RPM too low"]
engineIsRunning                                       = 0x83
NegativeResponseCode[engineIsRunning]                 = [engineIsRunning, "Engine is Running"]
engineIsNotRunning                                    = 0x84
NegativeResponseCode[engineIsNotRunning]              = [engineIsNotRunning, "Engine is off"]
shifterLeverNotInPark                                 = 0x90
NegativeResponseCode[shifterLeverNotInPark]           = [shifterLeverNotInPark, "Shifter is not in park"]
#############################################################################################################
# Intro GFX // terminal
#############################################################################################################
def intro():
    print("""
#################################################################################################################
   __    ___________    ____  /\     ___________             _________                                   __   
  / /    \_   _____/___/_   | \ \    \_   _____/ ____  __ __ \_   ___ \  ____   _____   _____   ______   \ \  
 / /      |    __)/ ___\|   |  \ \    |    __)__/ ___\|  |  \/    \  \/ /  _ \ /     \ /     \ /  ___/    \ \ 
 \ \      |     \/ /_/  >   |   \ \   |        \  \___|  |  /\     \___(  <_> )  Y Y  \  Y Y  \\___ \     / / 
  \_\     \___  /\___  /|___|    \ \ /_______  /\___  >____/  \______  /\____/|__|_|  /__|_|  /____  >   /_/  
              \//_____/           \/         \/     \/               \/             \/      \/     \/         
    Falcon Diagnostic Utility - FG1ECUComms
#################################################################################################################
            """)
    print("                            ")
    print("                            ")
#############################################################################################################
# Main Menu // terminal
#############################################################################################################
def menu():
    menu_options = {
        1:  '  [ run Diagnostic Message Parser            ',
        2:  '  [ start Diagnostc Session Service 0x10     ',
        3:  '  [ ecuReset Service 0x11                    ',
        4:  '  [ unlock Security Access Service 0x27      ', 
        5:  '  [ read + clear dtc Services 0x14 0x18       ',
        6:  '  [ read data identifiers Service 0x22        ',
        7:  '  [ controlDTCSetting Service 0x85            ',
        8:  '  [                                           ',
        9:  '  [ Unlock Manufacturer State Entry Service 0xBA          ',
        10: ' [ cansniffer         ',
        11: ' [ IPC EEPROM Download + Edit       ',
        12: ' [ Read and Clear Diagnostic Trouble Codes  ', 
        13: ' [  Exit                                    '
    }

    def print_menu():
        for key in menu_options.keys():
            print ('     ', key, '-', menu_options[key], '                                                                                              ]' )

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input(' Select Option: '))
        except:
            print('   Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            cleanscreen()
            Parser()
        elif option == 2: 
            cleanscreen()
            startDiagnosticSessionMenu()  
            cleanscreen()
            menu()
        elif option == 3:
            cleanscreen()
            ecuReset()
            cleanscreen()
            menu()
        elif option == 4:
            cleanscreen()
            SendKey(key)
        elif option == 5:
            cleanscreen()
            menu()
        elif option == 6:
            cleanscreen()
            menu()
        elif option == 7:
            cleanscreen()
            menu()
        elif option == 8:
            cleanscreen()
            menu()
        elif option == 9:
            cleanscreen()
            menu()
        elif option == 10:
            print("ctrl + c to go back")
            time.sleep(3)
            os.system("cansniffer vcan0 -c &")
        elif option == 11:
            cleanscreen()
            selfTest()
            cleanscreen()
            menu()
        elif option == 12:
            cleanscreen()
            menu()
        elif option == 13:
            cleanscreen()
            intro()
            print("Quitting...")
            exit()
        else:
            
            print('Invalid option. Try again fuckface.')
'''
    msg = can.Message(arbitration_id=0xc0f,data=[0, 25, 0, 0, 0, 0, 0, 0],is_extended_id=False)
    try:
        task = MidSpeedCan.send_periodic(msg,0.2)
        print("Message sent on {}".format(MidSpeedCan.channel_info))
    except can.CanError:
        print("Message NOT sent")
    
'''
#############################################################################################################
#  Clean up functions // terminal
#############################################################################################################

def cleanline():                      # cleans the last output line from the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def cleanscreen():                    # cleans the whole console screen
    os.system("clear")
    intro()

def ccp():
    cleanline()
    cleanline()
    cleanline()
    cleanline()
    cleanline()

#################################################################################################################
# Topbar menu
#################################################################################################################
menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', [['Special', 'Normal',['Normal1', 'Normal2'] ], 'Undo'], ],
                ['&Data', [['DBC Files', 'CAN Tables',['MidSpeedCan', 'HighSpeedCan'] ], 'Undo'], ],
                ['Module', ['Audio Control', 'Audio Interface', 'Body Electronic', 'Bluetooth Phone', 'Front Display Interface', 'Instrument Cluster', 'Parking Aid']],
                ['Tools', ['---', 'Download Firmware ::Command_Key', 'Edit Firmware', '---', 'Message Parser', 'Emulator']],
                ['Workshop Manuals', ['---', 'Download IPC Firmware ::Command_Key', 'Download FDIM Firmware', '---', 'Command &3', 'Command &4']],
                ['Wiring Diagams', ['---', 'Download IPC Firmware ::Command_Key', 'Download FDIM Firmware', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&About...']], ]
#################################################################################################################
# Top Banner
#################################################################################################################
top_banner = [[sg.Text('FG1ECUComms', font='Arial 25', enable_events=False, grab=False), sg.Push()]]
#################################################################################################################
# mid Banner
#################################################################################################################
mid_banner = [[sg.Text('Ford Diagnostic Utility', font='Arial 10', enable_events=False, grab=False), sg.Push()]]
#################################################################################################################
# Bottom Banner
#################################################################################################################
bottom_banner = [
                [sg.Text('By Jakka351 using PySimpleGUI & Python-CAN [ https://github.com/jakka351/FG-Falcon ]', font='Arial 8', enable_events=False, grab=False), sg.Push()]
                ]
               
#################################################################################################################
# Frontpage tab
#################################################################################################################
tab_Frontpage             = [[sg.Text('FG1ECUComms Diagnostic Utility.')]] 
#################################################################################################################
# Frontpage tab Test
##########################################(#######################################################################
tab_Frontpage_Test        = [[sg.Text('FG1ECUComms Diagnostic Utility.')]] 
#################################################################################################################
# Modules Tab
menu_modules =  ['Module', ['Audio Control', 'Audio Interface', 'Body Electronic', 'Bluetooth Phone', 'Front Display Interface', 'Instrument Cluster', 'Parking Aid']],


#################################################################################################################
# Sub-tab startdiagnosticsession
#################################################################################################################
tab_SID =  [[sg.Text('Diagnostic Services:')],
            [sg.Text('Request ECU Reset Service', size=(15,1))],
            [sg.Drop(values=('ecuReset - softReset 0x1102', 'ecuReset - hardReset 0x1101' ), size=(25, 1)), sg.Button('Send Service Request to ECU', size=(30, 1))],
            [sg.Drop(values=('ecuReset - softReset 0x1102', 'ecuReset - hardReset 0x1101' ), size=(25, 1)), sg.Button('Send Service Request to ECU', size=(30, 1))],
            [sg.Drop(values=('ecuReset - softReset 0x1102', 'ecuReset - hardReset 0x1101' ), size=(25, 1)), sg.Button('Send Service Request to ECU', size=(30, 1))],
            [sg.Drop(values=('ecuReset - softReset 0x1102', 'ecuReset - hardReset 0x1101' ), size=(25, 1)), sg.Button('Send Service Request to ECU', size=(30, 1))]]
           
                              
                  
#################################################################################################################
#
#################################################################################################################
tab_ecuReset               = [[sg.Text('Service 0x11ecuReset')], 
                              [sg.Button('    softReset 0x01')],
                              [sg.Button('    hardReset 0x02')]]
#################################################################################################################
#
#################################################################################################################
tab_securityAccess         =[[sg.Text('Service 0x27 securityAccess')],
                             [sg.Text('Tabs can be anywhere now!')]]
#################################################################################################################
#
#################################################################################################################
tab_readData               =[[sg.Text('This is inside tab 2')],
                             [sg.Text('Tabs can be anywhere now!')]]
#################################################################################################################
#
#################################################################################################################
tab_controlDtc             =[[sg.Text('This is inside tab 2')],
                             [sg.Text('This is inside tab 2')],
                             [sg.Text('This is inside tab 2')],
                             [sg.Text('This is inside tab 2')],
                             [sg.Text('This is inside tab 2')],
                             [sg.Text('This is inside tab 2')],
                             [sg.Text('This is inside tab 2')],
                             [sg.Text('Tabs can be anywhere now!')]]
#################################################################################################################
#
#################################################################################################################    
tab_diagnosticCommand      = [[sg.Text('This is inside tab 2')],
                              [sg.Text('Tabs can be anywhere now!')]]
#################################################################################################################
#
#################################################################################################################
tab_socketcan              = [[sg.Text('This is inside tab 2')],
                              [sg.Text('Tabs can be anywhere now!')]]
#################################################################################################################
#
#################################################################################################################
tab_ELM327                 = [[sg.Text('ELM327 Connection')],
                              [sg.Button('Connect', key='ELM327_CONNECT_BUTTON'),
                               sg.Button('Scan', key='ELM327_SCAN_BUTTON')],
                              [sg.Output(size=(100, 3), font='Courier 10')]]
#################################################################################################################
#
#################################################################################################################
tab_J2534                  = [[sg.Text('SAE-J2534 Interfaces')],
                             [sg.Text('Push button to get devices')],
                             [sg.Button('Get J534 Device List', key='getDevices')],
                             [sg.Output(size=(100, 3), font='Courier 10')]]
#################################################################################################################
#
#################################################################################################################
tab_connection             = [[sg.Frame('Connection',
                                [[sg.TabGroup([
                                  [sg.Tab('J2534', tab_J2534), 
                                   sg.Tab('ELM327', tab_ELM327), 
                                   sg.Tab('socketcan', tab_socketcan)],
                                ])],], 
                                )]]
#################################################################################################################
#
#################################################################################################################
tab_Services               = [[sg.Frame('', 
                                [[sg.TabGroup([
                                  [sg.Tab('  SID ',  tab_SID), 
                                   sg.Tab('  DID ', tab_ecuReset), 
                                   sg.Tab('  DTC ', tab_securityAccess)],
                                  [sg.Tab('MODCONFIG', tab_readData), 
                                   sg.Tab('FIRMWARE', tab_controlDtc), 
                                   sg.Tab('OTHER', tab_diagnosticCommand)],
                                ])],], 
                                )]]
#################################################################################################################
#
########################################

tab_Test1                  = [[sg.Text('Bus: ', size=(15, 1)), sg.Drop(values=('MidSpeedCan', 'HighSpeedCan'), size=(25, 1))]]
tab_Test                   = [[sg.Text('Module: ', size=(15, 1)), sg.Drop(values=('Audio Control', 'Audio Interface', 'Body Electronic', 'Bluetooth Phone', 'Front Display Interface', 'Instrument Cluster', "Parking Aid" ), size=(25, 1))]]
tab_Test2                  = [[sg.Text('Session Type: ', size=(15, 1)), sg.Drop(values=('standardDiagnosticSession', 'ecuProgrammingSession', 'ecuAdjustmentSession', 'vehicleManufacturerSpecific', 'systemSupplierSpecific'), size=(25, 1))]]
tab_Test3                  = [[sg.Text('Tester Present: ', size=(15, 1)), sg.Drop(values=('Request Response', 'Suppress Response' ), size=(25, 1))]]
tab_Test4                  = [[sg.Text('Security Access: ', size=(15, 1)), sg.Drop(values=('2701', '2703', '2705', '2711', '10FA'), size=(25, 1))]]
tab_Test5                  = [[sg.Text('J2534  Device Selection: ', size=(20, 1)), sg.Drop(values=('2701', '2703', '2705', '2711', '10FA'), size=(25, 1))], [sg.Button('Connect J2534  Interface', size=(50,1))]]
tab_Test6                  = [[sg.Text('ELM327 Device Selection: ', size=(25, 1)), sg.Drop(values=('2701', '2703', '2705', '2711', '10FA'), size=(25, 1))], [sg.Button('Connect ELM327 Interface', size=(50,1))]]
tab_Test7                  = [[sg.Button('start diagnostic session', size=(50,1))]]

layout                     = [[sg.Menu(menu_def, tearoff=False, key='-MENU BAR-')],     # This is how a Menu is normally defined                  
                              [sg.Frame('', top_banner, pad=(5,5),  expand_x=True, border_width=2, grab=True)],
                              [sg.Frame('', mid_banner, pad=(5,5),  expand_x=True, border_width=2, grab=True)],
                              [sg.Frame('Interface Setup', layout=(
                              [sg.Frame('', tab_Test5, pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                              [sg.Text('    ')],    
                              [sg.Text('Module Diagnostic')],    
                              [sg.Frame('', tab_Test1,   pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                              [sg.Frame('', tab_Test,   pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                              [sg.Frame('', tab_Test2,  pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                              [sg.Frame('', tab_Test3,  pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                              [sg.Frame('', tab_Test4,  pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                              [sg.Text(' CAN ID Rx:',  pad=(2,2), size=(10, 1)), sg.Input(default_text='0x720', size=(15, 1))], 
                              [sg.Text(' CAN ID Tx:',  pad=(2,2), size=(10, 1)), sg.Input(default_text='0x728', size=(15, 1)), ],
                              [sg.Frame('', tab_Test7,  pad=(2,2),  expand_x=True, border_width=2, grab=True)],
                                
                         ), size=(315, 385), pad=(5,5),  expand_x=False, border_width=2, grab=True),
                               sg.Frame("", frame_layout, size=(800,385), pad=(5,5),  expand_x=True, border_width=2, grab=True), sg.Slider(**option, key='V_Scrollbar'),],
                              [sg.StatusBar("", size=(800, 1), key="Status")],
                              [sg.Frame('', bottom_banner, pad=(5,5),  expand_x=True, border_width=2, grab=True)]]
                              
                                 
                             

#################################################################################################################
#
#################################################################################################################


#splash()
cleanscreen()
time.sleep(1)
menu()

