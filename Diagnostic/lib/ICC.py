#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function
import logging
import time
import can

logging.basicConfig(level=logging.INFO)

def simple_periodic_icc(bus):
    acm      = can.Message(arbitration_id=0x50C, data=[0x11, 0x02, 0x6E, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    fdim = can.Message(arbitration_id=0x55C, data=[0x01, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    aim      = can.Message(arbitration_id=0x555, data=[0x5C, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    bem      = can.Message(arbitration_id=0x501, data=[0x0C, 0x02, 0xEE, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    pam      = can.Message(arbitration_id=0x511, data=[0x55, 0x02, 0x6E, 0x00, 0x00, 0x04, 0x04, 0x00], is_extended_id=False)
    ic       = can.Message(arbitration_id=0x541, data=[0x55, 0x02, 0x6E, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    him      = can.Message(arbitration_id=0x353, data=[0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    ipc      = can.Message(arbitration_id=0x128, data=[0x00, 0xF1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    iat      = can.Message(arbitration_id=0x313, data=[0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    char738  = can.Message(arbitration_id=0x2E2, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    char764  = can.Message(arbitration_id=0x2FC, data=[0, 0, 1, 0, 31, 0, 2, 4], is_extended_id=False)
    char775  = can.Message(arbitration_id=0x307, data=[0, 0, 0, 0x80, 0, 0, 0, 0], is_extended_id=False)
    char777  = can.Message(arbitration_id=0x309, data=[0x47, 0x4F, 0x4C, 0x44, 0x31, 0x30, 0x34, 0x33], is_extended_id=False)
    char789  = can.Message(arbitration_id=0x315, data=[0, 0, 0, 0x04, 0x80, 0, 0, 0], is_extended_id=False)
    char1372 = can.Message(arbitration_id=0x55C, data=[1, 2, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    char742  = can.Message(arbitration_id=0x2E6, data=[4, 227, 0, 0, 0, 0, 0, 0], is_extended_id=False)
    char748  = can.Message(arbitration_id=0x2EC, data=[0x03, 0xCA, 0x02, 0xD5, 0x03, 0x15, 0x02, 0x00], is_extended_id=False)
    char751  = can.Message(arbitration_id=0x2EF, data=[0x03, 0x94, 0x04, 0x52, 0x05, 0x90, 0x00, 0x00], is_extended_id=False)
    char754  = can.Message(arbitration_id=0x2F2, data=[0x0A, 0x12, 0x11, 0x0E, 0x09, 0x49, 0x45, 0x00], is_extended_id=False)
    char756  = can.Message(arbitration_id=0x2F4, data=[0, 0, 255, 255, 255, 252, 0, 0], is_extended_id=False)
    char761  = can.Message(arbitration_id=0x2F9, data=[0,0,0,0,0,0,0,0], is_extended_id=False)
    vin      = can.Message(arbitration_id=0x317, data=[0x57, 0x39, 0x45, 0x38, 0x36, 0x31, 0x30, 0x31], is_extended_id=False)
    char30D  = can.Message(arbitration_id=0x30D, data=[0, 0, 0, 0x15, 0x30, 0xB6, 0, 0], is_extended_id=False)
    char30F  = can.Message(arbitration_id=0x30F, data=[0x03, 0x94, 0x04, 0x52, 0x05, 0x90, 0x00, 0x00], is_extended_id=False)
    char6FC  = can.Message(arbitration_id=0x6FC, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)

    print("P(retending to be an ICC for 5000 Seconds...")
    msg = (
        acm, aim, bem, pam, ic, him, ipc, iat, vin, char738, char742, 
        char748, char751, char754, char756, char761, char764, char775, char789, char1372, char30D, char30F, char6FC
        )
    task0 = bus.send_periodic(acm, 0.5)
    assert isinstance(task0, can.CyclicSendTaskABC)
    #task1 = bus.send_periodic(fdim, 0.5)
    #assert isinstance(task1, can.CyclicSendTaskABC)
    task2 = bus.send_periodic(aim, 0.5)
    assert isinstance(task2, can.CyclicSendTaskABC)
    task3 = bus.send_periodic(bem, 0.5)
    assert isinstance(task3, can.CyclicSendTaskABC)
    task4 = bus.send_periodic(pam, 0.5)
    assert isinstance(task4, can.CyclicSendTaskABC)
    task5 = bus.send_periodic(ic, 0.5)
    assert isinstance(task5, can.CyclicSendTaskABC)
    task6 = bus.send_periodic(him, 0.5)
    assert isinstance(task6, can.CyclicSendTaskABC)
    task7 = bus.send_periodic(ipc, 0.5)
    assert isinstance(task7, can.CyclicSendTaskABC)
    task8 = bus.send_periodic(iat, 0.5)
    assert isinstance(task8, can.CyclicSendTaskABC)
    task9 = bus.send_periodic(char738, 0.5)
    assert isinstance(task9, can.CyclicSendTaskABC)
    task10 = bus.send_periodic(char764, 0.5)
    assert isinstance(task10, can.CyclicSendTaskABC)
    task11 = bus.send_periodic(char775, 0.5)
    assert isinstance(task11, can.CyclicSendTaskABC)
    task12 = bus.send_periodic(char789, 0.5)
    assert isinstance(task12, can.CyclicSendTaskABC)
    task13 = bus.send_periodic(char1372, 0.5)
    assert isinstance(task13, can.CyclicSendTaskABC)
    task14 = bus.send_periodic(char742, 0.5)
    assert isinstance(task14, can.CyclicSendTaskABC)
    task15 = bus.send_periodic(char748, 0.5)
    assert isinstance(task15, can.CyclicSendTaskABC)
    task16 = bus.send_periodic(char751, 0.5)
    assert isinstance(task16, can.CyclicSendTaskABC)
    task17 = bus.send_periodic(char754, 0.5)
    assert isinstance(task17, can.CyclicSendTaskABC)
    task18 = bus.send_periodic(char756, 0.5)
    assert isinstance(task18, can.CyclicSendTaskABC)
    task19= bus.send_periodic(char761, 0.5)
    assert isinstance(task19, can.CyclicSendTaskABC)
    task20= bus.send_periodic(vin, 0.5)
    assert isinstance(task20, can.CyclicSendTaskABC)
    task21= bus.send_periodic(char6FC, 0.5)
    assert isinstance(task21, can.CyclicSendTaskABC)
    task22= bus.send_periodic(char30D, 0.5)
    assert isinstance(task22, can.CyclicSendTaskABC)
    task23= bus.send_periodic(char30F, 0.5)
    assert isinstance(task23, can.CyclicSendTaskABC)
    time.sleep(5000)
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
    msg.dlc = 8
    task.modify_data(msg)
    time.sleep(1)
    print("starting again")
    task.start()
    time.sleep(1)
    task.stop()
    print("done")
"""
