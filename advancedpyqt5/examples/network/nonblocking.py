#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This is an example of a non-blocking
network program.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QThread, QCoreApplication
import sys, time

class Worker(QThread):
    
    def __init__(self):
        super(Worker, self).__init__()
        
        print("Init Thread")
        
        
    def run(self):
        
        print("Thread started")
        
        time.sleep(10)
        
        print("Thread ended")

  
class Example(QObject):
  
    def __init__(self):
        super().__init__()
        
        self.openConnection()
        self.doSomeWork()
        
                
    def openConnection(self):    
        
        self.tcpSocket = QtNetwork.QTcpSocket()
        self.tcpSocket.readyRead.connect(self.readData)
        self.tcpSocket.error.connect(self.onError)
        
        self.tcpSocket.connectToHost("www.something.com", 80)    

        self.tcpSocket.write(b"GET / HTTP/1.1\r\n" \
                    b"Host: www.something.com\r\n" \
                    b"\r\n")
    
    
    def doSomeWork(self):

        self.wrk = Worker()
        self.wrk.finished.connect(QCoreApplication.quit)
        self.wrk.start()
   
        
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
                
app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())    

