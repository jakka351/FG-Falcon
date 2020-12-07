#!/bin/bash
#fg falcon mk1
#steering wheel controls

#cansend swc_phone
#cansend can0 2F2#02.E3.06.4E.08.1D.68.00
candump -L can0,2F2:2E3064E081D6800 | tee  'swc_phone.txt"  &

xdotool keypress
rm swc_phone.txt



