#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This is an example of an echo client.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QCoreApplication
import sys

  
class EchoClient(QObject):
  
    def __init__(self):
        super().__init__()
        
        self.getMessage()
        self.openConnection()
        
        
    def getMessage(self):
        
        args = sys.argv          
        
        if len(args) == 2:      
        
            self.msg = bytearray(args[1], 'UTF-8')
            
        else:
            print("Usage: echo_client.py message")
            sys.exit(1)        
        
                
    def openConnection(self):    
        
        self.tcpSocket = QtNetwork.QTcpSocket()
        self.tcpSocket.readyRead.connect(self.readData)
        self.tcpSocket.error.connect(self.onError)
        
        self.tcpSocket.connectToHost("localhost", 6001)    

        self.tcpSocket.write(self.msg)
                           
   
        
    def onError(self, e):
                      
        t = QtNetwork.QAbstractSocket.RemoteHostClosedError              
        
        if e == t:
            print("closing connection")
            
        else: 
            print("error")
            print(self.tcp.errorString())
        

    def readData(self):

        while not self.tcpSocket.atEnd():
            
            bytes_string = self.tcpSocket.readAll()
            print(str(bytes_string, 'utf-8'))   
            
        self.tcpSocket.close()            
        QCoreApplication.quit()    

    
app = QCoreApplication([])
ec = EchoClient()
sys.exit(app.exec_())    

