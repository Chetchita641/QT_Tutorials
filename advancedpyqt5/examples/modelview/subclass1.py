#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a read-only
QAbstractListModel subclass.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, 
        QListView, QVBoxLayout)
from PyQt5.QtCore import (Qt, QAbstractListModel, 
        QModelIndex, QVariant)
import sys
      

class MyListModel(QAbstractListModel):
    
    def __init__(self, lang):
        super().__init__()
        
        self.lang = lang
        
        
    def data(self, index, role): 
    
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.lang[index.row()])
            
        else: 
            return QVariant()    
        
        
    def rowCount(self, index=QModelIndex()): 
    
        return len(self.lang) 
    
    
    def flags(self, index):
        
        fg1 = Qt.ItemIsEnabled
        fg2 = Qt.ItemIsSelectable 
        
        return fg1 | fg2 
 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle("Subclassing")
       
        self.initData()
        self.initUI()
        
        
    def initData(self):
    
        languages = ("Python", "Ruby", "Java", 
                    "C", "C#", "C++")
        
        self.model = MyListModel(languages)
            
        
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
