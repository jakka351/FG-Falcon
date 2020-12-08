#!/usr/bin/python3
#
#FG Falcon python script swc_seek
#Listens on canbus for press of swc_seek and then activates keypress
#https://jakka351.github.io/FG-Falcon/
import RPi.GPIO as GPIO
import can
import time
import os
import uinput
import queue
from threading import Thread

led = 22 #GPIO22 on the PiCAN2 Board has a LED fitted
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)

# simulated keypresses setup
device = uinput.Device([
        uinput.KEY_NEXTSONG,
        uinput.KEY_PREVIOUSSONG,
        uinput.KEY_PLAYPAUSE,
        uinput.KEY_VOLUMEUP,
        uinput.KEY_VOLUMEDOWN,
        uinput.KEY_MUTE,
        uinput.KEY_M,
        uinput.KEY_O,
])


# add full can data
SWC_SEEK               = 0x09 #frame 8
SWC_SEEKHOLD           = 0x09 #frame 8
SWC_VOLUP              = 0x11 #frame 8
SWC_VOLDOWN            = 0x19 #frame 8
SWC_PHONE              = 0x68 #frame 7      
SWC                    = 0x2F2 #can id

print('\n\rSteering Wheel Controls Adapter Starting...')
print('PiCAN2 Board bringing up can0 hs-can...')
print('Generic CAN board bringing up can1 ms-can...')

# Bring up can0 interface at 500kbps
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
#os.system("sudo /sbin/ip link set can1 up type can bitrate 125000")
time.sleep(0.1)
print('can0 ready')
print('can1 ready')
print('listening for 0x2F2 can ids on bus...')

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    GPIO.output(led,False)
    exit()

def can_rx_task():  # Receive thread
    while True:
        message = bus.recv()
        if message.arbitration_id == SWC:
            q.put(message)          # Put message into queue
            print('')
            print('can frame queued...')
            print('detected steering wheel button:')
q = queue.Queue()
rx = Thread(target = can_rx_task)
rx.start()
c = ''
count = 0

# Main loop
try:
    while True:
        #for i in range(16):
            while(q.empty() == True):       # Wait until there is a message
                pass
            message = q.get()

            c = '{0:f},{1:d},'.format(message.timestamp,count)
            if message.arbitration_id == SWC and message.data[7] == SWC_SEEK:
                device.emit_click(uinput.KEY_NEXTSONG) # Next Track
                print('     Seek!')

            if message.arbitration_id == SWC and message.data[7] == SWC_VOLUP:
                device.emit_click(uinput.KEY_VOLUMEUP) # 
                print('     Volup!')
                                    
            if message.arbitration_id == SWC and message.data[7] == SWC_VOLDOWN:
                device.emit_click(uinput.KEY_VOLUMEDOWN) #
                print('     Voldown!')

            if message.arbitration_id == SWC and message.data[6] == SWC_PHONE:
                device.emit_click(uinput.KEY_M) # 
                print('     Phone!')

       #     if message.arbitration_id == SWC and message.data[7] == SWC_SEEKHOLD:
        #        device.emit_click(uinput.KEY_NEXTSONG) # 
         #       print('Seekhold!')                             

    print('FG Falcon')

except KeyboardInterrupt:
    #Catch keyboard interrupt
    GPIO.output(led,True)
    os.system("sudo /sbin/ip link set can0 down")
    print('\n\rcan0 down can1 down')
