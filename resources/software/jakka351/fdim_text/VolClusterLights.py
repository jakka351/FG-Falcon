#!/usr/bin/python3
# can0swc fg falcon swc-can adapter
# https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/can0swc
# assumes ms-can is up on can0
# buffers several CAN IDS, then matches byte specific data
# when it matches, emits keypress
############################
# Import modules
############################
import can
import time
import os
import queue
from threading import Thread
import sys, traceback

time.sleep(1)
c                      = ''
count                  = 0  
# CAN Id's
SWC                    = 0x2F2 
SWM                    = 0x2EC 
ICC                    = 0x2FC              #id 764
BEM                    = 0x307
# SWC Button CAN Data
SWC_SEEK               = (0x08, 0x09, 0x0C)  # seek button on bit [7] of id 0x2f2
SWC_VOLUP              = (0x10, 0x11, 0x14)  # volume + button on bit [7] of id 0x2f2
SWC_VOLDOWN            = (0x18, 0x19, 0x1C)  # volume - button on bit [7] of id 0x2f2
SWC_PHONE              = (0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68)  # phone button on bit [6] of id 0x2f2
SWC_MODE               = (0x10)
#AudioCurrentMediaMode byte 6 0x2f2
AUX                    = (0x01, 0x02, 0x41, 0x42, 0x47)
CDMP3                  = (0x03, 0x43)
PHONE                  = (0x06, 0x46)
RADIO                  = (0x05, 0x04, 0x44,0x45)
AUDIOOFF               = (0x08, 0x48)
# ICC Button CAN Data
ICC_VOLUP              = 0x41 # vol + button on bit [3] of id 0x2fc
ICC_VOLDOWN            = 0x81 # vol - button on bit [3] of id 0x2fc
ICC_NEXT               = 0x04 # seek + button on bit [0] of id 0x2fc
ICC_PREV               = 0x08 # seek - button on bit [0] of id 0x2fc
ICC_EJECT              = 0x80 # eject button on bit [1] of id 0x2fc
ICC_LOAD               = 0x40 # load button on bit [1] of id 0x2fc
#ICC_SCAN               = 0x20
#ICC_CDAUX              = 0x10
#ICC_FMAM               = 0x08
#ICC_OK                 = 0x04
#ICC_MENU               = 0x02
# Body Butonn CAN Data
#BEM_LOCK               = 0x04
#BEM_UNLOCK             = 0x02
#BEM_DSC                = 0x80
#BEM_DOMELIGHT          = 0x90
BEM_HAZARD             = 0x01

def scroll():
    #prints logo to console
        print('  ')
        print('''  
             ,777I77II??~++++=~::,,,,::::::::::~~~==+~                                        
           ,IIIIII,IIII+~..,,:,,,,,:~:,,.....,~,,:::~+?+?=                                    
         :=I7777I=IIIIII~...:===,:,=~:,,,,,,::=,,,:::~~:=?===                                 
      ~=,?I?777II7IIIII=~,.,,,,,,,,,,,:,,,,,,::,,,,~:~~~~:~+:~:~                              
      I=I?IIIIII~IIIIIII+:..,,,,,,,,,,,,.,.,,::.,,,,:::~~=~:=+~?~~                            
      I77?+?IIIIIIIII7I7=~,.,,,..,,,,.,.,.......,.,.,.,..,,,:~=~:==~~                         
     +=I7777I?+???IIIIII+=:..,,,,,,,,,,,...,,,,,,,,,,,,..,,,:..:?I7+...,,                     
     +=+=I7777I=~~+~:~IIII~,..,,,,,,,,,,..,,,,,...~+II?I?+?III7IIII777I7=.....                
      ==++++III=~~~::~+I:+?~:.........:+IIIIIIII+=?IIIIIII???????????III7II7I....             
     ?+=  ██████  █████  ███    ██  ██████  ███████ ██     ██  ██████++++???II?III....         
     ?+= ██      ██   ██ ████   ██ ██  ████ ██      ██     ██ ██     ======++?II?+7II.         
     ??+ ██      ███████ ██ ██  ██ ██ ██ ██ ███████ ██  █  ██ ██     ~~~~======+???++II.       
     ??+ ██      ██   ██ ██  ██ ██ ████  ██      ██ ██ ███ ██ ██     ~~~~~~~~~===++++=II,      
     I??  ██████ ██   ██ ██   ████  ██████  ███████  ███ ███   ██████:::~~~~~~~~~====+==I,     
      ?I+=~~fg+falcon+swc+adapter+??++++===~:~~~~~~~=???=?:=~~~~~::::::::~~~~~~~~~~=~=+?7~:    
       ?+=~~~~=++~~~~~+???~=?7II??+++++++==~~:~~~~~~:~~???=+:~~~~~~:::::::::~~~~=++:,.,+=,,   
        =?I+~~~==++~~:+??~====+I?+===+++++==~~~::::::::::~????~~~~~:::::~:~==+:,,,,?..::+=:   
          =?I=~~~==++=+++~==:,~~=+====+++++:,,...:,::~:::::~~~~+~:~~:~~==,.,,.?I~,..::~~=,:   
           ~=+I?=~~=~+++~~=...,~:=+====++?:~+=?I~,I=I??..~III7I:==~,.,,.,,.,,,...::~~++~:~:   
              ~?I+=~~~~+~~~.:+,,,:=+===+++~+==~=+:III=?I?77777I~~~===,,,,.,.,,~~~~=+=~::,,:   
                ~?I+=:~~~~~~,,+:,,+==~+++++,:~~:==,??,:,,=??I++,,,:~===,,,::~~=++=:::~=..,,   
             ,,,,:=+?==~~~~.=:~~,..,=+++++=~:=+=~:.,:,,,,::?=I=:::::+~====++++=~:::?I+?,..,   
              :,,,,~+====~:,,,:=,.,,,~~===~~~,:==~~~~~~:..,,,,,,..,,,~==+++~:,~++I++II?...    
               :,,,,,,+==+,:..:==.:,,~:~~~~~:,,,,:~~~~~~~~=========~++++~,....II+II+?...,:    
                 ,,,,,,,++.,,.,,,,=:,,~:::~:::,,,,,,,,,::~~~=====~====~.......?I=I.....,:~    
                   ::,,,,,,:~::,~+I+,..~::::::,,,,,,,,,,,,,,,,,~==~~~.........+.......,:,,    ''')
        
