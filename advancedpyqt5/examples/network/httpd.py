#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This is a simple skeleton of an web server.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QCoreApplication, QTextStream


class HttpSocket(QtNetwork.QTcpSocket):
    
    def __init__(self, p):
        super().__init__()        
        
        self.readyRead.connect(self.readClient)
        self.disconnected.connect(self.discardClient)

        self.error.connect(self.onError)
                        
        
    def readClient(self):
                    
        cmd = self.readLine().split(' ')[0]    
        
        if cmd.toUpper() == 'HEAD':
            self.do_head()
            
        elif cmd.toUpper() == 'GET':
            self.do_get()
            
        else:
            self.do_error()            
        
        
    def do_head(self):
        
        os = QTextStream(self)
        
        os.setAutoDetectUnicode(True)
        os << 'HTTP/1.1 200 OK\r\n' \
          + 'Content-Type: text/plain; charset="utf-8"\r\n' \
          + 'Server: HTTP skeleton server\r\n' \
          + '\r\n'
        self.close()      
        
        
    def do_get(self):
        
        os = QTextStream(self)
        
        os.setAutoDetectUnicode(True)
        os << 'HTTP/1.1 200 OK\r\n' \
          + 'Content-Type: text/plain; charset="utf-8"\r\n' \
          + 'Server: HTTP skeleton server\r\n' \
          + '\r\n' \
          + 'Simple web page\n'
        self.close()          
        
        
    def do_error(self):
        
        os = QTextStream(self)
        os.setAutoDetectUnicode(True)
        os << "HTTP/1.1 400 Bad Request\r\n" \
          + "Content-Type: text/plain; charset=\"utf-8\"\r\n" \
          + "\r\n" \
          + 'The request could not be understood by the\n' \
            'server due to malformed syntax.\n'
        self.close()        

        
    def discardClient(self):
        
        self.deleteLater()        
        print("Connection closed")
        
        
    def onError(self, error):    
        
        print("Error: ", error)


class HttpServer(QtNetwork.QTcpServer):
    
    def __init__(self, port):
        super().__init__()
        
        print("Starting HTTP Server")
        print("Listening on port:", port)
        self.listen(QtNetwork.QHostAddress.Any, port)

        
    def incomingConnection(self, socket):
              
        self.hs = HttpSocket(self)
        self.hs.setSocketDescriptor(socket)        
               

import sys, signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QCoreApplication([])
http = HttpServer(8080)
sys.exit(app.exec_())
        
    