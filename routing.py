#this file will get the node to which to send data based on what node is passed in.

from mac_addresses import *

class router:

    def __init__(self):
        self.routing_table = dict()
        self.my_mac = linux_computer_address
        self.routing_table[self.my_mac] = []

    def get_route(self, mac):
        path = dict()
        distances = dict()
        distances[self.my_mac] = 0
        unvisited = set()
        for k, v in self.routing_table.items():
            for n in v:
                unvisited.add(n)
        current_node = self.my_mac
        
        while mac in unvisited:
            for n in self.routing_table[current_node]:
                if (n not in distances) or distances[current_node] +1 < distances[n]:
                    distances[n] = distances[current_node] +1
                    path[n] = current_node
            unvisited.remove(current_node)
            low_v = 10000000
            low_n = None
            for n in unvisited:
                if n in distances:
                    if distances[n] < low_v:
                        low_v = distances[n]
                        low_n = n
            current_node = low_n
        a = mac
        b = path[mac]
        while b != self.my_mac:
            a = b
            b = path[a]
        return a #should be a valid mac to which I am connected.
            

    def add_connection(self, host_device, new_device):
        pass

    def remove_connection(self, host_device, new_device):
        pass