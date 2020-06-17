#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this examaple, we zoom 
items on the QGraphicsView.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QSlider,
        QGraphicsView, QGraphicsScene, QVBoxLayout)
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys
            

class View(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 300)
        self.setRenderHint(QPainter.Antialiasing)
       
        self.init()
        
        
    def init(self):

        self.scene = QGraphicsScene()
        
        r1 = self.scene.addRect(150, 40, 100, 100)
        r1.setBrush(QColor(250, 50, 0))
        r1.setPen(QColor(250, 50, 0))
               
        el = self.scene.addEllipse(40, 70, 80, 80)
        el.setBrush(QColor(0, 50, 250))
        el.setPen(QColor(0, 50, 250))
        
        r2 = self.scene.addRect(60, 180, 150, 70)
        r2.setBrush(QColor(0, 250, 50))
        r2.setPen(QColor(0, 250, 50))
        
        self.setScene(self.scene)  


class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

        
    def initUI(self):
        
        vbox = QVBoxLayout()
        
        self.view = View()
        
        slider = QSlider(Qt.Horizontal, self)
        slider.setRange(1, 500)
        slider.setValue(100)
        slider.valueChanged[int].connect(self.onZoom)
        
        vbox.addWidget(self.view)
        vbox.addWidget(slider)
        
        self.setLayout(vbox)
        self.setWindowTitle("Zoom")
        self.setGeometry(150, 150, 300, 300)
        
    
    def onZoom(self, value):
    
        val = value / 100    
        self.view.resetTransform()
        self.view.scale(val, val)
    

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())


