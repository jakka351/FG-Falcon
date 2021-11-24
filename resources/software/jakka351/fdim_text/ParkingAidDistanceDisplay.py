# rpm shift alert hack
# this is a hack and not advisable to actually use on the road - be warned!
# this script will send altered data to the cluster in order to trigger the engine overspeed alarm so it can be used as a shift alert
# the shift alert needs to be enabled via module configuration
# be aware it will log a fault code everytime it goes off - the script will periodically clear the all fault codes in the PCM 
# this script assumes the mki fg falcon highspeed can interface is up on can0
# https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/python3

############################
#import modules
############################
import can
import time
import os
import queue
from threading import Thread
import sys, traceback
############################
#Global Variables
############################

c                      = ''
count                  = 0  
PamId1                 = 0x360
PamId2                 = 0x365, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B) # last two digits of the RPM, set as a range to make it easier for python-can to catch it


def scroll():
    #prints logo to console
        print('  ')
        print('             ,777I77II??~++++=~::,,,,::::::::::~~~==+~                                        ')
        print('           ,IIIIII,IIII+~..,,:,,,,,:~:,,.....,~,,:::~+?+?=                                    ')
        print('         :=I7777I=IIIIII~...:===,:,=~:,,,,,,::=,,,:::~~:=?===                                 ')
        print('      ~=,?I?777II7IIIII=~,.,,,,,,,,,,,:,,,,,,::,,,,~:~~~~:~+:~:~                              ')
        print('      I=I?IIIIII~IIIIIII+:..,,,,,,,,,,,,.,.,,::.,,,,:::~~=~:=+~?~~                            ')
        print('      I77?+?IIIIIIIII7I7=~,.,,,..,,,,.,.,.......,.,.,.,..,,,:~=~:==~~                         ')
        print('     +=I7777I?+???IIIIII+=:..,,,,,,,,,,,...,,,,,,,,,,,,..,,,:..:?I7+...,,                     ')
        print('     +=+=I7777I=~~+~:~IIII~,..,,,,,,,,,,..,,,,,...~+II?I?+?III7IIII777I7=.....                ')
        print('      ==++++III=~~~::~+I:+?~:.........:+IIIIIIII+=?IIIIIII???????????III7II7I....             ')
        print('     ?+=======::,,,,...,,:=?==~?+?????????????+==~~~~~===+++++++++++++++???II?III....         ')
        print('     ?+=======+=~=I7III~:~~I??++??IIIIII??+??++++==~~~~:::~~~~============++?II?+7II.         ')
        print('     ??+=====~~~=~~~+III~~=III??++++=+++?II??+=+?+====~~~:::::~~~~~~~~~~======+???++II.       ')
        print('     ??+=?=~~~~~~~~~~=~I=77I7III??++==~++++=+I??+?~?+===~~~~::::::~~~~~~~~~~~===++++=II,      ')
        print('     I??+=++=~~~~~~~~~~~?I777IIII??++====~======????+==+==~~~~:::::::::~~~~~~~~~====+==I,     ')
        print('      ?I+=~~=++~~~~~~~~=?=:+IIIII??++++===~:~~~~~~~=???=?:=~~~~~::::::::~~~~~~~~~~=~=+?7~:    ')
        print('       ?+=~~~~=++~~~~~+???~=?7II??+++++++==~~:~~~~~~:~~???=+:~~~~~~:::::::::~~~~=++:,.,+=,,   ')
        print('        =?I+~~~==++~~:+??~====+I?+===+++++==~~~::::::::::~????~~~~~:::::~:~==+:,,,,?..::+=:   ')
        print('          =?I=~~~==++=+++~==:,~~=+====+++++:,,...:,::~:::::~~~~+~:~~:~~==,.,,.?I~,..::~~=,:   ')
        print('           ~=+I?=~~=~+++~~=...,~:=+====++?:~+=?I~,I=I??..~III7I:==~,.,,.,,.,,,...::~~++~:~:   ')
        print('              ~?I+=~~~~+~~~.:+,,,:=+===+++~+==~=+:III=?I?77777I~~~===,,,,.,.,,~~~~=+=~::,,:   ')
        print('                ~?I+=:~~~~~~,,+:,,+==~+++++,:~~:==,??,:,,=??I++,,,:~===,,,::~~=++=:::~=..,,   ')
        print('             ,,,,:=+?==~~~~.=:~~,..,=+++++=~:=+=~:.,:,,,,::?=I=:::::+~====++++=~:::?I+?,..,   ')
        print('              :,,,,~+====~:,,,:=,.,,,~~===~~~,:==~~~~~~:..,,,,,,..,,,~==+++~:,~++I++II?...    ')
        print('               :,,,,,,+==+,:..:==.:,,~:~~~~~:,,,,:~~~~~~~~=========~++++~,....II+II+?...,:    ')
        print('                 ,,,,,,,++.,,.,,,,=:,,~:::~:::,,,,,,,,,::~~~=====~====~.......?I=I.....,:~    ')
        print('                   ::,,,,,,:~::,~+I+,..~::::::,,,,,,,,,,,,,,,,,~==~~~.........+.......,:,,    ')        
        print('                        :,,,,,,:~::,~+I+FDIM DISPLAY HACK BY jakka351.     ..+.......,:,,     ') 
