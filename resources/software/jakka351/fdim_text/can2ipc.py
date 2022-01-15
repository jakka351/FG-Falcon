#!/usr/bin/python3
# can0swc fg falcon swc-can adapter
# diagnostics from steering wheel controls while audio off
############################
# Import modules
############################
import can
import time
import os
import sys
import queue
from threading import Thread
c                      = ''
count                  = 0  
# CAN Id's
SWC                    = 0x2F2 
#SWM                    = 0x2EC
#ICC                    = 0x2FC 
# SWC Button CAN Data
SteeringWheelControlSeek               = (0x08, 0x09, 0x0C, 0x0D)  # seek button on bit [7] of id 0x2f2
SWC_VOLUP              = (0x10, 0x11, 0x14, 0x15)  # volume + button on bit [7] of id 0x2f2
SWC_VOLDOWN            = (0x18, 0x19, 0x1C, 0x1D)  # volume - button on bit [7] of id 0x2f2
SWC_PHONE              = (0x68)  # phone button on bit [6] of id 0x2f2
#SWC_MODE               = (0x10)
AudioControlModuleOff  = (0x48, 0xC8)
def scroll():
    #prints logo to console
        print('  ')
        print('''  
             ,777I77II??~++++=~::,,,,::::::::::~~~==+~                                        
           ,IIIIII,IIII+~R,:A, S,,P:~O:,T..I.,F,,Y:::~+?+?=                                    
         :=I7777I=IIIIII~...:===,:,=~:,,,,,,::=,,,:::~~:=?===                                 
      ~=,?I?777II7IIIII=~,.,,,,,,,,,,,:,,,,,,::,,,,~:~~~~:~+:~:~                              
      I=I?IIIIII~IIIIIII+:..,,,,,,,,,,,,.,.,,::.,,,,:::~~=~:=+~?~~                            
      I77?+?IIIIIIIII7I7=~,.,,,..,,,,.,.,.......,.,.,.,..,,,:~=~:==~~                         
     +=I7777I?+???IIIIII+=:..,,,,,,,,,,,...,,,,,,,,,,,,..,,,:..:?I7+...,,                     
     +=+=I7777I=~~+~:~IIII~,..,,,,,,,,,,..,,,,,...~+II?I?+?IIHECTICII77I7=.....                
      ==++++III=~~~::~+I:+?~:.........:+IIIIIIII+=?IIJACK????????????III7II7I....             
     ?+=  ██████  █████  ███    ██  ██████  ███████ ██     ██  ██████++++???II?III....         
     ?+= ██ C    ██ A ██ ████ N ██ ██B ████ ██ U    ██     ██ ██   S ======++?II?+7II.         
     ??+ ██      ███████ ██ ██  ██ ██ ██ ██ ███████ ██  █  ██ ██     ~~~~======+???++II.       
     ??+ ██      ██   ██ ██  ██ ██ ████  ██      ██ ██ ███ ██ ██     ~~~~~~~~~===++++=II,      
     I??  ██████ ██   ██ ██   ████  ██████  ███████  ███ ███   ██████:::~~~~~~~~~====+==I,     
      ?I+=~~fg+falcon+swc+adapter+??++++===~:~~~~~~~=???=?:=H~~~~~::::::::~~~~~~~~~~=~=+?7~:    
       ?+=~~~~=++~~~~~+???~=?7II??+++++++==~~:~~~~~~:~~???=+:I~~~~~~:::::::::~~~~=++:,.,+=,,   
        =?I+~~~==++~~:+??~====+I?+===+++++==~~~::::::::::~????T~~~~~:::::~:~==+:,,,,?..::+=:   
          =?I=~~~==++=+++~==:,~~=+====+++++:,,...:,::~:::::~~~~E~:~~:~~==,.,,.?I~,..::~~=,:   
           ~=+I?=~~=~+++~~=...,~:=+====++?:~+=?I~,I=I??..~III7I:=F=~,.,,.,,.,,,...::~~++~:~:   
              ~?I+=~~~~+~~~.:+,,,:=+===+++~+==~=+:III=?I?LOL77I~~~O===,,,,.,.,,~~~~=+=~::,,:   
                ~?I+=:~~~~~~,,+:,,+==~+++++,:~~:==,??,:,,=??I++,,,: R===,,,::~~=++=:::~=..,,   
             ,,,,:=+?==~~~~.=:~~,..,=+++++=~:=+=~:.,:,,,,::?=I=:::::+~D====++++=~:::?I+?,..,   
              :,,,,~+====~:,,,:=,.,,,~~===~~~,:==~~~~~~:..,,,,,,..,,,~==S+++~:,~++I++II?...    
               :,,,,,,+==+,:..:==.:,,~:~~~~~:,,,,:~~~~~~~~=========~++++~,M....II+II+?...,:    
                 ,,,,,,,++.,,.,,,,=:,,~:::~:::,,,,,,,,,::~~~=====~====~......E.?I=I.....,:~    
                   ::,,,,,,:~::,~+I+,..~::::::,,,,,,,,,,,,,,,,,~==~~~.........+L....L..S:,,    ''')
        
