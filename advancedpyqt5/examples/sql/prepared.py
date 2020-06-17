#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example we work with a prepared
SQL statement.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5 import  QtSql
import sys
      

def check_error(q, db):
    
    ler = q.lastError()

    if ler.isValid():
        
        db.close()
        print(ler.text())
        sys.exit(1)
        

def main():       
        
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    
    if not db.open():
        print("Cannot establish a database connection")
        sys.exit(1)
        
    q = QtSql.QSqlQuery()
    q.prepare("SELECT Name, Price FROM Cars WHERE Id = ?")
    q.bindValue(0, 6)
    q.exec_()
    check_error(q, db)

    q.first()

    name = q.value(0)
    price = q.value(1)
    print(name, price)

    db.close()
    

if __name__ == '__main__':
    
    main()
    