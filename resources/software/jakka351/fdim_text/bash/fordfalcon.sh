#!/bin/bash
#displays "Ford" then "Falcon" on fdim
while true;
    do 
        cangen -I 309 -L 8 -D 466f726420202020 -g 10 vcan0 &
        sleep 0.75 
        sudo killall cangen
        cangen -I 309 -L 8 -D 46616c636f6e2020 -g 10 vcan0 &
        sleep 0.75 
        sudo killall cangen
    done
