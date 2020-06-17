#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we work with horizontal
alignment.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, 
        QApplication, QHBoxLayout, QVBoxLayout)     
from PyQt5.QtCore import Qt
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 250, 130)
        self.setWindowTitle("Horizontal alignment")
       
        self.initUI()
        
        
    def initUI(self):
    
        btn1 = QPushButton("Left", self)
        btn2 = QPushButton("Center", self)
        btn3 = QPushButton("Right", self)
        btn4 = QPushButton("Stretch", self)

        vbox = QVBoxLayout()
        
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        
        hbox1.addWidget(btn1)
        hbox1.setAlignment(Qt.AlignLeft)
        hbox2.addWidget(btn2)
        hbox2.setAlignment(Qt.AlignCenter)
        hbox3.addWidget(btn3)
        hbox3.setAlignment(Qt.AlignRight)
        
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(btn4)
        self.setLayout(vbox) 
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