def setup():
    global bus
    try:
        bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
                                                   # vcan0 is a virtual can interface, handy for testing
    except OSError:
        print("the can interface is not up...")
        sys.exit()
                                                   # quits if there is no canbus interface

    print("CANbus active on", bus)  
    print("..")     
    print("")
    print("")

def cleanline():                      # cleans the last output line from the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def msgbuffer():
    global message, q, bus, PamId1, PamId2                                        
    while True:
        message = bus.recv()          # if recieving can frames then put these can arb id's into a queue
        if message.arbitration_id == PamId1:                        
            q.put(message)
        elif messsage.arbitration_id == PamId2:
            q.put(message)

def main():

    try:
        while True:
            for i in range(8):
                while(q.empty() == True):                               # wait for messages to queue
                    pass
                message = q.get()           
                c = '{0:f},{1:d},'.format(message.timestamp,count)
                """
                If the system is engaged(ie car in reverse) then start another if loop
                """
                if message.arbitration_id == PamId1 and message.data[0] != 0:
                    timer = 0
                    while timer < 3:
                        #0x309 script here run once PARKING pause ACTIVE pause, repeat
                        PamActive1 = can.Message(arbitration_id=0x309, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
                        PamActive2 = can.Message(arbitration_id=0x309, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
                        task1 = bus.send_periodic(PamActive1, 0.01)
                        assert isinstance(task1, can.CyclicSendTaskABC)
                        time.sleep(1)
                        task.stop()
                        task1 = bus.send_periodic(PamActive2, 0.01)
                        assert isintance(task1, can.CyclicSendTaskABC)
                        time.sleep(1)
                        task.stop()
                        timer = timer + 1
                        if timer <= 3:
                            continue
                        else:
                            break

                        if message.arbitration_id == PamId2 and message.data[0] == 0x00:
                            continue
                        elif message.arbitration_id == PamId2 and message.data[0] != 0x00:
                            print(message)
                            #translate the sensor hex data 0x00-0xFF to hex-ascii format, 0xFF = 255 = 2550mm = 0x32, 0x35, 0x35, 0x30 = message.data[2550 mm ]
                            distance0 = []
                            start0, end0 = 0, 99
                            if start0 < end0:
                                distance0.extend(range(start0,end0))
                                distance0.append(end0)
                            distance1 = []
                            start1, end1 = 100, 199
                            if start1 < end1:
                                distance1.extend(range(start1,end1))
                                distance1.append(end1)
                            distance2 = []
                            start2, end2 = 200, 255
                            if start2 < end2:
                                distance2.extend(range(start2,end2))
                                distance2.append(end2)
                            
                            if message.data[0] in distance0:
                                dist0 = 0x30
                                dist1 = 0x30
                                
                            elif message.data[0] in distance1:
                                dist0 = 0x31
                            elif message.data[0] in distance2:
                                dist0 = 0x32
                                 
                            dist2 =
                            dist3 =
                            dist4 =
                            msg = can.Message(arbitration_id=0x309, data=[Dist1, Dist2, Dist3, Dist4, 0x20, 0x6D, 0x6d, 0x20], is_extended_id=False)
                       

                            timer = 2
                            Object1 = can.Message(arbitration_id=0x309, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
                            Detected2 = can.Message(arbitration_id=0x309, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
                            task1 = bus.send_periodic(Object1, 0.01)
                            assert isinstance(task1, can.CyclicSendTaskABC)
                            time.sleep(1)
                            task.stop()
                            task1 = bus.send_periodic(Detected2, 0.01)
                            assert isintance(task1, can.CyclicSendTaskABC)
                            time.sleep(1)
                            task.stop()
                            timer = timer + 1
                            if timer != 3:
                                continue
                            else:
                                break   
                            #print OBJECT DETECTED
                            #print 0000-2550 mm
                            #Run object detected script                    if message.arbitration_id == ClusterMessage and message.data[0] != 0:
                            msg = can.Message(arbitration_id=0x309, data=[Dist1, Dist2, Dist3, Dist4, 0x20, 0x6D, 0x6d, 0x20], is_extended_id=False)
                       cleanline()
                       cleanline()
                       print(message)
                       print("Data", time)
#dist1  = message.data[0]
                            #dist2  = message.data[1]
                            #dist3  = message.data[2] 
                            #dist4  = message.data[3]
                            
                       task = bus.send_periodic(msg, 0.01)
                       assert isinstance(task, can.CyclicSendTaskABC)
                       time.sleep(10)
                       task.stop()
                       time.sleep(3)
                    
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
# jakka351
############################
    

if __name__ == "__main__":                                       # run the program
    q                      = queue.Queue()                       #
    rx                     = Thread(target = msgbuffer)          #
    scroll()                                                     # scroll out fancy logo text
    setup()                                                      # set the can interface
    rx.start()                                                   # start the rx thread and queue msgs
    main()                                                       #
