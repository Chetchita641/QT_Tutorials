#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we have an arrow
which always points to the mouse
pointer.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsScene, 
        QGraphicsView, QGraphicsPixmapItem, QHBoxLayout)
from PyQt5.QtGui import QPainter, QPixmap, QTransform
from PyQt5.QtCore import Qt
import sys, math
      

class Arrow(QGraphicsPixmapItem):

    def __init__(self):
        super().__init__()
        
        self.setPixmap(QPixmap('arrow.png'))
        

class View(QGraphicsView):
    
    def __init__(self):
        super(View, self).__init__()
        
        self.setMouseTracking(True)
        
        self.setRenderHint(QPainter.Antialiasing)
        
        policy = Qt.ScrollBarAlwaysOff
        self.setVerticalScrollBarPolicy(policy)
        self.setHorizontalScrollBarPolicy(policy)
        
        self.initScene()
        
        
    def initScene(self):

        self.scene = QGraphicsScene()
        
        self.arrow = Arrow()
        self.scene.addItem(self.arrow)
                
        self.setScene(self.scene)        
        
        
    def mouseMoveEvent(self, event):
        
        s_coords = self.sceneCoordinates(event)
        theta_deg = self.calculateAngle(s_coords)   
        
        self.doTransform(theta_deg, s_coords[2], s_coords[3])
        
      
    def sceneCoordinates(self, event):
    
        point = event.pos()
    
        sMousePt = self.mapToScene(point.x(), point.y())
        
        s_mouse_x = sMousePt.x()
        s_mouse_y = sMousePt.y()

        arrowCenterPt = self.arrow.boundingRect().center()
        arrow_x = arrowCenterPt.x()
        arrow_y = arrowCenterPt.y()
        
        sArrowPt = self.arrow.mapToScene(arrow_x, arrow_y)

        s_arrow_x = sArrowPt.x()
        s_arrow_y = sArrowPt.y() 
        
        return (s_mouse_x, s_mouse_y, arrow_x, arrow_y, 
            s_arrow_x, s_arrow_y)
        
        
    def calculateAngle(self, coords):
        
        s_mouse_x, s_mouse_y = coords[0], coords[1] 
        s_arrow_x, s_arrow_y = coords[3], coords[4]
        
        a = abs(s_mouse_x - s_arrow_x)
        b = abs(s_mouse_y - s_arrow_y)
        
        if a == 0 and b == 0:
            return
        elif a == 0 and s_mouse_y < s_arrow_y:
            theta_deg = 270
        elif a == 0 and s_mouse_y > s_arrow_y: 
            theta_deg = 90
        else: 
            theta_rad = math.atan(b / a)
            theta_deg = math.degrees(theta_rad)
            
            if (s_mouse_x < s_arrow_x and \
                s_mouse_y > s_arrow_y):
                theta_deg = 180 - theta_deg
            
            elif (s_mouse_x < s_arrow_x and \
                s_mouse_y < s_arrow_y):
                theta_deg = 180 + theta_deg
                
            elif (s_mouse_x > s_arrow_x and \
                s_mouse_y < s_arrow_y):
                theta_deg = 360 - theta_deg      
                
        return theta_deg
        
        
    def doTransform(self, theta_deg, arrow_x, arrow_y):
    
        transform = QTransform()
        transform.translate(arrow_x, arrow_y)
        transform.rotate(theta_deg)
        transform.translate(-arrow_x, -arrow_y)
        
        self.arrow.setTransform(transform)
        

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        hbox = QHBoxLayout()
        
        self.view = View()       
        hbox.addWidget(self.view)                
        
        self.setLayout(hbox)
        self.setWindowTitle("Arrow")
        self.setGeometry(250, 150, 390, 390)        
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

