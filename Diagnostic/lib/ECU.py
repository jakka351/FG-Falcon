'''3.2.1 Electronics Control Unit (ECU) 
An ECU can be the microprocessor-based “brains” of all or a portion of each of the vehicle subsystems. 
Each ECU receives input data from various switches, sensors, etc. and processes that data to control the 
ECU’s outputs. Each ECU may support communication over the communications link and may also 
receive data from other ECUs on the link.'''

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
class Ecu(object):
    global DiagSig_Rx, DiagSig_Tx
    DiagSig_Tx                                            = {}
    DiagSig_Rx                                            = {}    
    IC_DiagSig_Rx                                         = 0x720
    IC_DiagSig_Tx                                         = 0x728
    BEM_DiagSig_Rx                                        = 0x726
    BEM_DiagSig_Tx                                        = 0x72E
    ACM_DiagSig_Rx                                        = 0x727
    ACM_DiagSig_Tx                                        = 0x72F
    FDIM_DiagSig_Rx                                       = 0x767
    FDIM_DiagSig_Tx                                       = 0x76F
    BPM_DiagSig_Rx                                        = 0x781
    BPM_DiagSig_Tx                                        = 0x789
    AIM_DiagSig_Rx                                        = 0x7A6
    AIM_DiagSig_Tx                                        = 0x7AE
    PAM_DiagSig_Rx                                        = 0x736
    PAM_DiagSig_Tx                                        = 0x73E
    PCM_DiagSig_Rx                                        = 0x7E0
    PCM_DiagSig_Tx                                        = 0x7E8
    TCM_DiagSig_Rx                                        = 0x7E1
    TCM_DiagSig_Tx                                        = 0x7E9
    OBD_DiagSig_Rx                                        = 0x7DF
    ABS_DiagSig_Rx                                        = 0x760
    ABS_DiagSig_Tx                                        = 0x768
    RCM_DiagSig_Rx                                        = 0x737
    RCM_DiagSig_Tx                                        = 0x73F
    HIM_DiagSig_Rx                                        = 0x733
    HIM_DiagSig_Tx                                        = 0x73B
    DiagSig_Tx[IC_DiagSig_Tx]                             = ["IPC 0x728", "Instrument Cluster"]
    DiagSig_Tx[BEM_DiagSig_Tx]                            = ["BEM 0x72E", "Body Electronic Module"]
    DiagSig_Tx[ACM_DiagSig_Tx]                            = ["ACM 0x72F", "Audio Control Module"]
    DiagSig_Tx[FDIM_DiagSig_Tx]                           = ["FDIM 0x76F", "Front Display Interface Module"]
    DiagSig_Tx[BPM_DiagSig_Tx]                            = ["BPM 0x789", "Bluetooth Phone Module"]
    DiagSig_Tx[AIM_DiagSig_Tx]                            = ["AIM 0x7AE", "Audio Inteface Module"]
    DiagSig_Tx[PAM_DiagSig_Tx]                            = ["PAM 0x73E", "Parking Aid Module"]
    DiagSig_Tx[PCM_DiagSig_Tx]                            = ["PCM 0x7E8", "Powertrain Contol Module Module"]
    DiagSig_Tx[TCM_DiagSig_Tx]                            = ["TCM 0x7E9", "Transmission Control Module"]
    DiagSig_Tx[ABS_DiagSig_Tx]                            = ["ABS 0x768", "Antilock BrakeModule"]
    DiagSig_Tx[HIM_DiagSig_Tx]                            = ["HIM 0x73B", "HVAC IntegratedModule"]
    DiagSig_Tx[RCM_DiagSig_Tx]                            = ["RCM 0x73F", "Restraints Control Module"]
    DiagSig_Rx[OBD_DiagSig_Rx]                            = ["OBDII 7DF", "On Board Diagnostics Emission Protocol"]
    DiagSig_Rx[IC_DiagSig_Rx]                             = ["IPC 0x720", "Instrument Cluster"]
    DiagSig_Rx[BEM_DiagSig_Rx]                            = ["BEM 0x726", "Body Electronic Module"]
    DiagSig_Rx[ACM_DiagSig_Rx]                            = ["ACM 0x727", "Audio Control Module"]
    DiagSig_Rx[FDIM_DiagSig_Rx]                           = ["FDIM 0x767", "Front Display Interface Module"]
    DiagSig_Rx[BPM_DiagSig_Rx]                            = ["BPM 0x781", "Bluetooth Phone Module"]
    DiagSig_Rx[AIM_DiagSig_Rx]                            = ["AIM 0x7A6", "Audio Inteface Module"]
    DiagSig_Rx[PAM_DiagSig_Rx]                            = ["PAM 0x736", "Parking Aid Module"]
    DiagSig_Rx[PCM_DiagSig_Rx]                            = ["PCM 0x7E0", "Powertrain Contol Module Module"]
    DiagSig_Rx[TCM_DiagSig_Rx]                            = ["TCM 0x7E1", "Transmission Control Module"]
    DiagSig_Rx[ABS_DiagSig_Rx]                            = ["ABS 0x760", "Antilock BrakeModule"]
    DiagSig_Rx[HIM_DiagSig_Rx]                            = ["HIM 0x733", "HVAC IntegratedModule"]
    DiagSig_Rx[RCM_DiagSig_Rx]                            = ["RCM 0x736", "Restraints Control Module"]
