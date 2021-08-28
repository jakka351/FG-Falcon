###################################
#canbus.com.au jakka351
#fg instrument cluster self test
###################################
#!/bin/bash

cansend can0  720#023E010000000000
cansend can0  728#017E000000000000
cansend can0  720#023E010000000000
cansend can0  728#017E000000000000
cansend can0  720#0210830000000000
cansend can0  728#037F101200000000
cansend can0  720#0331020000000000
cansend can0  728#0271020000000000
cansend can0  720#0233020000000000
cansend can0  728#037F337800000000
cansend can0  720#023E010000000000
cansend can0  728#0373020000000000


###################################
#canbus.com.au jakka351
#fg body electric self test
###################################
#!/bin/bash
cansend can0 726#023E010000000000
cansend can0 72E#017E000000000000   
cansend can0 726#023E010000000000  
cansend can0 72E#017E000000000000  
cansend can0 726#0210830000000000  
cansend can0 72E#037F101200000000  
cansend can0 726#0331020000000000  
cansend can0 72E#0271020000000000   
cansend can0 726#0233020000000000   
cansend can0 72E#037F337800000000   
cansend can0 726#023E010000000000   
cansend can0 72E#0373020000000000   



###################################
#canbus.com.au jakka351
#fg audio control module self test
###################################
#!/bin/bash
can0  RX - -  727   [8]  02 3E 01 00 00 00 00 00
can0  RX - -  72F   [8]  01 7E 00 00 00 00 00 00
can0  RX - -  727   [8]  02 3E 01 00 00 00 00 00
can0  RX - -  72F   [8]  01 7E 00 00 00 00 00 00
can0  RX - -  727   [8]  02 10 83 00 00 00 00 00  
can0  RX - -  72F   [8]  03 7F 10 12 00 00 00 00 
can0  RX - -  727   [8]  03 31 02 00 00 00 00 00  
can0  RX - -  72F   [8]  02 71 02 00 00 00 00 00
can0  RX - -  727   [8]  02 33 02 00 00 00 00 00
can0  RX - -  72F   [8]  07 73 02 01 A4 06 AC 98   '.s......'       
























