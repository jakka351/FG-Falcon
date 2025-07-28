![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<p align="right">

<img align="right" src="https://user-images.githubusercontent.com/57064943/163706360-f1d8e14a-aabd-40f2-90a0-0cdc0badf70c.png" height="20%" width="20%"/>
	
</p>


# FG Falcon  `FoA Orion`

<a href="https://testerpresent.com.au/"><img src="https://img.shields.io/badge/Tester Present -Specialist Automotive Solutions-blue" /></a>  

***

<sup>
The Ford Falcon is a full-sized car that was produced by Ford Australia from 2008 to 2014. It was the first iteration of the seventh and last generation of the Falcon.
To make a fresh start, Ford Australia decided to revolutionize the designation of all models within the range. In particular, the long-standing Futura, Fairmont, and Fairmont Ghia models were replaced by the more contemporary G6 and G6 E models, respectively. The FG moniker references the now discontinued Fairmont Ghia. The FG was superseded in December 2014, by the FG X series.
https://en.wikipedia.org/wiki/Ford_Falcon_(FG)
<br/></sup>

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/super-roo.png" height="20%" width="20%"/>


## Table of contents 

<table><sup>
<tr>	
<td>

- [Orion CanBus](https://github.com/jakka351/fg-falcon#orion)
- [Module Comms Overview](https://github.com/jakka351/fg-falcon#vehicle-network-layout)
- [CanBus Decoded](https://github.com/jakka351/fg-falcon#canbus-decoded)
- [As Built Data & CanDump logs](https://github.com/jakka351/fg-falcon#asbuilt-data--candump-logs)
- [Software](https://github.com/jakka351/fg-falcon#software)
  - [Community Written](https://github.com/jakka351/fg-falcon#software)   
  - [Forscan](https://github.com/jakka351/fg-falcon#forscan)
  - [OpenXC](https://github.com/jakka351/fg-falcon#fomoco-open-source)
  - [Powertrain](https://github.com/jakka351/fg-falcon#pcm-programming) 
    - [PCM Articles](https://github.com/jakka351/fg-falcon#articles--info-on-pcm-programming)    
    - [Nigel's Guide to Programming the FG Falcon ABS module for a Turbo conversion](https://www.tiperformance.com.au/knowledge-base/programming-the-fg-falcon-abs-module-for-a-turbo-conversion/). 
  - [Interior Command Centre](https://github.com/jakka351/fg-falcon#interior-command-centre---entertainment-system)
      - [ICC Splash Images](https://github.com/jakka351/fg-falcon#interior-command-centre---entertainment-system)  
      - [FGX FoA Wallpapers]()  
  - [Libraries](https://github.com/jakka351/fg-falcon#libraries)  
- [Resources](https://github.com/jakka351/fg-falcon#resources-folder)
- [Guides](https://github.com/jakka351/fg-falcon#guides) 
    - [The Ultimate Guide to Re Coding Fg Module VIN numbers with Forscan](https://github.com/jakka351/FG-Falcon/wiki/The-Ultimate-Guide-to-Coding-FG-Module-VIN-numbers-with-Forscan) 
    - [Instrument CLuster Police Mode](https://github.com/jakka351/FG-Falcon/wiki/Police-Mode)
    - [Enable FPV Logo on the Front Display Interface Module](https://github.com/jakka351/FG-Falcon/wiki/Enable-FPV-Logo-on-ICC)
- [Work Shop Manuals](#workshop-manuals)
    - [List of WSM](https://github.com/jakka351/FG-Falcon/tree/master/resources/wsm)   
    - Added All WSM 81 files 27/11/21  
- [Documents](#Documents)
- [Wiring Diagrams]()
- [Wiki](#wiki)
- [Links, Stores, Misc]()
- [Articles](#Articles)
- [Credit and license](#Credit-and-license)
- [Disclaimer](#Disclaimer)  
	   
</td>
	</tr></sup>
</table>

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<p align="right"> 
<img align="right" src="https://user-images.githubusercontent.com/57064943/163706907-48fcd541-6998-42c8-a673-b33784e09128.png" height="25%" width="25%" /></p>
</p>

# Orion CANBus

<sup> 
Controller Area Network (CAN) bus. This consists of two twisted wires and operates serially (data is transmitted sequentially). It is used for communication between the modules themselves and between the modules and the IDS. The modules are connected to the data bus in parallel. New modules can be incorporated easily, without modifying the other wiring or modules.
The transmitted data is received by every module connected to the Controller Area Network (CAN). As each data packet has an identifier, in which  the priority of the message is determined as well as the content identification, each module can  detect whether or not the data is relevant for its own information processing. This enables several modules to be addressed with a particular data packet and supplied with data simultaneously. For this purpose, it is ensured that important data (for example from the Anti-lock Brake System (ABS)) is transmitted first. The other modules are only 
able to submit their data to the data bus after the high-priority messages have been received. In order to guarantee a high degree of error  protection, two 120 Ohm terminating resistors are installed in the CAN. These are integrated in the first module connected to the CAN and in the  last module connected to the CAN respectively and are used for suppression as well as the elimination of voltage peaks. In order to ensure correct functioning of the data bus system, the modules must always be connected with an integral terminating resistor.   

</sup> <br/><br/>  
 
<p> <br/>
	
`Module Communications Network, 2008 Workshop Manual`  
	
</p>
<img src="https://user-images.githubusercontent.com/57064943/166141713-08ef10eb-26ea-45d1-94ad-ad35968772ff.png" align="right" height="15%" width="20%" />  

# Vehicle Network layout:  
![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<sup>
	
Protocol  | Modules | Speed | [ - - - - Function - - - - - -    ] |
---------|---------|-------|--------|  
   CAN     | AIM, ACM, BEM, BPM, FDIM, IC, PAM            | 125kbps | ICC, Audio, Bluetooth, Ipod, Cluster, Body Electric  |
   CAN     | ABS, DSC, PCM, TCM, RCM, HIM           | 500kbps | Powertrain Comms, ABS, Instrumentation  |
   CAN     | ABS, DSC, SAS, YRS, RCM              | 500kbps | Private-HS-CAN, ABS,DSC,EBA,TCS, Steering Angle Sensor, LPI module to PCM |
   ISO9141 | 6 Speed Trans Manufacturer            | - | Not directly accessible single wire bus  |
   LIN     | BEM to Alarm Link                 | 20kbps | Not directly accessible single wire master slave |  
   EOBD | PCM | 500kbps | Emissions & Diagnostics  |
   UART | AIM/Ipod | - | Apple Accessory Protool       |
   Bluetooth | BPM | - | Serial Port Profile |
   RF Comm | BEM | - | Keyfob |
   Infrared | NAV | Lightspeed! | Navigation Remote mk1 |
  
  </sup>
    

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


Module      | CPU | BUS | DiagSig_Rx  | DiagSig_Tx | Supported Diagnostic Sessions | SecurityAcess Levels |
---------|---------|-------|--------|--------|--------|--------|
AIM | V850 | Midspeed | 0x767 | 0x76F |  |   |
ACM | - |    Midspeed | 0x727| 0x72F |  |   |
BEM | - |    Midspeed | 0x726 | 0x72E |  |  |
BPM | V850  | Midspeed | 0x781 | 0x789 |  |  |
FDIM | V850 | Midspeed | 0x7A6 | 0x7AE |  |  |
IPC | V850  | Midspeed | 0x720 | 0x728 | 0x1081, 0x1087, 0x10FA  | Multiple Secure States, Up to Component Manufacturer State |
ABS | - |  High Speed | 0x766 | 0x76E |  |  |
PAM | - |  Midspeed | 0x736 | 0x73E|  0x1081, 0x1087, 0x10FA  | 0x2701 UnSuppported, module not secured |
PCM | - |  High Speed | 0x7E0 | 0x7E8 |  |  |
TCM | - |  High Speed | 0x7E1| 0x7E9 |   |  |  
HIM | - |  High Speed | 0x733 | 0x73A | |  |
</sup>  

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<img align="right" src="https://user-images.githubusercontent.com/57064943/163755801-ee0254f2-0ae0-42fc-9e42-6eabe058f516.png" height="35%" width="35%" />

## CanBus Decoded:
[`Spreadsheet .PNG`](https://user-images.githubusercontent.com/57064943/147951982-b6c589f0-b3d5-418f-abff-7b50921f7264.png)
			
  **Collection of FG-CAN Data from various sources**
   - [`latest and greatest fg can sheet`](https://github.com/jakka351/FG-Falcon/blob/master/6FPA.xlsx) 
   - [`fg_controller_area_network_latest.xlsx`](https://github.com/jakka351/FG-Falcon/raw/master/fg_controller_area_network_latest.xlsx)    
       - Contains a list of all process identifiers, start of decoding as built data, Mitchell H's CAN Docs, Jakka351's CAN spreadsheet
   ![image](https://user-images.githubusercontent.com/57064943/147952317-6d640d92-753a-4c46-b0a9-75013c3ccc4f.png)

  **CAN .dbc Database File written by** `Jakka351` 
   - [`Reaper from PCMtec forum's HS-CAN DBC file`](https://github.com/jakka351/FG-Falcon/blob/master/reaperpcmtecFORD%20HS%20CAN.dbc)   
   - [`fg_controller_area.dbc`](https://github.com/jakka351/FG-Falcon/raw/master/fg_controller_area.dbc)     
   - [`FG DBC git repo`](https://github.com/jakka351/fgdbc/)  
   - [`CAN Overview`](https://github.com/jakka351/FG-Falcon/wiki/CANB101)  
   
  **FG CAN Spreadsheets & Documents by** [`Mitchell H`]()   
   - [`FG%20CAN%20ID%20List.xlsx`](https://github.com/jakka351/FG-Falcon/blob/master/resources/FG%20CAN%20ID%20List.xlsx)  
   - [`HS-Can spreadsheet`](https://github.com/jakka351/FG-Falcon/raw/master/resources/FG%20HS%20CAN%20Decoded.xlsx)        
   - [`MS-Can spreadsheet`](https://github.com/jakka351/FG-Falcon/raw/master/resources/Low%20Speed%20CAN%20Bus%20decoded%20(Old).xls) 
   - [`FG CAN Document`](https://github.com/jakka351/FG-Falcon/raw/master/resources/CAN%20Codes.docx)

  **FG Falcon High Speed, MidSpeed and Diagnostic CAN Logs taken from Ford FJDS software**
   - [FG Falcon CAN Logs](https://github.com/jakka351/FG-Falcon-CAN-Logs)
 
   [**BA,BF CAN spreadsheet**](https://github.com/jakka351/FG-Falcon/blob/master/resources/BA%20BF%20SX%20SY%20Falcon%20Territory%20CAN-IDs.xlsx)  [`from Lukeyson`](https://forum.pcmtec.com/topic/279-can-messages/)   
   - [`BA,BF CAN spreadsheet`](https://github.com/jakka351/FG-Falcon/blob/master/resources/BA%20BF%20SX%20SY%20Falcon%20Territory%20CAN-IDs.xlsx)
 ![image](https://user-images.githubusercontent.com/57064943/147953425-1da72aa0-6974-447d-aa46-60243a4ff166.png)
   
  
 
   ![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)



   [` Using Savvy can to talk to the Instrument Cluster: YouTube video`](https://youtu.be/SlKu-BrJu_M) 
  
  [![IMAGE](http://img.youtube.com/vi/SlKu-BrJu_M/0.jpg)](http://www.youtube.com/watch?v=SlKu-BrJu_M "SavvyCAN IPC Hacking")  

![image](https://github.com/jakka351/FG-Falcon/assets/57064943/6f356cbe-204d-4f7c-9ca7-f432759b508c)
 
  ![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)
 


<img align="right" src="https://user-images.githubusercontent.com/57064943/165017526-8ecc6cf9-2e2e-43f2-8f25-713441db2dd6.png" height="30%" width="30%"/>

## Module Configuration [As Built Data]    

<p align="left">
    <sup>    
	    
 Diagnostic Services `0x21 readDataByLocalId`, `0x3B writeDataByLocalId` are generally what is used to read and write the `As Built` data. Ford's Diagnostic software IDS & FJDS have the capability to read and write to these memory locations, as does the FORScan software. The Vehicle Identification Number isgenerally at memory location `0x00` on each ECU, and can be read via `readDataByLocalId` with a can message ie `$7A6#0221000000000000` will ask the FDIM for its coded VIN number. To write a VIN you generally need to have had securityAccess granted via a seed & key exchange.</sup></p>   

  
  ### AsBuilt Data Files & Candump Logs:
   [`2009 FG Falcon FPV GS As Built Data`](https://github.com/jakka351/FG-FalconAsBuilt)   
   [`fg fpv 5.4 tr6060 candump log mscan`](https://github.com/jakka351/FG-Falcon/blob/master/resources/candump-2021-01-22_135811.log)   
   [`fg fpv 5.4 tr6060 candump log hscan`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/candump-2021-01-20_205722.log)    
  ### Module Configuration
   - [`Enable FPV Logo on ICC`](https://github.com/jakka351/FG-Falcon/wiki/Enable-FPV-Logo-on-ICC)   
   - [`Enable Reverse Camera`](https://github.com/jakka351/FG-Falcon/wiki/Enable-Reverse-Camera)  
   - [`Police Mode`](https://github.com/jakka351/FG-Falcon/wiki/Police-Mode)      
   - [`The Ultimate Guide to Re Coding Fg Module VIN numbers with Forscan`](https://github.com/jakka351/FG-Falcon/wiki/The-Ultimate-Guide-to-Coding-FG-Module-VIN-numbers-with-Forscan) 
   - [`Ford Wreckers Article on PCM Programming`](https://www.fordwreckers.com.au/powertrain-control-module-programming-ba-bf-fg-ford-falcons/)      
   - [`Activate Police Mode with Socketcan`](https://github.com/jakka351/FG-Falcon/wiki/Activate-Police-Mode-with-Socketcan). 



![image](https://user-images.githubusercontent.com/57064943/132037966-b5bffa27-8b1b-4eef-be3e-53b271d4302e.png)
   
   
   
<br/>


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

## Module Diagnostics

<p align="left">
    <sup>    
    The module diagnostic's on the FGI Falcon are very much aligned to ISO 14230 - KWP2000, however they are Ford Specific and the designated specification that the FGI Falcon was designed to is Ford's CAN Generic Diagnostic Specification v2001/V2003. There are some differences between the ford global specification and the diagnostic services on the vehicle. Beyond the diagnostics of the Ford Motor Company lies the component manufacturer diagnostics. Unknown and not accessible via Ford Diagnostic software, there are unknowns to be found within the vehicleManufacturerSpecific and systemSupplierSpecific diagnostic sessions, accessible on some modules without security access, some with hidden seed & key exchanges - and possibly with CAN Calibration protocol. Some of the component manufacturers are no longer around with respect to this vehicle, (SWSA), some have been renamed (VDO) and some are still around (Bosch). If anyone wants to share their secret documents, feel free to get in touch on ford forums au.
   </sup>
   
   ### ECU Rx/Tx Addressing 
   ![image](https://user-images.githubusercontent.com/57064943/194045888-cc97dc10-b80b-4cc3-a625-2388d0927b49.png)

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)
### CAN Generic Diagnostic Specification - Down Under Version - Mk1 only
Service  | Byte |
---------|---------|
diagnosticSessionControl | 0x10 | 
reportDiagnosticState | 0x50 | 
diagnosticSessionControl standardDiagnosticSession | 0x81 |
diagnosticSessionControl ecuProgrammingSession | 0x85 |
diagnosticSessionControl ecuAdjustmentSession | 0x87 |
diagnosticSessionControl systemSupplierSpecific | 0xFA|
clearDiagnosticInformation | 0x14 | 
readDTCByStatus | 0x18 | 
readDataByLocalID(As Built) | 0x21 | 
readMemoryByCommonID(Data IDentifiers [DID]) | 0x22 | 
readMemoryByAddress(Direct Memory Read[DMR]) | 0x23 | 
requestSecurityAccess | 0x27 | 
reportSecurityAccess | 0x67 | 
writeDataByCommonID(Write DID Memory) | 0x2E | 
inputOutputControlByLocalID (Routine Entry)| 0x2F | 
startRoutineByLocalIdentifier(Ecu Self Test) | 0x31 | 
stopRoutineByLocalIetdentifier | 0x32 | 
requestRoutineResultsByLocalID | 0x33 | 
requestDownload | 0x34 | 
requestUpload | 0x35 | 
transferData | 0x36 | 
requestTransferExit | 0x37 | 
writeDataByLocalId(Write As Built) | 0x3B | 
requestReadMemoryBlock | 0x3C | 
writeMemoryByAddress | 0x3D | 
testerPresent | 0x3E | 
testerPresent RequestResponse | 0x01 | 
testerPresentSuppressResponse | 0x02 | 
controlDTCSetting | 0x85 | 
requestDiagnosticDataPacket | 0xA0 | 
dynamicallyDefineDataPacket | 0xA1 | 
noStoredCodesLoggingStateEntry | 0xB0 | 
diagnosticCommand | 0xB1 | 
inputIntegrityTestStateEntry | 0xB2 | 
requestManufacturerStateEntry | 0xB4 |

### 0x27 requestSecurityAccess - Parking Aid Module  
```
    	//////////////////////////////////////////////////////////////////
        // / 0x736 Parking Aid Module
        // / Seed & Key Procedure
        // / must be in diagnostic mode 85 to get seed
        // /
        // /   Send >> 736$0210850000000000
        // /   Recv << 73E$0250850000000000
        // /   Send >> 736$0227010000000000
        // /   Recv << 73E$0567021122330000
        // /   Send >> 736$0227021122330000
        // /   Recv << 73E$0267020000000000
        // /
        // / 0.000000  736  02 27 01 00 00 00 00 00 .'.......
        // / 0.000000  73E  05 67 01 11 22 33 00 00 .g.."
        // /
        // / Took me one guess to crack the pam seed key procedure.
        // /
        // /  can0  RX - -  73E   [8]  05 67 01 11 22 33 00 00   '.g.."3..'
        // /  can0  TX - -  736   [8]  05 27 02 11 22 33 00 00   '.'.."3..'
        // /  can0  RX - -  73E   [8]  02 67 02 00 00 00 00 00   '.g......'
        //////////////////////////////////////////////////////////////////
        // / Also interesting to note: entering into a systemSupplierSpecific diagnostic session is possible without security access:
        // /  can0  TX - -  736   [8]  02 10 FA 00 00 00 00 00   
        // /  can0  RX - -  73E   [8]  02 50 FA 00 00 00 00 00   
        //////////////////////////////////////////////////////////////////
```
</p>  

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<img align="right" src="https://user-images.githubusercontent.com/57064943/166146149-194cba07-3baa-46d2-b5f0-cfa753d52178.png" height="20%" width="20%"/>


## Firmware

Falcon ECU Firmware related softwares and posts.  

  - [PHF2BIN](https://github.com/rollsch/PHF2BIN) - Converts a Ford  PCM .phf file to a binary image by rollsch  
  - [FG2ICCComms](https://github.com/jakka351/FG2ICCComms) - JasonACT's software tool to re-core the MK2 FDIM  
  -  FG2IPCComms - JasonACT's software tool for flashing firmware and eeprom of the IPC - not available here due to odometer fraud
  - [Barra in a Beamer](https://github.com/jakka351/Barra-in-a-Beamer)
  - [ABS Config Tool made with python for ELM327](https://github.com/jakka351/ABS-Config-ELM327/)
  - [Ford FG Diagnostics Big Python Script](https://github.com/jakka351/python-FG1ECU)
  - [PCMtec development blog](https://pcmhacking.net/forums/viewtopic.php?t=4940)    
  - [BA Falcon Body Module EEPROM](https://pcmhacking.net/forums/viewtopic.php?t=8424)
  - [Barra-BEM python-can script](https://github.com/jakka351/Barra-BEM)   
  - [FG Falcon Instrument Cluster Boot Mode & Firmware Download](https://pcmhacking.net/forums/viewtopic.php?t=8419)  
  - [FG Falcon Restraints Control Module](https://pcmhacking.net/forums/viewtopic.php?t=8425)
  - [FG Falcon Restraints Control Module Repo](https://github.com/jakka351/RestraintsControlModule)
  - [RPM Alarm Hack](https://github.com/jakka351/RpmAlarmHack)
  

    ![image](https://github.com/user-attachments/assets/6cefed94-2994-475a-8782-cb0367ec94e8)

  
<br />
<br />


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

![image](https://github.com/jakka351/FG-Falcon/assets/57064943/d031ee17-7e28-4477-b83a-d3bd6afe6e84)


<img align="right" src="https://user-images.githubusercontent.com/57064943/166145564-bb69cf50-aad1-4aab-aaab-0973dce81a8e.png" align="right" width="15%" height="15%" />
  
## Software
Software Written by owners and enthusiasts. 

Description   | Platform      | Model     | Author
--------|-----------|------------|--------
 [`ICC Can Interface`](https://github.com/jakka351/FG-Falcon/blob/master/resources/software/arduino/ICC_CAN_Interface.ino)  | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)   | FG | [Mitchell H]()
 [`ECU HSCAN Interface`](https://github.com/jakka351/FG-Falcon/blob/master/resources/software/arduino/ECU_HS_CAN_Interface.ino) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)   | FG | [Mitchell H]()       
 [`HVAC CAN Reader`](https://github.com/jakka351/FG-Falcon/blob/master/resources/software/arduino/CANReader.ino) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)  | FG | [Kyle May](https://kylemay.net.au)
 [`HVAC Python GUI`](https://github.com/KyleMay/Ford-FG-ICC/tree/master/Unmaintained/PythonGUI) |  [![image](https://img.shields.io/badge/python-v3.7-blue)](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/pythoncan) | FG |  [Kyle May](https://kylemay.net.au) 
 [`Ford FG ICC Repo`](https://github.com/KyleMay/Ford-FG-ICC) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)   | FG |  [Kyle May](https://kylemay.net.au) 
 [`FG ICC Fork`](https://github.com/Bull3time/Ford-FG-ICC) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)  | FG | Bulletime
 [`FG ICC Fork`](https://github.com/jakka351/Ford-FG-ICC) |  [![image](https://img.shields.io/badge/python-v3.7-blue)](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/pythoncan)| FG |Jakka351
 [`can0swc`](https://github.com/jakka351/can0swc) | [![image](https://img.shields.io/badge/%23-Raspberry%20Pi-red)](https://raspberrypi.org/) | FG | Jakka351
 [`ICC Emulator`](https://github.com/jakka351/ICC) | [![image](https://img.shields.io/badge/%23-Raspberry%20Pi-red)](https://raspberrypi.org/) | FG | Jakka351
 [`Android Climate App`](https://github.com/Goochy12/BA-Falcon-Custom-Climate-Control) | [![images](https://img.shields.io/badge/%23-Android-purple)](https://www.android.com/intl/en_au/)| BA | [Goochy12](https://github.com/Goochy12)
 [`Arduino Climate Code`](https://github.com/nkg-io/arduino-climate) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)   | AU/FG | [Nathaniel](https://github.com/nkg-io/) 
 [`SWC Adapter for Pioneer`](https://github.com/bigevtaylor/arduino-swc) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)   | BA/BF | [bigevtaylor](https://github.com/bigevtaylor/arduino-swc)
 [`SWC Adapter for JVC`](https://github.com/MarkSmithAU/FordBFJVCBridge) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)  | BA/BF | [MarkSmithAU](https://github.com/MarkSmithAU)  
 [`FDIM Controller project`](https://github.com/p1ne/fdim-controller) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)   | Ford | [P1ne](https://github.com/p1ne/fdim-controller)     
 [`CD emulato AUX audio`](https://github.com/ansonl/FordACP-AUX) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)  | Ford | Anson Liu     
 [`CD detailed instruction`](http://ansonliu.com/2017/09/ford-acp-cd-changer-emulator-aux-audio/) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)  | Ford | Anson Liu
 [`MitchellH's C source code`](https://github.com/jakka351/FG-Falcon/blob/master/resources/software/mitchellh.c) | - | FG | Mitchell H
 [`cansend can0 swc commands`](https://github.com/jakka351/FG-Falcon/tree/master/mscan/swc) | Can-Utils | FG | Jakka351
 [`cansend can0 icc commands`](https://github.com/jakka351/FG-Falcon/tree/master/mscan/icc) | Can-Utils | FG | Jakka351
 [`Python-OBDII Ford Reader`](https://github.com/jakka351/python-fordreader)     | OBDII | Ford |
 [`Ford Mustang CAN2CLUSTER Project`](https://github.com/thomastech/CAN2Cluster)    |   | Mustang | https://github.com/thomastech/
 [`FORD EEC-IV diagnostic scanner`](https://github.com/babroval/ford-eec-iv-diagnostic)     |   | Ford | https://github.com/babroval/
 [`Display HVAC info can0hvac.py`](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/jakka351)   | | |
 [`Police Mode Enabler`](https://github.com/jakka351/FG-Falcon/) | Windows | BA-FG  | [Cluster Mods](https://clustermods.com) |
 [`AsBuiltExplorer.exe`](https://github.com/jakka351/fg-python)  | Windows | Ford | Jesse Yeager www.compulsivecode.com |
 [`PodEmu Android Ipod Interface`](https://forum.xda-developers.com/t/app-4-0-3-podmode-connect-ur-android-device-to-iphone-dock-car-audio-interface.2220108/) | Android + AIM | FGI | [`Forum Post`](https://www.fordxr6turbo.com/forum/topic/86337-fg-iphone-connector-to-android/) [`Youtube`](https://www.youtube.com/watch?v=0UgZ8OL72OA) Classic |  
 
![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<br />
# 6HP26 Toolkit

The 6HP26 Toolkit is software for the 6HP26 Transmission Control Module, you can Read and Clear Fault codes, Read and Reset Clutch Wear Learnings and Adaptations, Read and Write the TCM Calibration and Completely Flash the TCM with this software...You can also convert BF to FG and vice versa.

[![Watch the Demo](https://img.youtube.com/vi/wjHF3a5AWUA/0.jpg)](https://youtu.be/wjHF3a5AWUA)





# FoA Orion Comms


<p align="right">

<img align="right" src="https://user-images.githubusercontent.com/57064943/179399073-ce0d1e13-7cf7-4ea7-8484-7afe53d876ca.png" height="20%" width="20%" alt="EFFGEE">

	
</p>




***


<sup>
FoA Orion Comms is a Diagnostic & Firmware Tool for the FG Falcon. It is capable of reading and clearing DTCs, conducting module on demand self tests, and diagnostic tool functions. It can read out the Instrument Cluster EEPROM via the OBD port and it can read, write and edit the firmware of the Powertrain Control Module. Available for purchase from https://facebook.com/testerPresent. 
<br/></sup>

![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/b3856fe1-2d63-47b4-8382-087a95bf2225)




# Features
- Workshop Manual Browser  
- ECU Reboot (Diagnostic Service 0x11 ecuReset)  
- Module On Demand Self Test & Factory End of Line Tests  
- Security Access Menu (Diagnostic Service 0x27 securityAccess)  
- Read and Write Instrument Cluster EEPROM via OBD Port, clone instrument clusters for replacements without having to do PATS  
- Read and Write Powertrain Control Module Flash Memory, Edit Vehicle Identification Number, PCM Cloning for replacement modules  
- VID Block Editor for PCM Firmware, Tyre Size, Diff Ratio, etc etc  
- Return Powertrain Control Module to stock tune, with OEM strategies available for download  
- Read & Clear Diagnostic Trouble Codes, with troubleshooting steps and online DTC look up tool, dictiionary of 15,000 Ford Fault Codes  
- Module VIN Programming done in plain text or hexadecimal input  
- Module Configuration Options  
- Clear Audio Code Error  
- Set the HVAC Display Zone of the Front Display Interface Module  
- Bruteforce Module Security Access Tool  
- Pair Key Fob  
- Reset PCM Learnt Adaptions  
- Fusebox Reference Chart  
- Wheel & tyre reference Chart  
- Globe reference chart  
- J2534 Interface Compatible  

![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/8c47bc32-d117-4bfa-ad3e-ac31af28a188)
![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/cd6ff7ea-9412-4059-b271-23f94fc7c93c)
![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/0b1c0fb2-d76f-458d-8ca5-71c2f3e298b5)
![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/6a20a4af-5322-4ab5-824b-4d7674dfec0c)
![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/d90ee8e7-1c82-4f73-92ac-eba02bfe2805)
![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/0fbdbbe7-ebfd-412c-989d-baf25362a669)
![image](https://github.com/jakka351/FoA-Orion-Comms/assets/57064943/9bd152e0-8f20-4bf8-99d4-fef42771278f)

<img src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/FGCOM.gif" height="100%" width="100%" align="center" /> 

<br />

<a href="https://fb.watch/fQ7c6DWO6V/"><img align="right" src="https://user-images.githubusercontent.com/57064943/192815222-37f1a4ed-14cf-4982-9738-e85218584072.png" height="35%" width="35%" /></a>



### [`FoA Orion - Front Display Interface Module HVAC Zone Tool`](https://facebook.com/testerPresent)  



  - `Set the Display of HVAC Data on the FDIM`
      - `Modifies a location in EEPROM memory within the FDIM allowing the HVAC zone display to be changed`
      - https://www.facebook.com/testerPresent%2Fposts%2Fpfbid02DTRSjXhtuYDz3cnkcUnqvWpgyeUGt2Rt2wX6n3gY2gAe9JTxoSXrYJdUDpinJfs4l
   
        ![image](https://github.com/jakka351/FG-Falcon/assets/57064943/0b3e3863-157e-4820-8f2e-5658788e1b3b)



<img src="hhttps://github.com/jakka351/FG-Falcon/assets/57064943/3014b086-b0ea-4bf9-8b49-e462c6db3bad" height="80%" width="80%" />

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<br />

<a href="https://fb.watch/fQ7c6DWO6V/"><img align="right" src="[https://user-images.githubusercontent.com/57064943/192815222-37f1a4ed-14cf-4982-9738-e85218584072.png](https://user-images.githubusercontent.com/57064943/163706907-48fcd541-6998-42c8-a673-b33784e09128.png)" height="20%" width="20%" /></a>



### [`FoA Orion - Police Mode Enabler`]()  



  - `Enable/Disable Police Mode`
      - `Modifies a location in As Built Data`
![image](https://github.com/jakka351/FG-Falcon/assets/57064943/bb9487d9-db0f-40cf-a593-c62fe85a79d6)


<br />

<a href="https://github.com/jakka351/can0swc"><img align="right" src="https://raw.githubusercontent.com/jakka351/can0swc/main/can0swc.png" height="30%" width="30%" /></a>


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


### [`can0swc`](https://github.com/jakka351/can0swc)  

  - `FG Steering Wheel Controls for Raspberry Pi`
      - Uses python-can library and SPI-CAN interface
      - Emit keypresses which are picked up by Android Auto  

<img src="https://user-images.githubusercontent.com/57064943/164008829-e267f4b3-ce48-440f-863c-020da48f7bca.png" height="50%" width="50%" />

     
<br/>

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<br/>
<a href="https://forscan.org"><img align="right" src="https://forscan.org/images/FORScanLiteAppIconRoundCorners144.png" height="70" width="70" /></a>

### [`Forscan`](https://forscan.org)

Forscan is community built and tested Diagnostic Software for Ford, Lincoln, Mazda Vehicles. It is primarily used by the DIYer and in the modification scene. <a href="https://forscan.org">`https://forscan.org`</a> for more information. Forums at <a href="https://forscan.org/forum/">`https://forscan.org/forum/`</a>.  Forscan is compatible with basic cheap ELM327 OBDII Readers, but a genuine <a href="https://www.boschdiagnostics.com/j2534-faq">J2534</a> interface is the <a href="https://forscan.org/forum/viewtopic.php?f=4&t=867">preferred option.</a>

<br/>
<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/ACM.png" width="50%" height="50%"/>
                                                                                                              
  - [`Australian FORSCAN Users Facebook Group`](https://www.facebook.com/groups/australianforscanusersgroup)  
  - [`Forscan Tutorial`](https://docs.google.com/document/d/1-8dKaS_Spu4Zw4hV_CrKC4tLoP9G8yejqegF1wxIqxY/edit)    
  - [`How to use output control`](https://forscan.org/forum/viewtopic.php?f=6&t=844)      
  - [`Modify Module As-Built Data`](http://www.2gfusions.net/showthread.php?tid=4573)    
  - [`How to access MS CAN bus with modified ELM327`](https://forscan.org/forum/viewtopic.php?f=4&t=4)       
  - [`How to run FORScan on Linux`](https://forscan.org/forum/viewtopic.php?f=4&t=6)          
  - [`Helpful Links`](https://forscan.org/forum/viewtopic.php?f=16&t=4393)     
  - [`Forum Write up - Good introduction to forscan`](http://www.2gfusions.net/showthread.php?tid=4573) `thanks John`  

  <br>
<br/>
<br/>
<br/>
<br/>

<br/>


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<a href="https://openxcplatform.com/"><img align="right" src="https://raw.githubusercontent.com/openxc/openxc-python/master/docs/_static/logo.png" /></a>    
    
### `FoMoCo Open Source`         

  
  - [`OpenXC`](https://openxcplatform.com/)    
  - [`OpenXC on GitHub`](https://github.com/openxc)      
  - [`Ford Developers`](https://developer.ford.com/)    
  - [`OpenXC Background Information`](https://developer.ford.com/pages/openxc)    
  - [`More Background`](http://vi.openxcplatform.com/)    
  - [`Supported Vehicles`](https://docs.google.com/spreadsheets/d/1hOBi9-tFwR1KRFXfeaHTAddwJuSGx5Ir1ET4N2zWAiE/edit#gid=2)    
  - [`Supported Data`](https://docs.google.com/spreadsheets/d/1hOBi9-tFwR1KRFXfeaHTAddwJuSGx5Ir1ET4N2zWAiE/edit#gid=6)  `Falcon is type 8`      
  - [`Smart Windscreen Wiper`](https://github.com/openxc/smart-wiper)    
  - [`Nighttime Forward Collision Warning `](https://github.com/openxc/nightvision)     

  <br/>


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)



<img align="right" src="https://user-images.githubusercontent.com/57064943/166143780-9685fc0f-eeac-4459-9320-abc607407b39.png" height="15%" width="15%"/>
      

<a href="https://pcmtec.com/"><img align="left" src="https://user-images.githubusercontent.com/57064943/163758478-19cf4445-84bc-47fa-ba10-061e6ed70b2e.png" height="45%" width="45%"></img></a>

<br /><br /><br /><br /><br /><br /><br />


PCMTec is Australian Developed PCM Tuning software specifically for FG,FG-X Falcons. Other Ford Models are actively supported. Forums located [here](https://forum.pcmtec.com/)    

-  [`Workshops that use PCMTec`](https://www.pcmtec.com/workshops)  
-  [`Software Demo Download`](https://www.pcmtec.com/demo)  
-  [`Falcon How-To Guides`](https://forum.pcmtec.com/forum/17-falcon-howto-guides/)  
-  [`PCMtec MKII Falcon Dash Emulator`](https://forum.pcmtec.com/topic/821-dash-emulator-for-testing-mft-multi-flash-tune-on-the-bench/)  
-  [`PCMtec development blog`](https://pcmhacking.net/forums/viewtopic.php?t=4940)  
-  [`Functionality that can be added includes:`]()
-  - `Launch Control`
-  - `Flat Foot Shifting in Manual Transmissions - clutch position switch triggers torque reduction while throttle stays open`
-  - `Boost by Gear/Speed`
-  - `Selectable Multi-tune via Cruise Control paddle`
-  - `PCM CustomOS` 

![image](https://user-images.githubusercontent.com/57064943/165012862-df8389c1-2731-417c-ae98-decb2ec7c9a1.png)
![image](https://user-images.githubusercontent.com/57064943/165012881-3bd462ca-6b72-47e1-9bdf-3874d300314b.png)

   
![image](https://github.com/jakka351/FG-Falcon/assets/57064943/d3b99b1d-904b-4c2e-b0a8-795164afe561)



![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


 <br/><img align="right" src="https://store.cansolutions.com.au/wp/wp-content/uploads/2020/07/CB2a.jpg" height="20%" width="20%" />

# [`CANBarra`](https://store.cansolutions.com.au/)    
Australian CanBus Products     
-  [`CANBarra CANBUS Translator`](https://store.cansolutions.com.au/product-category/canbarra-modules/)         
   Converts the CANBUS signals from BA BF FG PCMs for Barra Swapped vehicle
     Outputs : 
     ```
        Tach Output – Programmable from 2-12 cylinder to suit your Application  
        Tach Correction – to fix those minor errors from the Factory  
        Vehicle Speed – programmable to suit most OEM Speedometers  
        Check Engine Lamp Output  
        Engine Over Temperature Lamp Output  
        Oil Pressure Lamp Output (BF Onwards)  
        Alternator Lamp Output (FG Onward)  
     ```


     # Nigel!
   
![image](https://user-images.githubusercontent.com/57064943/166140369-735746f1-e1b8-4c79-b0d2-c1cb314214f5.png)

<br/>
<br/>

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<br/>
<img align="right" src="https://user-images.githubusercontent.com/57064943/163985391-fac33783-dad8-4021-9388-6d9c9c3e8b7e.png" height="35%" width="35%" />

  
# [`Whiteford Tech`](mailto:whitefordtech@outlook.com)

  -  `Ford Falcon BA-FGX and Territory SX-SZII Diagnostics and Module Programming Specialist. `  
  -  `FPV Engine Calibrations`    
  -  `Custom Insrument Cluster Start Up Logos` `AKA Bootsplashes`  
  -  `MKII Custom ICC Gauges and Graphix, GT-F 351 Gauges`  
  -  `Module Configuration & Programming - Feature Enablers - RPM Shift Alarm`
  -  `ZF 6HP26 Programming and Calibrations`
  -  `Firmware updates, upgrades, troubleshooting`
  -  `Barra Conversion Programming Services`
  -  `ICC Programming`
  -  `Passive Anti Theft System pairing and key pairing `
  -  `Odometer Correction for Replacement or Repaired Instrument Clusters BA, BF, FGI, FGII, FG-X`  

#### Contact Jack at WhitefordTech@outlook.com, or message Jack Whiteford on facebook.  

<img src="https://user-images.githubusercontent.com/57064943/163985635-4b60d424-1f77-4cb7-8d1d-d6d7b53e5143.png" height="85%" width="65%" />

# Engineer
   
![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<br/>
<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/barrascan.png" height="35%" width="35%" />

# [`Barra Scan`](BarraScanProgramming) 
Programming and Diagnostics specialist for BA-FGX Falcons, as well as supplier/installer of Kayhan Audio Headunits & audio systems.  
Ford Falcon & Territory  
 - `Remove security/audio code error`
 - `ECU/ICC/BCM swaps`
 - `PATS program`
 - `Mustang, Focus, etc`
![image](https://github.com/user-attachments/assets/c3df9b39-d90d-43c2-9642-ed5151e6a33a)

[https://www.barrascan.net/](https://www.barrascan.net/)  
[`Facebook`](https://www.facebook.com/BarraScanProgramming/)  
[`Instagram`](https://www.instagram.com/barra.scan/) 

  
KEY CUTTING AND PROGRAMMING AVAILABLE FOR MOST POPULAR MAKES AND MODELS!!
NORTH/WEST MELBOURNE

Contact Mick at [barrascan@gmail.com](mailto:barrascan@gmail.com) or 0431 533 262  
![image](https://github.com/user-attachments/assets/6a621a58-967c-4547-a5b5-9183238ff002)



![image](https://github.com/jakka351/FG-Falcon/assets/57064943/efc984e1-7f89-4891-bedf-ebaea389a8f9)


<br/><img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/GTF_SplashScreen.png" height="20%" width="20%" />

 ## ICC Splash Graphics 
 
  - [`FPV Splash`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/Fpv1.jpg)[`Ford ICC Splash`](https://github.com/jakka351/FG-Falcon/blob/master/resources/images/Ford4.jpg)[`FPV Pursuit Splash`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/PursuitSplashScreen.png)  
  - [`GT-F 351 Splash`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/GTF_SplashScreen.png)[`GT Logo`]()[`GS Logo`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/FPV_GS01.jpg)  
  - [`ICC Nav`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/navigationVariant.png)[`ICC NoNav`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/nonNavigationVariant.png)[`ICC Gauges Voltage`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/Background_Volts.png)  
 
  
Thanks to <a href="http://www.fordforums.com.au/showthread.php?t=11479908&page=9">JasonACT</a>
<br/>

<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-1.jpeg" height="30%" width="30%" />
<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-2.jpeg" height="30%" width="30%" />
<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-3.jpeg" height="30%" width="30%" />


## FGX FoA Backgrounds, found hiding on Ford.com.au 


No.   | FGX FoA Backgrounds   
--------|----------- 
Sprint |  [`cars-falconxr6sprint-gallery-trigger-large-1.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-1.jpeg)   
Dashboard | [`cars-falconxr6sprint-gallery-trigger-large-2.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-dashboard.jpeg)   
Engine | [`cars-falconxr6sprint-gallery-trigger-large-3.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-engine.jpeg)   
Headlights | [`cars-falconxr6sprint-gallery-trigger-large-4.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-headlight.jpeg)   
Sprint |  [`cars-falconxr6sprint-gallery-trigger-large-5.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-5.jpeg)   
XR6 Front Grill |  [`cars-falconxr6sprint-gallery-trigger-large-6.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-xr6-front-grill.jpeg)     
Sprint | [`cars-falconxr6sprint-gallery-trigger-large-7.jpeg`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/cars-falconxr6sprint-gallery-trigger-large-7.jpeg) 


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


![Fpv1](https://user-images.githubusercontent.com/57064943/185084769-d269cc72-b46e-4f96-93d8-aa3fab799fca.jpg)


<br/>

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<img align="right" src="https://user-images.githubusercontent.com/57064943/166145564-bb69cf50-aad1-4aab-aaab-0973dce81a8e.png" align="right" width="25%" height="25%" />

## Antilock Braking System  
### ABS Background & Guides  
  - [Nigel's Guide to Programming the FG Falcon ABS module for a Turbo conversion](https://www.tiperformance.com.au/knowledge-base/programming-the-fg-falcon-abs-module-for-a-turbo-conversion/)
  - [PCMtec Forums How-to on ABS Reprogramming](https://forum.pcmtec.com/topic/872-howto-abs-reprogramming/)
  - [PCMtec Forums Second Page with additional information on ABS/PCM Matching](https://forum.pcmtec.com/topic/872-howto-abs-reprogramming/page/2/)

### ABS Software
  - [ABS Config Tool for ELM327 Interface](https://github.com/jakka351/ABS-Config-ELM327/)
  - [ABS C# Windows Form Config Tool](https://github.com/jakka351/AntilockBraking)

### ABS Configuration Options [As Built Data]  
The ABS has a variety of configuration options - these much match up with the vehicle type & the PCM Strategy & Calibration.  
ABS As Built Config Options:  
``` 			       XTSportIG1G2RS            =  0x100401,
                               XTSportIRS                =  0x100501,
                               G6Turbo                   =  0x100601,
                               G6SedanDLPGXTG6G6ESport   =  0x110401,
                               PoliceSedanDLPGXTSport    =  0x110501,
                               UteDLPGREBXR612t          =  0x120402,
                               F6PursultUTE12t4pot       =  0x140102,
                               F6PursultUTE12t6pot       =  0x140202,
                               XT                        =  0x160401,
                               G6SedanDLPGXTStd          =  0x170401,
                               UteI6RDLPGXL34t           =  0x180402,
                               F6Force64potBrakes        =  0x190101,
                               F6Force66potBrakes        =  0x190201,
                               XR6                       =  0x190401,
                               XR6Turbo                  =  0x190601,
                               XR6TurboPolice            =  0x190701,
                               GTForce4pOtBrakes         =  0x200101,
                               GTGTPForces6potBrakes     =  0x200201,
                               XR8                       =  0x200601,
                               XR8Police                 =  0x200701,
                               UteI67DLPG1t              =  0x210402,
                               UteI6                     =  0x220402,
                               G6SedanDLPGXTHDSus        =  0x230401,
                               XTPoliceHDFrontSusandIRS  =  0x230501,
                               XTHDFrontSusandIRS        =  0x230401
```

  

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<br /> 
<img src="https://user-images.githubusercontent.com/57064943/166140705-da5ce4de-3a6c-4a4a-a8df-3c5378c6ea63.png" align="right" height="24%" width="24%" />



## Resources

A lot of stuff that is not listed is contained within the Resources folder. 

```github.com/jakkka351/fg-falcon
resources/
└── software/
|    ├── /
|    │   ├── file1
|    │   └── file2
|    └── folder4
|        ├── file3
|        └── file4
|____
     |
```
<img aligh="centre" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />  


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/gauge_speed_trans.png" height="20%" width="20%"/>

## [Troubleshooting Tips]()    

  
  [![IMAGE](http://img.youtube.com/vi/TRlQQ8DtfMQ/0.jpg)](http://www.youtube.com/watch?v=TRlQQ8DtfMQ "Territory CANbus Comms Issue")  
  `Whiteford saves the day again...`  
  
  - [`Body Elec Module differences MKI/MKII`](https://www.pandgmotors.com.au/uncategorized/ford-falcon-fg1-and-fg2-bcm-differences-and-programming-what-not-to-do/)  
  - [`F6 Miss`](https://www.scannerdanner.com/forum/post-your-repair-questions-here/742-ford-fg-f6-miss.html)  
  - [`Ford Territory CanBus Issue - YouTube Video`](https://www.youtube.com/watch?v=TRlQQ8DtfMQ)    
  - [`Ford Mods Technical Document Archive`](http://www.fordmods.com/ford-technical-documents.html)      
  - [`Ford Mods Forum List`](http://www.fordmods.com/fordmods-tech-f57/)    
  - [`Diagnostics & Maintenance FORScan Forum`](https://forscan.org/forum/viewforum.php?f=6) 
  - [`PCMTec Vehicle Diagnostics Forum`](https://forum.pcmtec.com/forum/18-diagnostics/)
  - [`Perfomance tech CANBus 101`](https://dsportmag.com/the-tech/education/performance-tech-can-bus-101/)
  - [`CAN Bus communication explained in 5 minutes`](https://www.youtube.com/watch?v=PEI5EWSgaRk)
  - [`Understandinng CANBUS faults`](https://www.mechanic.com.au/news/understanding-can-bus-faults/)
  - [`Common CAN faults`](https://www.meridiancableassemblies.com/2021/01/common-can-bus-problems/) 
  -  Hint: You can test the entire CANbus system in an Fg falcon without any tool by checking if the FDIM buttons are functioning correctly. 


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

![image]()



<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/CANBUSCOMAUQUOTE_html_4af13c7f15bbb0da.png" alt="EFFGEE">

## [Workshop Manuals](https://github.com/jakka351/FG-Falcon/tree/master/resources/wsm)     
[Utility to download from ford after purchasing subscription](https://github.com/iamtheyammer/fetch-ford-service-manuals)  
  
  - [`Owners Manual sedan`](https://github.com/jakka351/FG-Falcon/blob/master/resources/E240_MCA_CYS_Sedan_Owner_Manual%20(1).pdf)  
  - [`Owners Manual`](https://github.com/jakka351/FG-Falcon/blob/master/resources/E240_MCA_CYS_Ute_Owner_Manual.pdf)    
  - [`Owners Reference Guide`](https://github.com/jakka351/FG-Falcon/blob/master/resources/FG_Falcon_OM_2010_AU.pdf)    
  - [`Technical notes on the EEC-IV MCU`](https://github.com/jakka351/FG-Falcon/blob/master/resources/eectch98.pdf)  
  - [`Ford Vehicle Communications Manual - Snap On`](https://github.com/jakka351/FG-Falcon/blob/master/resources/AUS_Ford_Vehicle_Communication_Software_Manual.pdf)   
  - [`HVAC Integrated Module bf Bulletin`](https://github.com/jakka351/FG-Falcon/blob/master/resources/TSB%2038%208-10%20Ford%20HIM%20Part%201.pdf)  
  - [`FG ICC MK1.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20ICC%20MK1(1).pdf)  
  - [`FG Powertrain control module.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20Powertrain%20control%20module.pdf)    
  - [`FG ZF 6hp26 6 speed auto.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20ZF%206hp26%206%20speed%20auto.pdf)    
  - [`FG engine I6.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20engine%20I6.pdf)   
  - [`FG engine system general.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20engine%20system%20general.pdf)    
  - [`FG engine v8 4v.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20engine%20v8%204v.pdf)    
  - [`FG ent sys general(1).pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20ent%20sys%20general.pdf)  
  - [`FG fuel chargine and controls turbo.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20fuel%20chargine%20and%20controls%20turbo.pdf)    
  - [`FG fuel system.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20fuel%20system.pdf)    
  - [`FG handles and locks.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20handles%20and%20locks.pdf)    
  - [`FG horn.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20horn.pdf)    
  - [`FG instrument cluster.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20instrument%20cluster.pdf)    
  - [`FG instrument panel and console.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20instrument%20panel%20and%20console.pdf)    
  - [`FG module communications network.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20module%20communications%20network.pdf)    
  - [`FG parking aid.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20parking%20aid.pdf)    
  - [`FG wiring 400 to 419.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20400%20to%20419.pdf)    
  - [`FG wiring 501.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20501.pdf)    
  - [`FG wiring 700-06 conector location views.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20700-06%20conector%20location%20views.pdf)    
  - [`FG wiring 700-7-connector-views.pdf(courtesy @ fordforums.com.au)`](https://github.com/jakka351/FG-Falcon/blob/5249578a72c928d7a21c77b2d8b7d5a108b30a5b/resources/wsm/FG%20wiring%20700_07_Connector%20views_(Courtesy%20of%20FordForumsAustralia).pdf)  
  - [`FG wiring 700.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20700.pdf)    
  - [`FG wiring diagram.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20diagram.pdf)    
  - [`Supplement`](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1884)   
  - [`Module Comms Network`](http://fordforums.com.au/wsmpub/fgii/418-00.html)  
  - [`HVAC General Info`](http://fordforums.com.au/wsmpub/fgfpv50/412-00.html)   
  - [`ICC`](http://fordforums.com.au/wsmpub/fg/413-08.html)  
  - [`Remove ICC Assembly`](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=855)    
  - [`Component View & Location`](http://fordforums.com.au/wsmpub/wire/fgfpv/700-06.html)  
  - [`FG Falcon mkI Workshop Manual` @ FordForums.com.au](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1812)    


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<img align="right" src="https://user-images.githubusercontent.com/57064943/185085150-ba0969d9-1ea4-438d-8c27-4e10c5cf9bba.png" height="20%" width="20%"/>


## Wiring Diagrams & Pinouts                  [![images](https://img.shields.io/badge/Ford-Forums-darkblue)](https://fordforums.com.au/) 
 - [`ICC connector`](https://github.com/jakka351/FG-Falcon/wiki/Interior-Command-Centre)    
 - [`Cruise Control Buttons`](https://github.com/jakka351/FG-Falcon/wiki/Cruise-Control)  
 - [`Interior Fusebox Diagram`](https://github.com/jakka351/FG-Falcon/wiki/Interior-Fuse-Pinout)
 - [`Engine Bay Fuse Diagram`](https://github.com/jakka351/FG-Falcon/wiki/Engine-Bay-Fuse-Pinout)  
 - [`Audio Interface Module`](https://github.com/jakka351/FG-Falcon/wiki/Audio-Interface-Module)   
 - [`Bluetooth & Phone`](https://github.com/jakka351/FG-Falcon/wiki/Bluetooth)  
 - [`Diagnostic Port`](https://github.com/jakka351/FG-Falcon/wiki/Diagnostic-Port)  
 
 ### Diagnostic Port Pinout
![image](https://user-images.githubusercontent.com/57064943/199874632-1ebbcc49-a360-4226-b33a-c23fb95c0300.png)

 ### Engine Bay Fuse

![eng_bay_fuse](https://user-images.githubusercontent.com/57064943/185084553-fc54860a-c0b6-4d33-9529-0b25f569894c.png)

### Audio Interface Module Plug  
![image](https://user-images.githubusercontent.com/57064943/199873835-47d07223-4919-413a-980f-9b7014e14583.png)

### Schematic  
![image](https://user-images.githubusercontent.com/57064943/199874247-d7f259e4-ef1c-4dad-8ba4-de07b7e31f1b.png)




![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<img align="right" src="https://user-images.githubusercontent.com/57064943/179399073-ce0d1e13-7cf7-4ea7-8484-7afe53d876ca.png" height="20%" width="20%" alt="EFFGEE">

  
## [Wiki](https://github.com/jakka351/FG-Falcon/wiki)  
  - [Audio Interface Modules](https://github.com/jakka351/FG-Falcon/wiki/Audio-Interface-Module)  
  - [Bluetooth Phone Module](https://github.com/jakka351/FG-Falcon/wiki/Bluetooth-&-Phone)     
  - [Diagnostic Port Pinout](https://github.com/jakka351/FG-Falcon/wiki/Diagnostic-Port)  
  - [Engine Bay Fuse Pinout](https://github.com/jakka351/FG-Falcon/wiki/Engine-Bay-Fuse-Pinout)  
  - [Interior Command Centre Plugs](https://github.com/jakka351/FG-Falcon/wiki/Interior-Command-Centre)  
  - [Cabin Fusebox Pinout](https://github.com/jakka351/FG-Falcon/wiki/Interior-Fuse-Pinout)  
  - [Police Mode](https://github.com/jakka351/FG-Falcon/wiki/Police-Mode)  
  - [SWC Media Controls](https://github.com/jakka351/FG-Falcon/wiki/Steering-Wheel-Media-Controls)  
  
  
![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<img align="right" src="https://user-images.githubusercontent.com/57064943/179386128-bda7f254-c358-4428-95cc-6d8ced575978.png" height="20%" width="20%"/>

  
## Articles  

 - [`Bullet Performance Racing's Technical Archive`](http://www.bpracing.com.au/Technical.html)    
 - [`Ford Spanish & Silver Oak PCM Processor Info from BPR`](https://www.bulletperformanceracing.com.au/PPC-Hardware.html)  
 - [`SocketCAN Setup for Raspberry Pi`](https://github.com/jakka351/FG-Falcon/wiki/Socketcan-Setup-Raspberry-Pi)
 - [`JasonACT's Ford Forums Thread on the failing mkII ICC`](https://www.fordforums.com.au/showthread.php?t=11479908&page=15)  `Recommended Reading`
 - [`FG Github Wiki`](https://github.com/jakka351/FG-Falcon/wiki)   
 - [`Benny Ryan's Aussie Tech Blog - https://benryanau.wordpress.com/`](https://benryanau.wordpress.com/)    
 - [`Playing with Socketcan`](https://dayba.wordpress.com/2017/05/25/playing-with-socketcan-using-can-utils/)  
 - [`Infrared Communication Introduction`](https://www.sbprojects.net/knowledge/ir/) - `sbprojects.net`
 - [`iDoka's Awesome CANBUS`](https://github.com/iDoka/awesome-canbus) - `A curated list of awesome tools, hardware and resources for CAN bus.` 
 - [`iDoka's Awesome LINBUS`](https://github.com/iDoka/awesome-linbus)
 - [`iDoka's Awesome CAN ID`](https://github.com/iDoka/awesome-automotive-can-id)
 - [`SocketCAN Demo Programs`](https://github.com/zhanglongqi/socketcan-demo)
 - [`Socketcan C example software`](https://github.com/craigpeacock/CAN-Examples)
 - [`CANBus Gist`](https://gist.github.com/jackm/f33d6e3a023bfcc680ec3bfa7076e696) - `CAN Tools and Software List `
 - [`MCP2515 data sheet`](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)
 - [`Raspberry Pi PiCAN2 hat`](https://www.elektormagazine.com/news/pican-2-can-bus-board-for-raspberry-pi)    
 - [`Arduino CAN-Bus shield`](https://wiki.seeedstudio.com/CAN-BUS_Shield_V2.0/)  
 - [`Generic MCP2515 SPI board`](https://canbus.com.au/store-7/?model_number=mcp2515-sas)      
 - [`CANBUSv1`](https://github.com/DefinitiveDiagnosis-hub/CANBUSv1) - `training module `   
 
 
![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<a href="https://www.fordforums.com.au/"><img src="https://www.fordforums.com.au/banners/AFF_fordforums_banner.jpg" /></a><br/>  


![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)



<img align="right" src="https://user-images.githubusercontent.com/57064943/179386094-be411b38-93c1-4c9e-adc0-8685940acc3e.png" height="20%" width="20%"/>

  
## Sites, Stores & Forums
 [`Ford Forums AU`](https://fordforums.com.au/)   
 [`XR6 Turbo Forums`](https://www.fordxr6turbo.com/)  
 [`The Ford Modifications Website - fordmods.com`](https://fordmods.com)    
 [`Oz Falcon`](https://http://www.ozfalcon.com.au/)   
 [`Tester Present - Specialist Automotive Solutions`](https://testerpresent.com.au)  
 [`Whiteford Tech`](https://www.facebook.com/pages/category/Product-service/Whiteford-Tech-168145224027606/) - `Engineer`   
 [`Barra Scan`](BarraScanProgramming)   
 [`CAN Solutions`](https://cansolutions.com.au/)  
 [`PCMtec`](https://pcmtec.com)  
 [`Cluster Mods`](http://clustermods.com/index.php)     
 [`Fermec - ECU software and programming`](https://www.facebook.com/profile.php?id=100057603993203&mibextid=9R9pXO)    
 [`Matt's Ford Audio Page`](https://www.facebook.com/fordaudio)       
 [`ASL Automedia`](https://www.aslautomedia.com.au/)        
 [`MackiElec Industries`](https://mackielecindustries.com.au)     
 [`Hooton's Harnesses`](https://www.facebook.com/hootonsharnesses)  
 [`TI Performance`](https://www.tiperformance.com.au/vehicle/fg-falcon/)  
 [`Bullet Performance Racing`](http://www.bpracing.com.au/)    
 [`XR6 Turbo Developments`](https://www.xr6turbodevelopments.com.au/)    
 [`Australian FORScan Users Group`](https://www.facebook.com/groups/344706629955641/)   
 [`PCM Hacking Forums`](https://pcmhacking.net/forums/)  
 [`Injectronics`](https://injectronics.com.au)  
 [`FG Mods`](https://fgmods.com.au/) `Please double check any technical advice gotten from here, as this is more of an art project than a modification website`   
 [`Kayhan Audio`](https://aslautomedia.com.au)  
  
![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)


<img align="right" src="https://user-images.githubusercontent.com/57064943/179386244-7448da08-78d2-4e8d-918d-25340bf2ca78.png" height="20%" width="20%"/>


## Credit & License 
Note: The license referenced at the top only covers this readme file, persons listed below may have other applicable licenses in their works that are linked from here.
 - [`Kyle May`](https://www.kylemay.net.au/)   
 - [`Bull3time`](https://github.com/Bull3time)  
 - [`Mitchell H`](https://fordforums.com.au/member.php?u=2315299)
 - [`JasonACT`](https://www.fordforums.com.au/member.php?u=2479267)  
 - [`MRFGXR6`](http://fordforums.com.au/member.php?u=25234)  
 - [`XR6 ICC Replacement`](https://fordforums.com.au/showthread.php?t=11475851)    
 - [`ICC Replacement`](https://fordforums.com.au/showthread.php?p=6521457#post6521457)  
 - [`Ford Forums Australia`](https://fordforums.com.au)      
 - [`Ford of Australia`](https://ford.com.au)  

![image](https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png)

<img align="right" src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/images/gauge_temp_trans.png" height="20%" width="20%"/>

## Contributors
For queries, concerns, submissions, etc please message on fordforums.com.au.    
[`Jakka351`](https://github.com/jakka351)      
[`GokhanDeveloper`](https://github.com/gokhandeveloper)    
   

[`Feel free to Donate if you want the repository to keep expanding.`](https://www.paypal.com/donate/?hosted_button_id=DK2C5T7HS3U5W)

  
`pew.`  `pewpew.` 


## Grandad
![image](https://github.com/jakka351/FG-Falcon/blob/master/resources/Messenger_creation_83543882-E56C-441C-88ED-F47D1EE02BC7.jpeg)

Thanks to Catherine for supplying images of the Grandfather of the FG....the AU Falcon. 




## Twilight  
As these cars age and slowly fade away, hopefully this archive allows people to keep them alive for as long as possible...    


  
<img src="https://user-images.githubusercontent.com/57064943/163714778-8598c24a-6ae2-49f6-ba4c-42de94dfa025.png" align="center" />

<img align="right" src="https://github-production-user-asset-6210df.s3.amazonaws.com/57064943/254874402-88b6051a-9cbc-4413-8b0c-10994126dd5c.png" height="20%" width="20%"/>

## Disclaimer & Legal Notice
#### Modifying any system on a vehicle may have unforseen consequences. All of the information contained here has been collated from various sources and may not be  accurate, this is a permanent work in progress and common sense should be used. This github is not affiliated with Ford Australia in any way. All information has been sourced from publically available documents, or created by the listed persons.  

   
  ![image](https://github.com/jakka351/FG-Falcon/assets/57064943/58fa4e17-c96e-4c5c-a152-50c40d4e8781)


![TesterPresentNewBusinessCard](https://github.com/user-attachments/assets/e753d9dd-95e4-4608-9d54-19f8eda3d6cc)


