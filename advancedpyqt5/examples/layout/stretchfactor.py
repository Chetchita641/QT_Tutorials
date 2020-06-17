#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we demonstrate the stretch factor.
Button widgets grow at different ratio, when
the window is resized.

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
        self.setWindowTitle("Stretch factor")
       
        self.initUI()
        
        
    def initUI(self):
            
        b1 = QPushButton("Button")
        b2 = QPushButton("Button")
        b3 = QPushButton("Button")
               
        hbox = QHBoxLayout()
        
        hbox.addWidget(b1)
        hbox.addWidget(b2)
        hbox.addWidget(b3)
      
        hbox.setStretchFactor(b1, 1)
        hbox.setStretchFactor(b2, 5)
        hbox.setStretchFactor(b3, 8)

        self.setLayout(hbox) 
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
