#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example, we get the weather conditions
for a particular city.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import (QObject, QUrl, QCoreApplication, 
    QUrlQuery, QXmlStreamReader)
from urllib.request import urlopen
from urllib.parse import urlencode
import sys      

class Example(QObject):
  
    def __init__(self):        
        super().__init__()
        
        self.buildUrl()
        self.checkWeather()
        
        
    def buildUrl(self):
                
        args = sys.argv
        
        if len(args) == 2:      
        
            wid = args[1]
            
            baseurl = "https://query.yahooapis.com/v1/public/yql?"
            yql_query = "select * from weather.forecast where " \
                + "woeid={0} and u='c'".format(wid)

            yql_url = baseurl + urlencode({'q':yql_query}) 
            
            self.url = QUrl(yql_url)
            
        else:
            print("Usage: weather.py WOEID")
            sys.exit(1)
        
        
    def checkWeather(self):     
                
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        
        req = QtNetwork.QNetworkRequest(self.url)
        self.nam.get(req) 
        
        
    def handleResponse(self, reply):
        
        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            data = reply.readAll()
            
            r = QXmlStreamReader(str(data, 'UTF-8'))
            
            while not r.atEnd():
            
                r.readNext()
                
                if (r.qualifiedName() == "yweather:location"):
                    
                    if r.isStartElement():
                        
                        atr = r.attributes()
                        print("City:", atr.value("city"))
                        print("Country:", atr.value("country"))

                
                if (r.qualifiedName() == "yweather:condition"):
                    
                    if r.isStartElement():
                        
                        atr = r.attributes()
                        print("Date:", atr.value("date"))
                        print("Condition:", atr.value("text"))
                        print("Temperature:", \
                            atr.value("temp"), "deg C")                                            
            
            if r.hasError():
                print("Error reading feed")
            
        else:
            print("Error occured: ", er)
            print(er)
            print(reply.errorString())
            
        QCoreApplication.quit()                            
                                

app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())
    