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

from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
        QApplication, QHBoxLayout, QVBoxLayout)     
from PyQt5.QtCore import Qt, QSize
import sys 

class MyButton(QPushButton):
    
    def __init__(self, text, parent, size):
        super(MyButton, self).__init__(text, parent)
        
        self.size = size
        
    def sizeHint(self):
        return self.size

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 250, 230)
        self.setWindowTitle("Vertical alignment")
       
        self.initUI()
        
        
    def initUI(self):
    
        hbox = QHBoxLayout()
        
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        
        vbox1.setAlignment(Qt.AlignBottom)
        vbox1.addWidget(QPushButton("Button", self))
        vbox1.addWidget(QPushButton("Button", self))
        vbox1.addWidget(QPushButton("Button", self))

        vbox2.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(QPushButton("Button", self))
        vbox2.addWidget(QPushButton("Button", self))
        vbox2.addWidget(QPushButton("Button", self))
        
        vbox3.setAlignment(Qt.AlignTop)
        vbox3.addWidget(QPushButton("Button", self))
        vbox3.addWidget(QPushButton("Button", self))
        vbox3.addWidget(QPushButton("Button", self))        

        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)
        self.setLayout(hbox) 
                
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

