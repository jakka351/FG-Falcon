#!/bin/bash
echo '6FPA-Util'
echo 'Read Diagnostic Trouble Codes'
#script will print response
#dump & log response from these id's only 
candump -c -a -e -x can0,767:1FFFFFFF,736:1FFFFFFF,727:1FFFFFFF,726:1FFFFFFF,720:1FFFFFFF,7A6:1FFFFFFF,767:1FFFFFFF,781:1FFFFFFF,76F:1FFFFFFF,73E:1FFFFFFF,72E:1FFFFFFF,72F:1FFFFFFF,728:1FFFFFFF,7AE:1FFFFFFF,76F:1FFFFFFF,789:1FFFFFFF &
#diagsig rx signal to read dtcs
cansend can0 767#041800FF00000000
sleep 0.01
cansend can0 736#041800FF00000000
sleep 0.02
cansend can0 727#041800FF00000000
sleep 0.02
cansend can0 726#041800FF00000000
sleep 0.02
cansend can0 720#041800FF00000000
sleep 0.02
cansend can0 781#041800FF00000000
sleep 0.02
cansend can0 7A6#041800FF00000000
sleep 0.02
echo 'done.'
sudo killall candump
