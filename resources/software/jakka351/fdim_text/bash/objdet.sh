#!/bin/bash
while true;
    do 
        cangen -I 309 -L 8 -D 4f626a6563742020 -g 10 vcan0 &
        sleep 0.75 
        sudo killall cangen
        cangen -I 309 -L 8 -D 4465746563746564 -g 10 vcan0 &
        sleep 0.75 
        sudo killall cangen
    done