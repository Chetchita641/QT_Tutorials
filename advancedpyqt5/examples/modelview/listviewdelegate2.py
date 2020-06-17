#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we change the background
color of the selected item and the 
foreground color of all items using 
the QStyledItemDelegate class.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QListView, 
        QVBoxLayout, QStyledItemDelegate, QStyle)
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QStringListModel
import sys

      
class MyDelegate(QStyledItemDelegate):
    
    def __init__(self):
        super().__init__()
        

    def paint(self, painter, option, index):
    
        #super().paint(painter, option, index)          
     
        #painter.save()
               
        painter.setPen(QPen(Qt.NoPen))
        
        if option.state & QStyle.State_Selected:
            brush = QBrush(QColor("#66ff71"))
            painter.setBrush(brush)
            
        else:
            brush = QBrush(Qt.white)
            painter.setBrush(brush)
            
        painter.drawRect(option.rect)

        text = index.data(Qt.DisplayRole)
        
        if text:
            
            painter.setPen(QPen(Qt.blue))
            align = Qt.AlignCenter
            painter.drawText(option.rect, align, text)
            
        #painter.restore()
        

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle("Delegate")
       
        self.initData()
        self.initUI()
        
    
    def initData(self):
            
        names = ["Jack", "Tom", "Lucy", "Bill", "Jane"]          
        self.model = QStringListModel(names)
        
        
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
