#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This example shows column names of data.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5 import QtSql
import sys      
      
      
def check_error(q, db):
    
    ler = q.lastError()

    if ler.isValid():
        print(ler.text()  )
        
    
def main():
    
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")    

    if not db.open():
        print("Cannot establish a database connection")
        sys.exit(1)

    q = QtSql.QSqlQuery()
    q.exec_("SELECT * FROM Cars LIMIT 1")
    check_error(q, db)

    rec = q.record()

    print("Number of columns:", rec.count())

    print("Column names:")
    print(rec.fieldName(0))
    print(rec.fieldName(1))
    print(rec.fieldName(2))

    db.close()    
    
    
if __name__ == '__main__':
    
    main()
    
