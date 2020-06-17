#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This example prints the version of
the SQLite database. 

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5 import QtSql
import sys
      
      
def check_error(q, db):
    
    ler = q.lastError()

    if ler.isValid():
        
        print(ler.text())
        db.close()
        
        sys.exit(1)
    

def main():

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(":memory:")
    
    if not db.open():
        print("Cannot establish a database connection")
        sys.exit(1)

    q = QtSql.QSqlQuery()
    q.exec_("SELECT sqlite_version()")
    check_error(q, db)

    q.first()

    print("Database version: {0}".format(q.value(0)))

    db.close()


if __name__ == '__main__':
    
    main()





