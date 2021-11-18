#!/bin/bash
# manipulate instrument cluster back light

cansend can0 720#0210810000000000
cansend can0 720#0210870000000000
cansend can0 720#023E010000000000
cansend	can0 720#052F995907CA0000
cansend	can0 720#052F995907CA0000
sleep 10
cansend	can0 720#052F995907FF0000
cansend	can0 720#052F995907FF0000
sleep 10
cansend	can0 720#052F995907000000
cansend	can0 720#052F995907000000
sleep 10