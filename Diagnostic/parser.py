#usr/bin/python3
'''Diagnostic communication for all of the Ford supported protocols are defined to use a master/slave 
configuration. Interrogating devices (testers) that communicate with an ECU using a diagnostic protocol 
will be considered the master on the network. As the master, the tester initiates all diagnostic 
communication on the link and each ECU is considered the slave that responds to the tester. An ECU 
shall never initiate diagnostic dialog between itself and a tester'''
# CAN Generic Diagnostic Specification v2003
# https://github.com/jakka351/6FPA-util
# CAN Generic Diagnostic Specification v2003
# https://github.com/jakka351/6FPA-util
'''
 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         6FPAAAJGSW          FGI Diagnostic Parser'''
import can
import time
import os
import queue
import sys, traceback
from threading import Thread
from array import array
from lib.BUS import Bus, MidSpeedCan
from lib.ECU import DiagSig_Tx, DiagSig_Rx
from lib.SID import ServiceRequest
from lib.NRC import NegativeResponseCode
from lib.PID import CommonID
from lib.DTC import DiagnosticTroubleCode
from lib.ARB import FullBus
def intro():
    print('''              
 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         6FPAAAJGSW          FGI Diagnostic Message Parser             
                         ''')
    print("                            ")
    print("                            ")
    print("                            ")
    print("                            ")
    print("                            ")
    print("                            ")
    print("                            ")
    print("                            ")
    print("                            ")
    time.sleep(2)

    #light up IPC on start up
    OpenSessionMsg  = can.Message(arbitration_id=0x720, data=[0x02, 0x10, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)     
    IpcLightsOnMsg  = can.Message(arbitration_id=0x720, data=[0x06, 0x2F, 0x71, 0x30, 0x07, 0x80, 0x00, 0x00], extended_id=False)
    IpcLightsOffMsg = can.Message(arbitration_id=0x720, data=[0x06, 0x2F, 0x71, 0x30, 0x07, 0x00, 0x00, 0x00], extended_id=False)
    MidSpeedCan.send(OpenSessionMsg)
    MidSpeedCan.send(OpenSessionMsg)
    MidSpeedCan.send(IpcLightsOnMsg)
    MidSpeedCan.send(IpcLightsOnMsg)
    




def cleanline():                      # cleans the last output line from the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def cleanscreen():                    # cleans the whole console screen
    os.system("clear")

def ccp():
    cleanline()
    cleanline()
    cleanline()
    cleanline()

def Sender():
    input = ("Enter CAN id:")
    input = arbitration_id
            
            
def FullBus():
    from lib.ARB import AudioControlModule, AudioInterFaceModule, BluetoothPhoneModule, BodyElectronicModule, InstrumentCluster, FrontDisplayInterfaceModule, HvacIntegratedModule, ParkingAidModule
    try:
        while True:
            message = MidSpeedCan.recv()
            if message is not None:
                if message in AudioControlModule:     
                    try:
                        print("Volume:", AudioCurrentVolume)

                    except KeyError:
                        pass

                else:
                    pass
                    
    except KeyboardInterrupt:
        sys.exit(0)  
    except can.CanError:
        print("can error")                   
    except Exception:
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
        pass
    except OSError:
        sys.exit()

def Parser():
    try:
        while True:
            message = MidSpeedCan.recv()
            if message is not None:
                if message.arbitration_id in DiagSig_Rx:
                    try:
                        if message.data[1] in ServiceRequest:
                            ccp()
                            print(" //-------->> Rx ECU:")
                            print("\r", DiagSig_Rx[message.arbitration_id], "Service Request ID: ", ServiceRequest[message.data[1]], "[From Tester]")
                            print("\r", message)
                            print("\r", "   ")
                            
                        else:
                            pass  

                    except KeyError:
                        pass

                elif message.arbitration_id in DiagSig_Tx:     
                    try:
                        if (message.data[1] - 0x40) in ServiceRequest:
                            ccp()
                            print("\r", " //--------<< Tx ECU:")
                            print("\r", message)
                            print("\r", "Tx ECU: ", DiagSig_Tx[message.arbitration_id], "Positive Response:  ", ServiceRequest[message.data[1] - 0x40])
                            print("\r", "  ")
                            
                        elif message.data[1] == 0x7F and message.data[3] in NegativeResponseCode:
                            ccp()
                            print("\r", "  ")
                            print("\r", message)
                            print("\r", "             0x7F Negative Response: ", NegativeResponseCode[message.data[3]])
                            print("\r", "------//                          6FPA-util  ---//")
                            
                        else:
                            pass
                            
                    except KeyError:
                        pass

                else:
                    pass
                    
    except KeyboardInterrupt:
        sys.exit(0)  
    except can.CanError:
        print("can error")                   
    except Exception:
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
        pass
    except OSError:
        sys.exit()

if __name__ == "__main__":
    intro()
    Parser()
    FullBus()