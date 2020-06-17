#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example we fetch a favicon from 
a website.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtCore, QtGui, QtNetwork
import sys
      
      
class Example:
  
    def __init__(self):    
        
        self.doRequest()
        
        
    def doRequest(self):   
    
        url = "http://www.google.com/favicon.ico"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)    
             
      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            data = reply.readAll()
            self.saveFile(data)        
            
        else:
            print("Error occured: ", er)
            print(reply.errorString())
            
        QtCore.QCoreApplication.quit()    
        

    def saveFile(self, data):
        
        
        f = open('favicon.ico', 'wb')
        
        with f:
            
            f.write(data)
        
           
app = QtCore.QCoreApplication([])
ex = Example()
sys.exit(app.exec_())


    