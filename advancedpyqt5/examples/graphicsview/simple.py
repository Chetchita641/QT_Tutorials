#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a simple example of the
Graphics View framework.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QApplication, QGraphicsView, 
        QGraphicsScene)
import sys

class Example(QGraphicsView):
    
    def __init__(self):        
        super().__init__()
              
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Simple")              
              
        self.init()               
        
        
    def init(self):

        self.scene = QGraphicsScene()        
        self.scene.addText("ZetCode")
        self.setScene(self.scene)        

            
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())






