#!/bin/bash
#################################
# 6FPA-util
# parking aid module self test
#################################
candump can0,73E:1FFFFFFF &
cansend can0 736#023E010000000000   
cansend can0 736#023E010000000000  
cansend can0 736#0210830000000000 
cansend can0 736#0331020000000000 
cansend can0 736#0233020000000000