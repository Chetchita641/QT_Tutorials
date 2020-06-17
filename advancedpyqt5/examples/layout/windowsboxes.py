#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a Windows
window with layout boxes.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
        QVBoxLayout, QApplication, QHBoxLayout, 
        QListView, QSizePolicy)     
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Windows")
       
        self.initUI()


    def initUI(self):
        
        windows = QLabel('Windows')
        
        actBtn = QPushButton("Activate")
        clsBtn = QPushButton("Close")
        hlpBtn = QPushButton("Help")
        hlpBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        okBtn = QPushButton("OK")
        
        listView = QListView()
        
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        
        hbox1.addWidget(windows)
        vbox.addLayout(hbox1)
        
        hbox2 = QHBoxLayout()
        vboxl = QVBoxLayout()
        vboxr = QVBoxLayout()
        
        vboxl.addWidget(listView)
        vboxr.addWidget(actBtn)
        vboxr.addWidget(clsBtn)
       
        vboxr.setAlignment(clsBtn, Qt.AlignTop)
        
        hbox2.addLayout(vboxl)
        hbox2.addLayout(vboxr)
        vbox.addLayout(hbox2)
        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(hlpBtn)
        hbox3.addWidget(okBtn)
        hbox3.setAlignment(okBtn, Qt.AlignRight)
        vbox.addLayout(hbox3)
        
        self.setLayout(vbox)
       
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

