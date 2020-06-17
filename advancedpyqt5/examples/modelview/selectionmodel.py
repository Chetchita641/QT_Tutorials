#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we calculate
the sum of numbers in the QTableView

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QMainWindow, QApplication, 
        QTableView, QAction)
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
import sys
   
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle("Selection")
       
        self.initData()
        self.initUI()
        
        
    def initUI(self):
             
        self.tv = QTableView(self)
        self.tv.setModel(self.model)
        icon = QIcon('sum.png')
        self.nsum = QAction(icon, 'Sum', self)
        self.nsum.setShortcut('Ctrl+Q')
        
        self.nsum.triggered.connect(self.onClicked)
        
        self.toolbar = self.addToolBar('Sum')
        self.toolbar.addAction(self.nsum)

        self.setCentralWidget(self.tv) 
        
    
    def onClicked(self):
        
        nsum = 0
    
        selmod = self.tv.selectionModel()
        selection = selmod.selection()
        
        if not selection.count():
            return
        
        indexes = selection.indexes()
        
        for idx in indexes:
            
            d = idx.data()
            
            if d:
                try:
                    num = int(d)
                except ValueError:
                    num = 0 
            else:
                num = 0
            
            nsum += num
        
        lastIndex = indexes[-1]
        r, c = lastIndex.row(), lastIndex.column()
    
        item = QStandardItem(str((nsum)))
        self.model.setItem(r+1, c, item)
        
                          
    def initData(self):
        
        self.model = QStandardItemModel(15, 15)
 
        
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
