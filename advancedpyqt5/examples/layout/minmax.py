#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we demonstrate the maximum and
minumim size.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QTextEdit, 
        QApplication, QHBoxLayout)      
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.move(300, 300)
        self.setWindowTitle("Minimum and maximum size")
       
        self.initUI()
        
        
    def initUI(self):
    
        te = QTextEdit()
        te.setMinimumSize(15, 15)
        te.setMaximumSize(350, 350)
        
        layout = QHBoxLayout()
        layout.addWidget(te) 
        self.setLayout(layout) 
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
