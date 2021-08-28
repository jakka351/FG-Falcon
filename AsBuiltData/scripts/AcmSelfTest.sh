###################################
#canbus.com.au jakka351
#fg audio control module self test
###################################
#!/bin/bash
cansend can0 727#023E010000000000
cansend can0 72F#017E000000000000
cansend can0 727#023E010000000000
cansend can0 72F#017E000000000000
cansend can0 727#0210830000000000  
cansend can0 72F#037F101200000000 
cansend can0 727#0331020000000000  
cansend can0 72F#0271020000000000
cansend can0 727#0233020000000000
cansend can0 72F#07730201A406AC98