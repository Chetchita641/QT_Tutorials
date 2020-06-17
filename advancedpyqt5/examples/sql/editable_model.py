#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This example displays editable data from a SQLite
database in a QTableView widget. 

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5 import QtSql
from PyQt5.QtWidgets import (QMainWindow, QTableView, 
        QApplication, QAbstractItemView)
from PyQt5.QtCore import Qt
import sys      


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 400, 330)
        self.setWindowTitle("Editable model")
       
        self.createConnection()
        self.createModel()
        self.initUI()
        
        self.statusBar().showMessage("Ready")
        

    def onClicked(self, index):
        
        self.statusBar().showMessage(str(index.data()))
        
    
    def createConnection(self):
        
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        
        if not self.db.open():
            
            print("Cannot establish a database connection")
            return False
            
                
    def createModel(self):
    
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("Cars")
        self.model.select()
                
        self.model.setHeaderData(0, Qt.Horizontal, "Id")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Price")
        
        strategy = QtSql.QSqlTableModel.OnFieldChange
        self.model.setEditStrategy(strategy)
        
        
    def initUI(self):
    
        self.view = QTableView()
        self.view.setModel(self.model)
        
        mode = QAbstractItemView.SingleSelection
        self.view.setSelectionMode(mode)
        
        self.view.clicked.connect(self.onClicked)
                
        self.setCentralWidget(self.view) 
        
        
    def closeEvent(self, e):
        
        if (self.db.open()):
            self.db.close()

def main():
    
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


