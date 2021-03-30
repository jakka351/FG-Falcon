#!/usr/bin/python3
#can0 fg falcon hscan data display
#https://github.com/jakka351/FG-Falcon | https://github.com/jakka351/can0swc
import can
import time
import os
import queue
from threading import Thread
import sys, traceback
############################
# CAN Id's
###########################
PCM_TBP                   = 0x425
############################
#  CAN Data
############################
TurboBoostPressure        = 0 #0x425


print('      ┌─┐┌─┐┌┐┌┌┬┐┬─┐┌─┐┬  ┬  ┌─┐┬─┐  ┌─┐┬─┐┌─┐┌─┐  ┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─  ')
time.sleep(0.15)
print('      │  │ ││││ │ ├┬┘│ ││  │  ├┤ ├┬┘  ├─┤├┬┘├┤ ├─┤  │││├┤  │ ││││ │├┬┘├┴┐  ')
time.sleep(0.15)
print('      └─┘└─┘┘└┘ ┴ ┴└─└─┘┴─┘┴─┘└─┘┴└─  ┴ ┴┴└─└─┘┴ ┴  ┘└┘└─┘ ┴ └┴┘└─┘┴└─┴ ┴  ')

##########################
hs-can 
##########################
os.system("sudo /sbin/ip link set can0 type can bitrate 500000 triple-sampling on restart-ms 1000")
os.system("sudo /sbin/ifconfig can0 up txqueuelen 1250")

try:
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
except OSError:
    sys.exit()

############################
# CAN Rx
############################
def can_rx_task():                                               # rx can frames only with CAN_ID specified in SWC variable
    while True:
        message = bus.recv()
        if message.arbitration_id == PCM_TBP:                        # CAN_ID variable
            q.put(message)      

############################
# Rx Queue
############################
q = queue.Queue()
rx = Thread(target = can_rx_task)
rx.start()
c = ''
count = 0
############################
# Main Loop
############################
try:
    while True:
        for i in range(8):
            while(q.empty() == True):       # Wait until there is a message
                pass
            message = q.get()
            c = '{0:f},{1:d},'.format(message.timestamp,count)
            ###########################
            #intake absolute pressure
            ###########################
            if message.arbitration_id == PCM_TBP:
                if message.data[] == []:
                    time.sleep(0.1)
                elif message.data[] == []:
                    time.sleep(0.1)
            
            else:
                pass

except KeyboardInterrupt:
    sys.exit()
except Exception:
    traceback.print_exc(file=sys.stdout)
    sys.exit()
except OSError:
    sys.exit()

############################
# can0swc
############################
    
