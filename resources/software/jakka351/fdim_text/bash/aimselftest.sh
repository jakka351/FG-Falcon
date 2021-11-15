#!/bin/bash
###########################
# 6FPA-util 
# audio if module self test
###########################
echo 'AIM On-Demand Self Test Starting:'
candump -c -a -e -x -s 0 -l can0,767:1FFFFFFF,76F:1FFFFFFF &
sleep 1
echo 'Results:'
cansend can0 767#023E010000000000
cansend can0 767#023E010000000000
cansend can0 767#0210830000000000
cansend can0 767#0331020000000000
cansend can0 767#0233020000000000
sleep 3
sudo killall candump

