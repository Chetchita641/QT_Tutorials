#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a custom 
graphics item based on a QGraphicsRectItem.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsScene, 
        QGraphicsView, QGraphicsRectItem, QGraphicsItem)
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtCore import Qt
import sys
      

class Item(QGraphicsRectItem):
    
    def __init__(self,x,y,w,h):
        super().__init__(x, y, w, h)
        
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setCursor(Qt.SizeAllCursor)
        self.setBrush(QColor(250, 100, 0))
        self.setPen(QPen(Qt.NoPen))
        

class Example(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Custom item")
       
        self.init()
        
        
    def init(self):

        self.scene = QGraphicsScene()
        
        self.item = Item(0, 0, 100, 100)
        self.scene.addItem(self.item)
                
        self.setScene(self.scene)        
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())



