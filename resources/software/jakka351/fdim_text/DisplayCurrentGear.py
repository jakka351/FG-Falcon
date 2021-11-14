#!/usr/bin/python3
# fdim text display scripto-matic
# https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the impl   ied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <https://www.gnu.org/licenses/>.


############################
#import modules
############################
import can
import time
import datetime
import os
import queue
from threading import Thread
import sys, traceback
############################
#Global Variables
############################

MsCanClusterInfo              = 0x330          
    



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
        print('                        :,,,,,,:~::,~+I+Fdim Text Modifer by jakka351...+.......,:,,     ') 
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
    print("FDIM Text Display Modifier...")     
    print("")
    print("")

def cleanline():                      # cleans the last output line from the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def msgbuffer():
    global message, q, MsCanClusterInfo, bus                              
    while True:
        message = bus.recv()          # if recieving can frames then put these can arb id's into a queue
        if message.arbitration_id == MsCanClusterInfo:                        
            q.put(message)

def main():
    global message, q, MsCanClusterInfo, bus
    try:
        while True:
            for i in range(8):
                while(q.empty() == True):                               # wait for messages to queue
                    pass
                message = q.get()
                CurrentGear =                   (0x01, 0x02, 0x03, 0x04, 0x05, 0x06)
                TransNeutral                  = [0x4E, 0x65, 0x75, 0x74, 0x72, 0x61, 0x6C, 0x00]  # Neutral
               
                c = '{0:f},{1:d},'.format(message.timestamp,count)
                if message.arbitration_id == MsCanClusterInfo and message.data[2] in CurrentGear:
                    if message.data[2] == 1:
                        os.system("sudo killall cangen")
                        os.system("cangen -I 309 -L 8 -D 3173742047656172 -g 10 can0 &")
                    elif message.data[2] == 2:
                        os.system("sudo killall cangen")
                        os.system("cangen -I 309 -L 8 -D 326E642047656172 -g 10 can0 &")
                    elif message.data[2] == 3:
                        os.system("sudo killall cangen")
                        os.system("cangen -I 309 -L 8 -D 3372642047656172 -g 10 can0 &")
                    elif message.data[2] == 4:
                        os.system("sudo killall cangen")
                        os.system("cangen -I 309 -L 8 -D 3474682047656172 -g 10 can0 &")
                    elif message.data[2] == 5:
                        os.system("sudo killall cangen")
                        os.system("cangen -I 309 -L 8 -D 3572642047656172 -g 10 can0 &")
                    elif message.data[2] == 6:
                        os.system("sudo killall cangen")
                        os.system("cangen -I 309 -L 8 -D 3672642047656172 -g 10 can0 &")
                                                                                  
    except KeyboardInterrupt:
        sys.exit(0)                                              # quit if ctl + c is hit
    except Exception:
        traceback.print_exc(file=sys.stdout)                     # quit if there is a python problem
        sys.exit()
    except OSError:
        sys.exit()                                               # quit if there is a system issue

############################
# jakka351 remember to add 0x2F5 scrollling texts
############################
    

if __name__ == "__main__":                                       # run the program
    setup()                                                      # set the can interface

    c                             = ''
    count                         = 0  
    q                             = queue.Queue()                       #
    rx                            = Thread(target = msgbuffer)          #
    scroll()                                                     # scroll out fancy logo text
    rx.start()                                                   # start the rx thread and queue msgs
    main()                                                       #