def setup():
    global bus
    try:
        bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
    except OSError:
        sys.exit() # quits if there is no canbus interface
    print("                      ")
    print("        CANbus active on", bus)   
    print("        waiting for matching can frame...")     #this line gets replaced by the next matching can frame
    print("        Raspotify Control via CAN...")             # this line gets replaced by the button in the car that is pushed
    
def msgbuffer():
    global message, q, SWC
    while True:
        message = bus.recv()          # if recieving can frames then put these can arb id's into a queue
        if message.arbitration_id == SWC:                        
            q.put(message)
        #if message.arbitration_id == SWM:                        
        #   q.put(message)
        #if message.arbitration_id == ICC:                        
        #    q.put(message)
def diagnostics():
     global bus 
     bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
     AllMsCanModules = 0x720
     #AllMsCanModules = (0x720, 0x726, 0x727, 0x736, 0x760, 0x767, 0x781, 0x7A6)
     StartDiagnosticSession = can.Message(arbitration_id=AllMsCanModules,
                       data=[0x02, 0x10, 0x83, 0x00, 0x00, 0x00, 0x00, 0x00],
                       is_extended_id=False)
     try:
         bus.send(StartDiagnosticSession)
         print("Message sent on {}".format(bus.channel_info))
     except can.CanError:
         print("Message NOT sent")
     
def main(): 
    global message, bus, q, SWC, SteeringWheelControlSeek, SWC_VOLUP, SWC_VOLDOWN, SWC_PHONE, AudioControlModuleOff
    try:
        while True:
            for i in range(8):
                while(q.empty() == True):                               # wait for messages to queue
                    pass
                message = q.get()   
                c = '{0:f},{1:d},'.format(message.timestamp,count)
                if message.arbitration_id == SWC and message.data[6] in AudioControlModuleOff:
                    if message.arbitration_id == SWC and message.data[7] in SteeringWheelControlSeek:
                        diagnostics()
                        #light up the cluster with a diagnostics command 
                        os.system("""
                                cansend can0 720#0210870000000000
                                cansend can0 720#023E010000000000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#023E010000000000
                                cansend can0 720#0210830000000000
                                cansend can0 720#0331020000000000
                                cansend can0 720#0233020000000000
                                cansend can0 720#023E010000000000
                            """)
                        time.sleep(0.5)
                        print("SWCSeekBtn pushed @", message.timestamp)
                                                      
                    elif message.arbitration_id == SWC and message.data[7] in SWC_VOLUP:
                        os.system("") #IC Self-Test Here 
                        print("SWCVolUpBtn pushed @", message.timestamp)
                        time.sleep(0.5)
                            
                    elif message.arbitration_id == SWC and message.data[7] in SWC_VOLDOWN:  
                        os.system("") # FDIM SELF TEST HERE 
                        print("SWCVolDownBtn pushed @", message.timestamp)
                        time.sleep(0.5)
                        
                    elif message.arbitration_id == SWC and message.data[6] in SWC_PHONE:
                        os.system("") #ACM SELF TEST HEE
                        os.system("")
                        print("SWCPhoneBtn pushed @", message.timestamp)                    
                        time.sleep(0.5)
                    else:
                        pass        
                                                                   
    except KeyboardInterrupt:
        sys.exit(0)                                              # quit if ctl + c is hit
    except Exception:
        sys.exit()
    except OSError:
        sys.exit()                                               # quit if there is a system issue
############################
# can0swc 
############################
if __name__ == "__main__":
    q                      = queue.Queue()                       #
    rx                     = Thread(target = msgbuffer)          #
    scroll()                                                     # scroll out fancy logo text
    setup()                                                      # set the can interface
    rx.start()                                                   # start the rx thread and queue msgs
    main()                                                       
