#!/bin/bash
#fg falcon mk1
#steering wheel controls

#cansend swc_seek
cansend can0 2F2#02.E3.06.4E.08.1D.00.09
candump can0,2F2:2E3064E081D0009

#cansend swc_volup
cansend can0 2F2#02.E3.06.4E.08.1D.00.11
candump can0,2F2:2E3064E081D0011

#cansend swc_voldown
cansend can0 2F2#02.E3.06.4E.08.1D.00.19
candump can0,2F2:2E3064E081D0019

#cansend swc_phone
cansend can0 2F2#02.E3.06.4E.08.1D.68.00
candump can0,2F2:2E3064E081D6800




