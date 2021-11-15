#!/bin/bash
###################################
# 6FPA-util 
# audio control module self test
###################################
candump -c -a -e -x can0,727:1FFFFFFF,72F:1FFFFFFF &
sleep 1
echo 'ACM On-Demand Self Test Starting...'
sleep 1
Echo 'Results'
cansend can0 727#023E010000000000
cansend can0 727#0210810000000000  
cansend can0 727#0331020000000000  
cansend can0 727#0233020000000000
