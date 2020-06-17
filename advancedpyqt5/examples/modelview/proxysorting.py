#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we sort items in 
a QListView using a QSortFilterProxyModel class.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QListView, 
        QPushButton, QCheckBox)
from PyQt5.QtCore import (Qt, QStringListModel, 
        QSortFilterProxyModel)
import  sys

FIRST_COLUMN = 0

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Sorting")
       
        self.initData()
        self.initUI()
        
    
    def initData(self):
        
        names = ["Jack", "Tom", "Lucy", "Bill", "Jane"]      
        self.model = QStringListModel(names)
        
        self.model = QStringListModel(names)
        self.filterModel = QSortFilterProxyModel(self)
        self.filterModel.setSourceModel(self.model)
    
    
    def initUI(self):
    
        sortB = QPushButton("Sort", self)
        sortB.move(250, 20)
        
        self.sortType = QCheckBox("Ascending", self)
        self.sortType.move(250, 60)

        sortB.clicked.connect(self.sortItems)
        
        self.lv = QListView(self)
        self.lv.setModel(self.filterModel)
        self.lv.setGeometry(20, 20, 200, 150)
        
        
    def sortItems(self):
        
        checked = self.sortType.isChecked()
        
        if checked:
            self.filterModel.sort(FIRST_COLUMN, 
                Qt.AscendingOrder)
                
        else: 
            self.filterModel.sort(FIRST_COLUMN, 
                Qt.DescendingOrder)

        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
