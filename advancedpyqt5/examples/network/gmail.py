#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example, we send an EHLO command 
to an SMTP server.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QCoreApplication
import sys
                        

class Example(QObject):
    
    states = ("unconnected", "looking up host", "connecting", 
        "connected", "bound", "listening", "closing")    
  
    def __init__(self):        
        super().__init__()
        
        self.initExample()
        
        
    def initExample(self):     
        
        self.tcp = QtNetwork.QTcpSocket(self)
        
        self.tcp.readyRead.connect(self.readData)
        self.tcp.stateChanged.connect(self.stateChanged)
        self.tcp.error.connect(self.onError)
               
        self.tcp.connectToHost("smtp.gmail.com", 587)                   
        self.tcp.write(b"EHLO smtp.gmail.com\r\n")            
        self.tcp.write(b"QUIT\r\n")  

    def readData(self):

        while not self.tcp.atEnd():
            
            bytes_string = self.tcp.readAll()
            print(str(bytes_string, 'utf-8'))     
                    
      
    def stateChanged(self, state):    
    
        print(self.states[state])
        
        
    def onError(self, error):    
    
        t = QtNetwork.QAbstractSocket.RemoteHostClosedError
            
        if error == t:
            print("closing connection")
            
        else: 
            print("error")
            print(self.tcp.errorString())
        
        self.tcp.close()
        QCoreApplication.quit()                 
        

app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())
           
    
    