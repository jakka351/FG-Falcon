'''Each ECU contains on-board diagnostics (as specified in the Subsystem Specific Diagnostic Specification 
for that ECU) that allows the ECU and a set of its subsystem components to be evaluated via the vehicle’s 
serial communication link.'''
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

class Bus(object):
    global MidSpeedCan, HighSpeedCan
    MidSpeedCan   = can.interface.Bus(channel='vcan0', bustype='socketcan', bitrate="125000") # MS CAN
    HighSpeedCan  = can.interface.Bus(channel='vcan0', bustype='socketcan', bitrate="125000") # HS CAN