def setup():
    global bus
    try:
        bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
    except OSError:
        sys.exit() # quits if there is no canbus interface
    print("                      ")
    print("        CANbus active on", bus)   
    print("        waiting for matching can frame...")     #this line gets replaced by the next matching can frame
    
def msgbuffer():
    global message, q, SWC, ICC, BEM                                          
    while True:
        message = bus.recv()          # if recieving can frames then put these can arb id's into a queue
        if message.arbitration_id == SWC:                        
            q.put(message)
        if message.arbitration_id == ICC:                        
            q.put(message) 
        if message.arbitration_id == BEM:                        
            q.put(message)                       


def cleanline():                      # cleans the last output line from the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def cleanscreen():                    # cleans the whole console screen
    os.system("clear")

def ccp():
    cleanline()
    cleanline()
    print(message)
                        
def main(): 
    try:
        while True:
            for i in range(8):
                while(q.empty() == True):                               # wait for messages to queue
                    pass
                message = q.get()   
                c = '{0:f},{1:d},'.format(message.timestamp,count)

                if message.arbitration_id == SWC:     
                    if message.data[7] in SWC_SEEK:                  # and the message data of bit x matches from list
                        os.system("""
                                cansend can0 720#0210870000000000
                                cansend can0 720#023E010000000000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                sleep 1
                                cansend can0 720#062F713007000000
                                cansend can0 720#0210810000000000
                            """)
                        ccp()
                        print("SWCSeekBtn pushed @", message.timestamp) 
                        # Custom Button Function Here
                       
                    elif message.data[7] in SWC_VOLUP:
                        os.system("""
                                cansend can0 720#0210870000000000
                                cansend can0 720#023E010000000000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                            """)
                        print("SWCVOLUPBtn pushed @", message.timestamp) 
                                        
                        
                    elif message.data[7] in SWC_VOLDOWN:
                        os.system("""
                                cansend can0 720#0210870000000000
                                cansend can0 720#023E010000000000
                                cansend can0 720#062F713007800000
                                cansend can0 720#062F713007800000
                                cansend can0 309#4655434b59454148
                                                             """)
                        print("SWCVOLDOWNBtn pushed @", message.timestamp)

                    elif message.data[6]  in SWC_PHONE:
                        print("SWCPhoneBtn pushed @", message.timestamp)
                        os.system("""
                                cansend can0 720#0210870000000000
                                cansend can0 720#023E010000000000
                                cansend can0 720#062F713007000000
                                cansend can0 720#062F713007000000
                                cansend can0 309#4655434b59454148
                                cansend can0 309#4655434b59454148
                                cansend can0 309#4655434b59454148
                                cansend can0 309#4655434b59454148
                                cansend can0 309#4655434b59454148
                                cansend can0 309#4655434b59454148
                                cansend can0 309#4655434b59454148
                             """)
    
                    else:
                        pass

                else:
                    pass         
                                                                           
    except KeyboardInterrupt:
        sys.exit(0)                                              # quit if ctl + c is hit
    except Exception:
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
        sys.exit()
    except OSError:
        sys.exit()                                               # quit if there is a system issue

############################
# can0swc 
############################

if __name__ == "__main__":
    q                      = queue.Queue()                       #
    rx                     = Thread(target = msgbuffer)          #
    cleanscreen()                                                # clean the console screen
    scroll()                                                     # scroll out fancy logo text
    setup()                                                      # set the can interface
    rx.start()                                                   # start the rx thread and queue msgs
    main()                                                       # match ca


