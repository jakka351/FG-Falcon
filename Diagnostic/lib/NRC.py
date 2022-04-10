
# CAN Generic Diagnostic Specification v2003
# https://github.com/jakka351/6FPA-util
'''
 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         6FPAAAJGSW          FGI Diagnostic Parser'''
class Nrc:
    global NegativeResponseCode
    generalReject                                         = 0x10
    serviceNotSupported                                   = 0x11
    subFunctionNotSupported                               = 0x12
    responseTooLong                                       = 0x14
    busyRepeatRequest                                     = 0x21
    conditionsNotCorrect                                  = 0x22
    requestSequenceError                                  = 0x24
    requestOutOfRange                                     = 0x31
    securityAccessDenied                                  = 0x33
    invalidKey                                            = 0x35
    exceedNumberOfAttempts                                = 0x36
    requiredTimeDelayNotExpired                           = 0x37
    uploadDownloadNotAccepted                             = 0x70
    generalProgrammingFailure                             = 0x72
    requestCorrectlyReceived_ResponsePending              = 0x78
    subFuncionNotSupportedInActiveSession                 = 0x7E
    serviceNotSupportedInActiveSession                    = 0x7F
    rpmTooHigh                                            = 0x81
    rpmTooLow                                             = 0x82
    engineIsRunning                                       = 0x83
    engineIsNotRunning                                    = 0x84
    shifterLeverNotInPark                                 = 0x90
    
    NegativeResponseCode                                  = {}
    NegativeResponseCode[generalReject]                   = ["GR", "General Reject"]
    NegativeResponseCode[serviceNotSupported]             = ["SNS", "Service Not Supported"]
    NegativeResponseCode[subFunctionNotSupported]         = ["SFNS", "Subfunction Not Supported: Service exists but not supported by subfunction"]
    NegativeResponseCode[responseTooLong]                 = ["RTL", "Response Too Long"]
    NegativeResponseCode[busyRepeatRequest]               = ["BRR", "Busy Repeat Request"]
    NegativeResponseCode[conditionsNotCorrect]            = ["CNC", "Conditions Not Correct"]
    NegativeResponseCode[requestSequenceError]            = ["RSE", "Request Sequence Error: Server expectes different sequence of request messages"]
    NegativeResponseCode[requestOutOfRange]               = ["ROOR", "Request of out Range: There exists a parameter which is out of range"]
    NegativeResponseCode[securityAccessDenied]            = ["SAD", "Security Access Denied: Either 1) Test conditions not met 2) invalid sequence (try DiagSession) 3) requires unlocking of server"]
    NegativeResponseCode[invalidKey]                      = ["IK", "Invalid Key"]
    NegativeResponseCode[exceedNumberOfAttempts]          = ["ENOA", "Exceeded Number of Security Access Attempts"]
    NegativeResponseCode[requiredTimeDelayNotExpired]     = ["RTDNE", "Required Time Delay Not Expired: Client attempting to access security too quickly"]
    NegativeResponseCode[uploadDownloadNotAccepted]       = ["UDNA", "Upload / Download Not Accepted"]
    NegativeResponseCode[generalProgrammingFailure]       = ["GPF", "General Programming Failure"]
    NegativeResponseCode[requestCorrectlyReceived_ResponsePending] = ["RCRRP", "Request Correctly Received Response Pending: Wait for response"]
    NegativeResponseCode[subFuncionNotSupportedInActiveSession]    = ["SFNSIAS", "Subfunction Not Supported in Active Session"]
    NegativeResponseCode[serviceNotSupportedInActiveSession]       = ["SNSIAS", "Service Not Supported"]
   
   