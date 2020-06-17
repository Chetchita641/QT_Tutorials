#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This is an example of an echo server.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QCoreApplication
import sys, signal


class EchoSocket(QtNetwork.QTcpSocket):
    
    def __init__(self, p):
        super().__init__()        
        
        self.readyRead.connect(self.readClient)
        self.disconnected.connect(self.discardClient)

        self.error.connect(self.onError)
                        
        
    def readClient(self):
        
        msg = self.readLine()
        print(msg)
        self.write(msg)                                              

        
    def discardClient(self):
        
        self.deleteLater()        
        
        
    def onError(self, e):    
        
        t = QtNetwork.QAbstractSocket.RemoteHostClosedError
            
        if e == t:
            print("closing connection")
            
        else: 
            print("error")
            print(self.tcp.errorString())


class EchoServer(QtNetwork.QTcpServer):
    
    def __init__(self, port):
        super().__init__()
        
        print("Starting Echo Server")
        print("Listening on port:", port)
        self.listen(QtNetwork.QHostAddress.LocalHost, port)
        
        
    def incomingConnection(self, socket):
        
        self.es = EchoSocket(self)
        self.es.setSocketDescriptor(socket)        
                 

signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QCoreApplication([])
echo = EchoServer(6001)
sys.exit(app.exec_())
    