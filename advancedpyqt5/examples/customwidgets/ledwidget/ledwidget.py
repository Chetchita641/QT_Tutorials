#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a custom Led widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget,  QApplication, QVBoxLayout, 
        QHBoxLayout, QPushButton)
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QSize
import sys 

class Indic:
    
    RED = 0
    GREEN = 1
    ORANGE = 2
    BLACK = 3

    
class Led(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.color = Indic.GREEN
        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
        
        self.colors = ["red.svg", "green.svg",  
            "orange.svg", "black.svg"]
            
       
    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.drawCustomWidget(painter)
        painter.end()


    def drawCustomWidget(self, painter):

        renderer = QSvgRenderer()
        renderer.load(self.colors[self.color])
        renderer.render(painter)   
        

    def setColor(self, newColor):
    
        self.color = newColor
        self.update()
    

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Led widget')
        
        self.initUI()
        
        
    def initUI(self):
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        
        self.led = Led(self)

        hbox.addWidget(self.led)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        hbox = QHBoxLayout()

        self.pb1 = QPushButton("Normal", self)
        self.pb2 = QPushButton("Warning", self)
        self.pb3 = QPushButton("Emergency", self)
        self.pb4 = QPushButton("Off", self)
        
        hbox.addWidget(self.pb1)
        hbox.addWidget(self.pb2)
        hbox.addWidget(self.pb3)
        hbox.addWidget(self.pb4)
                
        vbox.addLayout(hbox)
        
        self.pb1.clicked.connect(self.onClick)
        self.pb2.clicked.connect(self.onClick)
        self.pb3.clicked.connect(self.onClick)
        self.pb4.clicked.connect(self.onClick)
        
        self.setLayout(vbox)
        
       
    def onClick(self):
   
        sender = self.sender()
        text = sender.text()
        
        if text == "Normal":
            self.led.setColor(Indic.GREEN)
        elif text == "Warning":
            self.led.setColor(Indic.ORANGE)
        elif text == "Emergency":
            self.led.setColor(Indic.RED)
        elif text == "Off":
            self.led.setColor(Indic.BLACK)                   
  

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
