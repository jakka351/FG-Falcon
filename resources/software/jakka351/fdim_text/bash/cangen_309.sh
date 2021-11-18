#!/bin/bash
while true;
counter=0

until [ $counter -gt 100 ]
do
    cangen -I 0x309 -L 8 -D 4650562047532020 -g 10 vcan0 

    echo Counter: $counter
  ((counter++))

until [ $counter -gt 200 ]
do
    cangen -I 0x309 -L 8 -D 426f737320352e34 -g 10 vcan0 
    
    echo Counter: $counter
  ((counter++))
done

