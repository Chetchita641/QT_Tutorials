#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we demonstrate the QSizePolicy
layout attribute.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, QSizePolicy,
        QApplication, QHBoxLayout)      
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.move(300, 300)
        self.setWindowTitle("Size policy")
       
        self.initUI()
        
        
    def initUI(self):
    
        btn1 = QPushButton("Button", self)
        btn1.setSizePolicy(QSizePolicy.Fixed, 
             QSizePolicy.Fixed)
        btn2 = QPushButton("Button", self)
        btn3 = QPushButton("Button", self)
        btn3.setSizePolicy(QSizePolicy.Fixed, 
             QSizePolicy.Fixed)
        
        layout = QHBoxLayout()
        layout.addWidget(btn1) 
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        
        self.setLayout(layout) 
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
