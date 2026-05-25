#!/usr/bin/env python3

"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.                                                                           
 """
from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from time import sleep, time
import can
import sys
import os
import time 

def cleanscreen():                    # cleans the whole console screen
    os.system("clear")   

def img():
    print('''              


 ██████  ███████ ██████   █████        ██    ██ ████████ ██ ██      ███████ 
██       ██      ██   ██ ██   ██       ██    ██    ██    ██ ██      ██      
███████  █████   ██████  ███████ █████ ██    ██    ██    ██ ██      ███████ 
██    ██ ██      ██      ██   ██       ██    ██    ██    ██ ██           ██ 
 ██████  ██      ██      ██   ██        ██████     ██    ██ ███████ ███████ 
                         Orion          Diagnostic Utility             
                         ''')
    #light up cluster on start up
    os.system("""
    cansend vcan0 720#0210870000000000
    cansend vcan0 720#023E010000000000
    cansend vcan0 720#062F713007800000
    cansend vcan0 720#023E010000000000
    cansend vcan0 720#062F713007800000
    cansend vcan0 720#023E010000000000
    sleep 1   
    cansend vcan0 720#023E010000000000
    sleep 1
    cansend vcan0 720#023E010000000000
    sleep 1
    cansend vcan0 720#062F713007000000
        """)
    #turn lights off
    time.sleep(1.0)    


def main():
    # Change some menu formatting
    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("Enter option:") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(8) \
        .set_right_margin(8) \
        .show_header_bottom_border(True)

#############################
# Front Page Title and Subtitle
#############################

    menu = ConsoleMenu("6FPA-util", "Command Line Diagnostic Utility", 
         prologue_text="https://canbus.com.au/", 
         epilogue_text="https://github.com/jakka351/6FPA-util",
                            formatter=MenuFormatBuilder()
                            .set_title_align('center')
                            .set_subtitle_align('center')
                            .set_border_style_type(MenuBorderStyleType.HEAVY_BORDER)
                            .set_left_margin(5) 
                            .set_right_margin(5)
                            .show_prologue_top_border(True)
                            .show_prologue_bottom_border(True)
                            .show_epilogue_top_border(True))

#############################
#DTC MENU
############################# 
    dtcmenu = ConsoleMenu("Diagnostic Trouble Code Menu", "Read and Clear Diagnostic Codes", formatter=menu_format)
    dtcread = CommandItem("Read Dtc",  """
    #!/bin/bash
    echo '6FPA-Util'
    echo 'Read Diagnostic Trouble Codes'
    sleep 1
    #script will print response
    #dump & log response from these id's only 
    candump -c -a -e -x vcan0,767:1FFFFFFF,736:1FFFFFFF,727:1FFFFFFF,726:1FFFFFFF,720:1FFFFFFF,7A6:1FFFFFFF,767:1FFFFFFF,781:1FFFFFFF,76F:1FFFFFFF,73E:1FFFFFFF,72E:1FFFFFFF,72F:1FFFFFFF,728:1FFFFFFF,7AE:1FFFFFFF,76F:1FFFFFFF,789:1FFFFFFF &
    #diagsig rx signal to read dtcs
    cansend vcan0 767#041800FF00000000
    sleep 0.5
    cansend vcan0 736#041800FF00000000
    sleep 0.5
    cansend vcan0 727#041800FF00000000
    sleep 0.5
    cansend vcan0 726#041800FF00000000
    sleep 0.5
    cansend vcan0 720#041800FF00000000
    sleep 0.5
    cansend vcan0 781#041800FF00000000
    sleep 0.5
    cansend vcan0 7A6#041800FF00000000
    sleep 0.5
    echo 'done.'
    sleep 5
    sudo killall candump
    
        """)
    dtcclear = CommandItem("Clear Dtc",  """
    !/bin/bash
    # clear diagnostic trouble codes 
    # StartDiagnosticSession, TesterPresent, Read Diagnostic Codes
    
    echo 'Clear All Midspeed CAN Diagnostic Trouble Codes'
    candump -c -a -e -x vcan0,767:1FFFFFFF,736:1FFFFFFF,727:1FFFFFFF,726:1FFFFFFF,720:1FFFFFFF,7A6:1FFFFFFF,767:1FFFFFFF,781:1FFFFFFF,76F:1FFFFFFF,73E:1FFFFFFF,72E:1FFFFFFF,72F:1FFFFFFF,728:1FFFFFFF,7AE:1FFFFFFF,76F:1FFFFFFF,789:1FFFFFFF &
    cansend vcan0 767#0210810000000000
    cansend vcan0 767#0210870000000000
    cansend vcan0 767#023E010000000000
    cansend vcan0 767#041800FF00000000
    sleep 0.5
    cansend vcan0 736#0210810000000000
    cansend vcan0 736#0210870000000000
    cansend vcan0 736#023E010000000000
    cansend vcan0 736#041800FF00000000
    sleep 0.5
    cansend vcan0 727#0210810000000000
    cansend vcan0 727#0210870000000000
    cansend vcan0 727#023E010000000000
    cansend vcan0 727#041800FF00000000
    sleep 0.5
    cansend vcan0 726#0210810000000000
    cansend vcan0 726#0210870000000000
    cansend vcan0 726#023E010000000000
    cansend vcan0 726#041800FF00000000
    sleep 0.5
    cansend vcan0 720#0210810000000000
    cansend vcan0 720#0210870000000000
    cansend vcan0 720#023E010000000000
    cansend vcan0 720#041800FF00000000
    sleep 0.5
    cansend vcan0 7A6#0210810000000000
    cansend vcan0 7A6#0210870000000000
    cansend vcan0 7A6#023E010000000000
    cansend vcan0 7A6#041800FF00000000
    sleep 0.5
    echo 'Diagnostic Session Opened'
    cansend vcan0 767#0314FF0000000000
    cansend vcan0 736#0314FF0000000000
    cansend vcan0 727#0314FF0000000000
    cansend vcan0 726#0314FF0000000000
    cansend vcan0 720#0314FF0000000000
    echo 'Reading DTC'
    cansend vcan0 767#041800FF00000000
    cansend vcan0 736#041800FF00000000
    cansend vcan0 727#041800FF00000000
    cansend vcan0 726#041800FF00000000
    cansend vcan0 720#041800FF00000000
    echo 'Done'
    sleep 5
    sudo killall candump
        """)
    resetecu = CommandItem("Reset All Modules",  """

        """)
    dtcmenu.append_item(dtcclear)
    dtcmenu.append_item(dtcread)
    dtcmenu.append_item(resetecu) 
    
    # Menu item for Front age
    submenu_item_2 = SubmenuItem("Diagnostic Trouble Codes" , submenu=dtcmenu)
    submenu_item_2.set_menu(menu)

#############################
# Service Tool Menu
############################# 
    servicemenu = ConsoleMenu("Service Tools Menu", "Perform Service Functions",
                            formatter=menu_format)
    koeoodst = CommandItem("[PCM] Key-On-Engine-Off On Demand SelfTest",  """

        """)
    koerodst = CommandItem("[PCM] Key-On-Engine-Running On Demand SelfTest",  """

        """)
    resetadaptations = CommandItem("[PCM] Reset Adaptations",  """

        """)
    abs_self_test = CommandItem("[ABS]On Demand SelfTest",  """

        """)
    him_self_test = CommandItem("[HIM]On Demand SelfTest",  """

        """)
    rcm_self_test = CommandItem("[RCM]On Demand SelfTest",  """"

        """)
    aim_self_test = CommandItem("[AIM]On Demand SelfTest",  """
    #!/bin/bash
    ###########################
    # 6FPA-util 
    # audio if module self test
    ###########################
    echo 'AIM On-Demand Self Test Starting:'
    candump -c -a -e -x -s 0 -l vcan0,767:1FFFFFFF,76F:1FFFFFFF &
    sleep 1
    echo 'Results:'
    cansend vcan0 767#023E010000000000
    cansend vcan0 767#023E010000000000
    cansend vcan0 767#0210830000000000
    cansend vcan0 767#0331020000000000
    cansend vcan0 767#0233020000000000
    sleep 3
    sudo killall candump
        """)
    acm_self_test = CommandItem("[ACM]On Demand SelfTest",  """
    #!/bin/bash
    ###################################
    # 6FPA-util 
    # audio control module self test
    ###################################
    candump -c -a -e -x -s 0 -l vcan0,727:1FFFFFFF,72F:1FFFFFFF &
    sleep 1
    echo 'ACM On-Demand Self Test Starting...'
    sleep 1
    Echo 'Results':
    cansend vcan0 727#023E010000000000
    cansend vcan0 727#0210810000000000  
    cansend vcan0 727#0331020000000000  
    cansend vcan0 727#0233020000000000
    sleep 3
    sudo killall candump
            """)
    bem_self_test = CommandItem("[BEM]On Demand SelfTest",  """
    #!/bin/bash
    ###################################
    #6FPA-util 
    # body electric self test
    ###################################
    echo 'BEM On-Demand Self Test Starting...'
    candump -c -a -e -x -s 0 -l vcan0,726:1FFFFFFF,72E:1FFFFFFF &
    sleep 1
    echo 'Results:'
    cansend vcan0 726#023E010000000000
    cansend vcan0 726#023E010000000000  
    cansend vcan0 726#0210830000000000  
    cansend vcan0 726#0331020000000000  
    cansend vcan0 726#0233020000000000   
    cansend vcan0 726#023E010000000000   
    sleep 3
    sudo killall candump
        """)
    bpm_self_test = CommandItem("[BPM]On Demand SelfTest",  """

        """)
    fdim_self_test = CommandItem("[FDIM]On Demand SelfTest",  """

        """)
    ic_self_test = CommandItem("[IC]On Demand SelfTest",  """
    #!/bin/bash
    ###################################
    # 6FPA-util 
    # instrument cluster self test
    ###################################
    sleep 1
    echo "6FPA-util"
    sleep 1
    echo "On Demand Self Test"
    sleep 1
    candump -c -a -e -x vcan0,720:1FFFFFFF,728:1FFFFFFF & 
    echo "Sending Tester Present Signal"
    cansend vcan0  720#023E010000000000
    sleep 0.25
    echo "Entering Diagnostic Session"
    cansend vcan0  720#0210830000000000
    sleep 0.25
    echo "Requesting Instrument Cluster On Demand Self-Test..."
    cansend vcan0  720#0331020000000000
    sleep 0.25
    cansend vcan0  720#0233020000000000
    sleep 0.25
    echo "Sending Tester Present Signal"
    cansend vcan0  720#023E010000000000
    sleep 5
        """)
    pam_self_test = CommandItem("[PAM]On Demand SelfTest",  """
    #!/bin/bash
    #################################
    # 6FPA-util
    # parking aid module self test
    #################################
    echo 'PAM On-Demand Self Test'
    sleep 1
    candump -c -a -e -x -s 0 -l vcan0,736:1FFFFFF,73E:1FFFFFFF &
    sleep 1
    echo 'Results:'
    cansend vcan0 736#023E010000000000   
    cansend vcan0 736#023E010000000000  
    cansend vcan0 736#0210830000000000 
    cansend vcan0 736#0331020000000000 
    cansend vcan0 736#0233020000000000
    sleep 3
    sudo killall candump
        """)
    servicemenu.append_item(abs_self_test)
    servicemenu.append_item(him_self_test)
    servicemenu.append_item(rcm_self_test)
    servicemenu.append_item(aim_self_test)
    servicemenu.append_item(acm_self_test)
    servicemenu.append_item(bem_self_test)
    servicemenu.append_item(bpm_self_test)
    servicemenu.append_item(fdim_self_test)
    servicemenu.append_item(pam_self_test)
    servicemenu.append_item(ic_self_test)
    servicemenu.append_item(koeoodst)
    servicemenu.append_item(koerodst)
    servicemenu.append_item(resetadaptations) 
    
    # Menu item for Front age
    servicetitle = SubmenuItem("Service Tools" , submenu=servicemenu)
    servicetitle.set_menu(menu)
   
#############################
#Mdulecoonfigmenn
#############################
    # Create a third submenu which uses double-line border
    submenu_3 = ConsoleMenu("Module Configuration", "As Built Data and Setting Enablers/Disablers",
                            prologue_text="This is my prologue. I am currently showing my top and bottom borders, but \
they are hidden by default. Also notice that my text is really long, so it extends beyond a single line, and should \
wrap properly within the menu borders. This is a useful place to put instructions to the user about how to use \
the menu.",
                            epilogue_text="6FA-util command line diagnostic utility for orion",
                            formatter=MenuFormatBuilder()
                            .set_title_align('center')
                            .set_subtitle_align('center')
                            .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)
                            .show_prologue_top_border(True)
                            .show_prologue_bottom_border(True))
    configoption1 = CommandItem("Enable Police Mode", """
    ###################################
    # 6FPA-util
    # EnablePoliceMode.sh
    ###################################
    #!/bin/bash
    echo 'Enable Police Mode'
    sleep 1
    candump -c -a -e -x vcan0,720:1FFFFFFF,728:1FFFFFFF &
    echo 'Starting Ecu Adjustment Diagnostic Session'
    cansend vcan0 720#0210870000000000
    sleep 0.1
    echo 'Tester Present Signal Sent'
    cansend vcan0 720#023E010000000000
    sleep 0.1
    echo 'Enabling Police Mode'
    cansend vcan0 720#043B038D0E000000
    sleep 0.1
    echo 'Checking Data'
    cansend vcan0 720#0322D10000000000
    sleep 0.1
    echo 'Re-entering Standard Diagnostic Session'
    cansend vcan0 720#0210810000000000
    sleep 0.1
    echo "Resetting Ecu at 0x720"
    cansend vcan0 720#0211010000000000
    sleep 0.1
    echo 'Please turn the ignition off and wait 3 seconds before turning the ignition back on. Do not start engine'
    sleep 5
    """ )

    configoption2 = CommandItem("Disable Police Mode",  """
    ###################################
    # 6FPA-util
    # DisablePoliceMode.sh
    ###################################
    #!/bin/bash
    echo 'Disable Police Mode'
    sleep 1
    candump -c -a -e -x vcan0,720:1FFFFFFF,728:1FFFFFFF &
    echo 'Starting Ecu Adjustment Diagnostic Session'
    cansend vcan0 720#0210870000000000
    sleep 0.25
    echo 'Tester Present Signal Sent'
    cansend vcan0 720#023E010000000000
    sleep 0.25
    echo 'Disabling Police Mode'
    cansend vcan0 720#043B03890E000000
    sleep 0.25
    echo 'Checking Data'
    cansend vcan0 720#0322D10000000000
    sleep 0.25
    echo 'Ending Communication Session`
    cansend vcan0 720#0210810000000000
    sleep 0.25
    echo "Resetting Ecu at 0x720"
    cansend vcan0 720#0211010000000000
    sleep 0.25
    echo 'Please turn the ignition off and wait 3 seconds before turning the ignition back on. Do not start engine'
    sleep 5

        """)    
    configoption3 = CommandItem("Enable Beltminder",  """ """)
    configoption4 = CommandItem("Disable Beltminder",  """ """)
        
    submenu_3.append_item(configoption1)
    submenu_3.append_item(configoption2)
    submenu_3.append_item(configoption3)
    submenu_3.append_item(configoption4)
    # Menu item for opening submenu 3
    submenu_item_3 = SubmenuItem("Module Configuration", submenu=submenu_3)
    submenu_item_3.set_menu(menu)

#############################
# Socketcan Menu
############################# 
    canmenu = ConsoleMenu("Socketcan Tools Menu", "can-utils",
                            formatter=menu_format)
    candump = CommandItem("candump ",  "candump -c -a -e -x -s 0 -l vcan0")
    cansniffer = CommandItem("cansniffer",  "cansniffer -c vcan0")
    canparser = CommandItem("canparser",  "sudo python3 parser.py")
    isotp_sniffer= CommandItem("ISO TP",  "touch hello.txt")
     
    canmenu.append_item(candump)
    canmenu.append_item(cansniffer)
    canmenu.append_item(canparser) 
    canmenu.append_item(isotp_sniffer)
    
    # Menu item for Front age
    cantitle = SubmenuItem("Socketcan Tools" , submenu=canmenu)
    cantitle.set_menu(menu)
    # Add all the items to the root menu
    menu.append_item(submenu_item_2)
    menu.append_item(servicetitle)
    menu.append_item(submenu_item_3)
    menu.append_item(cantitle)

    # Show the menu
    img()
    menu.start()
    menu.join()
    print(stdout)


if __name__ == "__main__":
    cleanscreen()
    main()

