#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we demostrate
how to span widgets in 
QGridLayout manager.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QLineEdit,
        QApplication, QGridLayout)     
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.move(300, 300)
        self.setWindowTitle("Spanning")
       
        self.initUI()


    def initUI(self):
                
        grid = QGridLayout()
        grid.addWidget(QLineEdit(), 0, 0)
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 0, 2)
        grid.addWidget(QLineEdit(), 0, 3)
        
        grid.addWidget(QLineEdit(), 1, 0, 1, 2)
        grid.addWidget(QLineEdit(), 2, 0, 1, 3)
        grid.addWidget(QLineEdit(), 3, 0, 1, 4)

        self.setLayout(grid)
        
       
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

