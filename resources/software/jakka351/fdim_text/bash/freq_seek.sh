#!/bin/bash
#fg falcon mk1
#steering wheel controls left seek 
#this is not tested in car yet, sends frame every x milliseconds

while true; do cansend can0 2F2#02.E3.06.4E.08.1D.00.09; sleep 0.002; done # sleep=frequency of frame sending in seconds
                                                                           # 0.002 seconds = 200 milliseconds
#cansend swc_seek single shot
#cansend can0 2F2#02.E3.06.4E.08.1D.00.09
#filter with candump
#candump can0,2F2:2E3064E081D0009 



