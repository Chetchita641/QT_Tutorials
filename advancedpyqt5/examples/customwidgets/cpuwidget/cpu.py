#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a custom CPU
widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import QWidget, QSlider, QApplication, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys 


class CPU(QWidget):
    
    def __init__(self, parent):
        super().__init__()

        self.parent = parent


    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.drawCustomWidget(painter)
        painter.end()


    def drawCustomWidget(self, painter):

        w = self.width()
        h = self.height()
        
        painter.scale(w/100, h/150)
        painter.setPen(Qt.NoPen)
        painter.fillRect(0, 0, w, h, Qt.black)

        value = self.parent.getValue()
        pos = value / 5
        
        for i in range(1, 21):
            
            if i > pos:
                painter.setBrush(QColor('#075100'))
                painter.drawRect(19, 120 - i*5+1, 30, 4)
                painter.drawRect(50, 120 - i*5+1, 30, 4)
                
            else:
                painter.setBrush(QColor('#36ff27'))
                painter.drawRect(19, 120 - i*5+1, 30, 4)
                painter.drawRect(50, 120 - i*5+1, 30, 4)
                


class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle('CPU Widget')
        
        self.initUI()
        
        
    def initUI(self):
        
        vbox = QVBoxLayout()

        self.value = 0
        
        self.cpu = CPU(self)
        vbox.addWidget(self.cpu)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(100)
        vbox.addWidget(self.slider)

        self.slider.valueChanged[int].connect(self.changeVal)
       
        self.setLayout(vbox)
       
       
    def changeVal(self):
        
        self.value = self.slider.value()
        self.cpu.repaint()
        
        
    def getValue(self):
        
        return self.value
  

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
