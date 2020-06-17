#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we work with the sizeHint
property.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication      
from PyQt5.QtCore import QSize
import sys 
      

class MyButton(QPushButton):
    
    def __init__(self, text, parent, size):
        super(MyButton, self).__init__(text, parent)
        
        self.size = size
        
    def sizeHint(self):
        return self.size


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 230)
        self.setWindowTitle("Size hints")
       
        self.initUI()
        
        
    def initUI(self):
    
        button1 = QPushButton("Button", self)
        button1.move(20, 50)
        
        button2 = MyButton("Button", self, 
                      QSize(140, 27))
        button2.move(150, 50)
        
        button3 = MyButton("Button", self, 
                      QSize(150, 60))
                      
        button3.move(50, 150)
      

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
