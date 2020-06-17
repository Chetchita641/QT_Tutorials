#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we align widgets in
QGridLayout manager.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, 
        QApplication, QGridLayout)   
from PyQt5.QtCore import Qt
import sys 
      
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle("Alignments")
       
        self.initUI()
        
        
    def initUI(self):
    
        button1 = QPushButton("Left")
        button2 = QPushButton("Center")
        button3 = QPushButton("Right")
        button4 = QPushButton("Stretch")

        grid = QGridLayout()
        grid.addWidget(button1, 0, 0, Qt.AlignLeft)
        grid.addWidget(button2, 1, 0, Qt.AlignCenter)
        grid.addWidget(button3, 2, 0, Qt.AlignRight)
        grid.addWidget(button4, 3, 0)

        self.setLayout(grid)
                                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
