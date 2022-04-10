#usr/bin/python3
'''Diagnostic communication for all of the Ford supported protocols are defined to use a master/slave 
configuration. Interrogating devices (testers) that communicate with an ECU using a diagnostic protocol 
will be considered the master on the network. As the master, the tester initiates all diagnostic 
communication on the link and each ECU is considered the slave that responds to the tester. An ECU 
shall never initiate diagnostic dialog between itself and a tester
 CAN Generic Diagnostic Specification v2003
 https://github.com/jakka351/6FPA-util

 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         6FPAAAJGSW          FGI [FullBus] Parser'''

import can 

class FullBus(object):
    AudioControlModule                                   = {}
    AudioInterFaceModule                                 = {}
    BluetoothPhoneModule                                 = {}
    BodyElectronicModule                                 = {}
    InstrumentCluster                                    = {}
    FrontDisplayInterfaceModule                          = {}
    HvacIntegratedModule                                 = {}
    ParkingAidModule                                     = {}
    
    HighBeamStatus = '', IllumLevelDisplay = '', IllumLevelSwitch = '', AutoHeadLampSwitchStatus = '', FogLampStatus = '', ParkAndLowBeamStatus = '', TurnStalkSwitchStatus = ""
    HeadLightStatus                                      = {}
    HeadLightStatus[ParkAndLowBeamStatus]                = [0x02]
    HeadLightStatus[HighBeamStatus]                      = [0x0E]
    HeadLightStatus[AutoHeadLampSwitchStatus]            = [0x01]
    HeadLightStatus[FogLampStatus]                       = [0x06]    
    IllumLevelDisplay                                    = {}
    IllumLevelDisplay[Dawn]                              = [0x00]
    IllumLevelDisplay[Daylight]                          = [0x00]
    IllumLevelDisplay[Twighlight]                        = [0x00]
    IllumLevelDisplay[Nighttime]                         = [0x00]
    TurnStalkSwitchStatus                                = {}
    TurnStalkSwitchStatus[IndicatingLeft]                = [0x10]
    TurnStalkSwitchStatus[IndicatingRight]               = [0x10]
    TurnStalkSwitchStatus[HazardLights]                  = [0x10]
    InstrumentCluster[0x128]                             = can.Message(arbitration_id=0x128, data=[HeadLightStatus, IllumLevelDisplay, TurnStalkSwitchStatus, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    BluetoothPhoneModule[DisplayTextAsciiData]           = can.Message(arbitration_id=0x2C0, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2C1]                          = can.Message(arbitration_id=0x2C1, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2C4]                          = can.Message(arbitration_id=0x2C4, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2CA]                          = can.Message(arbitration_id=0x2CA, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2CC]                          = can.Message(arbitration_id=0x2CC, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2CD]                          = can.Message(arbitration_id=0x2CD, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2CE]                          = can.Message(arbitration_id=0x2CE, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[0x2CF]                          = can.Message(arbitration_id=0x2CF, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioInterFaceModule[ConsumerDeviceNotConnected]     = can.Message(arbitration_id=0x2D2, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioInterFaceModule[0x2D4]                          = can.Message(arbitration_id=0x2D4, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[0x2E1]                            = can.Message(arbitration_id=0x2E1, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[0x2E2]                            = can.Message(arbitration_id=0x2E2, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[0x2E3]                            = can.Message(arbitration_id=0x2E3, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[AudioTunedFrequency]              = can.Message(arbitration_id=0x2E6, data=[AudioTunedFMFrequency, AudioFMFrequencyStep, AudioTunerBandPreset, RDS_PSN_State], is_extended_id=False)                     
    AudioControlModule[0x2EC]                            = can.Message(arbitration_id=0x2EC, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[0x2EF]                            = can.Message(arbitration_id=0x2EF, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[AudioCurrentMediaMode]            = can.Message(arbitration_id=0x2F2, data=[AudioCurrentVolume, AudioBassLevel, AudioTrebleLevel, AudioMiddleLevel, AudioBalanceLevel, AudioFadeLevel, AudioCurrentMedia, SteeringWheelControls], is_extended_id=False)                     
    AudioControlModule[0x2F4]                            = can.Message(arbitration_id=0x2F4, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[SmallScrollingFdimText]           = can.Message(arbitration_id=0x2F5, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[0x2F6]                            = can.Message(arbitration_id=0x2F6, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[0x2F9]                            = can.Message(arbitration_id=0x2F9, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    FrontDisplayInterfaceModule[IllumBatsaverRequest_MS] = can.Message(arbitration_id=0x2FC, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    FrontDisplayInterfaceModule[0x307]                   = can.Message(arbitration_id=0x307, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[AudioRDS_PSName]                  = can.Message(arbitration_id=0x309, data=[AudioRDS_PSName_0, AudioRDS_PSName_1, AudioRDS_PSName_2, AudioRDS_PSName_3, AudioRDS_PSName_4, AudioRDS_PSName_5, AudioRDS_PSName_6, AudioRDS_PSName_7], is_extended_id=False)                     
    AudioControlModule[CD_TrackNumber]                   = can.Message(arbitration_id=0x30B, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)                     
    AudioControlModule[0x30D]                            = can.Message(arbitration_id=0x30D, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)                     
    AudioControlModule[0x30F]                            = can.Message(arbitration_id=0x30F, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)                     
    AudioControlModule[0x311]                            = can.Message(arbitration_id=0x311, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    FrontDisplayInterfaceModule[InteriorActualTemp]      = can.Message(arbitration_id=0x313, data=[IntActualTemp, RadioDataServiceSwitches, ], is_extended_id=False)                         
    AudioControlModule[0x315]                            = can.Message(arbitration_id=0x315, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[VehicleIdentificationNumber]      = can.Message(arbitration_id=0x317, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    InstrumentCluster[ParkBrakeOn_MS]                    = can.Message(arbitration_id=0x330, data=[CurrentSpeed0, CurrentSpeed1, CurrentTransmissionGear, 0x00, 0x00, AudioEnableDisable, 0x00], is_extended_id=False)
    InstrumentCluster[FuelCutOffStatus]                  = can.Message(arbitration_id=0x340, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    HvacIntegratedModule[HeatingVentilationAirCon]       = can.Message(arbitration_id=0x353, data=[FanSpeedTarget, FanSpeedActual, VentPosition, RecirculationPosition, SetTemp, SetTempTarget], is_extended_id=False)
    ParkingAidModule[Sonar_ParkFailed]                   = can.Message(arbitration_id=0x360, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    ParkingAidModule[0x365]                              = can.Message(arbitration_id=0x365, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BodyElectronicModule[0x403]                          = can.Message(arbitration_id=0x403, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BodyElectronicModule[0x406]                          = can.Message(arbitration_id=0x406, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BodyElectronicModule[0x409]                          = can.Message(arbitration_id=0x409, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BodyElectronicModule[BemKeepAlive]                   = can.Message(arbitration_id=0x501, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[AcmKeepAlive]                     = can.Message(arbitration_id=0x50C, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    FrontDisplayInterfaceModule[FdimKeepAlive]           = can.Message(arbitration_id=0x55C, data=[IntActualTemp, RadioDataServiceSwitches, ], is_extended_id=False)                         
    AudioInterFaceModule[AimKeepAlive]                   = can.Message(arbitration_id=0x555, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    InstrumentCluster[IpcKeepAlive]                      = can.Message(arbitration_id=0x511, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    BluetoothPhoneModule[BpmKeepAlive]                   = can.Message(arbitration_id=0x541, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    ParkingAidModule[Sonar_ParkFailed]                   = can.Message(arbitration_id=0x360, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    InstrumentCluster[ManualsTransFlagFromPcm]           = can.Message(arbitration_id=0x640, data=[ManualTransmissionFlag, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)     
    BodyElectronicModule[PassiveAntiTheftSystem]         = can.Message(arbitration_id=0x6F8, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    AudioControlModule[SeventeenEightyEight]             = can.Message(arbitration_id=0x6FC, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    InstrumentCluster[DiagSig_tx]                        = can.Message(arbitration_id=0x728, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    BodyElectronicModule[DiagSig_tx]                     = can.Message(arbitration_id=0x72E, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    AudioControlModule[DiagSig_tx]                       = can.Message(arbitration_id=0x72F, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    ParkingAidModule[DiagSig_tx]                         = can.Message(arbitration_id=0x73A, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    AudioInterFaceModule[DiagSig_tx]                     = can.Message(arbitration_id=0x76F, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    FrontDisplayInterfaceModule[DiagSig_tx]              = can.Message(arbitration_id=0x7AE, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    BluetoothPhoneModule[DiagSig_tx]                     = can.Message(arbitration_id=0x789, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    
    
    AudioCurrentVolume                                   = AudioControlModule[AudioCurrentMediaMode].data[0] / 2
    AudioBassLevel                                       = AudioControlModule[AudioCurrentMediaMode].data[1]
    AudioTrebleLevel                                     = AudioControlModule[AudioCurrentMediaMode].data[2]
    AudioMiddleLevel                                     = AudioControlModule[AudioCurrentMediaMode].data[3]
    AudioBalanceLevel                                    = AudioControlModule[AudioCurrentMediaMode].data[4]
    AudioFadeLevel                                       = AudioControlModule[AudioCurrentMediaMode].data[5]
    AudioCurrentMedia                                    = AudioControlModule[AudioCurrentMediaMode].data[6]
    #Radio = 0x00, CdPlayer = 0x00, Aux1 = 0x00, Aux2 = 0x00, Ipod = 0x00, Mp3 = 0x00, AudioOff= 0x00, PhoneCallActive = 0x00
    AudioCurrentMedia = Radio,  CdPlayer, Aux1, Aux2, Ipod, Mp3, AudioOff, PhoneCallActive
    SteeringWheelControls                                = AudioControlModule[AudioCurrentMediaMode].data[7]
    '''
    IllumBatsaverRequest_MS[Byte_Dictionary]  = ["FDIM 0x307", IllumBatsaverRequest_MS, AcOn, AcOff, FanSpeedUp, FanSpeedDown, TempUp, TempDown, RecircOnOff, FrontDemist, RearBacklite] 
    byte0 = {}
    byte0[AcOn] = 0x00
    byte0[AcOff] = 0x00
    byte0[FanSpeedUp] = 0x00
    byte0[FanSpeedDown] = 0x00
    byte0[AcTempUp] = 0x00
    byte0[AcTempDown] = 0x00
    byte0[FrontDemist] = 0x00
    byte0[RearBacklite] = 0x00
    byte0[LockSwitch] = 0x00
    
    InstrumentCluster                                    = {}
    IllumLevelDisplay                                    = 0x128
    SpeedTransInfo                                       = 0x330
    FuelCutOffStatus                                     = 0x340
    InstrumentCluster[IllumLevelDisplay]                 = ["IPC 0x128", "Illumination Level Display", message.data[1]]
    InstrumentCluster[SpeedTransInfo]                    = ["IPC 0x330", "Current Speed:", message.data[0:1], "Current Gear:", message.data[2]]
    InstrumentCluster[FuelCutOffStatus]                  = ["IPC 0x340", "FuelCutOffStatus", message.data[0:8]] 
    Sonar_ParkFailed                                     = 0x360
    ArbitrationId                                                = {}
    ArbitrationId[AudioControlModule]                            = [0x2E1, 0x2E2, 0x2E3, 0x2E6, 0x2EC, 0x2EF, 0x2F2, 0x2F4, 0x2F5, 0x2F6, 0x2F9, 0x309, 0x30B, 0x30D, 0x30F, 0x317]
    ArbitrationId[AudioInterFaceModule]                          = [0x2D2, 0x2D3, 0x2D4, 0x555]
    ArbitrationId[BluetoothPhoneModule]                          = [0x2C0, 0x2C1, 0x2C4, 0x2CA, 0x2CC, 0x2CD, 0x2CE, 0x2CF]
    ArbitrationId[BodyElectronicModule]                          = [0x403, 0x406, 0x409, 0x541, 0x6F8]
    ArbitrationId[FrontDisplayInterfaceModule]                   = [0x2FC, 0x307, 0x311, 0x313, 0x315, 0x55C]
    ArbitrationId[InstrumentCluster]                             = [0x128, 0x330, 0x340, 0x511, 0x6FA]
    ArbitrationId[ParkingAidModule]                              = [0x360, 0x365]
    0x128 = ''
    0x2CA = ''
    0x2D4 = ''
    0x2E1 = ''
    0x2E2 = ''
    0x2E3 = ''
    0x2E6 = ''
    0x2EC = ''
    0x2EF = ''
    0x2F2 = ''
    0x2F4 = ''
    0x2F5 = ''
    0x2F9 = ''
    0x2FC = ''
    0x307 = ''
    0x309 = ''
    0x30B = ''
    0x30D = ''
    0x30F = ''
    0x311 = ''
    0x313 = ''
    0x315 = ''
    0x317 = ''
    0x330 = ''
    0x340 = ''
    0x353 = ''
    0x360 = ''
    0x365 = ''
    0x403 = ''
    0x406 = ''
    0x409 = ''
    0x501 = ''
    0x50C = ''
    0x511 = ''
    0x541 = ''
    0x555 = ''
    0x55C = ''
    0x640 = ''
    0x6F6 = ''
    0x6FC = ''
    MessageDescriptors = {}
    MessageDescriptors[0x128] = 
    MessageDescriptors[0x2CA] = []
    MessageDescriptors[0x2D4] = []
    MessageDescriptors[0x2E1] = []
    MessageDescriptors[0x2E2] = []
    MessageDescriptors[0x2E3] = []
    MessageDescriptors[0x2E6] = []
    MessageDescriptors[0x2EC] = []
    MessageDescriptors[0x2EF] = []
    MessageDescriptors[0x2F2] = [
    MessageDescriptors[0x2F4] = []
    MessageDescriptors[0x2F5] = []
    MessageDescriptors[0x2F9] = [CD_PlayingNow, CD_TrackNumber, CD_Type]
    MessageDescriptors[0x2FC] = []
    MessageDescriptors[0x307] = []
    MessageDescriptors[0x309] = []
    MessageDescriptors[0x30B] = []
    MessageDescriptors[0x30D] = []
    MessageDescriptors[0x30F] = []
    MessageDescriptors[0x311] = [BeltMinderStatus]
    MessageDescriptors[0x313] = []
    MessageDescriptors[0x315] = [DoorLockingSettings, CycleLockSetting, CabLightSettings,]
    MessageDescriptors[0x317] = [VehicleIdentificationNumber]
    MessageDescriptors[0x330] = [CurrentVehicleSpeed, CurrentTransmissionGear, AudioEnableDisable]
    MessageDescriptors[0x340] = [FuelCutOffStatus]
    MessageDescriptors[0x353] = []
    MessageDescriptors[0x360] = []
    MessageDescriptors[0x365] = []
    MessageDescriptors[0x403] = []
    MessageDescriptors[0x406] = []
    MessageDescriptors[0x409] = []
    MessageDescriptors[0x501] = []
    MessageDescriptors[0x50C] = []
    MessageDescriptors[0x511] = []
    MessageDescriptors[0x541] = []
    MessageDescriptors[0x555] = []
    MessageDescriptors[0x55C] = []
    MessageDescriptors[0x640] = []
    MessageDescriptors[0x6F6] = [PassiveAntiTheftSystem]
    MessageDescriptors[0x6FC] = [RadioModuleDiagnostics]
    AutoHeadLampSwitchStatus
    FogLampStatus
    HighBeamStatus
    IllumLevelDisplay 
    IllumLevelSwitch 
    ParkAndLowBeamStatus
    TurnStalkSwitchStatus'''