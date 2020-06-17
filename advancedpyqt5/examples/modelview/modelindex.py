#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we work with QModelIndex 
and QTreeView.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QTreeView, 
        QVBoxLayout, QAbstractItemView, QLabel)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
      
      
data = ( ["Jessica Alba", "Pomona", "1981"],   
       ["Angelina Jolie", "New York", "1975"],        
       ["Natalie Portman", "Yerusalem", "1981"],        
       ["Scarlett Jonahsson", "New York", "1984"] )
            

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Actresses")
       
        self.initData()
        self.initUI()
        
    
    def initData(self):
    
        self.model = QStandardItemModel()
        labels = ("Name", "Place", "Born")
        self.model.setHorizontalHeaderLabels(labels)
               
        for i in range(len(data)):
            
            name = QStandardItem(data[i][0])
            place = QStandardItem(data[i][1])
            born = QStandardItem(data[i][2])
            self.model.appendRow((name, place, born))
            
        
    def initUI(self):
             
        tv = QTreeView(self)
        tv.setRootIsDecorated(False)
        tv.setModel(self.model)
        behavior = QAbstractItemView.SelectRows
        tv.setSelectionBehavior(behavior)
        
        self.label = QLabel(self)
        
        layout = QVBoxLayout()
        layout.addWidget(tv) 
        layout.addWidget(self.label)
        self.setLayout(layout) 
        
        tv.clicked.connect(self.onClicked)
            
        
    def onClicked(self, idx):
        
        row = idx.row()
        cols = self.model.columnCount()
        
        data = []
        
        for col in range(cols):
            
            item = self.model.item(row, col)
            data.append(item.text())
                    
        self.label.setText((", ".join(data)))      
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())