#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

In this example, we set gaps
between the frame widgets.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QGridLayout, 
        QFrame, QApplication)
import sys 


class MyFrame(QFrame):
    
    def __init__(self):        
        super().__init__()
        
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
                
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Spacing")
       
        self.initUI()


    def initUI(self):
                
        frame1 = MyFrame()
        frame2 = MyFrame()
        frame3 = MyFrame()
        frame4 = MyFrame()
        frame5 = MyFrame()
        frame6 = MyFrame()
       
        grid = QGridLayout()
        grid.addWidget(frame1, 0, 0)
        grid.addWidget(frame2, 0, 1)
        grid.addWidget(frame3, 0, 2)
        grid.addWidget(frame4, 1, 0)
        grid.addWidget(frame5, 1, 1)
        grid.addWidget(frame6, 1, 2)
        
        grid.setHorizontalSpacing(3)
        grid.setVerticalSpacing(3)

        self.setLayout(grid)
        
       
app = QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

