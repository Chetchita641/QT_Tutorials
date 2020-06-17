#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we work with the
stretch factor applied on empty space.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton,
        QVBoxLayout, QApplication, QHBoxLayout)     
import sys
              

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle("Stretch space")
       
        self.initUI()
        
        
    def initUI(self):
    
        vbox = QVBoxLayout()
               
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(QPushButton("Button"))
        hbox1.addWidget(QPushButton("Button"))
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QPushButton("Button"))
        hbox2.addWidget(QPushButton("Button"))
        hbox2.addStretch(1)
               
        hbox3 = QHBoxLayout()
        hbox3.addWidget(QPushButton("Button"))
        hbox3.addStretch(1)
        hbox3.addWidget(QPushButton("Button"))
        
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(QPushButton("Button"))
        hbox4.addWidget(QPushButton("Button"))
        hbox4.addStretch(1)
        
        hbox5 = QHBoxLayout()
        hbox5.addWidget(QPushButton("Button"))
        hbox5.addStretch(1)
        hbox5.addWidget(QPushButton("Button"))
        hbox5.addStretch(1)
                
        vbox.addLayout(hbox1)        
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
       
        self.setLayout(vbox) 
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
