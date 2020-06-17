#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we use a 
new delegate in a QListView.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QListView, 
        QVBoxLayout, QSpinBox, QStyledItemDelegate)
from PyQt5.QtCore import Qt, QVariant, QStringListModel
import sys
      
      
class MyDelegate(QStyledItemDelegate):
    
    def __init__(self):
        super().__init__()

        
    def createEditor(self, parent, option, index):
    
        editor = QSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(100)

        return editor
        

    def setEditorData(self, editor, index):
    
        model = index.model()    
        role = Qt.DisplayRole
        value = model.data(index, role)
        editor.setValue(int(value))

        
    def setModelData(self, editor, model, index):

        value = editor.value()
        model.setData(index, QVariant(value))
        

    def updateEditorGeometry(self, editor, option, index):

        r = option.rect
        r.setHeight(30)
        editor.setGeometry(r)
        

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle("Delegate")
       
        self.initData()
        self.initUI()
        

    def initData(self):
            
        vals = ["0", "1", "2", "3", "4"]
        
        self.model = QStringListModel(vals)
        
        
    def initUI(self):
    
        lv = QListView(self)
        lv.setModel(self.model)
        
        self.de = MyDelegate()
        lv.setItemDelegate(self.de)
        
        layout = QVBoxLayout()
        layout.addWidget(lv) 
        self.setLayout(layout) 
       

app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())