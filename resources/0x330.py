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
ClusterMessage         = 0x330
FdimMessage            = 0x309

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
        print('                        :,,,,,,:~::,~+I+FDIM ENGINE DISPLAY HACK BY jakka351...+.......,:,,     ') 
def setup():
    global bus
    try:
        bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
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
    global message, q, RpmMessage                                        
    while True:
        message = bus.recv()          # if recieving can frames then put these can arb id's into a queue
        if message.arbitration_id == ClusterMessage:                        
            q.put(message)


# 52 50 4d 3a = R P M :
def main():

    try:
        while True:
            for i in range(255):
                while(q.empty() == True):                               # wait for messages to queue
                    pass
                message = q.get()
                       
                messdata1 = (0x00 - )
                    #   Want to display RPM, Speed and EOT CHT on FDIM
                c = '{0:f},{1:d},'.format(message.timestamp,count)
                if message.arbitration_id == ClusterMessage:
                    Rpm0 = 0
                    Rpm1 = 0
                    Rpm2 = 0
                    Rpm3 = 0
                    if message.data[0] == 0x09:
                        Rpm0 = 0x30 #Ascii 9
                        Rpm1 = 0x39
                    elif message.data[0] == 0x08:
                        Rpm0 = 0x30
                        Rpm1 = 0x38
                    elif message.data[0] == 0x0A:
                        Rpm0 = 0x31
                        Rpm1 = 0x30

                    else:
                        pass

                    if message.data[1] in 
                                            #Rpm0 = message.data[0] + 0x30
                    #Rpm1 = message.data[0]  
                    #Rpm2 = message.data[1] 
                    Gear2 = message.data[2] 
                    Data3 = message.data[3]
                    Speed4 = message.data[4]
                    Speed5 = message.data[5]
                    Data6 = message.data[6]
                    Data7 = message.data[7]
                    
                    try:
                        msg = can.Message(
                            arbitration_id=FdimMessage, data=[0x52, 0x50, 0x4D, 0x3A, Rpm0, Rpm1, Rpm2, Rpm3], is_extended_id=False
                        )

                        cleanline()
                        cleanline()
                        print(message)
                        print("Data", time)

                        task = bus.send_periodic(msg, 0.010)
                        assert isinstance(task, can.CyclicSendTaskABC)
                        time.sleep(0.1)
                        task.stop()
                        #time.sleep(3)
                    except KeyboardInterrupt:
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
