#!/bin/bash

sudo ip link set can0 up type can bitrate 125000
sudo ifconfig can0 up txqueuelen 65535 
