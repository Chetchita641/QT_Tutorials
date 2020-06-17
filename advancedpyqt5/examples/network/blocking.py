#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This is an example of a blocking
network program.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QTimer, QCoreApplication
import sys

  
class Example(QObject):
  
    def __init__(self):
        super().__init__()
        
        QTimer.singleShot(3000, self.openConnection)                
        QTimer.singleShot(4000, self.doSomeWork)    
        
        
    def openConnection(self):    
        
        tcpSocket = QtNetwork.QTcpSocket()
        tcpSocket.connectToHost("www.something.com", 80)    

        tcpSocket.write(b"GET / HTTP/1.1\r\n" \
                    b"Host: www.something.com\r\n" \
                    b"\r\n")
                    
        while tcpSocket.waitForReadyRead():
        
            bytes_string = tcpSocket.readAll()
            print(str(bytes_string, 'utf-8'))
            
                
        if tcpSocket.error():
            print(tcpSocket.errorString())
        
        tcpSocket.close()
                
        
    def doSomeWork(self):    
        
        print("Doing some work")
        QCoreApplication.quit()

        
app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())        

