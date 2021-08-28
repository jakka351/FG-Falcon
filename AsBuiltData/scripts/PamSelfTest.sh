#################################
#canbus.com.au jakka351
#fg parking aid module self test
#################################
#!/bin/bash
cansend can0 736#023E010000000000    
cansend can0 73E#017E000000000000    
cansend can0 736#023E010000000000  
cansend can0 73E#017E000000000000  
cansend can0 736#0210830000000000  
cansend can0 73E#037F101200000000 
cansend can0 736#0331020000000000   
cansend can0 73E#0271020000000000 
cansend can0 736#0233020000000000   
cansend can0 73E#0373020000000000