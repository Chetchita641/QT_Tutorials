#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we delete
selected items from the scene.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QApplication, QWidget, QFrame,
        QHBoxLayout, QVBoxLayout, QGraphicsItem, QGraphicsView,
        QGraphicsScene, QPushButton )
from PyQt5.QtGui import QPainter
import sys              

class View(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.setRenderHint(QPainter.Antialiasing)
         
        
class Scene(QGraphicsScene):
    
    def __init__(self):
        super().__init__()
        
        self.initScene()
        
        
    def initScene(self):
        
        for i in range(5):
            
            e = self.addEllipse(20*i, 40*i, 50, 50)
            
            flag1 = QGraphicsItem.ItemIsMovable
            flag2 = QGraphicsItem.ItemIsSelectable
            
            e.setFlag(flag1, True)
            e.setFlag(flag2, True)
                  
        
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
                
        self.setGeometry(150, 150, 350, 300)
        self.setWindowTitle("Selection")
        
        self.initUI()        
        
            
    def initUI(self):
    
        hbox = QHBoxLayout()
        
        self.view = View()       
        self.scene = Scene()
        self.view.setScene(self.scene)
        
        hbox.addWidget(self.view)
        
        frame = QFrame()
        
        self.delete = QPushButton("Delete", frame)
        self.delete.setEnabled(False)
        vbox = QVBoxLayout()
        vbox.addWidget(self.delete)
        vbox.addStretch(1)
        
        frame.setLayout(vbox)
        hbox.addWidget(frame)        
        self.setLayout(hbox)
        
        self.delete.clicked.connect(self.onClick)
        self.scene.selectionChanged.connect(self.selChanged)
        
        
    def onClick(self):

        selectedItems = self.scene.selectedItems()
        
        if len(selectedItems) > 0:
            for item in selectedItems:
                self.scene.removeItem(item)
                
                
    def selChanged(self):
    
        selectedItems = self.scene.selectedItems()
        
        if len(selectedItems):
            self.delete.setEnabled(True)
            
        else:
            self.delete.setEnabled(False)

            
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
