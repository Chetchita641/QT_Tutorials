#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a basic QListView example.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, 
        QListView, QVBoxLayout)
from PyQt5.QtCore import QStringListModel
import sys
          

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("QListView")
       
        self.initData()
        self.initUI()
        
        
    def initData(self):
        
        names = ["Jack", "Tom", "Lucy", "Bill", "Jane"]      
        self.model = QStringListModel(names)
        
    def initUI(self):
    
        lv = QListView(self)
        lv.setModel(self.model)
        
        layout = QVBoxLayout()
        layout.addWidget(lv) 
        self.setLayout(layout) 
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
