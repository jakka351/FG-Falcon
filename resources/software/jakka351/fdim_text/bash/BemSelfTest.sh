#!/bin/bash
###################################
#6FPA-util 
# body electric self test
###################################
candump can0,72E:1FFFFFFF &
cansend can0 726#023E010000000000
cansend can0 726#023E010000000000  
cansend can0 726#0210830000000000  
cansend can0 726#0331020000000000  
cansend can0 726#0233020000000000   
cansend can0 726#023E010000000000   
