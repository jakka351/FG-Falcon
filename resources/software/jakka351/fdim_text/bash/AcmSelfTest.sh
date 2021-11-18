#!/bin/bash
###################################
# 6FPA-util 
# audio control module self test
###################################
candump can0,72F:1FFFFFFF &
cansend can0 727#023E010000000000
cansend can0 727#0210810000000000  
cansend can0 727#0331020000000000  
cansend can0 727#0233020000000000
