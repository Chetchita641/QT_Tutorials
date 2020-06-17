#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This example selects five rows from
a Cars table.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5 import QtSql
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
    q.exec_("SELECT * FROM Cars LIMIT 5")
    check_error(q, db)

    while q.next():
        
        cid = q.value(0)
        name = q.value(1)
        price = q.value(2)
        
        print(cid, name, price)
        
    db.close()    
    

if __name__ == '__main__':
    
    main()
    