#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we group items.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsScene, 
        QGraphicsView, QGraphicsItemGroup, QGraphicsItem, 
        QHBoxLayout)
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt
import sys
          
            
class MyGroup(QGraphicsItemGroup):
    
    def __init__(self):
        super().__init__()
        
        self.setCursor(Qt.OpenHandCursor)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
    
    def paint(self, painter, option, widget):
    
        painter.setRenderHint(QPainter.Antialiasing)
        
        brush = QBrush(QColor("#333333"))
        pen = QPen(brush, 0.5)
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        
        if self.isSelected():
            boundRect = self.boundingRect()
            painter.drawRect(boundRect)        
            

class Scene(QGraphicsScene):
    
    def __init__(self):
        super().__init__()        
        
        self.initScene()
        
        
    def initScene(self):    
        
        self.r1 = self.addRect(20, 50, 120, 50)
        self.r1.setFlag(QGraphicsItem.ItemIsMovable)
        self.r1.setFlag(QGraphicsItem.ItemIsSelectable, True)
        
        self.r2 = self.addRect(150, 100, 50, 50)
        self.r2.setFlag(QGraphicsItem.ItemIsMovable)
        self.r2.setFlag(QGraphicsItem.ItemIsSelectable, True)

        self.c = self.addEllipse(30, 150, 60, 60)
        self.c.setFlag(QGraphicsItem.ItemIsMovable)
        self.c.setFlag(QGraphicsItem.ItemIsSelectable, True)
        

class View(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 300)
        
        policy = Qt.ScrollBarAlwaysOff
        
        self.setVerticalScrollBarPolicy(policy)
        self.setHorizontalScrollBarPolicy(policy)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.RubberBandDrag)
       
        self.init()
        
        
    def init(self):
          
        self.group = None  
        self.scene = Scene()
        self.setSceneRect(0, 0, 300, 300)    
        self.setScene(self.scene)  
        
        
    def keyPressEvent(self, event): 
           
        key = event.key() 
        
        if key == Qt.Key_U:
            
            if self.group != None and self.group.isSelected():
                
                items = self.group.childItems()
                self.scene.destroyItemGroup(self.group)
                self.group = None
               
                for item in items:
                    item.setSelected(False)
        
        if key == Qt.Key_G:
            
            if self.group:
                return
                
            selectedItems = self.scene.selectedItems()
            
            if len(selectedItems) > 0:
                self.group = MyGroup()
                
                for item in selectedItems:
                    self.group.addToGroup(item)
                
                self.scene.addItem(self.group)

        
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        hbox = QHBoxLayout()
        
        self.view = View()       
        hbox.addWidget(self.view)
        
        self.setLayout(hbox)
        self.setWindowTitle("Grouping")
        self.setGeometry(250, 150, 300, 300)
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())