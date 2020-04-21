"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

from mac_addresses import *
import threading 
import bluetooth

serverMACAddress = linux_computer_address
port = 25
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

s.close()

def sender(s):
    while 1:
        text = input() # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        s.send(text.encode())

def receiver(s):
    size = 1024
    #client, clientInfo = s.accept()
    while 1:
        data = s.recv(size)
        if data:
            print(data)

snd = threading.Thread(target=receiver, args=(s,))
rcv = threading.Thread(target=sender, args=(s,))
rcv.start()
snd.start()