#!/bin/bash
###########################
# 6FPA-util 
# audio if module self test
###########################
candump can0,76F:1FFFFFFF &
cansend can0 767#023E010000000000
cansend can0 767#023E010000000000
cansend can0 767#0210830000000000
cansend can0 767#0331020000000000
cansend can0 767#0233020000000000


