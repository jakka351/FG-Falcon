#!/usr/bin/env python3
# coding: utf-8
#ms-can m
from __future__ import print_function
import logging
import time
import can

logging.basicConfig(level=logging.INFO)

def tester_present(bus):
    acm      = can.Message(arbitration_id=0x727, data=[0x02, 0x3E, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False) 
    aim      = can.Message(arbitration_id=0x767, data=[0x02, 0x3E, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    bpm      = can.Message(arbitration_id=0x781, data=[0x02, 0x3E, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    fdim     = can.Message(arbitration_id=0x7A6, data=[0x02, 0x3E, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    ic       = can.Message(arbitration_id=0x720, data=[0x02, 0x3E, 0x01, 0x00, 0x09, 0x49, 0x45, 0x05], is_extended_id=False)
    bem      = can.Message(arbitration_id=0x726, data=[0x02, 0x3E, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)

    print("Tester Present Signal Script - jakka351")

    msg = (
       acm, aim, bem, bpm,fdim, ic
        )

    task0 = bus.send_periodic(acm, 2)
    assert isinstance(task0, can.CyclicSendTaskABC)
    task1 = bus.send_periodic(aim, 2)
    assert isinstance(task1, can.CyclicSendTaskABC)
    task2 = bus.send_periodic(bpm, 2)
    assert isinstance(task2, can.CyclicSendTaskABC)
    task3 = bus.send_periodic(fdim, 2)
    assert isinstance(task3, can.CyclicSendTaskABC)
    task4 = bus.send_periodic(ic, 2)
    assert isinstance(task4, can.CyclicSendTaskABC)
    task20= bus.send_periodic(bem, 2)
    assert isinstance(task20, can.CyclicSendTaskABC)
    
    time.sleep(5000)
    task.stop()
    print("""
        Tester Present for the Following Modules:
        ACM
        AIM
        BEM
        BPM
        FDIM
        IC
        """)

    
if __name__ == "__main__":

    reset_msg = can.Message(arbitration_id=0x00, data=[0, 0, 0, 0, 0, 0], is_extended_id=False)

    for interface, channel in [
        ('socketcan', 'can0'),
        ]:

        print("Carrying out cyclic tests with {} interface".format(interface))
        bus = can.Bus(interface=interface, channel=channel, bitrate=125000)
        bus.send(reset_msg)
        tester_present(bus)
        bus.send(reset_msg)
        bus.shutdown()
        time.sleep(2)
