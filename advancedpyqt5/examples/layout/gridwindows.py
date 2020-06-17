#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we create a Windows
window with QGridLayout

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QListView, QPushButton, 
        QApplication, QGridLayout, QLabel)      
from PyQt5.QtCore import Qt
import sys 

class Example(QWidget):
    def __init__(self):
        
        super().__init__()
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Windows")
       
        self.initUI()


    def initUI(self):
        
        windows = QLabel('Windows')
        
        actBtn = QPushButton("Activate")
        clsBtn = QPushButton("Close")
        hlpBtn = QPushButton("Help")
        okBtn = QPushButton("OK")
        
        listView = QListView()

        grid = QGridLayout()

        grid.addWidget(windows, 0, 0)
        grid.addWidget(listView, 1, 0, 2, 2)

        grid.addWidget(actBtn, 1, 4)
        grid.addWidget(clsBtn, 2, 4)

        grid.addWidget(hlpBtn, 4, 0)
        grid.addWidget(okBtn, 4, 4)
        
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(2, 1)
        
        grid.setAlignment(clsBtn, Qt.AlignTop)

        self.setLayout(grid)
        
       
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
