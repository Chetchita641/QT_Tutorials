#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This programs creates a sine wave animation of 
a ball object. 

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsView, 
        QGraphicsPixmapItem, QGraphicsScene, QGraphicsObject)
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import (QObject, QRect, QPoint, QPointF, 
        QPropertyAnimation, pyqtProperty)
import sys, math

TIME = 3000
                              
class Ball(QObject):
    
    def __init__(self):
        super().__init__()
        
        self.pixmap_item = QGraphicsPixmapItem(QPixmap("ball.png"))
        
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)        
    
    
class MyView(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.initView()
        
        
    def initView(self):    
        
        self.ball = Ball()
        self.ball.pos = QPointF(5, 50)
        
        self.animation = QPropertyAnimation(self.ball, b'pos')
        self.animation.setDuration(5000);
        self.animation.setStartValue(QPointF(5, 80))
        
        for i in range(20):
              self.animation.setKeyValueAt(i/20,
                   QPointF(i, math.sin(i))*30)      
        
        self.animation.setEndValue(QPointF(570, 5))
                   
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(120, -50, 250, 150)
        self.scene.addItem(self.ball.pixmap_item)
        self.setScene(self.scene)
        
        self.setWindowTitle("Sine wave animation")
        self.setRenderHint(QPainter.Antialiasing)        
        self.setGeometry(300, 300, 700, 200)
        
        self.animation.start()
                  
app = QApplication([])
view = MyView()
view.show()
sys.exit(app.exec_())
