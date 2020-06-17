#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
ZetCode Advanced PyQt5 tutorial 

In this example, we work with radial
gradients.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QRadialGradient
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):        
                
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Radial gradients')        
        self.show()
        
       
    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.drawGradients(painter)
        painter.end()               
        

    def drawGradients(self, painter):    

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        
        gr1 = QRadialGradient(20.0, 20.0, 110.0)
        painter.setBrush(gr1)
        painter.drawEllipse(20.0, 20.0, 100.0, 100.0)

        gr2 = QRadialGradient(190.0, 70.0, 50.0, 190.0, 70.0)
        gr2.setColorAt(0.2, Qt.yellow)
        gr2.setColorAt(0.7, Qt.black)
        painter.setBrush(gr2)
        painter.drawEllipse(140.0, 20.0, 100.0, 100.0)
        
            
app = QApplication([])
ex = Example()
sys.exit(app.exec_())

