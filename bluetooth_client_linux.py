"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

from mac_addresses import *
import bluetooth

serverMACAddress = mac_computer_address
port = 0
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(text.encode())
s.close()