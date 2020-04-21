"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""
from mac_addresses import *
import bluetooth
import routing

hostMACAddress = linux_computer_address# The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 25
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
client, clientInfo = s.accept()
import threading



hostMACAddress2 = linux_computer_address# The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port2 = 24
backlog = 1
size = 1024
s2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s2.bind((hostMACAddress2, port2))
s2.listen(backlog)
client2, clientInfo2 = s2.accept()




def forward_data2(data):
    global client2
    client2.send(data)




def receive(client):
    while 1:
        data = client.recv(size)
        if data:
            data = str(data.decode())
            print(data)
            if(data[0] == '1' or data[0] == '2'):
                forward_data2(data.encode())
    #        client.send(data) # Echo back to client
        
# def send(client):
#     while 1:
#         data = input()
#         client.send(data)

def forward_data(data):
    global client
    client.send(data)


# snd = threading.Thread(target=send, args=(client,))
rcv = threading.Thread(target=receive, args=(client,))
# snd.start()
rcv.start()

def receive2(client2):
    while 1:
        data = client2.recv(size)
        if data:
            data = data.decode()
            print(data)
        
def send2(client2):
    while 1:
        data = input()
        client2.send(data)


snd = threading.Thread(target=send2, args=(client2,))
rcv = threading.Thread(target=receive2, args=(client2,))
snd.start()
rcv.start()