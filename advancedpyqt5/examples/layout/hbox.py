#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a simple QHBoxLayout example.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, 
        QApplication, QHBoxLayout)      
import sys
      
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.move(300, 300)
        self.setWindowTitle("QHBoxLayout")
       
        self.initUI()
        
        
    def initUI(self):
    
        btn1 = QPushButton("Button", self)
        btn2 = QPushButton("Button", self)
        btn3 = QPushButton("Button", self)
        btn4 = QPushButton("Button", self)
        
        layout = QHBoxLayout()
        layout.addWidget(btn1) 
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        
        self.setLayout(layout) 
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
