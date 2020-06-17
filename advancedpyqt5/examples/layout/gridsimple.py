#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a very simple demonstration of
the QGridLayout manager.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, 
        QApplication, QGridLayout)      
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.move(300, 300)
        self.setWindowTitle("Buttons")
       
        self.initUI()


    def initUI(self):
                
        button1 = QPushButton("Button")
        button2 = QPushButton("Button")
        button3 = QPushButton("Button")
        button4 = QPushButton("Button")
        button5 = QPushButton("Button")
        button6 = QPushButton("Button")

        grid = QGridLayout()
        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button3, 0, 2)
        grid.addWidget(button4, 1, 0)
        grid.addWidget(button5, 1, 1)
        grid.addWidget(button6, 1, 2)
        
        self.setLayout(grid)
        
       
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

