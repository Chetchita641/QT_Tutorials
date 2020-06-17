#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example, we show how to authenticate
to a web page.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtCore, QtGui, QtNetwork
import sys, json
      
      
class Example:
  
    def __init__(self):    
        
        self.doRequest()
        
        
    def doRequest(self):   
        
        self.auth = 0
     
        url = "https://httpbin.org/basic-auth/user7/passwd7"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.authenticationRequired.connect(self.authenticate)
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)  
        
        
    def authenticate(self, reply, auth):
        
        print("Authenticating")
        
        self.auth += 1
        
        if self.auth >= 3:
            reply.abort()
        
        auth.setUser("user7")
        auth.setPassword("passwd7")         
             
      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            
            data = json.loads(str(bytes_string, 'utf-8'))
            
            print('Authenticated: {0}'.format(data['authenticated']))
            print('User: {0}'.format(data['user']))
            
            print()
            
        else:
            print("Error occurred: ", er)
            print(reply.errorString())
            
        QtCore.QCoreApplication.quit()    
        
           
app = QtCore.QCoreApplication([])
ex = Example()
sys.exit(app.exec_())


    