#!/usr/bin/python3
#// Ford FG can0hvac
#FG Falcon can-frames used in this example
#https://jakka351.github.io/FG-Falcon/
#import RPi.GPIO as GPIO #GPIO Library for LED on GPIO22 on PiCAN2 board
import can 
import time
import os
import uinput #keypress lib for version 1
import queue
from threading import Thread

HVAC                    =  0x353 #can id 851 
HVAC_off                =  0xAB  #  [5] A 129 0 0 34 [171] 0 0    All Off
HVAC_TEMP               =  0     #851 x4
HVAC_OUT                =  0     #Outside Temp 851 x5
HVAC_FANSPEED           =  0     #Fan speed 851 x8
HVAC_VENTSTATUS         =  0     #Vent tatus 851 x1
VA                      =  0x4B  # print('Foot Vents, Close Cabin')
VB                      =  0x2B  # print('Foot Vents, Open Cabin')
VC                      =  0x2F  # print('Window and Feet Vets, Open Cabin')
VD                      =  0x4F  # print('Window and Feet Vents, Close Cabin')
VE                      =  0x5B  # print('Face, Foot, Close Cabin')
VF                      =  0x3B  # print('Face, Foot, Open Cabin')
VG                      =  0x33  # print('Face, Open Cabin')
VH                      =  0x53  # print('Face, Close Cabin')
VI                      =  0x27  # print('Window, Manual Fan')
VJ                      =  0x26  # print('Window, Auto Fan')
VK                      =  0x83  # print('A/C Off, Open Cabin')
VL                      =  0x8B  # print('A/C Off, Foot Vents, Open Cabin')
VM                      =  0x8F  # print('A/C Off, Foot and Window Vents, Open Cabin')
VN                      =  0x9B  # print('A/C Off, Foot and Face Vents, Open Cabin')
VO                      =  0xA6  # print('A/C Off, Window Vents, Open Cabin')
VP                      =  0xA7  # print('A/C Off, Manual Fan, Open Cabin')
VQ                      =  0xC3  # print('A/C Off, Close Cabin')
VR                      =  0xCB  # print('A/C Off, Foot Vents, Close Cabin')
VS                      =  0xCF  # print('A/C Off, Foot and Window Vents, Close Cabin')
VT                      =  0xDB  # print('A/C Off, Foot and Face Vents, Close Cabin')
VU                      =  0x43  # print('Auto, Close Cabin')
VW                      =  0x23  # print('Auto, Open Cabin')

try:
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native') #bus channel & type refer to python-can docs
except OSError:
    print('can0swc cannot start can0 or can1 interface: can0swc cant get it up: check wiring and config')
    #GPIO.output(led,False)
    exit()

def can_rx_task():  # Recv can frames only with CAN_ID specified in SWC variable
    while True:
        message = bus.recv()
        if message.arbitration_id == HVAC: #CAN_ID variable
            q.put(message)          # Put message into queue
            print('')
q = queue.Queue()
rx = Thread(target = can_rx_task)
rx.start()
#c = ''
count = 0

time.sleep(0.1)

# Main loop
try:
    while True:
        for i in range(1):
            while(q.empty() == True):       # Wait until there is a message
                pass
            message = q.get()
 
            if message.arbitration_id == HVAC and message.data[3] != HVAC_TEMP:
                print('AC Temp:')
                print(message.data[3] / 2)
                time.sleep(1.0)

            if message.arbitration_id == HVAC and message.data[4] != HVAC_OUT:
                print('Outside Temp:')
                print(message.data[4])
                time.sleep(1.0)

            if message.arbitration_id == HVAC and message.data[7] != HVAC_FANSPEED:
                print('Fan Speed:')
                print(message.data[7])
                time.sleep(1.0)

            if message.arbitration_id == HVAC and message.data[0] != HVAC_VENTSTATUS:
                print('Vent Status:')
                print(message.data[0])
                if message.data[0] == VA:
                 print('Foot Vents, Close Cabin')
                if message.data[0] == VB:
                 print('Foot Vents, Open Cabin')
                if message.data[0] == VC: 
                 print('Window and Feet Vets, Open Cabin')
                if message.data[0] == VD:
                 print('Window and Feet Vents, Close Cabin')
                if message.data[0] == VE:
                 print('Face, Foot, Close Cabin')
                if message.data[0] == VF:
                 print('Face, Foot, Open Cabin')
                if message.data[0] == VG:
                 print('Face, Open Cabin')
                if message.data[0] == VH: 
                 print('Face, Close Cabin')
                if message.data[0] == VI: 
                 print('Window, Manual Fan')
                if message.data[0] == VJ: 
                 print('Window, Auto Fan')
                if message.data[0] == VK:
                 print('A/C Off, Open Cabin')
                if message.data[0] == VL:
                 print('A/C Off, Foot Vents, Open Cabin')
                if message.data[0] == VM:
                 print('A/C Off, Foot and Window Vents, Open Cabin')
                if message.data[0] == VN:
                 print('A/C Off, Foot and Face Vents, Open Cabin')
                if message.data[0] == VO:
                 print('A/C Off, Window Vents, Open Cabin')
                if message.data[0] == VP:
                 print('A/C Off, Manual Fan, Open Cabin')
                if message.data[0] == VQ:
                 print('A/C Off, Close Cabin')
                if message.data[0] == VR:
                 print('A/C Off, Foot Vents, Close Cabin')
                if message.data[0] == VS:
                 print('A/C Off, Foot and Window Vents, Close Cabin')
                if message.data[0] == VT:
                 print('A/C Off, Foot and Face Vents, Close Cabin')
                if message.data[0] == VU:
                 print('Auto, Close Cabin')
                if message.data[0] == VW: 
                 print('Auto, Open Cabin')
                time.sleep(1.0) 

            if message.arbitration_id == HVAC and message.data[5] == HVAC_off:
                print('AC Off')
                time.sleep(1.0)

            #if message.arbitration_id == HVAC:
             #   print('')
             #   time.sleep(1.0)

except KeyboardInterrupt:
    exit()
