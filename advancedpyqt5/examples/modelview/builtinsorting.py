#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we sort data in the
QTableView widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QTableView, 
        QPushButton, QHBoxLayout, QVBoxLayout, 
        QCheckBox, QSizePolicy)
from PyQt5.QtCore import Qt, QStringListModel
import  sys
   
FIRST_COLUMN = 0

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Sorting")
       
        self.initData()
        self.initUI()
        

    def initData(self):
    
        names = ["Jack", "Tom", "Lucy", "Bill", "Jane"]      
        self.model = QStringListModel(names)
        

    def initUI(self):
             
        self.tv = QTableView(self)
        self.tv.setModel(self.model)
        self.tv.setSortingEnabled(True)

        sortBtn = QPushButton("Sort", self)
        sortBtn.setSizePolicy(QSizePolicy.Fixed, 
             QSizePolicy.Fixed)
        
        self.sortType = QCheckBox("Ascending", self)
        self.sortType.setSizePolicy(QSizePolicy.Fixed, 
             QSizePolicy.Fixed)
        
        sortBtn.clicked.connect(self.sortItems)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.sortType)
        hbox.addWidget(sortBtn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tv) 
        vbox.addLayout(hbox)
        self.setLayout(vbox)  
        
        
    def sortItems(self):
        
        checked = self.sortType.isChecked()
        
        if checked:
            self.tv.sortByColumn(FIRST_COLUMN, 
                Qt.AscendingOrder)
                
        else:
            self.tv.sortByColumn(FIRST_COLUMN, 
                Qt.DescendingOrder)
            

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
