#!/bin/bash
###################################
# 6FPA-util 
# instrument cluster self test
###################################
echo "6FPA-util"
echo "On Demand Self Test"
candump can0,720:1FFFFFFF,728:1FFFFFFF & 
echo "Sending Tester Present Signal"
cansend can0  720#023E010000000000
sleep 0.25
echo "Entering Diagnostic Session"
cansend can0  720#0210830000000000
sleep 0.25
echo "Requesting Instrument Cluster On Demand Self-Test..."
cansend can0  720#0331020000000000
sleep 0.25
cansend can0  720#0233020000000000
sleep 0.25
echo "Sending Tester Present Signal"
cansend can0  720#023E010000000000
sleep 20

