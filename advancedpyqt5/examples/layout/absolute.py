#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we show three images
using absolute positioning.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 280)
        self.setWindowTitle("Absolute")
       
        self.initUI()
        

    def initUI(self):
    
        self.setStyleSheet("background-color: #222222")
        
        bardejov = QPixmap("bardejov.jpg")
        mincol = QPixmap("mincol.jpg")
        rotunda = QPixmap("rotunda.jpg")
        
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        
        label1.setPixmap(bardejov)
        label2.setPixmap(mincol)
        label3.setPixmap(rotunda)
        
        label1.setGeometry(20, 20, 120, 90)
        label2.setGeometry(40, 160, 120, 90)
        label3.setGeometry(170, 50, 120, 90)
        
        
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

