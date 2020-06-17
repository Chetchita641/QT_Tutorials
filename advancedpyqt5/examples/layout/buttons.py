#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we put two buttons
in the right bottom corner of the window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
        QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QSize
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Buttons")
       
        self.initUI()
        
        
    def initUI(self):
    
        okBtn = QPushButton("OK")
        canBtn = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(canBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())






