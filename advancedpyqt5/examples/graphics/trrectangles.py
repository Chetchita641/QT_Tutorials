#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we draw ten rectangles with
different levels of opacity.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter 
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):        
        
        self.setGeometry(300, 300, 590, 90)
        self.setWindowTitle('Transparent rectangles')
        self.show()
        

    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        self.drawRectangles(painter)
        painter.end()
        
        
    def drawRectangles(self, painter):
 
        for i in range(1, 11):
            
            painter.setOpacity(i*0.1)
            painter.fillRect(50*i, 20, 40, 40, 
                Qt.darkGray)
    

app = QApplication([])
ex = Example()
sys.exit(app.exec_())
