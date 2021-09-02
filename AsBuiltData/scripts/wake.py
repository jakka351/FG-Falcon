#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function
import logging
import time
import can

logging.basicConfig(level=logging.INFO)

def simple_periodic_icc(bus):
    vin      = can.Message(arbitration_id=0x317, data=[0x57, 0x39, 0x45, 0x38, 0x36, 0x31, 0x30, 0x31], is_extended_id=False)
    acm      = can.Message(arbitration_id=0x50C, data=[0x11, 0x02, 0x6E, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    fdimwake = can.Message(arbitration_id=0x406, data=[0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    fdimtext = can.Message(arbitration_id=0x309, data=[0x4A, 0x41, 0x43, 0x4B, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    audiocurrentmediamode = can.Message(arbitration_id=0x2F2, data=[0x0A, 0x12, 0x11, 0x0E, 0x09, 0x49, 0x45, 0x05], is_extended_id=False)
    hvac  = can.Message(arbitration_id=0x353, data=[0x00, 0x41, 0x43, 0x4B, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    print("Sending Wake signal to FDIM for 5000 Seconds...")
    msg = (
       vin, acm, fdimwake, fdimtext, hvac, audiocurrentmediamode
        )

    task0 = bus.send_periodic(acm, 0.5)
    assert isinstance(task0, can.CyclicSendTaskABC)
    task1 = bus.send_periodic(fdimwake, 0.5)
    assert isinstance(task1, can.CyclicSendTaskABC)
    task2 = bus.send_periodic(fdimtext, 0.5)
    assert isinstance(task2, can.CyclicSendTaskABC)
    task3 = bus.send_periodic(audiocurrentmediamode, 0.5)
    assert isinstance(task3, can.CyclicSendTaskABC)
    task4 = bus.send_periodic(hvac, 0.5)
    assert isinstance(task4, can.CyclicSendTaskABC)
    task20= bus.send_periodic(vin, 0.5)
    assert isinstance(task20, can.CyclicSendTaskABC)
    
    time.sleep(5000)
    task.stop()
    print("icc can data no longer being sent")

    
if __name__ == "__main__":

    reset_msg = can.Message(arbitration_id=0x00, data=[0, 0, 0, 0, 0, 0], is_extended_id=False)

    for interface, channel in [
        ('socketcan', 'can0'),
        #('ixxat', 0)
    ]:
        print("Carrying out cyclic tests with {} interface".format(interface))

        bus = can.Bus(interface=interface, channel=channel, bitrate=500000)
        bus.send(reset_msg)

        simple_periodic_icc(bus)

        bus.send(reset_msg)
        bus.shutdown()


        time.sleep(2)
"""
def test_periodic_send_with_modifying_data(bus):
    print("Starting to send a message every 200ms. Initial data is ones")
    msg = can.Message(arbitration_id=0x55C, data=[0x01, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    task = bus.send_periodic(msg, 0.500,100)
    if not isinstance(task, can.ModifiableCyclicTaskABC):
        print("This interface doesn't seem to support modification")
        task.stop()
        return
    time.sleep(2)
    print("Changing data of running task to begin with 99")
    msg.data[7] += 1 
    task.modify_data(msg)
    time.sleep(2)
    task.stop()
    print("stopped cyclic send")
    print("Changing data of stopped task to single ff byte")
    msg.data = bytearray([0x01, 0x02, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    print("Changing data of stopped task to single ff byte")
    msg.data = bytearray([0x01, 0x02, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    msg.dlc = 8
    task.modify_data(msg)
    time.sleep(1)
    print("starting again")
    task.start()
    time.sleep(1)
    task.stop()
    print("done")
"""


