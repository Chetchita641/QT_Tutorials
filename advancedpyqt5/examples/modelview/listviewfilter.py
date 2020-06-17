#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we filter items in 
a QListView using a QSortFilterProxyModel class.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication,  QListView, 
        QVBoxLayout, QLineEdit, QCheckBox, QComboBox, QGridLayout)
from PyQt5.QtCore import (Qt, QStringListModel, QRegExp, 
        QVariant, QSortFilterProxyModel)
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 400, 240)
        self.setWindowTitle("Filtering data")
       
        self.initData()
        self.initUI()
        
        
    def initData(self):
    
        words = ["radar", "robert", "Rome", "rodeo",
            "rust", "ready", "robot", "rampart", "RAM", "ROM"]

        self.model = QStringListModel(words)
        self.filterModel = QSortFilterProxyModel(self)
        self.filterModel.setSourceModel(self.model)
        self.filterModel.setDynamicSortFilter(True)
        
    
    def initUI(self):
    
        grid = QGridLayout()
        grid.setSpacing(10)
        
        self.lv = QListView(self)
        self.lv.setModel(self.filterModel)
        grid.addWidget(self.lv, 0, 0, 2, 2)             
    
        self.filText = QLineEdit(self)
        grid.addWidget(self.filText, 0, 3, Qt.AlignTop)
    
        self.case = QCheckBox("Case sensitive", self)
        grid.addWidget(self.case, 1, 3, Qt.AlignTop)
    
        self.filterCombo = QComboBox(self)
        self.filterCombo.addItem("Regular expression",
            QVariant(QRegExp.RegExp))
        self.filterCombo.addItem("Wildcard", 
            QVariant(QRegExp.Wildcard))
        self.filterCombo.addItem("Fixed string",
            QVariant(QRegExp.FixedString))
        grid.addWidget(self.filterCombo, 2, 0)
        
        self.filterCombo.activated[str].connect(self.filterItems)
        self.filText.textChanged[str].connect(self.filterItems)
        self.case.toggled[bool].connect(self.filterItems)
               
        self.setLayout(grid)       
        
        
    def filterItems(self, value):
        
        idx = self.filterCombo.currentIndex()
        
        syntaxType = self.filterCombo.itemData(idx)
        syntax = QRegExp.PatternSyntax(syntaxType)
        
        if self.case.isChecked():
            case = Qt.CaseSensitive
            
        else:
            case = Qt.CaseInsensitive
        
        regExp = QRegExp(self.filText.text(), case, syntax)
        self.filterModel.setFilterRegExp(regExp)
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
