#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a basic QTableView example.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QTableView, 
        QVBoxLayout)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
   

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("QTableView")
       
        self.initData()
        self.initUI()
        

    def initData(self):
    
        data = ("blue", "green", "yellow", "red")
        self.model = QStandardItemModel(10, 6)
        
        row = 0
        col = 0
        
        for i in data:
            
            item = QStandardItem(i)
            self.model.setItem(row, col, item)
            row = row + 1
            
            
    def initUI(self):
             
        self.tv = QTableView(self)
        self.tv.setModel(self.model)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tv) 
        self.setLayout(vbox)  
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
