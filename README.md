# FG-Falcon-specific #
![image](https://www.independentmotorsports.com.au/assets/images/Ford/Ford%20Coyote/FG_FGX%20Coyote%20banner.png)  
Collection of resources relating to electronic and mechanical systems of the FG Falcon.  

# Software  ![image](https://img.shields.io/badge/FG-Falcon-blue) ![image](https://img.shields.io/badge/mkI-mkII-lightblue) ![image](https://img.shields.io/badge/%23-Raspberry%20Pi-red) ![image](https://img.shields.io/badge/%23-Arduino-lightgrey) ![image](https://img.shields.io/badge/%23-Forscan-lightblue) ![image](https://img.shields.io/badge/github-can0swc-yellowgreen) ![image](https://img.shields.io/badge/cansend-can0-orange) [![GitHub issues](https://img.shields.io/github/issues/jakka351/FG-Falcon?style=social)](https://github.com/jakka351/FG-Falcon/issues)  
**FG Specific Arduino Sketches**   
 - [ICC Can Interface](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino)  
 - [ECU HSCAN Interface](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino)      
 - [HVAC CAN Reader](https://github.com/jakka351/FG-Falcon-specific/tree/master/software/arduino)     
 - [Kyle May's FG ICC Repo](https://github.com/KyleMay/Ford-FG-ICC)  
 - [Bull3time's FG ICC Fork](https://github.com/Bull3time/Ford-FG-ICC)  
 - mcp2515 arduino library[]()  
 - u8g2-master.zip depency library  
  
**FG Falcon Specific Scripts** ![image](https://img.shields.io/badge/python-v3.7-blue) [![GitHub issues](https://img.shields.io/github/issues/jakka351/FG-Falcon?style=social)](https://github.com/jakka351/FG-Falcon/issues)  
 - [Python3/can0 SWC Adapter for FG](https://github.com/jakka351/FG-Falcon/blob/master/gs302/swc_seek2.py) (untested)  
 - [can0swc:catch can frames and throw keypresses](https://github.com/jakka351/can0swc)     
 - hvac script todo  
 - [cansend can0 swc commands](https://github.com/jakka351/FG-Falcon/tree/master/mscan/swc) (untested)
 - [cansend can0 icc commands](https://github.com/jakka351/FG-Falcon/tree/master/mscan/icc) (untested)    
    
# FG CAN bus decoded      
[HS-Can spreadsheet](https://github.com/jakka351/FG-Falcon-specific/tree/master/resources)   
[MS-Can spreadsheet](https://github.com/jakka351/FG-Falcon-specific/tree/master/resources)    
[ICC Can codes](https://github.com/jakka351/FG-Falcon-specific/tree/master/resources)    
[HS-Can Database]()
[MS-Can Database]()
[Where & How]()
- add document explaining basics of two buses/speeds/obd pin out/various points in car to tee into wiring    
   
 ## Steering wheel media buttons

| Address | Data    | Function | Byte1      | Byte2      | Byte3 | Byte4 | Byte5 | Byte6 | Byte7   | Byte8   |
| ------- | ----    | -------- | -----      | -----      | ----- | ----- | ----- | ----- | -----   | -----   |
| `754`   | 8 bytes | Complex  | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x00 | 0x00|

Frame address 754 = 0x2F2 in hex

| Function | Byte1  | Byte2 | Byte3 | Byte4 | Byte5 | Byte6 | Byte7 | Byte8 |
| -------- | -----  | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| seek              | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x00 | 0x09 |
| volume UP         | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x00 | 0x11 |
| volume DOWN       | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x00 | 0x19 |
| phone             | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x68 | 0x00 |
| mode              | 0x02 | 0xE3 | 0x06 | 0x4E | 0x08 | 0x1D | 0x00 | 0x09 |

SWC are resistance based, ie one wire through all switches, pushing a button causes a specific resistance in circuit.  module then interprets and sends data on to mscan. 

 ![image](https://www.automobilesreview.com/gallery/2011-fpv-gt/2011-fpv-gt-04.jpg)  





**Raspberry Pi & Linux**  ![image](https://img.shields.io/badge/%23-Raspberry%20Pi-red)  
 - [Crankshaft NG](https://getcrankshaft.com/)    
 - [Opendsh/Dash Intelligent Auto](https://github.com/openDsh/dash)      
 - [Openauto - Android Auto](https://github.com/f1xpl/openauto)  
 - [Adding CAN to  Raspberry Pi](https://www.beyondlogic.org/adding-can-controller-area-network-to-the-raspberry-pi/)  
 - [Socketcan](https://python-can.readthedocs.io/en/master/interfaces/socketcan.html)   
 - [Socketcan Linux Documentation](https://android.googlesource.com/kernel/msm/+/228428428138e231a155464239880201e5cc8b44/Documentation/networking/can.txt)   
 - [Python-CAN PiCAN2 Examples](https://github.com/jakka351/FG-Falcon/tree/master/resources/software/pythoncan) 
![image](https://i.ibb.co/L8brGGM/fggreen.jpg)  
# Forscan Resources ![image](https://img.shields.io/badge/%23-Forscan-lightblue)  
[Forscan Website](https://forscan.org/)    
[How to access MS CAN bus using FORScan and modified ELM327](https://forscan.org/forum/viewtopic.php?f=4&t=4)     
[How to run FORScan on Linux](https://forscan.org/forum/viewtopic.php?f=4&t=6)      
[As Built Data ]()  
[Police Mode]()  
 ![image](https://i.ibb.co/WWzGWZz/silfg.jpg)  
# Technical Documents  ![image](https://img.shields.io/badge/FG-Falcon-blue)  
[FG Falcon mkI Workshop Manual](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1812)    
[FG Falcon mkII Workshop Manual]()    
[FG Falcon](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1813)  
[Supplement](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=1884)   
[Module Comms Network](http://fordforums.com.au/wsmpub/fgii/418-00.html)  
[HVAC General Info](http://fordforums.com.au/wsmpub/fgfpv50/412-00.html)   
[ICC](http://fordforums.com.au/wsmpub/fg/413-08.html)  
[Remove ICC Assembly](https://www.fordforums.com.au/vbportal/viewarticle.php?articleid=855)    
[Component View & Location](http://fordforums.com.au/wsmpub/wire/fgfpv/700-06.html)  
add workshop manual link  

# Wiring Diagrams ![images](https://img.shields.io/badge/Ford-Forums-darkblue)![image](https://img.shields.io/badge/FG-Falcon-blue)    
 - [ICC connector](https://github.com/jakka351/FG-Falcon/wiki/Interior-Command-Centre)    
 - [Interior Fuseboxe Diagram](https://github.com/jakka351/FG-Falcon/wiki/Interior-Fuse-Pinout)
 - [Audio Interface Module](https://github.com/jakka351/FG-Falcon/wiki/Audio-Interface-Module)   
 - [AIM & Phone](https://github.com/jakka351/FG-Falcon/wiki/Bluetooth)  
 - [Bluetooth & Phone](https://github.com/jakka351/FG-Falcon/wiki/Bluetooth)
 - [DIAGNOSTIC PORT]()  
   
 # Links #  
[Ford Forums AU](https://fordforums.com.au/)  
[Forscan](https://forscan.org/) 
[ASL Automedia](https://www.aslautomedia.com.au/)  
[PiCAN2 board](https://www.elektormagazine.com/news/pican-2-can-bus-board-for-raspberry-pi)    
   
# Disclaimer #
Modifying any system on a vehicle may have unforseen consequences. 
![image](https://i.postimg.cc/3NzQt9S9/FPV_FG_MK_II_GS_-_VANISH-_SILVER.jpg)  
# Credit & License #
[Kyle May](https://www.kylemay.net.au/)   
[Bull3time](https://github.com/Bull3time)  
[Mitchell H](https://fordforums.com.au/member.php?u=2315299)      
[MRFGXR6](http://fordforums.com.au/member.php?u=25234)  
[RSJudka - Intelligent Auto](https://github.com/rsjudka)    
[XR6 ICC Replacement](https://fordforums.com.au/showthread.php?t=11475851)    
[ICC Replacement](https://fordforums.com.au/showthread.php?p=6521457#post6521457)  
[Ford Forums Australia](https://fordforums.com.au)      


![image](https://img.favcars.com/fpv/logotypes/fpv_logotypes__wallpapers_1.jpg)  


