 #!/usr/bin/python3
        #
        #FG Falcon python script swc_seek
        #Listens on canbus for press of swc_seek and then activates keypress
        #https://jakka351.github.io/FG-Falcon/

        import RPi.GPIO as GPIO
        import can
        import time
        import os
        import serial
        import uinput
        import queue
        from threading import Thread

        led = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,True)

        # ==== Keyboard buttons configurations ====
        device = uinput.Device([
                uinput.KEY_NEXTSONG,
                uinput.KEY_PREVIOUSSONG,
                uinput.KEY_PLAYPAUSE,
                uinput.KEY_VOLUMEUP,
                    uinput.KEY_VOLUMEDOWN,
                    uinput.KEY_MUTE,
                uinput.KEY_M,
                uinput.KEY_O,
 ])


        # For a list of PIDs visit https://en.wikipedia.org/wiki/OBD-II_PIDs
        SWC_SEEK            = 0x09
        SWC                 = 0x2F2

        print('\n\rCAN Rx test')
        print('Bring up CAN0....')

        # Bring up can0 interface at 500kbps
        os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
        time.sleep(0.1)
        print('Ready')

        try:
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
        except OSError:
                print('Cannot find PiCAN board.')
 GPIO.output(led,False)
                exit()

        def can_rx_task():      # Receive thread
                while True:
                        message = bus.recv()
                        if message.arbitration_id == SWC:
                                q.put(message)                  # Put message into queue

        def can_tx_task():      # Transmit thread
                while True:

                        GPIO.output(led,True)
                        #
                        msg = can.Message(arbitration_id=0x123,data=[0x02,0x01,0x00,0x00,0x00,0x00,0x00,0x00],extended_id=False)
                        bus.send(msg)

  time.sleep(0.05)

                        GPIO.output(led,False)
                        time.sleep(0.1)

        q = queue.Queue()
        rx = Thread(target = can_rx_task)
        rx.start()
        tx = Thread(target = can_tx_task)
        tx.start()

        throttle = 0
        c = ''
        count = 0
        # Main loop
        try:
                while True:
                        for i in range(4):
                                while(q.empty() == True):       # Wait until there is a message
                                        pass
                                message = q.get()

                                c = '{0:f},{1:d},'.format(message.timestamp,count)
                                if message.arbitration_id == SWC and message.data[7] == SWC_SEEK:
                                        device.emit_click(uinput.KEY_NEXTSONG) # Next Track

                        print('Seek!')

        except KeyboardInterrupt:
                #Catch keyboard interrupt
                GPIO.output(led,False)
                os.system("sudo /sbin/ip link set can0 down")
                print('\n\rKeyboard interupt')

