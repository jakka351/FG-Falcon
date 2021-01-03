 # FG-Falcon-specific #
![image](https://www.independentmotorsports.com.au/assets/images/Ford/Ford%20Coyote/FG_FGX%20Coyote%20banner.png)  
[Collection of resources relating to electronic and mechanical systems of the FG Falcon.](https://github.com/jakka351/FG-Falcon/wiki)  

# Software  ![image](https://img.shields.io/badge/FG-Falcon-blue) ![image](https://img.shields.io/badge/mkI-mkII-lightblue) ![image](https://img.shields.io/badge/%23-Raspberry%20Pi-red) ![image](https://img.shields.io/badge/%23-Arduino-lightgrey) ![image](https://img.shields.io/badge/%23-Forscan-lightblue) ![image](https://img.shields.io/badge/github-can0swc-yellowgreen) ![image](https://img.shields.io/badge/cansend-can0-orange) [![GitHub issues](https://img.shields.io/github/issues/jakka351/FG-Falcon?style=social)](https://github.com/jakka351/FG-Falcon/issues)  
**FG Specific Arduino Sketches**   
 - [ICC Can Interface](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino)  
 - [ECU HSCAN Interface](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino)      
 - [HVAC CAN Reader](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino) 
 - [Nathaniels Arduino Climate Code](https://github.com/nkg-io/arduino-climate)  
 - [Kyle May's FG ICC Repo](https://github.com/KyleMay/Ford-FG-ICC)    
 - [Bull3time's FG ICC Fork](https://github.com/Bull3time/Ford-FG-ICC)  
 - [mcp2515 can library](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino/mcp2515) 
 
  
**FG Falcon Specific Scripts** ![image](https://img.shields.io/badge/python-v3.7-blue) [![GitHub issues](https://img.shields.io/github/issues/jakka351/FG-Falcon?style=social)](https://github.com/jakka351/FG-Falcon/issues)  
 - [Python3/can0 SWC Adapter for FG](https://github.com/jakka351/FG-Falcon/blob/master/gs302/swc_seek2.py) (untested)  
 - [can0swc:catch can frames and throw keypresses](https://github.com/jakka351/can0swc)     
 - [cansend can0 swc commands](https://github.com/jakka351/FG-Falcon/tree/master/mscan/swc) (untested)
 - [cansend can0 icc commands](https://github.com/jakka351/FG-Falcon/tree/master/mscan/icc) (untested)    
 -  hvac python script in progress    
 
# FG CAN bus decoded    

 - [Controller Area Network](https://github.com/jakka351/FG-Falcon/wiki/Controller-Area-Network)  
 - [HS-Can spreadsheet](https://github.com/jakka351/FG-Falcon-specific/tree/master/resources)   
 - [MS-Can spreadsheet](https://github.com/jakka351/FG-Falcon-specific/tree/master/resources)    
 - [ICC Can codes](https://github.com/jakka351/FG-Falcon-specific/tree/master/resources) 
 - [fg_controller_area_network_latest.xlsx](https://github.com/jakka351/FG-Falcon/blob/master/resources/fg_controller_area_network_latest.xlsx) - work in progress, little can frame data yet0 03/01/21    
 - [fg_controller_area.dbc](https://github.com/jakka351/FG-Falcon/blob/master/resources/fg_controller_area.dbc) - in progress 01/01/2021    
 - [CAN Database](https://github.com/jakka351/FG-Falcon/wiki/CAN_id,-frame-database) -scrap this for that ^03/01/2021 
 - [Steering wheel media buttons](https://github.com/jakka351/FG-Falcon/wiki/Steering-Wheel-Media-Controls)  
  
- add document explaining basics of two buses/speeds/obd pin out/various points in car to tee into wiring - in progress 01/01/21  
  
  
Currently this information only really covers the CAN identifiers and data from the Front Display Interface Module, Audio Control Module, Body Electronic Module and the HVAC Intergrated Module. I am keen to create a mostly full database for the fg mkI so the progress will go up here. Anyone interested doing the same with a BA, BF FGII or FG-X that wants to help give me a shout. - 01/01/2021  

 
 ## [Steering wheel media CAN data](https://github.com/jakka351/FG-Falcon/wiki/Steering-Wheel-Media-Controls)  

| Address | Data    | Function | Byte1      | Byte2      | Byte3 | Byte4 | Byte5 | Byte6 | Byte7   | Byte8   |
| ------- | ----    | -------- | -----      | -----      | ----- | ----- | ----- | ----- | -----   | -----   |
| `754`   | 8 bytes | Complex  | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x00 | 0x00|
  
    
    
 
**Raspberry Pi & Linux**  ![image](https://img.shields.io/badge/%23-Raspberry%20Pi-red)  
 - [Crankshaft NG](https://getcrankshaft.com/)    
 - [OpenDash](https://github.com/openDsh/dash)      
 - [Openauto - Android Auto](https://github.com/f1xpl/openauto)  
 - [Adding CAN to  Raspberry Pi](https://www.beyondlogic.org/adding-can-controller-area-network-to-the-raspberry-pi/)  
 - [Socketcan](https://python-can.readthedocs.io/en/master/interfaces/socketcan.html)   
 - [Socketcan Linux Documentation](https://android.googlesource.com/kernel/msm/+/228428428138e231a155464239880201e5cc8b44/Documentation/networking/can.txt)   
 - [Python-CAN PiCAN2 Examples](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/pythoncan) 
  
  
# Forscan Resources ![image](https://img.shields.io/badge/%23-Forscan-lightblue)  
[Forscan Website](https://forscan.org/)    
[How to access MS CAN bus using FORScan and modified ELM327](https://forscan.org/forum/viewtopic.php?f=4&t=4)     
[How to run FORScan on Linux](https://forscan.org/forum/viewtopic.php?f=4&t=6)        
[As Built Data ]()  
[Police Mode]()  
# Technical Documents  ![image](https://img.shields.io/badge/FG-Falcon-blue)  
[FG Github Wiki](https://github.com/jakka351/FG-Falcon/wiki)    
[FG Falcon mkI Workshop Manual](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1812)    
[FG Falcon mkII Workshop Manual]()    
[FG Falcon](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1813)  
[Supplement](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1884)   
[Module Comms Network](http://fordforums.com.au/wsmpub/fgii/418-00.html)  
[HVAC General Info](http://fordforums.com.au/wsmpub/fgfpv50/412-00.html)   
[ICC](http://fordforums.com.au/wsmpub/fg/413-08.html)  
[Remove ICC Assembly](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=855)    
[Component View & Location](http://fordforums.com.au/wsmpub/wire/fgfpv/700-06.html)  


# Wiring Diagrams ![images](https://img.shields.io/badge/Ford-Forums-darkblue)![image](https://img.shields.io/badge/FG-Falcon-blue)    
 - [ICC connector](https://github.com/jakka351/FG-Falcon/wiki/Interior-Command-Centre)    
 - [Interior Fuseboxe Diagram](https://github.com/jakka351/FG-Falcon/wiki/Interior-Fuse-Pinout)
 - [Engine Bay Fuse Diagram](https://github.com/jakka351/FG-Falcon/wiki/Engine-Bay-Fuse-Pinout)  
 - [Audio Interface Module](https://github.com/jakka351/FG-Falcon/wiki/Audio-Interface-Module)   
 - [Bluetooth & Phone](https://github.com/jakka351/FG-Falcon/wiki/Bluetooth)  
 - [DIAGNOSTIC PORT](https://github.com/jakka351/FG-Falcon/wiki/Diagnostic-Port)  
   
 # Links #  - add descriptions / warn of products for sale / no association
[Ford Forums AU](https://fordforums.com.au/) - Ford Forums Australia.  
[Forscan](https://forscan.org/) - Forscan is a Ford specific software compatible with various scantools.    
[ASL Automedia](https://www.aslautomedia.com.au/) - OEM Replacement Parts for FG ICC  
[CANBarra CANBUS Translator](https://www.tiperformance.com.au/products/canbarra-canbus-translator/) - converts the CANBUS signals from BA BF FG PCMs  
[FG Mods](https://fgmods.com.au/)  - FG Mods  
[MCP2515 microchip.com data sheet](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf)  
[iDoka's Awesome CANBUS](https://github.com/iDoka/awesome-canbus) - A curated list of awesome tools, hardware and resources for CAN bus.  
[Raspberry Pi PiCAN2 board](https://www.elektormagazine.com/news/pican-2-can-bus-board-for-raspberry-pi)    
[Arduino CAN-Bus shield](https://wiki.seeedstudio.com/CAN-BUS_Shield_V2.0/)  
[Seeed Arduino CAN library](https://github.com/Seeed-Studio/Seeed_Arduino_CAN)   
[Generic China MCP2515 board](https://www.ebay.com.au/i/383796813415?chn=ps&norover=1&mkevt=1&mkrid=705-139619-5960-0&mkcid=2&itemid=383796813415&targetid=921460872233&device=c&mktype=pla&googleloc=1000567&poi=&campaignid=10101784961&mkgroupid=102311923620&rlsatarget=pla-921460872233&abcId=9300367&merchantid=7364522&gclid=Cj0KCQiAoab_BRCxARIsANMx4S6cKtaHwxGH_U9m058T7V4VBV7SBE-QISec-tuDyB5hDgv58CXihvkaAlnnEALw_wcB)    
   
# Disclaimer #
Modifying any system on a vehicle may have unforseen consequences. 
![image](https://i.postimg.cc/3NzQt9S9/FPV_FG_MK_II_GS_-_VANISH-_SILVER.jpg)  
# Credit & License #
[Kyle May](https://www.kylemay.net.au/)   
[Bull3time](https://github.com/Bull3time)  
[Mitchell H](https://fordforums.com.au/member.php?u=2315299)      
[MRFGXR6](http://fordforums.com.au/member.php?u=25234)  
[RSJudka - OpenDash](https://github.com/rsjudka)    
[XR6 ICC Replacement](https://fordforums.com.au/showthread.php?t=11475851)    
[ICC Replacement](https://fordforums.com.au/showthread.php?p=6521457#post6521457)  
[Ford Forums Australia](https://fordforums.com.au)      


![image](https://img.favcars.com/fpv/logotypes/fpv_logotypes__wallpapers_1.jpg)  


