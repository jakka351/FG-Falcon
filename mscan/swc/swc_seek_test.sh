#!/bin/bash
#fg falcon swc_seek

#candumpseek () {
candump -L can0,2F2:2E364E81D9 | tee /can/fpv-gs/swc/test.txt &
#}

#TIME=`date +"%Y-%m-%d %T"`
${LOG}="cat ./test.txt"
${SEEK}="'can0 2F2[*]02 E3 06 4E 08 1D 00 09'"

if [ ${LOG} = ${SEEK}]
 then  echo swc_sweek

fi 
# then activate seek button 


