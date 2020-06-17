#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

In this example we determine the number of rows
affected by a query.

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
    q.exec_("DELETE FROM Cars WHERE Id IN (1, 2, 3)")
    check_error(q, db)

    print("The query affected {0} rows".format(q.numRowsAffected()))
    db.close()
    

if __name__ == '__main__':
    
    main()
