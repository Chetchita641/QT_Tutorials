#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a simple Model and View example,
which uses QFileSystemModel and QTreeView classes.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QTreeView, 
        QFileSystemModel, QVBoxLayout)
from PyQt5.QtCore import QDir
import os, sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 400, 350)
        self.setWindowTitle("QFileSystemModel")
       
        self.initUI()
        
        
    def initUI(self):
     
        self.model = QFileSystemModel()
        #print os.path.expanduser('~')
        homedir = QDir.home().path()
        print(homedir)
        #homedir = os.getenv('HOME')
        self.model.setRootPath(homedir)

        tv = QTreeView(self)
        tv.setModel(self.model)
        
        layout = QVBoxLayout()
        layout.addWidget(tv) 
        self.setLayout(layout) 
        

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
