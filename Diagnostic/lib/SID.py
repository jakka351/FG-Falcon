
# CAN Generic Diagnostic Specification v2003
# https://github.com/jakka351/6FPA-util
'''
 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         6FPAAAJGSW          FGI Diagnostic Parser'''
class Sid:
    global ServiceRequest, ServiceRequestSubFunction
    startDiagnosticSession                                = 0x10
    ReturnToOperationalState                              = 0x81
    standardDiagnosticSession                             = 0x83
    ecuProgrammingSession                                 = 0x85
    ecuAdjustmentSession                                  = 0x87
    supplierDiagnosticSession                             = 0xFA
    ecuReset                                              = 0x11
    HardReset                                             = 0x01
    SoftReset                                             = 0x02
    readFreezeFrameData                                   = 0x12
    requestStoredCodes                                    = 0x13
    clearDiagnosticInformation                            = 0x14
    readDTCByStatus                                       = 0x18
    operationalStateEntryRequest                          = 0x20
    readDataByLocalID                                     = 0x21
    readMemoryByCommonID                                  = 0x22
    readMemoryByAddress                                   = 0x23
    requestCommonIDScalingMasking                         = 0x24
    stopTransmittingRequestedData                         = 0x25
    requestSecurityAccess                                 = 0x27
    requestCommunicationControl                           = 0x28
    requestDiagnosticdataPacket                           = 0x2A
    dynamicallyDefineDiagnosticDataPacket                 = 0x2C
    writeDataByCommonID                                   = 0x2E
    inputOutputControlByLocalID                           = 0x2F
    startRoutineByLocalIdentifier                         = 0x31    
    stopRoutineByLocalIdentifier                          = 0x32
    requestRoutineResultsByLocalID                        = 0x33
    requestDownload                                       = 0x34
    requestUpload                                         = 0x35
    transferData                                          = 0x36
    requestTransferExit                                   = 0x37
    writeDataByLocalId                                    = 0x3B
    requestReadMemoryBlock                                = 0x3C
    writeMemoryByAddress                                  = 0x3D
    testerPresent                                         = 0x3E
    RequestResponse                                       = 0x01
    SuppressResponse                                      = 0x02
    reportDiagnosticState                                 = 0x50
    reportSecurityAccess                                  = 0x67
    g                                                     = 0x73 
    h                                                     = 0x74
    i                                                     = 0x75
    j                                                     = 0x76
    k                                                     = 0x77
    l                                                     = 0x78
    controlDTCSetting                                     = 0x85
    requestDiagnosticDataPacket                           = 0xA0
    dynamicallyDefineDataPacket                           = 0xA1
    noStoredCodesLoggingStateEntry                        = 0xB0
    diagnosticCommand                                     = 0xB1
    inputIntegrityTestStateEntry                          = 0xB2
    requestManufacturerStateEntry                         = 0xB4

    ServiceRequest                                        = {}
    ServiceRequest[startDiagnosticSession]                = ["startDiagnosticSession", "0x10"]
    ServiceRequest[ecuReset]                              = ["ecuReset", "0x11"]
    ServiceRequest[readFreezeFrameData]                   = ["readFreezeFrameData", "0x12"]
    ServiceRequest[requestStoredCodes]                    = ["requestStoredCodes", "0x13"] 
    ServiceRequest[clearDiagnosticInformation]            = ["clearDiagnosticInformation", "0x14"]
    ServiceRequest[readDTCByStatus]                       = ["readDTCByStatus", "0x18"]
    ServiceRequest[readDataByLocalID]                     = ["readDataByLocalID", "0x21"]
    ServiceRequest[readMemoryByCommonID]                  = ["readMemoryByAddress", "0x22"]
    ServiceRequest[readMemoryByAddress]                   = ["readMemoryByAddress", "0x23"] 
    ServiceRequest[requestCommonIDScalingMasking]         = ["requestCommonIDScalingMasking", "0x24"] 
    ServiceRequest[stopTransmittingRequestedData]         = ["stopTransmittingRequestedData", "0x25"] 
    ServiceRequest[requestSecurityAccess]                 = ["requestSecurityAccess", "0x27"]
    ServiceRequest[requestCommunicationControl]           = ["requestCommunicationControl", "0x28"]    
    ServiceRequest[requestDiagnosticdataPacket]           = ["requestDiagnosticdataPacket", "0x2A"]   
    ServiceRequest[dynamicallyDefineDiagnosticDataPacket] = ["dynamicallyDefineDiagnosticDataPacket","0x2C"]
    ServiceRequest[writeDataByCommonID]                   = ["writeDataByCommonID","0x2E"]
    ServiceRequest[inputOutputControlByLocalID]           = ["inputOutputControlByLocalID","0x2F"]
    ServiceRequest[startRoutineByLocalIdentifier]         = ["startRoutineByLocalIdentifier","0x31"]    
    ServiceRequest[stopRoutineByLocalIdentifier]          = ["stopRoutineByLocalIdentifier","0x32"]
    ServiceRequest[requestRoutineResultsByLocalID]        = ["requestRoutineResultsByLocalID","0x33"]
    ServiceRequest[requestDownload]                       = ["requestDownload","0x34"]
    ServiceRequest[requestUpload]                         = ["requestUpload","0x35"]
    ServiceRequest[transferData]                          = ["transferData","0x36"]
    ServiceRequest[requestTransferExit]                   = ["requestTransferExit","0x37"]
    ServiceRequest[writeDataByLocalId]                    = ["writeDataByLocalId","0x3B"]
    ServiceRequest[requestReadMemoryBlock]                = ["requestReadMemoryBlock","0x3C"]
    ServiceRequest[writeMemoryByAddress]                  = ["writeMemoryByAddress","0x3D"]
    ServiceRequest[controlDTCSetting]                     = ["controlDTCSetting", "0x85"] 
    ServiceRequest[requestDiagnosticdataPacket]           = ["requestDiagnosticdataPacket", "0xA0"]
    ServiceRequest[dynamicallyDefineDataPacket]           = ["dynamicallyDefineDataPacket", "0xA1"]
    ServiceRequest[noStoredCodesLoggingStateEntry]        = ["noStoredCodesLoggingStateEntry", "0xB0"]
    ServiceRequest[diagnosticCommand]                     = ["diagnosticCommand", "0xB1"]
    ServiceRequest[inputIntegrityTestStateEntry]          = ["inputIntegrityTestStateEntry", "0xB2"]
    ServiceRequest[requestManufacturerStateEntry]         = ["requestManufacturerStateEntry", "0xB4"]
    ServiceRequestSubFunction                             = {}
    ServiceRequestSubFunction[ReturnToOperationalState]   = ["81, ReturnToOperationalState"]
    ServiceRequestSubFunction[standardDiagnosticSession]  = ["83, standardDiagnosticSession"]
    ServiceRequestSubFunction[ecuProgrammingSession]      = ["85, ecuProgrammingSession"]
    ServiceRequestSubFunction[ecuAdjustmentSession]       = ["87, ecuAdjustmentSession"]
    ServiceRequestSubFunction[supplierDiagnosticSession]  = ["FA, supplierDiagnosticSession"]
    ServiceRequestSubFunction[HardReset]                  = ["ecuReset Hard Reset", "0x01"]
    ServiceRequestSubFunction[SoftReset]                  = ["ecuReset Hard Reset", "0x02"]
    # ServiceRequestSubFunction[]                           = [" "]  
    ServiceRequestSubFunction[RequestResponse]            = ["01 Requesst Response"]
    ServiceRequestSubFunction[SuppressResponse]           = ["02 Suppress Response"]

