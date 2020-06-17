#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we demonstrate the nesting of 
layout managers. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, 
        QApplication, QHBoxLayout, QVBoxLayout)      
import sys     

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.move(300, 300)
        self.setWindowTitle("Nesting")
       
        self.initUI()
        
        
    def initUI(self):
    
        hbox = QHBoxLayout()
        
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Button")) 
        
        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addWidget(QPushButton("Button"))
        vbox1.addWidget(QPushButton("Button"))
        vbox1.addStretch(1)
        
        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addWidget(QPushButton("Button"))
        vbox2.addWidget(QPushButton("Button"))
        vbox2.addWidget(QPushButton("Button"))
        vbox2.addStretch(1)
               
        vbox3 = QVBoxLayout()
        vbox3.addStretch(1)
        vbox3.addWidget(QPushButton("Button"))
        vbox3.addWidget(QPushButton("Button"))
        vbox3.addWidget(QPushButton("Button"))
        vbox3.addWidget(QPushButton("Button"))
        vbox3.addStretch(1)
        
        hbox.addLayout(vbox1)        
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)
        hbox.addStretch(1)
        
        self.setLayout(hbox) 
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
