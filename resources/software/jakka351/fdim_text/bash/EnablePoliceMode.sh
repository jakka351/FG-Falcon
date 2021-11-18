
	###################################
	# 6FPA-util
	# EnablePoliceMode.sh
	###################################
	#!/bin/bash
	sleep 10
	candump -c -a -e -x vcan0,720:1FFFFFFF,728:1FFFFFFF &
	echo 'Starting Ecu Adjustment Diagnostic Session'
	cansend vcan0 720#0210870000000000
	sleep 0.1
	echo 'Tester Present Signal Sent'
	cansend vcan0 720#023E010000000000
	sleep 0.1
	echo 'Enabling Police Mode'
	cansend vcan0 720#043B038D0E000000
	sleep 0.1
	echo 'Checking Data'
	cansend vcan0 720#0322D10000000000
	sleep 0.1
	echo 'Re-entering Standard Diagnostic Session'
	cansend vcan0 720#0210810000000000
	sleep 0.1
	echo "Resetting Ecu at 0x720"
	cansend vcan0 720#0211010000000000
	sleep 0.1
	echo 'Please turn the ignition off and wait 3 seconds before turning the ignition back on. Do not start engine'
    sleep 30
    