class SecurityAccess0xFA:
    global keygen, fixed, seed, key
    fixed = 0x123456
    def keygen(seed, fixed, key):
        challengeCode = array('Q')
        challengeCode.append(fixed & 0xff)
        challengeCode.append((fixed >> 8) & 0xff)
        challengeCode.append((fixed >> 16) & 0xff)
        challengeCode.append((fixed >> 24) & 0xff)
        challengeCode.append((fixed >> 32) & 0xff)
        challengeCode.append(seed[2])
        challengeCode.append(seed[1])
        challengeCode.append(seed[0])
        temp1 = 0xC541A9
        for i in range(64):
            abit = temp1 & 0x01
            chbit = challengeCode[7] & 0x01
            bbit = abit ^ chbit
            temp2 = (temp1 >> 1) + bbit * 0x800000 & -1
            temp1 = (temp2 ^ 0x109028 * bbit) & -1
            challengeCode[7] = challengeCode[7] >> 1 & 0xff
            for a in range(7, 0, -1):
                challengeCode[a] = challengeCode[a] + (challengeCode[a - 1] & 1) * 128 & 0xff
                challengeCode[a - 1] = challengeCode[a - 1] >> 1
        
        key = [ temp1 >> 4 & 0xff, ((temp1 >> 12 & 0x0f) << 4) + (temp1 >> 20 & 0x0f), (temp1 >> 16 & 0x0f) + ((temp1 & 0x0f) << 4) ]
        return key

