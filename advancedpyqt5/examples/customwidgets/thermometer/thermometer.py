#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a custom 
Thermometer widget.

Original author: Tomasz Ziobrowski
Adopted by: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget,  QApplication, 
        QVBoxLayout, QSlider)   
from PyQt5.QtGui import (QPainter, QPainterPath, QPen, QBrush, 
        QGradient, QLinearGradient, QRadialGradient, QColor)
from PyQt5.QtCore import Qt, QRectF, QPointF
import sys 

OFFSET = 10
SCALE_HEIGHT = 224

class Thermometer(QWidget):
    
    def __init__(self, parent):
        super().__init__()

        self.value = 0
        
    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.initDrawing(painter)
        self.drawTemperature(painter)
        self.drawOutline(painter)
        painter.end()
  

    def initDrawing(self, painter):
    
        self.normal = 25
        self.critical = 75
        self.m_min = 0
        self.m_max = 80

        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2, 0)
        painter.scale(self.height()/300, self.height()/300)
        
        
    def drawOutline(self, painter):

        path = QPainterPath()

        path.moveTo(-7.5, 257)
        path.quadTo(-12.5, 263, -12.5, 267.5)
        path.quadTo(-12.5, 278, 0, 280)
        path.quadTo(12.5, 278, 12.5, 267.5)
        path.moveTo(12.5, 267.5) 
        path.quadTo(12.5, 263, 7.5, 257) 
        
        path.lineTo(7.5, 25)
        path.quadTo(7.5, 12.5, 0, 12.5)
        path.quadTo(-7.5, 12.5, -7.5, 25)
        path.lineTo(-7.5, 257)
        
        p1 = QPointF(-2.0, 0)
        p2 = QPointF(12.5, 0)
        
        linearGrad = QLinearGradient(p1, p2)
        linearGrad.setSpread(QGradient.ReflectSpread)
        linearGrad.setColorAt(1, 
            QColor(0, 150, 255, 170))
        linearGrad.setColorAt(0, 
            QColor(255, 255, 255, 0))

        painter.setBrush(QBrush(linearGrad))
        painter.setPen(Qt.black)
        painter.drawPath(path)
        
        pen = QPen()
        length = 12
                
        for i in range(33):
            
            pen.setWidthF(1.0)
            length = 12
            
            if i % 4:
                length = 8 
                pen.setWidthF(0.8)
                
            if i % 2:
                length = 5
                pen.setWidthF(0.6)
                
            painter.setPen(pen)
            painter.drawLine(-7, 28+i*7, -7+length, 28+i*7)
        
        for i in range(9):    
            
            num = self.m_min + i*(self.m_max-self.m_min)/8
            val = "{0}".format(num)
            fm = painter.fontMetrics()
            size = fm.size(Qt.TextSingleLine, val)
            point = QPointF(OFFSET, 
                        252-i*28+size.width()/4.0)
            painter.drawText(point, val)
    
    
    def drawTemperature(self, painter):

        if self.value >= self.critical:
            color = QColor(255, 0, 0) 
     
        elif self.value >= self.normal:
            color = QColor(0, 200, 0)
        
        else:
            color = QColor(0, 0, 255)
            
        scale = QLinearGradient(0, 0, 5, 0)
        bulb = QRadialGradient(0, 267.0, 10, -5, 262)

        scale.setSpread(QGradient.ReflectSpread)
        bulb.setSpread(QGradient.ReflectSpread)

        color.setHsv(color.hue(), color.saturation(),
                      color.value())
        scale.setColorAt(1, color)
        bulb.setColorAt(1, color)

        color.setHsv(color.hue(), color.saturation()-200, 
            color.value())
        scale.setColorAt(0, color)
        bulb.setColorAt(0, color)

        factor = self.value-self.m_min 
        factor = (factor/self.m_max)-self.m_min

        temp = SCALE_HEIGHT * factor
        height = temp + OFFSET

        painter.setPen(Qt.NoPen)
        painter.setBrush(scale)
        painter.drawRect(-5, 252+OFFSET-height, 10, height)
        painter.setBrush(bulb)
        rect = QRectF(-10, 258, 20, 20)
        painter.drawEllipse(rect)
        

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 100, 250, 350)
        self.setWindowTitle('Thermometer')
        
        self.initUI()
        
        
    def initUI(self):
        
        self.value = 0
        
        vbox = QVBoxLayout()
        
        self.the = Thermometer(self)
        vbox.addWidget(self.the)

        self.slider = QSlider(Qt.Horizontal, self)
        vbox.addWidget(self.slider)
        self.slider.setMaximum(80)
        
        self.slider.valueChanged[int].connect(self.changeVal)

        self.setLayout(vbox)

        
    def changeVal(self):
        
        self.the.value = self.slider.value()
        self.the.repaint()
 

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
