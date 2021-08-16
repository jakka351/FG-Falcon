<p align="center">
  <a href="https://canbus.com.au/">
    <img src="https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/CANBUSCOMAUQUOTE_html_4af13c7f15bbb0da.png" alt="EFFGEE">
  </a>

  <h3 align="center">FG-Falcon</h3>
   
  <p align="center">
    <a href="https://canbus.com.au"><img src="https://img.shields.io/badge/%23-Contact-maroon" /></a> | 
    <a href="https://github.com/jakka351/fg-falcon/wiki"><img src="https://img.shields.io/badge/FG-Wiki-purple" /></a> | 
    <a href="https://fordforums.com.au/"><img src="https://img.shields.io/badge/Ford-Forums-blue" /></a> | 
    <a href="https://canbus.com.au/"><img src="https://img.shields.io/badge/canbus-.com.au-red" /></a> | 
    <a href="https://cansolutions.com.au/"><img src="https://img.shields.io/badge/Barra-Swapped%3F-lightgrey" /></a>  </p>
      <p align="center">
    <a href="https://github.com/jakka351/FG-Falcon/wiki">Collection of resources relating to electrical and mechanical systems of the FG Falcon.</a>  
    <br>
  </p>
</p>

## Table of contents
- [Orion CanBus](#Orion)
- [Powertrain](#PowerTrain)
- [InteriorCommandCentre](#InteriorCommandCentre)
- [InstrumentCluster](#InstrumentCluster)
- [Software](#Software)
  - [Forscan](#Forscan)
  - [OpenXC](#OpenXC)
  - [Community](#Community)
  - [Libraries](#Libraries)
  - [Guides](#Guides)
- [Work Shop Manuals](#workshop-manuals)
- [Documents](#Documents)
- [Wiring Diagrams]()
- [Links, Stores, Misc]()
- [Articles](#Articles)
- [Credit and license](#Credit-and-license)
- [Disclaimer](#Disclaimer)

## Orion 

   There are significant changes between the BF, FG, FGII and FG-X models. Most of these documents are referring to the mark I fg. In a nutshell the communications layers for 2008-2011 are as follows:
     <p align="center">
### Vehicle Network layout:
Bus      | Modules | Speed | Function  
---------|---------|-------|--------  
   CAN     | AIM, ACM, BEM, BPM, FDIM, IC, PAM | 125kbps | ICC, Audio, Bluetooth, Ipod, Cluster, Body Electric  
   CAN     | ABS, DSC, PCM, TCM, RCM, HIM | 500kbps | Powertrain Comms, ABS, Instrumentation  
   CAN     | ABS, DSC, TSC | 500kbps | Private-HS-CAN, ABS,DSC,EBA,TCS, Steering Angle Sensor, LPI module to PCM where fitted  
   ISO9141 | 6 Speed Trans Man | - | Not directly accessible single wire bus  
   LIN     | BEM to Alarm Link | 20kbps | Not directly accessible single wire master/slave  
   OBDII   | EOBD | - | Emissions & Diagnostics  
  </p>

## CanBus Decoded:

  Collection of FG-CAN Data from various sources 
   - [`fg_controller_area_network_latest.xlsx`](https://github.com/jakka351/FG-Falcon/raw/master/fg_controller_area_network_latest.xlsx)    
       - Contains a list of all process identifiers, start of decoding as built data, Mitchell H's CAN Docs, Jakka351's CAN spreadsheet
   
  CAN .dbc Database File written by `Jakka351` 
   - [`fg_controller_area.dbc`](https://github.com/jakka351/FG-Falcon/raw/master/fg_controller_area.dbc)     
   - [`FG DBC git repo`](https://github.com/jakka351/fgdbc/)  
   
  FG CAN Spreadsheets & Documents by [`Mitchell H`]()   
   - [`FG%20CAN%20ID%20List.xlsx`](https://github.com/jakka351/FG-Falcon/blob/master/resources/FG%20CAN%20ID%20List.xlsx)  
   - [`HS-Can spreadsheet`](https://github.com/jakka351/FG-Falcon/raw/master/resources/FG%20HS%20CAN%20Decoded.xlsx)        
   - [`MS-Can spreadsheet`](https://github.com/jakka351/FG-Falcon/raw/master/resources/Low%20Speed%20CAN%20Bus%20decoded%20(Old).xls) 
   - [`FG CAN Document`](https://github.com/jakka351/FG-Falcon/raw/master/resources/CAN%20Codes.docx)    
 
   [BA,BF CAN spreadsheet](https://github.com/jakka351/FG-Falcon/blob/master/resources/BA%20BF%20SX%20SY%20Falcon%20Territory%20CAN-IDs.xlsx)  [`from Lukeyson`](https://forum.pcmtec.com/topic/279-can-messages/)   
   - [`BA,BF CAN spreadsheet`](https://github.com/jakka351/FG-Falcon/blob/master/resources/BA%20BF%20SX%20SY%20Falcon%20Territory%20CAN-IDs.xlsx)
 
  ## AsBuilt Data & Candump Logs:
   - [`2009 FG Falcon FPV GS As Built Data`](https://github.com/jakka351/FG-FalconAsBuilt)        |  | 
   - [`fg fpv 5.4 tr6060 candump log mscan`](https://github.com/jakka351/FG-Falcon/blob/master/resources/candump-2021-01-22_135811.log)  |  |    
   - [`fg fpv 5.4 tr6060 candump log hscan`](https://raw.githubusercontent.com/jakka351/FG-Falcon/master/resources/candump-2021-01-20_205722.log) |  |     


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
 [`Instrument Cluster ReadFlash.ino`](https://github.com/jakka351/FG-Falcon/blob/master/resources/software/arduino/ReadFlash.ino.txt) | [![image](https://img.shields.io/badge/%23-Arduino-lightgrey)](https://arduino.cc/)  | FGII | [JasonACT]()  
 [`FG-MKII-ICC-Firmwares`](https://github.com/Jasoroony/Ford-Falcon-FG-MKII-ICC-Firmwares) | [QNX]() | FGII | [JasonACT]()
 [`JasonACT's FF Uploads`]() | [![images](https://img.shields.io/badge/Ford-Forums-darkblue)](https://fordforums.com.au/) | FG/FGII/FGX | [JasonACT]()
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



## Forscan
<p align="center">
<img src="https://forscan.org/images/FORScanLiteAppIconRoundCorners144.png" height="50" width="50" />  
  </p>
Forscan is community built and tested Diagnostic Software for Ford, Lincoln, Mazda Vehicles. It is primarily used by the DIYer and in the modification scene. https://forscan.org for more information. Forums at https://forscan.org/forum/.  Forscan is compatible with basic cheap ELM327 OBDII Readers, but a genuine [J2534](https://www.boschdiagnostics.com/j2534-faq) interface is the [preferred option](https://forscan.org/forum/viewtopic.php?f=4&t=867).   

  - [`Australian FORSCAN Users Facebook Group`](https://www.facebook.com/groups/australianforscanusersgroup)  
  - [`Forscan Tutorial`](https://docs.google.com/document/d/1-8dKaS_Spu4Zw4hV_CrKC4tLoP9G8yejqegF1wxIqxY/edit)    
  - [`How to use output control`](https://forscan.org/forum/viewtopic.php?f=6&t=844)      
  - [`Modify Module As-Built Data`](http://www.2gfusions.net/showthread.php?tid=4573)    
  - [`How to access MS CAN bus with modified ELM327`](https://forscan.org/forum/viewtopic.php?f=4&t=4)       
  - [`How to run FORScan on Linux`](https://forscan.org/forum/viewtopic.php?f=4&t=6)          
  - [`Helpful Links`](https://forscan.org/forum/viewtopic.php?f=16&t=4393)    
  
  <br>
   
## FoMoCo Open Source         
   <p align="center">  
 ![image](https://raw.githubusercontent.com/openxc/openxc-python/master/docs/_static/logo.png)      
  </p>  
  
  - [`OpenXC`](https://openxcplatform.com/)    
  - [`OpenXC on GitHub`](https://github.com/openxc)      
  - [`Ford Developers`](https://developer.ford.com/)    
  - [`OpenXC Background Information`](https://developer.ford.com/pages/openxc)    
  - [`More Background`](http://vi.openxcplatform.com/)    
  - [`Supported Vehicles`](https://docs.google.com/spreadsheets/d/1hOBi9-tFwR1KRFXfeaHTAddwJuSGx5Ir1ET4N2zWAiE/edit#gid=2)    
  - [`Supported Data`](https://docs.google.com/spreadsheets/d/1hOBi9-tFwR1KRFXfeaHTAddwJuSGx5Ir1ET4N2zWAiE/edit#gid=6)  `Falcon is type 8`      
  - [`Smart Windscreen Wiper`](https://github.com/openxc/smart-wiper)    
  - [`Nighttime Forward Collision Warning `](https://github.com/openxc/nightvision)     

  
  
***



 ## PCM Programming    
   
 [<img src="https://pcmtec.com/Plugins/Payments.Pcmtec/assets/dist/img/logo-horizontal.png" height="22" width="120"></img>](https://pcmtec.com/)   
 
    - PCMTec is Australian Developed PCM Tuning software specifically for FG,FG-X Falcons. Other Ford Models are actively supported. Forums located at https://forum.pcmtec.com/  
 
 
 [CAN Solutions](https://store.cansolutions.com.au/)    
     Australian CanBus Products         
      -  [`CANBarra CANBUS Translator`](https://store.cansolutions.com.au/product-category/canbarra-modules/)         
       converts the CANBUS signals from BA BF FG PCMs for Barra Swapped vehicles  `    
       
## Articles & Info on PCM Programming
  -  [`Ford Wreckrs Article on PCM Programming`](https://www.fordwreckers.com.au/powertrain-control-module-programming-ba-bf-fg-ford-falcons/)      
  -  [`ABS Reprogramming on PCMTec forums`](https://forum.pcmtec.com/topic/872-howto-abs-reprogramming)  
  -  [`Bosch J2534 FAQ`](https://www.boschdiagnostics.com/j2534-faq)  
  
  
  
## Resources Folder

A lot of stuff that is not listed is contained within the Resources folder. 

```github.com/jakkka351/fg-falcon
resources/
└── folder2/
    ├── folder3/
    │   ├── file1
    │   └── file2
    └── folder4/
        ├── file3
        └── file4
```

## Libraries  
  [`(KIVY installation aid)`](https://github.com/techcoder20/RPI-Kivy-Installer)    
  [`Generic PythonCAN`](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/pythoncan)   
  [`mcp2515 can library`](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/arduino/MCP2515)   
  [`Seeed Arduino MCP2515 Lib`](https://github.com/Seeed-Studio/Seeed_Arduino_CAN)     

## [Workshop Manuals](https://github.com/jakka351/FG-Falcon/tree/master/resources/wsm)   
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
  - [`FG wiring 700.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20700.pdf)    
  - [`FG wiring diagram.pdf`](https://github.com/jakka351/FG-Falcon/blob/master/resources/wsm/FG%20wiring%20diagram.pdf)    
  - [`Supplement`](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1884)   
  - [`Module Comms Network`](http://fordforums.com.au/wsmpub/fgii/418-00.html)  
  - [`HVAC General Info`](http://fordforums.com.au/wsmpub/fgfpv50/412-00.html)   
  - [`ICC`](http://fordforums.com.au/wsmpub/fg/413-08.html)  
  - [`Remove ICC Assembly`](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=855)    
  - [`Component View & Location`](http://fordforums.com.au/wsmpub/wire/fgfpv/700-06.html)  
  - [`FG Falcon mkI Workshop Manual` @ FordForums.com.au](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1812)    

## Wiring Diagrams & Pinouts                  [![images](https://img.shields.io/badge/Ford-Forums-darkblue)](https://fordforums.com.au/) 
 - [`ICC connector`](https://github.com/jakka351/FG-Falcon/wiki/Interior-Command-Centre)    
 - [`Cruise Control Buttons`](https://github.com/jakka351/FG-Falcon/wiki/Cruise-Control)  
 - [`Interior Fusebox Diagram`](https://github.com/jakka351/FG-Falcon/wiki/Interior-Fuse-Pinout)
 - [`Engine Bay Fuse Diagram`](https://github.com/jakka351/FG-Falcon/wiki/Engine-Bay-Fuse-Pinout)  
 - [`Audio Interface Module`](https://github.com/jakka351/FG-Falcon/wiki/Audio-Interface-Module)   
 - [`Bluetooth & Phone`](https://github.com/jakka351/FG-Falcon/wiki/Bluetooth)  
 - [`Diagnostic Port`](https://github.com/jakka351/FG-Falcon/wiki/Diagnostic-Port)  
  
## Articles  
 - [`SocketCAN Setup for Raspberry Pi`](https://github.com/jakka351/FG-Falcon/wiki/Socketcan-Setup-Raspberry-Pi)
 - [`Aftermarket Gauges`](https://github.com/jakka351/FG-Falcon/wiki/Installing-Aftermarket-Gauges-in-vehicles-that-transmit-sensor-data-over-CAN)
 - [`Police Mode`](https://github.com/jakka351/FG-Falcon/wiki/Police-Mode)
 - [`JasonACT's Ford Forums Thread on the failing mkII ICC`](https://www.fordforums.com.au/showthread.php?t=11479908&page=15)  `Recommended Reading`
 - [`FG Github Wiki`](https://github.com/jakka351/FG-Falcon/wiki)   
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
  
## Sites, Stores & Forums
 [`Ford Forums AU`](https://fordforums.com.au/)   
 [`XR6 Turbo Forums`](https://www.fordxr6turbo.com/)  
 [`The Ford Modifications Website - fordmods.com`](https://fordmods.com)    
 [`Oz Falcon`](https://http://www.ozfalcon.com.au/)  
 [`Cluster Mods`](http://clustermods.com/index.php)    
 [`FG Mods`](https://fgmods.com.au/)  
 [`Specialist Automotive Service | CANBus.com.au`](https://canbus.com.au/)      
 [`Matt's Ford Audio Page`](https://www.facebook.com/fordaudio)   `Bluetooth Audio Kits for FG`      
 [`ASL Automedia`](https://www.aslautomedia.com.au/)     
    ` OEM Replacement Parts for FG ICC  `  
## Credit & License 
 - [`Kyle May`](https://www.kylemay.net.au/)   
 - [`Bull3time`](https://github.com/Bull3time)  
 - [`Mitchell H`](https://fordforums.com.au/member.php?u=2315299)
 - [`JasonACT`](https://www.fordforums.com.au/member.php?u=2479267)  
 - [`MRFGXR6`](http://fordforums.com.au/member.php?u=25234)  
 - [`XR6 ICC Replacement`](https://fordforums.com.au/showthread.php?t=11475851)    
 - [`ICC Replacement`](https://fordforums.com.au/showthread.php?p=6521457#post6521457)  
 - [`Ford Forums Australia`](https://fordforums.com.au)      
  

## Contact  
Any queries, concerns, submissions, etc's email service@canbus.com.au. Nope, you cannot list your product here, unless you can demostrate that it actively contributes to the community that buys it.  
 
## Disclaimer 
#### Modifying any system on a vehicle may have unforseen consequences. All of the information contained here has been collated from various sources and may not be  accurate, this is a permanent work in progress and common sense should be used. This github is not affiliated with Ford Australia in any way. All information has been sourced from publically available documents, or created by the listed persons.

***
[![image](https://canbus.com.au/tiki-download_file.php?display&fileId=48)](https://canbus.com.au)

***
