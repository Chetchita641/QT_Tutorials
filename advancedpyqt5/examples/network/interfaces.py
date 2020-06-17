#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example, we find out all 
network interfaces on a host.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

import sys
from PyQt5 import QtNetwork
  

ai = QtNetwork.QNetworkInterface.allInterfaces()

for i in ai:
    
    print("Interface:", i.name())
    print("Hardware address:", i.hardwareAddress())
    print("IP address(es): ")
    
    ae = i.addressEntries()
    
    if len(ae) > 0:
    
        for e in ae:        
            print(e.ip().toString())
            
        print()    
