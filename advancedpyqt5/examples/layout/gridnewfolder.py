#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a New folder
window with QGridLayout.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
        QListView, QGridLayout, QApplication)      
import sys 
        
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("New folder")
       
        self.initUI()
        
        
    def initUI(self):
        
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Name: "), 0, 0)
        
        line = QLineEdit()
        grid.addWidget(line, 0, 1, 1, 3)

        grid.addWidget(QListView(), 1, 0, 2, 4)
        
        ok = QPushButton("OK")
        cancel = QPushButton("Cancel")
        
        grid.addWidget(ok, 3, 2)
        grid.addWidget(cancel, 3, 3)

        self.setLayout(grid)
                

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

