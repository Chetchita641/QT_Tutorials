#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example, we look up the IP
address for a given host name.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QCoreApplication
import sys
      

class Example(QObject):
  
    def __init__(self):                  
        super().__init__()
        
        self.doLookup()
        
        
    def doLookup(self):
                
        args = sys.argv
        
        if len(args) > 1:
            host = args[1]
            
        else: host = 'localhost'                    
        
        QtNetwork.QHostInfo.lookupHost(host, self.receive)

    
    def receive(self, info):
        
        er = info.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
            
            for ip in info.addresses():
                print(ip.toString())
            
        else:
            print("error occurred", er)        
        
        QCoreApplication.quit()   
    
   
app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())

    