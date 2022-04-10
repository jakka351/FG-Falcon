
# CAN Generic Diagnostic Specification v2003
# https://github.com/jakka351/6FPA-util
'''
 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         6FPAAAJGSW          FGI Diagnostic Parser'''
class Pid:
    global CommonID
    CommonID                                                = {}
    CommonID[0xE400]                                        = ["FNOS CAN Driver Version Number", ""]
    CommonID[0xE402]                                        = ["FNOS NM Junior/Node Management Version Number", ""]
    CommonID[0xE403]                                        = ["FNOS Interaction Layer Version Number", ""]
    CommonID[0xE404]                                        = ["FNOS Network Initialization Version Number", ""]
    CommonID[0xE405]                                        = ["FNOS Transport Layer Version Number", ""]
    CommonID[0xE406]                                        = ["FNOS Diagnostics Version Number", "" ]
    CommonID[0xE407]                                        = ["FNOS Generation Tool Version Number", "" ]
    CommonID[0xE408]                                        = ["FNOS Bootloader Version Number", "" ]
    CommonID[0xE409]                                        = ["FNOS Database Version Number", "" ]
   