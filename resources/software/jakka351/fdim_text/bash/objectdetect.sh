#!/bin/bash
while true;
    do 
        cangen -I 309 -L 8 -D 4261747465727920 -g 10 vcan0 &
        sleep 0.75 
        sudo killall cangen
        cangen -I 309 -L 8 -D 566F6C7461676520  -g 10 vcan0 &
        sleep 0.75 
        sudo killall cangen
    done

    4d 69 6c 6c 69 6d 65 74 72 65 73 3a 31 32 30 30 