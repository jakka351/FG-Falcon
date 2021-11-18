#!/bin/bash
###################################
# 6FPA-util 
# instrument cluster self test
###################################
candump can0,728:1FFFFFFF & 
cansend can0  720#023E010000000000
cansend can0  720#023E010000000000
cansend can0  720#0210830000000000
cansend can0  720#0331020000000000
cansend can0  720#0233020000000000
cansend can0  720#023E010000000000

























